github_url
hide

# CollisionObject3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `Area3D<class_Area3D>`, `PhysicsBody3D<class_PhysicsBody3D>`

Abstract base class for 3D physics objects.

classref-introduction-group

## Description

Abstract base class for 3D physics objects. **CollisionObject3D** can hold any number of `Shape3D<class_Shape3D>`s for collision. Each shape must be assigned to a *shape owner*. Shape owners are not nodes and do not appear in the editor, but are accessible through code using the `shape_owner_*` methods.

**Warning:** With a non-uniform scale, this node will likely not behave as expected. It is advised to keep its scale the same on all axes and adjust its collision shape(s) instead.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**input_event**(camera: `Node<class_Node>`, event: `InputEvent<class_InputEvent>`, event_position: `Vector3<class_Vector3>`, normal: `Vector3<class_Vector3>`, shape_idx: `int<class_int>`) `🔗<class_CollisionObject3D_signal_input_event>`

Emitted when the object receives an unhandled `InputEvent<class_InputEvent>`. `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point.

classref-item-separator

classref-signal

**mouse_entered**() `🔗<class_CollisionObject3D_signal_mouse_entered>`

Emitted when the mouse pointer enters any of this object's shapes. Requires `input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>` to be `true` and at least one `collision_layer<class_CollisionObject3D_property_collision_layer>` bit to be set.

**Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.

classref-item-separator

classref-signal

**mouse_exited**() `🔗<class_CollisionObject3D_signal_mouse_exited>`

Emitted when the mouse pointer exits all this object's shapes. Requires `input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>` to be `true` and at least one `collision_layer<class_CollisionObject3D_property_collision_layer>` bit to be set.

**Note:** Due to the lack of continuous collision detection, this signal may not be emitted in the expected order if the mouse moves fast enough and the **CollisionObject3D**'s area is small. This signal may also not be emitted if another **CollisionObject3D** is overlapping the **CollisionObject3D** in question.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DisableMode**: `🔗<enum_CollisionObject3D_DisableMode>`

classref-enumeration-constant

`DisableMode<enum_CollisionObject3D_DisableMode>` **DISABLE_MODE_REMOVE** = `0`

When `Node.process_mode<class_Node_property_process_mode>` is set to `Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`, remove from the physics simulation to stop all physics interactions with this **CollisionObject3D**.

Automatically re-added to the physics simulation when the `Node<class_Node>` is processed again.

classref-enumeration-constant

`DisableMode<enum_CollisionObject3D_DisableMode>` **DISABLE_MODE_MAKE_STATIC** = `1`

When `Node.process_mode<class_Node_property_process_mode>` is set to `Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`, make the body static. Doesn't affect `Area3D<class_Area3D>`. `PhysicsBody3D<class_PhysicsBody3D>` can't be affected by forces or other bodies while static.

Automatically set `PhysicsBody3D<class_PhysicsBody3D>` back to its original mode when the `Node<class_Node>` is processed again.

classref-enumeration-constant

`DisableMode<enum_CollisionObject3D_DisableMode>` **DISABLE_MODE_KEEP_ACTIVE** = `2`

When `Node.process_mode<class_Node_property_process_mode>` is set to `Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`, do not affect the physics simulation.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **collision_layer** = `1` `🔗<class_CollisionObject3D_property_collision_layer>`

classref-property-setget

- `void (No return value.)` **set_collision_layer**(value: `int<class_int>`)
- `int<class_int>` **get_collision_layer**()

The physics layers this CollisionObject3D **is in**. Collision objects can exist in one or more of 32 different layers. See also `collision_mask<class_CollisionObject3D_property_collision_mask>`.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

classref-item-separator

classref-property

`int<class_int>` **collision_mask** = `1` `🔗<class_CollisionObject3D_property_collision_mask>`

classref-property-setget

- `void (No return value.)` **set_collision_mask**(value: `int<class_int>`)
- `int<class_int>` **get_collision_mask**()

The physics layers this CollisionObject3D **scans**. Collision objects can scan one or more of 32 different layers. See also `collision_layer<class_CollisionObject3D_property_collision_layer>`.

**Note:** Object A can detect a contact with object B only if object B is in any of the layers that object A scans. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

classref-item-separator

classref-property

`float<class_float>` **collision_priority** = `1.0` `🔗<class_CollisionObject3D_property_collision_priority>`

classref-property-setget

- `void (No return value.)` **set_collision_priority**(value: `float<class_float>`)
- `float<class_float>` **get_collision_priority**()

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

classref-item-separator

classref-property

`DisableMode<enum_CollisionObject3D_DisableMode>` **disable_mode** = `0` `🔗<class_CollisionObject3D_property_disable_mode>`

classref-property-setget

- `void (No return value.)` **set_disable_mode**(value: `DisableMode<enum_CollisionObject3D_DisableMode>`)
- `DisableMode<enum_CollisionObject3D_DisableMode>` **get_disable_mode**()

Defines the behavior in physics when `Node.process_mode<class_Node_property_process_mode>` is set to `Node.PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`.

classref-item-separator

classref-property

`bool<class_bool>` **input_capture_on_drag** = `false` `🔗<class_CollisionObject3D_property_input_capture_on_drag>`

classref-property-setget

- `void (No return value.)` **set_capture_input_on_drag**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_capture_input_on_drag**()

If `true`, the **CollisionObject3D** will continue to receive input events as the mouse is dragged across its shapes.

classref-item-separator

classref-property

`bool<class_bool>` **input_ray_pickable** = `true` `🔗<class_CollisionObject3D_property_input_ray_pickable>`

classref-property-setget

- `void (No return value.)` **set_ray_pickable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_ray_pickable**()

If `true`, this object is pickable. A pickable object can detect the mouse pointer entering/leaving, and if the mouse is inside it, report input events. Requires at least one `collision_layer<class_CollisionObject3D_property_collision_layer>` bit to be set.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_input_event**(camera: `Camera3D<class_Camera3D>`, event: `InputEvent<class_InputEvent>`, event_position: `Vector3<class_Vector3>`, normal: `Vector3<class_Vector3>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CollisionObject3D_private_method__input_event>`

Receives unhandled `InputEvent<class_InputEvent>`s. `event_position` is the location in world space of the mouse pointer on the surface of the shape with index `shape_idx` and `normal` is the normal vector of the surface at that point. Connect to the `input_event<class_CollisionObject3D_signal_input_event>` signal to easily pick up these events.

**Note:** `_input_event()<class_CollisionObject3D_private_method__input_event>` requires `input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>` to be `true` and at least one `collision_layer<class_CollisionObject3D_property_collision_layer>` bit to be set.

classref-item-separator

classref-method

`void (No return value.)` **\_mouse_enter**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CollisionObject3D_private_method__mouse_enter>`

Called when the mouse pointer enters any of this object's shapes. Requires `input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>` to be `true` and at least one `collision_layer<class_CollisionObject3D_property_collision_layer>` bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.

classref-item-separator

classref-method

`void (No return value.)` **\_mouse_exit**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CollisionObject3D_private_method__mouse_exit>`

Called when the mouse pointer exits all this object's shapes. Requires `input_ray_pickable<class_CollisionObject3D_property_input_ray_pickable>` to be `true` and at least one `collision_layer<class_CollisionObject3D_property_collision_layer>` bit to be set. Note that moving between different shapes within a single **CollisionObject3D** won't cause this function to be called.

classref-item-separator

classref-method

`int<class_int>` **create_shape_owner**(owner: `Object<class_Object>`) `🔗<class_CollisionObject3D_method_create_shape_owner>`

Creates a new shape owner for the given object. Returns `owner_id` of the new owner for future reference.

classref-item-separator

classref-method

`bool<class_bool>` **get_collision_layer_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_get_collision_layer_value>`

Returns whether or not the specified layer of the `collision_layer<class_CollisionObject3D_property_collision_layer>` is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`bool<class_bool>` **get_collision_mask_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_get_collision_mask_value>`

Returns whether or not the specified layer of the `collision_mask<class_CollisionObject3D_property_collision_mask>` is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`RID<class_RID>` **get_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_get_rid>`

Returns the object's `RID<class_RID>`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_shape_owners**() `🔗<class_CollisionObject3D_method_get_shape_owners>`

Returns an `Array<class_Array>` of `owner_id` identifiers. You can use these ids in other methods that take `owner_id` as an argument.

classref-item-separator

classref-method

`bool<class_bool>` **is_shape_owner_disabled**(owner_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_is_shape_owner_disabled>`

If `true`, the shape owner and its shapes are disabled.

classref-item-separator

classref-method

`void (No return value.)` **remove_shape_owner**(owner_id: `int<class_int>`) `🔗<class_CollisionObject3D_method_remove_shape_owner>`

Removes the given shape owner.

classref-item-separator

classref-method

`void (No return value.)` **set_collision_layer_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_CollisionObject3D_method_set_collision_layer_value>`

Based on `value`, enables or disables the specified layer in the `collision_layer<class_CollisionObject3D_property_collision_layer>`, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_collision_mask_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_CollisionObject3D_method_set_collision_mask_value>`

Based on `value`, enables or disables the specified layer in the `collision_mask<class_CollisionObject3D_property_collision_mask>`, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`int<class_int>` **shape_find_owner**(shape_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_shape_find_owner>`

Returns the `owner_id` of the given shape.

classref-item-separator

classref-method

`void (No return value.)` **shape_owner_add_shape**(owner_id: `int<class_int>`, shape: `Shape3D<class_Shape3D>`) `🔗<class_CollisionObject3D_method_shape_owner_add_shape>`

Adds a `Shape3D<class_Shape3D>` to the shape owner.

classref-item-separator

classref-method

`void (No return value.)` **shape_owner_clear_shapes**(owner_id: `int<class_int>`) `🔗<class_CollisionObject3D_method_shape_owner_clear_shapes>`

Removes all shapes from the shape owner.

classref-item-separator

classref-method

`Object<class_Object>` **shape_owner_get_owner**(owner_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_shape_owner_get_owner>`

Returns the parent object of the given shape owner.

classref-item-separator

classref-method

`Shape3D<class_Shape3D>` **shape_owner_get_shape**(owner_id: `int<class_int>`, shape_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_shape_owner_get_shape>`

Returns the `Shape3D<class_Shape3D>` with the given ID from the given shape owner.

classref-item-separator

classref-method

`int<class_int>` **shape_owner_get_shape_count**(owner_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_shape_owner_get_shape_count>`

Returns the number of shapes the given shape owner contains.

classref-item-separator

classref-method

`int<class_int>` **shape_owner_get_shape_index**(owner_id: `int<class_int>`, shape_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_shape_owner_get_shape_index>`

Returns the child index of the `Shape3D<class_Shape3D>` with the given ID from the given shape owner.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **shape_owner_get_transform**(owner_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CollisionObject3D_method_shape_owner_get_transform>`

Returns the shape owner's `Transform3D<class_Transform3D>`.

classref-item-separator

classref-method

`void (No return value.)` **shape_owner_remove_shape**(owner_id: `int<class_int>`, shape_id: `int<class_int>`) `🔗<class_CollisionObject3D_method_shape_owner_remove_shape>`

Removes a shape from the given shape owner.

classref-item-separator

classref-method

`void (No return value.)` **shape_owner_set_disabled**(owner_id: `int<class_int>`, disabled: `bool<class_bool>`) `🔗<class_CollisionObject3D_method_shape_owner_set_disabled>`

If `true`, disables the given shape owner.

classref-item-separator

classref-method

`void (No return value.)` **shape_owner_set_transform**(owner_id: `int<class_int>`, transform: `Transform3D<class_Transform3D>`) `🔗<class_CollisionObject3D_method_shape_owner_set_transform>`

Sets the `Transform3D<class_Transform3D>` of the given shape owner.