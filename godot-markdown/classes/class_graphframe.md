github_url
hide

# GraphFrame

**Inherits:** `GraphElement<class_GraphElement>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

GraphFrame is a special `GraphElement<class_GraphElement>` that can be used to organize other `GraphElement<class_GraphElement>`s inside a `GraphEdit<class_GraphEdit>`.

classref-introduction-group

## Description

GraphFrame is a special `GraphElement<class_GraphElement>` to which other `GraphElement<class_GraphElement>`s can be attached. It can be configured to automatically resize to enclose all attached `GraphElement<class_GraphElement>`s. If the frame is moved, all the attached `GraphElement<class_GraphElement>`s inside it will be moved as well.

A GraphFrame is always kept behind the connection layer and other `GraphElement<class_GraphElement>`s inside a `GraphEdit<class_GraphEdit>`.

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

**autoshrink_changed**() `🔗<class_GraphFrame_signal_autoshrink_changed>`

Emitted when `autoshrink_enabled<class_GraphFrame_property_autoshrink_enabled>` or `autoshrink_margin<class_GraphFrame_property_autoshrink_margin>` changes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **autoshrink_enabled** = `true` `🔗<class_GraphFrame_property_autoshrink_enabled>`

classref-property-setget

- `void (No return value.)` **set_autoshrink_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_autoshrink_enabled**()

If `true`, the frame's rect will be adjusted automatically to enclose all attached `GraphElement<class_GraphElement>`s.

classref-item-separator

classref-property

`int<class_int>` **autoshrink_margin** = `40` `🔗<class_GraphFrame_property_autoshrink_margin>`

classref-property-setget

- `void (No return value.)` **set_autoshrink_margin**(value: `int<class_int>`)
- `int<class_int>` **get_autoshrink_margin**()

The margin around the attached nodes that is used to calculate the size of the frame when `autoshrink_enabled<class_GraphFrame_property_autoshrink_enabled>` is `true`.

classref-item-separator

classref-property

`int<class_int>` **drag_margin** = `16` `🔗<class_GraphFrame_property_drag_margin>`

classref-property-setget

- `void (No return value.)` **set_drag_margin**(value: `int<class_int>`)
- `int<class_int>` **get_drag_margin**()

The margin inside the frame that can be used to drag the frame.

classref-item-separator

classref-property

`Color<class_Color>` **tint_color** = `Color(0.3, 0.3, 0.3, 0.75)` `🔗<class_GraphFrame_property_tint_color>`

classref-property-setget

- `void (No return value.)` **set_tint_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_tint_color**()

The color of the frame when `tint_color_enabled<class_GraphFrame_property_tint_color_enabled>` is `true`.

classref-item-separator

classref-property

`bool<class_bool>` **tint_color_enabled** = `false` `🔗<class_GraphFrame_property_tint_color_enabled>`

classref-property-setget

- `void (No return value.)` **set_tint_color_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_tint_color_enabled**()

If `true`, the tint color will be used to tint the frame.

classref-item-separator

classref-property

`String<class_String>` **title** = `""` `🔗<class_GraphFrame_property_title>`

classref-property-setget

- `void (No return value.)` **set_title**(value: `String<class_String>`)
- `String<class_String>` **get_title**()

Title of the frame.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`HBoxContainer<class_HBoxContainer>` **get_titlebar_hbox**() `🔗<class_GraphFrame_method_get_titlebar_hbox>`

Returns the `HBoxContainer<class_HBoxContainer>` used for the title bar, only containing a `Label<class_Label>` for displaying the title by default.

This can be used to add custom controls to the title bar such as option or close buttons.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **resizer_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_GraphFrame_theme_color_resizer_color>`

The color modulation applied to the resizer icon.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel** `🔗<class_GraphFrame_theme_style_panel>`

The default `StyleBox<class_StyleBox>` used for the background of the **GraphFrame**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel_selected** `🔗<class_GraphFrame_theme_style_panel_selected>`

The `StyleBox<class_StyleBox>` used for the background of the **GraphFrame** when it is selected.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **titlebar** `🔗<class_GraphFrame_theme_style_titlebar>`

The `StyleBox<class_StyleBox>` used for the title bar of the **GraphFrame**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **titlebar_selected** `🔗<class_GraphFrame_theme_style_titlebar_selected>`

The `StyleBox<class_StyleBox>` used for the title bar of the **GraphFrame** when it is selected.