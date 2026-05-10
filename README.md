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
claude mcp add godot-docs -- uv run python C:/git/godot-doc-rag/godot_rag_mcp.py
```

## 删除 MCP

```bash
claude mcp remove godot-docs
```

## 效果演示

每次返回内容并不完全相同，消耗的token可以作为参考，同一个问题多次新会话测试`Messages`在7-9K。

> 帮我查一下 Godot 的 CharacterBody3D 怎么用

```
● CharacterBody3D 简介

  CharacterBody3D 是 Godot
  中专用于玩家/角色控制的物理体。它不受物理引擎影响（重力、摩擦力等需手动实现），但可以推动其他物理体。核心是提供了
  move_and_slide() 和 move_and_collide() 等高阶移动 API。

  ---
  核心属性

  ┌─────────────────────┬─────────┬─────────────────────────────────────────────────────────────────────┐
  │        属性         │  类型   │                                说明                                 │
  ├─────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
  │ velocity            │ Vector3 │ 当前速度向量（m/s），会被 move_and_slide() 修改                     │
  ├─────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
  │ up_direction        │ Vector3 │ 向上的方向（默认 Vector3.UP），用于区分墙/地板/天花板               │
  ├─────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
  │ floor_max_angle     │ float   │ 最大可攀爬角度（弧度），超过此角度被视为墙                          │
  ├─────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
  │ floor_stop_on_slide │ bool    │ 在斜坡上是否停止滑动                                                │
  ├─────────────────────┼─────────┼─────────────────────────────────────────────────────────────────────┤
  │ motion_mode         │ enum    │ MOTION_MODE_GROUNDED（地面模式）或 MOTION_MODE_FLOATING（浮动模式） │
  └─────────────────────┴─────────┴─────────────────────────────────────────────────────────────────────┘

  ---
  核心方法

  ┌─────────────────────────────┬──────────────────────┬──────────────────────────────────────┐
  │            方法             │        返回值        │                 说明                 │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ move_and_slide()            │ bool                 │ 移动并自动处理碰撞/滑行/坡度（推荐） │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ move_and_collide(velocity)  │ KinematicCollision3D │ 单次移动碰撞检测（底层 API）         │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ is_on_floor()               │ bool                 │ 是否站在地面上                       │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ is_on_wall()                │ bool                 │ 是否撞到墙                           │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ is_on_ceiling()             │ bool                 │ 是否撞到天花板                       │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ get_slide_collision(idx)    │ KinematicCollision3D │ 获取某次碰撞的详细信息               │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ get_last_slide_collision()  │ KinematicCollision3D │ 获取最后一次碰撞信息                 │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ get_slide_collision_count() │ int                  │ 获取碰撞次数                         │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ get_platform_velocity()     │ Vector3              │ 获取移动平台的线速度                 │
  ├─────────────────────────────┼──────────────────────┼──────────────────────────────────────┤
  │ get_real_velocity()         │ Vector3              │ 获取实际移动速度（含坡度导致的偏移） │
  └─────────────────────────────┴──────────────────────┴──────────────────────────────────────┘

  ---
  基本用法示例（GDScript）

  标准第三人称/第一人称移动

  extends CharacterBody3D

  @export var speed = 5.0
  @export var jump_velocity = 4.5

  func _physics_process(delta):
      # 添加重力
      if not is_on_floor():
          velocity.y -= gravity * delta  # gravity 来自 ProjectSettings

      # 处理跳跃
      if Input.is_action_just_pressed("jump") and is_on_floor():
          velocity.y = jump_velocity

      # 获取输入方向
      var input_dir = Input.get_vector("left", "right", "forward", "back")
      var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()

      # 水平移动
      if direction:
          velocity.x = direction.x * speed
          velocity.z = direction.z * speed
      else:
          velocity.x = move_toward(velocity.x, 0, speed)
          velocity.z = move_toward(velocity.z, 0, speed)

      # 执行移动
      move_and_slide()

  浮动模式（飞行/太空）

  extends CharacterBody3D

  @export var speed = 5.0
  var motion_mode = MotionMode.MOTION_MODE_FLOATING  # 所有碰撞都视为墙

  func _physics_process(delta):
      var input_dir = Input.get_vector("left", "right", "forward", "back")
      var direction = (transform.basis * Vector3(input_dir.x, input_dir.y, 0)).normalized()

      if direction:
          velocity = direction * speed
      else:
          velocity = velocity.move_toward(Vector3.ZERO, speed * delta)

      move_and_slide()

  ---
  关键要点

  1. 必须在 _physics_process() 中调用移动方法，不要直接在 _process() 里移动
  2. 不要直接设置 position，应当通过 velocity + move_and_slide() 来移动，否则会绕过物理碰撞检测
  3. 重力需要手动实现（velocity.y -= gravity * delta），引擎不会自动施加
  4. move_and_slide() 会自动：处理坡度攀爬、沿墙滑行、检测落地/撞墙
  5. velocity 是输入输出参数——传入期望速度，move_and_slide() 会根据碰撞修正它

  需要更具体的示例（如斜坡处理、爬楼梯、与 Area3D 交互等）可以继续问。

✻ Crunched for 40s

> /context
  ⎿  Context Usage
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁   deepseek-v4-flash
     ⛁ ⛁ ⛁ ⛀ ⛀ ⛀ ⛁ ⛁ ⛁ ⛁   36.3k/200k tokens (18%)
     ⛁ ⛀ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   Estimated usage by category
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System prompt: 6.8k tokens (3.4%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System tools: 20.9k tokens (10.5%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ MCP tools: 75 tokens (0.0%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Custom agents: 874 tokens (0.4%)
     ⛶ ⛶ ⛶ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Memory files: 442 tokens (0.2%)
     ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Skills: 1.5k tokens (0.7%)
                           ⛁ Messages: 9k tokens (4.5%)
                           ⛶ Free space: 127.4k (63.7%)
                           ⛝ Autocompact buffer: 33k tokens (16.5%)

     MCP tools · /mcp
     ├ mcp__godot-docs__godot_search: 34 tokens
     └ mcp__godot-docs__godot_search_in_file: 41 tokens
```
