github_url
hide

# Shortcut

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A shortcut for binding input.

classref-introduction-group

## Description

Shortcuts (also known as hotkeys) are containers of `InputEvent<class_InputEvent>` resources. They are commonly used to interact with a `Control<class_Control>` element from an `InputEvent<class_InputEvent>`.

One shortcut can contain multiple `InputEvent<class_InputEvent>` resources, making it possible to trigger one action with multiple different inputs.

**Example:** Capture the `Ctrl + S` shortcut using a **Shortcut** resource:

gdscript

extends Node

var save_shortcut = Shortcut.new() func ready(): var key_event = InputEventKey.new() key_event.keycode = KEY_S key_event.ctrl_pressed = true key_event.command_or_control_autoremap = true \# Swaps Ctrl for Command on Mac. save_shortcut.events = \[key_event\]

func input(event):
if save_shortcut.matches_event(event) and event.is_pressed() and not event.is_echo():
print("Save shortcut pressed!") get_viewport().set_input_as_handled()

csharp

using Godot;

public partial class MyNode : Node { private readonly Shortcut saveShortcut = new Shortcut();

> public override void Ready() { InputEventKey keyEvent = new InputEventKey { Keycode = Key.S, CtrlPressed = true, CommandOrControlAutoremap = true, // Swaps Ctrl for Command on Mac. };
>
> > saveShortcut.Events = \[keyEvent\];
>
> }
>
> public override void Input(InputEvent @event) { if (@event is InputEventKey keyEvent && saveShortcut.MatchesEvent(@event) && keyEvent.Pressed && !keyEvent.Echo) { GD.Print("Save shortcut pressed!"); GetViewport().SetInputAsHandled(); } }

}

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Array<class_Array>` **events** = `[]` `🔗<class_Shortcut_property_events>`

classref-property-setget

- `void (No return value.)` **set_events**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_events**()

The shortcut's `InputEvent<class_InputEvent>` array.

Generally the `InputEvent<class_InputEvent>` used is an `InputEventKey<class_InputEventKey>`, though it can be any `InputEvent<class_InputEvent>`, including an `InputEventAction<class_InputEventAction>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_as_text**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Shortcut_method_get_as_text>`

Returns the shortcut's first valid `InputEvent<class_InputEvent>` as a `String<class_String>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_valid_event**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Shortcut_method_has_valid_event>`

Returns whether `events<class_Shortcut_property_events>` contains an `InputEvent<class_InputEvent>` which is valid.

classref-item-separator

classref-method

`bool<class_bool>` **matches_event**(event: `InputEvent<class_InputEvent>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Shortcut_method_matches_event>`

Returns whether any `InputEvent<class_InputEvent>` in `events<class_Shortcut_property_events>` equals `event`. This uses `InputEvent.is_match()<class_InputEvent_method_is_match>` to compare events.