github_url
hide

# InputEventMouseButton

**Inherits:** `InputEventMouse<class_InputEventMouse>` **\<** `InputEventWithModifiers<class_InputEventWithModifiers>` **\<** `InputEventFromWindow<class_InputEventFromWindow>` **\<** `InputEvent<class_InputEvent>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a mouse button being pressed or released.

classref-introduction-group

## Description

Stores information about mouse click events. See `Node._input()<class_Node_private_method__input>`.

**Note:** On Wear OS devices, rotary input is mapped to `@GlobalScope.MOUSE_BUTTON_WHEEL_UP<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_UP>` and `@GlobalScope.MOUSE_BUTTON_WHEEL_DOWN<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_DOWN>`. This can be changed to `@GlobalScope.MOUSE_BUTTON_WHEEL_LEFT<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_LEFT>` and `@GlobalScope.MOUSE_BUTTON_WHEEL_RIGHT<class_@GlobalScope_constant_MOUSE_BUTTON_WHEEL_RIGHT>` with the `ProjectSettings.input_devices/pointing/android/rotary_input_scroll_axis<class_ProjectSettings_property_input_devices/pointing/android/rotary_input_scroll_axis>` setting.

classref-introduction-group

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`
- `Mouse and input coordinates <../tutorials/inputs/mouse_and_input_coordinates>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`MouseButton<enum_@GlobalScope_MouseButton>` **button_index** = `0` `🔗<class_InputEventMouseButton_property_button_index>`

classref-property-setget

- `void (No return value.)` **set_button_index**(value: `MouseButton<enum_@GlobalScope_MouseButton>`)
- `MouseButton<enum_@GlobalScope_MouseButton>` **get_button_index**()

The mouse button identifier, one of the `MouseButton<enum_@GlobalScope_MouseButton>` button or button wheel constants.

classref-item-separator

classref-property

`bool<class_bool>` **canceled** = `false` `🔗<class_InputEventMouseButton_property_canceled>`

classref-property-setget

- `void (No return value.)` **set_canceled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_canceled**()

If `true`, the mouse button event has been canceled.

classref-item-separator

classref-property

`bool<class_bool>` **double_click** = `false` `🔗<class_InputEventMouseButton_property_double_click>`

classref-property-setget

- `void (No return value.)` **set_double_click**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_double_click**()

If `true`, the mouse button's state is a double-click.

classref-item-separator

classref-property

`float<class_float>` **factor** = `1.0` `🔗<class_InputEventMouseButton_property_factor>`

classref-property-setget

- `void (No return value.)` **set_factor**(value: `float<class_float>`)
- `float<class_float>` **get_factor**()

The amount (or delta) of the event. When used for high-precision scroll events, this indicates the scroll amount (vertical or horizontal). This is only supported on some platforms; the reported sensitivity varies depending on the platform. May be `0` if not supported.

classref-item-separator

classref-property

`bool<class_bool>` **pressed** = `false` `🔗<class_InputEventMouseButton_property_pressed>`

classref-property-setget

- `void (No return value.)` **set_pressed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pressed**()

If `true`, the mouse button's state is pressed. If `false`, the mouse button's state is released.