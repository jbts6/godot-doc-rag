github_url
hide

# OpenXRSpatialCapabilityConfigurationPlaneTracking

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Configuration header for plane tracking.

classref-introduction-group

## Description

Configuration header for plane tracking. Pass this to `OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>` to create a spatial context with plane tracking capabilities.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PackedInt64Array<class_PackedInt64Array>` **get_enabled_components**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_get_enabled_components>`

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.

classref-item-separator

classref-method

`bool<class_bool>` **supports_labels**() `🔗<class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_labels>`

Returns `true` if we support the plane semantic label component (only valid after the OpenXR session has started). You can query these using the `OpenXRSpatialComponentPlaneSemanticLabelList<class_OpenXRSpatialComponentPlaneSemanticLabelList>` data object.

classref-item-separator

classref-method

`bool<class_bool>` **supports_mesh_2d**() `🔗<class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_mesh_2d>`

Returns `true` if we support the mesh 2D component (only valid after the OpenXR session has started). You can query these using the `OpenXRSpatialComponentMesh2DList<class_OpenXRSpatialComponentMesh2DList>` data object.

classref-item-separator

classref-method

`bool<class_bool>` **supports_polygons**() `🔗<class_OpenXRSpatialCapabilityConfigurationPlaneTracking_method_supports_polygons>`

Returns `true` if we support the polygon 2D component (only valid after the OpenXR session has started). You can query these using the `OpenXRSpatialComponentPolygon2DList<class_OpenXRSpatialComponentPolygon2DList>` data object.