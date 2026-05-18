github_url
hide

# NavigationMeshSourceGeometryData2D

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

`void (No return value.)` **add_obstruction_outline**(shape_outline: `PackedVector2Array<class_PackedVector2Array>`) `🔗<class_NavigationMeshSourceGeometryData2D_method_add_obstruction_outline>`

Adds the outline points of a shape as obstructed area.

classref-item-separator

classref-method

`void (No return value.)` **add_projected_obstruction**(vertices: `PackedVector2Array<class_PackedVector2Array>`, carve: `bool<class_bool>`) `🔗<class_NavigationMeshSourceGeometryData2D_method_add_projected_obstruction>`

Adds a projected obstruction shape to the source geometry. If `carve` is `true` the carved shape will not be affected by additional offsets (e.g. agent radius) of the navigation mesh baking process.

classref-item-separator

classref-method

`void (No return value.)` **add_traversable_outline**(shape_outline: `PackedVector2Array<class_PackedVector2Array>`) `🔗<class_NavigationMeshSourceGeometryData2D_method_add_traversable_outline>`

Adds the outline points of a shape as traversable area.

classref-item-separator

classref-method

`void (No return value.)` **append_obstruction_outlines**(obstruction_outlines: `Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\]) `🔗<class_NavigationMeshSourceGeometryData2D_method_append_obstruction_outlines>`

Appends another array of `obstruction_outlines` at the end of the existing obstruction outlines array.

classref-item-separator

classref-method

`void (No return value.)` **append_traversable_outlines**(traversable_outlines: `Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\]) `🔗<class_NavigationMeshSourceGeometryData2D_method_append_traversable_outlines>`

Appends another array of `traversable_outlines` at the end of the existing traversable outlines array.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_NavigationMeshSourceGeometryData2D_method_clear>`

Clears the internal data.

classref-item-separator

classref-method

`void (No return value.)` **clear_projected_obstructions**() `🔗<class_NavigationMeshSourceGeometryData2D_method_clear_projected_obstructions>`

Clears all projected obstructions.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **get_bounds**() `🔗<class_NavigationMeshSourceGeometryData2D_method_get_bounds>`

Returns an axis-aligned bounding box that covers all the stored geometry data. The bounds are calculated when calling this function with the result cached until further geometry changes are made.

classref-item-separator

classref-method

`Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\] **get_obstruction_outlines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationMeshSourceGeometryData2D_method_get_obstruction_outlines>`

Returns all the obstructed area outlines arrays.

classref-item-separator

classref-method

`Array<class_Array>` **get_projected_obstructions**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationMeshSourceGeometryData2D_method_get_projected_obstructions>`

Returns the projected obstructions as an `Array<class_Array>` of dictionaries. Each `Dictionary<class_Dictionary>` contains the following entries:

- `vertices` - A `PackedFloat32Array<class_PackedFloat32Array>` that defines the outline points of the projected shape.
- `carve` - A `bool<class_bool>` that defines how the projected shape affects the navigation mesh baking. If `true` the projected shape will not be affected by addition offsets, e.g. agent radius.

classref-item-separator

classref-method

`Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\] **get_traversable_outlines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationMeshSourceGeometryData2D_method_get_traversable_outlines>`

Returns all the traversable area outlines arrays.

classref-item-separator

classref-method

`bool<class_bool>` **has_data**() `🔗<class_NavigationMeshSourceGeometryData2D_method_has_data>`

Returns `true` when parsed source geometry data exists.

classref-item-separator

classref-method

`void (No return value.)` **merge**(other_geometry: `NavigationMeshSourceGeometryData2D<class_NavigationMeshSourceGeometryData2D>`) `🔗<class_NavigationMeshSourceGeometryData2D_method_merge>`

Adds the geometry data of another **NavigationMeshSourceGeometryData2D** to the navigation mesh baking data.

classref-item-separator

classref-method

`void (No return value.)` **set_obstruction_outlines**(obstruction_outlines: `Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\]) `🔗<class_NavigationMeshSourceGeometryData2D_method_set_obstruction_outlines>`

Sets all the obstructed area outlines arrays.

classref-item-separator

classref-method

`void (No return value.)` **set_projected_obstructions**(projected_obstructions: `Array<class_Array>`) `🔗<class_NavigationMeshSourceGeometryData2D_method_set_projected_obstructions>`

Sets the projected obstructions with an Array of Dictionaries with the following key value pairs:

gdscript

"vertices" : PackedFloat32Array "carve" : bool

classref-item-separator

classref-method

`void (No return value.)` **set_traversable_outlines**(traversable_outlines: `Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\]) `🔗<class_NavigationMeshSourceGeometryData2D_method_set_traversable_outlines>`

Sets all the traversable area outlines arrays.