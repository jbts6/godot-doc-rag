github_url
hide

# PrimitiveMesh

**Inherits:** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `BoxMesh<class_BoxMesh>`, `CapsuleMesh<class_CapsuleMesh>`, `CylinderMesh<class_CylinderMesh>`, `PlaneMesh<class_PlaneMesh>`, `PointMesh<class_PointMesh>`, `PrismMesh<class_PrismMesh>`, `RibbonTrailMesh<class_RibbonTrailMesh>`, `SphereMesh<class_SphereMesh>`, `TextMesh<class_TextMesh>`, `TorusMesh<class_TorusMesh>`, `TubeTrailMesh<class_TubeTrailMesh>`

Base class for all primitive meshes. Handles applying a `Material<class_Material>` to a primitive mesh.

classref-introduction-group

## Description

Base class for all primitive meshes. Handles applying a `Material<class_Material>` to a primitive mesh. Examples include `BoxMesh<class_BoxMesh>`, `CapsuleMesh<class_CapsuleMesh>`, `CylinderMesh<class_CylinderMesh>`, `PlaneMesh<class_PlaneMesh>`, `PrismMesh<class_PrismMesh>`, and `SphereMesh<class_SphereMesh>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **add_uv2** = `false` `🔗<class_PrimitiveMesh_property_add_uv2>`

classref-property-setget

- `void (No return value.)` **set_add_uv2**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_add_uv2**()

If set, generates UV2 UV coordinates applying a padding using the `uv2_padding<class_PrimitiveMesh_property_uv2_padding>` setting. UV2 is needed for lightmapping.

classref-item-separator

classref-property

`AABB<class_AABB>` **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` `🔗<class_PrimitiveMesh_property_custom_aabb>`

classref-property-setget

- `void (No return value.)` **set_custom_aabb**(value: `AABB<class_AABB>`)
- `AABB<class_AABB>` **get_custom_aabb**()

Overrides the `AABB<class_AABB>` with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

classref-item-separator

classref-property

`bool<class_bool>` **flip_faces** = `false` `🔗<class_PrimitiveMesh_property_flip_faces>`

classref-property-setget

- `void (No return value.)` **set_flip_faces**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_flip_faces**()

If `true`, the order of the vertices in each triangle is reversed, resulting in the backside of the mesh being drawn.

This gives the same result as using `BaseMaterial3D.CULL_FRONT<class_BaseMaterial3D_constant_CULL_FRONT>` in `BaseMaterial3D.cull_mode<class_BaseMaterial3D_property_cull_mode>`.

classref-item-separator

classref-property

`Material<class_Material>` **material** `🔗<class_PrimitiveMesh_property_material>`

classref-property-setget

- `void (No return value.)` **set_material**(value: `Material<class_Material>`)
- `Material<class_Material>` **get_material**()

The current `Material<class_Material>` of the primitive mesh.

classref-item-separator

classref-property

`float<class_float>` **uv2_padding** = `2.0` `🔗<class_PrimitiveMesh_property_uv2_padding>`

classref-property-setget

- `void (No return value.)` **set_uv2_padding**(value: `float<class_float>`)
- `float<class_float>` **get_uv2_padding**()

If `add_uv2<class_PrimitiveMesh_property_add_uv2>` is set, specifies the padding in pixels applied along seams of the mesh. Lower padding values allow making better use of the lightmap texture (resulting in higher texel density), but may introduce visible lightmap bleeding along edges.

If the size of the lightmap texture can't be determined when generating the mesh, UV2 is calculated assuming a texture size of 1024x1024.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Array<class_Array>` **\_create_mesh_array**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PrimitiveMesh_private_method__create_mesh_array>`

Override this method to customize how this primitive mesh should be generated. Should return an `Array<class_Array>` where each element is another Array of values required for the mesh (see the `ArrayType<enum_Mesh_ArrayType>` constants).

classref-item-separator

classref-method

`Array<class_Array>` **get_mesh_arrays**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PrimitiveMesh_method_get_mesh_arrays>`

Returns the mesh arrays used to make up the surface of this primitive mesh.

**Example:** Pass the result to `ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>` to create a new surface:

gdscript

var c = CylinderMesh.new() var arr_mesh = ArrayMesh.new() arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, c.get_mesh_arrays())

csharp

var c = new CylinderMesh(); var arrMesh = new ArrayMesh(); arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, c.GetMeshArrays());

classref-item-separator

classref-method

`void (No return value.)` **request_update**() `🔗<class_PrimitiveMesh_method_request_update>`

Request an update of this primitive mesh based on its properties.