github_url
hide

# OpenXRAnchorTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>` **\<** `XRPositionalTracker<class_XRPositionalTracker>` **\<** `XRTracker<class_XRTracker>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Positional tracker for our spatial entity anchor extension.

classref-introduction-group

## Description

Positional tracker for our OpenXR spatial entity anchor extension, it tracks a user defined location in real space and maps it to our virtual space.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**uuid_changed**() `🔗<class_OpenXRAnchorTracker_signal_uuid_changed>`

Emitted when the UUID for this anchor was changed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **uuid** = `""` `🔗<class_OpenXRAnchorTracker_property_uuid>`

classref-property-setget

- `void (No return value.)` **set_uuid**(value: `String<class_String>`)
- `String<class_String>` **get_uuid**()

The UUID provided for persistent anchors.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **has_uuid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRAnchorTracker_method_has_uuid>`

Returns `true` if a non-zero UUID is set.