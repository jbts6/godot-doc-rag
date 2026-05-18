github_url
hide

# GraphElement

**Inherits:** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `GraphFrame<class_GraphFrame>`, `GraphNode<class_GraphNode>`

A container that represents a basic element that can be placed inside a `GraphEdit<class_GraphEdit>` control.

classref-introduction-group

## Description

**GraphElement** allows to create custom elements for a `GraphEdit<class_GraphEdit>` graph. By default such elements can be selected, resized, and repositioned, but they cannot be connected. For a graph element that allows for connections see `GraphNode<class_GraphNode>`.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**delete_request**() `🔗<class_GraphElement_signal_delete_request>`

Emitted when removing the GraphElement is requested.

classref-item-separator

classref-signal

**dragged**(from: `Vector2<class_Vector2>`, to: `Vector2<class_Vector2>`) `🔗<class_GraphElement_signal_dragged>`

Emitted when the GraphElement is dragged.

classref-item-separator

classref-signal

**node_deselected**() `🔗<class_GraphElement_signal_node_deselected>`

Emitted when the GraphElement is deselected.

classref-item-separator

classref-signal

**node_selected**() `🔗<class_GraphElement_signal_node_selected>`

Emitted when the GraphElement is selected.

classref-item-separator

classref-signal

**position_offset_changed**() `🔗<class_GraphElement_signal_position_offset_changed>`

Emitted when the GraphElement is moved.

classref-item-separator

classref-signal

**raise_request**() `🔗<class_GraphElement_signal_raise_request>`

Emitted when displaying the GraphElement over other ones is requested. Happens on focusing (clicking into) the GraphElement.

classref-item-separator

classref-signal

**resize_end**(new_size: `Vector2<class_Vector2>`) `🔗<class_GraphElement_signal_resize_end>`

Emitted when releasing the mouse button after dragging the resizer handle (see `resizable<class_GraphElement_property_resizable>`).

classref-item-separator

classref-signal

**resize_request**(new_size: `Vector2<class_Vector2>`) `🔗<class_GraphElement_signal_resize_request>`

Emitted when resizing the GraphElement is requested. Happens on dragging the resizer handle (see `resizable<class_GraphElement_property_resizable>`).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **draggable** = `true` `🔗<class_GraphElement_property_draggable>`

classref-property-setget

- `void (No return value.)` **set_draggable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_draggable**()

If `true`, the user can drag the GraphElement.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **position_offset** = `Vector2(0, 0)` `🔗<class_GraphElement_property_position_offset>`

classref-property-setget

- `void (No return value.)` **set_position_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_position_offset**()

The offset of the GraphElement, relative to the scroll offset of the `GraphEdit<class_GraphEdit>`.

classref-item-separator

classref-property

`bool<class_bool>` **resizable** = `false` `🔗<class_GraphElement_property_resizable>`

classref-property-setget

- `void (No return value.)` **set_resizable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_resizable**()

If `true`, the user can resize the GraphElement.

**Note:** Dragging the handle will only emit the `resize_request<class_GraphElement_signal_resize_request>` and `resize_end<class_GraphElement_signal_resize_end>` signals, the GraphElement needs to be resized manually.

classref-item-separator

classref-property

`bool<class_bool>` **scaling_menus** = `false` `🔗<class_GraphElement_property_scaling_menus>`

classref-property-setget

- `void (No return value.)` **set_scaling_menus**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_scaling_menus**()

If `true`, `PopupMenu<class_PopupMenu>`s that are descendants of the GraphElement are scaled with the `GraphEdit<class_GraphEdit>` zoom.

classref-item-separator

classref-property

`bool<class_bool>` **selectable** = `true` `🔗<class_GraphElement_property_selectable>`

classref-property-setget

- `void (No return value.)` **set_selectable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_selectable**()

If `true`, the user can select the GraphElement.

classref-item-separator

classref-property

`bool<class_bool>` **selected** = `false` `🔗<class_GraphElement_property_selected>`

classref-property-setget

- `void (No return value.)` **set_selected**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_selected**()

If `true`, the GraphElement is selected.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Texture2D<class_Texture2D>` **resizer** `🔗<class_GraphElement_theme_icon_resizer>`

The icon used for the resizer, visible when `resizable<class_GraphElement_property_resizable>` is enabled.