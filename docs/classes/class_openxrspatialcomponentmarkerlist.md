github_url
hide

# OpenXRSpatialComponentMarkerList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the queries marker result data.

classref-introduction-group

## Description

Object for storing the queries marker result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **MarkerType**: `🔗<enum_OpenXRSpatialComponentMarkerList_MarkerType>`

classref-enumeration-constant

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **MARKER_TYPE_UNKNOWN** = `0`

Unknown or unset marker type.

classref-enumeration-constant

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **MARKER_TYPE_QRCODE** = `1`

Marker based on a QR code.

classref-enumeration-constant

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **MARKER_TYPE_MICRO_QRCODE** = `2`

Marker based on a micro QR code.

classref-enumeration-constant

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **MARKER_TYPE_ARUCO** = `3`

Marker based on an Aruco code.

classref-enumeration-constant

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **MARKER_TYPE_APRIL_TAG** = `4`

Marker based on an April Tag.

classref-enumeration-constant

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **MARKER_TYPE_MAX** = `5`

Maximum value for this enum.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Variant<class_Variant>` **get_marker_data**(snapshot: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentMarkerList_method_get_marker_data>`

Returns either a `String<class_String>` or a `PackedByteArray<class_PackedByteArray>` buffer with data for the marker at this `index`. Only applicable for QR code markers.

classref-item-separator

classref-method

`int<class_int>` **get_marker_id**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentMarkerList_method_get_marker_id>`

Returns the marker ID for the marker at this `index`. Only applicable for Aruco or April Tag markers.

classref-item-separator

classref-method

`MarkerType<enum_OpenXRSpatialComponentMarkerList_MarkerType>` **get_marker_type**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentMarkerList_method_get_marker_type>`

Returns the marker type for the marker at this `index`.