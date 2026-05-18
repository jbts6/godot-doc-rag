github_url
hide

# InputEventFromWindow

**Inherits:** `InputEvent<class_InputEvent>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `InputEventScreenDrag<class_InputEventScreenDrag>`, `InputEventScreenTouch<class_InputEventScreenTouch>`, `InputEventWithModifiers<class_InputEventWithModifiers>`

Abstract base class for `Viewport<class_Viewport>`-based input events.

classref-introduction-group

## Description

InputEventFromWindow represents events specifically received by windows. This includes mouse events, keyboard events in focused windows or touch screen actions.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **window_id** = `0` `🔗<class_InputEventFromWindow_property_window_id>`

classref-property-setget

- `void (No return value.)` **set_window_id**(value: `int<class_int>`)
- `int<class_int>` **get_window_id**()

The ID of a `Window<class_Window>` that received this event.