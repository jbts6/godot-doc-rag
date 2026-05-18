github_url
hide

# ShapeCast3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A 3D shape that sweeps a region of space to detect `CollisionObject3D<class_CollisionObject3D>`s.

classref-introduction-group

## Description

Shape casting allows to detect collision objects by sweeping its `shape<class_ShapeCast3D_property_shape>` along the cast direction determined by `target_position<class_ShapeCast3D_property_target_position>`. This is similar to `RayCast3D<class_RayCast3D>`, but it allows for sweeping a region of space, rather than just a straight line. **ShapeCast3D** can detect multiple collision objects. It is useful for things like wide laser beams or snapping a simple shape to a floor.

Immediate collision overlaps can be done with the `target_position<class_ShapeCast3D_property_target_position>` set to `Vector3(0, 0, 0)` and by calling `force_shapecast_update()<class_ShapeCast3D_method_force_shapecast_update>` within the same physics frame. This helps to overcome some limitations of `Area3D<class_Area3D>` when used as an instantaneous detection area, as collision information isn't immediately available to it.

**Note:** Shape casting is more computationally expensive than ray casting.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **collide_with_areas** = `false` `🔗<class_ShapeCast3D_property_collide_with_areas>`

classref-property-setget

- `void (No return value.)` **set_collide_with_areas**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collide_with_areas_enabled**()

If `true`, collisions with `Area3D<class_Area3D>`s will be reported.

classref-item-separator

classref-property

`bool<class_bool>` **collide_with_bodies** = `true` `🔗<class_ShapeCast3D_property_collide_with_bodies>`

classref-property-setget

- `void (No return value.)` **set_collide_with_bodies**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collide_with_bodies_enabled**()

If `true`, collisions with `PhysicsBody3D<class_PhysicsBody3D>`s will be reported.

classref-item-separator

classref-property

`int<class_int>` **collision_mask** = `1` `🔗<class_ShapeCast3D_property_collision_mask>`

classref-property-setget

- `void (No return value.)` **set_collision_mask**(value: `int<class_int>`)
- `int<class_int>` **get_collision_mask**()

The shape's collision mask. Only objects in at least one collision layer enabled in the mask will be detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

classref-item-separator

classref-property

`Array<class_Array>` **collision_result** = `[]` `🔗<class_ShapeCast3D_property_collision_result>`

classref-property-setget

- `Array<class_Array>` **get_collision_result**()

Returns the complete collision information from the collision sweep. The data returned is the same as in the `PhysicsDirectSpaceState3D.get_rest_info()<class_PhysicsDirectSpaceState3D_method_get_rest_info>` method.

classref-item-separator

classref-property

`Color<class_Color>` **debug_shape_custom_color** = `Color(0, 0, 0, 1)` `🔗<class_ShapeCast3D_property_debug_shape_custom_color>`

classref-property-setget

- `void (No return value.)` **set_debug_shape_custom_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_debug_shape_custom_color**()

The custom color to use to draw the shape in the editor and at run-time if **Visible Collision Shapes** is enabled in the **Debug** menu. This color will be highlighted at run-time if the **ShapeCast3D** is colliding with something.

If set to `Color(0.0, 0.0, 0.0)` (by default), the color set in `ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>` is used.

classref-item-separator

classref-property

`bool<class_bool>` **enabled** = `true` `🔗<class_ShapeCast3D_property_enabled>`

classref-property-setget

- `void (No return value.)` **set_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_enabled**()

If `true`, collisions will be reported.

classref-item-separator

classref-property

`bool<class_bool>` **exclude_parent** = `true` `🔗<class_ShapeCast3D_property_exclude_parent>`

classref-property-setget

- `void (No return value.)` **set_exclude_parent_body**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_exclude_parent_body**()

If `true`, the parent node will be excluded from collision detection.

classref-item-separator

classref-property

`float<class_float>` **margin** = `0.0` `🔗<class_ShapeCast3D_property_margin>`

classref-property-setget

- `void (No return value.)` **set_margin**(value: `float<class_float>`)
- `float<class_float>` **get_margin**()

The collision margin for the shape. A larger margin helps detecting collisions more consistently, at the cost of precision.

classref-item-separator

classref-property

`int<class_int>` **max_results** = `32` `🔗<class_ShapeCast3D_property_max_results>`

classref-property-setget

- `void (No return value.)` **set_max_results**(value: `int<class_int>`)
- `int<class_int>` **get_max_results**()

The number of intersections can be limited with this parameter, to reduce the processing time.

classref-item-separator

classref-property

`Shape3D<class_Shape3D>` **shape** `🔗<class_ShapeCast3D_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Shape3D<class_Shape3D>`)
- `Shape3D<class_Shape3D>` **get_shape**()

The shape to be used for collision queries.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **target_position** = `Vector3(0, -1, 0)` `🔗<class_ShapeCast3D_property_target_position>`

classref-property-setget

- `void (No return value.)` **set_target_position**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_target_position**()

The shape's destination point, relative to this node's `Node3D.position<class_Node3D_property_position>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_exception**(node: `CollisionObject3D<class_CollisionObject3D>`) `🔗<class_ShapeCast3D_method_add_exception>`

Adds a collision exception so the shape does not report collisions with the specified node.

classref-item-separator

classref-method

`void (No return value.)` **add_exception_rid**(rid: `RID<class_RID>`) `🔗<class_ShapeCast3D_method_add_exception_rid>`

Adds a collision exception so the shape does not report collisions with the specified `RID<class_RID>`.

classref-item-separator

classref-method

`void (No return value.)` **clear_exceptions**() `🔗<class_ShapeCast3D_method_clear_exceptions>`

Removes all collision exceptions for this shape.

classref-item-separator

classref-method

`void (No return value.)` **force_shapecast_update**() `🔗<class_ShapeCast3D_method_force_shapecast_update>`

Updates the collision information for the shape immediately, without waiting for the next `_physics_process` call. Use this method, for example, when the shape or its parent has changed state.

**Note:** Setting `enabled<class_ShapeCast3D_property_enabled>` to `true` is not required for this to work.

classref-item-separator

classref-method

`float<class_float>` **get_closest_collision_safe_fraction**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_closest_collision_safe_fraction>`

Returns the fraction from this cast's origin to its `target_position<class_ShapeCast3D_property_target_position>` of how far the shape can move without triggering a collision, as a value between `0.0` and `1.0`.

classref-item-separator

classref-method

`float<class_float>` **get_closest_collision_unsafe_fraction**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_closest_collision_unsafe_fraction>`

Returns the fraction from this cast's origin to its `target_position<class_ShapeCast3D_property_target_position>` of how far the shape must move to trigger a collision, as a value between `0.0` and `1.0`.

In ideal conditions this would be the same as `get_closest_collision_safe_fraction()<class_ShapeCast3D_method_get_closest_collision_safe_fraction>`, however shape casting is calculated in discrete steps, so the precise point of collision can occur between two calculated positions.

classref-item-separator

classref-method

`Object<class_Object>` **get_collider**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collider>`

Returns the collided `Object<class_Object>` of one of the multiple collisions at `index`, or `null` if no object is intersecting the shape (i.e. `is_colliding()<class_ShapeCast3D_method_is_colliding>` returns `false`).

classref-item-separator

classref-method

`RID<class_RID>` **get_collider_rid**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collider_rid>`

Returns the `RID<class_RID>` of the collided object of one of the multiple collisions at `index`.

classref-item-separator

classref-method

`int<class_int>` **get_collider_shape**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collider_shape>`

Returns the shape ID of the colliding shape of one of the multiple collisions at `index`, or `0` if no object is intersecting the shape (i.e. `is_colliding()<class_ShapeCast3D_method_is_colliding>` returns `false`).

classref-item-separator

classref-method

`int<class_int>` **get_collision_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collision_count>`

The number of collisions detected at the point of impact. Use this to iterate over multiple collisions as provided by `get_collider()<class_ShapeCast3D_method_get_collider>`, `get_collider_shape()<class_ShapeCast3D_method_get_collider_shape>`, `get_collision_point()<class_ShapeCast3D_method_get_collision_point>`, and `get_collision_normal()<class_ShapeCast3D_method_get_collision_normal>` methods.

classref-item-separator

classref-method

`bool<class_bool>` **get_collision_mask_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collision_mask_value>`

Returns whether or not the specified layer of the `collision_mask<class_ShapeCast3D_property_collision_mask>` is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_collision_normal**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collision_normal>`

Returns the normal of one of the multiple collisions at `index` of the intersecting object.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_collision_point**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_get_collision_point>`

Returns the collision point of one of the multiple collisions at `index` where the shape intersects the colliding object.

**Note:** This point is in the **global** coordinate system.

classref-item-separator

classref-method

`bool<class_bool>` **is_colliding**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ShapeCast3D_method_is_colliding>`

Returns whether any object is intersecting with the shape's vector (considering the vector length).

classref-item-separator

classref-method

`void (No return value.)` **remove_exception**(node: `CollisionObject3D<class_CollisionObject3D>`) `🔗<class_ShapeCast3D_method_remove_exception>`

Removes a collision exception so the shape does report collisions with the specified node.

classref-item-separator

classref-method

`void (No return value.)` **remove_exception_rid**(rid: `RID<class_RID>`) `🔗<class_ShapeCast3D_method_remove_exception_rid>`

Removes a collision exception so the shape does report collisions with the specified `RID<class_RID>`.

classref-item-separator

classref-method

`void (No return value.)` **resource_changed**(resource: `Resource<class_Resource>`) `🔗<class_ShapeCast3D_method_resource_changed>`

**Deprecated:** Use `Resource.changed<class_Resource_signal_changed>` instead.

This method does nothing.

classref-item-separator

classref-method

`void (No return value.)` **set_collision_mask_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_ShapeCast3D_method_set_collision_mask_value>`

Based on `value`, enables or disables the specified layer in the `collision_mask<class_ShapeCast3D_property_collision_mask>`, given a `layer_number` between 1 and 32.