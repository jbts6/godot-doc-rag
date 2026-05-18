github_url
hide

# OpenXRIPBinding

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Defines a binding between an `OpenXRAction<class_OpenXRAction>` and an XR input or output.

classref-introduction-group

## Description

This binding resource binds an `OpenXRAction<class_OpenXRAction>` to an input or output. As most controllers have left hand and right versions that are handled by the same interaction profile we can specify multiple bindings. For instance an action "Fire" could be bound to both "/user/hand/left/input/trigger" and "/user/hand/right/input/trigger". This would require two binding entries.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpenXRAction<class_OpenXRAction>` **action** `🔗<class_OpenXRIPBinding_property_action>`

classref-property-setget

- `void (No return value.)` **set_action**(value: `OpenXRAction<class_OpenXRAction>`)
- `OpenXRAction<class_OpenXRAction>` **get_action**()

`OpenXRAction<class_OpenXRAction>` that is bound to `binding_path<class_OpenXRIPBinding_property_binding_path>`.

classref-item-separator

classref-property

`Array<class_Array>` **binding_modifiers** = `[]` `🔗<class_OpenXRIPBinding_property_binding_modifiers>`

classref-property-setget

- `void (No return value.)` **set_binding_modifiers**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_binding_modifiers**()

Binding modifiers for this binding.

classref-item-separator

classref-property

`String<class_String>` **binding_path** = `""` `🔗<class_OpenXRIPBinding_property_binding_path>`

classref-property-setget

- `void (No return value.)` **set_binding_path**(value: `String<class_String>`)
- `String<class_String>` **get_binding_path**()

Binding path that defines the input or output bound to `action<class_OpenXRIPBinding_property_action>`.

**Note:** Binding paths are suggestions, an XR runtime may choose to bind the action to a different input or output emulating this input or output.

classref-item-separator

classref-property

`PackedStringArray<class_PackedStringArray>` **paths** `🔗<class_OpenXRIPBinding_property_paths>`

classref-property-setget

- `void (No return value.)` **set_paths**(value: `PackedStringArray<class_PackedStringArray>`)
- `PackedStringArray<class_PackedStringArray>` **get_paths**()

**Deprecated:** Use `binding_path<class_OpenXRIPBinding_property_binding_path>` instead.

Paths that define the inputs or outputs bound on the device.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedStringArray<class_PackedStringArray>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_path**(path: `String<class_String>`) `🔗<class_OpenXRIPBinding_method_add_path>`

**Deprecated:** Binding is for a single path.

Add an input/output path to this binding.

classref-item-separator

classref-method

`OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>` **get_binding_modifier**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRIPBinding_method_get_binding_modifier>`

Get the `OpenXRBindingModifier<class_OpenXRBindingModifier>` at this index.

classref-item-separator

classref-method

`int<class_int>` **get_binding_modifier_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRIPBinding_method_get_binding_modifier_count>`

Get the number of binding modifiers for this binding.

classref-item-separator

classref-method

`int<class_int>` **get_path_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRIPBinding_method_get_path_count>`

**Deprecated:** Binding is for a single path.

Get the number of input/output paths in this binding.

classref-item-separator

classref-method

`bool<class_bool>` **has_path**(path: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRIPBinding_method_has_path>`

**Deprecated:** Binding is for a single path.

Returns `true` if this input/output path is part of this binding.

classref-item-separator

classref-method

`void (No return value.)` **remove_path**(path: `String<class_String>`) `🔗<class_OpenXRIPBinding_method_remove_path>`

**Deprecated:** Binding is for a single path.

Removes this input/output path from this binding.