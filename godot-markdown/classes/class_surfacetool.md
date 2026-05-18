github_url
hide

# SurfaceTool

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Helper tool to create geometry.

classref-introduction-group

## Description

The **SurfaceTool** is used to construct a `Mesh<class_Mesh>` by specifying vertex attributes individually. It can be used to construct a `Mesh<class_Mesh>` from a script. All properties except indices need to be added before calling `add_vertex()<class_SurfaceTool_method_add_vertex>`. For example, to add vertex colors and UVs:

gdscript

var st = SurfaceTool.new() st.begin(Mesh.PRIMITIVE_TRIANGLES) st.set_color(Color(1, 0, 0)) st.set_uv(Vector2(0, 0)) st.add_vertex(Vector3(0, 0, 0))

csharp

var st = new SurfaceTool(); st.Begin(Mesh.PrimitiveType.Triangles); st.SetColor(new Color(1, 0, 0)); st.SetUV(new Vector2(0, 0)); st.AddVertex(new Vector3(0, 0, 0));

The above **SurfaceTool** now contains one vertex of a triangle which has a UV coordinate and a specified `Color<class_Color>`. If another vertex were added without calling `set_uv()<class_SurfaceTool_method_set_uv>` or `set_color()<class_SurfaceTool_method_set_color>`, then the last values would be used.

Vertex attributes must be passed **before** calling `add_vertex()<class_SurfaceTool_method_add_vertex>`. Failure to do so will result in an error when committing the vertex information to a mesh.

Additionally, the attributes used before the first vertex is added determine the format of the mesh. For example, if you only add UVs to the first vertex, you cannot add color to any of the subsequent vertices.

See also `ArrayMesh<class_ArrayMesh>`, `ImmediateMesh<class_ImmediateMesh>` and `MeshDataTool<class_MeshDataTool>` for procedural geometry generation.

**Note:** Godot uses clockwise [winding order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front faces of triangle primitive modes.

classref-introduction-group

## Tutorials

- `Using the SurfaceTool <../tutorials/3d/procedural_geometry/surfacetool>`
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **CustomFormat**: `🔗<enum_SurfaceTool_CustomFormat>`

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RGBA8_UNORM** = `0`

Limits range of data passed to `set_custom()<class_SurfaceTool_method_set_custom>` to unsigned normalized 0 to 1 stored in 8 bits per channel. See `Mesh.ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RGBA8_SNORM** = `1`

Limits range of data passed to `set_custom()<class_SurfaceTool_method_set_custom>` to signed normalized -1 to 1 stored in 8 bits per channel. See `Mesh.ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RG_HALF** = `2`

Stores data passed to `set_custom()<class_SurfaceTool_method_set_custom>` as half precision floats, and uses only red and green color channels. See `Mesh.ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RGBA_HALF** = `3`

Stores data passed to `set_custom()<class_SurfaceTool_method_set_custom>` as half precision floats and uses all color channels. See `Mesh.ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_R_FLOAT** = `4`

Stores data passed to `set_custom()<class_SurfaceTool_method_set_custom>` as full precision floats, and uses only red color channel. See `Mesh.ARRAY_CUSTOM_R_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_R_FLOAT>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RG_FLOAT** = `5`

Stores data passed to `set_custom()<class_SurfaceTool_method_set_custom>` as full precision floats, and uses only red and green color channels. See `Mesh.ARRAY_CUSTOM_RG_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_RG_FLOAT>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RGB_FLOAT** = `6`

Stores data passed to `set_custom()<class_SurfaceTool_method_set_custom>` as full precision floats, and uses only red, green and blue color channels. See `Mesh.ARRAY_CUSTOM_RGB_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_RGB_FLOAT>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_RGBA_FLOAT** = `7`

Stores data passed to `set_custom()<class_SurfaceTool_method_set_custom>` as full precision floats, and uses all color channels. See `Mesh.ARRAY_CUSTOM_RGBA_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_RGBA_FLOAT>`.

classref-enumeration-constant

`CustomFormat<enum_SurfaceTool_CustomFormat>` **CUSTOM_MAX** = `8`

Used to indicate a disabled custom channel.

classref-item-separator

classref-enumeration

enum **SkinWeightCount**: `🔗<enum_SurfaceTool_SkinWeightCount>`

classref-enumeration-constant

`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>` **SKIN_4_WEIGHTS** = `0`

Each individual vertex can be influenced by only 4 bone weights.

classref-enumeration-constant

`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>` **SKIN_8_WEIGHTS** = `1`

Each individual vertex can be influenced by up to 8 bone weights.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_index**(index: `int<class_int>`) `🔗<class_SurfaceTool_method_add_index>`

Adds a vertex to index array if you are using indexed vertices. Does not need to be called before adding vertices.

classref-item-separator

classref-method

`void (No return value.)` **add_triangle_fan**(vertices: `PackedVector3Array<class_PackedVector3Array>`, uvs: `PackedVector2Array<class_PackedVector2Array>` = PackedVector2Array(), colors: `PackedColorArray<class_PackedColorArray>` = PackedColorArray(), uv2s: `PackedVector2Array<class_PackedVector2Array>` = PackedVector2Array(), normals: `PackedVector3Array<class_PackedVector3Array>` = PackedVector3Array(), tangents: `Array<class_Array>`\[`Plane<class_Plane>`\] = \[\]) `🔗<class_SurfaceTool_method_add_triangle_fan>`

Inserts a triangle fan made of array data into `Mesh<class_Mesh>` being constructed.

Requires the primitive type be set to `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`.

classref-item-separator

classref-method

`void (No return value.)` **add_vertex**(vertex: `Vector3<class_Vector3>`) `🔗<class_SurfaceTool_method_add_vertex>`

Specifies the position of current vertex. Should be called after specifying other vertex properties (e.g. Color, UV).

classref-item-separator

classref-method

`void (No return value.)` **append_from**(existing: `Mesh<class_Mesh>`, surface: `int<class_int>`, transform: `Transform3D<class_Transform3D>`) `🔗<class_SurfaceTool_method_append_from>`

Append vertices from a given `Mesh<class_Mesh>` surface onto the current vertex array with specified `Transform3D<class_Transform3D>`.

classref-item-separator

classref-method

`void (No return value.)` **begin**(primitive: `PrimitiveType<enum_Mesh_PrimitiveType>`) `🔗<class_SurfaceTool_method_begin>`

Called before adding any vertices. Takes the primitive type as an argument (e.g. `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`).

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_SurfaceTool_method_clear>`

Clear all information passed into the surface tool so far.

classref-item-separator

classref-method

`ArrayMesh<class_ArrayMesh>` **commit**(existing: `ArrayMesh<class_ArrayMesh>` = null, flags: `int<class_int>` = 0) `🔗<class_SurfaceTool_method_commit>`

Returns a constructed `ArrayMesh<class_ArrayMesh>` from current information passed in. If an existing `ArrayMesh<class_ArrayMesh>` is passed in as an argument, will add an extra surface to the existing `ArrayMesh<class_ArrayMesh>`.

The `flags` argument can be the bitwise OR of `Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE<class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE>`, `Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>`, or `Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY<class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY>`.

classref-item-separator

classref-method

`Array<class_Array>` **commit_to_arrays**() `🔗<class_SurfaceTool_method_commit_to_arrays>`

Commits the data to the same format used by `ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`, `ImporterMesh.add_surface()<class_ImporterMesh_method_add_surface>`, and `create_from_arrays()<class_SurfaceTool_method_create_from_arrays>`. This way you can further process the mesh data using the `ArrayMesh<class_ArrayMesh>` or `ImporterMesh<class_ImporterMesh>` APIs.

classref-item-separator

classref-method

`void (No return value.)` **create_from**(existing: `Mesh<class_Mesh>`, surface: `int<class_int>`) `🔗<class_SurfaceTool_method_create_from>`

Creates a vertex array from an existing `Mesh<class_Mesh>`.

classref-item-separator

classref-method

`void (No return value.)` **create_from_arrays**(arrays: `Array<class_Array>`, primitive_type: `PrimitiveType<enum_Mesh_PrimitiveType>` = 3) `🔗<class_SurfaceTool_method_create_from_arrays>`

Creates this SurfaceTool from existing vertex arrays such as returned by `commit_to_arrays()<class_SurfaceTool_method_commit_to_arrays>`, `Mesh.surface_get_arrays()<class_Mesh_method_surface_get_arrays>`, `Mesh.surface_get_blend_shape_arrays()<class_Mesh_method_surface_get_blend_shape_arrays>`, `ImporterMesh.get_surface_arrays()<class_ImporterMesh_method_get_surface_arrays>`, and `ImporterMesh.get_surface_blend_shape_arrays()<class_ImporterMesh_method_get_surface_blend_shape_arrays>`. `primitive_type` controls the type of mesh data, defaulting to `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`.

classref-item-separator

classref-method

`void (No return value.)` **create_from_blend_shape**(existing: `Mesh<class_Mesh>`, surface: `int<class_int>`, blend_shape: `String<class_String>`) `🔗<class_SurfaceTool_method_create_from_blend_shape>`

Creates a vertex array from the specified blend shape of an existing `Mesh<class_Mesh>`. This can be used to extract a specific pose from a blend shape.

classref-item-separator

classref-method

`void (No return value.)` **deindex**() `🔗<class_SurfaceTool_method_deindex>`

Removes the index array by expanding the vertex array.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **generate_lod**(nd_threshold: `float<class_float>`, target_index_count: `int<class_int>` = 3) `🔗<class_SurfaceTool_method_generate_lod>`

**Deprecated:** This method is unused internally, as it does not preserve normals or UVs. Consider using `ImporterMesh.generate_lods()<class_ImporterMesh_method_generate_lods>` instead.

Generates an LOD for a given `nd_threshold` in linear units (square root of quadric error metric), using at most `target_index_count` indices.

classref-item-separator

classref-method

`void (No return value.)` **generate_normals**(flip: `bool<class_bool>` = false) `🔗<class_SurfaceTool_method_generate_normals>`

Generates normals from vertices so you do not have to do it manually. If `flip` is `true`, the resulting normals will be inverted. `generate_normals()<class_SurfaceTool_method_generate_normals>` should be called *after* generating geometry and *before* committing the mesh using `commit()<class_SurfaceTool_method_commit>` or `commit_to_arrays()<class_SurfaceTool_method_commit_to_arrays>`. For correct display of normal-mapped surfaces, you will also have to generate tangents using `generate_tangents()<class_SurfaceTool_method_generate_tangents>`.

**Note:** `generate_normals()<class_SurfaceTool_method_generate_normals>` only works if the primitive type is set to `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`.

**Note:** `generate_normals()<class_SurfaceTool_method_generate_normals>` takes smooth groups into account. To generate smooth normals, set the smooth group to a value greater than or equal to `0` using `set_smooth_group()<class_SurfaceTool_method_set_smooth_group>` or leave the smooth group at the default of `0`. To generate flat normals, set the smooth group to `-1` using `set_smooth_group()<class_SurfaceTool_method_set_smooth_group>` prior to adding vertices.

classref-item-separator

classref-method

`void (No return value.)` **generate_tangents**() `🔗<class_SurfaceTool_method_generate_tangents>`

Generates a tangent vector for each vertex. Requires that each vertex already has UVs and normals set (see `generate_normals()<class_SurfaceTool_method_generate_normals>`).

classref-item-separator

classref-method

`AABB<class_AABB>` **get_aabb**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SurfaceTool_method_get_aabb>`

Returns the axis-aligned bounding box of the vertex positions.

classref-item-separator

classref-method

`CustomFormat<enum_SurfaceTool_CustomFormat>` **get_custom_format**(channel_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SurfaceTool_method_get_custom_format>`

Returns the format for custom `channel_index` (currently up to 4). Returns `CUSTOM_MAX<class_SurfaceTool_constant_CUSTOM_MAX>` if this custom channel is unused.

classref-item-separator

classref-method

`PrimitiveType<enum_Mesh_PrimitiveType>` **get_primitive_type**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SurfaceTool_method_get_primitive_type>`

Returns the type of mesh geometry, such as `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`.

classref-item-separator

classref-method

`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>` **get_skin_weight_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SurfaceTool_method_get_skin_weight_count>`

By default, returns `SKIN_4_WEIGHTS<class_SurfaceTool_constant_SKIN_4_WEIGHTS>` to indicate only 4 bone influences per vertex are used.

Returns `SKIN_8_WEIGHTS<class_SurfaceTool_constant_SKIN_8_WEIGHTS>` if up to 8 influences are used.

**Note:** This function returns an enum, not the exact number of weights.

classref-item-separator

classref-method

`void (No return value.)` **index**() `🔗<class_SurfaceTool_method_index>`

Shrinks the vertex array by creating an index array. This can improve performance by avoiding vertex reuse.

classref-item-separator

classref-method

`void (No return value.)` **optimize_indices_for_cache**() `🔗<class_SurfaceTool_method_optimize_indices_for_cache>`

Optimizes triangle sorting for performance. Requires that `get_primitive_type()<class_SurfaceTool_method_get_primitive_type>` is `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`.

classref-item-separator

classref-method

`void (No return value.)` **set_bones**(bones: `PackedInt32Array<class_PackedInt32Array>`) `🔗<class_SurfaceTool_method_set_bones>`

Specifies an array of bones to use for the *next* vertex. `bones` must contain 4 integers.

classref-item-separator

classref-method

`void (No return value.)` **set_color**(color: `Color<class_Color>`) `🔗<class_SurfaceTool_method_set_color>`

Specifies a `Color<class_Color>` to use for the *next* vertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.

**Note:** The material must have `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` enabled for the vertex color to be visible.

classref-item-separator

classref-method

`void (No return value.)` **set_custom**(channel_index: `int<class_int>`, custom_color: `Color<class_Color>`) `🔗<class_SurfaceTool_method_set_custom>`

Sets the custom value on this vertex for `channel_index`.

`set_custom_format()<class_SurfaceTool_method_set_custom_format>` must be called first for this `channel_index`. Formats which are not RGBA will ignore other color channels.

classref-item-separator

classref-method

`void (No return value.)` **set_custom_format**(channel_index: `int<class_int>`, format: `CustomFormat<enum_SurfaceTool_CustomFormat>`) `🔗<class_SurfaceTool_method_set_custom_format>`

Sets the color format for this custom `channel_index`. Use `CUSTOM_MAX<class_SurfaceTool_constant_CUSTOM_MAX>` to disable.

Must be invoked after `begin()<class_SurfaceTool_method_begin>` and should be set before `commit()<class_SurfaceTool_method_commit>` or `commit_to_arrays()<class_SurfaceTool_method_commit_to_arrays>`.

classref-item-separator

classref-method

`void (No return value.)` **set_material**(material: `Material<class_Material>`) `🔗<class_SurfaceTool_method_set_material>`

Sets `Material<class_Material>` to be used by the `Mesh<class_Mesh>` you are constructing.

classref-item-separator

classref-method

`void (No return value.)` **set_normal**(normal: `Vector3<class_Vector3>`) `🔗<class_SurfaceTool_method_set_normal>`

Specifies a normal to use for the *next* vertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.

classref-item-separator

classref-method

`void (No return value.)` **set_skin_weight_count**(count: `SkinWeightCount<enum_SurfaceTool_SkinWeightCount>`) `🔗<class_SurfaceTool_method_set_skin_weight_count>`

Set to `SKIN_8_WEIGHTS<class_SurfaceTool_constant_SKIN_8_WEIGHTS>` to indicate that up to 8 bone influences per vertex may be used.

By default, only 4 bone influences are used (`SKIN_4_WEIGHTS<class_SurfaceTool_constant_SKIN_4_WEIGHTS>`).

**Note:** This function takes an enum, not the exact number of weights.

classref-item-separator

classref-method

`void (No return value.)` **set_smooth_group**(index: `int<class_int>`) `🔗<class_SurfaceTool_method_set_smooth_group>`

Specifies the smooth group to use for the *next* vertex. If this is never called, all vertices will have the default smooth group of `0` and will be smoothed with adjacent vertices of the same group. To produce a mesh with flat normals, set the smooth group to `-1`.

**Note:** This function actually takes a `uint32_t`, so C# users should use `uint32.MaxValue` instead of `-1` to produce a mesh with flat normals.

classref-item-separator

classref-method

`void (No return value.)` **set_tangent**(tangent: `Plane<class_Plane>`) `🔗<class_SurfaceTool_method_set_tangent>`

Specifies a tangent to use for the *next* vertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.

**Note:** Even though `tangent` is a `Plane<class_Plane>`, it does not directly represent the tangent plane. Its `Plane.x<class_Plane_property_x>`, `Plane.y<class_Plane_property_y>`, and `Plane.z<class_Plane_property_z>` represent the tangent vector and `Plane.d<class_Plane_property_d>` should be either `-1` or `1`. See also `Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>`.

classref-item-separator

classref-method

`void (No return value.)` **set_uv**(uv: `Vector2<class_Vector2>`) `🔗<class_SurfaceTool_method_set_uv>`

Specifies a set of UV coordinates to use for the *next* vertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.

classref-item-separator

classref-method

`void (No return value.)` **set_uv2**(uv2: `Vector2<class_Vector2>`) `🔗<class_SurfaceTool_method_set_uv2>`

Specifies an optional second set of UV coordinates to use for the *next* vertex. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.

classref-item-separator

classref-method

`void (No return value.)` **set_weights**(weights: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_SurfaceTool_method_set_weights>`

Specifies weight values to use for the *next* vertex. `weights` must contain 4 values. If every vertex needs to have this information set and you fail to submit it for the first vertex, this information may not be used at all.