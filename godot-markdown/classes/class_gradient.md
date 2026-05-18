github_url
hide

# Gradient

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A color transition.

classref-introduction-group

## Description

This resource describes a color transition by defining a set of colored points and how to interpolate between them.

See also `Curve<class_Curve>` which supports more complex easing methods, but does not support colors.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **InterpolationMode**: `🔗<enum_Gradient_InterpolationMode>`

classref-enumeration-constant

`InterpolationMode<enum_Gradient_InterpolationMode>` **GRADIENT_INTERPOLATE_LINEAR** = `0`

Linear interpolation.

classref-enumeration-constant

`InterpolationMode<enum_Gradient_InterpolationMode>` **GRADIENT_INTERPOLATE_CONSTANT** = `1`

Constant interpolation, color changes abruptly at each point and stays uniform between. This might cause visible aliasing when used for a gradient texture in some cases.

classref-enumeration-constant

`InterpolationMode<enum_Gradient_InterpolationMode>` **GRADIENT_INTERPOLATE_CUBIC** = `2`

Cubic interpolation.

classref-item-separator

classref-enumeration

enum **ColorSpace**: `🔗<enum_Gradient_ColorSpace>`

classref-enumeration-constant

`ColorSpace<enum_Gradient_ColorSpace>` **GRADIENT_COLOR_SPACE_SRGB** = `0`

sRGB color space.

classref-enumeration-constant

`ColorSpace<enum_Gradient_ColorSpace>` **GRADIENT_COLOR_SPACE_LINEAR_SRGB** = `1`

Linear sRGB color space.

classref-enumeration-constant

`ColorSpace<enum_Gradient_ColorSpace>` **GRADIENT_COLOR_SPACE_OKLAB** = `2`

[Oklab](https://bottosson.github.io/posts/oklab/) color space. This color space provides a smooth and uniform-looking transition between colors.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedColorArray<class_PackedColorArray>` **colors** = `PackedColorArray(0, 0, 0, 1, 1, 1, 1, 1)` `🔗<class_Gradient_property_colors>`

classref-property-setget

- `void (No return value.)` **set_colors**(value: `PackedColorArray<class_PackedColorArray>`)
- `PackedColorArray<class_PackedColorArray>` **get_colors**()

Gradient's colors as a `PackedColorArray<class_PackedColorArray>`.

**Note:** Setting this property updates all colors at once. To update any color individually use `set_color()<class_Gradient_method_set_color>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedColorArray<class_PackedColorArray>` for more details.

classref-item-separator

classref-property

`ColorSpace<enum_Gradient_ColorSpace>` **interpolation_color_space** = `0` `🔗<class_Gradient_property_interpolation_color_space>`

classref-property-setget

- `void (No return value.)` **set_interpolation_color_space**(value: `ColorSpace<enum_Gradient_ColorSpace>`)
- `ColorSpace<enum_Gradient_ColorSpace>` **get_interpolation_color_space**()

The color space used to interpolate between points of the gradient. It does not affect the returned colors, which will always use nonlinear sRGB encoding.

**Note:** This setting has no effect when `interpolation_mode<class_Gradient_property_interpolation_mode>` is set to `GRADIENT_INTERPOLATE_CONSTANT<class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT>`.

classref-item-separator

classref-property

`InterpolationMode<enum_Gradient_InterpolationMode>` **interpolation_mode** = `0` `🔗<class_Gradient_property_interpolation_mode>`

classref-property-setget

- `void (No return value.)` **set_interpolation_mode**(value: `InterpolationMode<enum_Gradient_InterpolationMode>`)
- `InterpolationMode<enum_Gradient_InterpolationMode>` **get_interpolation_mode**()

The algorithm used to interpolate between points of the gradient.

classref-item-separator

classref-property

`PackedFloat32Array<class_PackedFloat32Array>` **offsets** = `PackedFloat32Array(0, 1)` `🔗<class_Gradient_property_offsets>`

classref-property-setget

- `void (No return value.)` **set_offsets**(value: `PackedFloat32Array<class_PackedFloat32Array>`)
- `PackedFloat32Array<class_PackedFloat32Array>` **get_offsets**()

Gradient's offsets as a `PackedFloat32Array<class_PackedFloat32Array>`.

**Note:** Setting this property updates all offsets at once. To update any offset individually use `set_offset()<class_Gradient_method_set_offset>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedFloat32Array<class_PackedFloat32Array>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_point**(offset: `float<class_float>`, color: `Color<class_Color>`) `🔗<class_Gradient_method_add_point>`

Adds the specified color to the gradient, with the specified offset.

classref-item-separator

classref-method

`Color<class_Color>` **get_color**(point: `int<class_int>`) `🔗<class_Gradient_method_get_color>`

Returns the color of the gradient color at index `point`.

classref-item-separator

classref-method

`float<class_float>` **get_offset**(point: `int<class_int>`) `🔗<class_Gradient_method_get_offset>`

Returns the offset of the gradient color at index `point`.

classref-item-separator

classref-method

`int<class_int>` **get_point_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Gradient_method_get_point_count>`

Returns the number of colors in the gradient.

classref-item-separator

classref-method

`void (No return value.)` **remove_point**(point: `int<class_int>`) `🔗<class_Gradient_method_remove_point>`

Removes the color at index `point`.

classref-item-separator

classref-method

`void (No return value.)` **reverse**() `🔗<class_Gradient_method_reverse>`

Reverses/mirrors the gradient.

**Note:** This method mirrors all points around the middle of the gradient, which may produce unexpected results when `interpolation_mode<class_Gradient_property_interpolation_mode>` is set to `GRADIENT_INTERPOLATE_CONSTANT<class_Gradient_constant_GRADIENT_INTERPOLATE_CONSTANT>`.

classref-item-separator

classref-method

`Color<class_Color>` **sample**(offset: `float<class_float>`) `🔗<class_Gradient_method_sample>`

Returns the interpolated color specified by `offset`. `offset` should be between `0.0` and `1.0` (inclusive). Using a value lower than `0.0` will return the same color as `0.0`, and using a value higher than `1.0` will return the same color as `1.0`. If your input value is not within this range, consider using `@GlobalScope.remap()<class_@GlobalScope_method_remap>` on the input value with output values set to `0.0` and `1.0`.

classref-item-separator

classref-method

`void (No return value.)` **set_color**(point: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_Gradient_method_set_color>`

Sets the color of the gradient color at index `point`.

classref-item-separator

classref-method

`void (No return value.)` **set_offset**(point: `int<class_int>`, offset: `float<class_float>`) `🔗<class_Gradient_method_set_offset>`

Sets the offset for the gradient color at index `point`.