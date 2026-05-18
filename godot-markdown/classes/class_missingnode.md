github_url
hide

# MissingNode

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

An internal editor class intended for keeping the data of unrecognized nodes.

classref-introduction-group

## Description

This is an internal editor class intended for keeping data of nodes of unknown type (most likely this type was supplied by an extension that is no longer loaded). It can't be manually instantiated or placed in a scene.

**Warning:** Ignore missing nodes unless you know what you are doing. Existing properties on a missing node can be freely modified in code, regardless of the type they are intended to be.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **original_class** `🔗<class_MissingNode_property_original_class>`

classref-property-setget

- `void (No return value.)` **set_original_class**(value: `String<class_String>`)
- `String<class_String>` **get_original_class**()

The name of the class this node was supposed to be (see `Object.get_class()<class_Object_method_get_class>`).

classref-item-separator

classref-property

`String<class_String>` **original_scene** `🔗<class_MissingNode_property_original_scene>`

classref-property-setget

- `void (No return value.)` **set_original_scene**(value: `String<class_String>`)
- `String<class_String>` **get_original_scene**()

Returns the path of the scene this node was instance of originally.

classref-item-separator

classref-property

`bool<class_bool>` **recording_properties** `🔗<class_MissingNode_property_recording_properties>`

classref-property-setget

- `void (No return value.)` **set_recording_properties**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_recording_properties**()

If `true`, allows new properties to be set along with existing ones. If `false`, only existing properties' values can be set, and new properties cannot be added.

classref-item-separator

classref-property

`bool<class_bool>` **recording_signals** `🔗<class_MissingNode_property_recording_signals>`

classref-property-setget

- `void (No return value.)` **set_recording_signals**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_recording_signals**()

If `true`, allows new signals to be connected to along with existing ones. If `false`, only existing signals can be connected to, and new signals cannot be added.