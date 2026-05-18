github_url
hide

# AnimationNodeBlendSpace2D

**Inherits:** `AnimationRootNode<class_AnimationRootNode>` **\<** `AnimationNode<class_AnimationNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A set of `AnimationRootNode<class_AnimationRootNode>`s placed on 2D coordinates, crossfading between the three adjacent ones. Used by `AnimationTree<class_AnimationTree>`.

classref-introduction-group

## Description

A resource used by `AnimationNodeBlendTree<class_AnimationNodeBlendTree>`.

**AnimationNodeBlendSpace2D** represents a virtual 2D space on which `AnimationRootNode<class_AnimationRootNode>`s are placed. Outputs the linear blend of the three adjacent animations using a `Vector2<class_Vector2>` weight. Adjacent in this context means the three `AnimationRootNode<class_AnimationRootNode>`s making up the triangle that contains the current value.

You can add vertices to the blend space with `add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>` and automatically triangulate it by setting `auto_triangles<class_AnimationNodeBlendSpace2D_property_auto_triangles>` to `true`. Otherwise, use `add_triangle()<class_AnimationNodeBlendSpace2D_method_add_triangle>` and `remove_triangle()<class_AnimationNodeBlendSpace2D_method_remove_triangle>` to triangulate the blend space by hand.

classref-introduction-group

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**triangles_updated**() `🔗<class_AnimationNodeBlendSpace2D_signal_triangles_updated>`

Emitted every time the blend space's triangles are created, removed, or when one of their vertices changes position.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **BlendMode**: `🔗<enum_AnimationNodeBlendSpace2D_BlendMode>`

classref-enumeration-constant

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>` **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

classref-enumeration-constant

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>` **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

classref-enumeration-constant

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>` **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to `BLEND_MODE_DISCRETE<class_AnimationNodeBlendSpace2D_constant_BLEND_MODE_DISCRETE>`, but starts the new animation at the last animation's playback position.

classref-item-separator

classref-enumeration

enum **SyncMode**: `🔗<enum_AnimationNodeBlendSpace2D_SyncMode>`

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` **SYNC_MODE_NONE** = `0`

Inactive animations are frozen and do not advance.

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` **SYNC_MODE_INDEPENDENT** = `1`

Inactive animations advance with a weight of `0`. This is equivalent to the previous `sync = true` behavior.

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` **SYNC_MODE_CYCLIC_MUTABLE** = `2`

All animations are time-scaled so they stay in sync, with the cycle length dynamically computed from active blend weights. This is self-normalizing: a solo animation plays at normal speed.

**Note:** If you apply `AnimationNodeTimeSeek<class_AnimationNodeTimeSeek>` to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use `AnimationNodeAnimation.use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>` to align the animation lengths.

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` **SYNC_MODE_CYCLIC_CONSTANT** = `3`

All animations are time-scaled so they complete one cycle in `cyclic_length<class_AnimationNodeBlendSpace2D_property_cyclic_length>` seconds, keeping them in sync regardless of their individual lengths.

**Note:** If you apply `AnimationNodeTimeSeek<class_AnimationNodeTimeSeek>` to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use `AnimationNodeAnimation.use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>` to align the animation lengths.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **auto_triangles** = `true` `🔗<class_AnimationNodeBlendSpace2D_property_auto_triangles>`

classref-property-setget

- `void (No return value.)` **set_auto_triangles**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_auto_triangles**()

If `true`, the blend space is triangulated automatically. The mesh updates every time you add or remove points with `add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>` and `remove_blend_point()<class_AnimationNodeBlendSpace2D_method_remove_blend_point>`.

classref-item-separator

classref-property

`BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>` **blend_mode** = `0` `🔗<class_AnimationNodeBlendSpace2D_property_blend_mode>`

classref-property-setget

- `void (No return value.)` **set_blend_mode**(value: `BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>`)
- `BlendMode<enum_AnimationNodeBlendSpace2D_BlendMode>` **get_blend_mode**()

Controls the interpolation between animations.

classref-item-separator

classref-property

`float<class_float>` **cyclic_length** = `0.0` `🔗<class_AnimationNodeBlendSpace2D_property_cyclic_length>`

classref-property-setget

- `void (No return value.)` **set_cyclic_length**(value: `float<class_float>`)
- `float<class_float>` **get_cyclic_length**()

The cycle length in seconds used by `SYNC_MODE_CYCLIC_CONSTANT<class_AnimationNodeBlendSpace2D_constant_SYNC_MODE_CYCLIC_CONSTANT>`. All animations are time-scaled so they complete one full cycle in this duration. Must be greater than `0` for cyclic sync to take effect.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **max_space** = `Vector2(1, 1)` `🔗<class_AnimationNodeBlendSpace2D_property_max_space>`

classref-property-setget

- `void (No return value.)` **set_max_space**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_max_space**()

The blend space's X and Y axes' upper limit for the points' position. See `add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **min_space** = `Vector2(-1, -1)` `🔗<class_AnimationNodeBlendSpace2D_property_min_space>`

classref-property-setget

- `void (No return value.)` **set_min_space**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_min_space**()

The blend space's X and Y axes' lower limit for the points' position. See `add_blend_point()<class_AnimationNodeBlendSpace2D_method_add_blend_point>`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **snap** = `Vector2(0.1, 0.1)` `🔗<class_AnimationNodeBlendSpace2D_property_snap>`

classref-property-setget

- `void (No return value.)` **set_snap**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_snap**()

Position increment to snap to when moving a point.

classref-item-separator

classref-property

`bool<class_bool>` **sync** `🔗<class_AnimationNodeBlendSpace2D_property_sync>`

classref-property-setget

- `void (No return value.)` **set_use_sync**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_sync**()

**Deprecated:** Use `sync_mode<class_AnimationNodeBlendSpace2D_property_sync_mode>` instead.

If `true`, sync mode is enabled (equivalent to `SYNC_MODE_INDEPENDENT<class_AnimationNodeBlendSpace2D_constant_SYNC_MODE_INDEPENDENT>`). This property is kept for backward compatibility.

classref-item-separator

classref-property

`SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` **sync_mode** = `0` `🔗<class_AnimationNodeBlendSpace2D_property_sync_mode>`

classref-property-setget

- `void (No return value.)` **set_sync_mode**(value: `SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>`)
- `SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` **get_sync_mode**()

Controls how animations are synced when blended. See `SyncMode<enum_AnimationNodeBlendSpace2D_SyncMode>` for available options.

classref-item-separator

classref-property

`String<class_String>` **x_label** = `"x"` `🔗<class_AnimationNodeBlendSpace2D_property_x_label>`

classref-property-setget

- `void (No return value.)` **set_x_label**(value: `String<class_String>`)
- `String<class_String>` **get_x_label**()

Name of the blend space's X axis.

classref-item-separator

classref-property

`String<class_String>` **y_label** = `"y"` `🔗<class_AnimationNodeBlendSpace2D_property_y_label>`

classref-property-setget

- `void (No return value.)` **set_y_label**(value: `String<class_String>`)
- `String<class_String>` **get_y_label**()

Name of the blend space's Y axis.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_blend_point**(node: `AnimationRootNode<class_AnimationRootNode>`, pos: `Vector2<class_Vector2>`, at_index: `int<class_int>` = -1, name: `StringName<class_StringName>` = &"") `🔗<class_AnimationNodeBlendSpace2D_method_add_blend_point>`

Adds a new point with `name` that represents a `node` at the position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

**Note:** If no name is provided, safe index is used as reference. In the future, empty names will be deprecated, so explicitly passing a name is recommended.

classref-item-separator

classref-method

`void (No return value.)` **add_triangle**(x: `int<class_int>`, y: `int<class_int>`, z: `int<class_int>`, at_index: `int<class_int>` = -1) `🔗<class_AnimationNodeBlendSpace2D_method_add_triangle>`

Creates a new triangle using three points `x`, `y`, and `z`. Triangles can overlap. You can insert the triangle at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

classref-item-separator

classref-method

`int<class_int>` **find_blend_point_by_name**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace2D_method_find_blend_point_by_name>`

Returns the index of the blend point with the given `name`. Returns `-1` if no blend point with that name is found.

classref-item-separator

classref-method

`int<class_int>` **get_blend_point_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_count>`

Returns the number of points in the blend space.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_blend_point_name**(point: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_name>`

Returns the name of the blend point at index `point`.

classref-item-separator

classref-method

`AnimationRootNode<class_AnimationRootNode>` **get_blend_point_node**(point: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_node>`

Returns the `AnimationRootNode<class_AnimationRootNode>` referenced by the point at index `point`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_blend_point_position**(point: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace2D_method_get_blend_point_position>`

Returns the position of the point at index `point`.

classref-item-separator

classref-method

`int<class_int>` **get_triangle_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace2D_method_get_triangle_count>`

Returns the number of triangles in the blend space.

classref-item-separator

classref-method

`int<class_int>` **get_triangle_point**(triangle: `int<class_int>`, point: `int<class_int>`) `🔗<class_AnimationNodeBlendSpace2D_method_get_triangle_point>`

Returns the position of the point at index `point` in the triangle of index `triangle`.

classref-item-separator

classref-method

`void (No return value.)` **remove_blend_point**(point: `int<class_int>`) `🔗<class_AnimationNodeBlendSpace2D_method_remove_blend_point>`

Removes the point at index `point` from the blend space.

classref-item-separator

classref-method

`void (No return value.)` **remove_triangle**(triangle: `int<class_int>`) `🔗<class_AnimationNodeBlendSpace2D_method_remove_triangle>`

Removes the triangle at index `triangle` from the blend space.

classref-item-separator

classref-method

`void (No return value.)` **reorder_blend_point**(from_index: `int<class_int>`, to_index: `int<class_int>`) `🔗<class_AnimationNodeBlendSpace2D_method_reorder_blend_point>`

Swaps the blend points at indices `from_index` and `to_index`, exchanging their positions and properties.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_point_name**(point: `int<class_int>`, name: `StringName<class_StringName>`) `🔗<class_AnimationNodeBlendSpace2D_method_set_blend_point_name>`

Sets the name of the blend point at index `point`. If the name conflicts with an existing point, a unique name will be generated automatically.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_point_node**(point: `int<class_int>`, node: `AnimationRootNode<class_AnimationRootNode>`) `🔗<class_AnimationNodeBlendSpace2D_method_set_blend_point_node>`

Changes the `AnimationNode<class_AnimationNode>` referenced by the point at index `point`.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_point_position**(point: `int<class_int>`, pos: `Vector2<class_Vector2>`) `🔗<class_AnimationNodeBlendSpace2D_method_set_blend_point_position>`

Updates the position of the point at index `point` in the blend space.