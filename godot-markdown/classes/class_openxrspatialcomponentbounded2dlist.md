github_url
hide

# OpenXRSpatialComponentBounded2DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the queries bounded2d result data.

classref-introduction-group

## Description

Object for storing the queries 2D bounding rectangle result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Transform3D<class_Transform3D>` **get_center_pose**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentBounded2DList_method_get_center_pose>`

Returns the center of our bounding rectangle for the entity at this `index`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_size**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentBounded2DList_method_get_size>`

Returns the size of our bounding rectangle for the entity at this `index`.