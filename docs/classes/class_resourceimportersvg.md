github_url
hide

# ResourceImporterSVG

**Inherits:** `ResourceImporter<class_ResourceImporter>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Imports an SVG file as an automatically scalable texture for use in UI elements and 2D rendering.

classref-introduction-group

## Description

This importer imports `DPITexture<class_DPITexture>` resources. See also `ResourceImporterTexture<class_ResourceImporterTexture>` and `ResourceImporterImage<class_ResourceImporterImage>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **base_scale** = `1.0` `🔗<class_ResourceImporterSVG_property_base_scale>`

Texture scale. `1.0` is the original SVG size. Higher values result in a larger image.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **color_map** = `{}` `🔗<class_ResourceImporterSVG_property_color_map>`

If set, remaps texture colors according to `Color<class_Color>`-`Color<class_Color>` map.

classref-item-separator

classref-property

`bool<class_bool>` **compress** = `true` `🔗<class_ResourceImporterSVG_property_compress>`

If `true`, uses lossless compression for the SVG source.

classref-item-separator

classref-property

`bool<class_bool>` **fix_alpha_border** = `false` `🔗<class_ResourceImporterSVG_property_fix_alpha_border>`

If `true`, puts pixels of the same surrounding color in transition from transparent to opaque areas. For textures displayed with bilinear filtering, this helps to reduce the outline effect when exporting images from an image editor.

classref-item-separator

classref-property

`bool<class_bool>` **premult_alpha** = `false` `🔗<class_ResourceImporterSVG_property_premult_alpha>`

An alternative to fixing darkened borders with `fix_alpha_border<class_ResourceImporterSVG_property_fix_alpha_border>` is to use premultiplied alpha. By enabling this option, the texture will be converted to this format. A premultiplied alpha texture requires specific materials to be displayed correctly:

- In 2D, a `CanvasItemMaterial<class_CanvasItemMaterial>` will need to be created and configured to use the `CanvasItemMaterial.BLEND_MODE_PREMULT_ALPHA<class_CanvasItemMaterial_constant_BLEND_MODE_PREMULT_ALPHA>` blend mode on `CanvasItem<class_CanvasItem>`s that use this texture. In custom `canvas_item` shaders, `render_mode blend_premul_alpha;` should be used.
- In 3D, a `BaseMaterial3D<class_BaseMaterial3D>` will need to be created and configured to use the `BaseMaterial3D.BLEND_MODE_PREMULT_ALPHA<class_BaseMaterial3D_constant_BLEND_MODE_PREMULT_ALPHA>` blend mode on materials that use this texture. In custom `spatial` shaders, `render_mode blend_premul_alpha;` should be used.

classref-item-separator

classref-property

`float<class_float>` **saturation** = `1.0` `🔗<class_ResourceImporterSVG_property_saturation>`

Overrides texture saturation.