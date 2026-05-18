github_url
hide

# OpenXRSpatialComponentPlaneSemanticLabelList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the queries plane semantic label result data.

classref-introduction-group

## Description

Object for storing the queries plane semantic label result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **PlaneSemanticLabel**: `🔗<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>`

classref-enumeration-constant

`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` **PLANE_SEMANTIC_LABEL_UNCATEGORIZED** = `1`

Uncategorized plane.

classref-enumeration-constant

`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` **PLANE_SEMANTIC_LABEL_FLOOR** = `2`

Plane represents a floor.

classref-enumeration-constant

`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` **PLANE_SEMANTIC_LABEL_WALL** = `3`

Plane represents a wall.

classref-enumeration-constant

`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` **PLANE_SEMANTIC_LABEL_CEILING** = `4`

Plane represents a ceiling.

classref-enumeration-constant

`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` **PLANE_SEMANTIC_LABEL_TABLE** = `5`

Plane represents the surface of a table.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PlaneSemanticLabel<enum_OpenXRSpatialComponentPlaneSemanticLabelList_PlaneSemanticLabel>` **get_plane_semantic_label**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentPlaneSemanticLabelList_method_get_plane_semantic_label>`

Returns the plane semantic label for the parent entity at this `index`.