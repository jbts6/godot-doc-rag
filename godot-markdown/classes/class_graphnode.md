github_url
hide

# GraphNode

**Inherits:** `GraphElement<class_GraphElement>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A container with connection ports, representing a node in a `GraphEdit<class_GraphEdit>`.

classref-introduction-group

## Description

**GraphNode** allows to create nodes for a `GraphEdit<class_GraphEdit>` graph with customizable content based on its child controls. **GraphNode** is derived from `Container<class_Container>` and it is responsible for placing its children on screen. This works similar to `VBoxContainer<class_VBoxContainer>`. Children, in turn, provide **GraphNode** with so-called slots, each of which can have a connection port on either side.

Each **GraphNode** slot is defined by its index and can provide the node with up to two ports: one on the left, and one on the right. By convention the left port is also referred to as the **input port** and the right port is referred to as the **output port**. Each port can be enabled and configured individually, using different type and color. The type is an arbitrary value that you can define using your own considerations. The parent `GraphEdit<class_GraphEdit>` will receive this information on each connect and disconnect request.

Slots can be configured in the Inspector dock once you add at least one child `Control<class_Control>`. The properties are grouped by each slot's index in the "Slot" section.

**Note:** While GraphNode is set up using slots and slot indices, connections are made between the ports which are enabled. Because of that `GraphEdit<class_GraphEdit>` uses the port's index and not the slot's index. You can use `get_input_port_slot()<class_GraphNode_method_get_input_port_slot>` and `get_output_port_slot()<class_GraphNode_method_get_output_port_slot>` to get the slot index from the port index.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**slot_sizes_changed**() `🔗<class_GraphNode_signal_slot_sizes_changed>`

Emitted when any slot's size might have changed.

classref-item-separator

classref-signal

**slot_updated**(slot_index: `int<class_int>`) `🔗<class_GraphNode_signal_slot_updated>`

Emitted when any GraphNode's slot is updated.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **ignore_invalid_connection_type** = `false` `🔗<class_GraphNode_property_ignore_invalid_connection_type>`

classref-property-setget

- `void (No return value.)` **set_ignore_invalid_connection_type**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_ignoring_valid_connection_type**()

If `true`, you can connect ports with different types, even if the connection was not explicitly allowed in the parent `GraphEdit<class_GraphEdit>`.

classref-item-separator

classref-property

`FocusMode<enum_Control_FocusMode>` **slots_focus_mode** = `3` `🔗<class_GraphNode_property_slots_focus_mode>`

classref-property-setget

- `void (No return value.)` **set_slots_focus_mode**(value: `FocusMode<enum_Control_FocusMode>`)
- `FocusMode<enum_Control_FocusMode>` **get_slots_focus_mode**()

Determines how connection slots can be focused.

- If set to `Control.FOCUS_CLICK<class_Control_constant_FOCUS_CLICK>`, connections can only be made with the mouse.
- If set to `Control.FOCUS_ALL<class_Control_constant_FOCUS_ALL>`, slots can also be focused using the `ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>` and `ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>` and connected using `ProjectSettings.input/ui_left<class_ProjectSettings_property_input/ui_left>` and `ProjectSettings.input/ui_right<class_ProjectSettings_property_input/ui_right>` input actions.
- If set to `Control.FOCUS_ACCESSIBILITY<class_Control_constant_FOCUS_ACCESSIBILITY>`, slot input actions are only enabled when the screen reader is active.

classref-item-separator

classref-property

`String<class_String>` **title** = `""` `🔗<class_GraphNode_property_title>`

classref-property-setget

- `void (No return value.)` **set_title**(value: `String<class_String>`)
- `String<class_String>` **get_title**()

The text displayed in the GraphNode's title bar.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_draw_port**(slot_index: `int<class_int>`, position: `Vector2i<class_Vector2i>`, left: `bool<class_bool>`, color: `Color<class_Color>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_GraphNode_private_method__draw_port>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **clear_all_slots**() `🔗<class_GraphNode_method_clear_all_slots>`

Disables all slots of the GraphNode. This will remove all input/output ports from the GraphNode.

classref-item-separator

classref-method

`void (No return value.)` **clear_slot**(slot_index: `int<class_int>`) `🔗<class_GraphNode_method_clear_slot>`

Disables the slot with the given `slot_index`. This will remove the corresponding input and output port from the GraphNode.

classref-item-separator

classref-method

`Color<class_Color>` **get_input_port_color**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_input_port_color>`

Returns the `Color<class_Color>` of the input port with the given `port_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_input_port_count**() `🔗<class_GraphNode_method_get_input_port_count>`

Returns the number of slots with an enabled input port.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_input_port_position**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_input_port_position>`

Returns the position of the input port with the given `port_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_input_port_slot**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_input_port_slot>`

Returns the corresponding slot index of the input port with the given `port_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_input_port_type**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_input_port_type>`

Returns the type of the input port with the given `port_idx`.

classref-item-separator

classref-method

`Color<class_Color>` **get_output_port_color**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_output_port_color>`

Returns the `Color<class_Color>` of the output port with the given `port_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_output_port_count**() `🔗<class_GraphNode_method_get_output_port_count>`

Returns the number of slots with an enabled output port.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_output_port_position**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_output_port_position>`

Returns the position of the output port with the given `port_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_output_port_slot**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_output_port_slot>`

Returns the corresponding slot index of the output port with the given `port_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_output_port_type**(port_idx: `int<class_int>`) `🔗<class_GraphNode_method_get_output_port_type>`

Returns the type of the output port with the given `port_idx`.

classref-item-separator

classref-method

`Color<class_Color>` **get_slot_color_left**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_color_left>`

Returns the left (input) `Color<class_Color>` of the slot with the given `slot_index`.

classref-item-separator

classref-method

`Color<class_Color>` **get_slot_color_right**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_color_right>`

Returns the right (output) `Color<class_Color>` of the slot with the given `slot_index`.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_slot_custom_icon_left**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_custom_icon_left>`

Returns the left (input) custom `Texture2D<class_Texture2D>` of the slot with the given `slot_index`.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_slot_custom_icon_right**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_custom_icon_right>`

Returns the right (output) custom `Texture2D<class_Texture2D>` of the slot with the given `slot_index`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_slot_metadata_left**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_metadata_left>`

Returns the left (input) metadata of the slot with the given `slot_index`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_slot_metadata_right**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_metadata_right>`

Returns the right (output) metadata of the slot with the given `slot_index`.

classref-item-separator

classref-method

`int<class_int>` **get_slot_type_left**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_type_left>`

Returns the left (input) type of the slot with the given `slot_index`.

classref-item-separator

classref-method

`int<class_int>` **get_slot_type_right**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_get_slot_type_right>`

Returns the right (output) type of the slot with the given `slot_index`.

classref-item-separator

classref-method

`HBoxContainer<class_HBoxContainer>` **get_titlebar_hbox**() `🔗<class_GraphNode_method_get_titlebar_hbox>`

Returns the `HBoxContainer<class_HBoxContainer>` used for the title bar, only containing a `Label<class_Label>` for displaying the title by default. This can be used to add custom controls to the title bar such as option or close buttons.

classref-item-separator

classref-method

`bool<class_bool>` **is_slot_draw_stylebox**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_is_slot_draw_stylebox>`

Returns `true` if the background `StyleBox<class_StyleBox>` of the slot with the given `slot_index` is drawn.

classref-item-separator

classref-method

`bool<class_bool>` **is_slot_enabled_left**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_is_slot_enabled_left>`

Returns `true` if left (input) side of the slot with the given `slot_index` is enabled.

classref-item-separator

classref-method

`bool<class_bool>` **is_slot_enabled_right**(slot_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GraphNode_method_is_slot_enabled_right>`

Returns `true` if right (output) side of the slot with the given `slot_index` is enabled.

classref-item-separator

classref-method

`void (No return value.)` **set_slot**(slot_index: `int<class_int>`, enable_left_port: `bool<class_bool>`, type_left: `int<class_int>`, color_left: `Color<class_Color>`, enable_right_port: `bool<class_bool>`, type_right: `int<class_int>`, color_right: `Color<class_Color>`, custom_icon_left: `Texture2D<class_Texture2D>` = null, custom_icon_right: `Texture2D<class_Texture2D>` = null, draw_stylebox: `bool<class_bool>` = true) `🔗<class_GraphNode_method_set_slot>`

Sets properties of the slot with the given `slot_index`.

If `enable_left_port`/`enable_right_port` is `true`, a port will appear and the slot will be able to be connected from this side.

With `type_left`/`type_right` an arbitrary type can be assigned to each port. Two ports can be connected if they share the same type, or if the connection between their types is allowed in the parent `GraphEdit<class_GraphEdit>` (see `GraphEdit.add_valid_connection_type()<class_GraphEdit_method_add_valid_connection_type>`). Keep in mind that the `GraphEdit<class_GraphEdit>` has the final say in accepting the connection. Type compatibility simply allows the `GraphEdit.connection_request<class_GraphEdit_signal_connection_request>` signal to be emitted.

Ports can be further customized using `color_left`/`color_right` and `custom_icon_left`/`custom_icon_right`. The color parameter adds a tint to the icon. The custom icon can be used to override the default port dot.

Additionally, `draw_stylebox` can be used to enable or disable drawing of the background stylebox for each slot. See `slot<class_GraphNode_theme_style_slot>`.

Individual properties can also be set using one of the `set_slot_*` methods.

**Note:** This method only sets properties of the slot. To create the slot itself, add a `Control<class_Control>`-derived child to the GraphNode.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_color_left**(slot_index: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_GraphNode_method_set_slot_color_left>`

Sets the `Color<class_Color>` of the left (input) side of the slot with the given `slot_index` to `color`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_color_right**(slot_index: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_GraphNode_method_set_slot_color_right>`

Sets the `Color<class_Color>` of the right (output) side of the slot with the given `slot_index` to `color`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_custom_icon_left**(slot_index: `int<class_int>`, custom_icon: `Texture2D<class_Texture2D>`) `🔗<class_GraphNode_method_set_slot_custom_icon_left>`

Sets the custom `Texture2D<class_Texture2D>` of the left (input) side of the slot with the given `slot_index` to `custom_icon`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_custom_icon_right**(slot_index: `int<class_int>`, custom_icon: `Texture2D<class_Texture2D>`) `🔗<class_GraphNode_method_set_slot_custom_icon_right>`

Sets the custom `Texture2D<class_Texture2D>` of the right (output) side of the slot with the given `slot_index` to `custom_icon`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_draw_stylebox**(slot_index: `int<class_int>`, enable: `bool<class_bool>`) `🔗<class_GraphNode_method_set_slot_draw_stylebox>`

Toggles the background `StyleBox<class_StyleBox>` of the slot with the given `slot_index`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_enabled_left**(slot_index: `int<class_int>`, enable: `bool<class_bool>`) `🔗<class_GraphNode_method_set_slot_enabled_left>`

Toggles the left (input) side of the slot with the given `slot_index`. If `enable` is `true`, a port will appear on the left side and the slot will be able to be connected from this side.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_enabled_right**(slot_index: `int<class_int>`, enable: `bool<class_bool>`) `🔗<class_GraphNode_method_set_slot_enabled_right>`

Toggles the right (output) side of the slot with the given `slot_index`. If `enable` is `true`, a port will appear on the right side and the slot will be able to be connected from this side.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_metadata_left**(slot_index: `int<class_int>`, value: `Variant<class_Variant>`) `🔗<class_GraphNode_method_set_slot_metadata_left>`

Sets the custom metadata for the left (input) side of the slot with the given `slot_index` to `value`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_metadata_right**(slot_index: `int<class_int>`, value: `Variant<class_Variant>`) `🔗<class_GraphNode_method_set_slot_metadata_right>`

Sets the custom metadata for the right (output) side of the slot with the given `slot_index` to `value`.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_type_left**(slot_index: `int<class_int>`, type: `int<class_int>`) `🔗<class_GraphNode_method_set_slot_type_left>`

Sets the left (input) type of the slot with the given `slot_index` to `type`. If the value is negative, all connections will be disallowed to be created via user inputs.

classref-item-separator

classref-method

`void (No return value.)` **set_slot_type_right**(slot_index: `int<class_int>`, type: `int<class_int>`) `🔗<class_GraphNode_method_set_slot_type_right>`

Sets the right (output) type of the slot with the given `slot_index` to `type`. If the value is negative, all connections will be disallowed to be created via user inputs.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **resizer_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_GraphNode_theme_color_resizer_color>`

The color modulation applied to the resizer icon.

classref-item-separator

classref-themeproperty

`int<class_int>` **port_h_offset** = `0` `🔗<class_GraphNode_theme_constant_port_h_offset>`

Horizontal offset for the ports.

classref-item-separator

classref-themeproperty

`int<class_int>` **separation** = `2` `🔗<class_GraphNode_theme_constant_separation>`

The vertical distance between ports.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **port** `🔗<class_GraphNode_theme_icon_port>`

The icon used for representing ports.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel** `🔗<class_GraphNode_theme_style_panel>`

The default background for the slot area of the **GraphNode**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel_focus** `🔗<class_GraphNode_theme_style_panel_focus>`

`StyleBox<class_StyleBox>` used when the **GraphNode** is focused (when used with assistive apps).

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel_selected** `🔗<class_GraphNode_theme_style_panel_selected>`

The `StyleBox<class_StyleBox>` used for the slot area when selected.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **slot** `🔗<class_GraphNode_theme_style_slot>`

The `StyleBox<class_StyleBox>` used for each slot of the **GraphNode**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **slot_selected** `🔗<class_GraphNode_theme_style_slot_selected>`

`StyleBox<class_StyleBox>` used when the slot is focused (when used with assistive apps).

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **titlebar** `🔗<class_GraphNode_theme_style_titlebar>`

The `StyleBox<class_StyleBox>` used for the title bar of the **GraphNode**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **titlebar_selected** `🔗<class_GraphNode_theme_style_titlebar_selected>`

The `StyleBox<class_StyleBox>` used for the title bar of the **GraphNode** when it is selected.