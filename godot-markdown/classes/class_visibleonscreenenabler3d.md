github_url
hide

# VisibleOnScreenEnabler3D

**Inherits:** `VisibleOnScreenNotifier3D<class_VisibleOnScreenNotifier3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A box-shaped region of 3D space that, when visible on screen, enables a target node.

classref-introduction-group

## Description

**VisibleOnScreenEnabler3D** contains a box-shaped region of 3D space and a target node. The target node will be automatically enabled (via its `Node.process_mode<class_Node_property_process_mode>` property) when any part of this region becomes visible on the screen, and automatically disabled otherwise. This can for example be used to activate enemies only when the player approaches them.

See `VisibleOnScreenNotifier3D<class_VisibleOnScreenNotifier3D>` if you only want to be notified when the region is visible on screen.

**Note:** **VisibleOnScreenEnabler3D** uses an approximate heuristic that doesn't take walls and other occlusion into account, unless occlusion culling is used. It also won't function unless `Node3D.visible<class_Node3D_property_visible>` is set to `true`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **EnableMode**: `🔗<enum_VisibleOnScreenEnabler3D_EnableMode>`

classref-enumeration-constant

`EnableMode<enum_VisibleOnScreenEnabler3D_EnableMode>` **ENABLE_MODE_INHERIT** = `0`

Corresponds to `Node.PROCESS_MODE_INHERIT<class_Node_constant_PROCESS_MODE_INHERIT>`.

classref-enumeration-constant

`EnableMode<enum_VisibleOnScreenEnabler3D_EnableMode>` **ENABLE_MODE_ALWAYS** = `1`

Corresponds to `Node.PROCESS_MODE_ALWAYS<class_Node_constant_PROCESS_MODE_ALWAYS>`.

classref-enumeration-constant

`EnableMode<enum_VisibleOnScreenEnabler3D_EnableMode>` **ENABLE_MODE_WHEN_PAUSED** = `2`

Corresponds to `Node.PROCESS_MODE_WHEN_PAUSED<class_Node_constant_PROCESS_MODE_WHEN_PAUSED>`.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`EnableMode<enum_VisibleOnScreenEnabler3D_EnableMode>` **enable_mode** = `0` `🔗<class_VisibleOnScreenEnabler3D_property_enable_mode>`

classref-property-setget

- `void (No return value.)` **set_enable_mode**(value: `EnableMode<enum_VisibleOnScreenEnabler3D_EnableMode>`)
- `EnableMode<enum_VisibleOnScreenEnabler3D_EnableMode>` **get_enable_mode**()

Determines how the target node is enabled. Corresponds to `ProcessMode<enum_Node_ProcessMode>`. When the node is disabled, it always uses `Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **enable_node_path** = `NodePath("..")` `🔗<class_VisibleOnScreenEnabler3D_property_enable_node_path>`

classref-property-setget

- `void (No return value.)` **set_enable_node_path**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_enable_node_path**()

The path to the target node, relative to the **VisibleOnScreenEnabler3D**. The target node is cached; it's only assigned when setting this property (if the **VisibleOnScreenEnabler3D** is inside the scene tree) and every time the **VisibleOnScreenEnabler3D** enters the scene tree. If the path is empty, no node will be affected. If the path is invalid, an error is also generated.