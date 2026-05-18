github_url
hide

# CSGBox3D

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>` **\<** `CSGShape3D<class_CSGShape3D>` **\<** `GeometryInstance3D<class_GeometryInstance3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A CSG Box shape.

classref-introduction-group

## Description

This node allows you to create a box for use with the CSG system.

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

`Material<class_Material>` **material** `🔗<class_CSGBox3D_property_material>`

classref-property-setget

- `void (No return value.)` **set_material**(value: `Material<class_Material>`)
- `Material<class_Material>` **get_material**()

The material used to render the box.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **size** = `Vector3(1, 1, 1)` `🔗<class_CSGBox3D_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_size**()

The box's width, height and depth.