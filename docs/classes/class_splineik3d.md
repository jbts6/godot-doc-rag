github_url
hide

# SplineIK3D

**Inherits:** `ChainIK3D<class_ChainIK3D>` **\<** `IKModifier3D<class_IKModifier3D>` **\<** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A `SkeletonModifier3D<class_SkeletonModifier3D>` for aligning bones along a `Path3D<class_Path3D>`.

classref-introduction-group

## Description

A `SkeletonModifier3D<class_SkeletonModifier3D>` for aligning bones along a `Path3D<class_Path3D>`. The smoothness of the fitting depends on the `Curve3D.bake_interval<class_Curve3D_property_bake_interval>`.

If you want the `Path3D<class_Path3D>` to attach to a specific bone, it is recommended to place a `ModifierBoneTarget3D<class_ModifierBoneTarget3D>` before the **SplineIK3D** in the `SkeletonModifier3D<class_SkeletonModifier3D>` list (children of the `Skeleton3D<class_Skeleton3D>`), and then place a `Path3D<class_Path3D>` as the `ModifierBoneTarget3D<class_ModifierBoneTarget3D>`'s child.

Bone twist is determined based on the `Curve3D.get_point_tilt()<class_Curve3D_method_get_point_tilt>`.

If the root bone joint and the start point of the `Curve3D<class_Curve3D>` are separated, it assumes that there is a linear line segment between them. This means that the vector pointing toward the start point of the `Curve3D<class_Curve3D>` takes precedence over the shortest intersection point along the `Curve3D<class_Curve3D>`.

If the end bone joint exceeds the path length, it is bent as close as possible to the end point of the `Curve3D<class_Curve3D>`.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **setting_count** = `0` `🔗<class_SplineIK3D_property_setting_count>`

classref-property-setget

- `void (No return value.)` **set_setting_count**(value: `int<class_int>`)
- `int<class_int>` **get_setting_count**()

The number of settings.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`NodePath<class_NodePath>` **get_path_3d**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SplineIK3D_method_get_path_3d>`

Returns the node path of the `Path3D<class_Path3D>` which is describing the path.

classref-item-separator

classref-method

`int<class_int>` **get_tilt_fade_in**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SplineIK3D_method_get_tilt_fade_in>`

Returns the tilt interpolation method used between the root bone and the start point of the `Curve3D<class_Curve3D>` when they are apart. See also `set_tilt_fade_in()<class_SplineIK3D_method_set_tilt_fade_in>`.

classref-item-separator

classref-method

`int<class_int>` **get_tilt_fade_out**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SplineIK3D_method_get_tilt_fade_out>`

Returns the tilt interpolation method used between the end bone and the end point of the `Curve3D<class_Curve3D>` when they are apart. See also `set_tilt_fade_out()<class_SplineIK3D_method_set_tilt_fade_out>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_tilt_enabled**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SplineIK3D_method_is_tilt_enabled>`

Returns if the tilt property of the `Curve3D<class_Curve3D>` affects the bone twist.

classref-item-separator

classref-method

`void (No return value.)` **set_path_3d**(index: `int<class_int>`, path_3d: `NodePath<class_NodePath>`) `🔗<class_SplineIK3D_method_set_path_3d>`

Sets the node path of the `Path3D<class_Path3D>` which is describing the path.

classref-item-separator

classref-method

`void (No return value.)` **set_tilt_enabled**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_SplineIK3D_method_set_tilt_enabled>`

Sets if the tilt property of the `Curve3D<class_Curve3D>` should affect the bone twist.

classref-item-separator

classref-method

`void (No return value.)` **set_tilt_fade_in**(index: `int<class_int>`, size: `int<class_int>`) `🔗<class_SplineIK3D_method_set_tilt_fade_in>`

If `size` is greater than `0`, the tilt is interpolated between `size` start bones from the start point of the `Curve3D<class_Curve3D>` when they are apart.

If `size` is equal `0`, the tilts between the root bone head and the start point of the `Curve3D<class_Curve3D>` are unified with a tilt of the start point of the `Curve3D<class_Curve3D>`.

If `size` is less than `0`, the tilts between the root bone and the start point of the `Curve3D<class_Curve3D>` are `0.0`.

classref-item-separator

classref-method

`void (No return value.)` **set_tilt_fade_out**(index: `int<class_int>`, size: `int<class_int>`) `🔗<class_SplineIK3D_method_set_tilt_fade_out>`

If `size` is greater than `0`, the tilt is interpolated between `size` end bones from the end point of the `Curve3D<class_Curve3D>` when they are apart.

If `size` is equal `0`, the tilts between the end bone tail and the end point of the `Curve3D<class_Curve3D>` are unified with a tilt of the end point of the `Curve3D<class_Curve3D>`.

If `size` is less than `0`, the tilts between the end bone and the end point of the `Curve3D<class_Curve3D>` are `0.0`.