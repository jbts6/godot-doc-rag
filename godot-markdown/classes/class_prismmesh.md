github_url
hide

# PrismMesh

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>` **\<** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Class representing a prism-shaped `PrimitiveMesh<class_PrimitiveMesh>`.

classref-introduction-group

## Description

Class representing a prism-shaped `PrimitiveMesh<class_PrimitiveMesh>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **left_to_right** = `0.5` `🔗<class_PrismMesh_property_left_to_right>`

classref-property-setget

- `void (No return value.)` **set_left_to_right**(value: `float<class_float>`)
- `float<class_float>` **get_left_to_right**()

Displacement of the upper edge along the X axis. 0.0 positions edge straight above the bottom-left edge.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **size** = `Vector3(1, 1, 1)` `🔗<class_PrismMesh_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_size**()

Size of the prism.

classref-item-separator

classref-property

`int<class_int>` **subdivide_depth** = `0` `🔗<class_PrismMesh_property_subdivide_depth>`

classref-property-setget

- `void (No return value.)` **set_subdivide_depth**(value: `int<class_int>`)
- `int<class_int>` **get_subdivide_depth**()

Number of added edge loops along the Z axis.

classref-item-separator

classref-property

`int<class_int>` **subdivide_height** = `0` `🔗<class_PrismMesh_property_subdivide_height>`

classref-property-setget

- `void (No return value.)` **set_subdivide_height**(value: `int<class_int>`)
- `int<class_int>` **get_subdivide_height**()

Number of added edge loops along the Y axis.

classref-item-separator

classref-property

`int<class_int>` **subdivide_width** = `0` `🔗<class_PrismMesh_property_subdivide_width>`

classref-property-setget

- `void (No return value.)` **set_subdivide_width**(value: `int<class_int>`)
- `int<class_int>` **get_subdivide_width**()

Number of added edge loops along the X axis.