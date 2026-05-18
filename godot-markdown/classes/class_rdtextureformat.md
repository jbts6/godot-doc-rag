github_url
hide

# RDTextureFormat

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Texture format (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **array_layers** = `1` `🔗<class_RDTextureFormat_property_array_layers>`

classref-property-setget

- `void (No return value.)` **set_array_layers**(value: `int<class_int>`)
- `int<class_int>` **get_array_layers**()

The number of layers in the texture. Only relevant for 2D texture arrays.

classref-item-separator

classref-property

`int<class_int>` **depth** = `1` `🔗<class_RDTextureFormat_property_depth>`

classref-property-setget

- `void (No return value.)` **set_depth**(value: `int<class_int>`)
- `int<class_int>` **get_depth**()

The texture's depth (in pixels). This is always `1` for 2D textures.

classref-item-separator

classref-property

`DataFormat<enum_RenderingDevice_DataFormat>` **format** = `8` `🔗<class_RDTextureFormat_property_format>`

classref-property-setget

- `void (No return value.)` **set_format**(value: `DataFormat<enum_RenderingDevice_DataFormat>`)
- `DataFormat<enum_RenderingDevice_DataFormat>` **get_format**()

The texture's pixel data format.

classref-item-separator

classref-property

`int<class_int>` **height** = `1` `🔗<class_RDTextureFormat_property_height>`

classref-property-setget

- `void (No return value.)` **set_height**(value: `int<class_int>`)
- `int<class_int>` **get_height**()

The texture's height (in pixels).

classref-item-separator

classref-property

`bool<class_bool>` **is_discardable** = `false` `🔗<class_RDTextureFormat_property_is_discardable>`

classref-property-setget

- `void (No return value.)` **set_is_discardable**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_is_discardable**()

If a texture is discardable, its contents do not need to be preserved between frames. This flag is only relevant when the texture is used as target in a draw list.

This information is used by `RenderingDevice<class_RenderingDevice>` to figure out if a texture's contents can be discarded, eliminating unnecessary writes to memory and boosting performance.

classref-item-separator

classref-property

`bool<class_bool>` **is_resolve_buffer** = `false` `🔗<class_RDTextureFormat_property_is_resolve_buffer>`

classref-property-setget

- `void (No return value.)` **set_is_resolve_buffer**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_is_resolve_buffer**()

The texture will be used as the destination of a resolve operation.

classref-item-separator

classref-property

`int<class_int>` **mipmaps** = `1` `🔗<class_RDTextureFormat_property_mipmaps>`

classref-property-setget

- `void (No return value.)` **set_mipmaps**(value: `int<class_int>`)
- `int<class_int>` **get_mipmaps**()

The number of mipmaps available in the texture.

classref-item-separator

classref-property

`TextureSamples<enum_RenderingDevice_TextureSamples>` **samples** = `0` `🔗<class_RDTextureFormat_property_samples>`

classref-property-setget

- `void (No return value.)` **set_samples**(value: `TextureSamples<enum_RenderingDevice_TextureSamples>`)
- `TextureSamples<enum_RenderingDevice_TextureSamples>` **get_samples**()

The number of samples used when sampling the texture.

classref-item-separator

classref-property

`TextureType<enum_RenderingDevice_TextureType>` **texture_type** = `1` `🔗<class_RDTextureFormat_property_texture_type>`

classref-property-setget

- `void (No return value.)` **set_texture_type**(value: `TextureType<enum_RenderingDevice_TextureType>`)
- `TextureType<enum_RenderingDevice_TextureType>` **get_texture_type**()

The texture type.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`\] **usage_bits** = `0` `🔗<class_RDTextureFormat_property_usage_bits>`

classref-property-setget

- `void (No return value.)` **set_usage_bits**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TextureUsageBits<enum_RenderingDevice_TextureUsageBits>`\] **get_usage_bits**()

The texture's usage bits, which determine what can be done using the texture.

classref-item-separator

classref-property

`int<class_int>` **width** = `1` `🔗<class_RDTextureFormat_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `int<class_int>`)
- `int<class_int>` **get_width**()

The texture's width (in pixels).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_shareable_format**(format: `DataFormat<enum_RenderingDevice_DataFormat>`) `🔗<class_RDTextureFormat_method_add_shareable_format>`

Adds `format` as a valid format for the corresponding `RDTextureView<class_RDTextureView>`'s `RDTextureView.format_override<class_RDTextureView_property_format_override>` property. If any format is added as shareable, then the main `format<class_RDTextureFormat_property_format>` must also be added.

classref-item-separator

classref-method

`void (No return value.)` **remove_shareable_format**(format: `DataFormat<enum_RenderingDevice_DataFormat>`) `🔗<class_RDTextureFormat_method_remove_shareable_format>`

Removes `format` from the list of valid formats that the corresponding `RDTextureView<class_RDTextureView>`'s `RDTextureView.format_override<class_RDTextureView_property_format_override>` property can be set to.