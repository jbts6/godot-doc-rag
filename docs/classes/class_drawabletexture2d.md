github_url
hide

# DrawableTexture2D

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 2D texture that supports drawing to itself via Blit calls.

classref-introduction-group

## Description

A 2D texture that can be modified via blit calls, copying from a target texture to itself. Primarily intended to be managed in code, a user must call `setup()<class_DrawableTexture2D_method_setup>` to initialize the state before drawing. Each `blit_rect()<class_DrawableTexture2D_method_blit_rect>` call takes at least a rectangle, the area to draw to, and another texture, what to be drawn. The draw calls use a Texture_Blit Shader to process and calculate the result, pixel by pixel. Users can supply their own ShaderMaterial with custom Texture_Blit shaders for more complex behaviors.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DrawableFormat**: `🔗<enum_DrawableTexture2D_DrawableFormat>`

classref-enumeration-constant

`DrawableFormat<enum_DrawableTexture2D_DrawableFormat>` **DRAWABLE_FORMAT_RGBA8** = `0`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

classref-enumeration-constant

`DrawableFormat<enum_DrawableTexture2D_DrawableFormat>` **DRAWABLE_FORMAT_RGBA8_SRGB** = `1`

OpenGL texture format RGBA with four components, each with a bitdepth of 8.

When drawn to, an sRGB to linear color space conversion is performed.

classref-enumeration-constant

`DrawableFormat<enum_DrawableTexture2D_DrawableFormat>` **DRAWABLE_FORMAT_RGBAH** = `2`

OpenGL texture format GL_RGBA16F where there are four components, each a 16-bit "half-precision" floating-point value.

classref-enumeration-constant

`DrawableFormat<enum_DrawableTexture2D_DrawableFormat>` **DRAWABLE_FORMAT_RGBAF** = `3`

OpenGL texture format GL_RGBA32F where there are four components, each a 32-bit floating-point value.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **blit_rect**(rect: `Rect2i<class_Rect2i>`, source: `Texture2D<class_Texture2D>`, modulate: `Color<class_Color>` = Color(1, 1, 1, 1), mipmap: `int<class_int>` = 0, material: `Material<class_Material>` = null) `🔗<class_DrawableTexture2D_method_blit_rect>`

**Experimental:** This function and its parameters are likely to change in the 4.7 Dev Cycle

Draws to given `rect` on this texture by copying from the given `source`. A `modulate` color can be passed in for the shader to use, but defaults to White. The `mipmap` value can specify a draw to a lower mipmap level. The `material` parameter can take a ShaderMaterial with a TextureBlit Shader for custom drawing behavior.

classref-item-separator

classref-method

`void (No return value.)` **blit_rect_multi**(rect: `Rect2i<class_Rect2i>`, sources: `Array<class_Array>`\[`Texture2D<class_Texture2D>`\], extra_targets: `Array<class_Array>`\[`DrawableTexture2D<class_DrawableTexture2D>`\], modulate: `Color<class_Color>` = Color(1, 1, 1, 1), mipmap: `int<class_int>` = 0, material: `Material<class_Material>` = null) `🔗<class_DrawableTexture2D_method_blit_rect_multi>`

**Experimental:** This function and its parameters are likely to change in the 4.7 Dev Cycle

Draws to the given `rect` on this texture, as well as on up to 3 DrawableTexture `extra_targets`. All `extra_targets` must be the same size and DrawableFormat as the original target, otherwise the Shader may fail. Expects up to 4 Texture `sources`, but will replace missing `sources` with default Black Textures.

classref-item-separator

classref-method

`void (No return value.)` **generate_mipmaps**() `🔗<class_DrawableTexture2D_method_generate_mipmaps>`

Re-calculates the mipmaps for this texture on demand.

classref-item-separator

classref-method

`bool<class_bool>` **get_use_mipmaps**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_DrawableTexture2D_method_get_use_mipmaps>`

Returns `true` if mipmaps are set to be used on this DrawableTexture.

classref-item-separator

classref-method

`void (No return value.)` **set_format**(format: `DrawableFormat<enum_DrawableTexture2D_DrawableFormat>`) `🔗<class_DrawableTexture2D_method_set_format>`

Sets the format of this DrawableTexture.

classref-item-separator

classref-method

`void (No return value.)` **set_use_mipmaps**(mipmaps: `bool<class_bool>`) `🔗<class_DrawableTexture2D_method_set_use_mipmaps>`

Sets if mipmaps should be used on this DrawableTexture.

classref-item-separator

classref-method

`void (No return value.)` **setup**(width: `int<class_int>`, height: `int<class_int>`, format: `DrawableFormat<enum_DrawableTexture2D_DrawableFormat>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), use_mipmaps: `bool<class_bool>` = false) `🔗<class_DrawableTexture2D_method_setup>`

**Experimental:** This function and its parameters are likely to change in the 4.7 Dev Cycle

Initializes the DrawableTexture to a White texture of the given `width`, `height`, and `format`.