#!/usr/bin/env python3
"""
混合检索 + 对比测试（Mac / 无 torch 版）

从 Windows 复制到 Mac 的文件:
  - chroma_db/
  - bm25_index.pkl
  - onnx_model/

Mac 安装:
  uv pip install fastmcp chromadb rank-bm25 "numpy<2" onnxruntime transformers

用法:
  uv run python rag_query_onnx.py
"""

import re
import time
import pickle
import numpy as np
import chromadb
import onnxruntime as ort
from transformers import AutoTokenizer


# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"
BM25_PATH = "bm25_index.pkl"
ONNX_MODEL_DIR = "onnx_model"

VECTOR_TOP_K = 20
BM25_TOP_K = 20
RRF_K = 60
FUSION_TOP_K = 15
FINAL_TOP_N = 5

# ════════════════════════════════════════════════════════════════════════════════════


def english_tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)*", text.lower())


class HybridRetriever:
    """混合检索器：向量 + BM25 + RRF（Mac / ONNX 版）"""

    def __init__(self):
        print("初始化 HybridRetriever...")

        # ONNX Embedding
        print(f"  加载 ONNX 模型: {ONNX_MODEL_DIR}")
        self.tokenizer = AutoTokenizer.from_pretrained(ONNX_MODEL_DIR)
        self.session = ort.InferenceSession(
            f"{ONNX_MODEL_DIR}/model.onnx",
            providers=["CPUExecutionProvider"],
        )
        self._input_names = {inp.name for inp in self.session.get_inputs()}

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

        print("初始化完成\n")

    # ──────────── ONNX 编码 ────────────
    def encode_texts(self, texts: list[str]) -> list[list[float]]:
        inputs = self.tokenizer(texts, padding=True, truncation=True, return_tensors="np")
        ort_inputs = {k: v for k, v in inputs.items() if k in self._input_names}
        outputs = self.session.run(None, ort_inputs)

        hidden = outputs[0]
        mask = inputs["attention_mask"][..., None]
        pooled = (hidden * mask).sum(axis=1) / mask.sum(axis=1)
        norms = np.linalg.norm(pooled, axis=1, keepdims=True)
        return (pooled / norms).tolist()

    # ──────────── 向量检索 ────────────
    def vector_search(self, query: str, top_k: int) -> list[dict]:
        embedding = self.encode_texts([query])

        results = self.collection.query(
            query_embeddings=embedding,
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

    # ──────────── 完整检索 ────────────
    def search(self, query: str, verbose: bool = True) -> list[dict]:
        t0 = time.time()

        vector_results = self.vector_search(query, VECTOR_TOP_K)
        bm25_results = self.bm25_search(query, BM25_TOP_K)
        fused = self.rrf_fusion(vector_results, bm25_results)[:FUSION_TOP_K]
        final = fused[:FINAL_TOP_N]

        elapsed = time.time() - t0

        if verbose:
            both = sum(1 for x in fused if x["source"] == "VB")
            vec_only = sum(1 for x in fused if x["source"] == "V")
            bm25_only = sum(1 for x in fused if x["source"] == "B")

            print(f"\n{'─' * 60}")
            print(f"Query: {query}")
            print(f"  向量召回: {len(vector_results)} | BM25召回: {len(bm25_results)}")
            print(f"  RRF融合: {len(fused)} (双路={both}, 仅向量={vec_only}, 仅BM25={bm25_only})")
            print(f"  最终: {len(final)} 条 | 耗时: {elapsed:.2f}s\n")

            for i, item in enumerate(final):
                src = item["metadata"].get("source", "?")
                heading = item["metadata"].get("Header 1", "")
                print(f"  [{i+1}] rrf={item['score']:.5f} hit={item.get('source','')} | {src} > {heading}")
                print(f"      {item['text'][:100]}...")
                print()

        return final


# ═══════════════════════════════════════════════════════════════
#  对比测试
# ═══════════════════════════════════════════════════════════════

def compare_search(retriever: HybridRetriever, query: str):
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

    # 混合
    print(f"\n── 混合 + RRF ──")
    retriever.search(query, verbose=True)


# ═══════════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    retriever = HybridRetriever()

    compare_search(retriever, "how to create a character movement script")
    compare_search(retriever, "RigidBody vs CharacterBody difference")

    print("\n输入问题进行检索（输入 q 退出）:")
    while True:
        q = input("\n> ").strip()
        if q.lower() in ("q", "quit", "exit"):
            break
        if q:
            retriever.search(q)
