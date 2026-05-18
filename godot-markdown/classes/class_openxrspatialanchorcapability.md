github_url
hide

# OpenXRSpatialAnchorCapability

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>` **\<** `Object<class_Object>`

Implementation for handling spatial entity anchor logic.

classref-introduction-group

## Description

This is an internal class that handles the OpenXR anchor spatial entity extension.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **PersistenceScope**: `🔗<enum_OpenXRSpatialAnchorCapability_PersistenceScope>`

classref-enumeration-constant

`PersistenceScope<enum_OpenXRSpatialAnchorCapability_PersistenceScope>` **PERSISTENCE_SCOPE_SYSTEM_MANAGED** = `1`

Provides the application with read-only access (i.e. application cannot modify this scope) to spatial entities persisted and managed by the system. The application can use the UUID in the persistence component for this scope to correlate entities across spatial contexts and device reboots.

classref-enumeration-constant

`PersistenceScope<enum_OpenXRSpatialAnchorCapability_PersistenceScope>` **PERSISTENCE_SCOPE_LOCAL_ANCHORS** = `1000781000`

Persistence operations and data access is limited to spatial anchors, on the same device, for the same user and same app (using `persist_anchor()<class_OpenXRSpatialAnchorCapability_method_persist_anchor>` and `unpersist_anchor()<class_OpenXRSpatialAnchorCapability_method_unpersist_anchor>` functions)

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **create_default_persistence_context**(user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialAnchorCapability_method_create_default_persistence_context>`

Calls `create_persistence_context()<class_OpenXRSpatialAnchorCapability_method_create_persistence_context>` with a configuration that likely works with the XR runtime.

`user_callback` is called when the context is created.

classref-item-separator

classref-method

`OpenXRAnchorTracker<class_OpenXRAnchorTracker>` **create_new_anchor**(transform: `Transform3D<class_Transform3D>`, spatial_context: `RID<class_RID>` = RID(), next: `OpenXRStructureBase<class_OpenXRStructureBase>` = null) `🔗<class_OpenXRSpatialAnchorCapability_method_create_new_anchor>`

Creates a new anchor that will be tracked by the XR runtime. The `transform` should be a transform in the local space of your `XROrigin3D<class_XROrigin3D>` node. If `spatial_context` is not specified the default will be used, this requires `ProjectSettings.xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection<class_ProjectSettings_property_xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection>` to be set. The returned tracker will track the location in case our reference space changes.

`next` must be a valid next object for the `XrSpatialAnchorCreateInfoEXT` chain.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **create_persistence_context**(scope: `PersistenceScope<enum_OpenXRSpatialAnchorCapability_PersistenceScope>`, user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialAnchorCapability_method_create_persistence_context>`

Creates a new persistence context for storing persistent data.

**Note:** This is an asynchronous method and returns an `OpenXRFutureResult<class_OpenXRFutureResult>` object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is the `RID<class_RID>` for our persistence context.

classref-item-separator

classref-method

`void (No return value.)` **do_entity_update**(spatial_context: `RID<class_RID>`, component_data: `Array<class_Array>`\[`OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`\], next_snapshot_create: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, next_snapshot_query: `OpenXRStructureBase<class_OpenXRStructureBase>` = null) `🔗<class_OpenXRSpatialAnchorCapability_method_do_entity_update>`

Calls `OpenXRSpatialEntityExtension.update_spatial_entities()<class_OpenXRSpatialEntityExtension_method_update_spatial_entities>` and `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>` with the anchor entities associated with `spatial_context`.

`component_data` are the `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`s to update for this anchor capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in `OpenXRSpatialEntityExtension.update_spatial_entities()<class_OpenXRSpatialEntityExtension_method_update_spatial_entities>`.

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

classref-item-separator

classref-method

`void (No return value.)` **free_persistence_context**(persistence_context: `RID<class_RID>`) `🔗<class_OpenXRSpatialAnchorCapability_method_free_persistence_context>`

Frees a persistence context previously created with `create_persistence_context()<class_OpenXRSpatialAnchorCapability_method_create_persistence_context>`.

classref-item-separator

classref-method

`int<class_int>` **get_persistence_context_handle**(persistence_context: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialAnchorCapability_method_get_persistence_context_handle>`

Returns the internal handle for this persistence context.

**Note:** For GDExtension implementations.

classref-item-separator

classref-method

`bool<class_bool>` **is_persistence_scope_supported**(scope: `PersistenceScope<enum_OpenXRSpatialAnchorCapability_PersistenceScope>`) `🔗<class_OpenXRSpatialAnchorCapability_method_is_persistence_scope_supported>`

Returns `true` if this persistence scope is supported by our spatial anchor capability.

**Note:** Only valid after an OpenXR instance has been created.

classref-item-separator

classref-method

`bool<class_bool>` **is_spatial_anchor_supported**() `🔗<class_OpenXRSpatialAnchorCapability_method_is_spatial_anchor_supported>`

Returns `true` if spatial anchors are supported by the hardware. Only returns a valid value after OpenXR has been initialized.

classref-item-separator

classref-method

`bool<class_bool>` **is_spatial_persistence_supported**() `🔗<class_OpenXRSpatialAnchorCapability_method_is_spatial_persistence_supported>`

Returns `true` if persistent spatial anchors are supported by the hardware. Only returns a valid value after OpenXR has been initialized.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **persist_anchor**(anchor_tracker: `OpenXRAnchorTracker<class_OpenXRAnchorTracker>`, persistence_context: `RID<class_RID>` = RID(), user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialAnchorCapability_method_persist_anchor>`

Changes this anchor into a persistent anchor. This means its location will be stored on the device and the anchor will be restored the next time your application starts. If `persistence_context` is not specified the default will be used, this requires `ProjectSettings.xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection<class_ProjectSettings_property_xr/openxr/extensions/spatial_entity/enable_builtin_anchor_detection>` to be set.

**Note:** This is an asynchronous method and returns an `OpenXRFutureResult<class_OpenXRFutureResult>` object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is a boolean which will be set to `true` on successful completion.

classref-item-separator

classref-method

`void (No return value.)` **remove_anchor**(anchor_tracker: `OpenXRAnchorTracker<class_OpenXRAnchorTracker>`) `🔗<class_OpenXRSpatialAnchorCapability_method_remove_anchor>`

Remove an anchor previously created with `create_new_anchor()<class_OpenXRSpatialAnchorCapability_method_create_new_anchor>`. If this anchor was persistent you must first call `unpersist_anchor()<class_OpenXRSpatialAnchorCapability_method_unpersist_anchor>` and await its callback.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **start_entity_discovery**(spatial_context: `RID<class_RID>`, component_data: `Array<class_Array>`\[`OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`\], next_snapshot_create: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, next_snapshot_query: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialAnchorCapability_method_start_entity_discovery>`

Calls `OpenXRSpatialEntityExtension.discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>` and `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>` with the anchor entities associated with `spatial_context`.

`component_data` are the `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`s to discover for this anchor capability.

If `next_snapshot_create` is non-null, then pass this to the `next` parameter in `OpenXRSpatialEntityExtension.discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>`.

If `next_snapshot_query` is non-null, then pass this to the `next` parameter in `OpenXRSpatialEntityExtension.query_snapshot()<class_OpenXRSpatialEntityExtension_method_query_snapshot>`.

`user_callback`, when non-null, is called with two parameters usually twice. The first parameter is the `RID<class_RID>` of the discovery snapshot and the second parameter is a boolean where `false` indicates the discovery snapshot is about to be processed, and `true` indicates the discovery snapshot has been processed and `component_data` has valid data. The second call is skipped if an error was encountered.

The returned `OpenXRFutureResult<class_OpenXRFutureResult>` is identical to the return from `OpenXRSpatialEntityExtension.discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>`.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **unpersist_anchor**(anchor_tracker: `OpenXRAnchorTracker<class_OpenXRAnchorTracker>`, persistence_context: `RID<class_RID>` = RID(), user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialAnchorCapability_method_unpersist_anchor>`

Removes the persistent data from this anchor. The runtime will not recreate the anchor when your application restarts. If `persistence_context` is not specified the default will be used, this requires `ProjectSettings.xr/openxr/extensions/spatial_entity/enabled<class_ProjectSettings_property_xr/openxr/extensions/spatial_entity/enabled>` to be set.

**Note:** This is an asynchronous method and returns an `OpenXRFutureResult<class_OpenXRFutureResult>` object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result value for this function is a boolean which will be set to `true` on successful completion.