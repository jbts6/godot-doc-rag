github_url
hide

# DPITexture

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

An automatically scalable `Texture2D<class_Texture2D>` based on an SVG image.

classref-introduction-group

## Description

An automatically scalable `Texture2D<class_Texture2D>` based on an SVG image. **DPITexture**s are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See also `ProjectSettings.display/window/stretch/mode<class_ProjectSettings_property_display/window/stretch/mode>` ("canvas_items" mode) and `Viewport.oversampling_override<class_Viewport_property_oversampling_override>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **base_scale** = `1.0` `🔗<class_DPITexture_property_base_scale>`

classref-property-setget

- `void (No return value.)` **set_base_scale**(value: `float<class_float>`)
- `float<class_float>` **get_base_scale**()

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **color_map** = `{}` `🔗<class_DPITexture_property_color_map>`

classref-property-setget

- `void (No return value.)` **set_color_map**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_color_map**()

If set, remaps texture colors according to `Color<class_Color>`-`Color<class_Color>` map.

classref-item-separator

classref-property

`bool<class_bool>` **fix_alpha_border** = `false` `🔗<class_DPITexture_property_fix_alpha_border>`

classref-property-setget

- `void (No return value.)` **set_fix_alpha_border**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_fix_alpha_border**()

If `true`, puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps to reduce the outline effect when exporting images from an image editor.

classref-item-separator

classref-property

`bool<class_bool>` **premult_alpha** = `false` `🔗<class_DPITexture_property_premult_alpha>`

classref-property-setget

- `void (No return value.)` **set_premult_alpha**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_premult_alpha**()

An alternative to fixing darkened borders with `fix_alpha_border<class_DPITexture_property_fix_alpha_border>` is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a `CanvasItemMaterial<class_CanvasItemMaterial>` will need to be created and configured to use the `CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA<class_CanvasItemMaterial_constant_BLEND_MODE_PREMULT_ALPHA>` blend mode on `CanvasItem<class_CanvasItem>`s that use this texture. In custom `canvas_item` shaders, `render_mode blend_premul_alpha;` should be used.
- In 3D, a `BaseMaterial3D<class_BaseMaterial3D>` will need to be created and configured to use the `BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA<class_BaseMaterial3D_constant_BLEND_MODE_PREMULT_ALPHA>` blend mode on materials that use this texture. In custom `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

classref-item-separator

classref-property

`float<class_float>` **saturation** = `1.0` `🔗<class_DPITexture_property_saturation>`

classref-property-setget

- `void (No return value.)` **set_saturation**(value: `float<class_float>`)
- `float<class_float>` **get_saturation**()

Overrides texture saturation.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`DPITexture<class_DPITexture>` **create_from_string**(source: `String<class_String>`, scale: `float<class_float>` = 1.0, saturation: `float<class_float>` = 1.0, color_map: `Dictionary<class_Dictionary>` = {}) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_DPITexture_method_create_from_string>`

Creates a new **DPITexture** and initializes it by allocating and setting the SVG data to `source`.

classref-item-separator

classref-method

`RID<class_RID>` **get_scaled_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_DPITexture_method_get_scaled_rid>`

Returns the `RID<class_RID>` of the texture rasterized to match the oversampling of the currently drawn canvas item.

classref-item-separator

classref-method

`String<class_String>` **get_source**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_DPITexture_method_get_source>`

Returns this SVG texture's source code.

classref-item-separator

classref-method

`void (No return value.)` **set_size_override**(size: `Vector2i<class_Vector2i>`) `🔗<class_DPITexture_method_set_size_override>`

Resizes the texture to the specified dimensions.

classref-item-separator

classref-method

`void (No return value.)` **set_source**(source: `String<class_String>`) `🔗<class_DPITexture_method_set_source>`

Sets this SVG texture's source code.