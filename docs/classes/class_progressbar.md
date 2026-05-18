github_url
hide

# ProgressBar

**Inherits:** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A control used for visual representation of a percentage.

classref-introduction-group

## Description

A control used for visual representation of a percentage. Shows the fill percentage in the center. Can also be used to show indeterminate progress. For more fill modes, use `TextureProgressBar<class_TextureProgressBar>` instead.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FillMode**: `🔗<enum_ProgressBar_FillMode>`

classref-enumeration-constant

`FillMode<enum_ProgressBar_FillMode>` **FILL_BEGIN_TO_END** = `0`

The progress bar fills from begin to end horizontally, according to the language direction. If `Control.is_layout_rtl()<class_Control_method_is_layout_rtl>` returns `false`, it fills from left to right, and if it returns `true`, it fills from right to left.

classref-enumeration-constant

`FillMode<enum_ProgressBar_FillMode>` **FILL_END_TO_BEGIN** = `1`

The progress bar fills from end to begin horizontally, according to the language direction. If `Control.is_layout_rtl()<class_Control_method_is_layout_rtl>` returns `false`, it fills from right to left, and if it returns `true`, it fills from left to right.

classref-enumeration-constant

`FillMode<enum_ProgressBar_FillMode>` **FILL_TOP_TO_BOTTOM** = `2`

The progress fills from top to bottom.

classref-enumeration-constant

`FillMode<enum_ProgressBar_FillMode>` **FILL_BOTTOM_TO_TOP** = `3`

The progress fills from bottom to top.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **editor_preview_indeterminate** `🔗<class_ProgressBar_property_editor_preview_indeterminate>`

classref-property-setget

- `void (No return value.)` **set_editor_preview_indeterminate**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editor_preview_indeterminate_enabled**()

If `false`, the `indeterminate<class_ProgressBar_property_indeterminate>` animation will be paused in the editor.

classref-item-separator

classref-property

`int<class_int>` **fill_mode** = `0` `🔗<class_ProgressBar_property_fill_mode>`

classref-property-setget

- `void (No return value.)` **set_fill_mode**(value: `int<class_int>`)
- `int<class_int>` **get_fill_mode**()

The fill direction. See `FillMode<enum_ProgressBar_FillMode>` for possible values.

classref-item-separator

classref-property

`bool<class_bool>` **indeterminate** = `false` `🔗<class_ProgressBar_property_indeterminate>`

classref-property-setget

- `void (No return value.)` **set_indeterminate**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_indeterminate**()

When set to `true`, the progress bar indicates that something is happening with an animation, but does not show the fill percentage or value.

classref-item-separator

classref-property

`bool<class_bool>` **show_percentage** = `true` `🔗<class_ProgressBar_property_show_percentage>`

classref-property-setget

- `void (No return value.)` **set_show_percentage**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_percentage_shown**()

If `true`, the fill percentage is displayed on the bar.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **font_color** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_ProgressBar_theme_color_font_color>`

The color of the text.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_outline_color** = `Color(0, 0, 0, 1)` `🔗<class_ProgressBar_theme_color_font_outline_color>`

The tint of text outline of the **ProgressBar**.

classref-item-separator

classref-themeproperty

`int<class_int>` **outline_size** = `0` `🔗<class_ProgressBar_theme_constant_outline_size>`

The size of the text outline.

**Note:** If using a font with `FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>` enabled, its `FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the value of `outline_size<class_ProgressBar_theme_constant_outline_size>` for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **font** `🔗<class_ProgressBar_theme_font_font>`

Font used to draw the fill percentage if `show_percentage<class_ProgressBar_property_show_percentage>` is `true`.

classref-item-separator

classref-themeproperty

`int<class_int>` **font_size** `🔗<class_ProgressBar_theme_font_size_font_size>`

Font size used to draw the fill percentage if `show_percentage<class_ProgressBar_property_show_percentage>` is `true`.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **background** `🔗<class_ProgressBar_theme_style_background>`

The style of the background.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **fill** `🔗<class_ProgressBar_theme_style_fill>`

The style of the progress (i.e. the part that fills the bar).