github_url
hide

# SkeletonModification2DLookAt

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `SkeletonModification2D<class_SkeletonModification2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A modification that rotates a `Bone2D<class_Bone2D>` node to look at a target.

classref-introduction-group

## Description

This `SkeletonModification2D<class_SkeletonModification2D>` rotates a bone to look a target. This is extremely helpful for moving character's head to look at the player, rotating a turret to look at a target, or any other case where you want to make a bone rotate towards something quickly and easily.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`NodePath<class_NodePath>` **bone2d_node** = `NodePath("")` `🔗<class_SkeletonModification2DLookAt_property_bone2d_node>`

classref-property-setget

- `void (No return value.)` **set_bone2d_node**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_bone2d_node**()

The `Bone2D<class_Bone2D>` node that the modification will operate on.

classref-item-separator

classref-property

`int<class_int>` **bone_index** = `-1` `🔗<class_SkeletonModification2DLookAt_property_bone_index>`

classref-property-setget

- `void (No return value.)` **set_bone_index**(value: `int<class_int>`)
- `int<class_int>` **get_bone_index**()

The index of the `Bone2D<class_Bone2D>` node that the modification will operate on.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **target_nodepath** = `NodePath("")` `🔗<class_SkeletonModification2DLookAt_property_target_nodepath>`

classref-property-setget

- `void (No return value.)` **set_target_node**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_target_node**()

The NodePath to the node that is the target for the LookAt modification. This node is what the modification will rotate the `Bone2D<class_Bone2D>` to.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_additional_rotation**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DLookAt_method_get_additional_rotation>`

Returns the amount of additional rotation that is applied after the LookAt modification executes.

classref-item-separator

classref-method

`bool<class_bool>` **get_constraint_angle_invert**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DLookAt_method_get_constraint_angle_invert>`

Returns whether the constraints to this modification are inverted or not.

classref-item-separator

classref-method

`float<class_float>` **get_constraint_angle_max**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DLookAt_method_get_constraint_angle_max>`

Returns the constraint's maximum allowed angle.

classref-item-separator

classref-method

`float<class_float>` **get_constraint_angle_min**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DLookAt_method_get_constraint_angle_min>`

Returns the constraint's minimum allowed angle.

classref-item-separator

classref-method

`bool<class_bool>` **get_enable_constraint**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DLookAt_method_get_enable_constraint>`

Returns `true` if the LookAt modification is using constraints.

classref-item-separator

classref-method

`void (No return value.)` **set_additional_rotation**(rotation: `float<class_float>`) `🔗<class_SkeletonModification2DLookAt_method_set_additional_rotation>`

Sets the amount of additional rotation that is to be applied after executing the modification. This allows for offsetting the results by the inputted rotation amount.

classref-item-separator

classref-method

`void (No return value.)` **set_constraint_angle_invert**(invert: `bool<class_bool>`) `🔗<class_SkeletonModification2DLookAt_method_set_constraint_angle_invert>`

When `true`, the modification will use an inverted joint constraint.

An inverted joint constraint only constraints the `Bone2D<class_Bone2D>` to the angles *outside of* the inputted minimum and maximum angles. For this reason, it is referred to as an inverted joint constraint, as it constraints the joint to the outside of the inputted values.

classref-item-separator

classref-method

`void (No return value.)` **set_constraint_angle_max**(angle_max: `float<class_float>`) `🔗<class_SkeletonModification2DLookAt_method_set_constraint_angle_max>`

Sets the constraint's maximum allowed angle.

classref-item-separator

classref-method

`void (No return value.)` **set_constraint_angle_min**(angle_min: `float<class_float>`) `🔗<class_SkeletonModification2DLookAt_method_set_constraint_angle_min>`

Sets the constraint's minimum allowed angle.

classref-item-separator

classref-method

`void (No return value.)` **set_enable_constraint**(enable_constraint: `bool<class_bool>`) `🔗<class_SkeletonModification2DLookAt_method_set_enable_constraint>`

Sets whether this modification will use constraints or not. When `true`, constraints will be applied when solving the LookAt modification.