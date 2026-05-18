github_url
hide

# GradientTexture1D

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 1D texture that uses colors obtained from a `Gradient<class_Gradient>`.

classref-introduction-group

## Description

A 1D texture that obtains colors from a `Gradient<class_Gradient>` to fill the texture data. The texture is filled by sampling the gradient for each pixel. Therefore, the texture does not necessarily represent an exact copy of the gradient, as it may miss some colors if there are not enough pixels. See also `GradientTexture2D<class_GradientTexture2D>`, `CurveTexture<class_CurveTexture>` and `CurveXYZTexture<class_CurveXYZTexture>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Gradient<class_Gradient>` **gradient** `🔗<class_GradientTexture1D_property_gradient>`

classref-property-setget

- `void (No return value.)` **set_gradient**(value: `Gradient<class_Gradient>`)
- `Gradient<class_Gradient>` **get_gradient**()

The `Gradient<class_Gradient>` used to fill the texture.

classref-item-separator

classref-property

`bool<class_bool>` **use_hdr** = `false` `🔗<class_GradientTexture1D_property_use_hdr>`

classref-property-setget

- `void (No return value.)` **set_use_hdr**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_hdr**()

If `true`, the generated texture will support high dynamic range (`Image.FORMAT_RGBAF<class_Image_constant_FORMAT_RGBAF>` format). This allows for glow effects to work if `Environment.glow_enabled<class_Environment_property_glow_enabled>` is `true`. If `false`, the generated texture will use low dynamic range; overbright colors will be clamped (`Image.FORMAT_RGBA8<class_Image_constant_FORMAT_RGBA8>` format).

classref-item-separator

classref-property

`int<class_int>` **width** = `256` `🔗<class_GradientTexture1D_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `int<class_int>`)
- `int<class_int>` **get_width**()

The number of color samples that will be obtained from the `Gradient<class_Gradient>`.