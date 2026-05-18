github_url
hide

# NavigationMeshSourceGeometryData3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Container for parsed source geometry data used in navigation mesh baking.

classref-introduction-group

## Description

Container for parsed source geometry data used in navigation mesh baking.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_faces**(faces: `PackedVector3Array<class_PackedVector3Array>`, xform: `Transform3D<class_Transform3D>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_add_faces>`

Adds an array of vertex positions to the geometry data for navigation mesh baking to form triangulated faces. For each face the array must have three vertex positions in clockwise winding order. Since `NavigationMesh<class_NavigationMesh>` resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

classref-item-separator

classref-method

`void (No return value.)` **add_mesh**(mesh: `Mesh<class_Mesh>`, xform: `Transform3D<class_Transform3D>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_add_mesh>`

Adds the geometry data of a `Mesh<class_Mesh>` resource to the navigation mesh baking data. The mesh must have valid triangulated mesh data to be considered. Since `NavigationMesh<class_NavigationMesh>` resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

classref-item-separator

classref-method

`void (No return value.)` **add_mesh_array**(mesh_array: `Array<class_Array>`, xform: `Transform3D<class_Transform3D>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_add_mesh_array>`

Adds an `Array<class_Array>` the size of `Mesh.ARRAY_MAX<class_Mesh_constant_ARRAY_MAX>` and with vertices at index `Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>` and indices at index `Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>` to the navigation mesh baking data. The array must have valid triangulated mesh data to be considered. Since `NavigationMesh<class_NavigationMesh>` resources have no transform, all vertex positions need to be offset by the node's transform using `xform`.

classref-item-separator

classref-method

`void (No return value.)` **add_projected_obstruction**(vertices: `PackedVector3Array<class_PackedVector3Array>`, elevation: `float<class_float>`, height: `float<class_float>`, carve: `bool<class_bool>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction>`

Adds a projected obstruction shape to the source geometry. The `vertices` are considered projected on an xz-axes plane, placed at the global y-axis `elevation` and extruded by `height`. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

classref-item-separator

classref-method

`void (No return value.)` **append_arrays**(vertices: `PackedFloat32Array<class_PackedFloat32Array>`, indices: `PackedInt32Array<class_PackedInt32Array>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_append_arrays>`

Appends arrays of `vertices` and `indices` at the end of the existing arrays. Adds the existing index as an offset to the appended indices.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_NavigationMeshSourceGeometryData3D_method_clear>`

Clears the internal data.

classref-item-separator

classref-method

`void (No return value.)` **clear_projected_obstructions**() `🔗<class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions>`

Clears all projected obstructions.

classref-item-separator

classref-method

`AABB<class_AABB>` **get_bounds**() `🔗<class_NavigationMeshSourceGeometryData3D_method_get_bounds>`

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_indices**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationMeshSourceGeometryData3D_method_get_indices>`

Returns the parsed source geometry data indices array.

classref-item-separator

classref-method

`Array<class_Array>` **get_projected_obstructions**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions>`

Returns the projected obstructions as an `Array<class_Array>` of dictionaries. Each `Dictionary<class_Dictionary>` contains the following entries:

- `vertices` - A `PackedFloat32Array<class_PackedFloat32Array>` that defines the outline points of the projected shape.
- `elevation` - A `float<class_float>` that defines the projected shape placement on the y-axis.
- `height` - A `float<class_float>` that defines how much the projected shape is extruded along the y-axis.
- `carve` - A `bool<class_bool>` that defines how the obstacle affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

classref-item-separator

classref-method

`PackedFloat32Array<class_PackedFloat32Array>` **get_vertices**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationMeshSourceGeometryData3D_method_get_vertices>`

Returns the parsed source geometry data vertices array.

classref-item-separator

classref-method

`bool<class_bool>` **has_data**() `🔗<class_NavigationMeshSourceGeometryData3D_method_has_data>`

Returns `true` when parsed source geometry data exists.

classref-item-separator

classref-method

`void (No return value.)` **merge**(other_geometry: `NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_merge>`

Adds the geometry data of another **NavigationMeshSourceGeometryData3D** to the navigation mesh baking data.

classref-item-separator

classref-method

`void (No return value.)` **set_indices**(indices: `PackedInt32Array<class_PackedInt32Array>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_set_indices>`

Sets the parsed source geometry data indices. The indices need to be matched with appropriated vertices.

**Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.

classref-item-separator

classref-method

`void (No return value.)` **set_projected_obstructions**(projected_obstructions: `Array<class_Array>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions>`

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

gdscript

"vertices" : PackedFloat32Array "elevation" : float "height" : float "carve" : bool

classref-item-separator

classref-method

`void (No return value.)` **set_vertices**(vertices: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_NavigationMeshSourceGeometryData3D_method_set_vertices>`

Sets the parsed source geometry data vertices. The vertices need to be matched with appropriated indices.

**Warning:** Inappropriate data can crash the baking process of the involved third-party libraries.