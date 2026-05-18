github_url
hide

# PhysicsTestMotionParameters2D

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Provides parameters for `PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>`.

classref-introduction-group

## Description

By changing various properties of this object, such as the motion, you can configure the parameters for `PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **collide_separation_ray** = `false` `🔗<class_PhysicsTestMotionParameters2D_property_collide_separation_ray>`

classref-property-setget

- `void (No return value.)` **set_collide_separation_ray_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collide_separation_ray_enabled**()

If set to `true`, shapes of type `PhysicsServer2D.SHAPE_SEPARATION_RAY<class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY>` are used to detect collisions and can stop the motion. Can be useful when snapping to the ground.

If set to `false`, shapes of type `PhysicsServer2D.SHAPE_SEPARATION_RAY<class_PhysicsServer2D_constant_SHAPE_SEPARATION_RAY>` are only used for separation when overlapping with other bodies. That's the main use for separation ray shapes.

classref-item-separator

classref-property

`Array<class_Array>`\[`RID<class_RID>`\] **exclude_bodies** = `[]` `🔗<class_PhysicsTestMotionParameters2D_property_exclude_bodies>`

classref-property-setget

- `void (No return value.)` **set_exclude_bodies**(value: `Array<class_Array>`\[`RID<class_RID>`\])
- `Array<class_Array>`\[`RID<class_RID>`\] **get_exclude_bodies**()

Optional array of body `RID<class_RID>` to exclude from collision. Use `CollisionObject2D.get_rid()<class_CollisionObject2D_method_get_rid>` to get the `RID<class_RID>` associated with a `CollisionObject2D<class_CollisionObject2D>`-derived node.

classref-item-separator

classref-property

`Array<class_Array>`\[`int<class_int>`\] **exclude_objects** = `[]` `🔗<class_PhysicsTestMotionParameters2D_property_exclude_objects>`

classref-property-setget

- `void (No return value.)` **set_exclude_objects**(value: `Array<class_Array>`\[`int<class_int>`\])
- `Array<class_Array>`\[`int<class_int>`\] **get_exclude_objects**()

Optional array of object unique instance ID to exclude from collision. See `Object.get_instance_id()<class_Object_method_get_instance_id>`.

classref-item-separator

classref-property

`Transform2D<class_Transform2D>` **from** = `Transform2D(1, 0, 0, 1, 0, 0)` `🔗<class_PhysicsTestMotionParameters2D_property_from>`

classref-property-setget

- `void (No return value.)` **set_from**(value: `Transform2D<class_Transform2D>`)
- `Transform2D<class_Transform2D>` **get_from**()

Transform in global space where the motion should start. Usually set to `Node2D.global_transform<class_Node2D_property_global_transform>` for the current body's transform.

classref-item-separator

classref-property

`float<class_float>` **margin** = `0.08` `🔗<class_PhysicsTestMotionParameters2D_property_margin>`

classref-property-setget

- `void (No return value.)` **set_margin**(value: `float<class_float>`)
- `float<class_float>` **get_margin**()

Increases the size of the shapes involved in the collision detection.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **motion** = `Vector2(0, 0)` `🔗<class_PhysicsTestMotionParameters2D_property_motion>`

classref-property-setget

- `void (No return value.)` **set_motion**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_motion**()

Motion vector to define the length and direction of the motion to test.

classref-item-separator

classref-property

`bool<class_bool>` **recovery_as_collision** = `false` `🔗<class_PhysicsTestMotionParameters2D_property_recovery_as_collision>`

classref-property-setget

- `void (No return value.)` **set_recovery_as_collision_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_recovery_as_collision_enabled**()

If set to `true`, any depenetration from the recovery phase is reported as a collision; this is used e.g. by `CharacterBody2D<class_CharacterBody2D>` for improving floor detection during floor snapping.

If set to `false`, only collisions resulting from the motion are reported, which is generally the desired behavior.