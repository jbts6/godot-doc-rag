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

# 只导出随机 20 个
uv run python rag_audit.py --samples 20 --export sample.csv

# 只导出过短的
uv run python rag_audit.py --short --export short.csv

# 只导出某个文件的
uv run python rag_audit.py --source gdscript --export gdscript.csv

# 抽样 + 来源过滤 + 导出
uv run python rag_audit.py --source physics --samples 10 --export physics_sample.csv

# 终端显示（不导出）
uv run python rag_audit.py --samples 20
uv run python rag_audit.py --source gdscript --samples 5

```

## 添加 MCP

调整 `top_k` 的默认值，可以比对token使用情况

```bash
# 在项目目录下执行 windows / Mac 略有不同
claude mcp add godot-docs -- ~/godot-doc-rag/.venv/Scripts/python.exe ~/git/godot-doc-rag/godot_rag_mcp.py
```

## 删除 MCP

```bash
claude mcp remove godot-docs
```

