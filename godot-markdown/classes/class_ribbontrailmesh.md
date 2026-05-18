github_url
hide

# RibbonTrailMesh

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>` **\<** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a straight ribbon-shaped `PrimitiveMesh<class_PrimitiveMesh>` with variable width.

classref-introduction-group

## Description

**RibbonTrailMesh** represents a straight ribbon-shaped mesh with variable width. The ribbon is composed of a number of flat or cross-shaped sections, each with the same `section_length<class_RibbonTrailMesh_property_section_length>` and number of `section_segments<class_RibbonTrailMesh_property_section_segments>`. A `curve<class_RibbonTrailMesh_property_curve>` is sampled along the total length of the ribbon, meaning that the curve determines the size of the ribbon along its length.

This primitive mesh is usually used for particle trails.

classref-introduction-group

## Tutorials

- `3D Particle trails <../tutorials/3d/particles/trails>`
- `Particle systems (3D) <../tutorials/3d/particles/index>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Shape**: `🔗<enum_RibbonTrailMesh_Shape>`

classref-enumeration-constant

`Shape<enum_RibbonTrailMesh_Shape>` **SHAPE_FLAT** = `0`

Gives the mesh a single flat face.

classref-enumeration-constant

`Shape<enum_RibbonTrailMesh_Shape>` **SHAPE_CROSS** = `1`

Gives the mesh two perpendicular flat faces, making a cross shape.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Curve<class_Curve>` **curve** `🔗<class_RibbonTrailMesh_property_curve>`

classref-property-setget

- `void (No return value.)` **set_curve**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_curve**()

Determines the size of the ribbon along its length. The size of a particular section segment is obtained by multiplying the baseline `size<class_RibbonTrailMesh_property_size>` by the value of this curve at the given distance. For values smaller than `0`, the faces will be inverted. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **section_length** = `0.2` `🔗<class_RibbonTrailMesh_property_section_length>`

classref-property-setget

- `void (No return value.)` **set_section_length**(value: `float<class_float>`)
- `float<class_float>` **get_section_length**()

The length of a section of the ribbon.

classref-item-separator

classref-property

`int<class_int>` **section_segments** = `3` `🔗<class_RibbonTrailMesh_property_section_segments>`

classref-property-setget

- `void (No return value.)` **set_section_segments**(value: `int<class_int>`)
- `int<class_int>` **get_section_segments**()

The number of segments in a section. The `curve<class_RibbonTrailMesh_property_curve>` is sampled on each segment to determine its size. Higher values result in a more detailed ribbon at the cost of performance.

classref-item-separator

classref-property

`int<class_int>` **sections** = `5` `🔗<class_RibbonTrailMesh_property_sections>`

classref-property-setget

- `void (No return value.)` **set_sections**(value: `int<class_int>`)
- `int<class_int>` **get_sections**()

The total number of sections on the ribbon.

classref-item-separator

classref-property

`Shape<enum_RibbonTrailMesh_Shape>` **shape** = `1` `🔗<class_RibbonTrailMesh_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Shape<enum_RibbonTrailMesh_Shape>`)
- `Shape<enum_RibbonTrailMesh_Shape>` **get_shape**()

Determines the shape of the ribbon.

classref-item-separator

classref-property

`float<class_float>` **size** = `1.0` `🔗<class_RibbonTrailMesh_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `float<class_float>`)
- `float<class_float>` **get_size**()

The baseline size of the ribbon. The size of a particular section segment is obtained by multiplying this size by the value of the `curve<class_RibbonTrailMesh_property_curve>` at the given distance.