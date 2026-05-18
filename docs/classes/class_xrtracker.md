github_url
hide

# XRTracker

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `XRFaceTracker<class_XRFaceTracker>`, `XRPositionalTracker<class_XRPositionalTracker>`

A tracked object.

classref-introduction-group

## Description

This object is the base of all XR trackers.

classref-introduction-group

## Tutorials

- `XR documentation index <../tutorials/xr/index>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **description** = `""` `🔗<class_XRTracker_property_description>`

classref-property-setget

- `void (No return value.)` **set_tracker_desc**(value: `String<class_String>`)
- `String<class_String>` **get_tracker_desc**()

The description of this tracker.

classref-item-separator

classref-property

`StringName<class_StringName>` **name** = `&"Unknown"` `🔗<class_XRTracker_property_name>`

classref-property-setget

- `void (No return value.)` **set_tracker_name**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_tracker_name**()

The unique name of this tracker. The trackers that are available differ between various XR runtimes and can often be configured by the user. Godot maintains a number of reserved names that it expects the `XRInterface<class_XRInterface>` to implement if applicable:

- `"head"` identifies the `XRPositionalTracker<class_XRPositionalTracker>` of the player's head
- `"left_hand"` identifies the `XRControllerTracker<class_XRControllerTracker>` in the player's left hand
- `"right_hand"` identifies the `XRControllerTracker<class_XRControllerTracker>` in the player's right hand
- `"/user/hand_tracker/left"` identifies the `XRHandTracker<class_XRHandTracker>` for the player's left hand
- `"/user/hand_tracker/right"` identifies the `XRHandTracker<class_XRHandTracker>` for the player's right hand
- `"/user/body_tracker"` identifies the `XRBodyTracker<class_XRBodyTracker>` for the player's body
- `"/user/face_tracker"` identifies the `XRFaceTracker<class_XRFaceTracker>` for the player's face

classref-item-separator

classref-property

`TrackerType<enum_XRServer_TrackerType>` **type** = `128` `🔗<class_XRTracker_property_type>`

classref-property-setget

- `void (No return value.)` **set_tracker_type**(value: `TrackerType<enum_XRServer_TrackerType>`)
- `TrackerType<enum_XRServer_TrackerType>` **get_tracker_type**()

The type of tracker.