#!/usr/bin/env python3
"""
Godot 文档 RAG — MCP Server（混合检索 + Reranking）

启动:
    uv run python godot_rag_mcp.py          # stdio
    uv run python godot_rag_mcp.py --dev    # web inspector

依赖:
    uv pip install fastmcp chromadb sentence-transformers FlagEmbedding rank-bm25
"""

import re
import pickle
import numpy as np
import chromadb
from fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
from FlagEmbedding import FlagReranker

# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"
BM25_PATH = "bm25_index.pkl"

EMBED_MODEL = "sentence-transformers/all-mpnet-base-v2"
RERANK_MODEL = "mixedbread-ai/mxbai-rerank-large-v1"

VECTOR_TOP_K = 20
BM25_TOP_K = 20
RRF_K = 60
FUSION_TOP_K = 15
FINAL_TOP_N_DEFAULT = 5

# ════════════════════════════════════════════════════════════════════════════════════

mcp = FastMCP(
    "Godot Docs RAG",
    instructions=(
        "Search local Godot engine docs using hybrid retrieval (vector + BM25 + reranking). "
        "Always call godot_search before answering Godot questions. "
        "Reply in Chinese, keep code and technical terms in English."
    ),
)

# ── 全局单例（延迟加载）──

_model = None
_reranker = None
_bm25_data = None
_collection = None


def english_tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*", text.lower())


def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def get_reranker() -> FlagReranker:
    global _reranker
    if _reranker is None:
        _reranker = FlagReranker(model_name_or_path=RERANK_MODEL, use_fp16=True)
    return _reranker


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
    model = get_model()
    collection = get_collection()
    embedding = model.encode([query], normalize_embeddings=True).tolist()

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


def _rerank(query: str, candidates: list[dict], top_n: int) -> list[dict]:
    if not candidates:
        return []
    reranker = get_reranker()
    pairs = [[query, item["text"]] for item in candidates]
    scores = reranker.compute_score(pairs, normalize=True)
    if isinstance(scores, float):
        scores = [scores]
    for item, score in zip(candidates, scores):
        item["rerank_score"] = score
    candidates.sort(key=lambda x: -x["rerank_score"])
    return candidates[:top_n]


def hybrid_search(
    query: str,
    top_k: int = FINAL_TOP_N_DEFAULT,
    source_filter: str | None = None,
) -> list[dict]:
    """两阶段检索: 多路召回 → RRF → Reranker"""
    vector_results = _vector_search(query, VECTOR_TOP_K)
    bm25_results = _bm25_search(query, BM25_TOP_K)
    fused = _rrf_fusion(vector_results, bm25_results)

    if source_filter:
        fused = [
            item for item in fused
            if source_filter.lower() in item["metadata"].get("source", "").lower()
        ]
    fused = fused[:FUSION_TOP_K]

    return _rerank(query, fused, top_k)


# ═══════════════════════════════════════════════════════════════
#  格式化
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
        rerank_score = round(item.get("rerank_score", 0), 3)
        hit_source = item.get("source", "")

        block = f"### [{i}] (rerank: {rerank_score}, hit: {hit_source})\n"
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
    Uses hybrid retrieval (vector + BM25) with reranking for best results.

    Args:
        query: search query (English recommended for best results)
        top_k: number of results to return (default 5)
    """
    results = hybrid_search(query, top_k=min(top_k, 10))
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
        top_k=min(top_k, 10),
        source_filter=source_pattern,
    )
    return _format_results(results)


# ═══════════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    mcp.run()
