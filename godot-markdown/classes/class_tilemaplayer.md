github_url
hide

# TileMapLayer

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Node for 2D tile-based maps.

classref-introduction-group

## Description

Node for 2D tile-based maps. A **TileMapLayer** uses a `TileSet<class_TileSet>` which contain a list of tiles which are used to create grid-based maps. Unlike the `TileMap<class_TileMap>` node, which is deprecated, **TileMapLayer** has only one layer of tiles. You can use several **TileMapLayer** to achieve the same result as a `TileMap<class_TileMap>` node.

For performance reasons, all TileMap updates are batched at the end of a frame. Notably, this means that scene tiles from a `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>` are initialized after their parent. This is only queued when inside the scene tree.

To force an update earlier on, call `update_internals()<class_TileMapLayer_method_update_internals>`.

**Note:** For performance and compatibility reasons, the coordinates serialized by **TileMapLayer** are limited to 16-bit signed integers, i.e. the range for X and Y coordinates is from `-32768` to `32767`. When saving tile data, tiles outside this range are wrapped.

classref-introduction-group

## Tutorials

- `Using Tilemaps <../tutorials/2d/using_tilemaps>`
- [2D Platformer Demo](https://godotengine.org/asset-library/asset/2727)
- [2D Isometric Demo](https://godotengine.org/asset-library/asset/2718)
- [2D Hexagonal Demo](https://godotengine.org/asset-library/asset/2717)
- [2D Grid-based Navigation with AStarGrid2D Demo](https://godotengine.org/asset-library/asset/2723)
- [2D Role Playing Game (RPG) Demo](https://godotengine.org/asset-library/asset/2729)
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)
- [2D Dynamic TileMap Layers Demo](https://godotengine.org/asset-library/asset/2713)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**changed**() `🔗<class_TileMapLayer_signal_changed>`

Emitted when this **TileMapLayer**'s properties changes. This includes modified cells, properties, or changes made to its assigned `TileSet<class_TileSet>`.

**Note:** This signal may be emitted very often when batch-modifying a **TileMapLayer**. Avoid executing complex processing in a connected function, and consider delaying it to the end of the frame instead (i.e. calling `Object.call_deferred()<class_Object_method_call_deferred>`).

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DebugVisibilityMode**: `🔗<enum_TileMapLayer_DebugVisibilityMode>`

classref-enumeration-constant

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **DEBUG_VISIBILITY_MODE_DEFAULT** = `0`

Hide the collisions or navigation debug shapes in the editor, and use the debug settings to determine their visibility in game (i.e. `SceneTree.debug_collisions_hint<class_SceneTree_property_debug_collisions_hint>` or `SceneTree.debug_navigation_hint<class_SceneTree_property_debug_navigation_hint>`).

classref-enumeration-constant

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **DEBUG_VISIBILITY_MODE_FORCE_HIDE** = `2`

Always hide the collisions or navigation debug shapes.

classref-enumeration-constant

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **DEBUG_VISIBILITY_MODE_FORCE_SHOW** = `1`

Always show the collisions or navigation debug shapes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **collision_enabled** = `true` `🔗<class_TileMapLayer_property_collision_enabled>`

classref-property-setget

- `void (No return value.)` **set_collision_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collision_enabled**()

Enable or disable collisions.

classref-item-separator

classref-property

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **collision_visibility_mode** = `0` `🔗<class_TileMapLayer_property_collision_visibility_mode>`

classref-property-setget

- `void (No return value.)` **set_collision_visibility_mode**(value: `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`)
- `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **get_collision_visibility_mode**()

Show or hide the **TileMapLayer**'s collision shapes. If set to `DEBUG_VISIBILITY_MODE_DEFAULT<class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT>`, this depends on the show collision debug settings.

classref-item-separator

classref-property

`bool<class_bool>` **enabled** = `true` `🔗<class_TileMapLayer_property_enabled>`

classref-property-setget

- `void (No return value.)` **set_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_enabled**()

If `false`, disables this **TileMapLayer** completely (rendering, collision, navigation, scene tiles, etc.)

classref-item-separator

classref-property

`bool<class_bool>` **navigation_enabled** = `true` `🔗<class_TileMapLayer_property_navigation_enabled>`

classref-property-setget

- `void (No return value.)` **set_navigation_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_navigation_enabled**()

If `true`, navigation regions are enabled.

classref-item-separator

classref-property

`DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **navigation_visibility_mode** = `0` `🔗<class_TileMapLayer_property_navigation_visibility_mode>`

classref-property-setget

- `void (No return value.)` **set_navigation_visibility_mode**(value: `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>`)
- `DebugVisibilityMode<enum_TileMapLayer_DebugVisibilityMode>` **get_navigation_visibility_mode**()

Show or hide the **TileMapLayer**'s navigation meshes. If set to `DEBUG_VISIBILITY_MODE_DEFAULT<class_TileMapLayer_constant_DEBUG_VISIBILITY_MODE_DEFAULT>`, this depends on the show navigation debug settings.

classref-item-separator

classref-property

`bool<class_bool>` **occlusion_enabled** = `true` `🔗<class_TileMapLayer_property_occlusion_enabled>`

classref-property-setget

- `void (No return value.)` **set_occlusion_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_occlusion_enabled**()

Enable or disable light occlusion.

classref-item-separator

classref-property

`int<class_int>` **physics_quadrant_size** = `16` `🔗<class_TileMapLayer_property_physics_quadrant_size>`

classref-property-setget

- `void (No return value.)` **set_physics_quadrant_size**(value: `int<class_int>`)
- `int<class_int>` **get_physics_quadrant_size**()

The **TileMapLayer**'s physics quadrant size. Within a physics quadrant, cells with similar physics properties are grouped together and their collision shapes get merged. `physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>` defines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together `16 * 16 = 256` tiles.

**Note:** As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in the **TileMapLayer**'s local coordinate system.

**Note:** This impacts the value returned by `get_coords_for_body_rid()<class_TileMapLayer_method_get_coords_for_body_rid>`. Higher values will make that function less precise. To get the exact cell coordinates, you need to set `physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>` to `1`, which disables physics chunking.

classref-item-separator

classref-property

`int<class_int>` **rendering_quadrant_size** = `16` `🔗<class_TileMapLayer_property_rendering_quadrant_size>`

classref-property-setget

- `void (No return value.)` **set_rendering_quadrant_size**(value: `int<class_int>`)
- `int<class_int>` **get_rendering_quadrant_size**()

The **TileMapLayer**'s rendering quadrant size. A quadrant is a group of tiles to be drawn together on a single canvas item, for optimization purposes. `rendering_quadrant_size<class_TileMapLayer_property_rendering_quadrant_size>` defines the length of a square's side, in the map's coordinate system, that forms the quadrant. Thus, the default quadrant size groups together `16 * 16 = 256` tiles.

The quadrant size does not apply on a Y-sorted **TileMapLayer**, as tiles are grouped by Y position instead in that case.

**Note:** As quadrants are created according to the map's coordinate system, the quadrant's "square shape" might not look like square in the **TileMapLayer**'s local coordinate system.

classref-item-separator

classref-property

`PackedByteArray<class_PackedByteArray>` **tile_map_data** = `PackedByteArray()` `🔗<class_TileMapLayer_property_tile_map_data>`

classref-property-setget

- `void (No return value.)` **set_tile_map_data_from_array**(value: `PackedByteArray<class_PackedByteArray>`)
- `PackedByteArray<class_PackedByteArray>` **get_tile_map_data_as_array**()

The raw tile map data as a byte array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedByteArray<class_PackedByteArray>` for more details.

classref-item-separator

classref-property

`TileSet<class_TileSet>` **tile_set** `🔗<class_TileMapLayer_property_tile_set>`

classref-property-setget

- `void (No return value.)` **set_tile_set**(value: `TileSet<class_TileSet>`)
- `TileSet<class_TileSet>` **get_tile_set**()

The `TileSet<class_TileSet>` used by this layer. The textures, collisions, and additional behavior of all available tiles are stored here.

classref-item-separator

classref-property

`bool<class_bool>` **use_kinematic_bodies** = `false` `🔗<class_TileMapLayer_property_use_kinematic_bodies>`

classref-property-setget

- `void (No return value.)` **set_use_kinematic_bodies**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_kinematic_bodies**()

If `true`, this **TileMapLayer** collision shapes will be instantiated as kinematic bodies. This can be needed for moving **TileMapLayer** nodes (i.e. moving platforms).

classref-item-separator

classref-property

`bool<class_bool>` **x_draw_order_reversed** = `false` `🔗<class_TileMapLayer_property_x_draw_order_reversed>`

classref-property-setget

- `void (No return value.)` **set_x_draw_order_reversed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_x_draw_order_reversed**()

If `CanvasItem.y_sort_enabled<class_CanvasItem_property_y_sort_enabled>` is enabled, setting this to `true` will reverse the order the tiles are drawn on the X-axis.

classref-item-separator

classref-property

`int<class_int>` **y_sort_origin** = `0` `🔗<class_TileMapLayer_property_y_sort_origin>`

classref-property-setget

- `void (No return value.)` **set_y_sort_origin**(value: `int<class_int>`)
- `int<class_int>` **get_y_sort_origin**()

This Y-sort origin value is added to each tile's Y-sort origin value. This allows, for example, to fake a different height level. This can be useful for top-down view games.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_tile_data_runtime_update**(coords: `Vector2i<class_Vector2i>`, tile_data: `TileData<class_TileData>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TileMapLayer_private_method__tile_data_runtime_update>`

Called with a `TileData<class_TileData>` object about to be used internally by the **TileMapLayer**, allowing its modification at runtime.

This method is only called if `_use_tile_data_runtime_update()<class_TileMapLayer_private_method__use_tile_data_runtime_update>` is implemented and returns `true` for the given tile `coords`.

**Warning:** The `tile_data` object's sub-resources are the same as the one in the TileSet. Modifying them might impact the whole TileSet. Instead, make sure to duplicate those resources.

**Note:** If the properties of `tile_data` object should change over time, use `notify_runtime_tile_data_update()<class_TileMapLayer_method_notify_runtime_tile_data_update>` to notify the **TileMapLayer** it needs an update.

classref-item-separator

classref-method

`void (No return value.)` **\_update_cells**(coords: `Array<class_Array>`\[`Vector2i<class_Vector2i>`\], forced_cleanup: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TileMapLayer_private_method__update_cells>`

Called when this **TileMapLayer**'s cells need an internal update. This update may be caused from individual cells being modified or by a change in the `tile_set<class_TileMapLayer_property_tile_set>` (causing all cells to be queued for an update). The first call to this function is always for initializing all the **TileMapLayer**'s cells. `coords` contains the coordinates of all modified cells, roughly in the order they were modified. `forced_cleanup` is `true` when the **TileMapLayer**'s internals should be fully cleaned up. This is the case when:

- The layer is disabled;
- The layer is not visible;
- `tile_set<class_TileMapLayer_property_tile_set>` is set to `null`;
- The node is removed from the tree;
- The node is freed.

Note that any internal update happening while one of these conditions is verified is considered to be a "cleanup". See also `update_internals()<class_TileMapLayer_method_update_internals>`.

**Warning:** Implementing this method may degrade the **TileMapLayer**'s performance.

classref-item-separator

classref-method

`bool<class_bool>` **\_use_tile_data_runtime_update**(coords: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TileMapLayer_private_method__use_tile_data_runtime_update>`

Should return `true` if the tile at coordinates `coords` requires a runtime update.

**Warning:** Make sure this function only returns `true` when needed. Any tile processed at runtime without a need for it will imply a significant performance penalty.

**Note:** If the result of this function should change, use `notify_runtime_tile_data_update()<class_TileMapLayer_method_notify_runtime_tile_data_update>` to notify the **TileMapLayer** it needs an update.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_TileMapLayer_method_clear>`

Clears all cells.

classref-item-separator

classref-method

`void (No return value.)` **erase_cell**(coords: `Vector2i<class_Vector2i>`) `🔗<class_TileMapLayer_method_erase_cell>`

Erases the cell at coordinates `coords`.

classref-item-separator

classref-method

`void (No return value.)` **fix_invalid_tiles**() `🔗<class_TileMapLayer_method_fix_invalid_tiles>`

Clears cells containing tiles that do not exist in the `tile_set<class_TileMapLayer_property_tile_set>`.

classref-item-separator

classref-method

`int<class_int>` **get_cell_alternative_tile**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_cell_alternative_tile>`

Returns the tile alternative ID of the cell at coordinates `coords`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_cell_atlas_coords**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_cell_atlas_coords>`

Returns the tile atlas coordinates ID of the cell at coordinates `coords`. Returns `Vector2i(-1, -1)` if the cell does not exist.

classref-item-separator

classref-method

`int<class_int>` **get_cell_source_id**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_cell_source_id>`

Returns the tile source ID of the cell at coordinates `coords`. Returns `-1` if the cell does not exist.

classref-item-separator

classref-method

`TileData<class_TileData>` **get_cell_tile_data**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_cell_tile_data>`

Returns the `TileData<class_TileData>` object associated with the given cell, or `null` if the cell does not exist or is not a `TileSetAtlasSource<class_TileSetAtlasSource>`.

    func get_clicked_tile_power():
        var clicked_cell = tile_map_layer.local_to_map(tile_map_layer.get_local_mouse_position())
        var data = tile_map_layer.get_cell_tile_data(clicked_cell)
        if data:
            return data.get_custom_data("power")
        else:
            return 0

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_coords_for_body_rid**(body: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_coords_for_body_rid>`

Returns the coordinates of the physics quadrant (see `physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>`) for given physics body `RID<class_RID>`. Such an `RID<class_RID>` can be retrieved from `KinematicCollision2D.get_collider_rid()<class_KinematicCollision2D_method_get_collider_rid>`, when colliding with a tile.

**Note:** Higher values of `physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>` will make this function less precise. To get the exact cell coordinates, you need to set `physics_quadrant_size<class_TileMapLayer_property_physics_quadrant_size>` to `1`, which disables physics chunking.

classref-item-separator

classref-method

`RID<class_RID>` **get_navigation_map**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_navigation_map>`

Returns the `RID<class_RID>` of the `NavigationServer2D<class_NavigationServer2D>` navigation used by this **TileMapLayer**.

By default this returns the default `World2D<class_World2D>` navigation map, unless a custom map was provided using `set_navigation_map()<class_TileMapLayer_method_set_navigation_map>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_neighbor_cell**(coords: `Vector2i<class_Vector2i>`, neighbor: `CellNeighbor<enum_TileSet_CellNeighbor>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_neighbor_cell>`

Returns the neighboring cell to the one at coordinates `coords`, identified by the `neighbor` direction. This method takes into account the different layouts a TileMap can take.

classref-item-separator

classref-method

`TileMapPattern<class_TileMapPattern>` **get_pattern**(coords_array: `Array<class_Array>`\[`Vector2i<class_Vector2i>`\]) `🔗<class_TileMapLayer_method_get_pattern>`

Creates and returns a new `TileMapPattern<class_TileMapPattern>` from the given array of cells. See also `set_pattern()<class_TileMapLayer_method_set_pattern>`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **get_surrounding_cells**(coords: `Vector2i<class_Vector2i>`) `🔗<class_TileMapLayer_method_get_surrounding_cells>`

Returns the list of all neighboring cells to the one at `coords`. Any neighboring cell is one that is touching edges, so for a square cell 4 cells would be returned, for a hexagon 6 cells are returned.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **get_used_cells**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_used_cells>`

Returns a `Vector2i<class_Vector2i>` array with the positions of all cells containing a tile. A cell is considered empty if its source identifier equals `-1`, its atlas coordinate identifier is `Vector2(-1, -1)` and its alternative identifier is `-1`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **get_used_cells_by_id**(source_id: `int<class_int>` = -1, atlas_coords: `Vector2i<class_Vector2i>` = Vector2i(-1, -1), alternative_tile: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_used_cells_by_id>`

Returns a `Vector2i<class_Vector2i>` array with the positions of all cells containing a tile. Tiles may be filtered according to their source (`source_id`), their atlas coordinates (`atlas_coords`), or alternative id (`alternative_tile`).

If a parameter has its value set to the default one, this parameter is not used to filter a cell. Thus, if all parameters have their respective default values, this method returns the same result as `get_used_cells()<class_TileMapLayer_method_get_used_cells>`.

A cell is considered empty if its source identifier equals `-1`, its atlas coordinate identifier is `Vector2(-1, -1)` and its alternative identifier is `-1`.

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **get_used_rect**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_get_used_rect>`

Returns a rectangle enclosing the used (non-empty) tiles of the map.

classref-item-separator

classref-method

`bool<class_bool>` **has_body_rid**(body: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_has_body_rid>`

Returns whether the provided `body` `RID<class_RID>` belongs to one of this **TileMapLayer**'s cells.

classref-item-separator

classref-method

`bool<class_bool>` **is_cell_flipped_h**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_is_cell_flipped_h>`

Returns `true` if the cell at coordinates `coords` is flipped horizontally. The result is valid only for atlas sources.

classref-item-separator

classref-method

`bool<class_bool>` **is_cell_flipped_v**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_is_cell_flipped_v>`

Returns `true` if the cell at coordinates `coords` is flipped vertically. The result is valid only for atlas sources.

classref-item-separator

classref-method

`bool<class_bool>` **is_cell_transposed**(coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_is_cell_transposed>`

Returns `true` if the cell at coordinates `coords` is transposed. The result is valid only for atlas sources.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **local_to_map**(local_position: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_local_to_map>`

Returns the map coordinates of the cell containing the given `local_position`. If `local_position` is in global coordinates, consider using `Node2D.to_local()<class_Node2D_method_to_local>` before passing it to this method. See also `map_to_local()<class_TileMapLayer_method_map_to_local>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **map_pattern**(position_in_tilemap: `Vector2i<class_Vector2i>`, coords_in_pattern: `Vector2i<class_Vector2i>`, pattern: `TileMapPattern<class_TileMapPattern>`) `🔗<class_TileMapLayer_method_map_pattern>`

Returns for the given coordinates `coords_in_pattern` in a `TileMapPattern<class_TileMapPattern>` the corresponding cell coordinates if the pattern was pasted at the `position_in_tilemap` coordinates (see `set_pattern()<class_TileMapLayer_method_set_pattern>`). This mapping is required as in half-offset tile shapes, the mapping might not work by calculating `position_in_tile_map + coords_in_pattern`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **map_to_local**(map_position: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileMapLayer_method_map_to_local>`

Returns the centered position of a cell in the **TileMapLayer**'s local coordinate space. To convert the returned value into global coordinates, use `Node2D.to_global()<class_Node2D_method_to_global>`. See also `local_to_map()<class_TileMapLayer_method_local_to_map>`.

**Note:** This may not correspond to the visual position of the tile, i.e. it ignores the `TileData.texture_origin<class_TileData_property_texture_origin>` property of individual tiles.

classref-item-separator

classref-method

`void (No return value.)` **notify_runtime_tile_data_update**() `🔗<class_TileMapLayer_method_notify_runtime_tile_data_update>`

Notifies the **TileMapLayer** node that calls to `_use_tile_data_runtime_update()<class_TileMapLayer_private_method__use_tile_data_runtime_update>` or `_tile_data_runtime_update()<class_TileMapLayer_private_method__tile_data_runtime_update>` will lead to different results. This will thus trigger a **TileMapLayer** update.

**Warning:** Updating the **TileMapLayer** is computationally expensive and may impact performance. Try to limit the number of calls to this function to avoid unnecessary update.

**Note:** This does not trigger a direct update of the **TileMapLayer**, the update will be done at the end of the frame as usual (unless you call `update_internals()<class_TileMapLayer_method_update_internals>`).

classref-item-separator

classref-method

`void (No return value.)` **set_cell**(coords: `Vector2i<class_Vector2i>`, source_id: `int<class_int>` = -1, atlas_coords: `Vector2i<class_Vector2i>` = Vector2i(-1, -1), alternative_tile: `int<class_int>` = 0) `🔗<class_TileMapLayer_method_set_cell>`

Sets the tile identifiers for the cell at coordinates `coords`. Each tile of the `TileSet<class_TileSet>` is identified using three parts:

- The source identifier `source_id` identifies a `TileSetSource<class_TileSetSource>` identifier. See `TileSet.set_source_id()<class_TileSet_method_set_source_id>`,
- The atlas coordinate identifier `atlas_coords` identifies a tile coordinates in the atlas (if the source is a `TileSetAtlasSource<class_TileSetAtlasSource>`). For `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>` it should always be `Vector2i(0, 0)`,
- The alternative tile identifier `alternative_tile` identifies a tile alternative in the atlas (if the source is a `TileSetAtlasSource<class_TileSetAtlasSource>`), and the scene for a `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`.

If `source_id` is set to `-1`, `atlas_coords` to `Vector2i(-1, -1)`, or `alternative_tile` to `-1`, the cell will be erased. An erased cell gets **all** its identifiers automatically set to their respective invalid values, namely `-1`, `Vector2i(-1, -1)` and `-1`.

classref-item-separator

classref-method

`void (No return value.)` **set_cells_terrain_connect**(cells: `Array<class_Array>`\[`Vector2i<class_Vector2i>`\], terrain_set: `int<class_int>`, terrain: `int<class_int>`, ignore_empty_terrains: `bool<class_bool>` = true) `🔗<class_TileMapLayer_method_set_cells_terrain_connect>`

Update all the cells in the `cells` coordinates array so that they use the given `terrain` for the given `terrain_set`. If an updated cell has the same terrain as one of its neighboring cells, this function tries to join the two. This function might update neighboring tiles if needed to create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.

**Note:** To work correctly, this method requires the **TileMapLayer**'s TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.

classref-item-separator

classref-method

`void (No return value.)` **set_cells_terrain_path**(path: `Array<class_Array>`\[`Vector2i<class_Vector2i>`\], terrain_set: `int<class_int>`, terrain: `int<class_int>`, ignore_empty_terrains: `bool<class_bool>` = true) `🔗<class_TileMapLayer_method_set_cells_terrain_path>`

Update all the cells in the `path` coordinates array so that they use the given `terrain` for the given `terrain_set`. The function will also connect two successive cell in the path with the same terrain. This function might update neighboring tiles if needed to create correct terrain transitions.

If `ignore_empty_terrains` is `true`, empty terrains will be ignored when trying to find the best fitting tile for the given terrain constraints.

**Note:** To work correctly, this method requires the **TileMapLayer**'s TileSet to have terrains set up with all required terrain combinations. Otherwise, it may produce unexpected results.

classref-item-separator

classref-method

`void (No return value.)` **set_navigation_map**(map: `RID<class_RID>`) `🔗<class_TileMapLayer_method_set_navigation_map>`

Sets a custom `map` as a `NavigationServer2D<class_NavigationServer2D>` navigation map. If not set, uses the default `World2D<class_World2D>` navigation map instead.

classref-item-separator

classref-method

`void (No return value.)` **set_pattern**(position: `Vector2i<class_Vector2i>`, pattern: `TileMapPattern<class_TileMapPattern>`) `🔗<class_TileMapLayer_method_set_pattern>`

Pastes the `TileMapPattern<class_TileMapPattern>` at the given `position` in the tile map. See also `get_pattern()<class_TileMapLayer_method_get_pattern>`.

classref-item-separator

classref-method

`void (No return value.)` **update_internals**() `🔗<class_TileMapLayer_method_update_internals>`

Triggers a direct update of the **TileMapLayer**. Usually, calling this function is not needed, as **TileMapLayer** node updates automatically when one of its properties or cells is modified.

However, for performance reasons, those updates are batched and delayed to the end of the frame. Calling this function will force the **TileMapLayer** to update right away instead.

**Warning:** Updating the **TileMapLayer** is computationally expensive and may impact performance. Try to limit the number of updates and how many tiles they impact.