github_url
hide

# OpenXRAction

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

An OpenXR action.

classref-introduction-group

## Description

This resource defines an OpenXR action. Actions can be used both for inputs (buttons, joysticks, triggers, etc.) and outputs (haptics).

OpenXR performs automatic conversion between action type and input type whenever possible. An analog trigger bound to a boolean action will thus return `false` if the trigger is depressed and `true` if pressed fully.

Actions are not directly bound to specific devices, instead OpenXR recognizes a limited number of top level paths that identify devices by usage. We can restrict which devices an action can be bound to by these top level paths. For instance an action that should only be used for hand held controllers can have the top level paths "/user/hand/left" and "/user/hand/right" associated with them. See the [reserved path section in the OpenXR specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-reserved) for more info on the top level paths.

Note that the name of the resource is used to register the action with.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ActionType**: `🔗<enum_OpenXRAction_ActionType>`

classref-enumeration-constant

`ActionType<enum_OpenXRAction_ActionType>` **OPENXR_ACTION_BOOL** = `0`

This action provides a boolean value.

classref-enumeration-constant

`ActionType<enum_OpenXRAction_ActionType>` **OPENXR_ACTION_FLOAT** = `1`

This action provides a float value between `0.0` and `1.0` for any analog input such as triggers.

classref-enumeration-constant

`ActionType<enum_OpenXRAction_ActionType>` **OPENXR_ACTION_VECTOR2** = `2`

This action provides a `Vector2<class_Vector2>` value and can be bound to embedded trackpads and joysticks.

classref-enumeration-constant

`ActionType<enum_OpenXRAction_ActionType>` **OPENXR_ACTION_POSE** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`ActionType<enum_OpenXRAction_ActionType>` **action_type** = `1` `🔗<class_OpenXRAction_property_action_type>`

classref-property-setget

- `void (No return value.)` **set_action_type**(value: `ActionType<enum_OpenXRAction_ActionType>`)
- `ActionType<enum_OpenXRAction_ActionType>` **get_action_type**()

The type of action.

classref-item-separator

classref-property

`String<class_String>` **localized_name** = `""` `🔗<class_OpenXRAction_property_localized_name>`

classref-property-setget

- `void (No return value.)` **set_localized_name**(value: `String<class_String>`)
- `String<class_String>` **get_localized_name**()

The localized description of this action.

classref-item-separator

classref-property

`PackedStringArray<class_PackedStringArray>` **toplevel_paths** = `PackedStringArray()` `🔗<class_OpenXRAction_property_toplevel_paths>`

classref-property-setget

- `void (No return value.)` **set_toplevel_paths**(value: `PackedStringArray<class_PackedStringArray>`)
- `PackedStringArray<class_PackedStringArray>` **get_toplevel_paths**()

A collections of toplevel paths to which this action can be bound.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedStringArray<class_PackedStringArray>` for more details.