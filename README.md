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
uv run python rst2md_batch.py
```

## 生成chroma_db
如果你是N卡，请先看下面的**NVIDIA GPU 加速**。
CPU跑要十几分钟，N卡会快非常多。
不想构建的去看[issue](https://github.com/jbts6/godot-doc-rag/issues/1)
如果保留全部Markdown的话，一共1580个文件,47k chunk，只留`classes`和`tutorials`的话，1469，少2000左右的chunk。

```bash
uv run python rag_index.py
```

### 验证

```python
import torch
print(torch.cuda.is_available())    # True
print(torch.cuda.get_device_name()) # 你的显卡型号
```

### 性能对比（47k chunks, all-mpnet-base-v2）

| | CPU | NVIDIA GPU |
|---|---|---|
| 建索引编码 | ~15 min | ~1 min |
| 单次查询 encode | 50-80ms | 3-8ms |
| Rerank 12 条 | 200-500ms | 20-50ms |

直接复制进 README 就行，以后换 N 卡按这个改三个地方就完事。

## 检验chunk 质量

```bash
# 查看对比结果
uv run pyton rag_query.py

# 先看总体情况
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

调整 `top_k` 的默认值，可以比对token使用情况。
如果你和我一样是 intel Mac 并且更新到了 MaxOS 26，那请使用`godot_rag_mcp_onnx.py`

```bash
# 记得修改PATH
claude mcp add godot-docs -- uv run python C:/git/godot-doc-rag/godot_rag_mcp.py
```

如果是用于其他IDE，可以参考
```
{
  "mcpServers": {
    "godot-docs": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\git\\godot-doc-rag",
        "run",
        "python",
        "godot_rag_mcp.py"
      ]
    }
  }
}
```

## 删除 MCP

```bash
claude mcp remove godot-docs
```