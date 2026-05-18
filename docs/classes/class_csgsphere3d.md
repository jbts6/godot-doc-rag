github_url
hide

# CSGSphere3D

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>` **\<** `CSGShape3D<class_CSGShape3D>` **\<** `GeometryInstance3D<class_GeometryInstance3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A CSG Sphere shape.

classref-introduction-group

## Description

This node allows you to create a sphere for use with the CSG system.

**Note:** CSG nodes are intended to be used for level prototyping. Creating CSG nodes has a significant CPU cost compared to creating a `MeshInstance3D<class_MeshInstance3D>` with a `PrimitiveMesh<class_PrimitiveMesh>`. Moving a CSG node within another CSG node also has a significant CPU cost, so it should be avoided during gameplay.

classref-introduction-group

## Tutorials

- `Prototyping levels with CSG <../tutorials/3d/csg_tools>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Material<class_Material>` **material** `🔗<class_CSGSphere3D_property_material>`

classref-property-setget

- `void (No return value.)` **set_material**(value: `Material<class_Material>`)
- `Material<class_Material>` **get_material**()

The material used to render the sphere.

classref-item-separator

classref-property

`int<class_int>` **radial_segments** = `12` `🔗<class_CSGSphere3D_property_radial_segments>`

classref-property-setget

- `void (No return value.)` **set_radial_segments**(value: `int<class_int>`)
- `int<class_int>` **get_radial_segments**()

Number of vertical slices for the sphere.

classref-item-separator

classref-property

`float<class_float>` **radius** = `0.5` `🔗<class_CSGSphere3D_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

Radius of the sphere.

classref-item-separator

classref-property

`int<class_int>` **rings** = `6` `🔗<class_CSGSphere3D_property_rings>`

classref-property-setget

- `void (No return value.)` **set_rings**(value: `int<class_int>`)
- `int<class_int>` **get_rings**()

Number of horizontal slices for the sphere.

classref-item-separator

classref-property

`bool<class_bool>` **smooth_faces** = `true` `🔗<class_CSGSphere3D_property_smooth_faces>`

classref-property-setget

- `void (No return value.)` **set_smooth_faces**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_smooth_faces**()

If `true` the normals of the sphere are set to give a smooth effect making the sphere seem rounded. If `false` the sphere will have a flat shaded look.