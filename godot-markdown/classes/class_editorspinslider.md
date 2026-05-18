github_url
hide

# EditorSpinSlider

**Inherits:** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Godot editor's control for editing numeric values.

classref-introduction-group

## Description

This `Control<class_Control>` node is used in the editor's Inspector dock to allow editing of numeric values. Can be used with `EditorInspectorPlugin<class_EditorInspectorPlugin>` to recreate the same behavior.

If the `Range.step<class_Range_property_step>` value is `1`, the **EditorSpinSlider** will display up/down arrows, similar to `SpinBox<class_SpinBox>`. If the `Range.step<class_Range_property_step>` value is not `1`, a slider will be displayed instead.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**grabbed**() `🔗<class_EditorSpinSlider_signal_grabbed>`

Emitted when the spinner/slider is grabbed.

classref-item-separator

classref-signal

**ungrabbed**() `🔗<class_EditorSpinSlider_signal_ungrabbed>`

Emitted when the spinner/slider is ungrabbed.

classref-item-separator

classref-signal

**updown_pressed**() `🔗<class_EditorSpinSlider_signal_updown_pressed>`

Emitted when the updown button is pressed.

classref-item-separator

classref-signal

**value_focus_entered**() `🔗<class_EditorSpinSlider_signal_value_focus_entered>`

Emitted when the value form gains focus.

classref-item-separator

classref-signal

**value_focus_exited**() `🔗<class_EditorSpinSlider_signal_value_focus_exited>`

Emitted when the value form loses focus.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ControlState**: `🔗<enum_EditorSpinSlider_ControlState>`

classref-enumeration-constant

`ControlState<enum_EditorSpinSlider_ControlState>` **CONTROL_STATE_DEFAULT** = `0`

The type of control used will depend on the value of `editing_integer<class_EditorSpinSlider_property_editing_integer>`. Up-down arrows if `true`, a slider if `false`.

classref-enumeration-constant

`ControlState<enum_EditorSpinSlider_ControlState>` **CONTROL_STATE_PREFER_SLIDER** = `1`

A slider will always be used, even if `editing_integer<class_EditorSpinSlider_property_editing_integer>` is enabled.

classref-enumeration-constant

`ControlState<enum_EditorSpinSlider_ControlState>` **CONTROL_STATE_HIDE** = `2`

Neither the up-down arrows nor the slider will be shown.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`ControlState<enum_EditorSpinSlider_ControlState>` **control_state** = `0` `🔗<class_EditorSpinSlider_property_control_state>`

classref-property-setget

- `void (No return value.)` **set_control_state**(value: `ControlState<enum_EditorSpinSlider_ControlState>`)
- `ControlState<enum_EditorSpinSlider_ControlState>` **get_control_state**()

The state in which the control used to manipulate the value will be.

classref-item-separator

classref-property

`bool<class_bool>` **deferred_drag_mode** = `false` `🔗<class_EditorSpinSlider_property_deferred_drag_mode>`

classref-property-setget

- `void (No return value.)` **set_deferred_drag_mode_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_deferred_drag_mode_enabled**()

If `true`, changing via dragging is applied only at the end of the input (for example, when the user releases a mouse button).

classref-item-separator

classref-property

`bool<class_bool>` **editing_integer** = `false` `🔗<class_EditorSpinSlider_property_editing_integer>`

classref-property-setget

- `void (No return value.)` **set_editing_integer**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editing_integer**()

If `true`, the **EditorSpinSlider** is considered to be editing an integer value. If `false`, the **EditorSpinSlider** is considered to be editing a floating-point value. This is used to determine whether a slider should be drawn by default. The slider is only drawn for floats; integers use up-down arrows similar to `SpinBox<class_SpinBox>` instead, unless `control_state<class_EditorSpinSlider_property_control_state>` is set to `CONTROL_STATE_PREFER_SLIDER<class_EditorSpinSlider_constant_CONTROL_STATE_PREFER_SLIDER>`. It will also use `EditorSettings.interface/inspector/integer_drag_speed<class_EditorSettings_property_interface/inspector/integer_drag_speed>` instead of `EditorSettings.interface/inspector/float_drag_speed<class_EditorSettings_property_interface/inspector/float_drag_speed>` if the slider is available.

classref-item-separator

classref-property

`bool<class_bool>` **flat** = `false` `🔗<class_EditorSpinSlider_property_flat>`

classref-property-setget

- `void (No return value.)` **set_flat**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_flat**()

If `true`, the slider will not draw background.

classref-item-separator

classref-property

`bool<class_bool>` **hide_slider** = `false` `🔗<class_EditorSpinSlider_property_hide_slider>`

classref-property-setget

- `void (No return value.)` **set_hide_slider**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_hiding_slider**()

**Deprecated:** Use `control_state<class_EditorSpinSlider_property_control_state>` instead.

If `true`, the slider and up/down arrows are hidden.

classref-item-separator

classref-property

`String<class_String>` **label** = `""` `🔗<class_EditorSpinSlider_property_label>`

classref-property-setget

- `void (No return value.)` **set_label**(value: `String<class_String>`)
- `String<class_String>` **get_label**()

The text that displays to the left of the value.

classref-item-separator

classref-property

`bool<class_bool>` **read_only** = `false` `🔗<class_EditorSpinSlider_property_read_only>`

classref-property-setget

- `void (No return value.)` **set_read_only**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_read_only**()

If `true`, the slider can't be interacted with.

classref-item-separator

classref-property

`String<class_String>` **suffix** = `""` `🔗<class_EditorSpinSlider_property_suffix>`

classref-property-setget

- `void (No return value.)` **set_suffix**(value: `String<class_String>`)
- `String<class_String>` **get_suffix**()

The suffix to display after the value (in a faded color). This should generally be a plural word. You may have to use an abbreviation if the suffix is too long to be displayed.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Texture2D<class_Texture2D>` **updown** `🔗<class_EditorSpinSlider_theme_icon_updown>`

Single texture representing both the up and down buttons.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **updown_disabled** `🔗<class_EditorSpinSlider_theme_icon_updown_disabled>`

Single texture representing both the up and down buttons, when the control is readonly or disabled.