github_url
hide

# AnimationNodeBlendSpace1D

**Inherits:** `AnimationRootNode<class_AnimationRootNode>` **\<** `AnimationNode<class_AnimationNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A set of `AnimationRootNode<class_AnimationRootNode>`s placed on a virtual axis, crossfading between the two adjacent ones. Used by `AnimationTree<class_AnimationTree>`.

classref-introduction-group

## Description

A resource used by `AnimationNodeBlendTree<class_AnimationNodeBlendTree>`.

**AnimationNodeBlendSpace1D** represents a virtual axis on which any type of `AnimationRootNode<class_AnimationRootNode>`s can be added using `add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>`. Outputs the linear blend of the two `AnimationRootNode<class_AnimationRootNode>`s adjacent to the current value.

You can set the extents of the axis with `min_space<class_AnimationNodeBlendSpace1D_property_min_space>` and `max_space<class_AnimationNodeBlendSpace1D_property_max_space>`.

classref-introduction-group

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **BlendMode**: `🔗<enum_AnimationNodeBlendSpace1D_BlendMode>`

classref-enumeration-constant

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>` **BLEND_MODE_INTERPOLATED** = `0`

The interpolation between animations is linear.

classref-enumeration-constant

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>` **BLEND_MODE_DISCRETE** = `1`

The blend space plays the animation of the animation node which blending position is closest to. Useful for frame-by-frame 2D animations.

classref-enumeration-constant

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>` **BLEND_MODE_DISCRETE_CARRY** = `2`

Similar to `BLEND_MODE_DISCRETE<class_AnimationNodeBlendSpace1D_constant_BLEND_MODE_DISCRETE>`, but starts the new animation at the last animation's playback position.

classref-item-separator

classref-enumeration

enum **SyncMode**: `🔗<enum_AnimationNodeBlendSpace1D_SyncMode>`

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` **SYNC_MODE_NONE** = `0`

Inactive animations are frozen and do not advance.

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` **SYNC_MODE_INDEPENDENT** = `1`

Inactive animations advance with a weight of `0`. This is equivalent to the previous `sync = true` behavior.

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` **SYNC_MODE_CYCLIC_MUTABLE** = `2`

All animations are time-scaled so they stay in sync, with the cycle length dynamically computed from active blend weights. This is self-normalizing: a solo animation plays at normal speed.

**Note:** If you apply `AnimationNodeTimeSeek<class_AnimationNodeTimeSeek>` to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use `AnimationNodeAnimation.use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>` to align the animation lengths.

classref-enumeration-constant

`SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` **SYNC_MODE_CYCLIC_CONSTANT** = `3`

All animations are time-scaled so they complete one cycle in `cyclic_length<class_AnimationNodeBlendSpace1D_property_cyclic_length>` seconds, keeping them in sync regardless of their individual lengths.

**Note:** If you apply `AnimationNodeTimeSeek<class_AnimationNodeTimeSeek>` to the result when handling animations of different lengths, synchronization will be broken. In such cases, it is recommended to use `AnimationNodeAnimation.use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>` to align the animation lengths.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>` **blend_mode** = `0` `🔗<class_AnimationNodeBlendSpace1D_property_blend_mode>`

classref-property-setget

- `void (No return value.)` **set_blend_mode**(value: `BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>`)
- `BlendMode<enum_AnimationNodeBlendSpace1D_BlendMode>` **get_blend_mode**()

Controls the interpolation between animations.

classref-item-separator

classref-property

`float<class_float>` **cyclic_length** = `0.0` `🔗<class_AnimationNodeBlendSpace1D_property_cyclic_length>`

classref-property-setget

- `void (No return value.)` **set_cyclic_length**(value: `float<class_float>`)
- `float<class_float>` **get_cyclic_length**()

The cycle length in seconds used by `SYNC_MODE_CYCLIC_CONSTANT<class_AnimationNodeBlendSpace1D_constant_SYNC_MODE_CYCLIC_CONSTANT>`. All animations are time-scaled so they complete one full cycle in this duration. Must be greater than `0` for cyclic sync to take effect.

classref-item-separator

classref-property

`float<class_float>` **max_space** = `1.0` `🔗<class_AnimationNodeBlendSpace1D_property_max_space>`

classref-property-setget

- `void (No return value.)` **set_max_space**(value: `float<class_float>`)
- `float<class_float>` **get_max_space**()

The blend space's axis's upper limit for the points' position. See `add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>`.

classref-item-separator

classref-property

`float<class_float>` **min_space** = `-1.0` `🔗<class_AnimationNodeBlendSpace1D_property_min_space>`

classref-property-setget

- `void (No return value.)` **set_min_space**(value: `float<class_float>`)
- `float<class_float>` **get_min_space**()

The blend space's axis's lower limit for the points' position. See `add_blend_point()<class_AnimationNodeBlendSpace1D_method_add_blend_point>`.

classref-item-separator

classref-property

`float<class_float>` **snap** = `0.1` `🔗<class_AnimationNodeBlendSpace1D_property_snap>`

classref-property-setget

- `void (No return value.)` **set_snap**(value: `float<class_float>`)
- `float<class_float>` **get_snap**()

Position increment to snap to when moving a point on the axis.

classref-item-separator

classref-property

`bool<class_bool>` **sync** `🔗<class_AnimationNodeBlendSpace1D_property_sync>`

classref-property-setget

- `void (No return value.)` **set_use_sync**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_sync**()

**Deprecated:** Use `sync_mode<class_AnimationNodeBlendSpace1D_property_sync_mode>` instead.

If `true`, sync mode is enabled (equivalent to `SYNC_MODE_INDEPENDENT<class_AnimationNodeBlendSpace1D_constant_SYNC_MODE_INDEPENDENT>`). This property is kept for backward compatibility.

classref-item-separator

classref-property

`SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` **sync_mode** = `0` `🔗<class_AnimationNodeBlendSpace1D_property_sync_mode>`

classref-property-setget

- `void (No return value.)` **set_sync_mode**(value: `SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>`)
- `SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` **get_sync_mode**()

Controls how animations are synced when blended. See `SyncMode<enum_AnimationNodeBlendSpace1D_SyncMode>` for available options.

classref-item-separator

classref-property

`String<class_String>` **value_label** = `"value"` `🔗<class_AnimationNodeBlendSpace1D_property_value_label>`

classref-property-setget

- `void (No return value.)` **set_value_label**(value: `String<class_String>`)
- `String<class_String>` **get_value_label**()

Label of the virtual axis of the blend space.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_blend_point**(node: `AnimationRootNode<class_AnimationRootNode>`, pos: `float<class_float>`, at_index: `int<class_int>` = -1, name: `StringName<class_StringName>` = &"") `🔗<class_AnimationNodeBlendSpace1D_method_add_blend_point>`

Adds a new point with `name` that represents a `node` on the virtual axis at a given position set by `pos`. You can insert it at a specific index using the `at_index` argument. If you use the default value for `at_index`, the point is inserted at the end of the blend points array.

**Note:** If no name is provided, safe index is used as reference. In the future, empty names will be deprecated, so explicitly passing a name is recommended.

classref-item-separator

classref-method

`int<class_int>` **find_blend_point_by_name**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace1D_method_find_blend_point_by_name>`

Returns the index of the blend point with the given `name`. Returns `-1` if no blend point with that name is found.

classref-item-separator

classref-method

`int<class_int>` **get_blend_point_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_count>`

Returns the number of points on the blend axis.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_blend_point_name**(point: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_name>`

Returns the name of the blend point at index `point`.

classref-item-separator

classref-method

`AnimationRootNode<class_AnimationRootNode>` **get_blend_point_node**(point: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_node>`

Returns the `AnimationNode<class_AnimationNode>` referenced by the point at index `point`.

classref-item-separator

classref-method

`float<class_float>` **get_blend_point_position**(point: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeBlendSpace1D_method_get_blend_point_position>`

Returns the position of the point at index `point`.

classref-item-separator

classref-method

`void (No return value.)` **remove_blend_point**(point: `int<class_int>`) `🔗<class_AnimationNodeBlendSpace1D_method_remove_blend_point>`

Removes the point at index `point` from the blend axis.

classref-item-separator

classref-method

`void (No return value.)` **reorder_blend_point**(from_index: `int<class_int>`, to_index: `int<class_int>`) `🔗<class_AnimationNodeBlendSpace1D_method_reorder_blend_point>`

Swaps the blend points at indices `from_index` and `to_index`, exchanging their positions and properties.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_point_name**(point: `int<class_int>`, name: `StringName<class_StringName>`) `🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_name>`

Sets the name of the blend point at index `point`. If the name conflicts with an existing point, a unique name will be generated automatically.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_point_node**(point: `int<class_int>`, node: `AnimationRootNode<class_AnimationRootNode>`) `🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_node>`

Changes the `AnimationNode<class_AnimationNode>` referenced by the point at index `point`.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_point_position**(point: `int<class_int>`, pos: `float<class_float>`) `🔗<class_AnimationNodeBlendSpace1D_method_set_blend_point_position>`

Updates the position of the point at index `point` on the blend axis.