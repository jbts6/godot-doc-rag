github_url
hide

# OpenXRSpatialComponentPlaneAlignmentList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the queries plane alignment result data.

classref-introduction-group

## Description

Object for storing the queries plane alignment result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **PlaneAlignment**: `🔗<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>`

classref-enumeration-constant

`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **PLANE_ALIGNMENT_HORIZONTAL_UPWARD** = `0`

Plane is facing upward.

classref-enumeration-constant

`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **PLANE_ALIGNMENT_HORIZONTAL_DOWNWARD** = `1`

Plane is facing downwards.

classref-enumeration-constant

`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **PLANE_ALIGNMENT_VERTICAL** = `2`

Plane is vertically aligned.

classref-enumeration-constant

`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **PLANE_ALIGNMENT_ARBITRARY** = `3`

Plane has an arbitrary alignment.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **get_plane_alignment**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentPlaneAlignmentList_method_get_plane_alignment>`

Returns the plane alignment for the parent entity at this `index`.