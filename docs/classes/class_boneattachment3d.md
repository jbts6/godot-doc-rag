github_url
hide

# BoneAttachment3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

А node that dynamically copies or overrides the 3D transform of a bone in its parent `Skeleton3D<class_Skeleton3D>`.

classref-introduction-group

## Description

This node selects a bone in a `Skeleton3D<class_Skeleton3D>` and attaches to it. This means that the **BoneAttachment3D** node will either dynamically copy or override the 3D transform of the selected bone.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **bone_idx** = `-1` `🔗<class_BoneAttachment3D_property_bone_idx>`

classref-property-setget

- `void (No return value.)` **set_bone_idx**(value: `int<class_int>`)
- `int<class_int>` **get_bone_idx**()

The index of the attached bone.

classref-item-separator

classref-property

`String<class_String>` **bone_name** = `""` `🔗<class_BoneAttachment3D_property_bone_name>`

classref-property-setget

- `void (No return value.)` **set_bone_name**(value: `String<class_String>`)
- `String<class_String>` **get_bone_name**()

The name of the attached bone.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **external_skeleton** `🔗<class_BoneAttachment3D_property_external_skeleton>`

classref-property-setget

- `void (No return value.)` **set_external_skeleton**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_external_skeleton**()

The `NodePath<class_NodePath>` to the external `Skeleton3D<class_Skeleton3D>` node.

classref-item-separator

classref-property

`bool<class_bool>` **override_pose** = `false` `🔗<class_BoneAttachment3D_property_override_pose>`

classref-property-setget

- `void (No return value.)` **set_override_pose**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_override_pose**()

Whether the **BoneAttachment3D** node will override the bone pose of the bone it is attached to. When set to `true`, the **BoneAttachment3D** node can change the pose of the bone. When set to `false`, the **BoneAttachment3D** will always be set to the bone's transform.

**Note:** This override performs interruptively in the skeleton update process using signals due to the old design. It may cause unintended behavior when used at the same time with `SkeletonModifier3D<class_SkeletonModifier3D>`.

classref-item-separator

classref-property

`bool<class_bool>` **use_external_skeleton** = `false` `🔗<class_BoneAttachment3D_property_use_external_skeleton>`

classref-property-setget

- `void (No return value.)` **set_use_external_skeleton**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_external_skeleton**()

Whether the **BoneAttachment3D** node will use an external `Skeleton3D<class_Skeleton3D>` node rather than attempting to use its parent node as the `Skeleton3D<class_Skeleton3D>`. When set to `true`, the **BoneAttachment3D** node will use the external `Skeleton3D<class_Skeleton3D>` node set in `external_skeleton<class_BoneAttachment3D_property_external_skeleton>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Skeleton3D<class_Skeleton3D>` **get_skeleton**() `🔗<class_BoneAttachment3D_method_get_skeleton>`

Returns the parent or external `Skeleton3D<class_Skeleton3D>` node if it exists, otherwise returns `null`.

classref-item-separator

classref-method

`void (No return value.)` **on_skeleton_update**() `🔗<class_BoneAttachment3D_method_on_skeleton_update>`

A function that is called automatically when the `Skeleton3D<class_Skeleton3D>` is updated. This function is where the **BoneAttachment3D** node updates its position so it is correctly bound when it is *not* set to override the bone pose.