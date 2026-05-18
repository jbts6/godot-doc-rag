github_url
hide

# MultiMeshInstance3D

**Inherits:** `GeometryInstance3D<class_GeometryInstance3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Node that instances a `MultiMesh<class_MultiMesh>`.

classref-introduction-group

## Description

**MultiMeshInstance3D** is a specialized node to instance `GeometryInstance3D<class_GeometryInstance3D>`s based on a `MultiMesh<class_MultiMesh>` resource.

This is useful to optimize the rendering of a high number of instances of a given mesh (for example trees in a forest or grass strands).

classref-introduction-group

## Tutorials

- `Using MultiMeshInstance <../tutorials/3d/using_multi_mesh_instance>`
- `Optimization using MultiMeshes <../tutorials/performance/using_multimesh>`
- `Animating thousands of fish with MultiMeshInstance <../tutorials/performance/vertex_animation/animating_thousands_of_fish>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`MultiMesh<class_MultiMesh>` **multimesh** `🔗<class_MultiMeshInstance3D_property_multimesh>`

classref-property-setget

- `void (No return value.)` **set_multimesh**(value: `MultiMesh<class_MultiMesh>`)
- `MultiMesh<class_MultiMesh>` **get_multimesh**()

The `MultiMesh<class_MultiMesh>` resource that will be used and shared among all instances of the **MultiMeshInstance3D**.