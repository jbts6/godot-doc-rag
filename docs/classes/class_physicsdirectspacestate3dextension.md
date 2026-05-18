github_url
hide

# PhysicsDirectSpaceState3DExtension

**Inherits:** `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` **\<** `Object<class_Object>`

Provides virtual methods that can be overridden to create custom `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` implementations.

classref-introduction-group

## Description

This class extends `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>` by providing additional virtual methods that can be overridden. When these methods are overridden, they will be called instead of the internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **\_cast_motion**(shape_rid: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`, motion: `Vector3<class_Vector3>`, margin: `float<class_float>`, collision_mask: `int<class_int>`, collide_with_bodies: `bool<class_bool>`, collide_with_areas: `bool<class_bool>`, r_closest_safe: `float*`, r_closest_unsafe: `float*`, r_info: `PhysicsServer3DExtensionShapeRestInfo*`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__cast_motion>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_collide_shape**(shape_rid: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`, motion: `Vector3<class_Vector3>`, margin: `float<class_float>`, collision_mask: `int<class_int>`, collide_with_bodies: `bool<class_bool>`, collide_with_areas: `bool<class_bool>`, r_results: `void*`, max_results: `int<class_int>`, r_result_count: `int32_t*`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__collide_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_get_closest_point_to_object_volume**(object: `RID<class_RID>`, point: `Vector3<class_Vector3>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__get_closest_point_to_object_volume>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_intersect_point**(position: `Vector3<class_Vector3>`, collision_mask: `int<class_int>`, collide_with_bodies: `bool<class_bool>`, collide_with_areas: `bool<class_bool>`, r_results: `PhysicsServer3DExtensionShapeResult*`, max_results: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_point>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_intersect_ray**(from: `Vector3<class_Vector3>`, to: `Vector3<class_Vector3>`, collision_mask: `int<class_int>`, collide_with_bodies: `bool<class_bool>`, collide_with_areas: `bool<class_bool>`, hit_from_inside: `bool<class_bool>`, hit_back_faces: `bool<class_bool>`, pick_ray: `bool<class_bool>`, r_result: `PhysicsServer3DExtensionRayResult*`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_ray>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_intersect_shape**(shape_rid: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`, motion: `Vector3<class_Vector3>`, margin: `float<class_float>`, collision_mask: `int<class_int>`, collide_with_bodies: `bool<class_bool>`, collide_with_areas: `bool<class_bool>`, r_result_count: `PhysicsServer3DExtensionShapeResult*`, max_results: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__intersect_shape>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_rest_info**(shape_rid: `RID<class_RID>`, transform: `Transform3D<class_Transform3D>`, motion: `Vector3<class_Vector3>`, margin: `float<class_float>`, collision_mask: `int<class_int>`, collide_with_bodies: `bool<class_bool>`, collide_with_areas: `bool<class_bool>`, r_rest_info: `PhysicsServer3DExtensionShapeRestInfo*`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_PhysicsDirectSpaceState3DExtension_private_method__rest_info>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **is_body_excluded_from_query**(body: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PhysicsDirectSpaceState3DExtension_method_is_body_excluded_from_query>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!