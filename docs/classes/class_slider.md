github_url
hide

# Slider

**Inherits:** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `HSlider<class_HSlider>`, `VSlider<class_VSlider>`

Abstract base class for sliders.

classref-introduction-group

## Description

Abstract base class for sliders, used to adjust a value by moving a grabber along a horizontal or vertical axis. Sliders are `Range<class_Range>`-based controls.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**drag_ended**(value_changed: `bool<class_bool>`) `🔗<class_Slider_signal_drag_ended>`

Emitted when the grabber stops being dragged. If `value_changed` is `true`, `Range.value<class_Range_property_value>` is different from the value when the dragging was started.

classref-item-separator

classref-signal

**drag_started**() `🔗<class_Slider_signal_drag_started>`

Emitted when the grabber starts being dragged. This is emitted before the corresponding `Range.value_changed<class_Range_signal_value_changed>` signal.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **TickPosition**: `🔗<enum_Slider_TickPosition>`

classref-enumeration-constant

`TickPosition<enum_Slider_TickPosition>` **TICK_POSITION_BOTTOM_RIGHT** = `0`

Places the ticks at the bottom of the `HSlider<class_HSlider>`, or right of the `VSlider<class_VSlider>`.

classref-enumeration-constant

`TickPosition<enum_Slider_TickPosition>` **TICK_POSITION_TOP_LEFT** = `1`

Places the ticks at the top of the `HSlider<class_HSlider>`, or left of the `VSlider<class_VSlider>`.

classref-enumeration-constant

`TickPosition<enum_Slider_TickPosition>` **TICK_POSITION_BOTH** = `2`

Places the ticks at the both sides of the slider.

classref-enumeration-constant

`TickPosition<enum_Slider_TickPosition>` **TICK_POSITION_CENTER** = `3`

Places the ticks at the center of the slider.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **editable** = `true` `🔗<class_Slider_property_editable>`

classref-property-setget

- `void (No return value.)` **set_editable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editable**()

If `true`, the slider can be interacted with. If `false`, the value can be changed only by code.

classref-item-separator

classref-property

`bool<class_bool>` **scrollable** = `true` `🔗<class_Slider_property_scrollable>`

classref-property-setget

- `void (No return value.)` **set_scrollable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_scrollable**()

If `true`, the value can be changed using the mouse wheel.

classref-item-separator

classref-property

`int<class_int>` **tick_count** = `0` `🔗<class_Slider_property_tick_count>`

classref-property-setget

- `void (No return value.)` **set_ticks**(value: `int<class_int>`)
- `int<class_int>` **get_ticks**()

Number of ticks displayed on the slider, including border ticks. Ticks are uniformly-distributed value markers.

classref-item-separator

classref-property

`bool<class_bool>` **ticks_on_borders** = `false` `🔗<class_Slider_property_ticks_on_borders>`

classref-property-setget

- `void (No return value.)` **set_ticks_on_borders**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_ticks_on_borders**()

If `true`, the slider will display ticks for minimum and maximum values.

classref-item-separator

classref-property

`TickPosition<enum_Slider_TickPosition>` **ticks_position** = `0` `🔗<class_Slider_property_ticks_position>`

classref-property-setget

- `void (No return value.)` **set_ticks_position**(value: `TickPosition<enum_Slider_TickPosition>`)
- `TickPosition<enum_Slider_TickPosition>` **get_ticks_position**()

Sets the position of the ticks. See `TickPosition<enum_Slider_TickPosition>` for details.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`int<class_int>` **center_grabber** = `0` `🔗<class_Slider_theme_constant_center_grabber>`

Boolean constant. If `1`, the grabber texture size will be ignored and it will fit within slider's bounds based only on its center position.

classref-item-separator

classref-themeproperty

`int<class_int>` **grabber_offset** = `0` `🔗<class_Slider_theme_constant_grabber_offset>`

Vertical or horizontal offset of the grabber.

classref-item-separator

classref-themeproperty

`int<class_int>` **tick_offset** = `0` `🔗<class_Slider_theme_constant_tick_offset>`

Vertical or horizontal offset of the ticks. The offset is reversed for top or left ticks.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **grabber** `🔗<class_Slider_theme_icon_grabber>`

The texture for the grabber (the draggable element).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **grabber_disabled** `🔗<class_Slider_theme_icon_grabber_disabled>`

The texture for the grabber when it's disabled.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **grabber_highlight** `🔗<class_Slider_theme_icon_grabber_highlight>`

The texture for the grabber when it's focused.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **tick** `🔗<class_Slider_theme_icon_tick>`

The texture for the ticks, visible when `tick_count<class_Slider_property_tick_count>` is greater than 0.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **grabber_area** `🔗<class_Slider_theme_style_grabber_area>`

The background of the area to the left or bottom of the grabber.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **grabber_area_highlight** `🔗<class_Slider_theme_style_grabber_area_highlight>`

The background of the area to the left or bottom of the grabber that displays when it's being hovered or focused.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **slider** `🔗<class_Slider_theme_style_slider>`

The background for the whole slider. Affects the height or width of the `grabber_area<class_Slider_theme_style_grabber_area>`.