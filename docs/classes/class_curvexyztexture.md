github_url
hide

# CurveXYZTexture

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 1D texture where the red, green, and blue color channels correspond to points on 3 curves.

classref-introduction-group

## Description

A 1D texture where the red, green, and blue color channels correspond to points on 3 unit `Curve<class_Curve>` resources. Compared to using separate `CurveTexture<class_CurveTexture>`s, this further simplifies the task of saving curves as image files.

If you only need to store one curve within a single texture, use `CurveTexture<class_CurveTexture>` instead. See also `GradientTexture1D<class_GradientTexture1D>` and `GradientTexture2D<class_GradientTexture2D>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Curve<class_Curve>` **curve_x** `🔗<class_CurveXYZTexture_property_curve_x>`

classref-property-setget

- `void (No return value.)` **set_curve_x**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_curve_x**()

The `Curve<class_Curve>` that is rendered onto the texture's red channel. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`Curve<class_Curve>` **curve_y** `🔗<class_CurveXYZTexture_property_curve_y>`

classref-property-setget

- `void (No return value.)` **set_curve_y**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_curve_y**()

The `Curve<class_Curve>` that is rendered onto the texture's green channel. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`Curve<class_Curve>` **curve_z** `🔗<class_CurveXYZTexture_property_curve_z>`

classref-property-setget

- `void (No return value.)` **set_curve_z**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_curve_z**()

The `Curve<class_Curve>` that is rendered onto the texture's blue channel. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`int<class_int>` **width** = `256` `🔗<class_CurveXYZTexture_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `int<class_int>`)
- `int<class_int>` **get_width**()

The width of the texture (in pixels). Higher values make it possible to represent high-frequency data better (such as sudden direction changes), at the cost of increased generation time and memory usage.