github_url
hide

# ColorPicker

**Inherits:** `VBoxContainer<class_VBoxContainer>` **\<** `BoxContainer<class_BoxContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A widget that provides an interface for selecting or modifying a color.

classref-introduction-group

## Description

A widget that provides an interface for selecting or modifying a color. It can optionally provide functionalities like a color sampler (eyedropper), color modes, and presets.

**Note:** This control is the color picker widget itself. You can use a `ColorPickerButton<class_ColorPickerButton>` instead if you need a button that brings up a **ColorPicker** in a popup.

classref-introduction-group

## Tutorials

- [Tween Interpolation Demo](https://godotengine.org/asset-library/asset/2733)

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

**color_changed**(color: `Color<class_Color>`) `🔗<class_ColorPicker_signal_color_changed>`

Emitted when the color is changed.

classref-item-separator

classref-signal

**preset_added**(color: `Color<class_Color>`) `🔗<class_ColorPicker_signal_preset_added>`

Emitted when a preset is added.

classref-item-separator

classref-signal

**preset_removed**(color: `Color<class_Color>`) `🔗<class_ColorPicker_signal_preset_removed>`

Emitted when a preset is removed.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ColorModeType**: `🔗<enum_ColorPicker_ColorModeType>`

classref-enumeration-constant

`ColorModeType<enum_ColorPicker_ColorModeType>` **MODE_RGB** = `0`

Allows editing the color with Red/Green/Blue sliders in sRGB color space.

classref-enumeration-constant

`ColorModeType<enum_ColorPicker_ColorModeType>` **MODE_HSV** = `1`

Allows editing the color with Hue/Saturation/Value sliders.

classref-enumeration-constant

`ColorModeType<enum_ColorPicker_ColorModeType>` **MODE_RAW** = `2`

**Deprecated:** This is replaced by `MODE_LINEAR<class_ColorPicker_constant_MODE_LINEAR>`.

classref-enumeration-constant

`ColorModeType<enum_ColorPicker_ColorModeType>` **MODE_LINEAR** = `2`

Allows editing the color with Red/Green/Blue sliders in linear color space.

classref-enumeration-constant

`ColorModeType<enum_ColorPicker_ColorModeType>` **MODE_OKHSL** = `3`

Allows editing the color with Hue/Saturation/Lightness sliders.

OKHSL is a new color space similar to HSL but that better match perception by leveraging the Oklab color space which is designed to be simple to use, while doing a good job at predicting perceived lightness, chroma and hue.

[Okhsv and Okhsl color spaces](https://bottosson.github.io/posts/colorpicker/)

classref-item-separator

classref-enumeration

enum **PickerShapeType**: `🔗<enum_ColorPicker_PickerShapeType>`

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_HSV_RECTANGLE** = `0`

HSV Color Model rectangle color space.

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_HSV_WHEEL** = `1`

HSV Color Model rectangle color space with a wheel.

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_VHS_CIRCLE** = `2`

HSV Color Model circle color space. Use Saturation as a radius.

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_OKHSL_CIRCLE** = `3`

HSL OK Color Model circle color space.

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_NONE** = `4`

The color space shape and the shape select button are hidden. Can't be selected from the shapes popup.

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_OK_HS_RECTANGLE** = `5`

OKHSL Color Model rectangle with constant lightness.

classref-enumeration-constant

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **SHAPE_OK_HL_RECTANGLE** = `6`

OKHSL Color Model rectangle with constant saturation.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **can_add_swatches** = `true` `🔗<class_ColorPicker_property_can_add_swatches>`

classref-property-setget

- `void (No return value.)` **set_can_add_swatches**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_swatches_enabled**()

If `true`, it's possible to add presets under Swatches. If `false`, the button to add presets is disabled.

classref-item-separator

classref-property

`Color<class_Color>` **color** = `Color(1, 1, 1, 1)` `🔗<class_ColorPicker_property_color>`

classref-property-setget

- `void (No return value.)` **set_pick_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_pick_color**()

The currently selected color.

classref-item-separator

classref-property

`ColorModeType<enum_ColorPicker_ColorModeType>` **color_mode** = `0` `🔗<class_ColorPicker_property_color_mode>`

classref-property-setget

- `void (No return value.)` **set_color_mode**(value: `ColorModeType<enum_ColorPicker_ColorModeType>`)
- `ColorModeType<enum_ColorPicker_ColorModeType>` **get_color_mode**()

The currently selected color mode.

classref-item-separator

classref-property

`bool<class_bool>` **color_modes_visible** = `true` `🔗<class_ColorPicker_property_color_modes_visible>`

classref-property-setget

- `void (No return value.)` **set_modes_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_modes_visible**()

If `true`, the color mode buttons are visible.

classref-item-separator

classref-property

`bool<class_bool>` **deferred_mode** = `false` `🔗<class_ColorPicker_property_deferred_mode>`

classref-property-setget

- `void (No return value.)` **set_deferred_mode**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_deferred_mode**()

If `true`, the color will apply only after the user releases the mouse button, otherwise it will apply immediately even in mouse motion event (which can cause performance issues).

classref-item-separator

classref-property

`bool<class_bool>` **edit_alpha** = `true` `🔗<class_ColorPicker_property_edit_alpha>`

classref-property-setget

- `void (No return value.)` **set_edit_alpha**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editing_alpha**()

If `true`, shows an alpha channel slider (opacity).

classref-item-separator

classref-property

`bool<class_bool>` **edit_intensity** = `true` `🔗<class_ColorPicker_property_edit_intensity>`

classref-property-setget

- `void (No return value.)` **set_edit_intensity**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editing_intensity**()

If `true`, shows an intensity slider. The intensity is applied as follows: convert the color to linear encoding, multiply it by `2 ** intensity`, and then convert it back to nonlinear sRGB encoding.

classref-item-separator

classref-property

`bool<class_bool>` **hex_visible** = `true` `🔗<class_ColorPicker_property_hex_visible>`

classref-property-setget

- `void (No return value.)` **set_hex_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_hex_visible**()

If `true`, the hex color code input field is visible.

classref-item-separator

classref-property

`PickerShapeType<enum_ColorPicker_PickerShapeType>` **picker_shape** = `0` `🔗<class_ColorPicker_property_picker_shape>`

classref-property-setget

- `void (No return value.)` **set_picker_shape**(value: `PickerShapeType<enum_ColorPicker_PickerShapeType>`)
- `PickerShapeType<enum_ColorPicker_PickerShapeType>` **get_picker_shape**()

The shape of the color space view.

classref-item-separator

classref-property

`bool<class_bool>` **presets_visible** = `true` `🔗<class_ColorPicker_property_presets_visible>`

classref-property-setget

- `void (No return value.)` **set_presets_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_presets_visible**()

If `true`, the Swatches and Recent Colors presets are visible.

classref-item-separator

classref-property

`bool<class_bool>` **sampler_visible** = `true` `🔗<class_ColorPicker_property_sampler_visible>`

classref-property-setget

- `void (No return value.)` **set_sampler_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_sampler_visible**()

If `true`, the color sampler and color preview are visible.

classref-item-separator

classref-property

`bool<class_bool>` **sliders_visible** = `true` `🔗<class_ColorPicker_property_sliders_visible>`

classref-property-setget

- `void (No return value.)` **set_sliders_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_sliders_visible**()

If `true`, the color sliders are visible.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_preset**(color: `Color<class_Color>`) `🔗<class_ColorPicker_method_add_preset>`

Adds the given color to a list of color presets. The presets are displayed in the color picker and the user will be able to select them.

**Note:** The presets list is only for *this* color picker.

classref-item-separator

classref-method

`void (No return value.)` **add_recent_preset**(color: `Color<class_Color>`) `🔗<class_ColorPicker_method_add_recent_preset>`

Adds the given color to a list of color recent presets so that it can be picked later. Recent presets are the colors that were picked recently, a new preset is automatically created and added to recent presets when you pick a new color.

**Note:** The recent presets list is only for *this* color picker.

classref-item-separator

classref-method

`void (No return value.)` **erase_preset**(color: `Color<class_Color>`) `🔗<class_ColorPicker_method_erase_preset>`

Removes the given color from the list of color presets of this color picker.

classref-item-separator

classref-method

`void (No return value.)` **erase_recent_preset**(color: `Color<class_Color>`) `🔗<class_ColorPicker_method_erase_recent_preset>`

Removes the given color from the list of color recent presets of this color picker.

classref-item-separator

classref-method

`PackedColorArray<class_PackedColorArray>` **get_presets**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ColorPicker_method_get_presets>`

Returns the list of colors in the presets of the color picker.

classref-item-separator

classref-method

`PackedColorArray<class_PackedColorArray>` **get_recent_presets**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ColorPicker_method_get_recent_presets>`

Returns the list of colors in the recent presets of the color picker.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **focused_not_editing_cursor_color** = `Color(1, 1, 1, 0.275)` `🔗<class_ColorPicker_theme_color_focused_not_editing_cursor_color>`

Color of rectangle or circle drawn when a picker shape part is focused but not editable via keyboard or joypad. Displayed *over* the picker shape, so a partially transparent color should be used to ensure the picker shape remains visible.

classref-item-separator

classref-themeproperty

`int<class_int>` **center_slider_grabbers** = `1` `🔗<class_ColorPicker_theme_constant_center_slider_grabbers>`

Overrides the `Slider.center_grabber<class_Slider_theme_constant_center_grabber>` theme property of the sliders.

classref-item-separator

classref-themeproperty

`int<class_int>` **h_width** = `30` `🔗<class_ColorPicker_theme_constant_h_width>`

The width of the hue selection slider.

classref-item-separator

classref-themeproperty

`int<class_int>` **label_width** = `10` `🔗<class_ColorPicker_theme_constant_label_width>`

The minimum width of the color labels next to sliders.

classref-item-separator

classref-themeproperty

`int<class_int>` **margin** = `4` `🔗<class_ColorPicker_theme_constant_margin>`

The margin around the **ColorPicker**.

classref-item-separator

classref-themeproperty

`int<class_int>` **sv_height** = `256` `🔗<class_ColorPicker_theme_constant_sv_height>`

The height of the saturation-value selection box.

classref-item-separator

classref-themeproperty

`int<class_int>` **sv_width** = `256` `🔗<class_ColorPicker_theme_constant_sv_width>`

The width of the saturation-value selection box.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **add_preset** `🔗<class_ColorPicker_theme_icon_add_preset>`

The icon for the "Add Preset" button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **bar_arrow** `🔗<class_ColorPicker_theme_icon_bar_arrow>`

The texture for the arrow grabber.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **color_copy** `🔗<class_ColorPicker_theme_icon_color_copy>`

The icon for the button that copies the color in text format to the clipboard.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **color_hue** `🔗<class_ColorPicker_theme_icon_color_hue>`

Custom texture for the hue selection slider on the right.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **color_script** `🔗<class_ColorPicker_theme_icon_color_script>`

The icon for the button that switches color text to hexadecimal.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **expanded_arrow** `🔗<class_ColorPicker_theme_icon_expanded_arrow>`

The icon for color preset drop down menu when expanded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **folded_arrow** `🔗<class_ColorPicker_theme_icon_folded_arrow>`

The icon for color preset drop down menu when folded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **menu_option** `🔗<class_ColorPicker_theme_icon_menu_option>`

The icon for color preset option menu.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **overbright_indicator** `🔗<class_ColorPicker_theme_icon_overbright_indicator>`

The indicator used to signalize that the color value is outside the 0-1 range.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **picker_cursor** `🔗<class_ColorPicker_theme_icon_picker_cursor>`

The image displayed over the color box/circle (depending on the `picker_shape<class_ColorPicker_property_picker_shape>`), marking the currently selected color.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **picker_cursor_bg** `🔗<class_ColorPicker_theme_icon_picker_cursor_bg>`

The fill image displayed behind the picker cursor.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **sample_bg** `🔗<class_ColorPicker_theme_icon_sample_bg>`

Background panel for the color preview box (visible when the color is translucent).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **sample_revert** `🔗<class_ColorPicker_theme_icon_sample_revert>`

The icon for the revert button (visible on the middle of the "old" color when it differs from the currently selected color). This icon is modulated with a dark color if the "old" color is bright enough, so the icon should be bright to ensure visibility in both scenarios.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **screen_picker** `🔗<class_ColorPicker_theme_icon_screen_picker>`

The icon for the screen color picker button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **shape_circle** `🔗<class_ColorPicker_theme_icon_shape_circle>`

The icon for circular picker shapes.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **shape_rect** `🔗<class_ColorPicker_theme_icon_shape_rect>`

The icon for rectangular picker shapes.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **shape_rect_wheel** `🔗<class_ColorPicker_theme_icon_shape_rect_wheel>`

The icon for rectangular wheel picker shapes.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **picker_focus_circle** `🔗<class_ColorPicker_theme_style_picker_focus_circle>`

The `StyleBox<class_StyleBox>` used when the circle-shaped part of the picker is focused. Displayed *over* the picker shape, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the picker shape remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **picker_focus_rectangle** `🔗<class_ColorPicker_theme_style_picker_focus_rectangle>`

The `StyleBox<class_StyleBox>` used when the rectangle-shaped part of the picker is focused. Displayed *over* the picker shape, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the picker shape remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **sample_focus** `🔗<class_ColorPicker_theme_style_sample_focus>`

The `StyleBox<class_StyleBox>` used for the old color sample part when it is focused. Displayed *over* the sample, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the picker shape remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.