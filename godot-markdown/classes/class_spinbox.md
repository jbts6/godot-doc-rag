github_url
hide

# SpinBox

**Inherits:** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

An input field for numbers.

classref-introduction-group

## Description

**SpinBox** is a numerical input text field. It allows entering integers and floating-point numbers. The **SpinBox** also has up and down buttons that can be clicked to increase or decrease the value. The value can also be changed by dragging the mouse up or down over the **SpinBox**'s arrows.

Additionally, mathematical expressions can be entered. These are evaluated when the user presses `Enter` while editing the **SpinBox**'s text field. This uses the `Expression<class_Expression>` class to parse and evaluate the expression. The result of the expression is then set as the value of the **SpinBox**. Some examples of valid expressions are `5 + 2 * 3`, `pow(2, 4)`, and `PI + sin(0.5)`. Expressions are case-sensitive.

**Example:** Create a **SpinBox**, disable its context menu and set its text alignment to right.

gdscript

var spin_box = SpinBox.new() add_child(spin_box) var line_edit = spin_box.get_line_edit() line_edit.context_menu_enabled = false spin_box.horizontal_alignment = LineEdit.HORIZONTAL_ALIGNMENT_RIGHT

csharp

var spinBox = new SpinBox(); AddChild(spinBox); var lineEdit = spinBox.GetLineEdit(); lineEdit.ContextMenuEnabled = false; spinBox.AlignHorizontal = LineEdit.HorizontalAlignEnum.Right;

See `Range<class_Range>` class for more options over the **SpinBox**.

**Note:** With the **SpinBox**'s context menu disabled, you can right-click the bottom half of the spinbox to set the value to its minimum, while right-clicking the top half sets the value to its maximum.

**Note:** **SpinBox** relies on an underlying `LineEdit<class_LineEdit>` node. To theme a **SpinBox**'s background, add theme items for `LineEdit<class_LineEdit>` and customize them. The `LineEdit<class_LineEdit>` has the `SpinBoxInnerLineEdit` theme variation, so that you can give it a distinct appearance from regular `LineEdit<class_LineEdit>`s.

**Note:** If you want to implement drag and drop for the underlying `LineEdit<class_LineEdit>`, you can use `Control.set_drag_forwarding()<class_Control_method_set_drag_forwarding>` on the node returned by `get_line_edit()<class_SpinBox_method_get_line_edit>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **alignment** = `0` `🔗<class_SpinBox_property_alignment>`

classref-property-setget

- `void (No return value.)` **set_horizontal_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_horizontal_alignment**()

Changes the alignment of the underlying `LineEdit<class_LineEdit>`.

classref-item-separator

classref-property

`bool<class_bool>` **custom_arrow_round** = `false` `🔗<class_SpinBox_property_custom_arrow_round>`

classref-property-setget

- `void (No return value.)` **set_custom_arrow_round**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_custom_arrow_rounding**()

If `true`, the value will be rounded to a multiple of `custom_arrow_step<class_SpinBox_property_custom_arrow_step>` when interacting with the arrow buttons. Otherwise, increments the value by `custom_arrow_step<class_SpinBox_property_custom_arrow_step>` and then rounds it according to `Range.step<class_Range_property_step>`.

classref-item-separator

classref-property

`float<class_float>` **custom_arrow_step** = `0.0` `🔗<class_SpinBox_property_custom_arrow_step>`

classref-property-setget

- `void (No return value.)` **set_custom_arrow_step**(value: `float<class_float>`)
- `float<class_float>` **get_custom_arrow_step**()

If not `0`, sets the step when interacting with the arrow buttons of the **SpinBox**.

**Note:** `Range.value<class_Range_property_value>` will still be rounded to a multiple of `Range.step<class_Range_property_step>`.

classref-item-separator

classref-property

`bool<class_bool>` **editable** = `true` `🔗<class_SpinBox_property_editable>`

classref-property-setget

- `void (No return value.)` **set_editable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editable**()

If `true`, the **SpinBox** will be editable. Otherwise, it will be read only.

classref-item-separator

classref-property

`String<class_String>` **prefix** = `""` `🔗<class_SpinBox_property_prefix>`

classref-property-setget

- `void (No return value.)` **set_prefix**(value: `String<class_String>`)
- `String<class_String>` **get_prefix**()

Adds the specified prefix string before the numerical value of the **SpinBox**.

classref-item-separator

classref-property

`bool<class_bool>` **select_all_on_focus** = `false` `🔗<class_SpinBox_property_select_all_on_focus>`

classref-property-setget

- `void (No return value.)` **set_select_all_on_focus**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_select_all_on_focus**()

If `true`, the **SpinBox** will select the whole text when the `LineEdit<class_LineEdit>` gains focus. Clicking the up and down arrows won't trigger this behavior.

classref-item-separator

classref-property

`String<class_String>` **suffix** = `""` `🔗<class_SpinBox_property_suffix>`

classref-property-setget

- `void (No return value.)` **set_suffix**(value: `String<class_String>`)
- `String<class_String>` **get_suffix**()

Adds the specified suffix string after the numerical value of the **SpinBox**.

classref-item-separator

classref-property

`bool<class_bool>` **update_on_text_changed** = `false` `🔗<class_SpinBox_property_update_on_text_changed>`

classref-property-setget

- `void (No return value.)` **set_update_on_text_changed**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_update_on_text_changed**()

Sets the value of the `Range<class_Range>` for this **SpinBox** when the `LineEdit<class_LineEdit>` text is *changed* instead of *submitted*. See `LineEdit.text_changed<class_LineEdit_signal_text_changed>` and `LineEdit.text_submitted<class_LineEdit_signal_text_submitted>`.

**Note:** If set to `true`, this will interfere with entering mathematical expressions in the **SpinBox**. The **SpinBox** will try to evaluate the expression as you type, which means symbols like a trailing `+` are removed immediately by the expression being evaluated.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **apply**() `🔗<class_SpinBox_method_apply>`

Applies the current value of this **SpinBox**. This is equivalent to pressing `Enter` while editing the `LineEdit<class_LineEdit>` used by the **SpinBox**. This will cause `LineEdit.text_submitted<class_LineEdit_signal_text_submitted>` to be emitted and its currently contained expression to be evaluated.

classref-item-separator

classref-method

`LineEdit<class_LineEdit>` **get_line_edit**() `🔗<class_SpinBox_method_get_line_edit>`

Returns the `LineEdit<class_LineEdit>` instance from this **SpinBox**. You can use it to access properties and methods of `LineEdit<class_LineEdit>`.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `CanvasItem.visible<class_CanvasItem_property_visible>` property.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **down_disabled_icon_modulate** = `Color(0.875, 0.875, 0.875, 0.5)` `🔗<class_SpinBox_theme_color_down_disabled_icon_modulate>`

Down button icon modulation color, when the button is disabled.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **down_hover_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_SpinBox_theme_color_down_hover_icon_modulate>`

Down button icon modulation color, when the button is hovered.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **down_icon_modulate** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_SpinBox_theme_color_down_icon_modulate>`

Down button icon modulation color.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **down_pressed_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_SpinBox_theme_color_down_pressed_icon_modulate>`

Down button icon modulation color, when the button is being pressed.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **up_disabled_icon_modulate** = `Color(0.875, 0.875, 0.875, 0.5)` `🔗<class_SpinBox_theme_color_up_disabled_icon_modulate>`

Up button icon modulation color, when the button is disabled.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **up_hover_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_SpinBox_theme_color_up_hover_icon_modulate>`

Up button icon modulation color, when the button is hovered.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **up_icon_modulate** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_SpinBox_theme_color_up_icon_modulate>`

Up button icon modulation color.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **up_pressed_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_SpinBox_theme_color_up_pressed_icon_modulate>`

Up button icon modulation color, when the button is being pressed.

classref-item-separator

classref-themeproperty

`int<class_int>` **buttons_vertical_separation** = `0` `🔗<class_SpinBox_theme_constant_buttons_vertical_separation>`

Vertical separation between the up and down buttons.

classref-item-separator

classref-themeproperty

`int<class_int>` **buttons_width** = `16` `🔗<class_SpinBox_theme_constant_buttons_width>`

Width of the up and down buttons. If smaller than any icon set on the buttons, the respective icon may overlap neighboring elements. If smaller than `0`, the width is automatically adjusted from the icon size.

classref-item-separator

classref-themeproperty

`int<class_int>` **field_and_buttons_separation** = `2` `🔗<class_SpinBox_theme_constant_field_and_buttons_separation>`

Width of the horizontal separation between the text input field (`LineEdit<class_LineEdit>`) and the buttons.

classref-item-separator

classref-themeproperty

`int<class_int>` **set_min_buttons_width_from_icons** = `1` `🔗<class_SpinBox_theme_constant_set_min_buttons_width_from_icons>`

If not `0`, the minimum button width corresponds to the widest of all icons set on those buttons, even if `buttons_width<class_SpinBox_theme_constant_buttons_width>` is smaller.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **down** `🔗<class_SpinBox_theme_icon_down>`

Down button icon, displayed in the middle of the down (value-decreasing) button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **down_disabled** `🔗<class_SpinBox_theme_icon_down_disabled>`

Down button icon when the button is disabled.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **down_hover** `🔗<class_SpinBox_theme_icon_down_hover>`

Down button icon when the button is hovered.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **down_pressed** `🔗<class_SpinBox_theme_icon_down_pressed>`

Down button icon when the button is being pressed.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **up** `🔗<class_SpinBox_theme_icon_up>`

Up button icon, displayed in the middle of the up (value-increasing) button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **up_disabled** `🔗<class_SpinBox_theme_icon_up_disabled>`

Up button icon when the button is disabled.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **up_hover** `🔗<class_SpinBox_theme_icon_up_hover>`

Up button icon when the button is hovered.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **up_pressed** `🔗<class_SpinBox_theme_icon_up_pressed>`

Up button icon when the button is being pressed.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **updown** `🔗<class_SpinBox_theme_icon_updown>`

Single texture representing both the up and down buttons icons. It is displayed in the middle of the buttons and does not change upon interaction. If a valid icon is assigned, it will replace `up<class_SpinBox_theme_icon_up>` and `down<class_SpinBox_theme_icon_down>`.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **down_background** `🔗<class_SpinBox_theme_style_down_background>`

Background style of the down button.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **down_background_disabled** `🔗<class_SpinBox_theme_style_down_background_disabled>`

Background style of the down button when disabled.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **down_background_hovered** `🔗<class_SpinBox_theme_style_down_background_hovered>`

Background style of the down button when hovered.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **down_background_pressed** `🔗<class_SpinBox_theme_style_down_background_pressed>`

Background style of the down button when being pressed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **field_and_buttons_separator** `🔗<class_SpinBox_theme_style_field_and_buttons_separator>`

`StyleBox<class_StyleBox>` drawn in the space occupied by the separation between the input field and the buttons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **up_background** `🔗<class_SpinBox_theme_style_up_background>`

Background style of the up button.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **up_background_disabled** `🔗<class_SpinBox_theme_style_up_background_disabled>`

Background style of the up button when disabled.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **up_background_hovered** `🔗<class_SpinBox_theme_style_up_background_hovered>`

Background style of the up button when hovered.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **up_background_pressed** `🔗<class_SpinBox_theme_style_up_background_pressed>`

Background style of the up button when being pressed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **up_down_buttons_separator** `🔗<class_SpinBox_theme_style_up_down_buttons_separator>`

`StyleBox<class_StyleBox>` drawn in the space occupied by the separation between the up and down buttons.