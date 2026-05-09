# godot-doc-rag

## 安装依赖
需要先安装`uv`后，执行`uv venv`

```bash
uv pip install fastmcp chromadb sentence-transformers docutils beautifulsoup4 langchain-text-splitters
```

## 更新submodules

```bash
git submodule update --remote --recursive
```

## 转成Markdown
Markdown 会生成在 **godot-markdown** 文件夹

```bash
uv run python rts2md_batch.py
```

## 生成chroma_db

```bash
uv run python rag_index.py
```

## 检验chunk 质量

```bash
# 1. 先看总体情况
uv run python rag_audit.py

# 2. 随机抽 20 个 chunk 看内容质量
uv run python rag_audit.py --samples 20

# 3. 只看 gdscript 相关的 chunk
uv run python rag_audit.py --source gdscript --samples 10

# 4. 看过短的 chunk（可能是噪音）
uv run python rag_audit.py --short

# 5. 看过长的 chunk（可能没切好）
uv run python rag_audit.py --long

# 6. 导出到 CSV，用 Excel 审查全部 chunk
uv run python rag_audit.py --export audit.csv

```

## 添加 MCP

```bash
# 在项目目录下执行 windows / Mac 略有不同
claude mcp add godot-docs -- ~/godot-doc-rag/.venv/Scripts/python.exe ~/git/godot-doc-rag/godot_rag_mcp.py
```