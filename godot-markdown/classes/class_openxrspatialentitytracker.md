github_url
hide

# OpenXRSpatialEntityTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `XRPositionalTracker<class_XRPositionalTracker>` **\<** `XRTracker<class_XRTracker>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `OpenXRAnchorTracker<class_OpenXRAnchorTracker>`, `OpenXRMarkerTracker<class_OpenXRMarkerTracker>`, `OpenXRPlaneTracker<class_OpenXRPlaneTracker>`

Base class for Positional trackers managed by OpenXR's spatial entity extensions.

classref-introduction-group

## Description

These are trackers created and managed by OpenXR's spatial entity extensions that give access to specific data related to OpenXR's spatial entities. They will always be of type `TRACKER_ANCHOR`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**next_changed**() `🔗<class_OpenXRSpatialEntityTracker_signal_next_changed>`

Emitted when the next-chain changes, from either `add_next()<class_OpenXRSpatialEntityTracker_method_add_next>` or `remove_next()<class_OpenXRSpatialEntityTracker_method_remove_next>`.

classref-item-separator

classref-signal

**spatial_tracking_state_changed**(spatial_tracking_state: `int<class_int>`) `🔗<class_OpenXRSpatialEntityTracker_signal_spatial_tracking_state_changed>`

There is currently no description for this signal. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **EntityTrackingState**: `🔗<enum_OpenXRSpatialEntityTracker_EntityTrackingState>`

classref-enumeration-constant

`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` **ENTITY_TRACKING_STATE_STOPPED** = `1`

This anchor has stopped tracking.

classref-enumeration-constant

`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` **ENTITY_TRACKING_STATE_PAUSED** = `2`

Tracking is currently paused.

classref-enumeration-constant

`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` **ENTITY_TRACKING_STATE_TRACKING** = `3`

This anchor is currently being tracked.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **entity** = `RID()` `🔗<class_OpenXRSpatialEntityTracker_property_entity>`

classref-property-setget

- `void (No return value.)` **set_entity**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_entity**()

The spatial entity associated with this tracker.

classref-item-separator

classref-property

`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` **spatial_tracking_state** = `2` `🔗<class_OpenXRSpatialEntityTracker_property_spatial_tracking_state>`

classref-property-setget

- `void (No return value.)` **set_spatial_tracking_state**(value: `EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>`)
- `EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` **get_spatial_tracking_state**()

The spatial tracking state for this tracker.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_next**(next: `OpenXRStructureBase<class_OpenXRStructureBase>`) `🔗<class_OpenXRSpatialEntityTracker_method_add_next>`

Adds a new `OpenXRStructureBase<class_OpenXRStructureBase>` to the next-chain.

`get_next()<class_OpenXRSpatialEntityTracker_method_get_next>` will return this `next` until either `add_next()<class_OpenXRSpatialEntityTracker_method_add_next>` is called again or it's removed in `remove_next()<class_OpenXRSpatialEntityTracker_method_remove_next>`.

classref-item-separator

classref-method

`OpenXRStructureBase<class_OpenXRStructureBase>` **get_next**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityTracker_method_get_next>`

Gets the head `OpenXRStructureBase<class_OpenXRStructureBase>` in the next-chain.

See also `add_next()<class_OpenXRSpatialEntityTracker_method_add_next>` and `remove_next()<class_OpenXRSpatialEntityTracker_method_remove_next>`.

classref-item-separator

classref-method

`RID<class_RID>` **get_spatial_context**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityTracker_method_get_spatial_context>`

Gets the spatial context used to create this **OpenXRSpatialEntityTracker**.

classref-item-separator

classref-method

`void (No return value.)` **remove_next**(next: `OpenXRStructureBase<class_OpenXRStructureBase>`) `🔗<class_OpenXRSpatialEntityTracker_method_remove_next>`

Removes a `next` object previously added in `add_next()<class_OpenXRSpatialEntityTracker_method_add_next>` from the next-chain.

classref-item-separator

classref-method

`void (No return value.)` **set_spatial_context**(spatial_context: `RID<class_RID>`) `🔗<class_OpenXRSpatialEntityTracker_method_set_spatial_context>`

Sets the spatial context used to create this tracker.