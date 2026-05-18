github_url
hide

# OpenXRBindingModifier

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>`, `OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>`

Binding modifier base class.

classref-introduction-group

## Description

Binding modifier base class. Subclasses implement various modifiers that alter how an OpenXR runtime processes inputs.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **\_get_description**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRBindingModifier_private_method__get_description>`

Return the description of this class that is used for the title bar of the binding modifier editor.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **\_get_ip_modification**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_OpenXRBindingModifier_private_method__get_ip_modification>`

Returns the data that is sent to OpenXR when submitting the suggested interacting bindings this modifier is a part of.

**Note:** This must be data compatible with an `XrBindingModificationBaseHeaderKHR` structure.