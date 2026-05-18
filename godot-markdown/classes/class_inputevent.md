github_url
hide

# InputEvent

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `InputEventAction<class_InputEventAction>`, `InputEventFromWindow<class_InputEventFromWindow>`, `InputEventJoypadButton<class_InputEventJoypadButton>`, `InputEventJoypadMotion<class_InputEventJoypadMotion>`, `InputEventMIDI<class_InputEventMIDI>`, `InputEventShortcut<class_InputEventShortcut>`

Abstract base class for input events.

classref-introduction-group

## Description

Abstract base class of all types of input events. See `Node._input()<class_Node_private_method__input>`.

classref-introduction-group

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`
- `Viewport and canvas transforms <../tutorials/2d/2d_transforms>`
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**DEVICE_ID_EMULATION** = `-1` `🔗<class_InputEvent_constant_DEVICE_ID_EMULATION>`

Device ID used for emulated mouse input from a touchscreen, or for emulated touch input from a mouse. This can be used to distinguish emulated mouse input from physical mouse input, or emulated touch input from physical touch input.

classref-constant

**DEVICE_ID_KEYBOARD** = `16` `🔗<class_InputEvent_constant_DEVICE_ID_KEYBOARD>`

Device ID used for input from a keyboard. This can be used to distinguish keyboard input events from joypad input events.

classref-constant

**DEVICE_ID_MOUSE** = `32` `🔗<class_InputEvent_constant_DEVICE_ID_MOUSE>`

Device ID used for input from a mouse. This can be used to distinguish mouse input events from joypad input events.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **device** = `0` `🔗<class_InputEvent_property_device>`

classref-property-setget

- `void (No return value.)` **set_device**(value: `int<class_int>`)
- `int<class_int>` **get_device**()

The event's device ID.

**Note:** `device<class_InputEvent_property_device>` can be negative for special use cases that don't refer to devices physically present on the system. See `DEVICE_ID_EMULATION<class_InputEvent_constant_DEVICE_ID_EMULATION>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **accumulate**(with_event: `InputEvent<class_InputEvent>`) `🔗<class_InputEvent_method_accumulate>`

Returns `true` if the given input event and this input event can be added together (only for events of type `InputEventMouseMotion<class_InputEventMouseMotion>`).

The given input event's position, global position and speed will be copied. The resulting `relative` is a sum of both events. Both events' modifiers have to be identical.

classref-item-separator

classref-method

`String<class_String>` **as_text**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_as_text>`

Returns a `String<class_String>` representation of the event.

classref-item-separator

classref-method

`float<class_float>` **get_action_strength**(action: `StringName<class_StringName>`, exact_match: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_get_action_strength>`

Returns a value between 0.0 and 1.0 depending on the given actions' state. Useful for getting the value of events of type `InputEventJoypadMotion<class_InputEventJoypadMotion>`.

If `exact_match` is `false`, it ignores additional input modifiers for `InputEventKey<class_InputEventKey>` and `InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for `InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

classref-item-separator

classref-method

`bool<class_bool>` **is_action**(action: `StringName<class_StringName>`, exact_match: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_action>`

Returns `true` if this input event matches a pre-defined action of any type.

If `exact_match` is `false`, it ignores additional input modifiers for `InputEventKey<class_InputEventKey>` and `InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for `InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

classref-item-separator

classref-method

`bool<class_bool>` **is_action_pressed**(action: `StringName<class_StringName>`, allow_echo: `bool<class_bool>` = false, exact_match: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_action_pressed>`

Returns `true` if the given action matches this event and is being pressed (and is not an echo event for `InputEventKey<class_InputEventKey>` events, unless `allow_echo` is `true`). Not relevant for events of type `InputEventMouseMotion<class_InputEventMouseMotion>` or `InputEventScreenDrag<class_InputEventScreenDrag>`.

If `exact_match` is `false`, it ignores additional input modifiers for `InputEventKey<class_InputEventKey>` and `InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for `InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

**Note:** Due to keyboard ghosting, `is_action_pressed()<class_InputEvent_method_is_action_pressed>` may return `false` even if one of the action's keys is pressed. See [Input examples](../tutorials/inputs/input_examples.html#keyboard-events) in the documentation for more information.

classref-item-separator

classref-method

`bool<class_bool>` **is_action_released**(action: `StringName<class_StringName>`, exact_match: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_action_released>`

Returns `true` if the given action matches this event and is released (i.e. not pressed). Not relevant for events of type `InputEventMouseMotion<class_InputEventMouseMotion>` or `InputEventScreenDrag<class_InputEventScreenDrag>`.

If `exact_match` is `false`, it ignores additional input modifiers for `InputEventKey<class_InputEventKey>` and `InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for `InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

classref-item-separator

classref-method

`bool<class_bool>` **is_action_type**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_action_type>`

Returns `true` if this input event's type is one that can be assigned to an input action: `InputEventKey<class_InputEventKey>`, `InputEventMouseButton<class_InputEventMouseButton>`, `InputEventJoypadButton<class_InputEventJoypadButton>`, `InputEventJoypadMotion<class_InputEventJoypadMotion>`, `InputEventAction<class_InputEventAction>`. Returns `false` for all other input event types.

classref-item-separator

classref-method

`bool<class_bool>` **is_canceled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_canceled>`

Returns `true` if this input event has been canceled.

classref-item-separator

classref-method

`bool<class_bool>` **is_echo**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_echo>`

Returns `true` if this input event is an echo event (only for events of type `InputEventKey<class_InputEventKey>`). An echo event is a repeated key event sent when the user is holding down the key. Any other event type returns `false`.

**Note:** The rate at which echo events are sent is typically around 20 events per second (after holding down the key for roughly half a second). However, the key repeat delay/speed can be changed by the user or disabled entirely in the operating system settings. To ensure your project works correctly on all configurations, do not assume the user has a specific key repeat configuration in your project's behavior.

classref-item-separator

classref-method

`bool<class_bool>` **is_match**(event: `InputEvent<class_InputEvent>`, exact_match: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_match>`

Returns `true` if the specified `event` matches this event. Only valid for action events, which include key (`InputEventKey<class_InputEventKey>`), button (`InputEventMouseButton<class_InputEventMouseButton>` or `InputEventJoypadButton<class_InputEventJoypadButton>`), axis `InputEventJoypadMotion<class_InputEventJoypadMotion>`, and action (`InputEventAction<class_InputEventAction>`) events.

If `exact_match` is `false`, the check ignores additional input modifiers for `InputEventKey<class_InputEventKey>` and `InputEventMouseButton<class_InputEventMouseButton>` events, and the direction for `InputEventJoypadMotion<class_InputEventJoypadMotion>` events.

**Note:** This method only considers the event configuration (such as the keyboard key or the joypad axis), not state information like `is_pressed()<class_InputEvent_method_is_pressed>`, `is_released()<class_InputEvent_method_is_released>`, `is_echo()<class_InputEvent_method_is_echo>`, or `is_canceled()<class_InputEvent_method_is_canceled>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_pressed**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_pressed>`

Returns `true` if this input event is pressed. Not relevant for events of type `InputEventMouseMotion<class_InputEventMouseMotion>` or `InputEventScreenDrag<class_InputEventScreenDrag>`.

**Note:** Due to keyboard ghosting, `is_pressed()<class_InputEvent_method_is_pressed>` may return `false` even if one of the action's keys is pressed. See [Input examples](../tutorials/inputs/input_examples.html#keyboard-events) in the documentation for more information.

classref-item-separator

classref-method

`bool<class_bool>` **is_released**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_is_released>`

Returns `true` if this input event is released. Not relevant for events of type `InputEventMouseMotion<class_InputEventMouseMotion>` or `InputEventScreenDrag<class_InputEventScreenDrag>`.

classref-item-separator

classref-method

`InputEvent<class_InputEvent>` **xformed_by**(xform: `Transform2D<class_Transform2D>`, local_ofs: `Vector2<class_Vector2>` = Vector2(0, 0)) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEvent_method_xformed_by>`

Returns a copy of the given input event which has been offset by `local_ofs` and transformed by `xform`. Relevant for events of type `InputEventMouseButton<class_InputEventMouseButton>`, `InputEventMouseMotion<class_InputEventMouseMotion>`, `InputEventScreenTouch<class_InputEventScreenTouch>`, `InputEventScreenDrag<class_InputEventScreenDrag>`, `InputEventMagnifyGesture<class_InputEventMagnifyGesture>` and `InputEventPanGesture<class_InputEventPanGesture>`.