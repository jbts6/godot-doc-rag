github_url
hide

# PhysicsServer3DExtension

**Inherits:** `PhysicsServer3D<class_PhysicsServer3D>` **\<** `Object<class_Object>`

Provides virtual methods that can be overridden to create custom `PhysicsServer3D<class_PhysicsServer3D>` implementations.

classref-introduction-group

## Description

This class extends `PhysicsServer3D<class_PhysicsServer3D>` by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of `PhysicsServer3D<class_PhysicsServer3D>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_area_add_shape**(area: `RID<class_RID>`, shape: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`, disabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_add_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_attach_object_instance_id**(area: `RID<class_RID>`, id: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_attach_object_instance_id>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_clear_shapes**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_clear_shapes>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_area_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_area_get_collision_layer**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_area_get_collision_mask**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_area_get_object_instance_id**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_object_instance_id>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Variant<class_Variant>` **\_area_get_param**(area: `RID<class_RID>`, param: `AreaParameter<enum_PhysicsServer3D_AreaParameter>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_area_get_shape**(area: `RID<class_RID>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_area_get_shape_count**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_shape_count>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **\_area_get_shape_transform**(area: `RID<class_RID>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_shape_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_area_get_space**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_space>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **\_area_get_transform**(area: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__area_get_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_remove_shape**(area: `RID<class_RID>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_remove_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_area_monitor_callback**(area: `RID<class_RID>`, callback: `Callable<class_Callable>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_area_monitor_callback>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_collision_layer**(area: `RID<class_RID>`, layer: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_collision_mask**(area: `RID<class_RID>`, mask: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_monitor_callback**(area: `RID<class_RID>`, callback: `Callable<class_Callable>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_monitor_callback>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_monitorable**(area: `RID<class_RID>`, monitorable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_monitorable>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_param**(area: `RID<class_RID>`, param: `AreaParameter<enum_PhysicsServer3D_AreaParameter>`, value: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_ray_pickable**(area: `RID<class_RID>`, enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_ray_pickable>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_shape**(area: `RID<class_RID>`, shape_idx: `int<class_int>`, shape: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_shape_disabled**(area: `RID<class_RID>`, shape_idx: `int<class_int>`, disabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_shape_disabled>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_shape_transform**(area: `RID<class_RID>`, shape_idx: `int<class_int>`, transform: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_shape_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_space**(area: `RID<class_RID>`, space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_space>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_area_set_transform**(area: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__area_set_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_add_collision_exception**(body: `RID<class_RID>`, excepted_body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_add_collision_exception>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_add_constant_central_force**(body: `RID<class_RID>`, force: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_add_constant_central_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_add_constant_force**(body: `RID<class_RID>`, force: `Vector3<class_Vector3>`, position: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_add_constant_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_add_constant_torque**(body: `RID<class_RID>`, torque: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_add_constant_torque>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_add_shape**(body: `RID<class_RID>`, shape: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`, disabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_add_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_apply_central_force**(body: `RID<class_RID>`, force: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_apply_central_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_apply_central_impulse**(body: `RID<class_RID>`, impulse: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_apply_central_impulse>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_apply_force**(body: `RID<class_RID>`, force: `Vector3<class_Vector3>`, position: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_apply_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_apply_impulse**(body: `RID<class_RID>`, impulse: `Vector3<class_Vector3>`, position: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_apply_impulse>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_apply_torque**(body: `RID<class_RID>`, torque: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_apply_torque>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_apply_torque_impulse**(body: `RID<class_RID>`, impulse: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_apply_torque_impulse>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_attach_object_instance_id**(body: `RID<class_RID>`, id: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_attach_object_instance_id>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_clear_shapes**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_clear_shapes>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_body_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Array<class_Array>`\[`RID<class_RID>`\] **\_body_get_collision_exceptions**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_exceptions>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_body_get_collision_layer**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_body_get_collision_mask**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_body_get_collision_priority**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_priority>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_body_get_constant_force**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_constant_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_body_get_constant_torque**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_constant_torque>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_body_get_contacts_reported_depth_threshold**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_contacts_reported_depth_threshold>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>` **\_body_get_direct_state**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_direct_state>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_body_get_max_contacts_reported**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_max_contacts_reported>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`BodyMode<enum_PhysicsServer3D_BodyMode>` **\_body_get_mode**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_mode>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_body_get_object_instance_id**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_object_instance_id>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Variant<class_Variant>` **\_body_get_param**(body: `RID<class_RID>`, param: `BodyParameter<enum_PhysicsServer3D_BodyParameter>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_body_get_shape**(body: `RID<class_RID>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_body_get_shape_count**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_shape_count>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **\_body_get_shape_transform**(body: `RID<class_RID>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_shape_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_body_get_space**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_space>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Variant<class_Variant>` **\_body_get_state**(body: `RID<class_RID>`, state: `BodyState<enum_PhysicsServer3D_BodyState>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_state>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_body_get_user_flags**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_get_user_flags>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_body_is_axis_locked**(body: `RID<class_RID>`, axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_is_axis_locked>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_body_is_continuous_collision_detection_enabled**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_is_continuous_collision_detection_enabled>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_body_is_omitting_force_integration**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_is_omitting_force_integration>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_remove_collision_exception**(body: `RID<class_RID>`, excepted_body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_remove_collision_exception>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_remove_shape**(body: `RID<class_RID>`, shape_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_remove_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_reset_mass_properties**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_reset_mass_properties>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_axis_lock**(body: `RID<class_RID>`, axis: `BodyAxis<enum_PhysicsServer3D_BodyAxis>`, lock: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_axis_lock>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_axis_velocity**(body: `RID<class_RID>`, axis_velocity: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_axis_velocity>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_collision_layer**(body: `RID<class_RID>`, layer: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_collision_mask**(body: `RID<class_RID>`, mask: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_collision_priority**(body: `RID<class_RID>`, priority: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_collision_priority>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_constant_force**(body: `RID<class_RID>`, force: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_constant_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_constant_torque**(body: `RID<class_RID>`, torque: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_constant_torque>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_contacts_reported_depth_threshold**(body: `RID<class_RID>`, threshold: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_contacts_reported_depth_threshold>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_enable_continuous_collision_detection**(body: `RID<class_RID>`, enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_enable_continuous_collision_detection>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_force_integration_callback**(body: `RID<class_RID>`, callable: `Callable<class_Callable>`, userdata: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_force_integration_callback>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_max_contacts_reported**(body: `RID<class_RID>`, amount: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_max_contacts_reported>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_mode**(body: `RID<class_RID>`, mode: `BodyMode<enum_PhysicsServer3D_BodyMode>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_mode>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_omit_force_integration**(body: `RID<class_RID>`, enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_omit_force_integration>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_param**(body: `RID<class_RID>`, param: `BodyParameter<enum_PhysicsServer3D_BodyParameter>`, value: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_ray_pickable**(body: `RID<class_RID>`, enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_ray_pickable>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_shape**(body: `RID<class_RID>`, shape_idx: `int<class_int>`, shape: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_shape_disabled**(body: `RID<class_RID>`, shape_idx: `int<class_int>`, disabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_shape_disabled>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_shape_transform**(body: `RID<class_RID>`, shape_idx: `int<class_int>`, transform: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_shape_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_space**(body: `RID<class_RID>`, space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_space>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_state**(body: `RID<class_RID>`, state: `BodyState<enum_PhysicsServer3D_BodyState>`, value: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_state>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_state_sync_callback**(body: `RID<class_RID>`, callable: `Callable<class_Callable>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_state_sync_callback>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_body_set_user_flags**(body: `RID<class_RID>`, flags: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__body_set_user_flags>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_body_test_motion**(body: `RID<class_RID>`, from: `Transform3D<class_Transform3D>`, motion: `Vector3<class_Vector3>`, margin: `float<class_float>`, max_collisions: `int<class_int>`, collide_separation_ray: `bool<class_bool>`, recovery_as_collision: `bool<class_bool>`, r_result: `PhysicsServer3DExtensionMotionResult*`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__body_test_motion>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_box_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__box_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_capsule_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__capsule_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_concave_polygon_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__concave_polygon_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_cone_twist_joint_get_param**(joint: `RID<class_RID>`, param: `ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__cone_twist_joint_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_cone_twist_joint_set_param**(joint: `RID<class_RID>`, param: `ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`, value: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__cone_twist_joint_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_convex_polygon_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__convex_polygon_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_custom_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__custom_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_cylinder_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__cylinder_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_end_sync**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__end_sync>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_finish**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__finish>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_flush_queries**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__flush_queries>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_free_rid**(rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__free_rid>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_generic_6dof_joint_get_flag**(joint: `RID<class_RID>`, axis: `Axis<enum_Vector3_Axis>`, flag: `G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_flag>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_generic_6dof_joint_get_param**(joint: `RID<class_RID>`, axis: `Axis<enum_Vector3_Axis>`, param: `G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_generic_6dof_joint_set_flag**(joint: `RID<class_RID>`, axis: `Axis<enum_Vector3_Axis>`, flag: `G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`, enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_flag>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_generic_6dof_joint_set_param**(joint: `RID<class_RID>`, axis: `Axis<enum_Vector3_Axis>`, param: `G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`, value: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_get_process_info**(process_info: `ProcessInfo<enum_PhysicsServer3D_ProcessInfo>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__get_process_info>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_heightmap_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__heightmap_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_hinge_joint_get_flag**(joint: `RID<class_RID>`, flag: `HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_get_flag>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_hinge_joint_get_param**(joint: `RID<class_RID>`, param: `HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_hinge_joint_set_flag**(joint: `RID<class_RID>`, flag: `HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`, enabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_set_flag>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_hinge_joint_set_param**(joint: `RID<class_RID>`, param: `HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`, value: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_init**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__init>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_is_flushing_queries**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__is_flushing_queries>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_clear**(joint: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_clear>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_joint_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_disable_collisions_between_bodies**(joint: `RID<class_RID>`, disable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_disable_collisions_between_bodies>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_joint_get_solver_priority**(joint: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_get_solver_priority>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`JointType<enum_PhysicsServer3D_JointType>` **\_joint_get_type**(joint: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_get_type>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_joint_is_disabled_collisions_between_bodies**(joint: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_is_disabled_collisions_between_bodies>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_make_cone_twist**(joint: `RID<class_RID>`, body_A: `RID<class_RID>`, local_ref_A: `Transform3D<class_Transform3D>`, body_B: `RID<class_RID>`, local_ref_B: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_make_cone_twist>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_make_generic_6dof**(joint: `RID<class_RID>`, body_A: `RID<class_RID>`, local_ref_A: `Transform3D<class_Transform3D>`, body_B: `RID<class_RID>`, local_ref_B: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_make_generic_6dof>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_make_hinge**(joint: `RID<class_RID>`, body_A: `RID<class_RID>`, hinge_A: `Transform3D<class_Transform3D>`, body_B: `RID<class_RID>`, hinge_B: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_make_hinge>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_make_hinge_simple**(joint: `RID<class_RID>`, body_A: `RID<class_RID>`, pivot_A: `Vector3<class_Vector3>`, axis_A: `Vector3<class_Vector3>`, body_B: `RID<class_RID>`, pivot_B: `Vector3<class_Vector3>`, axis_B: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_make_hinge_simple>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_make_pin**(joint: `RID<class_RID>`, body_A: `RID<class_RID>`, local_A: `Vector3<class_Vector3>`, body_B: `RID<class_RID>`, local_B: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_make_pin>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_make_slider**(joint: `RID<class_RID>`, body_A: `RID<class_RID>`, local_ref_A: `Transform3D<class_Transform3D>`, body_B: `RID<class_RID>`, local_ref_B: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_make_slider>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_joint_set_solver_priority**(joint: `RID<class_RID>`, priority: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__joint_set_solver_priority>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_pin_joint_get_local_a**(joint: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__pin_joint_get_local_a>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_pin_joint_get_local_b**(joint: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__pin_joint_get_local_b>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_pin_joint_get_param**(joint: `RID<class_RID>`, param: `PinJointParam<enum_PhysicsServer3D_PinJointParam>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__pin_joint_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_pin_joint_set_local_a**(joint: `RID<class_RID>`, local_A: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__pin_joint_set_local_a>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_pin_joint_set_local_b**(joint: `RID<class_RID>`, local_B: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__pin_joint_set_local_b>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_pin_joint_set_param**(joint: `RID<class_RID>`, param: `PinJointParam<enum_PhysicsServer3D_PinJointParam>`, value: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__pin_joint_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_separation_ray_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__separation_ray_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_set_active**(active: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__set_active>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_shape_get_custom_solver_bias**(shape: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_get_custom_solver_bias>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Variant<class_Variant>` **\_shape_get_data**(shape: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_get_data>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_shape_get_margin**(shape: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_get_margin>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`ShapeType<enum_PhysicsServer3D_ShapeType>` **\_shape_get_type**(shape: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_get_type>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_shape_set_custom_solver_bias**(shape: `RID<class_RID>`, bias: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_set_custom_solver_bias>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_shape_set_data**(shape: `RID<class_RID>`, data: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_set_data>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_shape_set_margin**(shape: `RID<class_RID>`, margin: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__shape_set_margin>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_slider_joint_get_param**(joint: `RID<class_RID>`, param: `SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__slider_joint_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_slider_joint_set_param**(joint: `RID<class_RID>`, param: `SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`, value: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__slider_joint_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_add_collision_exception**(body: `RID<class_RID>`, body_b: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_add_collision_exception>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_apply_central_force**(body: `RID<class_RID>`, force: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_central_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_apply_central_impulse**(body: `RID<class_RID>`, impulse: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_central_impulse>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_apply_point_force**(body: `RID<class_RID>`, point_index: `int<class_int>`, force: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_point_force>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_apply_point_impulse**(body: `RID<class_RID>`, point_index: `int<class_int>`, impulse: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_point_impulse>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_soft_body_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`AABB<class_AABB>` **\_soft_body_get_bounds**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_bounds>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Array<class_Array>`\[`RID<class_RID>`\] **\_soft_body_get_collision_exceptions**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_collision_exceptions>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_soft_body_get_collision_layer**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_soft_body_get_collision_mask**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_soft_body_get_damping_coefficient**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_damping_coefficient>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_soft_body_get_drag_coefficient**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_drag_coefficient>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_soft_body_get_linear_stiffness**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_linear_stiffness>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_soft_body_get_point_global_position**(body: `RID<class_RID>`, point_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_point_global_position>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_soft_body_get_pressure_coefficient**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_pressure_coefficient>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_soft_body_get_shrinking_factor**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_shrinking_factor>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_soft_body_get_simulation_precision**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_simulation_precision>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_soft_body_get_space**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_space>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Variant<class_Variant>` **\_soft_body_get_state**(body: `RID<class_RID>`, state: `BodyState<enum_PhysicsServer3D_BodyState>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_state>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_soft_body_get_total_mass**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_total_mass>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_soft_body_is_point_pinned**(body: `RID<class_RID>`, point_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_is_point_pinned>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_move_point**(body: `RID<class_RID>`, point_index: `int<class_int>`, global_position: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_move_point>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_pin_point**(body: `RID<class_RID>`, point_index: `int<class_int>`, pin: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_pin_point>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_remove_all_pinned_points**(body: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_remove_all_pinned_points>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_remove_collision_exception**(body: `RID<class_RID>`, body_b: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_remove_collision_exception>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_collision_layer**(body: `RID<class_RID>`, layer: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_collision_mask**(body: `RID<class_RID>`, mask: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_damping_coefficient**(body: `RID<class_RID>`, damping_coefficient: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_damping_coefficient>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_drag_coefficient**(body: `RID<class_RID>`, drag_coefficient: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_drag_coefficient>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_linear_stiffness**(body: `RID<class_RID>`, linear_stiffness: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_linear_stiffness>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_mesh**(body: `RID<class_RID>`, mesh: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_mesh>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_pressure_coefficient**(body: `RID<class_RID>`, pressure_coefficient: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_pressure_coefficient>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_ray_pickable**(body: `RID<class_RID>`, enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_ray_pickable>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_shrinking_factor**(body: `RID<class_RID>`, shrinking_factor: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_shrinking_factor>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_simulation_precision**(body: `RID<class_RID>`, simulation_precision: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_simulation_precision>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_space**(body: `RID<class_RID>`, space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_space>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_state**(body: `RID<class_RID>`, state: `BodyState<enum_PhysicsServer3D_BodyState>`, variant: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_state>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_total_mass**(body: `RID<class_RID>`, total_mass: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_total_mass>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_set_transform**(body: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_transform>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_soft_body_update_rendering_server**(body: `RID<class_RID>`, rendering_server_handler: `PhysicsServer3DRenderingServerHandler<class_PhysicsServer3DRenderingServerHandler>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_space_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__space_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_space_get_contact_count**(space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__space_get_contact_count>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PackedVector3Array<class_PackedVector3Array>` **\_space_get_contacts**(space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__space_get_contacts>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` **\_space_get_direct_state**(space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__space_get_direct_state>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **\_space_get_param**(space: `RID<class_RID>`, param: `SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__space_get_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_space_is_active**(space: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_private_method__space_is_active>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_space_set_active**(space: `RID<class_RID>`, active: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__space_set_active>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_space_set_debug_contacts**(space: `RID<class_RID>`, max_contacts: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__space_set_debug_contacts>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_space_set_param**(space: `RID<class_RID>`, param: `SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`, value: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__space_set_param>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_sphere_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__sphere_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_step**(step: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__step>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_sync**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__sync>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`RID<class_RID>` **\_world_boundary_shape_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsServer3DExtension_private_method__world_boundary_shape_create>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **body_test_motion_is_excluding_body**(body: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_body>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **body_test_motion_is_excluding_object**(object: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_object>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!