github_url
hide

# Skeleton2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

The parent of a hierarchy of `Bone2D<class_Bone2D>`s, used to create a 2D skeletal animation.

classref-introduction-group

## Description

**Skeleton2D** parents a hierarchy of `Bone2D<class_Bone2D>` nodes. It holds a reference to each `Bone2D<class_Bone2D>`'s rest pose and acts as a single point of access to its bones.

To set up different types of inverse kinematics for the given Skeleton2D, a `SkeletonModificationStack2D<class_SkeletonModificationStack2D>` should be created. The inverse kinematics be applied by increasing `SkeletonModificationStack2D.modification_count<class_SkeletonModificationStack2D_property_modification_count>` and creating the desired number of modifications.

classref-introduction-group

## Tutorials

- `2D skeletons <../tutorials/animation/2d_skeletons>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**bone_setup_changed**() `🔗<class_Skeleton2D_signal_bone_setup_changed>`

Emitted when the `Bone2D<class_Bone2D>` setup attached to this skeletons changes. This is primarily used internally within the skeleton.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **execute_modifications**(delta: `float<class_float>`, execution_mode: `int<class_int>`) `🔗<class_Skeleton2D_method_execute_modifications>`

Executes all the modifications on the `SkeletonModificationStack2D<class_SkeletonModificationStack2D>`, if the Skeleton2D has one assigned.

classref-item-separator

classref-method

`Bone2D<class_Bone2D>` **get_bone**(idx: `int<class_int>`) `🔗<class_Skeleton2D_method_get_bone>`

Returns a `Bone2D<class_Bone2D>` from the node hierarchy parented by Skeleton2D. The object to return is identified by the parameter `idx`. Bones are indexed by descending the node hierarchy from top to bottom, adding the children of each branch before moving to the next sibling.

classref-item-separator

classref-method

`int<class_int>` **get_bone_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Skeleton2D_method_get_bone_count>`

Returns the number of `Bone2D<class_Bone2D>` nodes in the node hierarchy parented by Skeleton2D.

classref-item-separator

classref-method

`Transform2D<class_Transform2D>` **get_bone_local_pose_override**(bone_idx: `int<class_int>`) `🔗<class_Skeleton2D_method_get_bone_local_pose_override>`

Returns the local pose override transform for `bone_idx`.

classref-item-separator

classref-method

`SkeletonModificationStack2D<class_SkeletonModificationStack2D>` **get_modification_stack**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Skeleton2D_method_get_modification_stack>`

Returns the `SkeletonModificationStack2D<class_SkeletonModificationStack2D>` attached to this skeleton, if one exists.

classref-item-separator

classref-method

`RID<class_RID>` **get_skeleton**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Skeleton2D_method_get_skeleton>`

Returns the `RID<class_RID>` of a Skeleton2D instance.

classref-item-separator

classref-method

`void (No return value.)` **set_bone_local_pose_override**(bone_idx: `int<class_int>`, override_pose: `Transform2D<class_Transform2D>`, strength: `float<class_float>`, persistent: `bool<class_bool>`) `🔗<class_Skeleton2D_method_set_bone_local_pose_override>`

Sets the local pose transform, `override_pose`, for the bone at `bone_idx`.

`strength` is the interpolation strength that will be used when applying the pose, and `persistent` determines if the applied pose will remain.

**Note:** The pose transform needs to be a local transform relative to the `Bone2D<class_Bone2D>` node at `bone_idx`!

classref-item-separator

classref-method

`void (No return value.)` **set_modification_stack**(modification_stack: `SkeletonModificationStack2D<class_SkeletonModificationStack2D>`) `🔗<class_Skeleton2D_method_set_modification_stack>`

Sets the `SkeletonModificationStack2D<class_SkeletonModificationStack2D>` attached to this skeleton.