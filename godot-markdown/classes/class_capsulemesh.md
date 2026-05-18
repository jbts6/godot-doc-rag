github_url
hide

# CapsuleMesh

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>` **\<** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Class representing a capsule-shaped `PrimitiveMesh<class_PrimitiveMesh>`.

classref-introduction-group

## Description

Class representing a capsule-shaped `PrimitiveMesh<class_PrimitiveMesh>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **height** = `2.0` `🔗<class_CapsuleMesh_property_height>`

classref-property-setget

- `void (No return value.)` **set_height**(value: `float<class_float>`)
- `float<class_float>` **get_height**()

Total height of the capsule mesh (including the hemispherical ends).

**Note:** The `height<class_CapsuleMesh_property_height>` of a capsule must be at least twice its `radius<class_CapsuleMesh_property_radius>`. Otherwise, the capsule becomes a circle. If the `height<class_CapsuleMesh_property_height>` is less than twice the `radius<class_CapsuleMesh_property_radius>`, the properties adjust to a valid value.

classref-item-separator

classref-property

`int<class_int>` **radial_segments** = `64` `🔗<class_CapsuleMesh_property_radial_segments>`

classref-property-setget

- `void (No return value.)` **set_radial_segments**(value: `int<class_int>`)
- `int<class_int>` **get_radial_segments**()

Number of radial segments on the capsule mesh.

classref-item-separator

classref-property

`float<class_float>` **radius** = `0.5` `🔗<class_CapsuleMesh_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

Radius of the capsule mesh.

**Note:** The `radius<class_CapsuleMesh_property_radius>` of a capsule cannot be greater than half of its `height<class_CapsuleMesh_property_height>`. Otherwise, the capsule becomes a circle. If the `radius<class_CapsuleMesh_property_radius>` is greater than half of the `height<class_CapsuleMesh_property_height>`, the properties adjust to a valid value.

classref-item-separator

classref-property

`int<class_int>` **rings** = `8` `🔗<class_CapsuleMesh_property_rings>`

classref-property-setget

- `void (No return value.)` **set_rings**(value: `int<class_int>`)
- `int<class_int>` **get_rings**()

Number of rings along the height of the capsule.