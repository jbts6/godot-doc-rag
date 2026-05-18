github_url
hide

# OpenXRSpatialContextPersistenceConfig

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRStructureBase<class_OpenXRStructureBase>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Configuration header for spatial persistence.

classref-introduction-group

## Description

Configuration header for spatial persistence. Pass this to `OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>` as the next parameter to create a spatial context with spatial persistence capabilities.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_persistence_context**(persistence_context: `RID<class_RID>`) `🔗<class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context>`

Adds a persistence context to this configuration. You must add at least one persistence context to create a valid configuration. You can create a persistence context by calling `OpenXRSpatialAnchorCapability.create_persistence_context()<class_OpenXRSpatialAnchorCapability_method_create_persistence_context>`.

classref-item-separator

classref-method

`Array<class_Array>` **get_persistence_contexts**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialContextPersistenceConfig_method_get_persistence_contexts>`

Gets the persistence context(s) (as `RID<class_RID>`s) received by `add_persistence_context()<class_OpenXRSpatialContextPersistenceConfig_method_add_persistence_context>`.

classref-item-separator

classref-method

`void (No return value.)` **remove_persistence_context**(persistence_context: `RID<class_RID>`) `🔗<class_OpenXRSpatialContextPersistenceConfig_method_remove_persistence_context>`

Removes a persistence context.