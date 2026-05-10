#!/usr/bin/env python3
"""
将 godot-markdown/ 下的 .md 文件分块并向量化存入 ChromaDB，同时构建 BM25 索引。

优化点:
1. Markdown-aware 分块（保标题/代码块边界）
2. all-mpnet-base-v2 英文强模型
3. BM25 索引一并构建
4. 多进程分块 + 大 batch 编码

依赖:
    uv pip install langchain-text-splitters chromadb sentence-transformers rank-bm25

用法:
    uv run python rag_index.py
"""

import sys
import re
import time
import hashlib
import pickle
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor

import chromadb
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
    Language,
)


# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

MD_ROOT = "godot-markdown"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"
BM25_PATH = "bm25_index.pkl"

EMBED_MODEL = "sentence-transformers/all-mpnet-base-v2"

# 分块参数
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
MIN_CHUNK_CHARS = 60
MIN_ALPHA_RATIO = 0.3

# 性能参数
SPLIT_WORKERS = 8
EMBED_BATCH = 512
DB_WRITE_BATCH = 5000

# ════════════════════════════════════════════════════════════════════════════════════


HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
]


def english_tokenize(text: str) -> list[str]:
    """英文分词：保留下划线和点号（move_and_slide、CharacterBody2D）"""
    return re.findall(r"[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*", text.lower())


def is_low_quality(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if len(stripped) < MIN_CHUNK_CHARS:
        return True
    alpha_chars = sum(1 for c in stripped if c.isalpha())
    if alpha_chars / len(stripped) < MIN_ALPHA_RATIO:
        return True
    lines = [l.strip() for l in stripped.split("\n") if l.strip()]
    link_lines = sum(1 for l in lines if l.startswith("[") and "](" in l)
    if len(lines) > 3 and link_lines / len(lines) > 0.7:
        return True
    return False


# ═══════════════════════════════════════════════════════════════
#  分块函数（可在子进程中调用）
# ═══════════════════════════════════════════════════════════════

def split_one_file(args: tuple) -> list[dict]:
    """处理单个文件，返回 list[dict]（可被 pickle 序列化，支持多进程）。"""
    file_str, md_root_str = args
    file_path = Path(file_str)
    md_root = Path(md_root_str)

    text = file_path.read_text(encoding="utf-8")
    rel_path = str(file_path.relative_to(md_root))

    if not text.strip():
        return []

    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False,
    )

    # Markdown-aware 分块：优先在标题、代码块、列表项边界断开
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.MARKDOWN,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    md_docs = md_splitter.split_text(text)
    splits = text_splitter.split_documents(md_docs)

    results = []
    for doc in splits:
        content = doc.page_content.strip()
        if is_low_quality(content):
            continue
        meta = dict(doc.metadata)
        meta["source"] = rel_path
        results.append({"content": content, "metadata": meta})

    return results


def build_chunks(md_root: Path) -> list[dict]:
    md_files = sorted(md_root.rglob("*.md"))
    total_files = len(md_files)
    print(f"扫描到 {total_files} 个 .md 文件")

    tasks = [(str(f), str(md_root)) for f in md_files]
    all_chunks = []

    t0 = time.time()

    if SPLIT_WORKERS <= 1:
        for i, task in enumerate(tasks):
            chunks = split_one_file(task)
            all_chunks.extend(chunks)
            if (i + 1) % 100 == 0:
                print(f"  分块进度: {i + 1}/{total_files}")
    else:
        with ProcessPoolExecutor(max_workers=SPLIT_WORKERS) as executor:
            results = executor.map(split_one_file, tasks, chunksize=8)
            for i, chunks in enumerate(results):
                all_chunks.extend(chunks)
                if (i + 1) % 100 == 0:
                    print(f"  分块进度: {i + 1}/{total_files}")

    elapsed = time.time() - t0
    print(f"分块完成: {len(all_chunks)} 个 chunk, 耗时 {elapsed:.1f}s")

    if all_chunks:
        sizes = [len(c["content"]) for c in all_chunks]
        avg = sum(sizes) // len(sizes)
        print(f"  平均: {avg} 字符, 最短: {min(sizes)}, 最长: {max(sizes)}")

    return all_chunks


# ═══════════════════════════════════════════════════════════════
#  辅助函数
# ═══════════════════════════════════════════════════════════════

def make_id(source: str, heading: str, index: int) -> str:
    raw = f"{source}::{heading}::{index}"
    return hashlib.md5(raw.encode()).hexdigest()


def heading_path(meta: dict) -> str:
    parts = []
    for key in ("Header 1", "Header 2", "Header 3", "Header 4"):
        if key in meta and meta[key]:
            parts.append(meta[key])
    return " > ".join(parts)


def build_full_text(heading: str, content: str) -> str:
    """拼接 heading 前缀，与向量检索保持一致"""
    return (heading + "\n" + content) if heading else content


# ═══════════════════════════════════════════════════════════════
#  向量化 + ChromaDB 存储
# ═══════════════════════════════════════════════════════════════

def index_chunks(chunks: list[dict]):
    print(f"\n加载 embedding 模型: {EMBED_MODEL}")
    model = SentenceTransformer(EMBED_MODEL)

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    try:
        client.delete_collection(COLLECTION_NAME)
        print(f"已删除旧集合: {COLLECTION_NAME}")
    except Exception:
        pass

    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    total = len(chunks)
    t0 = time.time()

    # ── 阶段 1: 批量编码 ──
    print(f"\n开始 embedding 编码 (batch_size={EMBED_BATCH})...")

    all_embeddings = []
    all_texts = []  # heading + content，用于 BM25 索引

    for i in range(0, total, EMBED_BATCH):
        batch = chunks[i : i + EMBED_BATCH]
        texts = []
        for c in batch:
            h = heading_path(c["metadata"])
            texts.append(build_full_text(h, c["content"]))
        all_texts.extend(texts)

        emb = model.encode(
            texts,
            batch_size=EMBED_BATCH,
            show_progress_bar=False,
            normalize_embeddings=True,
        )
        all_embeddings.extend(emb.tolist())

        done = min(i + EMBED_BATCH, total)
        if done % 2048 == 0 or done == total:
            print(f"  编码进度: {done}/{total}")

    t_embed = time.time() - t0
    print(f"编码完成: {t_embed:.1f}s")

    # ── 阶段 2: 批量写入 ChromaDB ──
    print(f"\n写入 ChromaDB (batch_size={DB_WRITE_BATCH})...")
    t1 = time.time()

    ids_all = []
    docs_all = []
    metas_all = []

    for i, c in enumerate(chunks):
        h = heading_path(c["metadata"])
        ids_all.append(make_id(c["metadata"]["source"], h, i))
        docs_all.append(c["content"])
        metas_all.append(c["metadata"])

    for start in range(0, total, DB_WRITE_BATCH):
        end = min(start + DB_WRITE_BATCH, total)
        collection.add(
            ids=ids_all[start:end],
            embeddings=all_embeddings[start:end],
            documents=docs_all[start:end],
            metadatas=metas_all[start:end],
        )
        print(f"  写入进度: {end}/{total}")

    t_write = time.time() - t1
    t_total = time.time() - t0

    print(f"\n{'═' * 50}")
    print(f"  完成!")
    print(f"  集合:     {COLLECTION_NAME}")
    print(f"  记录数:   {collection.count()}")
    print(f"  编码耗时: {t_embed:.1f}s")
    print(f"  写入耗时: {t_write:.1f}s")
    print(f"  总耗时:   {t_total:.1f}s")
    print(f"  ChromaDB: {CHROMA_DIR}")
    print(f"{'═' * 50}")

    return all_texts


# ═══════════════════════════════════════════════════════════════
#  BM25 索引构建
# ═══════════════════════════════════════════════════════════════

def build_bm25_index(texts: list[str], metadatas: list[dict]):
    """用英文分词构建 BM25 索引并持久化"""
    from rank_bm25 import BM25Okapi

    print(f"\n构建 BM25 索引 ({len(texts)} 条)...")
    t0 = time.time()

    tokenized_corpus = [english_tokenize(t) for t in texts]
    bm25 = BM25Okapi(tokenized_corpus)

    with open(BM25_PATH, "wb") as f:
        pickle.dump({
            "bm25": bm25,
            "texts": texts,
            "metadatas": metadatas,
        }, f)

    elapsed = time.time() - t0
    print(f"BM25 索引已保存: {BM25_PATH} ({elapsed:.1f}s)")


# ═══════════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════════

def main():
    md_root = Path(MD_ROOT).resolve()
    if not md_root.is_dir():
        print(f"错误: 目录不存在 → {md_root}", file=sys.stderr)
        sys.exit(1)

    chunks = build_chunks(md_root)
    if not chunks:
        print("没有分块，检查路径。")
        sys.exit(1)

    print("\n── 分块示例 ──")
    for c in chunks[:3]:
        print(f"  来源: {c['metadata'].get('source', '')}")
        print(f"  标题: {heading_path(c['metadata'])}")
        print(f"  长度: {len(c['content'])}")
        print(f"  预览: {c['content'][:120]}...")
        print()

    # 构建向量索引，同时收集 heading+content 文本
    all_texts = index_chunks(chunks)

    # 构建 BM25 索引
    all_metadatas = [c["metadata"] for c in chunks]
    build_bm25_index(all_texts, all_metadatas)


if __name__ == "__main__":
    main()
