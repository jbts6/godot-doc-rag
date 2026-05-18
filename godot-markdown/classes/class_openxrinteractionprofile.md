github_url
hide

# OpenXRInteractionProfile

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Suggested bindings object for OpenXR.

classref-introduction-group

## Description

This object stores suggested bindings for an interaction profile. Interaction profiles define the metadata for a tracked XR device such as an XR controller.

For more information see the [interaction profiles info in the OpenXR specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles).

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Array<class_Array>` **binding_modifiers** = `[]` `🔗<class_OpenXRInteractionProfile_property_binding_modifiers>`

classref-property-setget

- `void (No return value.)` **set_binding_modifiers**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_binding_modifiers**()

Binding modifiers for this interaction profile.

classref-item-separator

classref-property

`Array<class_Array>` **bindings** = `[]` `🔗<class_OpenXRInteractionProfile_property_bindings>`

classref-property-setget

- `void (No return value.)` **set_bindings**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_bindings**()

Action bindings for this interaction profile.

classref-item-separator

classref-property

`String<class_String>` **interaction_profile_path** = `""` `🔗<class_OpenXRInteractionProfile_property_interaction_profile_path>`

classref-property-setget

- `void (No return value.)` **set_interaction_profile_path**(value: `String<class_String>`)
- `String<class_String>` **get_interaction_profile_path**()

The interaction profile path identifying the XR device.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`OpenXRIPBinding<class_OpenXRIPBinding>` **get_binding**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRInteractionProfile_method_get_binding>`

Retrieve the binding at this index.

classref-item-separator

classref-method

`int<class_int>` **get_binding_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRInteractionProfile_method_get_binding_count>`

Get the number of bindings in this interaction profile.

classref-item-separator

classref-method

`OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>` **get_binding_modifier**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRInteractionProfile_method_get_binding_modifier>`

Get the `OpenXRBindingModifier<class_OpenXRBindingModifier>` at this index.

classref-item-separator

classref-method

`int<class_int>` **get_binding_modifier_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRInteractionProfile_method_get_binding_modifier_count>`

Get the number of binding modifiers in this interaction profile.