github_url
hide

# MeshDataTool

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Helper tool to access and edit `Mesh<class_Mesh>` data.

classref-introduction-group

## Description

MeshDataTool provides access to individual vertices in a `Mesh<class_Mesh>`. It allows users to read and edit vertex data of meshes. It also creates an array of faces and edges.

To use MeshDataTool, load a mesh with `create_from_surface()<class_MeshDataTool_method_create_from_surface>`. When you are finished editing the data commit the data to a mesh with `commit_to_surface()<class_MeshDataTool_method_commit_to_surface>`.

Below is an example of how MeshDataTool may be used.

gdscript

var mesh = ArrayMesh.new() mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, BoxMesh.new().get_mesh_arrays()) var mdt = MeshDataTool.new() mdt.create_from_surface(mesh, 0) for i in range(mdt.get_vertex_count()): var vertex = mdt.get_vertex(i) \# In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded. vertex += mdt.get_vertex_normal(i) \# Save your change. mdt.set_vertex(i, vertex) mesh.clear_surfaces() mdt.commit_to_surface(mesh) var mi = MeshInstance.new() mi.mesh = mesh add_child(mi)

csharp

var mesh = new ArrayMesh(); mesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, new BoxMesh().GetMeshArrays()); var mdt = new MeshDataTool(); mdt.CreateFromSurface(mesh, 0); for (var i = 0; i \< mdt.GetVertexCount(); i++) { Vector3 vertex = mdt.GetVertex(i); // In this example we extend the mesh by one unit, which results in separated faces as it is flat shaded. vertex += mdt.GetVertexNormal(i); // Save your change. mdt.SetVertex(i, vertex); } mesh.ClearSurfaces(); mdt.CommitToSurface(mesh); var mi = new MeshInstance(); mi.Mesh = mesh; AddChild(mi);

See also `ArrayMesh<class_ArrayMesh>`, `ImmediateMesh<class_ImmediateMesh>` and `SurfaceTool<class_SurfaceTool>` for procedural geometry generation.

**Note:** Godot uses clockwise [winding order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front faces of triangle primitive modes.

classref-introduction-group

## Tutorials

- `Using the MeshDataTool <../tutorials/3d/procedural_geometry/meshdatatool>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear**() `🔗<class_MeshDataTool_method_clear>`

Clears all data currently in MeshDataTool.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **commit_to_surface**(mesh: `ArrayMesh<class_ArrayMesh>`, compression_flags: `int<class_int>` = 0) `🔗<class_MeshDataTool_method_commit_to_surface>`

Adds a new surface to specified `Mesh<class_Mesh>` with edited data.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **create_from_surface**(mesh: `ArrayMesh<class_ArrayMesh>`, surface: `int<class_int>`) `🔗<class_MeshDataTool_method_create_from_surface>`

Uses specified surface of given `Mesh<class_Mesh>` to populate data for MeshDataTool.

Requires `Mesh<class_Mesh>` with primitive type `Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`.

classref-item-separator

classref-method

`int<class_int>` **get_edge_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_edge_count>`

Returns the number of edges in this `Mesh<class_Mesh>`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_edge_faces**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_edge_faces>`

Returns array of faces that touch given edge.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_edge_meta**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_edge_meta>`

Returns meta information assigned to given edge.

classref-item-separator

classref-method

`int<class_int>` **get_edge_vertex**(idx: `int<class_int>`, vertex: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_edge_vertex>`

Returns the index of the specified `vertex` connected to the edge at index `idx`.

`vertex` can only be `0` or `1`, as edges are composed of two vertices.

classref-item-separator

classref-method

`int<class_int>` **get_face_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_face_count>`

Returns the number of faces in this `Mesh<class_Mesh>`.

classref-item-separator

classref-method

`int<class_int>` **get_face_edge**(idx: `int<class_int>`, edge: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_face_edge>`

Returns the edge associated with the face at index `idx`.

`edge` argument must be either `0`, `1`, or `2` because a face only has three edges.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_face_meta**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_face_meta>`

Returns the metadata associated with the given face.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_face_normal**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_face_normal>`

Calculates and returns the face normal of the given face.

classref-item-separator

classref-method

`int<class_int>` **get_face_vertex**(idx: `int<class_int>`, vertex: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_face_vertex>`

Returns the specified vertex index of the given face.

`vertex` must be either `0`, `1`, or `2` because faces contain three vertices.

gdscript

var index = mesh_data_tool.get_face_vertex(0, 1) \# Gets the index of the second vertex of the first face. var position = mesh_data_tool.get_vertex(index) var normal = mesh_data_tool.get_vertex_normal(index)

csharp

int index = meshDataTool.GetFaceVertex(0, 1); // Gets the index of the second vertex of the first face. Vector3 position = meshDataTool.GetVertex(index); Vector3 normal = meshDataTool.GetVertexNormal(index);

classref-item-separator

classref-method

`int<class_int>` **get_format**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_format>`

Returns the `Mesh<class_Mesh>`'s format as a combination of the `ArrayFormat<enum_Mesh_ArrayFormat>` flags. For example, a mesh containing both vertices and normals would return a format of `3` because `Mesh.ARRAY_FORMAT_VERTEX<class_Mesh_constant_ARRAY_FORMAT_VERTEX>` is `1` and `Mesh.ARRAY_FORMAT_NORMAL<class_Mesh_constant_ARRAY_FORMAT_NORMAL>` is `2`.

classref-item-separator

classref-method

`Material<class_Material>` **get_material**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_material>`

Returns the material assigned to the `Mesh<class_Mesh>`.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_vertex**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex>`

Returns the position of the given vertex.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_vertex_bones**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_bones>`

Returns the bones of the given vertex.

classref-item-separator

classref-method

`Color<class_Color>` **get_vertex_color**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_color>`

Returns the color of the given vertex.

classref-item-separator

classref-method

`int<class_int>` **get_vertex_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_count>`

Returns the total number of vertices in `Mesh<class_Mesh>`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_vertex_edges**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_edges>`

Returns an array of edges that share the given vertex.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_vertex_faces**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_faces>`

Returns an array of faces that share the given vertex.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_vertex_meta**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_meta>`

Returns the metadata associated with the given vertex.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_vertex_normal**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_normal>`

Returns the normal of the given vertex.

classref-item-separator

classref-method

`Plane<class_Plane>` **get_vertex_tangent**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_tangent>`

Returns the tangent of the given vertex.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_vertex_uv**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_uv>`

Returns the UV of the given vertex.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_vertex_uv2**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_uv2>`

Returns the UV2 of the given vertex.

classref-item-separator

classref-method

`PackedFloat32Array<class_PackedFloat32Array>` **get_vertex_weights**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshDataTool_method_get_vertex_weights>`

Returns bone weights of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_edge_meta**(idx: `int<class_int>`, meta: `Variant<class_Variant>`) `🔗<class_MeshDataTool_method_set_edge_meta>`

Sets the metadata of the given edge.

classref-item-separator

classref-method

`void (No return value.)` **set_face_meta**(idx: `int<class_int>`, meta: `Variant<class_Variant>`) `🔗<class_MeshDataTool_method_set_face_meta>`

Sets the metadata of the given face.

classref-item-separator

classref-method

`void (No return value.)` **set_material**(material: `Material<class_Material>`) `🔗<class_MeshDataTool_method_set_material>`

Sets the material to be used by newly-constructed `Mesh<class_Mesh>`.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex**(idx: `int<class_int>`, vertex: `Vector3<class_Vector3>`) `🔗<class_MeshDataTool_method_set_vertex>`

Sets the position of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_bones**(idx: `int<class_int>`, bones: `PackedInt32Array<class_PackedInt32Array>`) `🔗<class_MeshDataTool_method_set_vertex_bones>`

Sets the bones of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_color**(idx: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_MeshDataTool_method_set_vertex_color>`

Sets the color of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_meta**(idx: `int<class_int>`, meta: `Variant<class_Variant>`) `🔗<class_MeshDataTool_method_set_vertex_meta>`

Sets the metadata associated with the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_normal**(idx: `int<class_int>`, normal: `Vector3<class_Vector3>`) `🔗<class_MeshDataTool_method_set_vertex_normal>`

Sets the normal of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_tangent**(idx: `int<class_int>`, tangent: `Plane<class_Plane>`) `🔗<class_MeshDataTool_method_set_vertex_tangent>`

Sets the tangent of the given vertex.

**Note:** Even though `tangent` is a `Plane<class_Plane>`, it does not directly represent the tangent plane. Its `Plane.x<class_Plane_property_x>`, `Plane.y<class_Plane_property_y>`, and `Plane.z<class_Plane_property_z>` represent the tangent vector and `Plane.d<class_Plane_property_d>` should be either `-1` or `1`. See also `Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>`.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_uv**(idx: `int<class_int>`, uv: `Vector2<class_Vector2>`) `🔗<class_MeshDataTool_method_set_vertex_uv>`

Sets the UV of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_uv2**(idx: `int<class_int>`, uv2: `Vector2<class_Vector2>`) `🔗<class_MeshDataTool_method_set_vertex_uv2>`

Sets the UV2 of the given vertex.

classref-item-separator

classref-method

`void (No return value.)` **set_vertex_weights**(idx: `int<class_int>`, weights: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_MeshDataTool_method_set_vertex_weights>`

Sets the bone weights of the given vertex.