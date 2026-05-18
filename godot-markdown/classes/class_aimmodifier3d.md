github_url
hide

# AimModifier3D

**Inherits:** `BoneConstraint3D<class_BoneConstraint3D>` **\<** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

The **AimModifier3D** rotates a bone to look at a reference bone.

classref-introduction-group

## Description

This is a simple version of `LookAtModifier3D<class_LookAtModifier3D>` that only allows bone to the reference without advanced options such as angle limitation or time-based interpolation.

The feature is simplified, but instead it is implemented with smooth tracking without euler, see `set_use_euler()<class_AimModifier3D_method_set_use_euler>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **setting_count** = `0` `🔗<class_AimModifier3D_property_setting_count>`

classref-property-setget

- `void (No return value.)` **set_setting_count**(value: `int<class_int>`)
- `int<class_int>` **get_setting_count**()

The number of settings in the modifier.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>` **get_forward_axis**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AimModifier3D_method_get_forward_axis>`

Returns the forward axis of the bone.

classref-item-separator

classref-method

`Axis<enum_Vector3_Axis>` **get_primary_rotation_axis**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AimModifier3D_method_get_primary_rotation_axis>`

Returns the axis of the first rotation. It is enabled only if `is_using_euler()<class_AimModifier3D_method_is_using_euler>` is `true`.

classref-item-separator

classref-method

`bool<class_bool>` **is_relative**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AimModifier3D_method_is_relative>`

Returns `true` if the relative option is enabled in the setting at `index`.

classref-item-separator

classref-method

`bool<class_bool>` **is_using_euler**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AimModifier3D_method_is_using_euler>`

Returns `true` if it provides rotation with using euler.

classref-item-separator

classref-method

`bool<class_bool>` **is_using_secondary_rotation**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AimModifier3D_method_is_using_secondary_rotation>`

Returns `true` if it provides rotation by two axes. It is enabled only if `is_using_euler()<class_AimModifier3D_method_is_using_euler>` is `true`.

classref-item-separator

classref-method

`void (No return value.)` **set_forward_axis**(index: `int<class_int>`, axis: `BoneAxis<enum_SkeletonModifier3D_BoneAxis>`) `🔗<class_AimModifier3D_method_set_forward_axis>`

Sets the forward axis of the bone.

classref-item-separator

classref-method

`void (No return value.)` **set_primary_rotation_axis**(index: `int<class_int>`, axis: `Axis<enum_Vector3_Axis>`) `🔗<class_AimModifier3D_method_set_primary_rotation_axis>`

Sets the axis of the first rotation. It is enabled only if `is_using_euler()<class_AimModifier3D_method_is_using_euler>` is `true`.

classref-item-separator

classref-method

`void (No return value.)` **set_relative**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_AimModifier3D_method_set_relative>`

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the rotation is applied relative to the pose.

If sets `enabled` to `false`, the rotation is applied relative to the rest. It means to replace the current pose with the **AimModifier3D**'s result.

classref-item-separator

classref-method

`void (No return value.)` **set_use_euler**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_AimModifier3D_method_set_use_euler>`

If sets `enabled` to `true`, it provides rotation with using euler.

If sets `enabled` to `false`, it provides rotation with using rotation by arc generated from the forward axis vector and the vector toward the reference.

classref-item-separator

classref-method

`void (No return value.)` **set_use_secondary_rotation**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_AimModifier3D_method_set_use_secondary_rotation>`

If sets `enabled` to `true`, it provides rotation by two axes. It is enabled only if `is_using_euler()<class_AimModifier3D_method_is_using_euler>` is `true`.