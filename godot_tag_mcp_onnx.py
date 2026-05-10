#!/usr/bin/env python3
"""
Godot 文档 RAG — MCP Server (Mac / 无 torch 版)

原理: 用 ONNX Runtime 做 embedding 推理，完全不依赖 PyTorch。
建索引在 Windows 上完成，Mac 只负责查询。

从 Windows 复制到 Mac 的文件:
  - chroma_db/         向量数据库
  - bm25_index.pkl     BM25 索引
  - onnx_model/        ONNX 模型 (export_onnx.py 生成)

Mac 安装:
  uv pip install fastmcp chromadb rank-bm25 numpy onnxruntime transformers

启动:
  uv run python godot_tag_mcp_onnx.py
"""

import re
import pickle
import numpy as np
import chromadb
import onnxruntime as ort
from transformers import AutoTokenizer
from fastmcp import FastMCP


# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"
BM25_PATH = "bm25_index.pkl"
ONNX_MODEL_DIR = "onnx_model"

VECTOR_TOP_K = 20
BM25_TOP_K = 20
RRF_K = 60
FUSION_TOP_K = 15
FINAL_TOP_N_DEFAULT = 5

# ════════════════════════════════════════════════════════════════════════════════════

mcp = FastMCP(
    "Godot Docs RAG",
    instructions=(
        "Search local Godot engine docs using hybrid retrieval (vector + BM25). "
        "Always call godot_search before answering Godot questions. "
        "Reply in Chinese, keep code and technical terms in English."
    ),
)

# ── 全局单例（延迟加载，首次调用时才初始化）──

_tokenizer = None
_onnx_session = None
_input_names = None
_bm25_data = None
_collection = None


# ═══════════════════════════════════════════════════════════════
#  工具函数
# ═══════════════════════════════════════════════════════════════

def english_tokenize(text: str) -> list[str]:
    """英文分词，保留下划线和点号"""
    return re.findall(r"[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*", text.lower())


def get_tokenizer():
    global _tokenizer
    if _tokenizer is None:
        _tokenizer = AutoTokenizer.from_pretrained(ONNX_MODEL_DIR)
    return _tokenizer


def get_onnx_session():
    global _onnx_session, _input_names
    if _onnx_session is None:
        _onnx_session = ort.InferenceSession(
            f"{ONNX_MODEL_DIR}/model.onnx",
            providers=["CPUExecutionProvider"],
        )
        _input_names = {inp.name for inp in _onnx_session.get_inputs()}
    return _onnx_session


def encode_texts(texts: list[str]) -> list[list[float]]:
    """ONNX 推理生成 embedding，不依赖 torch"""
    tokenizer = get_tokenizer()
    session = get_onnx_session()

    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="np")

    # 只传 ONNX 模型实际接受的输入
    ort_inputs = {k: v for k, v in inputs.items() if k in _input_names}
    outputs = session.run(None, ort_inputs)

    # Mean pooling
    hidden = outputs[0]                          # (batch, seq_len, hidden)
    mask = inputs["attention_mask"][..., None]    # (batch, seq_len, 1)
    pooled = (hidden * mask).sum(axis=1) / mask.sum(axis=1)

    # L2 归一化（建索引时 normalize_embeddings=True，查询时保持一致）
    norms = np.linalg.norm(pooled, axis=1, keepdims=True)
    normalized = pooled / norms

    return normalized.tolist()


def get_bm25_data() -> dict:
    global _bm25_data
    if _bm25_data is None:
        with open(BM25_PATH, "rb") as f:
            _bm25_data = pickle.load(f)
    return _bm25_data


def get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        _collection = client.get_collection(name=COLLECTION_NAME)
    return _collection


# ═══════════════════════════════════════════════════════════════
#  检索核心
# ═══════════════════════════════════════════════════════════════

def _vector_search(query: str, top_k: int) -> list[dict]:
    collection = get_collection()
    embedding = encode_texts([query])

    results = collection.query(
        query_embeddings=embedding,
        n_results=min(top_k, 50),
        include=["documents", "metadatas", "distances"],
    )

    items = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        items.append({"text": doc, "score": 1.0 - dist, "metadata": meta})
    return items


def _bm25_search(query: str, top_k: int) -> list[dict]:
    data = get_bm25_data()
    tokens = english_tokenize(query)
    scores = data["bm25"].get_scores(tokens)

    top_indices = np.argsort(scores)[::-1][:top_k]
    items = []
    for idx in top_indices:
        if scores[idx] <= 0:
            break
        items.append({
            "text": data["texts"][idx],
            "score": float(scores[idx]),
            "metadata": data["metadatas"][idx],
        })
    return items


def _rrf_fusion(vector_results: list[dict], bm25_results: list[dict]) -> list[dict]:
    """Reciprocal Rank Fusion"""
    score_map: dict[str, float] = {}
    meta_map: dict[str, dict] = {}
    source_map: dict[str, str] = {}

    for rank, item in enumerate(vector_results):
        t = item["text"]
        score_map[t] = score_map.get(t, 0.0) + 1.0 / (RRF_K + rank + 1)
        meta_map[t] = item["metadata"]
        source_map[t] = source_map.get(t, "") + "V"

    for rank, item in enumerate(bm25_results):
        t = item["text"]
        score_map[t] = score_map.get(t, 0.0) + 1.0 / (RRF_K + rank + 1)
        if t not in meta_map:
            meta_map[t] = item["metadata"]
        source_map[t] = source_map.get(t, "") + "B"

    sorted_texts = sorted(score_map.keys(), key=lambda t: -score_map[t])
    return [
        {"text": t, "score": score_map[t], "metadata": meta_map[t], "source": source_map[t]}
        for t in sorted_texts
    ]


def hybrid_search(
    query: str,
    top_k: int = FINAL_TOP_N_DEFAULT,
    source_filter: str | None = None,
) -> list[dict]:
    """向量 + BM25 → RRF 融合"""
    vector_results = _vector_search(query, VECTOR_TOP_K)
    bm25_results = _bm25_search(query, BM25_TOP_K)
    fused = _rrf_fusion(vector_results, bm25_results)

    if source_filter:
        fused = [
            item for item in fused
            if source_filter.lower() in item["metadata"].get("source", "").lower()
        ]

    return fused[:top_k]


# ═══════════════════════════════════════════════════════════════
#  格式化输出
# ═══════════════════════════════════════════════════════════════

def _fmt_heading(meta: dict) -> str:
    parts = []
    for key in ("Header 1", "Header 2", "Header 3", "Header 4"):
        if key in meta and meta[key]:
            parts.append(meta[key])
    return " > ".join(parts)


def _format_results(results: list[dict]) -> str:
    if not results:
        return "No matching docs found."

    parts = []
    for i, item in enumerate(results, 1):
        meta = item["metadata"]
        source = meta.get("source", "")
        heading = _fmt_heading(meta)
        rrf_score = round(item.get("score", 0), 5)
        hit = item.get("source", "")

        block = f"### [{i}] (rrf: {rrf_score}, hit: {hit})\n"
        block += f"Source: `{source}`"
        if heading:
            block += f" | Section: {heading}"
        block += f"\n\n{item['text']}"
        parts.append(block)

    return "\n\n---\n\n".join(parts)


# ═══════════════════════════════════════════════════════════════
#  MCP 工具
# ═══════════════════════════════════════════════════════════════

@mcp.tool()
def godot_search(query: str, top_k: int = 5) -> str:
    """
    Search Godot engine docs by keyword or question.
    Uses hybrid retrieval (vector + BM25) for best results.

    Args:
        query: search query (English recommended for best results)
        top_k: number of results to return (default 5)
    """
    results = hybrid_search(query, top_k=min(top_k, 20))
    return _format_results(results)


@mcp.tool()
def godot_search_in_file(query: str, source_pattern: str, top_k: int = 5) -> str:
    """
    Search Godot docs within files matching a path pattern.
    Useful for narrowing results to a specific topic area.

    Args:
        query: search query (English recommended)
        source_pattern: keyword to filter file paths (e.g. "gdscript", "physics/rigid_body")
        top_k: number of results to return (default 5)
    """
    results = hybrid_search(
        query,
        top_k=min(top_k, 20),
        source_filter=source_pattern,
    )
    return _format_results(results)


# ═══════════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    mcp.run()
