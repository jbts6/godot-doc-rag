github_url
hide

# OpenXRSpatialComponentData

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `OpenXRSpatialComponentAnchorList<class_OpenXRSpatialComponentAnchorList>`, `OpenXRSpatialComponentBounded2DList<class_OpenXRSpatialComponentBounded2DList>`, `OpenXRSpatialComponentBounded3DList<class_OpenXRSpatialComponentBounded3DList>`, `OpenXRSpatialComponentMarkerList<class_OpenXRSpatialComponentMarkerList>`, `OpenXRSpatialComponentMesh2DList<class_OpenXRSpatialComponentMesh2DList>`, `OpenXRSpatialComponentMesh3DList<class_OpenXRSpatialComponentMesh3DList>`, `OpenXRSpatialComponentParentList<class_OpenXRSpatialComponentParentList>`, `OpenXRSpatialComponentPersistenceList<class_OpenXRSpatialComponentPersistenceList>`, `OpenXRSpatialComponentPlaneAlignmentList<class_OpenXRSpatialComponentPlaneAlignmentList>`, `OpenXRSpatialComponentPlaneSemanticLabelList<class_OpenXRSpatialComponentPlaneSemanticLabelList>`, `OpenXRSpatialComponentPolygon2DList<class_OpenXRSpatialComponentPolygon2DList>`, `OpenXRSpatialQueryResultData<class_OpenXRSpatialQueryResultData>`

Object for storing OpenXR spatial entity component data.

classref-introduction-group

## Description

Object for storing OpenXR spatial entity component data.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **\_get_component_type**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentData_private_method__get_component_type>`

Return the component type for the component we store data for.

classref-item-separator

classref-method

`int<class_int>` **\_get_structure_data**(next: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_OpenXRSpatialComponentData_private_method__get_structure_data>`

Return a pointer to the structure data that will be submitted along with the snapshot query. This pointer must remain valid as long as this object is instantiated.

classref-item-separator

classref-method

`void (No return value.)` **\_set_capacity**(capacity: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_OpenXRSpatialComponentData_private_method__set_capacity>`

Sets the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.

classref-item-separator

classref-method

`int<class_int>` **get_component_type**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentData_method_get_component_type>`

Gets this **OpenXRSpatialComponentData**'s `XrSpatialComponentTypeEXT`.

classref-item-separator

classref-method

`void (No return value.)` **set_capacity**(capacity: `int<class_int>`) `🔗<class_OpenXRSpatialComponentData_method_set_capacity>`

Sets the expected capacity as provided by the spatial entities query system. Buffers should be initialized with the correct storage.