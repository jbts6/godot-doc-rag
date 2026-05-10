#!/usr/bin/env python3
"""
混合检索 + Reranking 查询接口（命令行测试用）
与 rag_index.py 配合使用。

依赖:
    uv pip install chromadb sentence-transformers FlagEmbedding rank-bm25
"""

import re
import time
import pickle
import numpy as np
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer
from FlagEmbedding import FlagReranker


# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"
BM25_PATH = "bm25_index.pkl"

EMBED_MODEL = "sentence-transformers/all-mpnet-base-v2"
RERANK_MODEL = "mixedbread-ai/mxbai-rerank-large-v1"

# 检索参数
VECTOR_TOP_K = 20
BM25_TOP_K = 20
RRF_K = 60
FUSION_TOP_K = 15
FINAL_TOP_N = 5

# ════════════════════════════════════════════════════════════════════════════════════


def english_tokenize(text: str) -> list[str]:
    """英文分词：保留下划线和点号（move_and_slide、CharacterBody2D）"""
    return re.findall(r"[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*", text.lower())


class HybridRetriever:
    """混合检索器：向量 + BM25 + RRF + Reranking"""

    def __init__(self):
        print("初始化 HybridRetriever...")

        # Embedding
        print(f"  加载 Embedding: {EMBED_MODEL}")
        self.embed_model = SentenceTransformer(EMBED_MODEL)

        # ChromaDB
        client = chromadb.PersistentClient(path=CHROMA_DIR)
        self.collection = client.get_collection(COLLECTION_NAME)
        print(f"  向量库: {self.collection.count()} 条")

        # BM25
        with open(BM25_PATH, "rb") as f:
            data = pickle.load(f)
        self.bm25 = data["bm25"]
        self.bm25_texts = data["texts"]
        self.bm25_metadatas = data["metadatas"]
        print(f"  BM25: {len(self.bm25_texts)} 条")

        # Reranker
        print(f"  加载 Reranker: {RERANK_MODEL}")
        self.reranker = FlagReranker(
            model_name_or_path=RERANK_MODEL,
            use_fp16=True,
        )

        print("初始化完成\n")

    # ──────────── 向量检索 ────────────
    def vector_search(self, query: str, top_k: int) -> list[dict]:
        query_emb = self.embed_model.encode(
            [query], normalize_embeddings=True
        ).tolist()

        results = self.collection.query(
            query_embeddings=query_emb,
            n_results=top_k,
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

    # ──────────── BM25 检索 ────────────
    def bm25_search(self, query: str, top_k: int) -> list[dict]:
        tokens = english_tokenize(query)
        scores = self.bm25.get_scores(tokens)

        top_indices = np.argsort(scores)[::-1][:top_k]
        items = []
        for idx in top_indices:
            if scores[idx] <= 0:
                break
            items.append({
                "text": self.bm25_texts[idx],
                "score": float(scores[idx]),
                "metadata": self.bm25_metadatas[idx],
            })
        return items

    # ──────────── RRF 融合 ────────────
    @staticmethod
    def rrf_fusion(
        vector_results: list[dict],
        bm25_results: list[dict],
    ) -> list[dict]:
        """Reciprocal Rank Fusion — 只看排名，不看分数绝对值"""
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
            {
                "text": t,
                "score": score_map[t],
                "metadata": meta_map[t],
                "source": source_map[t],
            }
            for t in sorted_texts
        ]

    # ──────────── Reranking ────────────
    def rerank(self, query: str, candidates: list[dict], top_n: int) -> list[dict]:
        """Cross-Encoder 精排"""
        if not candidates:
            return []

        pairs = [[query, item["text"]] for item in candidates]
        scores = self.reranker.compute_score(pairs, normalize=True)
        if isinstance(scores, float):
            scores = [scores]

        for item, score in zip(candidates, scores):
            item["rerank_score"] = score

        candidates.sort(key=lambda x: -x["rerank_score"])
        return candidates[:top_n]

    # ──────────── 完整检索 ────────────
    def search(self, query: str, verbose: bool = True) -> list[dict]:
        """
        两阶段检索:
        Stage 1: 向量 + BM25 → RRF 融合
        Stage 2: Reranker 精排
        """
        t0 = time.time()

        # Stage 1
        vector_results = self.vector_search(query, VECTOR_TOP_K)
        bm25_results = self.bm25_search(query, BM25_TOP_K)
        fused = self.rrf_fusion(vector_results, bm25_results)[:FUSION_TOP_K]

        # Stage 2
        final = self.rerank(query, fused, FINAL_TOP_N)

        elapsed = time.time() - t0

        if verbose:
            both = sum(1 for x in fused if x["source"] == "VB")
            vec_only = sum(1 for x in fused if x["source"] == "V")
            bm25_only = sum(1 for x in fused if x["source"] == "B")

            print(f"\n{'─' * 60}")
            print(f"Query: {query}")
            print(f"  向量召回: {len(vector_results)} | BM25召回: {len(bm25_results)}")
            print(f"  RRF融合: {len(fused)} (双路={both}, 仅向量={vec_only}, 仅BM25={bm25_only})")
            print(f"  Rerank后: {len(final)} 条 | 耗时: {elapsed:.2f}s\n")

            for i, item in enumerate(final):
                src = item["metadata"].get("source", "?")
                heading = item["metadata"].get("Header 1", "")
                print(f"  [{i+1}] rerank={item['rerank_score']:.3f} hit={item.get('source','')} | {src} > {heading}")
                print(f"      {item['text'][:100]}...")
                print()

        return final


# ═══════════════════════════════════════════════════════════════
#  对比测试
# ═══════════════════════════════════════════════════════════════

def compare_search(retriever: HybridRetriever, query: str):
    """对比三种检索方式"""
    print(f"\n{'═' * 60}")
    print(f"Query: {query}")
    print(f"{'═' * 60}")

    # 纯向量
    vec = retriever.vector_search(query, FINAL_TOP_N)
    print(f"\n── 纯向量 ──")
    for i, item in enumerate(vec):
        src = item["metadata"].get("source", "?")
        print(f"  [{i+1}] score={item['score']:.3f} | {src} | {item['text'][:80]}...")

    # 纯 BM25
    bm25 = retriever.bm25_search(query, FINAL_TOP_N)
    print(f"\n── 纯 BM25 ──")
    for i, item in enumerate(bm25):
        src = item["metadata"].get("source", "?")
        print(f"  [{i+1}] score={item['score']:.3f} | {src} | {item['text'][:80]}...")

    # 混合 + Rerank
    print(f"\n── 混合 + Rerank ──")
    retriever.search(query, verbose=True)


# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    retriever = HybridRetriever()

    # 对比测试
    compare_search(retriever, "how to create a character movement script")
    compare_search(retriever, "RigidBody vs CharacterBody difference")

    # 交互式
    print("\n输入问题进行检索（输入 q 退出）:")
    while True:
        q = input("\n> ").strip()
        if q.lower() in ("q", "quit", "exit"):
            break
        if q:
            retriever.search(q)
