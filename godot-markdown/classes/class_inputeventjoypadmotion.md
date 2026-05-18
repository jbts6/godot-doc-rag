github_url
hide

# InputEventJoypadMotion

**Inherits:** `InputEvent<class_InputEvent>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents axis motions (such as joystick or analog triggers) from a gamepad.

classref-introduction-group

## Description

Stores information about joystick motions. One **InputEventJoypadMotion** represents one axis at a time. For gamepad buttons, see `InputEventJoypadButton<class_InputEventJoypadButton>`.

classref-introduction-group

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`JoyAxis<enum_@GlobalScope_JoyAxis>` **axis** = `0` `🔗<class_InputEventJoypadMotion_property_axis>`

classref-property-setget

- `void (No return value.)` **set_axis**(value: `JoyAxis<enum_@GlobalScope_JoyAxis>`)
- `JoyAxis<enum_@GlobalScope_JoyAxis>` **get_axis**()

Axis identifier.

classref-item-separator

classref-property

`float<class_float>` **axis_value** = `0.0` `🔗<class_InputEventJoypadMotion_property_axis_value>`

classref-property-setget

- `void (No return value.)` **set_axis_value**(value: `float<class_float>`)
- `float<class_float>` **get_axis_value**()

Current position of the joystick on the given axis. The value ranges from `-1.0` to `1.0`. A value of `0` means the axis is in its resting position.