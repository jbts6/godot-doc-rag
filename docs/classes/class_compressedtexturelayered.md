github_url
hide

# CompressedTextureLayered

**Inherits:** `TextureLayered<class_TextureLayered>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `CompressedCubemap<class_CompressedCubemap>`, `CompressedCubemapArray<class_CompressedCubemapArray>`, `CompressedTexture2DArray<class_CompressedTexture2DArray>`

Base class for texture arrays that can optionally be compressed.

classref-introduction-group

## Description

Base class for `CompressedTexture2DArray<class_CompressedTexture2DArray>` and `CompressedTexture3D<class_CompressedTexture3D>`. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. See also `TextureLayered<class_TextureLayered>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **load_path** = `""` `🔗<class_CompressedTextureLayered_property_load_path>`

classref-property-setget

- `Error<enum_@GlobalScope_Error>` **load**(path: `String<class_String>`)
- `String<class_String>` **get_load_path**()

The path the texture should be loaded from.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Error<enum_@GlobalScope_Error>` **load**(path: `String<class_String>`) `🔗<class_CompressedTextureLayered_method_load>`

Loads the texture at `path`.