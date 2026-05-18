github_url
hide

# EditorSelection

**Inherits:** `Object<class_Object>`

Manages the SceneTree selection in the editor.

classref-introduction-group

## Description

This object manages the SceneTree selection in the editor.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using `EditorInterface.get_selection()<class_EditorInterface_method_get_selection>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**selection_changed**() `🔗<class_EditorSelection_signal_selection_changed>`

Emitted when the selection changes.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_node**(node: `Node<class_Node>`) `🔗<class_EditorSelection_method_add_node>`

Adds a node to the selection.

**Note:** The newly selected node will not be automatically edited in the inspector. If you want to edit a node, use `EditorInterface.edit_node()<class_EditorInterface_method_edit_node>`.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_EditorSelection_method_clear>`

Clear the selection.

classref-item-separator

classref-method

`Array<class_Array>`\[`Node<class_Node>`\] **get_selected_nodes**() `🔗<class_EditorSelection_method_get_selected_nodes>`

Returns the list of selected nodes.

classref-item-separator

classref-method

`Array<class_Array>`\[`Node<class_Node>`\] **get_top_selected_nodes**() `🔗<class_EditorSelection_method_get_top_selected_nodes>`

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.).

For example, if there is a node A with a child B and a sibling C, then selecting all three will cause this method to return only A and C. Changing the global transform of A will affect the global transform of B, so there is no need to change B separately.

classref-item-separator

classref-method

`Array<class_Array>`\[`Node<class_Node>`\] **get_transformable_selected_nodes**() `🔗<class_EditorSelection_method_get_transformable_selected_nodes>`

**Deprecated:** Use `get_top_selected_nodes()<class_EditorSelection_method_get_top_selected_nodes>` instead.

Returns the list of top selected nodes only, excluding any children. This is useful for performing transform operations (moving them, rotating, etc.). See `get_top_selected_nodes()<class_EditorSelection_method_get_top_selected_nodes>`.

classref-item-separator

classref-method

`void (No return value.)` **remove_node**(node: `Node<class_Node>`) `🔗<class_EditorSelection_method_remove_node>`

Removes a node from the selection.