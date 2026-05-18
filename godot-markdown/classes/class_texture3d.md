github_url
hide

# Texture3D

**Inherits:** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `CompressedTexture3D<class_CompressedTexture3D>`, `ImageTexture3D<class_ImageTexture3D>`, `NoiseTexture3D<class_NoiseTexture3D>`, `PlaceholderTexture3D<class_PlaceholderTexture3D>`, `Texture3DRD<class_Texture3DRD>`

Base class for 3-dimensional textures.

classref-introduction-group

## Description

Base class for `ImageTexture3D<class_ImageTexture3D>` and `CompressedTexture3D<class_CompressedTexture3D>`. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types. **Texture3D** is the base class for all 3-dimensional texture types. See also `TextureLayered<class_TextureLayered>`.

All images need to have the same width, height and number of mipmap levels.

To create such a texture file yourself, reimport your image files using the Godot Editor import presets.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Array<class_Array>`\[`Image<class_Image>`\] **\_get_data**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_private_method__get_data>`

Called when the **Texture3D**'s data is queried.

classref-item-separator

classref-method

`int<class_int>` **\_get_depth**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_private_method__get_depth>`

Called when the **Texture3D**'s depth is queried.

classref-item-separator

classref-method

`Format<enum_Image_Format>` **\_get_format**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_private_method__get_format>`

Called when the **Texture3D**'s format is queried.

classref-item-separator

classref-method

`int<class_int>` **\_get_height**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_private_method__get_height>`

Called when the **Texture3D**'s height is queried.

classref-item-separator

classref-method

`int<class_int>` **\_get_width**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_private_method__get_width>`

Called when the **Texture3D**'s width is queried.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_mipmaps**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_private_method__has_mipmaps>`

Called when the presence of mipmaps in the **Texture3D** is queried.

classref-item-separator

classref-method

`Resource<class_Resource>` **create_placeholder**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_create_placeholder>`

Creates a placeholder version of this resource (`PlaceholderTexture3D<class_PlaceholderTexture3D>`).

classref-item-separator

classref-method

`Array<class_Array>`\[`Image<class_Image>`\] **get_data**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_get_data>`

Returns the **Texture3D**'s data as an array of `Image<class_Image>`s. Each `Image<class_Image>` represents a *slice* of the **Texture3D**, with different slices mapping to different depth (Z axis) levels.

classref-item-separator

classref-method

`int<class_int>` **get_depth**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_get_depth>`

Returns the **Texture3D**'s depth in pixels. Depth is typically represented by the Z axis (a dimension not present in `Texture2D<class_Texture2D>`).

classref-item-separator

classref-method

`Format<enum_Image_Format>` **get_format**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_get_format>`

Returns the current format being used by this texture.

classref-item-separator

classref-method

`int<class_int>` **get_height**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_get_height>`

Returns the **Texture3D**'s height in pixels. Width is typically represented by the Y axis.

classref-item-separator

classref-method

`int<class_int>` **get_width**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_get_width>`

Returns the **Texture3D**'s width in pixels. Width is typically represented by the X axis.

classref-item-separator

classref-method

`bool<class_bool>` **has_mipmaps**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture3D_method_has_mipmaps>`

Returns `true` if the **Texture3D** has generated mipmaps.