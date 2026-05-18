github_url
hide

# OpenXRSpatialComponentMesh3DList

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Object for storing the queries mesh3d result data.

classref-introduction-group

## Description

Object for storing the queries 3d mesh result data when calling `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Mesh<class_Mesh>` **get_mesh**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentMesh3DList_method_get_mesh>`

Returns the mesh for the entity at this `index`.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_transform**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialComponentMesh3DList_method_get_transform>`

Returns the transform for positioning our mesh for the entity at this `index`.