github_url
hide

# SkeletonModification2DPhysicalBones

**Experimental:** Physical bones may be changed in the future to perform the position update of `Bone2D<class_Bone2D>` on their own, without needing this resource.

**Inherits:** `SkeletonModification2D<class_SkeletonModification2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A modification that applies the transforms of `PhysicalBone2D<class_PhysicalBone2D>` nodes to `Bone2D<class_Bone2D>` nodes.

classref-introduction-group

## Description

This modification takes the transforms of `PhysicalBone2D<class_PhysicalBone2D>` nodes and applies them to `Bone2D<class_Bone2D>` nodes. This allows the `Bone2D<class_Bone2D>` nodes to react to physics thanks to the linked `PhysicalBone2D<class_PhysicalBone2D>` nodes.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **physical_bone_chain_length** = `0` `🔗<class_SkeletonModification2DPhysicalBones_property_physical_bone_chain_length>`

classref-property-setget

- `void (No return value.)` **set_physical_bone_chain_length**(value: `int<class_int>`)
- `int<class_int>` **get_physical_bone_chain_length**()

The number of `PhysicalBone2D<class_PhysicalBone2D>` nodes linked in this modification.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **fetch_physical_bones**() `🔗<class_SkeletonModification2DPhysicalBones_method_fetch_physical_bones>`

Empties the list of `PhysicalBone2D<class_PhysicalBone2D>` nodes and populates it with all `PhysicalBone2D<class_PhysicalBone2D>` nodes that are children of the `Skeleton2D<class_Skeleton2D>`.

classref-item-separator

classref-method

`NodePath<class_NodePath>` **get_physical_bone_node**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DPhysicalBones_method_get_physical_bone_node>`

Returns the `PhysicalBone2D<class_PhysicalBone2D>` node at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_physical_bone_node**(joint_idx: `int<class_int>`, physicalbone2d_node: `NodePath<class_NodePath>`) `🔗<class_SkeletonModification2DPhysicalBones_method_set_physical_bone_node>`

Sets the `PhysicalBone2D<class_PhysicalBone2D>` node at `joint_idx`.

**Note:** This is just the index used for this modification, not the bone index used in the `Skeleton2D<class_Skeleton2D>`.

classref-item-separator

classref-method

`void (No return value.)` **start_simulation**(bones: `Array<class_Array>`\[`StringName<class_StringName>`\] = \[\]) `🔗<class_SkeletonModification2DPhysicalBones_method_start_simulation>`

Tell the `PhysicalBone2D<class_PhysicalBone2D>` nodes to start simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only `PhysicalBone2D<class_PhysicalBone2D>` nodes with those names to start simulating.

classref-item-separator

classref-method

`void (No return value.)` **stop_simulation**(bones: `Array<class_Array>`\[`StringName<class_StringName>`\] = \[\]) `🔗<class_SkeletonModification2DPhysicalBones_method_stop_simulation>`

Tell the `PhysicalBone2D<class_PhysicalBone2D>` nodes to stop simulating and interacting with the physics world.

Optionally, an array of bone names can be passed to this function, and that will cause only `PhysicalBone2D<class_PhysicalBone2D>` nodes with those names to stop simulating.