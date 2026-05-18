github_url
hide

# OpenXRSpatialEntityExtension

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>` **\<** `Object<class_Object>`

OpenXR extension that handles spatial entities.

classref-introduction-group

## Description

OpenXR extension that handles spatial entities and, when enabled, allows querying those spatial entities. This extension will also automatically manage `XRTracker<class_XRTracker>` objects for static entities.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**spatial_discovery_recommended**(spatial_context: `RID<class_RID>`) `🔗<class_OpenXRSpatialEntityExtension_signal_spatial_discovery_recommended>`

Emitted when OpenXR recommends running a discovery query because entities managed by this spatial context have (likely) changed.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Capability**: `🔗<enum_OpenXRSpatialEntityExtension_Capability>`

classref-enumeration-constant

`Capability<enum_OpenXRSpatialEntityExtension_Capability>` **CAPABILITY_PLANE_TRACKING** = `1000741000`

Plane tracking capability.

classref-enumeration-constant

`Capability<enum_OpenXRSpatialEntityExtension_Capability>` **CAPABILITY_MARKER_TRACKING_QR_CODE** = `1000743000`

QR code based marker tracking capability.

classref-enumeration-constant

`Capability<enum_OpenXRSpatialEntityExtension_Capability>` **CAPABILITY_MARKER_TRACKING_MICRO_QR_CODE** = `1000743001`

Micro QR code based marker tracking capability.

classref-enumeration-constant

`Capability<enum_OpenXRSpatialEntityExtension_Capability>` **CAPABILITY_MARKER_TRACKING_ARUCO_MARKER** = `1000743002`

Aruco marker based marker tracking capability.

classref-enumeration-constant

`Capability<enum_OpenXRSpatialEntityExtension_Capability>` **CAPABILITY_MARKER_TRACKING_APRIL_TAG** = `1000743003`

April tag based marker tracking capability.

classref-enumeration-constant

`Capability<enum_OpenXRSpatialEntityExtension_Capability>` **CAPABILITY_ANCHOR** = `1000762000`

Anchor capability.

classref-item-separator

classref-enumeration

enum **ComponentType**: `🔗<enum_OpenXRSpatialEntityExtension_ComponentType>`

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_BOUNDED_2D** = `1`

Component that provides the 2D bounds for a spatial entity. The corresponding list structure is `XrSpatialComponentBounded2DListEXT`; the corresponding data structure is `XrSpatialBounded2DDataEXT`.

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_BOUNDED_3D** = `2`

Component that provides the 3D bounds for a spatial entity. The corresponding list structure is `XrSpatialComponentBounded3DListEXT`; the corresponding data structure is `XrBoxf`.

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_PARENT** = `3`

Component that provides the XrSpatialEntityIdEXT of the parent for a spatial entity. The corresponding list structure is `XrSpatialComponentParentListEXT`; the corresponding data structure is `XrSpatialEntityIdEXT`.

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_MESH_3D** = `4`

Component that provides a 3D mesh for a spatial entity. The corresponding list structure is `XrSpatialComponentMesh3DListEXT`; the corresponding data structure is `XrSpatialMeshDataEXT`.

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_PLANE_ALIGNMENT** = `1000741000`

Component that provides the plane alignment enum for a spatial entity. The corresponding list structure is `XrSpatialComponentPlaneAlignmentListEXT`; the corresponding data structure is `XrSpatialPlaneAlignmentEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_MESH_2D** = `1000741001`

Component that provides a 2D mesh for a spatial entity. The corresponding list structure is `XrSpatialComponentMesh2DListEXT`; the corresponding data structure is `XrSpatialMeshDataEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_POLYGON_2D** = `1000741002`

Component that provides a 2D boundary polygon for a spatial entity. The corresponding list structure is `XrSpatialComponentPolygon2DListEXT`; the corresponding data structure is `XrSpatialPolygon2DDataEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_PLANE_SEMANTIC_LABEL** = `1000741003`

Component that provides a semantic label for a plane. The corresponding list structure is `XrSpatialComponentPlaneSemanticLabelListEXT`; the corresponding data structure is `XrSpatialPlaneSemanticLabelEXT` (Added by the `XR_EXT_spatial_plane_tracking` extension).

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_MARKER** = `1000743000`

A component describing the marker type, ID and location. The corresponding list structure is `XrSpatialComponentMarkerListEXT`; the corresponding data structure is `XrSpatialMarkerDataEXT` (Added by the `XR_EXT_spatial_marker_tracking` extension).

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_ANCHOR** = `1000762000`

Component that provides the location for an anchor. The corresponding list structure is `XrSpatialComponentAnchorListEXT`; the corresponding data structure is `XrPosef` (Added by the `XR_EXT_spatial_anchor` extension).

classref-enumeration-constant

`ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>` **COMPONENT_TYPE_PERSISTENCE** = `1000763000`

Component that provides the persisted UUID for a spatial entity. The corresponding list structure is `XrSpatialComponentPersistenceListEXT; the corresponding data structure is [code]XrSpatialPersistenceDataEXT` (Added by the `XR_EXT_spatial_persistence` extension).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **add_spatial_entity**(spatial_context: `RID<class_RID>`, entity_id: `int<class_int>`, entity: `int<class_int>`) `🔗<class_OpenXRSpatialEntityExtension_method_add_spatial_entity>`

Registers an entity that was created directly on the OpenXR runtime.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **create_spatial_context**(capability_configurations: `Array<class_Array>`\[`OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>`\], next: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialEntityExtension_method_create_spatial_context>`

Creates a new spatial context that handles entities for the provided capability configurations. `capability_configurations` is an array of `OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>` with the needed capability configuration data.

`next` is an optional parameter that can contain additional information for creating our spatial context.

**Note:** This is an asynchronous method and returns an `OpenXRFutureResult<class_OpenXRFutureResult>` object with which to track the status, discarding this object will not cancel the creation process. On success `user_callback` will be called if specified. The result data for this function is the `RID<class_RID>` for our spatial context.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **discover_spatial_entities**(spatial_context: `RID<class_RID>`, component_types: `PackedInt64Array<class_PackedInt64Array>`, next: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>`

Starts a new discovery query, this will gather all objects tracked by the `spatial_context` that have at least one of the component types specified in `component_types`.

`next` is an optional parameter that can contain additional information for executing the discovery query.

**Note:** This is an asynchronous method and returns an `OpenXRFutureResult<class_OpenXRFutureResult>` object with which to track the status, discarding this object will not cancel the discovery process. On success `user_callback` will be called if specified. The result data for this function is the `RID<class_RID>` for our snapshot.

classref-item-separator

classref-method

`OpenXRFutureResult<class_OpenXRFutureResult>` **discover_spatial_entities_with_component_data**(spatial_context: `RID<class_RID>`, component_data: `Array<class_Array>`\[`OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`\], next: `OpenXRStructureBase<class_OpenXRStructureBase>` = null, user_callback: `Callable<class_Callable>` = Callable()) `🔗<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities_with_component_data>`

Convenience method when the caller only has an `Array<class_Array>` of `OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>` and needs to discover spatial entities.

classref-item-separator

classref-method

`RID<class_RID>` **find_spatial_entity**(entity_id: `int<class_int>`) `🔗<class_OpenXRSpatialEntityExtension_method_find_spatial_entity>`

Returns the `RID<class_RID>` for the specified spatial entity ID.

classref-item-separator

classref-method

`void (No return value.)` **free_spatial_context**(spatial_context: `RID<class_RID>`) `🔗<class_OpenXRSpatialEntityExtension_method_free_spatial_context>`

Frees a spatial context previously created when calling `create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>`. If the spatial context creation is still ongoing, the asynchronous process is cancelled.

classref-item-separator

classref-method

`void (No return value.)` **free_spatial_entity**(entity: `RID<class_RID>`) `🔗<class_OpenXRSpatialEntityExtension_method_free_spatial_entity>`

Frees an entity previously created when calling `add_spatial_entity()<class_OpenXRSpatialEntityExtension_method_add_spatial_entity>` or `make_spatial_entity()<class_OpenXRSpatialEntityExtension_method_make_spatial_entity>`.

classref-item-separator

classref-method

`void (No return value.)` **free_spatial_snapshot**(spatial_snapshot: `RID<class_RID>`) `🔗<class_OpenXRSpatialEntityExtension_method_free_spatial_snapshot>`

Frees a spatial snapshot previously created when calling `discover_spatial_entities()<class_OpenXRSpatialEntityExtension_method_discover_spatial_entities>`. If the spatial snapshot creation is still ongoing, the asynchronous process is cancelled.

classref-item-separator

classref-method

`PackedFloat32Array<class_PackedFloat32Array>` **get_float_buffer**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_float_buffer>`

Returns a buffer with floats from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`int<class_int>` **get_spatial_context_handle**(spatial_context: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_spatial_context_handle>`

Returns the OpenXR spatial context handle for this snapshot.

**Note:** This method is intended to be used from GDExtensions that implement spatial entity capability handlers.

classref-item-separator

classref-method

`bool<class_bool>` **get_spatial_context_ready**(spatial_context: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_spatial_context_ready>`

Returns `true` if the spatial context finished its creation and is ready to be used.

classref-item-separator

classref-method

`RID<class_RID>` **get_spatial_entity_context**(entity: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_spatial_entity_context>`

Returns the spatial context for this entity.

classref-item-separator

classref-method

`int<class_int>` **get_spatial_entity_id**(entity: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_spatial_entity_id>`

Returns the internal `XrSpatialEntityIdEXT` associated with the entity.

classref-item-separator

classref-method

`RID<class_RID>` **get_spatial_snapshot_context**(spatial_snapshot: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_spatial_snapshot_context>`

Returns the spatial context related to this spatial snapshot.

classref-item-separator

classref-method

`int<class_int>` **get_spatial_snapshot_handle**(spatial_snapshot: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_spatial_snapshot_handle>`

Returns the OpenXR spatial snapshot handle for this snapshot.

**Note:** This method is intended to be used from GDExtensions that implement spatial entity capability handlers.

classref-item-separator

classref-method

`String<class_String>` **get_string**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_string>`

Returns a string from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **get_uint8_buffer**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_uint8_buffer>`

Returns a buffer with 8 bit ints from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_uint16_buffer**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_uint16_buffer>`

Returns a buffer with 16 bit ints from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_uint32_buffer**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_uint32_buffer>`

Returns a buffer with 32 bit ints from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **get_vector2_buffer**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_vector2_buffer>`

Returns a buffer with `Vector2<class_Vector2>` entries from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`PackedVector3Array<class_PackedVector3Array>` **get_vector3_buffer**(spatial_snapshot: `RID<class_RID>`, buffer_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialEntityExtension_method_get_vector3_buffer>`

Returns a buffer with `Vector3<class_Vector3>` entries from a buffer that was retrieved when taking a snapshot.

classref-item-separator

classref-method

`RID<class_RID>` **make_spatial_entity**(spatial_context: `RID<class_RID>`, entity_id: `int<class_int>`) `🔗<class_OpenXRSpatialEntityExtension_method_make_spatial_entity>`

Creates a new entity for this `entity_id`. The `spatial_context` should match the context that discovered the entity.

classref-item-separator

classref-method

`bool<class_bool>` **query_snapshot**(spatial_snapshot: `RID<class_RID>`, component_data: `Array<class_Array>`\[`OpenXRSpatialComponentData<class_OpenXRSpatialComponentData>`\], next: `OpenXRStructureBase<class_OpenXRStructureBase>` = null) `🔗<class_OpenXRSpatialEntityExtension_method_query_snapshot>`

Queries the snapshot data. This will find all entities in the snapshot that contain all requested components in `component_data`. The objects held within `component_data` will then be populated with the queried data. `component_data` must always have an object of `OpenXRSpatialQueryResultData<class_OpenXRSpatialQueryResultData>` as the first entry.

`next` is an optional parameter that can contain additional information passed when setting our query conditions.

classref-item-separator

classref-method

`bool<class_bool>` **supports_capability**(capability: `Capability<enum_OpenXRSpatialEntityExtension_Capability>`) `🔗<class_OpenXRSpatialEntityExtension_method_supports_capability>`

Returns `true` if this spatial entity `capability` is supported by the hardware used.

classref-item-separator

classref-method

`bool<class_bool>` **supports_component_type**(capability: `Capability<enum_OpenXRSpatialEntityExtension_Capability>`, component_type: `ComponentType<enum_OpenXRSpatialEntityExtension_ComponentType>`) `🔗<class_OpenXRSpatialEntityExtension_method_supports_component_type>`

Returns `true` if this `capability` supports the `component_type`.

classref-item-separator

classref-method

`RID<class_RID>` **update_spatial_entities**(spatial_context: `RID<class_RID>`, entities: `Array<class_Array>`\[`RID<class_RID>`\], component_types: `PackedInt64Array<class_PackedInt64Array>`, next: `OpenXRStructureBase<class_OpenXRStructureBase>` = null) `🔗<class_OpenXRSpatialEntityExtension_method_update_spatial_entities>`

Performs a snapshot for a limited number of entities. This is NOT an asynchronous method and will return the snapshot immediately.