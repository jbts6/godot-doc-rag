github_url
hide

# PhysicsBody3D

**Inherits:** `CollisionObject3D<class_CollisionObject3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `CharacterBody3D<class_CharacterBody3D>`, `PhysicalBone3D<class_PhysicalBone3D>`, `RigidBody3D<class_RigidBody3D>`, `StaticBody3D<class_StaticBody3D>`

Abstract base class for 3D game objects affected by physics.

classref-introduction-group

## Description

**PhysicsBody3D** is an abstract base class for 3D game objects affected by physics. All 3D physics bodies inherit from it.

**Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

classref-introduction-group

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`
- `Troubleshooting physics issues <../tutorials/physics/troubleshooting_physics_issues>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **axis_lock_angular_x** = `false` `🔗<class_PhysicsBody3D_property_axis_lock_angular_x>`

classref-property-setget

- `void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`)
- `bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Lock the body's rotation in the X axis.

classref-item-separator

classref-property

`bool<class_bool>` **axis_lock_angular_y** = `false` `🔗<class_PhysicsBody3D_property_axis_lock_angular_y>`

classref-property-setget

- `void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`)
- `bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Lock the body's rotation in the Y axis.

classref-item-separator

classref-property

`bool<class_bool>` **axis_lock_angular_z** = `false` `🔗<class_PhysicsBody3D_property_axis_lock_angular_z>`

classref-property-setget

- `void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`)
- `bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Lock the body's rotation in the Z axis.

classref-item-separator

classref-property

`bool<class_bool>` **axis_lock_linear_x** = `false` `🔗<class_PhysicsBody3D_property_axis_lock_linear_x>`

classref-property-setget

- `void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`)
- `bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Lock the body's linear movement in the X axis.

classref-item-separator

classref-property

`bool<class_bool>` **axis_lock_linear_y** = `false` `🔗<class_PhysicsBody3D_property_axis_lock_linear_y>`

classref-property-setget

- `void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`)
- `bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Lock the body's linear movement in the Y axis.

classref-item-separator

classref-property

`bool<class_bool>` **axis_lock_linear_z** = `false` `🔗<class_PhysicsBody3D_property_axis_lock_linear_z>`

classref-property-setget

- `void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`)
- `bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Lock the body's linear movement in the Z axis.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_collision_exception_with**(body: `Node<class_Node>`) `🔗<class_PhysicsBody3D_method_add_collision_exception_with>`

Adds a body to the list of bodies that this body can't collide with.

classref-item-separator

classref-method

`bool<class_bool>` **get_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsBody3D_method_get_axis_lock>`

Returns `true` if the specified linear or rotational `axis` is locked.

classref-item-separator

classref-method

`Array<class_Array>`\[`PhysicsBody3D<class_PhysicsBody3D>`\] **get_collision_exceptions**() `🔗<class_PhysicsBody3D_method_get_collision_exceptions>`

Returns an array of nodes that were added as collision exceptions for this body.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_gravity**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsBody3D_method_get_gravity>`

Returns the gravity vector computed from all sources that can affect the body, including all gravity overrides from `Area3D<class_Area3D>` nodes and the global world gravity.

classref-item-separator

classref-method

`KinematicCollision3D<class_KinematicCollision3D>` **move_and_collide**(motion: `Vector3<class_Vector3>`, test_only: `bool<class_bool>` = false, safe_margin: `float<class_float>` = 0.001, recovery_as_collision: `bool<class_bool>` = false, max_collisions: `int<class_int>` = 1) `🔗<class_PhysicsBody3D_method_move_and_collide>`

Moves the body along the vector `motion`. In order to be frame rate independent in `Node._physics_process()<class_Node_private_method__physics_process>` or `Node._process()<class_Node_private_method__process>`, `motion` should be computed using `delta`.

The body will stop if it collides. Returns a `KinematicCollision3D<class_KinematicCollision3D>`, which contains information about the collision when stopped, or when touching another body along the motion.

If `test_only` is `true`, the body does not move but the would-be collision information is given.

`safe_margin` is the extra margin used for collision recovery (see `CharacterBody3D.safe_margin<class_CharacterBody3D_property_safe_margin>` for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is used e.g. by `CharacterBody3D<class_CharacterBody3D>` for improving floor detection during floor snapping.

`max_collisions` allows to retrieve more than one collision result.

classref-item-separator

classref-method

`void (No return value.)` **remove_collision_exception_with**(body: `Node<class_Node>`) `🔗<class_PhysicsBody3D_method_remove_collision_exception_with>`

Removes a body from the list of bodies that this body can't collide with.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_lock**(axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`) `🔗<class_PhysicsBody3D_method_set_axis_lock>`

Locks or unlocks the specified linear or rotational `axis` depending on the value of `lock`.

classref-item-separator

classref-method

`bool<class_bool>` **test_move**(from: `Transform3D<class_Transform3D>`, motion: `Vector3<class_Vector3>`, collision: `KinematicCollision3D<class_KinematicCollision3D>` = null, safe_margin: `float<class_float>` = 0.001, recovery_as_collision: `bool<class_bool>` = false, max_collisions: `int<class_int>` = 1) `🔗<class_PhysicsBody3D_method_test_move>`

Checks for collisions without moving the body. In order to be frame rate independent in `Node._physics_process()<class_Node_private_method__physics_process>` or `Node._process()<class_Node_private_method__process>`, `motion` should be computed using `delta`.

Virtually sets the node's position, scale and rotation to that of the given `Transform3D<class_Transform3D>`, then tries to move the body along the vector `motion`. Returns `true` if a collision would stop the body from moving along the whole path.

`collision` is an optional object of type `KinematicCollision3D<class_KinematicCollision3D>`, which contains additional information about the collision when stopped, or when touching another body along the motion.

`safe_margin` is the extra margin used for collision recovery (see `CharacterBody3D.safe_margin<class_CharacterBody3D_property_safe_margin>` for more details).

If `recovery_as_collision` is `true`, any depenetration from the recovery phase is also reported as a collision; this is useful for checking whether the body would *touch* any other bodies.

`max_collisions` allows to retrieve more than one collision result.