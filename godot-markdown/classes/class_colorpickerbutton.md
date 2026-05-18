github_url
hide

# ColorPickerButton

**Inherits:** `Button<class_Button>` **\<** `BaseButton<class_BaseButton>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A button that brings up a `ColorPicker<class_ColorPicker>` when pressed.

classref-introduction-group

## Description

Encapsulates a `ColorPicker<class_ColorPicker>`, making it accessible by pressing a button. Pressing the button will toggle the `ColorPicker<class_ColorPicker>`'s visibility.

See also `BaseButton<class_BaseButton>` which contains common properties and methods associated with this node.

**Note:** By default, the button may not be wide enough for the color preview swatch to be visible. Make sure to set `Control.custom_minimum_size<class_Control_property_custom_minimum_size>` to a big enough value to give the button enough space.

classref-introduction-group

## Tutorials

- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [GUI Drag And Drop Demo](https://godotengine.org/asset-library/asset/2767)

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

**color_changed**(color: `Color<class_Color>`) `🔗<class_ColorPickerButton_signal_color_changed>`

Emitted when the color changes.

classref-item-separator

classref-signal

**picker_created**() `🔗<class_ColorPickerButton_signal_picker_created>`

Emitted when the `ColorPicker<class_ColorPicker>` is created (the button is pressed for the first time).

classref-item-separator

classref-signal

**popup_closed**() `🔗<class_ColorPickerButton_signal_popup_closed>`

Emitted when the `ColorPicker<class_ColorPicker>` is closed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **color** = `Color(0, 0, 0, 1)` `🔗<class_ColorPickerButton_property_color>`

classref-property-setget

- `void (No return value.)` **set_pick_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_pick_color**()

The currently selected color.

classref-item-separator

classref-property

`bool<class_bool>` **edit_alpha** = `true` `🔗<class_ColorPickerButton_property_edit_alpha>`

classref-property-setget

- `void (No return value.)` **set_edit_alpha**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editing_alpha**()

If `true`, the alpha channel in the displayed `ColorPicker<class_ColorPicker>` will be visible.

classref-item-separator

classref-property

`bool<class_bool>` **edit_intensity** = `true` `🔗<class_ColorPickerButton_property_edit_intensity>`

classref-property-setget

- `void (No return value.)` **set_edit_intensity**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editing_intensity**()

If `true`, the intensity slider in the displayed `ColorPicker<class_ColorPicker>` will be visible.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`ColorPicker<class_ColorPicker>` **get_picker**() `🔗<class_ColorPickerButton_method_get_picker>`

Returns the `ColorPicker<class_ColorPicker>` that this node toggles.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `CanvasItem.visible<class_CanvasItem_property_visible>` property.

classref-item-separator

classref-method

`PopupPanel<class_PopupPanel>` **get_popup**() `🔗<class_ColorPickerButton_method_get_popup>`

Returns the control's `PopupPanel<class_PopupPanel>` which allows you to connect to popup signals. This allows you to handle events when the ColorPicker is shown or hidden.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `Window.visible<class_Window_property_visible>` property.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Texture2D<class_Texture2D>` **bg** `🔗<class_ColorPickerButton_theme_icon_bg>`

The background of the color preview rect on the button.