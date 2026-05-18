github_url
hide

# VirtualJoystick

**Inherits:** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A virtual joystick control for touchscreen devices.

classref-introduction-group

## Description

A customizable on-screen joystick control designed for touchscreen devices. It allows users to provide directional input by dragging a virtual tip within a defined circular area.

This control can simulate directional actions (see `action_up<class_VirtualJoystick_property_action_up>`, `action_down<class_VirtualJoystick_property_action_down>`, `action_left<class_VirtualJoystick_property_action_left>`, and `action_right<class_VirtualJoystick_property_action_right>`), which are triggered when the joystick is moved in the corresponding directions.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**flick_canceled**() `🔗<class_VirtualJoystick_signal_flick_canceled>`

Emitted when the tip enters the deadzone after being outside of it.

classref-item-separator

classref-signal

**flicked**(input_vector: `Vector2<class_Vector2>`) `🔗<class_VirtualJoystick_signal_flicked>`

Emitted when the tip moved outside the deadzone and the joystick is released. The `input_vector` contains the last input direction and strength before release. Its length is between `0.0` and `1.0`.

classref-item-separator

classref-signal

**pressed**() `🔗<class_VirtualJoystick_signal_pressed>`

Emitted when the joystick is pressed.

classref-item-separator

classref-signal

**released**(input_vector: `Vector2<class_Vector2>`) `🔗<class_VirtualJoystick_signal_released>`

Emitted when the joystick is released. The `input_vector` is the final input direction and strength, with a length between `0.0` and `1.0`.

classref-item-separator

classref-signal

**tapped**() `🔗<class_VirtualJoystick_signal_tapped>`

Emitted when the joystick is released without moving the tip.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **JoystickMode**: `🔗<enum_VirtualJoystick_JoystickMode>`

classref-enumeration-constant

`JoystickMode<enum_VirtualJoystick_JoystickMode>` **JOYSTICK_FIXED** = `0`

The joystick doesn't move.

classref-enumeration-constant

`JoystickMode<enum_VirtualJoystick_JoystickMode>` **JOYSTICK_DYNAMIC** = `1`

The joystick is moved to the initial touch position as long as it's within the joystick's bounds. It moves back to its original position when released.

classref-enumeration-constant

`JoystickMode<enum_VirtualJoystick_JoystickMode>` **JOYSTICK_FOLLOWING** = `2`

The joystick is moved to the initial touch position as long as it's within the joystick's bounds. It will follow the touch input if it goes outside the joystick's range. It moves back to its original position when released.

classref-item-separator

classref-enumeration

enum **VisibilityMode**: `🔗<enum_VirtualJoystick_VisibilityMode>`

classref-enumeration-constant

`VisibilityMode<enum_VirtualJoystick_VisibilityMode>` **VISIBILITY_ALWAYS** = `0`

The joystick is always visible.

classref-enumeration-constant

`VisibilityMode<enum_VirtualJoystick_VisibilityMode>` **VISIBILITY_WHEN_TOUCHED** = `1`

The joystick is only visible when being touched.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`StringName<class_StringName>` **action_down** = `&"ui_down"` `🔗<class_VirtualJoystick_property_action_down>`

classref-property-setget

- `void (No return value.)` **set_action_down**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_action_down**()

The action to trigger when the joystick is moved down.

classref-item-separator

classref-property

`StringName<class_StringName>` **action_left** = `&"ui_left"` `🔗<class_VirtualJoystick_property_action_left>`

classref-property-setget

- `void (No return value.)` **set_action_left**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_action_left**()

The action to trigger when the joystick is moved left.

classref-item-separator

classref-property

`StringName<class_StringName>` **action_right** = `&"ui_right"` `🔗<class_VirtualJoystick_property_action_right>`

classref-property-setget

- `void (No return value.)` **set_action_right**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_action_right**()

The action to trigger when the joystick is moved right.

classref-item-separator

classref-property

`StringName<class_StringName>` **action_up** = `&"ui_up"` `🔗<class_VirtualJoystick_property_action_up>`

classref-property-setget

- `void (No return value.)` **set_action_up**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_action_up**()

The action to trigger when the joystick is moved up.

classref-item-separator

classref-property

`float<class_float>` **clampzone_ratio** = `1.0` `🔗<class_VirtualJoystick_property_clampzone_ratio>`

classref-property-setget

- `void (No return value.)` **set_clampzone_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_clampzone_ratio**()

The multiplier applied to the joystick's radius that defines the clamp zone.

This zone limits how far the joystick tip can move from its center before being clamped.

A value of `1.0` means the tip can move up to the edge of the joystick's visual size.

In `JOYSTICK_FOLLOWING<class_VirtualJoystick_constant_JOYSTICK_FOLLOWING>` mode, this radius also determines how far the finger can move before the joystick base starts following the touch input.

classref-item-separator

classref-property

`float<class_float>` **deadzone_ratio** = `0.0` `🔗<class_VirtualJoystick_property_deadzone_ratio>`

classref-property-setget

- `void (No return value.)` **set_deadzone_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_deadzone_ratio**()

The ratio of the joystick size that defines the joystick deadzone. The joystick tip must move beyond this ratio before being considered active.

This deadzone is applied before triggering input actions and affects the joystick's input vector and all related signals.

Note that input actions may also define their own deadzones in the InputMap. If both are set, the joystick deadzone is applied first, followed by the action's deadzone.

By default, this value is `0.0`, meaning the joystick does not apply its own deadzone and relies entirely on the InputMap action deadzones.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **initial_offset_ratio** = `Vector2(0.5, 0.5)` `🔗<class_VirtualJoystick_property_initial_offset_ratio>`

classref-property-setget

- `void (No return value.)` **set_initial_offset_ratio**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_initial_offset_ratio**()

The initial position of the joystick as a ratio of the control's size. `(0, 0)` is top-left and `(1, 1)` is bottom-right.

classref-item-separator

classref-property

`JoystickMode<enum_VirtualJoystick_JoystickMode>` **joystick_mode** = `0` `🔗<class_VirtualJoystick_property_joystick_mode>`

classref-property-setget

- `void (No return value.)` **set_joystick_mode**(value: `JoystickMode<enum_VirtualJoystick_JoystickMode>`)
- `JoystickMode<enum_VirtualJoystick_JoystickMode>` **get_joystick_mode**()

The joystick mode to use.

classref-item-separator

classref-property

`float<class_float>` **joystick_size** = `100.0` `🔗<class_VirtualJoystick_property_joystick_size>`

classref-property-setget

- `void (No return value.)` **set_joystick_size**(value: `float<class_float>`)
- `float<class_float>` **get_joystick_size**()

The size of the joystick in pixels.

classref-item-separator

classref-property

`float<class_float>` **tip_size** = `50.0` `🔗<class_VirtualJoystick_property_tip_size>`

classref-property-setget

- `void (No return value.)` **set_tip_size**(value: `float<class_float>`)
- `float<class_float>` **get_tip_size**()

The size of the joystick tip in pixels.

classref-item-separator

classref-property

`VisibilityMode<enum_VirtualJoystick_VisibilityMode>` **visibility_mode** = `0` `🔗<class_VirtualJoystick_property_visibility_mode>`

classref-property-setget

- `void (No return value.)` **set_visibility_mode**(value: `VisibilityMode<enum_VirtualJoystick_VisibilityMode>`)
- `VisibilityMode<enum_VirtualJoystick_VisibilityMode>` **get_visibility_mode**()

The visibility mode to use.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`StyleBox<class_StyleBox>` **normal_joystick** `🔗<class_VirtualJoystick_theme_style_normal_joystick>`

Base joystick `StyleBox<class_StyleBox>`.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **normal_tip** `🔗<class_VirtualJoystick_theme_style_normal_tip>`

Tip joystick `StyleBox<class_StyleBox>`.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **pressed_joystick** `🔗<class_VirtualJoystick_theme_style_pressed_joystick>`

Base joystick `StyleBox<class_StyleBox>` when pressed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **pressed_tip** `🔗<class_VirtualJoystick_theme_style_pressed_tip>`

Tip joystick `StyleBox<class_StyleBox>` when pressed.