github_url
hide

# PortableCompressedTexture2D

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Provides a compressed texture for disk and/or VRAM in a way that is portable.

classref-introduction-group

## Description

This class allows storing compressed textures as self contained (not imported) resources.

For 2D usage (compressed on disk, uncompressed on VRAM), the lossy and lossless modes are recommended. For 3D usage (compressed on VRAM) it depends on the target platform.

If you intend to only use desktop, S3TC or BPTC are recommended. For only mobile, ETC2 is recommended.

For portable, self contained 3D textures that work on both desktop and mobile, Basis Universal is recommended (although it has a small quality cost and longer compression time as a tradeoff).

This resource is intended to be created from code.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **CompressionMode**: `🔗<enum_PortableCompressedTexture2D_CompressionMode>`

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_LOSSLESS** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_LOSSY** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_BASIS_UNIVERSAL** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_S3TC** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_ETC2** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_BPTC** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **COMPRESSION_MODE_ASTC** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **keep_compressed_buffer** = `false` `🔗<class_PortableCompressedTexture2D_property_keep_compressed_buffer>`

classref-property-setget

- `void (No return value.)` **set_keep_compressed_buffer**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_keeping_compressed_buffer**()

If `true`, when running in the editor, this texture will keep the source-compressed data in memory, allowing the data to persist after loading. Otherwise, the source-compressed data is lost after loading and the texture can't be re-saved.

**Note:** This property must be set before `create_from_image()<class_PortableCompressedTexture2D_method_create_from_image>` for this to work.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **size_override** = `Vector2(0, 0)` `🔗<class_PortableCompressedTexture2D_property_size_override>`

classref-property-setget

- `void (No return value.)` **set_size_override**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_size_override**()

Allows overriding the texture's size (for 2D only).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **create_from_image**(image: `Image<class_Image>`, compression_mode: `CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>`, normal_map: `bool<class_bool>` = false, lossy_quality: `float<class_float>` = 0.8) `🔗<class_PortableCompressedTexture2D_method_create_from_image>`

Initializes the compressed texture from a base image. The compression mode must be provided.

`normal_map` is recommended to ensure optimum quality if this image will be used as a normal map.

If lossy compression is requested, the quality setting can optionally be provided. This maps to Lossy WebP compression quality.

classref-item-separator

classref-method

`CompressionMode<enum_PortableCompressedTexture2D_CompressionMode>` **get_compression_mode**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PortableCompressedTexture2D_method_get_compression_mode>`

Return the compression mode used (valid after initialized).

classref-item-separator

classref-method

`bool<class_bool>` **is_keeping_all_compressed_buffers**() `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_PortableCompressedTexture2D_method_is_keeping_all_compressed_buffers>`

Returns `true` if the flag is overridden for all textures of this type.

classref-item-separator

classref-method

`void (No return value.)` **set_basisu_compressor_params**(uastc_level: `int<class_int>`, rdo_quality_loss: `float<class_float>`) `🔗<class_PortableCompressedTexture2D_method_set_basisu_compressor_params>`

Sets the compressor parameters for Basis Universal compression. See also the settings in `ResourceImporterTexture<class_ResourceImporterTexture>`.

**Note:** This method must be called before `create_from_image()<class_PortableCompressedTexture2D_method_create_from_image>` for this to work.

classref-item-separator

classref-method

`void (No return value.)` **set_keep_all_compressed_buffers**(keep: `bool<class_bool>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_PortableCompressedTexture2D_method_set_keep_all_compressed_buffers>`

If `keep` is `true`, overrides the flag globally for all textures of this type. This is used primarily by the editor.