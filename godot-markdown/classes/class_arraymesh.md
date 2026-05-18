github_url
hide

# ArrayMesh

**Inherits:** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

`Mesh<class_Mesh>` type that provides utility for constructing a surface from arrays.

classref-introduction-group

## Description

The **ArrayMesh** is used to construct a `Mesh<class_Mesh>` by specifying the attributes as arrays.

The most basic example is the creation of a single triangle:

gdscript

var vertices = PackedVector3Array() vertices.push_back(Vector3(0, 1, 0)) vertices.push_back(Vector3(1, 0, 0)) vertices.push_back(Vector3(0, 0, 1))

\# Initialize the ArrayMesh. var arr_mesh = ArrayMesh.new() var arrays = \[\] arrays.resize(Mesh.ARRAY_MAX) arrays\[Mesh.ARRAY_VERTEX\] = vertices

\# Create the Mesh. arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays) var m = MeshInstance3D.new() m.mesh = arr_mesh

csharp

Vector3\[\] vertices = \[ new Vector3(0, 1, 0), new Vector3(1, 0, 0), new Vector3(0, 0, 1), \];

// Initialize the ArrayMesh. var arrMesh = new ArrayMesh(); Godot.Collections.Array arrays = \[\]; arrays.Resize((int)Mesh.ArrayType.Max); arrays\[(int)Mesh.ArrayType.Vertex\] = vertices;

// Create the Mesh. arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays); var m = new MeshInstance3D(); m.Mesh = arrMesh;

The `MeshInstance3D<class_MeshInstance3D>` is ready to be added to the `SceneTree<class_SceneTree>` to be shown.

See also `ImmediateMesh<class_ImmediateMesh>`, `MeshDataTool<class_MeshDataTool>` and `SurfaceTool<class_SurfaceTool>` for procedural geometry generation.

**Note:** Godot uses clockwise [winding order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front faces of triangle primitive modes.

classref-introduction-group

## Tutorials

- `Procedural geometry using the ArrayMesh <../tutorials/3d/procedural_geometry/arraymesh>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BlendShapeMode<enum_Mesh_BlendShapeMode>` **blend_shape_mode** = `1` `🔗<class_ArrayMesh_property_blend_shape_mode>`

classref-property-setget

- `void (No return value.)` **set_blend_shape_mode**(value: `BlendShapeMode<enum_Mesh_BlendShapeMode>`)
- `BlendShapeMode<enum_Mesh_BlendShapeMode>` **get_blend_shape_mode**()

The blend shape mode.

classref-item-separator

classref-property

`AABB<class_AABB>` **custom_aabb** = `AABB(0, 0, 0, 0, 0, 0)` `🔗<class_ArrayMesh_property_custom_aabb>`

classref-property-setget

- `void (No return value.)` **set_custom_aabb**(value: `AABB<class_AABB>`)
- `AABB<class_AABB>` **get_custom_aabb**()

Overrides the `AABB<class_AABB>` with one defined by user for use with frustum culling. Especially useful to avoid unexpected culling when using a shader to offset vertices.

classref-item-separator

classref-property

`ArrayMesh<class_ArrayMesh>` **shadow_mesh** `🔗<class_ArrayMesh_property_shadow_mesh>`

classref-property-setget

- `void (No return value.)` **set_shadow_mesh**(value: `ArrayMesh<class_ArrayMesh>`)
- `ArrayMesh<class_ArrayMesh>` **get_shadow_mesh**()

An optional mesh which can be used for rendering shadows and the depth prepass. Can be used to increase performance by supplying a mesh with fused vertices and only vertex position data (without normals, UVs, colors, etc.).

**Note:** This mesh must have exactly the same vertex positions as the source mesh (including the source mesh's LODs, if present). If vertex positions differ, then the mesh will not draw correctly.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_blend_shape**(name: `StringName<class_StringName>`) `🔗<class_ArrayMesh_method_add_blend_shape>`

Adds name for a blend shape that will be added with `add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`. Must be called before surface is added.

classref-item-separator

classref-method

`void (No return value.)` **add_surface_from_arrays**(primitive: `PrimitiveType<enum_Mesh_PrimitiveType>`, arrays: `Array<class_Array>`, blend_shapes: `Array<class_Array>`\[`Array<class_Array>`\] = \[\], lods: `Dictionary<class_Dictionary>` = {}, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`ArrayFormat<enum_Mesh_ArrayFormat>`\] = 0) `🔗<class_ArrayMesh_method_add_surface_from_arrays>`

Creates a new surface. `Mesh.get_surface_count()<class_Mesh_method_get_surface_count>` will become the `surf_idx` for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be any of the values defined in `PrimitiveType<enum_Mesh_PrimitiveType>`.

The `arrays` argument is an array of arrays. Each of the `Mesh.ARRAY_MAX<class_Mesh_constant_ARRAY_MAX>` elements contains an array with some of the mesh data for this surface as described by the corresponding member of `ArrayType<enum_Mesh_ArrayType>` or `null` if it is not used by the surface. For example, `arrays[0]` is the array of vertices. That first vertex sub-array is always required; the others are optional. Adding an index array puts this surface into "index mode" where the vertex and other arrays become the sources of data and the index array defines the vertex order. All sub-arrays must have the same length as the vertex array (or be an exact multiple of the vertex array's length, when multiple elements of a sub-array correspond to a single vertex) or be empty, except for `Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>` if it is used.

The `blend_shapes` argument is an array of vertex data for each blend shape. Each element is an array of the same structure as `arrays`, but `Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>`, `Mesh.ARRAY_NORMAL<class_Mesh_constant_ARRAY_NORMAL>`, and `Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>` are set if and only if they are set in `arrays` and all other entries are `null`.

The `lods` argument is a dictionary with `float<class_float>` keys and `PackedInt32Array<class_PackedInt32Array>` values. Each entry in the dictionary represents an LOD level of the surface, where the value is the `Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>` array to use for the LOD level and the key is roughly proportional to the distance at which the LOD stats being used. I.e., increasing the key of an LOD also increases the distance that the objects has to be from the camera before the LOD is used.

The `flags` argument is the bitwise OR of, as required: One value of `ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>` left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom channel in use, `Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE<class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE>`, `Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>`, or `Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY<class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY>`.

**Note:** When using indices, it is recommended to only use points, lines, or triangles.

classref-item-separator

classref-method

`void (No return value.)` **clear_blend_shapes**() `🔗<class_ArrayMesh_method_clear_blend_shapes>`

Removes all blend shapes from this **ArrayMesh**.

classref-item-separator

classref-method

`void (No return value.)` **clear_surfaces**() `🔗<class_ArrayMesh_method_clear_surfaces>`

Removes all surfaces from this **ArrayMesh**.

classref-item-separator

classref-method

`int<class_int>` **get_blend_shape_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_get_blend_shape_count>`

Returns the number of blend shapes that the **ArrayMesh** holds.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_blend_shape_name**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_get_blend_shape_name>`

Returns the name of the blend shape at this index.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **lightmap_unwrap**(transform: `Transform3D<class_Transform3D>`, texel_size: `float<class_float>`) `🔗<class_ArrayMesh_method_lightmap_unwrap>`

Performs a UV unwrap on the **ArrayMesh** to prepare the mesh for lightmapping.

classref-item-separator

classref-method

`void (No return value.)` **regen_normal_maps**() `🔗<class_ArrayMesh_method_regen_normal_maps>`

Regenerates tangents for each of the **ArrayMesh**'s surfaces.

classref-item-separator

classref-method

`void (No return value.)` **set_blend_shape_name**(index: `int<class_int>`, name: `StringName<class_StringName>`) `🔗<class_ArrayMesh_method_set_blend_shape_name>`

Sets the name of the blend shape at this index.

classref-item-separator

classref-method

`int<class_int>` **surface_find_by_name**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_surface_find_by_name>`

Returns the index of the first surface with this name held within this **ArrayMesh**. If none are found, -1 is returned.

classref-item-separator

classref-method

`int<class_int>` **surface_get_array_index_len**(surf_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_surface_get_array_index_len>`

Returns the length in indices of the index array in the requested surface (see `add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`).

classref-item-separator

classref-method

`int<class_int>` **surface_get_array_len**(surf_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_surface_get_array_len>`

Returns the length in vertices of the vertex array in the requested surface (see `add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`).

classref-item-separator

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`ArrayFormat<enum_Mesh_ArrayFormat>`\] **surface_get_format**(surf_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_surface_get_format>`

Returns the format mask of the requested surface (see `add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`).

classref-item-separator

classref-method

`String<class_String>` **surface_get_name**(surf_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_surface_get_name>`

Gets the name assigned to this surface.

classref-item-separator

classref-method

`PrimitiveType<enum_Mesh_PrimitiveType>` **surface_get_primitive_type**(surf_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ArrayMesh_method_surface_get_primitive_type>`

Returns the primitive type of the requested surface (see `add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`).

classref-item-separator

classref-method

`void (No return value.)` **surface_remove**(surf_idx: `int<class_int>`) `🔗<class_ArrayMesh_method_surface_remove>`

Removes the surface at the given index from the Mesh, shifting surfaces with higher index down by one.

classref-item-separator

classref-method

`void (No return value.)` **surface_set_name**(surf_idx: `int<class_int>`, name: `String<class_String>`) `🔗<class_ArrayMesh_method_surface_set_name>`

Sets a name for a given surface.

classref-item-separator

classref-method

`void (No return value.)` **surface_update_attribute_region**(surf_idx: `int<class_int>`, offset: `int<class_int>`, data: `PackedByteArray<class_PackedByteArray>`) `🔗<class_ArrayMesh_method_surface_update_attribute_region>`

Updates the attribute buffer of this mesh's surface with the given `data`. The expected data per attribute is 12 or 8 bytes (4 bytes per float, 2 floats per `Vector2<class_Vector2>`, and 3 floats per `Vector3<class_Vector3>`) depending on if the mesh is using `Vector3<class_Vector3>` or `Vector2<class_Vector2>` vertices. This value can be determined with `RenderingServer.mesh_surface_get_format_attribute_stride()<class_RenderingServer_method_mesh_surface_get_format_attribute_stride>`.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each attribute.

A `PackedVector3Array<class_PackedVector3Array>` of attribute locations can be converted into a `PackedByteArray<class_PackedByteArray>` using `PackedVector3Array.to_byte_array()<class_PackedVector3Array_method_to_byte_array>` for use in `data`.

classref-item-separator

classref-method

`void (No return value.)` **surface_update_skin_region**(surf_idx: `int<class_int>`, offset: `int<class_int>`, data: `PackedByteArray<class_PackedByteArray>`) `🔗<class_ArrayMesh_method_surface_update_skin_region>`

Updates the skin buffer of this mesh's surface with the given `data`. The expected data per skin is 12 or 8 bytes (4 bytes per float, 2 floats per `Vector2<class_Vector2>`, and 3 floats per `Vector3<class_Vector3>`) depending on if the mesh is using `Vector3<class_Vector3>` or `Vector2<class_Vector2>` vertices. This value can be determined with `RenderingServer.mesh_surface_get_format_skin_stride()<class_RenderingServer_method_mesh_surface_get_format_skin_stride>`.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each skin.

A `PackedVector3Array<class_PackedVector3Array>` of skin locations can be converted into a `PackedByteArray<class_PackedByteArray>` using `PackedVector3Array.to_byte_array()<class_PackedVector3Array_method_to_byte_array>` for use in `data`.

classref-item-separator

classref-method

`void (No return value.)` **surface_update_vertex_region**(surf_idx: `int<class_int>`, offset: `int<class_int>`, data: `PackedByteArray<class_PackedByteArray>`) `🔗<class_ArrayMesh_method_surface_update_vertex_region>`

Updates the vertex buffer of this mesh's surface with the given `data`. The expected data per vertex is 12 or 8 bytes (4 bytes per float, 2 floats per `Vector2<class_Vector2>`, and 3 floats per `Vector3<class_Vector3>`) depending on if the mesh is using `Vector3<class_Vector3>` or `Vector2<class_Vector2>` vertices. This value can be determined with `RenderingServer.mesh_surface_get_format_vertex_stride()<class_RenderingServer_method_mesh_surface_get_format_vertex_stride>`.

The starting point of the updates can be changed with `offset`. The value of `offset` should be a multiple of 12 bytes in most cases to align to each vertex.

A `PackedVector3Array<class_PackedVector3Array>` of vertex locations can be converted into a `PackedByteArray<class_PackedByteArray>` using `PackedVector3Array.to_byte_array()<class_PackedVector3Array_method_to_byte_array>` for use in `data`.