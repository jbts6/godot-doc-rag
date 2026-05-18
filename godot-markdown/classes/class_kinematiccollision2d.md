github_url
hide

# KinematicCollision2D

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Holds collision data from the movement of a `PhysicsBody2D<class_PhysicsBody2D>`.

classref-introduction-group

## Description

Holds collision data from the movement of a `PhysicsBody2D<class_PhysicsBody2D>`, usually from `PhysicsBody2D.move_and_collide()<class_PhysicsBody2D_method_move_and_collide>`. When a `PhysicsBody2D<class_PhysicsBody2D>` is moved, it stops if it detects a collision with another body. If a collision is detected, a **KinematicCollision2D** object is returned.

The collision data includes the colliding object, the remaining motion, and the collision position. This data can be used to determine a custom response to the collision.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_angle**(up_direction: `Vector2<class_Vector2>` = Vector2(0, -1)) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_angle>`

Returns the collision angle according to `up_direction`, which is `Vector2.UP<class_Vector2_constant_UP>` by default. This value is always positive.

classref-item-separator

classref-method

`Object<class_Object>` **get_collider**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_collider>`

Returns the colliding body's attached `Object<class_Object>`.

classref-item-separator

classref-method

`int<class_int>` **get_collider_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_collider_id>`

Returns the unique instance ID of the colliding body's attached `Object<class_Object>`. See `Object.get_instance_id()<class_Object_method_get_instance_id>`.

classref-item-separator

classref-method

`RID<class_RID>` **get_collider_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_collider_rid>`

Returns the colliding body's `RID<class_RID>` used by the `PhysicsServer2D<class_PhysicsServer2D>`.

classref-item-separator

classref-method

`Object<class_Object>` **get_collider_shape**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_collider_shape>`

Returns the colliding body's shape.

classref-item-separator

classref-method

`int<class_int>` **get_collider_shape_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_collider_shape_index>`

Returns the colliding body's shape index. See `CollisionObject2D<class_CollisionObject2D>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_collider_velocity**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_collider_velocity>`

Returns the colliding body's velocity.

classref-item-separator

classref-method

`float<class_float>` **get_depth**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_depth>`

Returns the colliding body's length of overlap along the collision normal.

classref-item-separator

classref-method

`Object<class_Object>` **get_local_shape**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_local_shape>`

Returns the moving object's colliding shape.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_normal**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_normal>`

Returns the colliding body's shape's normal at the point of collision.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_position**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_position>`

Returns the point of collision in global coordinates.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_remainder**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_remainder>`

Returns the moving object's remaining movement vector.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_travel**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_KinematicCollision2D_method_get_travel>`

Returns the moving object's travel before collision.