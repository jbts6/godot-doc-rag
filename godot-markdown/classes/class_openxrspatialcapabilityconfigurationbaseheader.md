github_url
hide

# OpenXRSpatialCapabilityConfigurationBaseHeader

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `OpenXRSpatialCapabilityConfigurationAnchor<class_OpenXRSpatialCapabilityConfigurationAnchor>`, `OpenXRSpatialCapabilityConfigurationAprilTag<class_OpenXRSpatialCapabilityConfigurationAprilTag>`, `OpenXRSpatialCapabilityConfigurationAruco<class_OpenXRSpatialCapabilityConfigurationAruco>`, `OpenXRSpatialCapabilityConfigurationMicroQrCode<class_OpenXRSpatialCapabilityConfigurationMicroQrCode>`, `OpenXRSpatialCapabilityConfigurationPlaneTracking<class_OpenXRSpatialCapabilityConfigurationPlaneTracking>`, `OpenXRSpatialCapabilityConfigurationQrCode<class_OpenXRSpatialCapabilityConfigurationQrCode>`

Wrapper base class for OpenXR Spatial Capability Configuration headers.

classref-introduction-group

## Description

Wrapper base class for OpenXR Spatial Capability Configuration headers. This class needs to be implemented for each capability configuration structure usable within OpenXR's spatial entities system.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **\_get_configuration**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration>`

Return a pointer (encoded as an `int64_t`) to a struct holding the spatial capability configuration data. The memory for this struct should remain accessible as long as this object remains instantiated.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_valid_configuration**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__has_valid_configuration>`

Return `true` if this object contains a valid configuration that can be retrieved when calling `_get_configuration()<class_OpenXRSpatialCapabilityConfigurationBaseHeader_private_method__get_configuration>`.

classref-item-separator

classref-method

`int<class_int>` **get_configuration**() `🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_get_configuration>`

Gets a pointer to the `XrSpatialCapabilityConfigurationBaseHeaderEXT` struct.

**Note:** This method is intended to be used from GDExtensions.

classref-item-separator

classref-method

`bool<class_bool>` **has_valid_configuration**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialCapabilityConfigurationBaseHeader_method_has_valid_configuration>`

Returns `true` if this object contains a valid configuration that can be used when calling `OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>`.