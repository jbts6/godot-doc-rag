#!/usr/bin/env python3
"""
单文件 RST → MD 转换（用于测试）。

用法:
    修改下方 RST_PATH 和 REMOVE_DIV，然后直接运行。
    输出到当前工作目录，文件名与源文件相同但扩展名为 .md。
"""

import subprocess
import re
import sys
from pathlib import Path

# ═══════════════════════════════════════ 配置区 ═══════════════════════════════════════

# 输入文件路径（写死，按需修改）
RST_PATH = "C:\git\godot-doc-rag\\2d_transforms.rst"

# 是否去除 div 及其他包装标签
REMOVE_DIV = True

# ════════════════════════════════════════════════════════════════════════════════════


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
        print(f"pandoc 错误:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return result.stdout


def clean_markdown(md: str, remove_div: bool) -> str:
    text = md

    if remove_div:
        # 移除所有包装性 HTML 标签
        for tag in WRAPPER_TAGS:
            text = re.sub(rf"</?{tag}[^>]*>", "", text, flags=re.IGNORECASE)
        # 移除 HTML 注释
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        # 移除 :class: 残留
        text = re.sub(r":class:\s*\S+", "", text)

    # 以下为始终执行的清理
    text = re.sub(r":ref:`([^<`]+)\s*<[^>]+>`", r"\1", text)
    text = re.sub(r":doc:`([^`]+)`", r"\1", text)
    text = re.sub(r":math:`([^`]+)`", r"$\1$", text)
    text = re.sub(r":(\w+):`([^`]+)`", r"`\2`", text)
    text = re.sub(r"\.\.\s+(\w+)::", r"**\1:**", text)
    text = re.sub(r"^\.\.\s.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[]$$[^)]*$$", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)

    return text.strip()


def main():
    rst_path = Path(RST_PATH).resolve()

    if not rst_path.exists():
        print(f"文件不存在: {rst_path}", file=sys.stderr)
        sys.exit(1)

    print(f"输入:     {rst_path}")
    print(f"去 div:   {'是' if REMOVE_DIV else '否'}")

    rst_text = rst_path.read_text(encoding="utf-8")
    print(f"RST 大小: {len(rst_text)} 字节")

    md_text = convert_rst_to_md(rst_text)
    print(f"转换完成: {len(md_text)} 字节 (pandoc)")

    md_text = clean_markdown(md_text, remove_div=REMOVE_DIV)
    print(f"清理完成: {len(md_text)} 字节")

    out_path = Path.cwd() / rst_path.with_suffix(".md").name
    out_path.write_text(md_text, encoding="utf-8")
    print(f"已保存:   {out_path}")


if __name__ == "__main__":
    main()
