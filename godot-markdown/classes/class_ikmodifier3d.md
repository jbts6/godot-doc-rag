github_url
hide

# IKModifier3D

**Inherits:** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `ChainIK3D<class_ChainIK3D>`, `TwoBoneIK3D<class_TwoBoneIK3D>`

A node for inverse kinematics which may modify more than one bone.

classref-introduction-group

## Description

Base class of `SkeletonModifier3D<class_SkeletonModifier3D>`s that has some joint lists and applies inverse kinematics. This class has some structs, enums, and helper methods which are useful to solve inverse kinematics.

classref-introduction-group

## Tutorials

- [Inverse Kinematics Returns to Godot 4.6 - IKModifier3D](https://godotengine.org/article/inverse-kinematics-returns-to-godot-4-6/#ikmodifier3d-and-7-child-classes)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **mutable_bone_axes** = `true` `🔗<class_IKModifier3D_property_mutable_bone_axes>`

classref-property-setget

- `void (No return value.)` **set_mutable_bone_axes**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_bone_axes_mutable**()

If `true`, the solver retrieves the bone axis from the bone pose every frame.

If `false`, the solver retrieves the bone axis from the bone rest and caches it, which increases performance slightly, but position changes in the bone pose made before processing this **IKModifier3D** are ignored.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_settings**() `🔗<class_IKModifier3D_method_clear_settings>`

Clears all settings.

classref-item-separator

classref-method

`int<class_int>` **get_setting_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_IKModifier3D_method_get_setting_count>`

Returns the number of settings.

classref-item-separator

classref-method

`void (No return value.)` **reset**() `🔗<class_IKModifier3D_method_reset>`

Resets a state with respect to the current bone pose.

classref-item-separator

classref-method

`void (No return value.)` **set_setting_count**(count: `int<class_int>`) `🔗<class_IKModifier3D_method_set_setting_count>`

Sets the number of settings.