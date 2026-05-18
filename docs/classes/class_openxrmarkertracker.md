github_url
hide

# OpenXRMarkerTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>` **\<** `XRPositionalTracker<class_XRPositionalTracker>` **\<** `XRTracker<class_XRTracker>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Spatial entity tracker for our spatial entity marker tracking extension.

classref-introduction-group

## Description

Spatial entity tracker for our OpenXR spatial entity marker tracking extension. These trackers identify entities in our real space detected by a visual marker such as a QRCode or Aruco code, and map their location to our virtual space.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector2<class_Vector2>` **bounds_size** = `Vector2(0, 0)` `🔗<class_OpenXRMarkerTracker_property_bounds_size>`

classref-property-setget

- `void (No return value.)` **set_bounds_size**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_bounds_size**()

The bounds size for this marker.

classref-item-separator

classref-property

`int<class_int>` **marker_id** = `0` `🔗<class_OpenXRMarkerTracker_property_marker_id>`

classref-property-setget

- `void (No return value.)` **set_marker_id**(value: `int<class_int>`)
- `int<class_int>` **get_marker_id**()

The marker ID for this marker, this is only returned for Aruco and April Tag markers. Call `get_marker_data()<class_OpenXRMarkerTracker_method_get_marker_data>` for QRCode markers.

classref-item-separator

classref-property

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **marker_type** = `0` `🔗<class_OpenXRMarkerTracker_property_marker_type>`

classref-property-setget

- `void (No return value.)` **set_marker_type**(value: `MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>`)
- `MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **get_marker_type**()

The type of marker.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Variant<class_Variant>` **get_marker_data**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRMarkerTracker_method_get_marker_data>`

Returns the marker data for this marker. This can return a `String<class_String>` or `PackedByteArray<class_PackedByteArray>`. Only applicable to QR Code based markers.

classref-item-separator

classref-method

`void (No return value.)` **set_marker_data**(marker_data: `Variant<class_Variant>`) `🔗<class_OpenXRMarkerTracker_method_set_marker_data>`

Sets the marker data for this marker.

**Note:** This should only be set by marker discovery logic.