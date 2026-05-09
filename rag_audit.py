#!/usr/bin/env python3
"""
审查 rag_index.py 生成的 chunk 质量。

用法:
    python rag_audit.py                  # 统计概览
    python rag_audit.py --samples 20     # 随机抽样 20 个 chunk
    python rag_audit.py --source gdscript  # 只看某个文件的 chunk
    python rag_audit.py --short          # 只看过短的 chunk
    python rag_audit.py --long           # 只看过长的 chunk
    python rag_audit.py --export audit.csv  # 导出全部 chunk 到 CSV
"""

import argparse
import csv
import random
import sys
from pathlib import Path

import chromadb


# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "godot_docs"

# 阈值
SHORT_THRESHOLD = 100       # 低于此字符视为过短
LONG_THRESHOLD = 800        # 高于此字符视为过长

# ════════════════════════════════════════════════════════════════════════════════════


def load_all():
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_collection(name=COLLECTION_NAME)
    total = collection.count()

    all_docs = []
    all_metas = []
    PAGE = 5000

    for offset in range(0, total, PAGE):
        data = collection.get(
            include=["documents", "metadatas"],
            limit=PAGE,
            offset=offset,
        )
        all_docs.extend(data["documents"])
        all_metas.extend(data["metadatas"])

    data = {"documents": all_docs, "metadatas": all_metas}
    return collection, data



def heading(meta: dict) -> str:
    parts = []
    for key in ("Header 1", "Header 2", "Header 3", "Header 4"):
        if key in meta and meta[key]:
            parts.append(meta[key])
    return " > ".join(parts)


def print_chunk(i: int, doc: str, meta: dict, max_preview: int = 300):
    source = meta.get("source", "?")
    h = heading(meta)
    preview = doc[:max_preview].replace("\n", "↵")
    if len(doc) > max_preview:
        preview += "..."

    print(f"\n{'─' * 70}")
    print(f"  [{i}] 来源: {source}")
    print(f"       章节: {h}")
    print(f"       长度: {len(doc)} 字符")
    print(f"       ──")
    print(f"       {preview}")
    print(f"{'─' * 70}")


# ═══════════════════════════════════════════════════════════════
#  概览统计
# ═══════════════════════════════════════════════════════════════

def cmd_overview(data):
    docs = data["documents"]
    metas = data["metadatas"]
    total = len(docs)

    sizes = [len(d) for d in docs]
    sizes.sort()

    # 来源文件统计
    sources = {}
    for m in metas:
        s = m.get("source", "?")
        sources[s] = sources.get(s, 0) + 1

    # 长度分布
    short = sum(1 for s in sizes if s < SHORT_THRESHOLD)
    ok = sum(1 for s in sizes if SHORT_THRESHOLD <= s <= LONG_THRESHOLD)
    long = sum(1 for s in sizes if s > LONG_THRESHOLD)

    # 百分位
    def percentile(lst, p):
        idx = int(len(lst) * p / 100)
        return lst[min(idx, len(lst) - 1)]

    print(f"\n{'═' * 50}")
    print(f"  Chunk 质量概览")
    print(f"{'═' * 50}")
    print(f"  总数:          {total}")
    print(f"  来源文件数:    {len(sources)}")
    print(f"")
    print(f"  长度分布:")
    print(f"    过短 (<{SHORT_THRESHOLD}字符):   {short}  ({short * 100 // total}%)")
    print(f"    正常:                       {ok}  ({ok * 100 // total}%)")
    print(f"    过长 (>{LONG_THRESHOLD}字符):   {long}  ({long * 100 // total}%)")
    print(f"")
    print(f"  长度百分位:")
    print(f"    P10:  {percentile(sizes, 10)}")
    print(f"    P25:  {percentile(sizes, 25)}")
    print(f"    P50:  {percentile(sizes, 50)}  (中位数)")
    print(f"    P75:  {percentile(sizes, 75)}")
    print(f"    P90:  {percentile(sizes, 90)}")
    print(f"")
    print(f"  最短: {sizes[0]}, 最长: {sizes[-1]}")
    print(f"  平均: {sum(sizes) // total}")

    # Top 10 文件
    print(f"\n  Chunk 最多的文件 (Top 10):")
    for source, count in sorted(sources.items(), key=lambda x: -x[1])[:10]:
        print(f"    {count:>4}  {source}")

    # 无标题的 chunk
    no_heading = sum(1 for m in metas if not heading(m))
    print(f"\n  无标题 chunk:  {no_heading}  ({no_heading * 100 // total}%)")


# ═══════════════════════════════════════════════════════════════
#  随机抽样
# ═══════════════════════════════════════════════════════════════

def cmd_samples(data, n: int, source_filter: str = None):
    docs = data["documents"]
    metas = data["metadatas"]
    total = len(docs)

    # 按来源过滤
    if source_filter:
        indices = [i for i in range(total) if source_filter.lower() in metas[i].get("source", "").lower()]
        if not indices:
            print(f"未找到匹配 '{source_filter}' 的 chunk")
            return
        print(f"匹配 '{source_filter}' 的 chunk 共 {len(indices)} 个")
    else:
        indices = list(range(total))

    sampled = random.sample(indices, min(n, len(indices)))

    for idx in sampled:
        print_chunk(idx, docs[idx], metas[idx])

    print(f"\n显示 {len(sampled)}/{len(indices)} 个 chunk")


# ═══════════════════════════════════════════════════════════════
#  短 chunk / 长 chunk
# ═══════════════════════════════════════════════════════════════

def cmd_filter_by_length(data, short: bool = False, long: bool = False):
    docs = data["documents"]
    metas = data["metadatas"]

    if short:
        threshold = SHORT_THRESHOLD
        label = "过短"
        indices = [i for i in range(len(docs)) if len(docs[i]) < threshold]
    elif long:
        threshold = LONG_THRESHOLD
        label = "过长"
        indices = [i for i in range(len(docs)) if len(docs[i]) > threshold]
    else:
        return

    print(f"\n{label} chunk (< {threshold} 字符) 共 {len(indices)} 个:\n")

    for idx in indices[:50]:  # 最多显示 50 个
        print_chunk(idx, docs[idx], metas[idx])

    if len(indices) > 50:
        print(f"\n... 还有 {len(indices) - 50} 个未显示")


# ═══════════════════════════════════════════════════════════════
#  导出 CSV
# ═══════════════════════════════════════════════════════════════

def cmd_export(data, output: str):
    docs = data["documents"]
    metas = data["metadatas"]

    with open(output, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "source", "heading", "length", "content"])

        for i in range(len(docs)):
            writer.writerow([
                i,
                metas[i].get("source", ""),
                heading(metas[i]),
                len(docs[i]),
                docs[i],
            ])

    print(f"已导出 {len(docs)} 条 chunk → {output}")
    print(f"用 Excel 打开即可审查")


# ═══════════════════════════════════════════════════════════════
#  入口
# ═══════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="审查 chunk 质量")
    parser.add_argument("--samples", type=int, default=0, help="随机抽样 N 个 chunk 查看")
    parser.add_argument("--source", type=str, default=None, help="按来源文件名过滤")
    parser.add_argument("--short", action="store_true", help="只显示过短的 chunk")
    parser.add_argument("--long", action="store_true", help="只显示过长的 chunk")
    parser.add_argument("--export", type=str, default=None, help="导出全部 chunk 到 CSV")
    args = parser.parse_args()

    collection, data = load_all()
    print(f"集合 '{COLLECTION_NAME}' 共 {collection.count()} 条记录")

    # 默认：显示概览
    if not any([args.samples, args.short, args.long, args.export]):
        cmd_overview(data)
        return

    if args.export:
        cmd_export(data, args.export)

    if args.short or args.long:
        cmd_filter_by_length(data, short=args.short, long=args.long)

    if args.samples:
        cmd_samples(data, args.samples, source_filter=args.source)


if __name__ == "__main__":
    main()
