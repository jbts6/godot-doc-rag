github_url
hide

# GridMap

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Node for 3D tile-based maps.

classref-introduction-group

## Description

GridMap lets you place meshes on a grid interactively. It works both from the editor and from scripts, which can help you create in-game level editors.

GridMaps use a `MeshLibrary<class_MeshLibrary>` which contains a list of tiles. Each tile is a mesh with materials plus optional collision and navigation shapes.

A GridMap contains a collection of cells. Each grid cell refers to a tile in the `MeshLibrary<class_MeshLibrary>`. All cells in the map have the same dimensions.

Internally, a GridMap is split into a sparse collection of octants for efficient rendering and physics processing. Every octant has the same dimensions and can contain several cells.

**Note:** GridMap doesn't extend `VisualInstance3D<class_VisualInstance3D>` and therefore can't be hidden or cull masked based on `VisualInstance3D.layers<class_VisualInstance3D_property_layers>`. If you make a light not affect the first layer, the whole GridMap won't be lit by the light in question.

classref-introduction-group

## Tutorials

- `Using gridmaps <../tutorials/3d/using_gridmaps>`
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**cell_size_changed**(cell_size: `Vector3<class_Vector3>`) `🔗<class_GridMap_signal_cell_size_changed>`

Emitted when `cell_size<class_GridMap_property_cell_size>` changes.

classref-item-separator

classref-signal

**changed**() `🔗<class_GridMap_signal_changed>`

Emitted when the `MeshLibrary<class_MeshLibrary>` of this GridMap changes.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DebugVisibilityMode**: `🔗<enum_GridMap_DebugVisibilityMode>`

classref-enumeration-constant

`DebugVisibilityMode<enum_GridMap_DebugVisibilityMode>` **DEBUG_VISIBILITY_MODE_DEFAULT** = `0`

Hide the collisions debug shapes in the editor, and use the debug settings to determine their visibility in game (i.e. `SceneTree.debug_collisions_hint<class_SceneTree_property_debug_collisions_hint>` or `SceneTree.debug_navigation_hint<class_SceneTree_property_debug_navigation_hint>`).

classref-enumeration-constant

`DebugVisibilityMode<enum_GridMap_DebugVisibilityMode>` **DEBUG_VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show the collisions debug shapes.

classref-enumeration-constant

`DebugVisibilityMode<enum_GridMap_DebugVisibilityMode>` **DEBUG_VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide the collisions debug shapes.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**INVALID_CELL_ITEM** = `-1` `🔗<class_GridMap_constant_INVALID_CELL_ITEM>`

Invalid cell item that can be used in `set_cell_item()<class_GridMap_method_set_cell_item>` to clear cells (or represent an empty cell in `get_cell_item()<class_GridMap_method_get_cell_item>`).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **bake_navigation** = `false` `🔗<class_GridMap_property_bake_navigation>`

classref-property-setget

- `void (No return value.)` **set_bake_navigation**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_baking_navigation**()

If `true`, this GridMap creates a navigation region for each cell that uses a `mesh_library<class_GridMap_property_mesh_library>` item with a navigation mesh. The created navigation region will use the navigation layers bitmask assigned to the `MeshLibrary<class_MeshLibrary>`'s item.

classref-item-separator

classref-property

`bool<class_bool>` **cell_center_x** = `true` `🔗<class_GridMap_property_cell_center_x>`

classref-property-setget

- `void (No return value.)` **set_center_x**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_center_x**()

If `true`, grid items are centered on the X axis.

classref-item-separator

classref-property

`bool<class_bool>` **cell_center_y** = `true` `🔗<class_GridMap_property_cell_center_y>`

classref-property-setget

- `void (No return value.)` **set_center_y**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_center_y**()

If `true`, grid items are centered on the Y axis.

classref-item-separator

classref-property

`bool<class_bool>` **cell_center_z** = `true` `🔗<class_GridMap_property_cell_center_z>`

classref-property-setget

- `void (No return value.)` **set_center_z**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_center_z**()

If `true`, grid items are centered on the Z axis.

classref-item-separator

classref-property

`int<class_int>` **cell_octant_size** = `8` `🔗<class_GridMap_property_cell_octant_size>`

classref-property-setget

- `void (No return value.)` **set_octant_size**(value: `int<class_int>`)
- `int<class_int>` **get_octant_size**()

The size of each octant measured in number of cells. This applies to all three axis.

classref-item-separator

classref-property

`float<class_float>` **cell_scale** = `1.0` `🔗<class_GridMap_property_cell_scale>`

classref-property-setget

- `void (No return value.)` **set_cell_scale**(value: `float<class_float>`)
- `float<class_float>` **get_cell_scale**()

The scale of the cell items.

This does not affect the size of the grid cells themselves, only the items in them. This can be used to make cell items overlap their neighbors.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **cell_size** = `Vector3(2, 2, 2)` `🔗<class_GridMap_property_cell_size>`

classref-property-setget

- `void (No return value.)` **set_cell_size**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_cell_size**()

The dimensions of the grid's cells.

This does not affect the size of the meshes. See `cell_scale<class_GridMap_property_cell_scale>`.

classref-item-separator

classref-property

`int<class_int>` **collision_layer** = `1` `🔗<class_GridMap_property_collision_layer>`

classref-property-setget

- `void (No return value.)` **set_collision_layer**(value: `int<class_int>`)
- `int<class_int>` **get_collision_layer**()

The physics layers this GridMap is in.

GridMaps act as static bodies, meaning they aren't affected by gravity or other forces. They only affect other physics bodies that collide with them.

classref-item-separator

classref-property

`int<class_int>` **collision_mask** = `1` `🔗<class_GridMap_property_collision_mask>`

classref-property-setget

- `void (No return value.)` **set_collision_mask**(value: `int<class_int>`)
- `int<class_int>` **get_collision_mask**()

The physics layers this GridMap detects collisions in. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

classref-item-separator

classref-property

`float<class_float>` **collision_priority** = `1.0` `🔗<class_GridMap_property_collision_priority>`

classref-property-setget

- `void (No return value.)` **set_collision_priority**(value: `float<class_float>`)
- `float<class_float>` **get_collision_priority**()

The priority used to solve colliding when occurring penetration. The higher the priority is, the lower the penetration into the object will be. This can for example be used to prevent the player from breaking through the boundaries of a level.

classref-item-separator

classref-property

`DebugVisibilityMode<enum_GridMap_DebugVisibilityMode>` **collision_visibility_mode** = `0` `🔗<class_GridMap_property_collision_visibility_mode>`

classref-property-setget

- `void (No return value.)` **set_collision_visibility_mode**(value: `DebugVisibilityMode<enum_GridMap_DebugVisibilityMode>`)
- `DebugVisibilityMode<enum_GridMap_DebugVisibilityMode>` **get_collision_visibility_mode**()

Show or hide the **GridMap**'s collision shapes. If set to `DEBUG_VISIBILITY_MODE_DEFAULT<class_GridMap_constant_DEBUG_VISIBILITY_MODE_DEFAULT>`, this depends on the show collision debug settings.

classref-item-separator

classref-property

`MeshLibrary<class_MeshLibrary>` **mesh_library** `🔗<class_GridMap_property_mesh_library>`

classref-property-setget

- `void (No return value.)` **set_mesh_library**(value: `MeshLibrary<class_MeshLibrary>`)
- `MeshLibrary<class_MeshLibrary>` **get_mesh_library**()

The assigned `MeshLibrary<class_MeshLibrary>`.

classref-item-separator

classref-property

`PhysicsMaterial<class_PhysicsMaterial>` **physics_material** `🔗<class_GridMap_property_physics_material>`

classref-property-setget

- `void (No return value.)` **set_physics_material**(value: `PhysicsMaterial<class_PhysicsMaterial>`)
- `PhysicsMaterial<class_PhysicsMaterial>` **get_physics_material**()

Overrides the default friction and bounce physics properties for the whole **GridMap**.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear**() `🔗<class_GridMap_method_clear>`

Clear all cells.

classref-item-separator

classref-method

`void (No return value.)` **clear_baked_meshes**() `🔗<class_GridMap_method_clear_baked_meshes>`

Clears all baked meshes. See `make_baked_meshes()<class_GridMap_method_make_baked_meshes>`.

classref-item-separator

classref-method

`RID<class_RID>` **get_bake_mesh_instance**(idx: `int<class_int>`) `🔗<class_GridMap_method_get_bake_mesh_instance>`

Returns `RID<class_RID>` of a baked mesh with the given `idx`.

classref-item-separator

classref-method

`Array<class_Array>` **get_bake_meshes**() `🔗<class_GridMap_method_get_bake_meshes>`

Returns an array of `ArrayMesh<class_ArrayMesh>`es and `Transform3D<class_Transform3D>` references of all bake meshes that exist within the current GridMap. Even indices contain `ArrayMesh<class_ArrayMesh>`es, while odd indices contain `Transform3D<class_Transform3D>`s that are always equal to `Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>`.

This method relies on the output of `make_baked_meshes()<class_GridMap_method_make_baked_meshes>`, which will be called with `gen_lightmap_uv` set to `true` and `lightmap_uv_texel_size` set to `0.1` if it hasn't been called yet.

classref-item-separator

classref-method

`Basis<class_Basis>` **get_basis_with_orthogonal_index**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_basis_with_orthogonal_index>`

Returns one of 24 possible rotations that lie along the vectors (x,y,z) with each component being either -1, 0, or 1. For further details, refer to the Godot source code.

classref-item-separator

classref-method

`int<class_int>` **get_cell_item**(position: `Vector3i<class_Vector3i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_cell_item>`

The `MeshLibrary<class_MeshLibrary>` item index located at the given grid coordinates. If the cell is empty, `INVALID_CELL_ITEM<class_GridMap_constant_INVALID_CELL_ITEM>` will be returned.

classref-item-separator

classref-method

`Basis<class_Basis>` **get_cell_item_basis**(position: `Vector3i<class_Vector3i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_cell_item_basis>`

Returns the basis that gives the specified cell its orientation.

classref-item-separator

classref-method

`int<class_int>` **get_cell_item_orientation**(position: `Vector3i<class_Vector3i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_cell_item_orientation>`

The orientation of the cell at the given grid coordinates. `-1` is returned if the cell is empty.

classref-item-separator

classref-method

`bool<class_bool>` **get_collision_layer_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_collision_layer_value>`

Returns whether or not the specified layer of the `collision_layer<class_GridMap_property_collision_layer>` is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`bool<class_bool>` **get_collision_mask_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_collision_mask_value>`

Returns whether or not the specified layer of the `collision_mask<class_GridMap_property_collision_mask>` is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`Array<class_Array>` **get_meshes**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_meshes>`

Returns an array of `Transform3D<class_Transform3D>` and `Mesh<class_Mesh>` references corresponding to the non-empty cells in the grid. The transforms are specified in local space. Even indices contain `Transform3D<class_Transform3D>`s, while odd indices contain `Mesh<class_Mesh>`es related to the `Transform3D<class_Transform3D>` in the index preceding it.

classref-item-separator

classref-method

`RID<class_RID>` **get_navigation_map**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_navigation_map>`

Returns the `RID<class_RID>` of the navigation map this GridMap node uses for its cell baked navigation meshes.

This function returns always the map set on the GridMap node and not the map on the NavigationServer. If the map is changed directly with the NavigationServer API the GridMap node will not be aware of the map change.

classref-item-separator

classref-method

`Vector3i<class_Vector3i>` **get_octant_coords_from_cell_coords**(cell_coords: `Vector3i<class_Vector3i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_octant_coords_from_cell_coords>`

Returns the `Vector3i<class_Vector3i>` octant coordinates of the octant that the cell at `cell_coords` belongs to.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_octants_in_bounds**(bounds: `AABB<class_AABB>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_octants_in_bounds>`

Returns an array of `Vector3i<class_Vector3i>` octant coordinates that are inside the given `bounds`, including octants that have no cells in use.

classref-item-separator

classref-method

`int<class_int>` **get_orthogonal_index_from_basis**(basis: `Basis<class_Basis>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_orthogonal_index_from_basis>`

This function considers a discretization of rotations into 24 points on unit sphere, lying along the vectors (x,y,z) with each component being either -1, 0, or 1, and returns the index (in the range from 0 to 23) of the point best representing the orientation of the object. For further details, refer to the Godot source code.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_cells**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_cells>`

Returns an array of `Vector3<class_Vector3>` with the non-empty cell coordinates in the grid map.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_cells_by_item**(item: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_cells_by_item>`

Returns an array of all cells with the given item index specified in `item`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_cells_in_octant**(octant_coords: `Vector3i<class_Vector3i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_cells_in_octant>`

Returns an array of `Vector3i<class_Vector3i>`s with the cell coordinates of non-empty cells inside the octant at `octant_coords`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_cells_in_octant_by_item**(octant_coords: `Vector3i<class_Vector3i>`, item: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_cells_in_octant_by_item>`

Returns an array of `Vector3i<class_Vector3i>`s with the cell coordinates of cells inside the octant at `octant_coords` that use the specified cell `item`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_octants**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_octants>`

Returns an array of `Vector3i<class_Vector3i>`s with the octant coordinates of the non-empty octants in the grid map.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_octants_by_item**(item: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_octants_by_item>`

Returns an array of `Vector3i<class_Vector3i>`s with the octant coordinates of the octants that use the specified `item` in the grid map.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **get_used_octants_in_bounds**(bounds: `AABB<class_AABB>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_get_used_octants_in_bounds>`

Returns an array of `Vector3i<class_Vector3i>`s with the octant coordinates of non-empty octants that are inside the local `bounds`.

classref-item-separator

classref-method

`Vector3i<class_Vector3i>` **local_to_map**(local_position: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_local_to_map>`

Returns the map coordinates of the cell containing the given `local_position`. If `local_position` is in global coordinates, consider using `Node3D.to_local()<class_Node3D_method_to_local>` before passing it to this method. See also `map_to_local()<class_GridMap_method_map_to_local>`.

classref-item-separator

classref-method

`void (No return value.)` **make_baked_meshes**(gen_lightmap_uv: `bool<class_bool>` = false, lightmap_uv_texel_size: `float<class_float>` = 0.1) `🔗<class_GridMap_method_make_baked_meshes>`

Generates a baked mesh that represents all meshes in the assigned `MeshLibrary<class_MeshLibrary>` for use with `LightmapGI<class_LightmapGI>`. If `gen_lightmap_uv` is `true`, UV2 data will be generated for each mesh currently used in the **GridMap**. Otherwise, only meshes that already have UV2 data present will be able to use baked lightmaps. When generating UV2, `lightmap_uv_texel_size` controls the texel density for lightmaps, with lower values resulting in more detailed lightmaps. `lightmap_uv_texel_size` is ignored if `gen_lightmap_uv` is `false`. See also `get_bake_meshes()<class_GridMap_method_get_bake_meshes>`, which relies on the output of this method.

**Note:** Calling this method will not actually bake lightmaps, as lightmap baking is performed using the `LightmapGI<class_LightmapGI>` node.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **map_to_local**(map_position: `Vector3i<class_Vector3i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMap_method_map_to_local>`

Returns the position of a grid cell in the GridMap's local coordinate space. To convert the returned value into global coordinates, use `Node3D.to_global()<class_Node3D_method_to_global>`. See also `local_to_map()<class_GridMap_method_local_to_map>`.

classref-item-separator

classref-method

`void (No return value.)` **resource_changed**(resource: `Resource<class_Resource>`) `🔗<class_GridMap_method_resource_changed>`

**Deprecated:** Use `Resource.changed<class_Resource_signal_changed>` instead.

This method does nothing.

classref-item-separator

classref-method

`void (No return value.)` **set_cell_item**(position: `Vector3i<class_Vector3i>`, item: `int<class_int>`, orientation: `int<class_int>` = 0) `🔗<class_GridMap_method_set_cell_item>`

Sets the mesh index for the cell referenced by its grid coordinates.

A negative item index such as `INVALID_CELL_ITEM<class_GridMap_constant_INVALID_CELL_ITEM>` will clear the cell.

Optionally, the item's orientation can be passed. For valid orientation values, see `get_orthogonal_index_from_basis()<class_GridMap_method_get_orthogonal_index_from_basis>`.

classref-item-separator

classref-method

`void (No return value.)` **set_collision_layer_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_GridMap_method_set_collision_layer_value>`

Based on `value`, enables or disables the specified layer in the `collision_layer<class_GridMap_property_collision_layer>`, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_collision_mask_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_GridMap_method_set_collision_mask_value>`

Based on `value`, enables or disables the specified layer in the `collision_mask<class_GridMap_property_collision_mask>`, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_navigation_map**(navigation_map: `RID<class_RID>`) `🔗<class_GridMap_method_set_navigation_map>`

Sets the `RID<class_RID>` of the navigation map this GridMap node should use for its cell baked navigation meshes.