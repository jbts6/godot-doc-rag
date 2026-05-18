github_url
hide

# OpenXRSpatialPlaneTrackingCapability

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>` **\<** `Object<class_Object>`

Implementation for handling spatial entity plane tracking logic.

classref-introduction-group

## Description

This class handles the OpenXR plane tracking spatial entity extension.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_supported**() `🔗<class_OpenXRSpatialPlaneTrackingCapability_method_is_supported>`

Returns `true` if plane tracking is supported by the current device.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **start_entity_discovery**(spatial_context: `RID<class_RID>`, component_data: `Array<class_Array>`\[`OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`\], next_snapshot_create: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, next_snapshot_query: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialPlaneTrackingCapability_method_start_entity_discovery>`

Calls `OpenXRSpatialEntityExtension.discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>` and `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>` with the plane entities associated with `spatial_context`.

`component_data` are the `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`s to discover for this plane capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in `OpenXRSpatialEntityExtension.discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>`.

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

`user_callback`, when non-null, is called with two parameters usually twice. The first parameter is the `RID<class_RID>` of the discovery snapshot and the second parameter is a boolean where `false` indicates the discovery snapshot is about to be processed, and `true` indicates the discovery snapshot has been processed and `component_data` has valid data. The second call is skipped if an error was encountered.

The returned `OpenXRFutureResult<class_OpenXRFutureResult>` is identical to the return from `OpenXRSpatialEntityExtension.discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>`.