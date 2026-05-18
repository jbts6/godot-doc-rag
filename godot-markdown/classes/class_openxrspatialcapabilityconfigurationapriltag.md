github_url
hide

# OpenXRSpatialCapabilityConfigurationAprilTag

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialCapabilityConfigurationBaseHeader<class_OpenXRSpatialCapabilityConfigurationBaseHeader>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Configuration header for April tag markers.

classref-introduction-group

## Description

Configuration header for April tag markers. Pass this to `OpenXRSpatialEntityExtension.create_spatial_context()<class_OpenXRSpatialEntityExtension_method_create_spatial_context>` to create a spatial context that can detect April tags.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **AprilTagDict**: `🔗<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>`

classref-enumeration-constant

`AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>` **APRIL_TAG_DICT_16H5** = `1`

4 by 4 bits, minimum Hamming distance between any two codes = 5, 30 codes.

classref-enumeration-constant

`AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>` **APRIL_TAG_DICT_25H9** = `2`

5 by 5 bits, minimum Hamming distance between any two codes = 9, 35 codes.

classref-enumeration-constant

`AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>` **APRIL_TAG_DICT_36H10** = `3`

6 by 6 bits, minimum Hamming distance between any two codes = 10, 2320 codes.

classref-enumeration-constant

`AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>` **APRIL_TAG_DICT_36H11** = `4`

6 by 6 bits, minimum Hamming distance between any two codes = 11, 587 codes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>` **april_dict** = `4` `🔗<class_OpenXRSpatialCapabilityConfigurationAprilTag_property_april_dict>`

classref-property-setget

- `void (No return value.)` **set_april_dict**(value: `AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>`)
- `AprilTagDict<enum_OpenXRSpatialCapabilityConfigurationAprilTag_AprilTagDict>` **get_april_dict**()

Dictionary to use to decode April tags.

**Note:** Must be set before using this configuration to create a spatial context.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PackedInt64Array<class_PackedInt64Array>` **get_enabled_components**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRSpatialCapabilityConfigurationAprilTag_method_get_enabled_components>`

Returns the components enabled by this configuration.

**Note:** Only valid after this configuration was used to create a spatial context.