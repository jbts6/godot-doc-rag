github_url
hide

# OpenXRSpatialQueryResultData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the main query result data.

classref-introduction-group

## Description

Object for storing the main query result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`. This must always be the first component requested.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_capacity**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialQueryResultData_method_get_capacity>`

Returns the number of entities that were retrieved.

classref-item-separator

classref-method

`int<class_int>` **get_entity_id**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialQueryResultData_method_get_entity_id>`

Returns the entity id (`XrSpatialEntityIdEXT`) for the entity at this `index`.

classref-item-separator

classref-method

`EntityTrackingState<enum_OpenXRSpatialEntityTracker_EntityTrackingState>` **get_entity_state**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialQueryResultData_method_get_entity_state>`

Returns the entity state for the entity at this `index`.