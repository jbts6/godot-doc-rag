github_url
hide

# SphereMesh

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>` **\<** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Class representing a spherical `PrimitiveMesh<class_PrimitiveMesh>`.

classref-introduction-group

## Description

Class representing a spherical `PrimitiveMesh<class_PrimitiveMesh>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **height** = `1.0` `🔗<class_SphereMesh_property_height>`

classref-property-setget

- `void (No return value.)` **set_height**(value: `float<class_float>`)
- `float<class_float>` **get_height**()

Full height of the sphere.

classref-item-separator

classref-property

`bool<class_bool>` **is_hemisphere** = `false` `🔗<class_SphereMesh_property_is_hemisphere>`

classref-property-setget

- `void (No return value.)` **set_is_hemisphere**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_is_hemisphere**()

If `true`, a hemisphere is created rather than a full sphere.

**Note:** To get a regular hemisphere, the height and radius of the sphere must be equal.

classref-item-separator

classref-property

`int<class_int>` **radial_segments** = `64` `🔗<class_SphereMesh_property_radial_segments>`

classref-property-setget

- `void (No return value.)` **set_radial_segments**(value: `int<class_int>`)
- `int<class_int>` **get_radial_segments**()

Number of radial segments on the sphere.

classref-item-separator

classref-property

`float<class_float>` **radius** = `0.5` `🔗<class_SphereMesh_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

Radius of sphere.

classref-item-separator

classref-property

`int<class_int>` **rings** = `32` `🔗<class_SphereMesh_property_rings>`

classref-property-setget

- `void (No return value.)` **set_rings**(value: `int<class_int>`)
- `int<class_int>` **get_rings**()

Number of segments along the height of the sphere.