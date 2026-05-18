github_url
hide

# ResourceImporterBitMap

**Inherits:** `ResourceImporter<class_ResourceImporter>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Imports a `BitMap<class_BitMap>` resource (2D array of boolean values).

classref-introduction-group

## Description

`BitMap<class_BitMap>` resources are typically used as click masks in `TextureButton<class_TextureButton>` and `TouchScreenButton<class_TouchScreenButton>`.

classref-introduction-group

## Tutorials

- `Importing images <../tutorials/assets_pipeline/importing_images>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **create_from** = `0` `🔗<class_ResourceImporterBitMap_property_create_from>`

The data source to use for generating the bitmap.

**Black & White:** Pixels whose HSV value is greater than the `threshold<class_ResourceImporterBitMap_property_threshold>` will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

**Alpha:** Pixels whose alpha value is greater than the `threshold<class_ResourceImporterBitMap_property_threshold>` will be considered as "enabled" (bit is `true`). If the pixel is lower than or equal to the threshold, it will be considered as "disabled" (bit is `false`).

classref-item-separator

classref-property

`float<class_float>` **threshold** = `0.5` `🔗<class_ResourceImporterBitMap_property_threshold>`

The threshold to use to determine which bits should be considered enabled or disabled. See also `create_from<class_ResourceImporterBitMap_property_create_from>`.