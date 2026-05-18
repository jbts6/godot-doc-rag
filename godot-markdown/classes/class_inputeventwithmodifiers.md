github_url
hide

# InputEventWithModifiers

**Inherits:** `InputEventFromWindow<class_InputEventFromWindow>` **\<** `InputEvent<class_InputEvent>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `InputEventGesture<class_InputEventGesture>`, `InputEventKey<class_InputEventKey>`, `InputEventMouse<class_InputEventMouse>`

Abstract base class for input events affected by modifier keys like `Shift` and `Alt`.

classref-introduction-group

## Description

Stores information about mouse, keyboard, and touch gesture input events. This includes information about which modifier keys are pressed, such as `Shift` or `Alt`. See `Node._input()<class_Node_private_method__input>`.

**Note:** Modifier keys are considered modifiers only when used in combination with another key. As a result, their corresponding member variables, such as `ctrl_pressed<class_InputEventWithModifiers_property_ctrl_pressed>`, will return `false` if the key is pressed on its own.

classref-introduction-group

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **alt_pressed** = `false` `🔗<class_InputEventWithModifiers_property_alt_pressed>`

classref-property-setget

- `void (No return value.)` **set_alt_pressed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_alt_pressed**()

State of the `Alt` modifier.

classref-item-separator

classref-property

`bool<class_bool>` **command_or_control_autoremap** = `false` `🔗<class_InputEventWithModifiers_property_command_or_control_autoremap>`

classref-property-setget

- `void (No return value.)` **set_command_or_control_autoremap**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_command_or_control_autoremap**()

Automatically use `Meta` (`Cmd`) on macOS and `Ctrl` on other platforms. If `true`, `ctrl_pressed<class_InputEventWithModifiers_property_ctrl_pressed>` and `meta_pressed<class_InputEventWithModifiers_property_meta_pressed>` cannot be set.

classref-item-separator

classref-property

`bool<class_bool>` **ctrl_pressed** = `false` `🔗<class_InputEventWithModifiers_property_ctrl_pressed>`

classref-property-setget

- `void (No return value.)` **set_ctrl_pressed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_ctrl_pressed**()

State of the `Ctrl` modifier.

classref-item-separator

classref-property

`bool<class_bool>` **meta_pressed** = `false` `🔗<class_InputEventWithModifiers_property_meta_pressed>`

classref-property-setget

- `void (No return value.)` **set_meta_pressed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_meta_pressed**()

State of the `Meta` modifier. On Windows and Linux, this represents the Windows key (sometimes called "meta" or "super" on Linux). On macOS, this represents the Command key.

classref-item-separator

classref-property

`bool<class_bool>` **shift_pressed** = `false` `🔗<class_InputEventWithModifiers_property_shift_pressed>`

classref-property-setget

- `void (No return value.)` **set_shift_pressed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_shift_pressed**()

State of the `Shift` modifier.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`\] **get_modifiers_mask**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEventWithModifiers_method_get_modifiers_mask>`

Returns the keycode combination of modifier keys.

classref-item-separator

classref-method

`bool<class_bool>` **is_command_or_control_pressed**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_InputEventWithModifiers_method_is_command_or_control_pressed>`

On macOS, returns `true` if `Meta` (`Cmd`) is pressed.

On other platforms, returns `true` if `Ctrl` is pressed.