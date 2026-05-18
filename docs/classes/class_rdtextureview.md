github_url
hide

# RDTextureView

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Texture view (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`DataFormat<enum_RenderingDevice_DataFormat>` **format_override** = `232` `🔗<class_RDTextureView_property_format_override>`

classref-property-setget

- `void (No return value.)` **set_format_override**(value: `DataFormat<enum_RenderingDevice_DataFormat>`)
- `DataFormat<enum_RenderingDevice_DataFormat>` **get_format_override**()

Optional override for the data format to return sampled values in. The corresponding `RDTextureFormat<class_RDTextureFormat>` must have had this added as a shareable format. The default value of `RenderingDevice.DATA_FORMAT_MAX<class_RenderingDevice_constant_DATA_FORMAT_MAX>` does not override the format.

classref-item-separator

classref-property

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **swizzle_a** = `6` `🔗<class_RDTextureView_property_swizzle_a>`

classref-property-setget

- `void (No return value.)` **set_swizzle_a**(value: `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`)
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **get_swizzle_a**()

The channel to sample when sampling the alpha channel.

classref-item-separator

classref-property

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **swizzle_b** = `5` `🔗<class_RDTextureView_property_swizzle_b>`

classref-property-setget

- `void (No return value.)` **set_swizzle_b**(value: `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`)
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **get_swizzle_b**()

The channel to sample when sampling the blue color channel.

classref-item-separator

classref-property

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **swizzle_g** = `4` `🔗<class_RDTextureView_property_swizzle_g>`

classref-property-setget

- `void (No return value.)` **set_swizzle_g**(value: `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`)
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **get_swizzle_g**()

The channel to sample when sampling the green color channel.

classref-item-separator

classref-property

`TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **swizzle_r** = `3` `🔗<class_RDTextureView_property_swizzle_r>`

classref-property-setget

- `void (No return value.)` **set_swizzle_r**(value: `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>`)
- `TextureSwizzle<enum_RenderingDevice_TextureSwizzle>` **get_swizzle_r**()

The channel to sample when sampling the red color channel.