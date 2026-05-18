github_url
hide

# TwoBoneIK3D

**Inherits:** `IKModifier3D<class_IKModifier3D>` **\<** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Rotation based intersection of two circles inverse kinematics solver.

classref-introduction-group

## Description

This `IKModifier3D<class_IKModifier3D>` requires a pole target. It provides deterministic results by constructing a plane from each joint and pole target and finding the intersection of two circles (disks in 3D).

This IK can handle twist by setting the pole direction. If there are more than one bone between each set bone, their rotations are ignored, and the straight line connecting the root-middle and middle-end joints are treated as virtual bones.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **setting_count** = `0` `🔗<class_TwoBoneIK3D_property_setting_count>`

classref-property-setget

- `void (No return value.)` **set_setting_count**(value: `int<class_int>`)
- `int<class_int>` **get_setting_count**()

The number of settings.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_end_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_end_bone>`

Returns the end bone index.

classref-item-separator

classref-method

`BoneDirection<enum_SkeletonModifier3D_BoneDirection>` **get_end_bone_direction**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_end_bone_direction>`

Returns the end bone's tail direction when `is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`float<class_float>` **get_end_bone_length**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_end_bone_length>`

Returns the end bone tail length of the bone chain when `is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`String<class_String>` **get_end_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_end_bone_name>`

Returns the end bone name.

classref-item-separator

classref-method

`int<class_int>` **get_middle_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_middle_bone>`

Returns the middle bone index.

classref-item-separator

classref-method

`String<class_String>` **get_middle_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_middle_bone_name>`

Returns the middle bone name.

classref-item-separator

classref-method

`SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>` **get_pole_direction**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_pole_direction>`

Returns the pole direction.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_pole_direction_vector**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_pole_direction_vector>`

Returns the pole direction vector.

If `get_pole_direction()<class_TwoBoneIK3D_method_get_pole_direction>` is `SkeletonModifier3D.SECONDARY_DIRECTION_NONE<class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE>`, this method returns `Vector3(0, 0, 0)`.

classref-item-separator

classref-method

`NodePath<class_NodePath>` **get_pole_node**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_pole_node>`

Returns the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

classref-item-separator

classref-method

`int<class_int>` **get_root_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_root_bone>`

Returns the root bone index.

classref-item-separator

classref-method

`String<class_String>` **get_root_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_root_bone_name>`

Returns the root bone name.

classref-item-separator

classref-method

`NodePath<class_NodePath>` **get_target_node**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_get_target_node>`

Returns the target node that the end bone is trying to reach.

classref-item-separator

classref-method

`bool<class_bool>` **is_end_bone_extended**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_is_end_bone_extended>`

Returns `true` if the end bone is extended to have a tail.

classref-item-separator

classref-method

`bool<class_bool>` **is_using_virtual_end**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TwoBoneIK3D_method_is_using_virtual_end>`

Returns `true` if the end bone is extended from the middle bone as a virtual bone.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_TwoBoneIK3D_method_set_end_bone>`

Sets the end bone index.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone_direction**(index: `int<class_int>`, bone_direction: `BoneDirection<enum_SkeletonModifier3D_BoneDirection>`) `🔗<class_TwoBoneIK3D_method_set_end_bone_direction>`

Sets the end bone tail direction when `is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone_length**(index: `int<class_int>`, length: `float<class_float>`) `🔗<class_TwoBoneIK3D_method_set_end_bone_length>`

Sets the end bone tail length when `is_end_bone_extended()<class_TwoBoneIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_TwoBoneIK3D_method_set_end_bone_name>`

Sets the end bone name.

**Note:** The end bone must be a child of the middle bone.

classref-item-separator

classref-method

`void (No return value.)` **set_extend_end_bone**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_TwoBoneIK3D_method_set_extend_end_bone>`

If `enabled` is `true`, the end bone is extended to have a tail.

classref-item-separator

classref-method

`void (No return value.)` **set_middle_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_TwoBoneIK3D_method_set_middle_bone>`

Sets the middle bone index.

classref-item-separator

classref-method

`void (No return value.)` **set_middle_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_TwoBoneIK3D_method_set_middle_bone_name>`

Sets the middle bone name.

**Note:** The middle bone must be a child of the root bone.

classref-item-separator

classref-method

`void (No return value.)` **set_pole_direction**(index: `int<class_int>`, direction: `SecondaryDirection<enum_SkeletonModifier3D_SecondaryDirection>`) `🔗<class_TwoBoneIK3D_method_set_pole_direction>`

Sets the pole direction.

The pole is on the middle bone and will direct to the pole target.

The rotation axis is a vector that is orthogonal to this and the forward vector.

**Note:** The pole direction and the forward vector shouldn't be colinear to avoid unintended rotation.

classref-item-separator

classref-method

`void (No return value.)` **set_pole_direction_vector**(index: `int<class_int>`, vector: `Vector3<class_Vector3>`) `🔗<class_TwoBoneIK3D_method_set_pole_direction_vector>`

Sets the pole direction vector.

This vector is normalized by an internal process.

If the vector length is `0`, it is considered synonymous with `SkeletonModifier3D.SECONDARY_DIRECTION_NONE<class_SkeletonModifier3D_constant_SECONDARY_DIRECTION_NONE>`.

classref-item-separator

classref-method

`void (No return value.)` **set_pole_node**(index: `int<class_int>`, pole_node: `NodePath<class_NodePath>`) `🔗<class_TwoBoneIK3D_method_set_pole_node>`

Sets the pole target node that constructs a plane which the joints are all on and the pole is trying to direct.

classref-item-separator

classref-method

`void (No return value.)` **set_root_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_TwoBoneIK3D_method_set_root_bone>`

Sets the root bone index.

classref-item-separator

classref-method

`void (No return value.)` **set_root_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_TwoBoneIK3D_method_set_root_bone_name>`

Sets the root bone name.

classref-item-separator

classref-method

`void (No return value.)` **set_target_node**(index: `int<class_int>`, target_node: `NodePath<class_NodePath>`) `🔗<class_TwoBoneIK3D_method_set_target_node>`

Sets the target node that the end bone is trying to reach.

classref-item-separator

classref-method

`void (No return value.)` **set_use_virtual_end**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_TwoBoneIK3D_method_set_use_virtual_end>`

If `enabled` is `true`, the end bone is extended from the middle bone as a virtual bone.