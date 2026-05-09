#!/usr/bin/env python3
"""
批量 RST → MD 转换。递归扫描目录下所有 .rst 文件。

用法:
    python rst2md_batch.py
    python rst2md_batch.py -i godot-docs -o godot-markdown
    python rst2md_batch.py --dry-run
    python rst2md_batch.py -w 8
"""

import argparse
import os
import re
import subprocess
import shutil
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed


WRAPPER_TAGS = (
    "div", "section", "span", "article", "aside",
    "nav", "header", "footer", "figure", "figcaption",
    "main", "details", "summary", "colgroup", "col",
    "thead", "tbody", "tfoot",
)


def convert_rst_to_md(rst_text: str) -> str:
    result = subprocess.run(
        ["pandoc", "-f", "rst", "-t", "gfm", "--wrap=none"],
        input=rst_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def clean_markdown(md: str) -> str:
    text = md

    for tag in WRAPPER_TAGS:
        text = re.sub(rf"</?{tag}[^>]*>", "", text, flags=re.IGNORECASE)

    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r":ref:`([^<`]+)\s*<[^>]+>`", r"\1", text)
    text = re.sub(r":doc:`([^`]+)`", r"\1", text)
    text = re.sub(r":math:`([^`]+)`", r"$\1$", text)
    text = re.sub(r":(\w+):`([^`]+)`", r"`\2`", text)
    text = re.sub(r"\.\.\s+(\w+)::", r"**\1:**", text)
    text = re.sub(r"^\.\.\s.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r":class:\s*\S+", "", text)
    text = re.sub(r"\[]$$[^)]*$$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)

    return text.strip()


def process_one(rst_path: str, out_path: str) -> tuple[str, bool, str]:
    try:
        rst_text = Path(rst_path).read_text(encoding="utf-8")
        md_text = convert_rst_to_md(rst_text)
        md_text = clean_markdown(md_text)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        Path(out_path).write_text(md_text, encoding="utf-8")
        return (rst_path, True, f"{len(rst_text)}B → {len(md_text)}B")
    except Exception as e:
        return (rst_path, False, str(e))


def main():
    parser = argparse.ArgumentParser(description="批量 .rst → .md 转换")
    parser.add_argument(
        "-i", "--input",
        default="godot-docs",
        help="输入目录 (默认: godot-docs)",
    )
    parser.add_argument(
        "-o", "--output",
        default="godot-markdown",
        help="输出目录 (默认: godot-markdown)",
    )
    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=4,
        help="并行进程数 (默认: 4)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅预览文件映射，不实际转换",
    )

    args = parser.parse_args()

    if not shutil.which("pandoc"):
        print("错误: 未找到 pandoc。", file=sys.stderr)
        print("  Ubuntu/Debian: sudo apt install pandoc", file=sys.stderr)
        print("  macOS:         brew install pandoc", file=sys.stderr)
        sys.exit(1)

    input_root = Path(args.input).resolve()
    output_root = Path(args.output).resolve()

    if not input_root.is_dir():
        print(f"错误: 目录不存在 → {input_root}", file=sys.stderr)
        sys.exit(1)

    rst_files = sorted(input_root.rglob("*.rst"))
    total = len(rst_files)

    if total == 0:
        print(f"未找到 .rst 文件: {input_root}")
        return

    print(f"输入目录: {input_root}")
    print(f"输出目录: {output_root}")
    print(f"找到 {total} 个 .rst 文件\n")

    if args.dry_run:
        for rst in rst_files:
            rel = rst.relative_to(input_root)
            out = output_root / rel.with_suffix(".md")
            print(f"  {rst}  →  {out}")
        print(f"\n(dry-run，未实际转换)")
        return

    tasks = []
    for rst in rst_files:
        rel = rst.relative_to(input_root)
        out = output_root / rel.with_suffix(".md")
        tasks.append((str(rst), str(out)))

    ok_count = 0
    fail_count = 0

    if args.workers <= 1:
        for i, (rp, op) in enumerate(tasks, 1):
            _, success, msg = process_one(rp, op)
            status = "✓" if success else "✗"
            print(f"  [{i}/{total}] {status}  {rp}  {msg}")
            ok_count += success
            fail_count += (not success)
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as executor:
            futures = {
                executor.submit(process_one, rp, op): (rp, i)
                for i, (rp, op) in enumerate(tasks, 1)
            }
            for future in as_completed(futures):
                rp, idx = futures[future]
                _, success, msg = future.result()
                status = "✓" if success else "✗"
                print(f"  [{idx}/{total}] {status}  {rp}  {msg}")
                ok_count += success
                fail_count += (not success)

    print(f"\n完成: {ok_count} 成功, {fail_count} 失败, 共 {total}")


if __name__ == "__main__":
    main()
