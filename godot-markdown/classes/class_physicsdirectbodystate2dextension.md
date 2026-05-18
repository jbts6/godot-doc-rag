github_url
hide

# PhysicsDirectBodyState2DExtension

**Inherits:** `PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>` **\<** `Object<class_Object>`

Provides virtual methods that can be overridden to create custom `PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>` implementations.

classref-introduction-group

## Description

This class extends `PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>` by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of `PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_add_constant_central_force**(force: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__add_constant_central_force>`

Overridable version of `PhysicsDirectBodyState2D.add_constant_central_force()<class_PhysicsDirectBodyState2D_method_add_constant_central_force>`.

classref-item-separator

classref-method

`void (No return value.)` **\_add_constant_force**(force: `Vector2<class_Vector2>`, position: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__add_constant_force>`

Overridable version of `PhysicsDirectBodyState2D.add_constant_force()<class_PhysicsDirectBodyState2D_method_add_constant_force>`.

classref-item-separator

classref-method

`void (No return value.)` **\_add_constant_torque**(torque: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__add_constant_torque>`

Overridable version of `PhysicsDirectBodyState2D.add_constant_torque()<class_PhysicsDirectBodyState2D_method_add_constant_torque>`.

classref-item-separator

classref-method

`void (No return value.)` **\_apply_central_force**(force: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_central_force>`

Overridable version of `PhysicsDirectBodyState2D.apply_central_force()<class_PhysicsDirectBodyState2D_method_apply_central_force>`.

classref-item-separator

classref-method

`void (No return value.)` **\_apply_central_impulse**(impulse: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_central_impulse>`

Overridable version of `PhysicsDirectBodyState2D.apply_central_impulse()<class_PhysicsDirectBodyState2D_method_apply_central_impulse>`.

classref-item-separator

classref-method

`void (No return value.)` **\_apply_force**(force: `Vector2<class_Vector2>`, position: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_force>`

Overridable version of `PhysicsDirectBodyState2D.apply_force()<class_PhysicsDirectBodyState2D_method_apply_force>`.

classref-item-separator

classref-method

`void (No return value.)` **\_apply_impulse**(impulse: `Vector2<class_Vector2>`, position: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_impulse>`

Overridable version of `PhysicsDirectBodyState2D.apply_impulse()<class_PhysicsDirectBodyState2D_method_apply_impulse>`.

classref-item-separator

classref-method

`void (No return value.)` **\_apply_torque**(torque: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_torque>`

Overridable version of `PhysicsDirectBodyState2D.apply_torque()<class_PhysicsDirectBodyState2D_method_apply_torque>`.

classref-item-separator

classref-method

`void (No return value.)` **\_apply_torque_impulse**(impulse: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__apply_torque_impulse>`

Overridable version of `PhysicsDirectBodyState2D.apply_torque_impulse()<class_PhysicsDirectBodyState2D_method_apply_torque_impulse>`.

classref-item-separator

classref-method

`float<class_float>` **\_get_angular_velocity**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_angular_velocity>`

Implement to override the behavior of `PhysicsDirectBodyState2D.angular_velocity<class_PhysicsDirectBodyState2D_property_angular_velocity>` and its respective getter.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_center_of_mass**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_center_of_mass>`

Implement to override the behavior of `PhysicsDirectBodyState2D.center_of_mass<class_PhysicsDirectBodyState2D_property_center_of_mass>` and its respective getter.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_center_of_mass_local**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_center_of_mass_local>`

Implement to override the behavior of `PhysicsDirectBodyState2D.center_of_mass_local<class_PhysicsDirectBodyState2D_property_center_of_mass_local>` and its respective getter.

classref-item-separator

classref-method

`int<class_int>` **\_get_collision_layer**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_get_collision_mask**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_constant_force**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_constant_force>`

Overridable version of `PhysicsDirectBodyState2D.get_constant_force()<class_PhysicsDirectBodyState2D_method_get_constant_force>`.

classref-item-separator

classref-method

`float<class_float>` **\_get_constant_torque**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_constant_torque>`

Overridable version of `PhysicsDirectBodyState2D.get_constant_torque()<class_PhysicsDirectBodyState2D_method_get_constant_torque>`.

classref-item-separator

classref-method

`RID<class_RID>` **\_get_contact_collider**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_collider()<class_PhysicsDirectBodyState2D_method_get_contact_collider>`.

classref-item-separator

classref-method

`int<class_int>` **\_get_contact_collider_id**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_id>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_collider_id()<class_PhysicsDirectBodyState2D_method_get_contact_collider_id>`.

classref-item-separator

classref-method

`Object<class_Object>` **\_get_contact_collider_object**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_object>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_collider_object()<class_PhysicsDirectBodyState2D_method_get_contact_collider_object>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_contact_collider_position**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_position>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_collider_position()<class_PhysicsDirectBodyState2D_method_get_contact_collider_position>`.

classref-item-separator

classref-method

`int<class_int>` **\_get_contact_collider_shape**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_shape>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_collider_shape()<class_PhysicsDirectBodyState2D_method_get_contact_collider_shape>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_contact_collider_velocity_at_position**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_collider_velocity_at_position>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_collider_velocity_at_position()<class_PhysicsDirectBodyState2D_method_get_contact_collider_velocity_at_position>`.

classref-item-separator

classref-method

`int<class_int>` **\_get_contact_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_count>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_count()<class_PhysicsDirectBodyState2D_method_get_contact_count>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_contact_impulse**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_impulse>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_impulse()<class_PhysicsDirectBodyState2D_method_get_contact_impulse>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_contact_local_normal**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_normal>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_local_normal()<class_PhysicsDirectBodyState2D_method_get_contact_local_normal>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_contact_local_position**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_position>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_local_position()<class_PhysicsDirectBodyState2D_method_get_contact_local_position>`.

classref-item-separator

classref-method

`int<class_int>` **\_get_contact_local_shape**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_shape>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_local_shape()<class_PhysicsDirectBodyState2D_method_get_contact_local_shape>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_contact_local_velocity_at_position**(contact_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_contact_local_velocity_at_position>`

Overridable version of `PhysicsDirectBodyState2D.get_contact_local_velocity_at_position()<class_PhysicsDirectBodyState2D_method_get_contact_local_velocity_at_position>`.

classref-item-separator

classref-method

`float<class_float>` **\_get_inverse_inertia**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_inverse_inertia>`

Implement to override the behavior of `PhysicsDirectBodyState2D.inverse_inertia<class_PhysicsDirectBodyState2D_property_inverse_inertia>` and its respective getter.

classref-item-separator

classref-method

`float<class_float>` **\_get_inverse_mass**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_inverse_mass>`

Implement to override the behavior of `PhysicsDirectBodyState2D.inverse_mass<class_PhysicsDirectBodyState2D_property_inverse_mass>` and its respective getter.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_linear_velocity**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_linear_velocity>`

Implement to override the behavior of `PhysicsDirectBodyState2D.linear_velocity<class_PhysicsDirectBodyState2D_property_linear_velocity>` and its respective getter.

classref-item-separator

classref-method

`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>` **\_get_space_state**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_space_state>`

Overridable version of `PhysicsDirectBodyState2D.get_space_state()<class_PhysicsDirectBodyState2D_method_get_space_state>`.

classref-item-separator

classref-method

`float<class_float>` **\_get_step**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_step>`

Implement to override the behavior of `PhysicsDirectBodyState2D.step<class_PhysicsDirectBodyState2D_property_step>` and its respective getter.

classref-item-separator

classref-method

`float<class_float>` **\_get_total_angular_damp**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_total_angular_damp>`

Implement to override the behavior of `PhysicsDirectBodyState2D.total_angular_damp<class_PhysicsDirectBodyState2D_property_total_angular_damp>` and its respective getter.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_total_gravity**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_total_gravity>`

Implement to override the behavior of `PhysicsDirectBodyState2D.total_gravity<class_PhysicsDirectBodyState2D_property_total_gravity>` and its respective getter.

classref-item-separator

classref-method

`float<class_float>` **\_get_total_linear_damp**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_total_linear_damp>`

Implement to override the behavior of `PhysicsDirectBodyState2D.total_linear_damp<class_PhysicsDirectBodyState2D_property_total_linear_damp>` and its respective getter.

classref-item-separator

classref-method

`Transform2D<class_Transform2D>` **\_get_transform**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_transform>`

Implement to override the behavior of `PhysicsDirectBodyState2D.transform<class_PhysicsDirectBodyState2D_property_transform>` and its respective getter.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_velocity_at_local_position**(local_position: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__get_velocity_at_local_position>`

Overridable version of `PhysicsDirectBodyState2D.get_velocity_at_local_position()<class_PhysicsDirectBodyState2D_method_get_velocity_at_local_position>`.

classref-item-separator

classref-method

`void (No return value.)` **\_integrate_forces**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__integrate_forces>`

Overridable version of `PhysicsDirectBodyState2D.integrate_forces()<class_PhysicsDirectBodyState2D_method_integrate_forces>`.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_sleeping**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__is_sleeping>`

Implement to override the behavior of `PhysicsDirectBodyState2D.sleeping<class_PhysicsDirectBodyState2D_property_sleeping>` and its respective getter.

classref-item-separator

classref-method

`void (No return value.)` **\_set_angular_velocity**(velocity: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_angular_velocity>`

Implement to override the behavior of `PhysicsDirectBodyState2D.angular_velocity<class_PhysicsDirectBodyState2D_property_angular_velocity>` and its respective setter.

classref-item-separator

classref-method

`void (No return value.)` **\_set_collision_layer**(layer: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_collision_layer>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_set_collision_mask**(mask: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_collision_mask>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_set_constant_force**(force: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_constant_force>`

Overridable version of `PhysicsDirectBodyState2D.set_constant_force()<class_PhysicsDirectBodyState2D_method_set_constant_force>`.

classref-item-separator

classref-method

`void (No return value.)` **\_set_constant_torque**(torque: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_constant_torque>`

Overridable version of `PhysicsDirectBodyState2D.set_constant_torque()<class_PhysicsDirectBodyState2D_method_set_constant_torque>`.

classref-item-separator

classref-method

`void (No return value.)` **\_set_linear_velocity**(velocity: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_linear_velocity>`

Implement to override the behavior of `PhysicsDirectBodyState2D.linear_velocity<class_PhysicsDirectBodyState2D_property_linear_velocity>` and its respective setter.

classref-item-separator

classref-method

`void (No return value.)` **\_set_sleep_state**(enabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_sleep_state>`

Implement to override the behavior of `PhysicsDirectBodyState2D.sleeping<class_PhysicsDirectBodyState2D_property_sleeping>` and its respective setter.

classref-item-separator

classref-method

`void (No return value.)` **\_set_transform**(transform: `Transform2D<class_Transform2D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectBodyState2DExtension_private_method__set_transform>`

Implement to override the behavior of `PhysicsDirectBodyState2D.transform<class_PhysicsDirectBodyState2D_property_transform>` and its respective setter.