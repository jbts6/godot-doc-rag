github_url
hide

# GLTFTextureSampler

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a glTF texture sampler

classref-introduction-group

## Description

Represents a texture sampler as defined by the base glTF spec. Texture samplers in glTF specify how to sample data from the texture's base image, when rendering the texture on an object.

classref-introduction-group

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **mag_filter** = `9729` `🔗<class_GLTFTextureSampler_property_mag_filter>`

classref-property-setget

- `void (No return value.)` **set_mag_filter**(value: `int<class_int>`)
- `int<class_int>` **get_mag_filter**()

Texture's magnification filter, used when texture appears larger on screen than the source image.

classref-item-separator

classref-property

`int<class_int>` **min_filter** = `9987` `🔗<class_GLTFTextureSampler_property_min_filter>`

classref-property-setget

- `void (No return value.)` **set_min_filter**(value: `int<class_int>`)
- `int<class_int>` **get_min_filter**()

Texture's minification filter, used when the texture appears smaller on screen than the source image.

classref-item-separator

classref-property

`int<class_int>` **wrap_s** = `10497` `🔗<class_GLTFTextureSampler_property_wrap_s>`

classref-property-setget

- `void (No return value.)` **set_wrap_s**(value: `int<class_int>`)
- `int<class_int>` **get_wrap_s**()

Wrapping mode to use for S-axis (horizontal) texture coordinates.

classref-item-separator

classref-property

`int<class_int>` **wrap_t** = `10497` `🔗<class_GLTFTextureSampler_property_wrap_t>`

classref-property-setget

- `void (No return value.)` **set_wrap_t**(value: `int<class_int>`)
- `int<class_int>` **get_wrap_t**()

Wrapping mode to use for T-axis (vertical) texture coordinates.