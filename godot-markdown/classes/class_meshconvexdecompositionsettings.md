github_url
hide

# MeshConvexDecompositionSettings

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Parameters to be used with a `Mesh<class_Mesh>` convex decomposition operation.

classref-introduction-group

## Description

Parameters to be used with a `Mesh<class_Mesh>` convex decomposition operation.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Mode**: `🔗<enum_MeshConvexDecompositionSettings_Mode>`

classref-enumeration-constant

`Mode<enum_MeshConvexDecompositionSettings_Mode>` **CONVEX_DECOMPOSITION_MODE_VOXEL** = `0`

Constant for voxel-based approximate convex decomposition.

classref-enumeration-constant

`Mode<enum_MeshConvexDecompositionSettings_Mode>` **CONVEX_DECOMPOSITION_MODE_TETRAHEDRON** = `1`

Constant for tetrahedron-based approximate convex decomposition.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **convex_hull_approximation** = `true` `🔗<class_MeshConvexDecompositionSettings_property_convex_hull_approximation>`

classref-property-setget

- `void (No return value.)` **set_convex_hull_approximation**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_convex_hull_approximation**()

If `true`, uses approximation for computing convex hulls.

classref-item-separator

classref-property

`int<class_int>` **convex_hull_downsampling** = `4` `🔗<class_MeshConvexDecompositionSettings_property_convex_hull_downsampling>`

classref-property-setget

- `void (No return value.)` **set_convex_hull_downsampling**(value: `int<class_int>`)
- `int<class_int>` **get_convex_hull_downsampling**()

Controls the precision of the convex-hull generation process during the clipping plane selection stage. Ranges from `1` to `16`.

classref-item-separator

classref-property

`float<class_float>` **max_concavity** = `1.0` `🔗<class_MeshConvexDecompositionSettings_property_max_concavity>`

classref-property-setget

- `void (No return value.)` **set_max_concavity**(value: `float<class_float>`)
- `float<class_float>` **get_max_concavity**()

Maximum concavity. Ranges from `0.0` to `1.0`.

classref-item-separator

classref-property

`int<class_int>` **max_convex_hulls** = `1` `🔗<class_MeshConvexDecompositionSettings_property_max_convex_hulls>`

classref-property-setget

- `void (No return value.)` **set_max_convex_hulls**(value: `int<class_int>`)
- `int<class_int>` **get_max_convex_hulls**()

The maximum number of convex hulls to produce from the merge operation.

classref-item-separator

classref-property

`int<class_int>` **max_num_vertices_per_convex_hull** = `32` `🔗<class_MeshConvexDecompositionSettings_property_max_num_vertices_per_convex_hull>`

classref-property-setget

- `void (No return value.)` **set_max_num_vertices_per_convex_hull**(value: `int<class_int>`)
- `int<class_int>` **get_max_num_vertices_per_convex_hull**()

Controls the maximum number of triangles per convex-hull. Ranges from `4` to `1024`.

classref-item-separator

classref-property

`float<class_float>` **min_volume_per_convex_hull** = `0.0001` `🔗<class_MeshConvexDecompositionSettings_property_min_volume_per_convex_hull>`

classref-property-setget

- `void (No return value.)` **set_min_volume_per_convex_hull**(value: `float<class_float>`)
- `float<class_float>` **get_min_volume_per_convex_hull**()

Controls the adaptive sampling of the generated convex-hulls. Ranges from `0.0` to `0.01`.

classref-item-separator

classref-property

`Mode<enum_MeshConvexDecompositionSettings_Mode>` **mode** = `0` `🔗<class_MeshConvexDecompositionSettings_property_mode>`

classref-property-setget

- `void (No return value.)` **set_mode**(value: `Mode<enum_MeshConvexDecompositionSettings_Mode>`)
- `Mode<enum_MeshConvexDecompositionSettings_Mode>` **get_mode**()

Mode for the approximate convex decomposition.

classref-item-separator

classref-property

`bool<class_bool>` **normalize_mesh** = `false` `🔗<class_MeshConvexDecompositionSettings_property_normalize_mesh>`

classref-property-setget

- `void (No return value.)` **set_normalize_mesh**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_normalize_mesh**()

If `true`, normalizes the mesh before applying the convex decomposition.

classref-item-separator

classref-property

`int<class_int>` **plane_downsampling** = `4` `🔗<class_MeshConvexDecompositionSettings_property_plane_downsampling>`

classref-property-setget

- `void (No return value.)` **set_plane_downsampling**(value: `int<class_int>`)
- `int<class_int>` **get_plane_downsampling**()

Controls the granularity of the search for the "best" clipping plane. Ranges from `1` to `16`.

classref-item-separator

classref-property

`bool<class_bool>` **project_hull_vertices** = `true` `🔗<class_MeshConvexDecompositionSettings_property_project_hull_vertices>`

classref-property-setget

- `void (No return value.)` **set_project_hull_vertices**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_project_hull_vertices**()

If `true`, projects output convex hull vertices onto the original source mesh to increase floating-point accuracy of the results.

classref-item-separator

classref-property

`int<class_int>` **resolution** = `10000` `🔗<class_MeshConvexDecompositionSettings_property_resolution>`

classref-property-setget

- `void (No return value.)` **set_resolution**(value: `int<class_int>`)
- `int<class_int>` **get_resolution**()

Maximum number of voxels generated during the voxelization stage.

classref-item-separator

classref-property

`float<class_float>` **revolution_axes_clipping_bias** = `0.05` `🔗<class_MeshConvexDecompositionSettings_property_revolution_axes_clipping_bias>`

classref-property-setget

- `void (No return value.)` **set_revolution_axes_clipping_bias**(value: `float<class_float>`)
- `float<class_float>` **get_revolution_axes_clipping_bias**()

Controls the bias toward clipping along revolution axes. Ranges from `0.0` to `1.0`.

classref-item-separator

classref-property

`float<class_float>` **symmetry_planes_clipping_bias** = `0.05` `🔗<class_MeshConvexDecompositionSettings_property_symmetry_planes_clipping_bias>`

classref-property-setget

- `void (No return value.)` **set_symmetry_planes_clipping_bias**(value: `float<class_float>`)
- `float<class_float>` **get_symmetry_planes_clipping_bias**()

Controls the bias toward clipping along symmetry planes. Ranges from `0.0` to `1.0`.