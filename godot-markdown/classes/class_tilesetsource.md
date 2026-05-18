github_url
hide

# TileSetSource

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `TileSetAtlasSource<class_TileSetAtlasSource>`, `TileSetScenesCollectionSource<class_TileSetScenesCollectionSource>`

Exposes a set of tiles for a `TileSet<class_TileSet>` resource.

classref-introduction-group

## Description

Exposes a set of tiles for a `TileSet<class_TileSet>` resource.

Tiles in a source are indexed with two IDs, coordinates ID (of type Vector2i) and an alternative ID (of type int), named according to their use in the `TileSetAtlasSource<class_TileSetAtlasSource>` class.

Depending on the TileSet source type, those IDs might have restrictions on their values, this is why the base **TileSetSource** class only exposes getters for them.

You can iterate over all tiles exposed by a TileSetSource by first iterating over coordinates IDs using `get_tiles_count()<class_TileSetSource_method_get_tiles_count>` and `get_tile_id()<class_TileSetSource_method_get_tile_id>`, then over alternative IDs using `get_alternative_tiles_count()<class_TileSetSource_method_get_alternative_tiles_count>` and `get_alternative_tile_id()<class_TileSetSource_method_get_alternative_tile_id>`.

**Warning:** **TileSetSource** can only be added to one TileSet at the same time. Calling `TileSet.add_source()<class_TileSet_method_add_source>` on a second `TileSet<class_TileSet>` will remove the source from the first one.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_alternative_tile_id**(atlas_coords: `Vector2i<class_Vector2i>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileSetSource_method_get_alternative_tile_id>`

Returns the alternative ID for the tile with coordinates ID `atlas_coords` at index `index`.

classref-item-separator

classref-method

`int<class_int>` **get_alternative_tiles_count**(atlas_coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileSetSource_method_get_alternative_tiles_count>`

Returns the number of alternatives tiles for the coordinates ID `atlas_coords`.

For `TileSetAtlasSource<class_TileSetAtlasSource>`, this always return at least 1, as the base tile with ID 0 is always part of the alternatives list.

Returns -1 if there is not tile at the given coords.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_tile_id**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileSetSource_method_get_tile_id>`

Returns the tile coordinates ID of the tile with index `index`.

classref-item-separator

classref-method

`int<class_int>` **get_tiles_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileSetSource_method_get_tiles_count>`

Returns how many tiles this atlas source defines (not including alternative tiles).

classref-item-separator

classref-method

`bool<class_bool>` **has_alternative_tile**(atlas_coords: `Vector2i<class_Vector2i>`, alternative_tile: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileSetSource_method_has_alternative_tile>`

Returns if the base tile at coordinates `atlas_coords` has an alternative with ID `alternative_tile`.

classref-item-separator

classref-method

`bool<class_bool>` **has_tile**(atlas_coords: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TileSetSource_method_has_tile>`

Returns if this atlas has a tile with coordinates ID `atlas_coords`.