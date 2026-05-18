github_url
hide

# OpenXRSpatialCapabilityConfigurationMicroQrCode

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Configuration header for QR code markers.

classref-introduction-group

## Description

Configuration header for QR code markers. Pass this to `OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>` to create a spatial context that can detect QR code markers.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PackedInt64Array<class_PackedInt64Array>` **get_enabled_components**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialCapabilityConfigurationMicroQrCode_method_get_enabled_components>`

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.