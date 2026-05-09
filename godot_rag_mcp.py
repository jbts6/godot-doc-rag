#!/usr/bin/env python3
"""
Godot 文档 RAG — MCP Server
让 Claude 通过 MCP 协议检索本地 Godot 文档。

启动方式:
    python godot_rag_mcp.py          # stdio 模式
    python godot_rag_mcp.py --dev    # 带 web inspector

依赖:
    pip install fastmcp chromadb sentence-transformers
"""

import sys
import chromadb
from fastmcp import FastMCP
from sentence_transformers import SentenceTransformer

# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"
EMBED_MODEL = "all-MiniLM-L6-v2"

# ════════════════════════════════════════════════════════════════════════════════════

# instructions 精简到一句话
mcp = FastMCP(
    "Godot Docs RAG",
    instructions="检索本地 Godot 文档。回答 Godot 问题前先调 godot_search。",
)

_collection = None
_model = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model


def get_collection():
    global _collection
    if _collection is None:
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        _collection = client.get_collection(name=COLLECTION_NAME)
    return _collection


def _fmt_heading(meta: dict) -> str:
    parts = []
    for key in ("Header 1", "Header 2", "Header 3", "Header 4"):
        if key in meta and meta[key]:
            parts.append(meta[key])
    return " > ".join(parts)


# ═══════════════════════════════════════════════════════════════
#  工具
# ═══════════════════════════════════════════════════════════════

# description 尽量短，省 token
@mcp.tool()
def godot_search(query: str, top_k: int = 5) -> str:
    """
    Search Godot engine docs by keyword or question. Returns relevant doc snippets with source and section info.

    Args:
        query: search query (English)
        top_k: number of results (default 5)
    """
    model = get_model()
    collection = get_collection()
    embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=embedding,
        n_results=min(top_k, 20),
        include=["documents", "metadatas", "distances"],
    )

    if not results["ids"][0]:
        return "No matching docs found."

    parts = []
    for i in range(len(results["ids"][0])):
        doc = results["documents"][0][i]
        meta = results["metadatas"][0][i]
        dist = results["distances"][0][i]

        source = meta.get("source", "")
        heading = _fmt_heading(meta)
        relevance = round(1 - dist, 3)

        block = f"### [{i+1}] (relevance: {relevance})\n"
        block += f"Source: `{source}`"
        if heading:
            block += f" | Section: {heading}"
        block += f"\n\n{doc}"
        parts.append(block)

    return "\n\n---\n\n".join(parts)


@mcp.tool()
def godot_search_in_file(query: str, source_pattern: str, top_k: int = 5) -> str:
    """
    Search Godot docs within files matching a path pattern (e.g. "gdscript", "physics/rigid_body").

    Args:
        query: search query (English)
        source_pattern: keyword to filter file paths
        top_k: number of results (default 5)
    """
    model = get_model()
    collection = get_collection()
    embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=embedding,
        n_results=50,
        include=["documents", "metadatas", "distances"],
    )

    filtered = []
    for i in range(len(results["ids"][0])):
        source = results["metadatas"][0][i].get("source", "")
        if source_pattern.lower() in source.lower():
            filtered.append({
                "doc": results["documents"][0][i],
                "meta": results["metadatas"][0][i],
                "dist": results["distances"][0][i],
            })
            if len(filtered) >= top_k:
                break

    if not filtered:
        return f"No docs found matching '{source_pattern}'."

    parts = []
    for i, item in enumerate(filtered, 1):
        relevance = round(1 - item["dist"], 3)
        heading = _fmt_heading(item["meta"])
        block = f"### [{i}] (relevance: {relevance})\n"
        block += f"Source: `{item['meta'].get('source', '')}`"
        if heading:
            block += f" | Section: {heading}"
        block += f"\n\n{item['doc']}"
        parts.append(block)

    return "\n\n---\n\n".join(parts)


# ═══════════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    mcp.run()
