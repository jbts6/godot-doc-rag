github_url
hide

# FontFile

**Inherits:** `Font<class_Font>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Holds font source data and prerendered glyph cache, imported from a dynamic or a bitmap font.

classref-introduction-group

## Description

**FontFile** contains a set of glyphs to represent Unicode characters imported from a font file, as well as a cache of rasterized glyphs, and a set of fallback `Font<class_Font>`s to use.

Use `FontVariation<class_FontVariation>` to access specific OpenType variation of the font, create simulated bold / slanted version, and draw lines of text.

For more complex text processing, use `FontVariation<class_FontVariation>` in conjunction with `TextLine<class_TextLine>` or `TextParagraph<class_TextParagraph>`.

Supported font formats:

- Dynamic font importer: TrueType (.ttf), TrueType collection (.ttc), OpenType (.otf), OpenType collection (.otc), WOFF (.woff), WOFF2 (.woff2), Type 1 (.pfb, .pfm).
- Bitmap font importer: AngelCode BMFont (.fnt, .font), text and binary (version 3) format variants.
- Monospace image font importer: All supported image formats.

**Note:** A character is a symbol that represents an item (letter, digit etc.) in an abstract way.

**Note:** A glyph is a bitmap or a shape used to draw one or more characters in a context-dependent manner. Glyph indices are bound to the specific font data source.

**Note:** If none of the font data sources contain glyphs for a character used in a string, the character in question will be replaced with a box displaying its hexadecimal code.

gdscript

var f = load("res://BarlowCondensed-Bold.ttf") \$Label.add_theme_font_override("font", f) \$Label.add_theme_font_size_override("font_size", 64)

csharp

var f = ResourceLoader.Load\<FontFile\>("res://BarlowCondensed-Bold.ttf"); GetNode("Label").AddThemeFontOverride("font", f); GetNode("Label").AddThemeFontSizeOverride("font_size", 64);

classref-introduction-group

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **allow_system_fallback** = `true` `🔗<class_FontFile_property_allow_system_fallback>`

classref-property-setget

- `void (No return value.)` **set_allow_system_fallback**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_allow_system_fallback**()

If set to `true`, system fonts can be automatically used as fallbacks.

classref-item-separator

classref-property

`FontAntialiasing<enum_TextServer_FontAntialiasing>` **antialiasing** = `1` `🔗<class_FontFile_property_antialiasing>`

classref-property-setget

- `void (No return value.)` **set_antialiasing**(value: `FontAntialiasing<enum_TextServer_FontAntialiasing>`)
- `FontAntialiasing<enum_TextServer_FontAntialiasing>` **get_antialiasing**()

Font anti-aliasing mode.

classref-item-separator

classref-property

`PackedByteArray<class_PackedByteArray>` **data** = `PackedByteArray()` `🔗<class_FontFile_property_data>`

classref-property-setget

- `void (No return value.)` **set_data**(value: `PackedByteArray<class_PackedByteArray>`)
- `PackedByteArray<class_PackedByteArray>` **get_data**()

Contents of the dynamic font source file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedByteArray<class_PackedByteArray>` for more details.

classref-item-separator

classref-property

`bool<class_bool>` **disable_embedded_bitmaps** = `true` `🔗<class_FontFile_property_disable_embedded_bitmaps>`

classref-property-setget

- `void (No return value.)` **set_disable_embedded_bitmaps**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_disable_embedded_bitmaps**()

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

classref-item-separator

classref-property

`int<class_int>` **fixed_size** = `0` `🔗<class_FontFile_property_fixed_size>`

classref-property-setget

- `void (No return value.)` **set_fixed_size**(value: `int<class_int>`)
- `int<class_int>` **get_fixed_size**()

Font size, used only for the bitmap fonts.

classref-item-separator

classref-property

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **fixed_size_scale_mode** = `0` `🔗<class_FontFile_property_fixed_size_scale_mode>`

classref-property-setget

- `void (No return value.)` **set_fixed_size_scale_mode**(value: `FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`)
- `FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **get_fixed_size_scale_mode**()

Scaling mode, used only for the bitmap fonts with `fixed_size<class_FontFile_property_fixed_size>` greater than zero.

classref-item-separator

classref-property

`String<class_String>` **font_name** = `""` `🔗<class_FontFile_property_font_name>`

classref-property-setget

- `void (No return value.)` **set_font_name**(value: `String<class_String>`)
- `String<class_String>` **get_font_name**()

Font family name.

classref-item-separator

classref-property

`int<class_int>` **font_stretch** = `100` `🔗<class_FontFile_property_font_stretch>`

classref-property-setget

- `void (No return value.)` **set_font_stretch**(value: `int<class_int>`)
- `int<class_int>` **get_font_stretch**()

Font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\] **font_style** = `0` `🔗<class_FontFile_property_font_style>`

classref-property-setget

- `void (No return value.)` **set_font_style**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\] **get_font_style**()

Font style flags.

classref-item-separator

classref-property

`int<class_int>` **font_weight** = `400` `🔗<class_FontFile_property_font_weight>`

classref-property-setget

- `void (No return value.)` **set_font_weight**(value: `int<class_int>`)
- `int<class_int>` **get_font_weight**()

Weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

classref-item-separator

classref-property

`bool<class_bool>` **force_autohinter** = `false` `🔗<class_FontFile_property_force_autohinter>`

classref-property-setget

- `void (No return value.)` **set_force_autohinter**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_force_autohinter**()

If set to `true`, auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only (MSDF fonts don't support hinting).

classref-item-separator

classref-property

`bool<class_bool>` **generate_mipmaps** = `false` `🔗<class_FontFile_property_generate_mipmaps>`

classref-property-setget

- `void (No return value.)` **set_generate_mipmaps**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_generate_mipmaps**()

If set to `true`, generate mipmaps for the font textures.

classref-item-separator

classref-property

`Hinting<enum_TextServer_Hinting>` **hinting** = `1` `🔗<class_FontFile_property_hinting>`

classref-property-setget

- `void (No return value.)` **set_hinting**(value: `Hinting<enum_TextServer_Hinting>`)
- `Hinting<enum_TextServer_Hinting>` **get_hinting**()

Font hinting mode. Used by dynamic fonts only.

classref-item-separator

classref-property

`bool<class_bool>` **keep_rounding_remainders** = `true` `🔗<class_FontFile_property_keep_rounding_remainders>`

classref-property-setget

- `void (No return value.)` **set_keep_rounding_remainders**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_keep_rounding_remainders**()

If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

classref-item-separator

classref-property

`bool<class_bool>` **modulate_color_glyphs** = `false` `🔗<class_FontFile_property_modulate_color_glyphs>`

classref-property-setget

- `void (No return value.)` **set_modulate_color_glyphs**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_modulate_color_glyphs**()

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

classref-item-separator

classref-property

`int<class_int>` **msdf_pixel_range** = `16` `🔗<class_FontFile_property_msdf_pixel_range>`

classref-property-setget

- `void (No return value.)` **set_msdf_pixel_range**(value: `int<class_int>`)
- `int<class_int>` **get_msdf_pixel_range**()

The width of the range around the shape between the minimum and maximum representable signed distance. If using font outlines, `msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the size of the largest font outline. The default `msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` value of `16` allows outline sizes up to `8` to look correct.

classref-item-separator

classref-property

`int<class_int>` **msdf_size** = `48` `🔗<class_FontFile_property_msdf_size>`

classref-property-setget

- `void (No return value.)` **set_msdf_size**(value: `int<class_int>`)
- `int<class_int>` **get_msdf_size**()

Source font size used to generate MSDF textures. Higher values allow for more precision, but are slower to render and require more memory. Only increase this value if you notice a visible lack of precision in glyph rendering.

classref-item-separator

classref-property

`bool<class_bool>` **multichannel_signed_distance_field** = `false` `🔗<class_FontFile_property_multichannel_signed_distance_field>`

classref-property-setget

- `void (No return value.)` **set_multichannel_signed_distance_field**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_multichannel_signed_distance_field**()

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field (MSDF) generated from the dynamic font vector data. Since this approach does not rely on rasterizing the font every time its size changes, this allows for resizing the font in real-time without any performance penalty. Text will also not look grainy for `Control<class_Control>`s that are scaled down (or for `Label3D<class_Label3D>`s viewed from a long distance). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

**Note:** If using font outlines, `msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the size of the largest font outline.

**Note:** MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **opentype_feature_overrides** = `{}` `🔗<class_FontFile_property_opentype_feature_overrides>`

classref-property-setget

- `void (No return value.)` **set_opentype_feature_overrides**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_opentype_feature_overrides**()

Font OpenType feature set override.

classref-item-separator

classref-property

`float<class_float>` **oversampling** = `0.0` `🔗<class_FontFile_property_oversampling>`

classref-property-setget

- `void (No return value.)` **set_oversampling**(value: `float<class_float>`)
- `float<class_float>` **get_oversampling**()

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See `Viewport.oversampling<class_Viewport_property_oversampling>`. This value doesn't override the `oversampling` parameter of `draw_*` methods.

classref-item-separator

classref-property

`String<class_String>` **style_name** = `""` `🔗<class_FontFile_property_style_name>`

classref-property-setget

- `void (No return value.)` **set_font_style_name**(value: `String<class_String>`)
- `String<class_String>` **get_font_style_name**()

Font style name.

classref-item-separator

classref-property

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **subpixel_positioning** = `1` `🔗<class_FontFile_property_subpixel_positioning>`

classref-property-setget

- `void (No return value.)` **set_subpixel_positioning**(value: `SubpixelPositioning<enum_TextServer_SubpixelPositioning>`)
- `SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **get_subpixel_positioning**()

Font glyph subpixel positioning mode. Subpixel positioning provides shaper text and better kerning for smaller font sizes, at the cost of higher memory usage and lower font rasterization speed. Use `TextServer.SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>` to automatically enable it based on the font size.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_cache**() `🔗<class_FontFile_method_clear_cache>`

Removes all font cache entries.

classref-item-separator

classref-method

`void (No return value.)` **clear_glyphs**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`) `🔗<class_FontFile_method_clear_glyphs>`

Removes all rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use `remove_texture()<class_FontFile_method_remove_texture>` to remove them manually.

classref-item-separator

classref-method

`void (No return value.)` **clear_kerning_map**(cache_index: `int<class_int>`, size: `int<class_int>`) `🔗<class_FontFile_method_clear_kerning_map>`

Removes all kerning overrides.

classref-item-separator

classref-method

`void (No return value.)` **clear_size_cache**(cache_index: `int<class_int>`) `🔗<class_FontFile_method_clear_size_cache>`

Removes all font sizes from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **clear_textures**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`) `🔗<class_FontFile_method_clear_textures>`

Removes all textures from font cache entry.

**Note:** This function will not remove glyphs associated with the texture, use `remove_glyph()<class_FontFile_method_remove_glyph>` to remove them manually.

classref-item-separator

classref-method

`float<class_float>` **get_cache_ascent**(cache_index: `int<class_int>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_cache_ascent>`

Returns the font ascent (number of pixels above the baseline).

classref-item-separator

classref-method

`int<class_int>` **get_cache_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_cache_count>`

Returns number of the font cache entries.

classref-item-separator

classref-method

`float<class_float>` **get_cache_descent**(cache_index: `int<class_int>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_cache_descent>`

Returns the font descent (number of pixels below the baseline).

classref-item-separator

classref-method

`float<class_float>` **get_cache_scale**(cache_index: `int<class_int>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_cache_scale>`

Returns scaling factor of the color bitmap font.

classref-item-separator

classref-method

`float<class_float>` **get_cache_underline_position**(cache_index: `int<class_int>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_cache_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **get_cache_underline_thickness**(cache_index: `int<class_int>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_cache_underline_thickness>`

Returns thickness of the underline in pixels.

classref-item-separator

classref-method

`int<class_int>` **get_char_from_glyph_index**(size: `int<class_int>`, glyph_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_char_from_glyph_index>`

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid. See `get_glyph_index()<class_FontFile_method_get_glyph_index>`.

classref-item-separator

classref-method

`float<class_float>` **get_embolden**(cache_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_embolden>`

Returns embolden strength, if is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

classref-item-separator

classref-method

`float<class_float>` **get_extra_baseline_offset**(cache_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_extra_baseline_offset>`

Returns extra baseline offset (as a fraction of font height).

classref-item-separator

classref-method

`int<class_int>` **get_extra_spacing**(cache_index: `int<class_int>`, spacing: `SpacingType<enum_TextServer_SpacingType>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_extra_spacing>`

Returns spacing for `spacing` in pixels (not relative to the font size).

classref-item-separator

classref-method

`int<class_int>` **get_face_index**(cache_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_face_index>`

Returns an active face index in the TrueType / OpenType collection.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_glyph_advance**(cache_index: `int<class_int>`, size: `int<class_int>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_advance>`

Returns glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

classref-item-separator

classref-method

`int<class_int>` **get_glyph_index**(size: `int<class_int>`, char: `int<class_int>`, variation_selector: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_index>`

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_glyph_list**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_list>`

Returns list of rendered glyphs in the cache entry.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_glyph_offset**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_offset>`

Returns glyph offset from the baseline.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_glyph_size**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_size>`

Returns glyph size.

classref-item-separator

classref-method

`int<class_int>` **get_glyph_texture_idx**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_texture_idx>`

Returns index of the cache texture containing the glyph.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **get_glyph_uv_rect**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_glyph_uv_rect>`

Returns rectangle in the cache texture containing the glyph.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_kerning**(cache_index: `int<class_int>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_kerning>`

Returns kerning for the pair of glyphs.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **get_kerning_list**(cache_index: `int<class_int>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_kerning_list>`

Returns list of the kerning overrides.

classref-item-separator

classref-method

`bool<class_bool>` **get_language_support_override**(language: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_language_support_override>`

Returns `true` if support override is enabled for the `language`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_language_support_overrides**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_language_support_overrides>`

Returns list of language support overrides.

classref-item-separator

classref-method

`bool<class_bool>` **get_script_support_override**(script: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_script_support_override>`

Returns `true` if support override is enabled for the `script`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_script_support_overrides**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_script_support_overrides>`

Returns list of script support overrides.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **get_size_cache_list**(cache_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_size_cache_list>`

Returns list of the font sizes in the cache. Each size is `Vector2i<class_Vector2i>` with font size and outline size.

classref-item-separator

classref-method

`int<class_int>` **get_texture_count**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_texture_count>`

Returns number of textures used by font cache entry.

classref-item-separator

classref-method

`Image<class_Image>` **get_texture_image**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_texture_image>`

Returns a copy of the font cache texture image.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_texture_offsets**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_texture_offsets>`

Returns a copy of the array containing glyph packing data.

classref-item-separator

classref-method

`Transform2D<class_Transform2D>` **get_transform**(cache_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_transform>`

Returns 2D transform, applied to the font outlines, can be used for slanting, flipping and rotating glyphs.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_variation_coordinates**(cache_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FontFile_method_get_variation_coordinates>`

Returns variation coordinates for the specified font cache entry. See `Font.get_supported_variation_list()<class_Font_method_get_supported_variation_list>` for more info.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **load_bitmap_font**(path: `String<class_String>`) `🔗<class_FontFile_method_load_bitmap_font>`

Loads an AngelCode BMFont (.fnt, .font) bitmap font from file `path`.

**Warning:** This method should only be used in the editor or in cases when you need to load external fonts at run-time, such as fonts located at the `user://` directory.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **load_dynamic_font**(path: `String<class_String>`) `🔗<class_FontFile_method_load_dynamic_font>`

Loads a TrueType (.ttf), OpenType (.otf), WOFF (.woff), WOFF2 (.woff2) or Type 1 (.pfb, .pfm) dynamic font from file `path`.

**Warning:** This method should only be used in the editor or in cases when you need to load external fonts at run-time, such as fonts located at the `user://` directory.

classref-item-separator

classref-method

`void (No return value.)` **remove_cache**(cache_index: `int<class_int>`) `🔗<class_FontFile_method_remove_cache>`

Removes specified font cache entry.

classref-item-separator

classref-method

`void (No return value.)` **remove_glyph**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `🔗<class_FontFile_method_remove_glyph>`

Removes specified rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use `remove_texture()<class_FontFile_method_remove_texture>` to remove them manually.

classref-item-separator

classref-method

`void (No return value.)` **remove_kerning**(cache_index: `int<class_int>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`) `🔗<class_FontFile_method_remove_kerning>`

Removes kerning override for the pair of glyphs.

classref-item-separator

classref-method

`void (No return value.)` **remove_language_support_override**(language: `String<class_String>`) `🔗<class_FontFile_method_remove_language_support_override>`

Remove language support override.

classref-item-separator

classref-method

`void (No return value.)` **remove_script_support_override**(script: `String<class_String>`) `🔗<class_FontFile_method_remove_script_support_override>`

Removes script support override.

classref-item-separator

classref-method

`void (No return value.)` **remove_size_cache**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`) `🔗<class_FontFile_method_remove_size_cache>`

Removes specified font size from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **remove_texture**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `🔗<class_FontFile_method_remove_texture>`

Removes specified texture from the cache entry.

**Note:** This function will not remove glyphs associated with the texture. Remove them manually using `remove_glyph()<class_FontFile_method_remove_glyph>`.

classref-item-separator

classref-method

`void (No return value.)` **render_glyph**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, index: `int<class_int>`) `🔗<class_FontFile_method_render_glyph>`

Renders specified glyph to the font cache texture.

classref-item-separator

classref-method

`void (No return value.)` **render_range**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, start: `int<class_int>`, end: `int<class_int>`) `🔗<class_FontFile_method_render_range>`

Renders the range of characters to the font cache texture.

classref-item-separator

classref-method

`void (No return value.)` **set_cache_ascent**(cache_index: `int<class_int>`, size: `int<class_int>`, ascent: `float<class_float>`) `🔗<class_FontFile_method_set_cache_ascent>`

Sets the font ascent (number of pixels above the baseline).

classref-item-separator

classref-method

`void (No return value.)` **set_cache_descent**(cache_index: `int<class_int>`, size: `int<class_int>`, descent: `float<class_float>`) `🔗<class_FontFile_method_set_cache_descent>`

Sets the font descent (number of pixels below the baseline).

classref-item-separator

classref-method

`void (No return value.)` **set_cache_scale**(cache_index: `int<class_int>`, size: `int<class_int>`, scale: `float<class_float>`) `🔗<class_FontFile_method_set_cache_scale>`

Sets scaling factor of the color bitmap font.

classref-item-separator

classref-method

`void (No return value.)` **set_cache_underline_position**(cache_index: `int<class_int>`, size: `int<class_int>`, underline_position: `float<class_float>`) `🔗<class_FontFile_method_set_cache_underline_position>`

Sets pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`void (No return value.)` **set_cache_underline_thickness**(cache_index: `int<class_int>`, size: `int<class_int>`, underline_thickness: `float<class_float>`) `🔗<class_FontFile_method_set_cache_underline_thickness>`

Sets thickness of the underline in pixels.

classref-item-separator

classref-method

`void (No return value.)` **set_embolden**(cache_index: `int<class_int>`, strength: `float<class_float>`) `🔗<class_FontFile_method_set_embolden>`

Sets embolden strength, if is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

classref-item-separator

classref-method

`void (No return value.)` **set_extra_baseline_offset**(cache_index: `int<class_int>`, baseline_offset: `float<class_float>`) `🔗<class_FontFile_method_set_extra_baseline_offset>`

Sets extra baseline offset (as a fraction of font height).

classref-item-separator

classref-method

`void (No return value.)` **set_extra_spacing**(cache_index: `int<class_int>`, spacing: `SpacingType<enum_TextServer_SpacingType>`, value: `int<class_int>`) `🔗<class_FontFile_method_set_extra_spacing>`

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

classref-item-separator

classref-method

`void (No return value.)` **set_face_index**(cache_index: `int<class_int>`, face_index: `int<class_int>`) `🔗<class_FontFile_method_set_face_index>`

Sets an active face index in the TrueType / OpenType collection.

classref-item-separator

classref-method

`void (No return value.)` **set_glyph_advance**(cache_index: `int<class_int>`, size: `int<class_int>`, glyph: `int<class_int>`, advance: `Vector2<class_Vector2>`) `🔗<class_FontFile_method_set_glyph_advance>`

Sets glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

classref-item-separator

classref-method

`void (No return value.)` **set_glyph_offset**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, offset: `Vector2<class_Vector2>`) `🔗<class_FontFile_method_set_glyph_offset>`

Sets glyph offset from the baseline.

classref-item-separator

classref-method

`void (No return value.)` **set_glyph_size**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, gl_size: `Vector2<class_Vector2>`) `🔗<class_FontFile_method_set_glyph_size>`

Sets glyph size.

classref-item-separator

classref-method

`void (No return value.)` **set_glyph_texture_idx**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, texture_idx: `int<class_int>`) `🔗<class_FontFile_method_set_glyph_texture_idx>`

Sets index of the cache texture containing the glyph.

classref-item-separator

classref-method

`void (No return value.)` **set_glyph_uv_rect**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, uv_rect: `Rect2<class_Rect2>`) `🔗<class_FontFile_method_set_glyph_uv_rect>`

Sets rectangle in the cache texture containing the glyph.

classref-item-separator

classref-method

`void (No return value.)` **set_kerning**(cache_index: `int<class_int>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`, kerning: `Vector2<class_Vector2>`) `🔗<class_FontFile_method_set_kerning>`

Sets kerning for the pair of glyphs.

classref-item-separator

classref-method

`void (No return value.)` **set_language_support_override**(language: `String<class_String>`, supported: `bool<class_bool>`) `🔗<class_FontFile_method_set_language_support_override>`

Adds override for `Font.is_language_supported()<class_Font_method_is_language_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **set_script_support_override**(script: `String<class_String>`, supported: `bool<class_bool>`) `🔗<class_FontFile_method_set_script_support_override>`

Adds override for `Font.is_script_supported()<class_Font_method_is_script_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **set_texture_image**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`, image: `Image<class_Image>`) `🔗<class_FontFile_method_set_texture_image>`

Sets font cache texture image.

classref-item-separator

classref-method

`void (No return value.)` **set_texture_offsets**(cache_index: `int<class_int>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`, offset: `PackedInt32Array<class_PackedInt32Array>`) `🔗<class_FontFile_method_set_texture_offsets>`

Sets array containing glyph packing data.

classref-item-separator

classref-method

`void (No return value.)` **set_transform**(cache_index: `int<class_int>`, transform: `Transform2D<class_Transform2D>`) `🔗<class_FontFile_method_set_transform>`

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

classref-item-separator

classref-method

`void (No return value.)` **set_variation_coordinates**(cache_index: `int<class_int>`, variation_coordinates: `Dictionary<class_Dictionary>`) `🔗<class_FontFile_method_set_variation_coordinates>`

Sets variation coordinates for the specified font cache entry. See `Font.get_supported_variation_list()<class_Font_method_get_supported_variation_list>` for more info.