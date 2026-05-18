github_url
hide

# PhysicalBone2D

**Inherits:** `RigidBody2D<class_RigidBody2D>` **\<** `PhysicsBody2D<class_PhysicsBody2D>` **\<** `CollisionObject2D<class_CollisionObject2D>` **\<** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A `RigidBody2D<class_RigidBody2D>`-derived node used to make `Bone2D<class_Bone2D>`s in a `Skeleton2D<class_Skeleton2D>` react to physics.

classref-introduction-group

## Description

The **PhysicalBone2D** node is a `RigidBody2D<class_RigidBody2D>`-based node that can be used to make `Bone2D<class_Bone2D>`s in a `Skeleton2D<class_Skeleton2D>` react to physics.

**Note:** To make the `Bone2D<class_Bone2D>`s visually follow the **PhysicalBone2D** node, use a `SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>` modification on the `Skeleton2D<class_Skeleton2D>` parent.

**Note:** The **PhysicalBone2D** node does not automatically create a `Joint2D<class_Joint2D>` node to keep **PhysicalBone2D** nodes together. They must be created manually. For most cases, you want to use a `PinJoint2D<class_PinJoint2D>` node. The **PhysicalBone2D** node will automatically configure the `Joint2D<class_Joint2D>` node once it's been added as a child node.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **auto_configure_joint** = `true` `🔗<class_PhysicalBone2D_property_auto_configure_joint>`

classref-property-setget

- `void (No return value.)` **set_auto_configure_joint**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_auto_configure_joint**()

If `true`, the **PhysicalBone2D** will automatically configure the first `Joint2D<class_Joint2D>` child node. The automatic configuration is limited to setting up the node properties and positioning the `Joint2D<class_Joint2D>`.

classref-item-separator

classref-property

`int<class_int>` **bone2d_index** = `-1` `🔗<class_PhysicalBone2D_property_bone2d_index>`

classref-property-setget

- `void (No return value.)` **set_bone2d_index**(value: `int<class_int>`)
- `int<class_int>` **get_bone2d_index**()

The index of the `Bone2D<class_Bone2D>` that this **PhysicalBone2D** should simulate.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **bone2d_nodepath** = `NodePath("")` `🔗<class_PhysicalBone2D_property_bone2d_nodepath>`

classref-property-setget

- `void (No return value.)` **set_bone2d_nodepath**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_bone2d_nodepath**()

The `NodePath<class_NodePath>` to the `Bone2D<class_Bone2D>` that this **PhysicalBone2D** should simulate.

classref-item-separator

classref-property

`bool<class_bool>` **follow_bone_when_simulating** = `false` `🔗<class_PhysicalBone2D_property_follow_bone_when_simulating>`

classref-property-setget

- `void (No return value.)` **set_follow_bone_when_simulating**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_follow_bone_when_simulating**()

If `true`, the **PhysicalBone2D** will keep the transform of the bone it is bound to when simulating physics.

classref-item-separator

classref-property

`bool<class_bool>` **simulate_physics** = `false` `🔗<class_PhysicalBone2D_property_simulate_physics>`

classref-property-setget

- `void (No return value.)` **set_simulate_physics**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_simulate_physics**()

If `true`, the **PhysicalBone2D** will start simulating using physics. If `false`, the **PhysicalBone2D** will follow the transform of the `Bone2D<class_Bone2D>` node.

**Note:** To have the `Bone2D<class_Bone2D>`s visually follow the **PhysicalBone2D**, use a `SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>` modification on the `Skeleton2D<class_Skeleton2D>` node with the `Bone2D<class_Bone2D>` nodes.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Joint2D<class_Joint2D>` **get_joint**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicalBone2D_method_get_joint>`

Returns the first `Joint2D<class_Joint2D>` child node, if one exists. This is mainly a helper function to make it easier to get the `Joint2D<class_Joint2D>` that the **PhysicalBone2D** is autoconfiguring.

classref-item-separator

classref-method

`bool<class_bool>` **is_simulating_physics**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicalBone2D_method_is_simulating_physics>`

Returns a boolean that indicates whether the **PhysicalBone2D** is running and simulating using the Godot 2D physics engine. When `true`, the PhysicalBone2D node is using physics.