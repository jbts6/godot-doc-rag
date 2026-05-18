github_url
hide

# SpringArm3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A 3D raycast that dynamically moves its children near the collision point.

classref-introduction-group

## Description

**SpringArm3D** casts a ray or a shape along its Z axis and moves all its direct children to the collision point, with an optional margin. This is useful for 3rd person cameras that move closer to the player when inside a tight space (you may need to exclude the player's collider from the **SpringArm3D**'s collision check).

classref-introduction-group

## Tutorials

- `Third-person camera with spring arm <../tutorials/3d/spring_arm>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **collision_mask** = `1` `🔗<class_SpringArm3D_property_collision_mask>`

classref-property-setget

- `void (No return value.)` **set_collision_mask**(value: `int<class_int>`)
- `int<class_int>` **get_collision_mask**()

The layers against which the collision check will be done. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

classref-item-separator

classref-property

`float<class_float>` **margin** = `0.01` `🔗<class_SpringArm3D_property_margin>`

classref-property-setget

- `void (No return value.)` **set_margin**(value: `float<class_float>`)
- `float<class_float>` **get_margin**()

When the collision check is made, a candidate length for the SpringArm3D is given.

The margin is then subtracted to this length and the translation is applied to the child objects of the SpringArm3D.

This margin is useful for when the SpringArm3D has a `Camera3D<class_Camera3D>` as a child node: without the margin, the `Camera3D<class_Camera3D>` would be placed on the exact point of collision, while with the margin the `Camera3D<class_Camera3D>` would be placed close to the point of collision.

classref-item-separator

classref-property

`Shape3D<class_Shape3D>` **shape** `🔗<class_SpringArm3D_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Shape3D<class_Shape3D>`)
- `Shape3D<class_Shape3D>` **get_shape**()

The `Shape3D<class_Shape3D>` to use for the SpringArm3D.

When the shape is set, the SpringArm3D will cast the `Shape3D<class_Shape3D>` on its z axis instead of performing a ray cast.

classref-item-separator

classref-property

`float<class_float>` **spring_length** = `1.0` `🔗<class_SpringArm3D_property_spring_length>`

classref-property-setget

- `void (No return value.)` **set_length**(value: `float<class_float>`)
- `float<class_float>` **get_length**()

The maximum extent of the SpringArm3D. This is used as a length for both the ray and the shape cast used internally to calculate the desired position of the SpringArm3D's child nodes.

To know more about how to perform a shape cast or a ray cast, please consult the `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` documentation.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_excluded_object**(RID: `RID<class_RID>`) `🔗<class_SpringArm3D_method_add_excluded_object>`

Adds the `PhysicsBody3D<class_PhysicsBody3D>` object with the given `RID<class_RID>` to the list of `PhysicsBody3D<class_PhysicsBody3D>` objects excluded from the collision check.

classref-item-separator

classref-method

`void (No return value.)` **clear_excluded_objects**() `🔗<class_SpringArm3D_method_clear_excluded_objects>`

Clears the list of `PhysicsBody3D<class_PhysicsBody3D>` objects excluded from the collision check.

classref-item-separator

classref-method

`float<class_float>` **get_hit_length**() `🔗<class_SpringArm3D_method_get_hit_length>`

Returns the spring arm's current length.

classref-item-separator

classref-method

`bool<class_bool>` **remove_excluded_object**(RID: `RID<class_RID>`) `🔗<class_SpringArm3D_method_remove_excluded_object>`

Removes the given `RID<class_RID>` from the list of `PhysicsBody3D<class_PhysicsBody3D>` objects excluded from the collision check.