github_url
hide

# BoneConstraint3D

**Inherits:** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `AimModifier3D<class_AimModifier3D>`, `ConvertTransformModifier3D<class_ConvertTransformModifier3D>`, `CopyTransformModifier3D<class_CopyTransformModifier3D>`

A node that may modify Skeleton3D's bone with associating the two bones.

classref-introduction-group

## Description

Base class of `SkeletonModifier3D<class_SkeletonModifier3D>` that modifies the bone set in `set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>` based on the transform of the bone retrieved by `get_reference_bone()<class_BoneConstraint3D_method_get_reference_bone>`.

**Note:** Most methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/amount`).

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ReferenceType**: `🔗<enum_BoneConstraint3D_ReferenceType>`

classref-enumeration-constant

`ReferenceType<enum_BoneConstraint3D_ReferenceType>` **REFERENCE_TYPE_BONE** = `0`

The reference target is a bone. In this case, the reference target spaces is local space.

classref-enumeration-constant

`ReferenceType<enum_BoneConstraint3D_ReferenceType>` **REFERENCE_TYPE_NODE** = `1`

The reference target is a `Node3D<class_Node3D>`. In this case, the reference target spaces is model space.

In other words, the reference target's coordinates are treated as if it were placed directly under `Skeleton3D<class_Skeleton3D>` which parent of the **BoneConstraint3D**.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_setting**() `🔗<class_BoneConstraint3D_method_clear_setting>`

Clear all settings.

classref-item-separator

classref-method

`float<class_float>` **get_amount**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_amount>`

Returns the apply amount of the setting at `index`.

classref-item-separator

classref-method

`int<class_int>` **get_apply_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_apply_bone>`

Returns the apply bone of the setting at `index`. This bone will be modified.

classref-item-separator

classref-method

`String<class_String>` **get_apply_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_apply_bone_name>`

Returns the apply bone name of the setting at `index`. This bone will be modified.

classref-item-separator

classref-method

`int<class_int>` **get_reference_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_reference_bone>`

Returns the reference bone of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

classref-item-separator

classref-method

`String<class_String>` **get_reference_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_reference_bone_name>`

Returns the reference bone name of the setting at `index`.

This bone will be only referenced and not modified by this modifier.

classref-item-separator

classref-method

`NodePath<class_NodePath>` **get_reference_node**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_reference_node>`

Returns the reference node path of the setting at `index`.

This node will be only referenced and not modified by this modifier.

classref-item-separator

classref-method

`ReferenceType<enum_BoneConstraint3D_ReferenceType>` **get_reference_type**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_reference_type>`

Returns the reference target type of the setting at `index`. See also `ReferenceType<enum_BoneConstraint3D_ReferenceType>`.

classref-item-separator

classref-method

`int<class_int>` **get_setting_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneConstraint3D_method_get_setting_count>`

Returns the number of settings in the modifier.

classref-item-separator

classref-method

`void (No return value.)` **set_amount**(index: `int<class_int>`, amount: `float<class_float>`) `🔗<class_BoneConstraint3D_method_set_amount>`

Sets the apply amount of the setting at `index` to `amount`.

classref-item-separator

classref-method

`void (No return value.)` **set_apply_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_BoneConstraint3D_method_set_apply_bone>`

Sets the apply bone of the setting at `index` to `bone`. This bone will be modified.

classref-item-separator

classref-method

`void (No return value.)` **set_apply_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_BoneConstraint3D_method_set_apply_bone_name>`

Sets the apply bone of the setting at `index` to `bone_name`. This bone will be modified.

classref-item-separator

classref-method

`void (No return value.)` **set_reference_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_BoneConstraint3D_method_set_reference_bone>`

Sets the reference bone of the setting at `index` to `bone`.

This bone will be only referenced and not modified by this modifier.

classref-item-separator

classref-method

`void (No return value.)` **set_reference_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_BoneConstraint3D_method_set_reference_bone_name>`

Sets the reference bone of the setting at `index` to `bone_name`.

This bone will be only referenced and not modified by this modifier.

classref-item-separator

classref-method

`void (No return value.)` **set_reference_node**(index: `int<class_int>`, node: `NodePath<class_NodePath>`) `🔗<class_BoneConstraint3D_method_set_reference_node>`

Sets the reference node path of the setting at `index` to `node`.

This node will be only referenced and not modified by this modifier.

classref-item-separator

classref-method

`void (No return value.)` **set_reference_type**(index: `int<class_int>`, type: `ReferenceType<enum_BoneConstraint3D_ReferenceType>`) `🔗<class_BoneConstraint3D_method_set_reference_type>`

Sets the reference target type of the setting at `index` to `type`. See also `ReferenceType<enum_BoneConstraint3D_ReferenceType>`.

classref-item-separator

classref-method

`void (No return value.)` **set_setting_count**(count: `int<class_int>`) `🔗<class_BoneConstraint3D_method_set_setting_count>`

Sets the number of settings in the modifier.