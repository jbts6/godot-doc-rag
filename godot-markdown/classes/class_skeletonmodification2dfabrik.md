github_url
hide

# SkeletonModification2DFABRIK

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `SkeletonModification2D<class_SkeletonModification2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A modification that uses FABRIK to manipulate a series of `Bone2D<class_Bone2D>` nodes to reach a target.

classref-introduction-group

## Description

This `SkeletonModification2D<class_SkeletonModification2D>` uses an algorithm called Forward And Backward Reaching Inverse Kinematics, or FABRIK, to rotate a bone chain so that it reaches a target.

FABRIK works by knowing the positions and lengths of a series of bones, typically called a "bone chain". It first starts by running a forward pass, which places the final bone at the target's position. Then all other bones are moved towards the tip bone, so they stay at the defined bone length away. Then a backwards pass is performed, where the root/first bone in the FABRIK chain is placed back at the origin. Then all other bones are moved so they stay at the defined bone length away. This positions the bone chain so that it reaches the target when possible, but all of the bones stay the correct length away from each other.

Because of how FABRIK works, it often gives more natural results than those seen in `SkeletonModification2DCCDIK<class_SkeletonModification2DCCDIK>`.

**Note:** The FABRIK modifier has `fabrik_joints`, which are the data objects that hold the data for each joint in the FABRIK chain. This is different from `Bone2D<class_Bone2D>` nodes! FABRIK joints hold the data needed for each `Bone2D<class_Bone2D>` in the bone chain used by FABRIK.

To help control how the FABRIK joints move, a magnet vector can be passed, which can nudge the bones in a certain direction prior to solving, giving a level of control over the final result.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **fabrik_data_chain_length** = `0` `🔗<class_SkeletonModification2DFABRIK_property_fabrik_data_chain_length>`

classref-property-setget

- `void (No return value.)` **set_fabrik_data_chain_length**(value: `int<class_int>`)
- `int<class_int>` **get_fabrik_data_chain_length**()

The number of FABRIK joints in the FABRIK modification.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **target_nodepath** = `NodePath("")` `🔗<class_SkeletonModification2DFABRIK_property_target_nodepath>`

classref-property-setget

- `void (No return value.)` **set_target_node**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_target_node**()

The NodePath to the node that is the target for the FABRIK modification. This node is what the FABRIK chain will attempt to rotate the bone chain to.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`NodePath<class_NodePath>` **get_fabrik_joint_bone2d_node**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_bone2d_node>`

Returns the `Bone2D<class_Bone2D>` node assigned to the FABRIK joint at `joint_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_fabrik_joint_bone_index**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_bone_index>`

Returns the index of the `Bone2D<class_Bone2D>` node assigned to the FABRIK joint at `joint_idx`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_fabrik_joint_magnet_position**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_magnet_position>`

Returns the magnet position vector for the joint at `joint_idx`.

classref-item-separator

classref-method

`bool<class_bool>` **get_fabrik_joint_use_target_rotation**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_use_target_rotation>`

Returns whether the joint is using the target's rotation rather than allowing FABRIK to rotate the joint. This option only applies to the tip/final joint in the chain.

classref-item-separator

classref-method

`void (No return value.)` **set_fabrik_joint_bone2d_node**(joint_idx: `int<class_int>`, bone2d_nodepath: `NodePath<class_NodePath>`) `🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_bone2d_node>`

Sets the `Bone2D<class_Bone2D>` node assigned to the FABRIK joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_fabrik_joint_bone_index**(joint_idx: `int<class_int>`, bone_idx: `int<class_int>`) `🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_bone_index>`

Sets the bone index, `bone_idx`, of the FABRIK joint at `joint_idx`. When possible, this will also update the `bone2d_node` of the FABRIK joint based on data provided by the linked skeleton.

classref-item-separator

classref-method

`void (No return value.)` **set_fabrik_joint_magnet_position**(joint_idx: `int<class_int>`, magnet_position: `Vector2<class_Vector2>`) `🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_magnet_position>`

Sets the magnet position vector for the joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_fabrik_joint_use_target_rotation**(joint_idx: `int<class_int>`, use_target_rotation: `bool<class_bool>`) `🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_use_target_rotation>`

Sets whether the joint at `joint_idx` will use the target node's rotation rather than letting FABRIK rotate the node.

**Note:** This option only works for the tip/final joint in the chain. For all other nodes, this option will be ignored.