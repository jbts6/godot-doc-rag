github_url
hide

# ChainIK3D

**Inherits:** `IKModifier3D<class_IKModifier3D>` **\<** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `IterateIK3D<class_IterateIK3D>`, `SplineIK3D<class_SplineIK3D>`

A `SkeletonModifier3D<class_SkeletonModifier3D>` to apply inverse kinematics to bone chains containing an arbitrary number of bones.

classref-introduction-group

## Description

Base class of `SkeletonModifier3D<class_SkeletonModifier3D>` that automatically generates a joint list from the bones between the root bone and the end bone.

**Note:** All the methods in this class take an `index` parameter. This parameter specifies which setting list entry to return if the IK has multiple entries (e.g. `settings/<index>/root_bone_name`).

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_end_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_end_bone>`

Returns the end bone index of the bone chain.

classref-item-separator

classref-method

`BoneDirection<enum_SkeletonModifier3D_BoneDirection>` **get_end_bone_direction**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_end_bone_direction>`

Returns the tail direction of the end bone of the bone chain when `is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`float<class_float>` **get_end_bone_length**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_end_bone_length>`

Returns the end bone tail length of the bone chain when `is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`String<class_String>` **get_end_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_end_bone_name>`

Returns the end bone name of the bone chain.

classref-item-separator

classref-method

`int<class_int>` **get_joint_bone**(index: `int<class_int>`, joint: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_joint_bone>`

Returns the bone index at `joint` in the bone chain's joint list.

classref-item-separator

classref-method

`String<class_String>` **get_joint_bone_name**(index: `int<class_int>`, joint: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_joint_bone_name>`

Returns the bone name at `joint` in the bone chain's joint list.

classref-item-separator

classref-method

`int<class_int>` **get_joint_count**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_joint_count>`

Returns the joint count of the bone chain's joint list.

classref-item-separator

classref-method

`int<class_int>` **get_root_bone**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_root_bone>`

Returns the root bone index of the bone chain.

classref-item-separator

classref-method

`String<class_String>` **get_root_bone_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_get_root_bone_name>`

Returns the root bone name of the bone chain.

classref-item-separator

classref-method

`bool<class_bool>` **is_end_bone_extended**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ChainIK3D_method_is_end_bone_extended>`

Returns `true` if the end bone is extended to have a tail.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_ChainIK3D_method_set_end_bone>`

Sets the end bone index of the bone chain.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone_direction**(index: `int<class_int>`, bone_direction: `BoneDirection<enum_SkeletonModifier3D_BoneDirection>`) `🔗<class_ChainIK3D_method_set_end_bone_direction>`

Sets the end bone tail direction of the bone chain when `is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone_length**(index: `int<class_int>`, length: `float<class_float>`) `🔗<class_ChainIK3D_method_set_end_bone_length>`

Sets the end bone tail length of the bone chain when `is_end_bone_extended()<class_ChainIK3D_method_is_end_bone_extended>` is `true`.

classref-item-separator

classref-method

`void (No return value.)` **set_end_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_ChainIK3D_method_set_end_bone_name>`

Sets the end bone name of the bone chain.

**Note:** The end bone must be the root bone or a child of the root bone. If they are the same, the tail must be extended by `set_extend_end_bone()<class_ChainIK3D_method_set_extend_end_bone>` to modify the bone.

classref-item-separator

classref-method

`void (No return value.)` **set_extend_end_bone**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_ChainIK3D_method_set_extend_end_bone>`

If `enabled` is `true`, the end bone is extended to have a tail.

The extended tail config is allocated to the last element in the joint list. In other words, if you set `enabled` to `false`, the config of the last element in the joint list has no effect in the simulated result.

classref-item-separator

classref-method

`void (No return value.)` **set_root_bone**(index: `int<class_int>`, bone: `int<class_int>`) `🔗<class_ChainIK3D_method_set_root_bone>`

Sets the root bone index of the bone chain.

classref-item-separator

classref-method

`void (No return value.)` **set_root_bone_name**(index: `int<class_int>`, bone_name: `String<class_String>`) `🔗<class_ChainIK3D_method_set_root_bone_name>`

Sets the root bone name of the bone chain.