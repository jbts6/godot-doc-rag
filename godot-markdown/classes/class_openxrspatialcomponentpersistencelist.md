github_url
hide

# OpenXRSpatialComponentPersistenceList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the query persistence result data.

classref-introduction-group

## Description

Object for storing the query persistence result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_persistent_state**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentPersistenceList_method_get_persistent_state>`

Returns the persistent state (`XrSpatialPersistenceStateEXT`) for the entity at this `index`.

classref-item-separator

classref-method

`String<class_String>` **get_persistent_uuid**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentPersistenceList_method_get_persistent_uuid>`

Returns the persistent uuid for the entity at this `index`.