github_url
hide

# SkeletonModification2DTwoBoneIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `SkeletonModification2D<class_SkeletonModification2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A modification that rotates two bones using the law of cosines to reach the target.

classref-introduction-group

## Description

This `SkeletonModification2D<class_SkeletonModification2D>` uses an algorithm typically called TwoBoneIK. This algorithm works by leveraging the law of cosines and the lengths of the bones to figure out what rotation the bones currently have, and what rotation they need to make a complete triangle, where the first bone, the second bone, and the target form the three vertices of the triangle. Because the algorithm works by making a triangle, it can only operate on two bones.

TwoBoneIK is great for arms, legs, and really any joints that can be represented by just two bones that bend to reach a target. This solver is more lightweight than `SkeletonModification2DFABRIK<class_SkeletonModification2DFABRIK>`, but gives similar, natural looking results.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **flip_bend_direction** = `false` `🔗<class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction>`

classref-property-setget

- `void (No return value.)` **set_flip_bend_direction**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_flip_bend_direction**()

If `true`, the bones in the modification will bend outward as opposed to inwards when contracting. If `false`, the bones will bend inwards when contracting.

classref-item-separator

classref-property

`float<class_float>` **target_maximum_distance** = `0.0` `🔗<class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance>`

classref-property-setget

- `void (No return value.)` **set_target_maximum_distance**(value: `float<class_float>`)
- `float<class_float>` **get_target_maximum_distance**()

The maximum distance the target can be at. If the target is farther than this distance, the modification will solve as if it's at this maximum distance. When set to `0`, the modification will solve without distance constraints.

classref-item-separator

classref-property

`float<class_float>` **target_minimum_distance** = `0.0` `🔗<class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance>`

classref-property-setget

- `void (No return value.)` **set_target_minimum_distance**(value: `float<class_float>`)
- `float<class_float>` **get_target_minimum_distance**()

The minimum distance the target can be at. If the target is closer than this distance, the modification will solve as if it's at this minimum distance. When set to `0`, the modification will solve without distance constraints.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **target_nodepath** = `NodePath("")` `🔗<class_SkeletonModification2DTwoBoneIK_property_target_nodepath>`

classref-property-setget

- `void (No return value.)` **set_target_node**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_target_node**()

The NodePath to the node that is the target for the TwoBoneIK modification. This node is what the modification will use when bending the `Bone2D<class_Bone2D>` nodes.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`NodePath<class_NodePath>` **get_joint_one_bone2d_node**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node>`

Returns the `Bone2D<class_Bone2D>` node that is being used as the first bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`int<class_int>` **get_joint_one_bone_idx**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx>`

Returns the index of the `Bone2D<class_Bone2D>` node that is being used as the first bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`NodePath<class_NodePath>` **get_joint_two_bone2d_node**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node>`

Returns the `Bone2D<class_Bone2D>` node that is being used as the second bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`int<class_int>` **get_joint_two_bone_idx**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx>`

Returns the index of the `Bone2D<class_Bone2D>` node that is being used as the second bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`void (No return value.)` **set_joint_one_bone2d_node**(bone2d_node: `NodePath<class_NodePath>`) `🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node>`

Sets the `Bone2D<class_Bone2D>` node that is being used as the first bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`void (No return value.)` **set_joint_one_bone_idx**(bone_idx: `int<class_int>`) `🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx>`

Sets the index of the `Bone2D<class_Bone2D>` node that is being used as the first bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`void (No return value.)` **set_joint_two_bone2d_node**(bone2d_node: `NodePath<class_NodePath>`) `🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node>`

Sets the `Bone2D<class_Bone2D>` node that is being used as the second bone in the TwoBoneIK modification.

classref-item-separator

classref-method

`void (No return value.)` **set_joint_two_bone_idx**(bone_idx: `int<class_int>`) `🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx>`

Sets the index of the `Bone2D<class_Bone2D>` node that is being used as the second bone in the TwoBoneIK modification.