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
如果你是N卡，请先看下面的**NVIDIA GPU 加速**。
CPU跑要十几分钟，N卡会快非常多。

```bash
uv run python rag_index.py
```

```markdown
## NVIDIA GPU 加速

### 安装

## NVIDIA GPU 加速

### 安装

# 先卸载 CPU 版 PyTorch
uv remove torch

# 安装 CUDA 版 PyTorch（以下以 CUDA 12.x 为例）
uv pip install torch --index-url https://download.pytorch.org/whl/cu124

# 其余依赖不变
uv pip install langchain-text-splitters chromadb sentence-transformers FlagEmbedding rank-bm25 fastmcp

### rag_index.py 关键改动

# 配置区
EMBED_BATCH = 2048    # GPU 显存充足时可以调大（CPU 时为 512）

# 加载模型时指定 device
model = SentenceTransformer(EMBED_MODEL, device="cuda")

### rag_query.py 关键改动

EMBED_BATCH = 2048    # GPU 显存充足时可以调大（CPU 时为 512）
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
```

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
claude mcp add godot-docs -- uv run PATH/godot-doc-rag/godot_rag_mcp_onnx.py
```

## 删除 MCP

```bash
claude mcp remove godot-docs
```

## 效果演示

每次返回内容并不完全相同，消耗的token可以作为参考，同一个问题多次新会话测试`Messages`在7-9K。

> 帮我查一下 Godot 的 CharacterBody3D 怎么用

```
● CharacterBody3D 使用指南

  概述

  CharacterBody3D 是 Godot
  中专为玩家控制的物理体设计的类。它不受物理引擎影响（重力、摩擦力等需手动实现），但可以推动其他物理体。主要特点：

  - 手动控制移动，提供 move_and_slide() 和 move_and_collide() 方法
  - 自带墙壁/斜坡检测功能
  - 适合平台游戏、第一/三人称角色等

  核心用法

  1. 基础移动模板

  extends CharacterBody3D

  var speed = 5.0
  var jump_velocity = 4.5

  # 获取重力（从项目设置）
  func get_gravity() -> float:
      return ProjectSettings.get_setting("physics/3d/default_gravity")

  func _physics_process(delta):
      # 添加重力
      if not is_on_floor():
          velocity.y -= get_gravity() * delta

      # 处理跳跃
      if Input.is_action_just_pressed("ui_accept") and is_on_floor():
          velocity.y = jump_velocity

      # 获取输入方向
      var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
      var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()

      if direction:
          velocity.x = direction.x * speed
          velocity.z = direction.z * speed
      else:
          velocity.x = move_toward(velocity.x, 0, speed)
          velocity.z = move_toward(velocity.z, 0, speed)

      move_and_slide()


  2. 关键方法

  ┌────────────────────────────────────┬────────────────────────────────────────────┐
  │                方法                │                    说明                    │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ move_and_slide()                   │ 沿速度方向移动并自动处理滑动碰撞（推荐）   │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ move_and_collide(velocity * delta) │ 基础碰撞移动，返回 KinematicCollision3D    │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ is_on_floor()                      │ 是否在地面上（需设 up_direction）          │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ is_on_wall()                       │ 是否撞墙                                   │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ is_on_ceiling()                    │ 是否撞天花板                               │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ get_last_slide_collision()         │ 获取最后一次滑动碰撞信息                   │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ get_slide_collision_count()        │ 获取本次移动的碰撞次数                     │
  ├────────────────────────────────────┼────────────────────────────────────────────┤
  │ get_real_velocity()                │ 获取实际移动速度（爬坡时与 velocity 不同） │
  └────────────────────────────────────┴────────────────────────────────────────────┘

  3. 重要属性

  ┌──────────────────────┬───────────────────────────────────────────────────────────────────────────┐
  │         属性         │                                   说明                                    │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ velocity             │ 当前速度向量（m/s），被 move_and_slide() 修改                             │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ up_direction         │ 地平面方向，默认 Vector3(0, -1, 0)                                        │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ motion_mode          │ MOTION_MODE_GROUNDED（地面模式，默认）或 MOTION_MODE_FLOATING（浮动模式） │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ max_slides           │ 每次移动最大滑动次数，默认 4                                              │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ floor_stop_on_slope  │ 是否在斜坡上静止不动                                                      │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ floor_max_angle      │ 最大坡角（弧度），默认 45°                                                │
  ├──────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ wall_min_slide_angle │ 墙面最小滑动角度，默认 15°                                                │
  └──────────────────────┴───────────────────────────────────────────────────────────────────────────┘

  4. 两种运动模式

  - MOTION_MODE_GROUNDED（默认）：区分地板/墙壁/天花板，支持斜坡检测
  - MOTION_MODE_FLOATING：所有碰撞视为墙壁，适合太空/飞行场景

  5. 注意事项

  - 移动逻辑必须在 _physics_process() 中处理，而不是 _process()
  - 不要直接设置 position，应使用 move_and_slide() 或 move_and_collide()
  - 如果身体卡住，检查 max_slides 和 floor_max_angle 是否合理
  - 处理移动平台时，move_and_slide() 会自动加上平台速度

  需要我帮你写一个具体的 3D 角色控制器示例代码吗？

✻ Crunched for 31s

> /context
  ⎿  Context Usage
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁   deepseek-v4-flash
     ⛁ ⛁ ⛁ ⛀ ⛀ ⛁ ⛁ ⛁ ⛁ ⛁   35.5k/200k tokens (18%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   Estimated usage by category
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System prompt: 6.8k tokens (3.4%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System tools: 20.9k tokens (10.5%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ MCP tools: 61 tokens (0.0%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Custom agents: 874 tokens (0.4%)
     ⛶ ⛶ ⛶ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Skills: 1.5k tokens (0.7%)
     ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Messages: 8.4k tokens (4.2%)
                           ⛶ Free space: 128.5k (64.3%)
                           ⛝ Autocompact buffer: 33k tokens (16.5%)

    MCP tools · /mcp
    ├ mcp__godot-docs__godot_search: 27 tokens
    └ mcp__godot-docs__godot_search_in_file: 34 tokens
```
