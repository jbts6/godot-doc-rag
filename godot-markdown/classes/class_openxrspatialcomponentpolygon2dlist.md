github_url
hide

# OpenXRSpatialComponentPolygon2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the queries polygon2d result data.

classref-introduction-group

## Description

Object for storing the queries 2D polygon result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Transform3D<class_Transform3D>` **get_transform**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentPolygon2DList_method_get_transform>`

Returns the transform for positioning our polygon for the entity at this `index`.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **get_vertices**(snapshot: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentPolygon2DList_method_get_vertices>`

Returns the polygon vertices for the entity at this `index`.