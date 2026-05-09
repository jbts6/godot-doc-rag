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

该操作需要十几分钟，性能好的可以把`SPLIT_WORKERS`改大点，再手动删除一些无意义的Markdown，比如`404.md`，最后执行操作。

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
# 记得修改PATH
claude mcp add godot-docs -- PATH/godot-doc-rag/.venv/Scripts/python.exe PATH/godot-doc-rag/godot_rag_mcp.py
```

## 删除 MCP

```bash
claude mcp remove godot-docs
```

# 效果演示

Q: 帮我查一下 Godot 的 CharacterBody3D 怎么用

A:
● 以下是 CharacterBody3D 的使用总结，来自 Godot 官方文档：

  ---
  概述

  CharacterBody3D 是用于用户控制的物理体（如角色、移动平台等）。它不受引擎物理影响（重力、摩擦力需要自己写代码实现），但
  可以推动其他物理体。

  ---
  核心用法

  1. 在 _physics_process() 中移动

  extends CharacterBody3D

  var speed = 5.0
  var jump_speed = 4.5
  var gravity = 9.8

  func _physics_process(delta):
      # 添加重力
      velocity.y -= gravity * delta

      # 处理跳跃
      if Input.is_action_just_pressed("jump") and is_on_floor():
          velocity.y = jump_speed

      # 获取输入方向
      var input_dir = Input.get_vector("left", "right", "forward", "back")
      var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
      if direction:
          velocity.x = direction.x * speed
          velocity.z = direction.z * speed
      else:
          velocity.x = move_toward(velocity.x, 0, speed)
          velocity.z = move_toward(velocity.z, 0, speed)

      move_and_slide()

  2. 两种移动方法

  ┌────────────────────┬───────────────────────────────────────┐
  │        方法        │                 说明                  │
  ├────────────────────┼───────────────────────────────────────┤
  │ move_and_slide()   │ 自动处理滑动碰撞，适合平台/俯视角游戏 │
  ├────────────────────┼───────────────────────────────────────┤
  │ move_and_collide() │ 返回碰撞信息，需要手动处理碰撞响应    │
  └────────────────────┴───────────────────────────────────────┘

  ▎ 不要直接设置 position，而是用 move_and_slide() 或 move_and_collide()。

  ---
  关键属性
  │        属性         │  类型   │   默认值    │                    说明                    │
  ├─────────────────────┼─────────┼─────────────┼────────────────────────────────────────────┤
  │ velocity            │ Vector3 │ (0, 0, 0)   │ 当前速度向量，move_and_slide() 会修改它    │
  ├─────────────────────┼─────────┼─────────────┼────────────────────────────────────────────┤
  │ up_direction        │ Vector3 │ (0, 1, 0)   │ 定义"地板"方向（用于检测地面/墙壁/天花板） │
  ├─────────────────────┼─────────┼─────────────┼────────────────────────────────────────────┤
  │ floor_stop_on_slope │ bool    │ true        │ 在斜坡上是否停止                           │
  ├─────────────────────┼─────────┼─────────────┼────────────────────────────────────────────┤
  │ floor_max_angle     │ float   │ 0.785 (45°) │ 最大可行走坡度角度                         │
  └─────────────────────┴─────────┴─────────────┴────────────────────────────────────────────┘

  ---
  碰撞检测方法

  ┌─────────────────────────────┬────────────────────────────────┐
  │            方法             │              说明              │
  ├─────────────────────────────┼────────────────────────────────┤
  │ is_on_floor()               │ 是否在地面上                   │
  ├─────────────────────────────┼────────────────────────────────┤
  │ is_on_wall()                │ 是否在墙上                     │
  ├─────────────────────────────┼────────────────────────────────┤
  │ is_on_ceiling()             │ 是否在天花板上                 │
  ├─────────────────────────────┼────────────────────────────────┤
  │ get_real_velocity()         │ 获取实际移动速度（考虑斜坡等） │
  ├─────────────────────────────┼────────────────────────────────┤
  │ get_last_slide_collision()  │ 获取最近一次滑动碰撞信息       │
  ├─────────────────────────────┼────────────────────────────────┤
  │ get_slide_collision_count() │ 获取碰撞次数                   │
  ├─────────────────────────────┼────────────────────────────────┤
  │ get_slide_collision(i)      │ 获取第 i 次碰撞的详细信息      │
  └─────────────────────────────┴────────────────────────────────┘

  ---
  实战套路

  CharacterBody3D
  ├── CollisionShape3D (碰撞形状)
  ├── MeshInstance3D (视觉模型，可选)
  └── 脚本 (处理输入、重力、移动)

  基本流程：
  1. 设置 velocity
  2. 调用 move_and_slide()
  3. 用 is_on_floor() 等方法检测状态
  4. 重复步骤 1

  ---
  如果你想看更具体的示例（比如第一人称控制器、平台跳跃等），可以告诉我具体的场景。

✻ Baked for 35s

> /context
  ⎿  Context Usage
     ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁ ⛁   deepseek-v4-flash
     ⛁ ⛁ ⛁ ⛀ ⛀ ⛁ ⛁ ⛁ ⛁ ⛁   36k/200k tokens (18%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   Estimated usage by category
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System prompt: 6.8k tokens (3.4%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ System tools: 20.9k tokens (10.5%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ MCP tools: 61 tokens (0.0%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Custom agents: 874 tokens (0.4%)
     ⛶ ⛶ ⛶ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Skills: 1.5k tokens (0.7%)
     ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝   ⛁ Messages: 9k tokens (4.5%)
                           ⛶ Free space: 127.9k (64.0%)
                           ⛝ Autocompact buffer: 33k tokens (16.5%)

     MCP tools · /mcp
     ├ mcp__godot-docs__godot_search: 27 tokens
     └ mcp__godot-docs__godot_search_in_file: 34 tokens

