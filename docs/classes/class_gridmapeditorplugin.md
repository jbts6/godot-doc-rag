github_url
hide

# GridMapEditorPlugin

**Inherits:** `EditorPlugin<class_EditorPlugin>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Editor for `GridMap<class_GridMap>` nodes.

classref-introduction-group

## Description

GridMapEditorPlugin provides access to the `GridMap<class_GridMap>` editor functionality.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_selection**() `🔗<class_GridMapEditorPlugin_method_clear_selection>`

Deselects any currently selected cells.

classref-item-separator

classref-method

`GridMap<class_GridMap>` **get_current_grid_map**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMapEditorPlugin_method_get_current_grid_map>`

Returns the `GridMap<class_GridMap>` node currently edited by the grid map editor.

classref-item-separator

classref-method

`Array<class_Array>` **get_selected_cells**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMapEditorPlugin_method_get_selected_cells>`

Returns an array of `Vector3i<class_Vector3i>`s with the selected cells' coordinates.

classref-item-separator

classref-method

`int<class_int>` **get_selected_palette_item**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMapEditorPlugin_method_get_selected_palette_item>`

Returns the index of the selected `MeshLibrary<class_MeshLibrary>` item in the grid map editor's palette or `-1` if no item is selected.

**Note:** The indices might not be in the same order as they appear in the editor's interface.

classref-item-separator

classref-method

`AABB<class_AABB>` **get_selection**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMapEditorPlugin_method_get_selection>`

Returns the cell coordinate bounds of the current selection. Use `has_selection()<class_GridMapEditorPlugin_method_has_selection>` to check if there is an active selection.

classref-item-separator

classref-method

`bool<class_bool>` **has_selection**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMapEditorPlugin_method_has_selection>`

Returns `true` if there are selected cells.

classref-item-separator

classref-method

`void (No return value.)` **set_selected_palette_item**(item: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GridMapEditorPlugin_method_set_selected_palette_item>`

Selects the `MeshLibrary<class_MeshLibrary>` item with the given index in the grid map editor's palette. If a negative index is given, no item will be selected. If a value greater than the last index is given, the last item will be selected.

**Note:** The indices might not be in the same order as they appear in the editor's interface.

classref-item-separator

classref-method

`void (No return value.)` **set_selection**(begin: `Vector3i<class_Vector3i>`, end: `Vector3i<class_Vector3i>`) `🔗<class_GridMapEditorPlugin_method_set_selection>`

Selects the cells inside the given bounds from `begin` to `end`.