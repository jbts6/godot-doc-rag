github_url
hide

# GLTFPhysicsBody

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a glTF physics body.

classref-introduction-group

## Description

Represents a physics body as an intermediary between the `OMI_physics_body` glTF data and Godot's nodes, and it's abstracted in a way that allows adding support for different glTF physics extensions in the future.

classref-introduction-group

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`
- [OMI_physics_body glTF extension](https://github.com/omigroup/gltf-extensions/tree/main/extensions/2.0/OMI_physics_body)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector3<class_Vector3>` **angular_velocity** = `Vector3(0, 0, 0)` `🔗<class_GLTFPhysicsBody_property_angular_velocity>`

classref-property-setget

- `void (No return value.)` **set_angular_velocity**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_angular_velocity**()

The angular velocity of the physics body, in radians per second. This is only used when the body type is "rigid" or "vehicle".

classref-item-separator

classref-property

`String<class_String>` **body_type** = `"rigid"` `🔗<class_GLTFPhysicsBody_property_body_type>`

classref-property-setget

- `void (No return value.)` **set_body_type**(value: `String<class_String>`)
- `String<class_String>` **get_body_type**()

The type of the body.

When importing, this controls what type of `CollisionObject3D<class_CollisionObject3D>` node Godot should generate. Valid values are `"static"`, `"animatable"`, `"character"`, `"rigid"`, `"vehicle"`, and `"trigger"`.

When exporting, this will be squashed down to one of `"static"`, `"kinematic"`, or `"dynamic"` motion types, or the `"trigger"` property.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **center_of_mass** = `Vector3(0, 0, 0)` `🔗<class_GLTFPhysicsBody_property_center_of_mass>`

classref-property-setget

- `void (No return value.)` **set_center_of_mass**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_center_of_mass**()

The center of mass of the body, in meters. This is in local space relative to the body. By default, the center of the mass is the body's origin.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **inertia_diagonal** = `Vector3(0, 0, 0)` `🔗<class_GLTFPhysicsBody_property_inertia_diagonal>`

classref-property-setget

- `void (No return value.)` **set_inertia_diagonal**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_inertia_diagonal**()

The inertia strength of the physics body, in kilogram meter squared (kg⋅m²). This represents the inertia around the principle axes, the diagonal of the inertia tensor matrix. This is only used when the body type is "rigid" or "vehicle".

When converted to a Godot `RigidBody3D<class_RigidBody3D>` node, if this value is zero, then the inertia will be calculated automatically.

classref-item-separator

classref-property

`Quaternion<class_Quaternion>` **inertia_orientation** = `Quaternion(0, 0, 0, 1)` `🔗<class_GLTFPhysicsBody_property_inertia_orientation>`

classref-property-setget

- `void (No return value.)` **set_inertia_orientation**(value: `Quaternion<class_Quaternion>`)
- `Quaternion<class_Quaternion>` **get_inertia_orientation**()

The inertia orientation of the physics body. This defines the rotation of the inertia's principle axes relative to the object's local axes. This is only used when the body type is "rigid" or "vehicle" and `inertia_diagonal<class_GLTFPhysicsBody_property_inertia_diagonal>` is set to a non-zero value.

classref-item-separator

classref-property

`Basis<class_Basis>` **inertia_tensor** = `Basis(0, 0, 0, 0, 0, 0, 0, 0, 0)` `🔗<class_GLTFPhysicsBody_property_inertia_tensor>`

classref-property-setget

- `void (No return value.)` **set_inertia_tensor**(value: `Basis<class_Basis>`)
- `Basis<class_Basis>` **get_inertia_tensor**()

**Deprecated:** This property may be changed or removed in future versions.

The inertia tensor of the physics body, in kilogram meter squared (kg⋅m²). This is only used when the body type is "rigid" or "vehicle".

When converted to a Godot `RigidBody3D<class_RigidBody3D>` node, if this value is zero, then the inertia will be calculated automatically.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **linear_velocity** = `Vector3(0, 0, 0)` `🔗<class_GLTFPhysicsBody_property_linear_velocity>`

classref-property-setget

- `void (No return value.)` **set_linear_velocity**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_linear_velocity**()

The linear velocity of the physics body, in meters per second. This is only used when the body type is "rigid" or "vehicle".

classref-item-separator

classref-property

`float<class_float>` **mass** = `1.0` `🔗<class_GLTFPhysicsBody_property_mass>`

classref-property-setget

- `void (No return value.)` **set_mass**(value: `float<class_float>`)
- `float<class_float>` **get_mass**()

The mass of the physics body, in kilograms. This is only used when the body type is "rigid" or "vehicle".

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`GLTFPhysicsBody<class_GLTFPhysicsBody>` **from_dictionary**(dictionary: `Dictionary<class_Dictionary>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_GLTFPhysicsBody_method_from_dictionary>`

Creates a new GLTFPhysicsBody instance by parsing the given `Dictionary<class_Dictionary>` in the `OMI_physics_body` glTF extension format.

classref-item-separator

classref-method

`GLTFPhysicsBody<class_GLTFPhysicsBody>` **from_node**(body_node: `CollisionObject3D<class_CollisionObject3D>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_GLTFPhysicsBody_method_from_node>`

Creates a new GLTFPhysicsBody instance from the given Godot `CollisionObject3D<class_CollisionObject3D>` node.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **to_dictionary**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFPhysicsBody_method_to_dictionary>`

Serializes this GLTFPhysicsBody instance into a `Dictionary<class_Dictionary>`. It will be in the format expected by the `OMI_physics_body` glTF extension.

classref-item-separator

classref-method

`CollisionObject3D<class_CollisionObject3D>` **to_node**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFPhysicsBody_method_to_node>`

Converts this GLTFPhysicsBody instance into a Godot `CollisionObject3D<class_CollisionObject3D>` node.