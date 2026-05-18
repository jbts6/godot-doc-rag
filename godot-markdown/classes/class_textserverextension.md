github_url
hide

# TextServerExtension

**Inherits:** `TextServer<class_TextServer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `TextServerAdvanced<class_TextServerAdvanced>`, `TextServerDummy<class_TextServerDummy>`, `TextServerFallback<class_TextServerFallback>`

Base class for custom `TextServer<class_TextServer>` implementations (plugins).

classref-introduction-group

## Description

External `TextServer<class_TextServer>` implementations should inherit from this class.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_cleanup**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__cleanup>`

This method is called before text server is unregistered.

classref-item-separator

classref-method

`RID<class_RID>` **\_create_font**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__create_font>`

Creates a new, empty font cache entry resource.

classref-item-separator

classref-method

`RID<class_RID>` **\_create_font_linked_variation**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__create_font_linked_variation>`

Optional, implement if font supports extra spacing or baseline offset.

Creates a new variation existing font which is reusing the same glyph cache and font data.

classref-item-separator

classref-method

`RID<class_RID>` **\_create_shaped_text**(direction: `Direction<enum_TextServer_Direction>`, orientation: `Orientation<enum_TextServer_Orientation>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__create_shaped_text>`

Creates a new buffer for complex text layout, with the given `direction` and `orientation`.

classref-item-separator

classref-method

`void (No return value.)` **\_draw_hex_code_box**(canvas: `RID<class_RID>`, size: `int<class_int>`, pos: `Vector2<class_Vector2>`, index: `int<class_int>`, color: `Color<class_Color>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__draw_hex_code_box>`

Draws box displaying character hexadecimal code.

classref-item-separator

classref-method

`void (No return value.)` **\_font_clear_glyphs**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_clear_glyphs>`

Removes all rendered glyph information from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_clear_kerning_map**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_clear_kerning_map>`

Removes all kerning overrides.

classref-item-separator

classref-method

`void (No return value.)` **\_font_clear_size_cache**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_clear_size_cache>`

Removes all font sizes from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_clear_system_fallback_cache**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_clear_system_fallback_cache>`

Frees all automatically loaded system fonts.

classref-item-separator

classref-method

`void (No return value.)` **\_font_clear_textures**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_clear_textures>`

Removes all textures from font cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_draw_glyph**(font_rid: `RID<class_RID>`, canvas: `RID<class_RID>`, size: `int<class_int>`, pos: `Vector2<class_Vector2>`, index: `int<class_int>`, color: `Color<class_Color>`, oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_draw_glyph>`

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **\_font_draw_glyph_outline**(font_rid: `RID<class_RID>`, canvas: `RID<class_RID>`, size: `int<class_int>`, outline_size: `int<class_int>`, pos: `Vector2<class_Vector2>`, index: `int<class_int>`, color: `Color<class_Color>`, oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_draw_glyph_outline>`

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`FontAntialiasing<enum_TextServer_FontAntialiasing>` **\_font_get_antialiasing**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_antialiasing>`

Returns font anti-aliasing mode.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_ascent**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_ascent>`

Returns the font ascent (number of pixels above the baseline).

classref-item-separator

classref-method

`float<class_float>` **\_font_get_baseline_offset**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_baseline_offset>`

Returns extra baseline offset (as a fraction of font height).

classref-item-separator

classref-method

`int<class_int>` **\_font_get_char_from_glyph_index**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_char_from_glyph_index>`

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_descent**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_descent>`

Returns the font descent (number of pixels below the baseline).

classref-item-separator

classref-method

`bool<class_bool>` **\_font_get_disable_embedded_bitmaps**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_disable_embedded_bitmaps>`

Returns whether the font's embedded bitmap loading is disabled.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_embolden**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_embolden>`

Returns font embolden strength.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_face_count**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_face_count>`

Returns number of faces in the TrueType / OpenType collection.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_face_index**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_face_index>`

Returns an active face index in the TrueType / OpenType collection.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_fixed_size**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_fixed_size>`

Returns bitmap font fixed size.

classref-item-separator

classref-method

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **\_font_get_fixed_size_scale_mode**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_fixed_size_scale_mode>`

Returns bitmap font scaling mode.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_get_generate_mipmaps**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_generate_mipmaps>`

Returns `true` if font texture mipmap generation is enabled.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_global_oversampling**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_global_oversampling>`

Returns the font oversampling factor, shared by all fonts in the TextServer.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_font_get_glyph_advance**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_advance>`

Returns glyph advance (offset of the next glyph).

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_font_get_glyph_contours**(font_rid: `RID<class_RID>`, size: `int<class_int>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_contours>`

Returns outline contours of the glyph.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_glyph_index**(font_rid: `RID<class_RID>`, size: `int<class_int>`, char: `int<class_int>`, variation_selector: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_index>`

Returns the glyph index of a `char`, optionally modified by the `variation_selector`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_font_get_glyph_list**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_list>`

Returns list of rendered glyphs in the cache entry.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_font_get_glyph_offset**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_offset>`

Returns glyph offset from the baseline.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_font_get_glyph_size**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_size>`

Returns size of the glyph.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_glyph_texture_idx**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_texture_idx>`

Returns index of the cache texture containing the glyph.

classref-item-separator

classref-method

`RID<class_RID>` **\_font_get_glyph_texture_rid**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_texture_rid>`

Returns resource ID of the cache texture containing the glyph.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_font_get_glyph_texture_size**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_texture_size>`

Returns size of the cache texture containing the glyph.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **\_font_get_glyph_uv_rect**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_glyph_uv_rect>`

Returns rectangle in the cache texture containing the glyph.

classref-item-separator

classref-method

`Hinting<enum_TextServer_Hinting>` **\_font_get_hinting**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_hinting>`

Returns the font hinting mode. Used by dynamic fonts only.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_get_keep_rounding_remainders**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_keep_rounding_remainders>`

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_font_get_kerning**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_kerning>`

Returns kerning for the pair of glyphs.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **\_font_get_kerning_list**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_kerning_list>`

Returns list of the kerning overrides.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_get_language_support_override**(font_rid: `RID<class_RID>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_get_language_support_override>`

Returns `true` if support override is enabled for the `language`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_font_get_language_support_overrides**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_get_language_support_overrides>`

Returns list of language support overrides.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_msdf_pixel_range**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_msdf_pixel_range>`

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_msdf_size**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_msdf_size>`

Returns source font size used to generate MSDF textures.

classref-item-separator

classref-method

`String<class_String>` **\_font_get_name**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_name>`

Returns font family name.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_font_get_opentype_feature_overrides**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_opentype_feature_overrides>`

Returns font OpenType feature set override.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_font_get_ot_name_strings**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_ot_name_strings>`

Returns `Dictionary<class_Dictionary>` with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

classref-item-separator

classref-method

`float<class_float>` **\_font_get_oversampling**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_oversampling>`

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See `Viewport.oversampling<class_Viewport_property_oversampling>`. This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

classref-item-separator

classref-method

`PackedColorArray<class_PackedColorArray>` **\_font_get_palette_colors**(font_rid: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_palette_colors>`

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using `_font_set_palette_custom_colors()<class_TextServerExtension_private_method__font_set_palette_custom_colors>`.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_palette_count**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_palette_count>`

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

classref-item-separator

classref-method

`PackedColorArray<class_PackedColorArray>` **\_font_get_palette_custom_colors**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_palette_custom_colors>`

Returns array of custom colors to override predefined palette.

classref-item-separator

classref-method

`String<class_String>` **\_font_get_palette_name**(font_rid: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_palette_name>`

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_scale**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_scale>`

Returns scaling factor of the color bitmap font.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_get_script_support_override**(font_rid: `RID<class_RID>`, script: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_get_script_support_override>`

Returns `true` if support override is enabled for the `script`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_font_get_script_support_overrides**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_get_script_support_overrides>`

Returns list of script support overrides.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_font_get_size_cache_info**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_size_cache_info>`

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **\_font_get_size_cache_list**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_size_cache_list>`

Returns list of the font sizes in the cache. Each size is `Vector2i<class_Vector2i>` with font size and outline size.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_spacing**(font_rid: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_spacing>`

Returns the spacing for `spacing` in pixels (not relative to the font size).

classref-item-separator

classref-method

`int<class_int>` **\_font_get_stretch**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_stretch>`

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

classref-item-separator

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\] **\_font_get_style**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_style>`

Returns font style flags.

classref-item-separator

classref-method

`String<class_String>` **\_font_get_style_name**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_style_name>`

Returns font style name.

classref-item-separator

classref-method

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **\_font_get_subpixel_positioning**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_subpixel_positioning>`

Returns font subpixel glyph positioning mode.

classref-item-separator

classref-method

`String<class_String>` **\_font_get_supported_chars**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_supported_chars>`

Returns a string containing all the characters available in the font.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_font_get_supported_glyphs**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_supported_glyphs>`

Returns an array containing all glyph indices in the font.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_texture_count**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_texture_count>`

Returns number of textures used by font cache entry.

classref-item-separator

classref-method

`Image<class_Image>` **\_font_get_texture_image**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_texture_image>`

Returns font cache texture image data.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_font_get_texture_offsets**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_texture_offsets>`

Returns array containing glyph packing data.

classref-item-separator

classref-method

`Transform2D<class_Transform2D>` **\_font_get_transform**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_transform>`

Returns 2D transform applied to the font outlines.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_underline_position**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **\_font_get_underline_thickness**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_underline_thickness>`

Returns thickness of the underline in pixels.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_used_palette**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_used_palette>`

Returns used palette index.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_font_get_variation_coordinates**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_variation_coordinates>`

Returns variation coordinates for the specified font cache entry.

classref-item-separator

classref-method

`int<class_int>` **\_font_get_weight**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_get_weight>`

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_has_char**(font_rid: `RID<class_RID>`, char: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_has_char>`

Returns `true` if a Unicode `char` is available in the font.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_is_allow_system_fallback**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_is_allow_system_fallback>`

Returns `true` if system fonts can be automatically used as fallbacks.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_is_force_autohinter**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_is_force_autohinter>`

Returns `true` if auto-hinting is supported and preferred over font built-in hinting.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_is_language_supported**(font_rid: `RID<class_RID>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_is_language_supported>`

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

classref-item-separator

classref-method

`bool<class_bool>` **\_font_is_modulate_color_glyphs**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_is_modulate_color_glyphs>`

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_is_multichannel_signed_distance_field**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_is_multichannel_signed_distance_field>`

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

classref-item-separator

classref-method

`bool<class_bool>` **\_font_is_script_supported**(font_rid: `RID<class_RID>`, script: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_is_script_supported>`

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

classref-item-separator

classref-method

`void (No return value.)` **\_font_remove_glyph**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_remove_glyph>`

Removes specified rendered glyph information from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_remove_kerning**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_remove_kerning>`

Removes kerning override for the pair of glyphs.

classref-item-separator

classref-method

`void (No return value.)` **\_font_remove_language_support_override**(font_rid: `RID<class_RID>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_remove_language_support_override>`

Remove language support override.

classref-item-separator

classref-method

`void (No return value.)` **\_font_remove_script_support_override**(font_rid: `RID<class_RID>`, script: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_remove_script_support_override>`

Removes script support override.

classref-item-separator

classref-method

`void (No return value.)` **\_font_remove_size_cache**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_remove_size_cache>`

Removes specified font size from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_remove_texture**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_remove_texture>`

Removes specified texture from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_render_glyph**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_render_glyph>`

Renders specified glyph to the font cache texture.

classref-item-separator

classref-method

`void (No return value.)` **\_font_render_range**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, start: `int<class_int>`, end: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_render_range>`

Renders the range of characters to the font cache texture.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_allow_system_fallback**(font_rid: `RID<class_RID>`, allow_system_fallback: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_allow_system_fallback>`

If set to `true`, system fonts can be automatically used as fallbacks.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_antialiasing**(font_rid: `RID<class_RID>`, antialiasing: `FontAntialiasing<enum_TextServer_FontAntialiasing>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_antialiasing>`

Sets font anti-aliasing mode.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_ascent**(font_rid: `RID<class_RID>`, size: `int<class_int>`, ascent: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_ascent>`

Sets the font ascent (number of pixels above the baseline).

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_baseline_offset**(font_rid: `RID<class_RID>`, baseline_offset: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_baseline_offset>`

Sets extra baseline offset (as a fraction of font height).

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_data**(font_rid: `RID<class_RID>`, data: `PackedByteArray<class_PackedByteArray>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_data>`

Sets font source data, e.g contents of the dynamic font source file.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_data_ptr**(font_rid: `RID<class_RID>`, data_ptr: `const uint8_t*`, data_size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_data_ptr>`

Sets pointer to the font source data, e.g contents of the dynamic font source file.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_descent**(font_rid: `RID<class_RID>`, size: `int<class_int>`, descent: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_descent>`

Sets the font descent (number of pixels below the baseline).

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_disable_embedded_bitmaps**(font_rid: `RID<class_RID>`, disable_embedded_bitmaps: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_disable_embedded_bitmaps>`

If set to `true`, embedded font bitmap loading is disabled.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_embolden**(font_rid: `RID<class_RID>`, strength: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_embolden>`

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_face_index**(font_rid: `RID<class_RID>`, face_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_face_index>`

Sets an active face index in the TrueType / OpenType collection.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_fixed_size**(font_rid: `RID<class_RID>`, fixed_size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_fixed_size>`

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_fixed_size_scale_mode**(font_rid: `RID<class_RID>`, fixed_size_scale_mode: `FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_fixed_size_scale_mode>`

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_force_autohinter**(font_rid: `RID<class_RID>`, force_autohinter: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_force_autohinter>`

If set to `true` auto-hinting is preferred over font built-in hinting.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_generate_mipmaps**(font_rid: `RID<class_RID>`, generate_mipmaps: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_generate_mipmaps>`

If set to `true` font texture mipmap generation is enabled.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_global_oversampling**(oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_global_oversampling>`

Sets oversampling factor, shared by all font in the TextServer.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_glyph_advance**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph: `int<class_int>`, advance: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_glyph_advance>`

Sets glyph advance (offset of the next glyph).

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_glyph_offset**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, offset: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_glyph_offset>`

Sets glyph offset from the baseline.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_glyph_size**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, gl_size: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_glyph_size>`

Sets size of the glyph.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_glyph_texture_idx**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, texture_idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_glyph_texture_idx>`

Sets index of the cache texture containing the glyph.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_glyph_uv_rect**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, uv_rect: `Rect2<class_Rect2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_glyph_uv_rect>`

Sets rectangle in the cache texture containing the glyph.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_hinting**(font_rid: `RID<class_RID>`, hinting: `Hinting<enum_TextServer_Hinting>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_hinting>`

Sets font hinting mode. Used by dynamic fonts only.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_keep_rounding_remainders**(font_rid: `RID<class_RID>`, keep_rounding_remainders: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_keep_rounding_remainders>`

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_kerning**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`, kerning: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_kerning>`

Sets kerning for the pair of glyphs.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_language_support_override**(font_rid: `RID<class_RID>`, language: `String<class_String>`, supported: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_language_support_override>`

Adds override for `_font_is_language_supported()<class_TextServerExtension_private_method__font_is_language_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_modulate_color_glyphs**(font_rid: `RID<class_RID>`, modulate: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_modulate_color_glyphs>`

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_msdf_pixel_range**(font_rid: `RID<class_RID>`, msdf_pixel_range: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_msdf_pixel_range>`

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_msdf_size**(font_rid: `RID<class_RID>`, msdf_size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_msdf_size>`

Sets source font size used to generate MSDF textures.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_multichannel_signed_distance_field**(font_rid: `RID<class_RID>`, msdf: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_multichannel_signed_distance_field>`

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_name**(font_rid: `RID<class_RID>`, name: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_name>`

Sets the font family name.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_opentype_feature_overrides**(font_rid: `RID<class_RID>`, overrides: `Dictionary<class_Dictionary>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_opentype_feature_overrides>`

Sets font OpenType feature set override.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_oversampling**(font_rid: `RID<class_RID>`, oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_oversampling>`

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See `Viewport.oversampling<class_Viewport_property_oversampling>`. This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_palette_custom_colors**(font_rid: `RID<class_RID>`, colors: `PackedColorArray<class_PackedColorArray>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_palette_custom_colors>`

Sets array of custom colors to override predefined palette. Set to empty array to reset overrides. Use `Color(0, 0, 0, 0)`, to keep predefined palette color at specific position.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_scale**(font_rid: `RID<class_RID>`, size: `int<class_int>`, scale: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_scale>`

Sets scaling factor of the color bitmap font.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_script_support_override**(font_rid: `RID<class_RID>`, script: `String<class_String>`, supported: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_script_support_override>`

Adds override for `_font_is_script_supported()<class_TextServerExtension_private_method__font_is_script_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_spacing**(font_rid: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`, value: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_spacing>`

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_stretch**(font_rid: `RID<class_RID>`, stretch: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_stretch>`

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_style**(font_rid: `RID<class_RID>`, style: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_style>`

Sets the font style flags.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_style_name**(font_rid: `RID<class_RID>`, name_style: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_style_name>`

Sets the font style name.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_subpixel_positioning**(font_rid: `RID<class_RID>`, subpixel_positioning: `SubpixelPositioning<enum_TextServer_SubpixelPositioning>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_subpixel_positioning>`

Sets font subpixel glyph positioning mode.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_texture_image**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`, image: `Image<class_Image>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_texture_image>`

Sets font cache texture image data.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_texture_offsets**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`, offset: `PackedInt32Array<class_PackedInt32Array>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_texture_offsets>`

Sets array containing glyph packing data.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_transform**(font_rid: `RID<class_RID>`, transform: `Transform2D<class_Transform2D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_transform>`

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_underline_position**(font_rid: `RID<class_RID>`, size: `int<class_int>`, underline_position: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_underline_position>`

Sets pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_underline_thickness**(font_rid: `RID<class_RID>`, size: `int<class_int>`, underline_thickness: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__font_set_underline_thickness>`

Sets thickness of the underline in pixels.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_used_palette**(font_rid: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_used_palette>`

Sets used palette index.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_variation_coordinates**(font_rid: `RID<class_RID>`, variation_coordinates: `Dictionary<class_Dictionary>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_variation_coordinates>`

Sets variation coordinates for the specified font cache entry.

classref-item-separator

classref-method

`void (No return value.)` **\_font_set_weight**(font_rid: `RID<class_RID>`, weight: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__font_set_weight>`

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_font_supported_feature_list**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_supported_feature_list>`

Returns the dictionary of the supported OpenType features.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_font_supported_variation_list**(font_rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__font_supported_variation_list>`

Returns the dictionary of the supported OpenType variation coordinates.

classref-item-separator

classref-method

`String<class_String>` **\_format_number**(number: `String<class_String>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__format_number>`

**Deprecated:** Use `TranslationServer.format_number()<class_TranslationServer_method_format_number>` instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

classref-item-separator

classref-method

`void (No return value.)` **\_free_rid**(rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__free_rid>`

Frees an object created by this `TextServer<class_TextServer>`.

classref-item-separator

classref-method

`int<class_int>` **\_get_features**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__get_features>`

Returns text server features, see `Feature<enum_TextServer_Feature>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_get_hex_code_box_size**(size: `int<class_int>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__get_hex_code_box_size>`

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

classref-item-separator

classref-method

`String<class_String>` **\_get_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__get_name>`

Returns the name of the server interface.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **\_get_support_data**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__get_support_data>`

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

classref-item-separator

classref-method

`String<class_String>` **\_get_support_data_filename**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__get_support_data_filename>`

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

classref-item-separator

classref-method

`String<class_String>` **\_get_support_data_info**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__get_support_data_info>`

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

classref-item-separator

classref-method

`bool<class_bool>` **\_has**(rid: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__has>`

Returns `true` if `rid` is valid resource owned by this text server.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_feature**(feature: `Feature<enum_TextServer_Feature>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__has_feature>`

Returns `true` if the server supports a feature.

classref-item-separator

classref-method

`int<class_int>` **\_is_confusable**(string: `String<class_String>`, dict: `PackedStringArray<class_PackedStringArray>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__is_confusable>`

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_locale_right_to_left**(locale: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__is_locale_right_to_left>`

Returns `true` if locale is right-to-left.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_locale_using_support_data**(locale: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__is_locale_using_support_data>`

Returns `true` if the locale requires text server support data for line/word breaking.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_valid_identifier**(string: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__is_valid_identifier>`

Returns `true` if `string` is a valid identifier.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_valid_letter**(unicode: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__is_valid_letter>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_load_support_data**(filename: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__load_support_data>`

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

classref-item-separator

classref-method

`int<class_int>` **\_name_to_tag**(name: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__name_to_tag>`

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

classref-item-separator

classref-method

`String<class_String>` **\_parse_number**(number: `String<class_String>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__parse_number>`

**Deprecated:** Use `TranslationServer.parse_number()<class_TranslationServer_method_parse_number>` instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **\_parse_structured_text**(parser_type: `StructuredTextParser<enum_TextServer_StructuredTextParser>`, args: `Array<class_Array>`, text: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__parse_structured_text>`

Default implementation of the BiDi algorithm override function.

classref-item-separator

classref-method

`String<class_String>` **\_percent_sign**(language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__percent_sign>`

**Deprecated:** Use `TranslationServer.get_percent_sign()<class_TranslationServer_method_get_percent_sign>` instead.

Returns percent sign used in the given `language`.

classref-item-separator

classref-method

`void (No return value.)` **\_reference_oversampling_level**(oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__reference_oversampling_level>`

Increases the reference count of the specified oversampling level. This method is called by `Viewport<class_Viewport>`, and should not be used directly.

classref-item-separator

classref-method

`bool<class_bool>` **\_save_support_data**(filename: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__save_support_data>`

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_get_run_count**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_count>`

Returns the number of uniform text runs in the buffer.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **\_shaped_get_run_direction**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_direction>`

Returns the direction of the `index` text run (in visual order).

classref-item-separator

classref-method

`RID<class_RID>` **\_shaped_get_run_font_rid**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_font_rid>`

Returns the font RID of the `index` text run (in visual order).

classref-item-separator

classref-method

`int<class_int>` **\_shaped_get_run_font_size**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_font_size>`

Returns the font size of the `index` text run (in visual order).

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **\_shaped_get_run_glyph_range**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_glyph_range>`

Returns the glyph range of the `index` text run (in visual order).

classref-item-separator

classref-method

`String<class_String>` **\_shaped_get_run_language**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_language>`

Returns the language of the `index` text run (in visual order).

classref-item-separator

classref-method

`Variant<class_Variant>` **\_shaped_get_run_object**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_object>`

Returns the embedded object of the `index` text run (in visual order).

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **\_shaped_get_run_range**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_range>`

Returns the source text range of the `index` text run (in visual order).

classref-item-separator

classref-method

`String<class_String>` **\_shaped_get_run_text**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_run_text>`

Returns the source text of the `index` text run (in visual order).

classref-item-separator

classref-method

`int<class_int>` **\_shaped_get_span_count**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_span_count>`

Returns number of text spans added using `_shaped_text_add_string()<class_TextServerExtension_private_method__shaped_text_add_string>` or `_shaped_text_add_object()<class_TextServerExtension_private_method__shaped_text_add_object>`.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_shaped_get_span_embedded_object**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_span_embedded_object>`

Returns text embedded object key.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_shaped_get_span_meta**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_span_meta>`

Returns text span metadata.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_shaped_get_span_object**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_span_object>`

Returns the text span embedded object key.

classref-item-separator

classref-method

`String<class_String>` **\_shaped_get_span_text**(shaped: `RID<class_RID>`, index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_span_text>`

Returns the text span source text.

classref-item-separator

classref-method

`String<class_String>` **\_shaped_get_text**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_get_text>`

Returns the text buffer source text, including object replacement characters.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_set_span_update_font**(shaped: `RID<class_RID>`, index: `int<class_int>`, fonts: `Array<class_Array>`\[`RID<class_RID>`\], size: `int<class_int>`, opentype_features: `Dictionary<class_Dictionary>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_set_span_update_font>`

Changes text span font, font size, and OpenType features, without changing the text.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_add_object**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>`, length: `int<class_int>`, baseline: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_add_object>`

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_add_string**(shaped: `RID<class_RID>`, text: `String<class_String>`, fonts: `Array<class_Array>`\[`RID<class_RID>`\], size: `int<class_int>`, opentype_features: `Dictionary<class_Dictionary>`, language: `String<class_String>`, meta: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_add_string>`

Adds text span and font to draw it to the text buffer.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_clear**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_clear>`

Clears text buffer (removes text and inline objects).

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_closest_character_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_closest_character_pos>`

Returns composite character position closest to the `pos`.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_draw**(shaped: `RID<class_RID>`, canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, clip_l: `float<class_float>`, clip_r: `float<class_float>`, color: `Color<class_Color>`, oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_draw>`

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_draw_outline**(shaped: `RID<class_RID>`, canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, clip_l: `float<class_float>`, clip_r: `float<class_float>`, outline_size: `int<class_int>`, color: `Color<class_Color>`, oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_draw_outline>`

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`RID<class_RID>` **\_shaped_text_duplicate**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_duplicate>`

Duplicates shaped text buffer.

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_fit_to_width**(shaped: `RID<class_RID>`, width: `float<class_float>`, justification_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_fit_to_width>`

Adjusts text width to fit to specified width, returns new text width.

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_get_ascent**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_ascent>`

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_get_carets**(shaped: `RID<class_RID>`, position: `int<class_int>`, r_caret: `CaretInfo*`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_carets>`

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_shaped_text_get_character_breaks**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_character_breaks>`

Returns array of the composite character boundaries.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_custom_ellipsis**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_custom_ellipsis>`

Returns ellipsis character used for text clipping.

classref-item-separator

classref-method

`String<class_String>` **\_shaped_text_get_custom_punctuation**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_custom_punctuation>`

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_get_descent**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_descent>`

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **\_shaped_text_get_direction**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_direction>`

Returns direction of the text.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_dominant_direction_in_range**(shaped: `RID<class_RID>`, start: `int<class_int>`, end: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_dominant_direction_in_range>`

Returns dominant direction of in the range of text.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_ellipsis_glyph_count**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyph_count>`

Returns number of glyphs in the ellipsis.

classref-item-separator

classref-method

`const Glyph*` **\_shaped_text_get_ellipsis_glyphs**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_ellipsis_glyphs>`

Returns array of the glyphs in the ellipsis.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_ellipsis_pos**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_ellipsis_pos>`

Returns position of the ellipsis.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_glyph_count**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_glyph_count>`

Returns number of glyphs in the buffer.

classref-item-separator

classref-method

`const Glyph*` **\_shaped_text_get_glyphs**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_glyphs>`

Returns an array of glyphs in the visual order.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_shaped_text_get_grapheme_bounds**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_grapheme_bounds>`

Returns composite character's bounds as offsets from the start of the line.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **\_shaped_text_get_inferred_direction**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_inferred_direction>`

Returns direction of the text, inferred by the BiDi algorithm.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_shaped_text_get_line_breaks**(shaped: `RID<class_RID>`, width: `float<class_float>`, start: `int<class_int>`, break_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_line_breaks>`

Breaks text to the lines and returns character ranges for each line.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_shaped_text_get_line_breaks_adv**(shaped: `RID<class_RID>`, width: `PackedFloat32Array<class_PackedFloat32Array>`, start: `int<class_int>`, once: `bool<class_bool>`, break_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_line_breaks_adv>`

Breaks text to the lines and columns. Returns character ranges for each segment.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_object_glyph**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_object_glyph>`

Returns the glyph index of the inline object.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **\_shaped_text_get_object_range**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_object_range>`

Returns the character range of the inline object.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **\_shaped_text_get_object_rect**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_object_rect>`

Returns bounding rectangle of the inline object.

classref-item-separator

classref-method

`Array<class_Array>` **\_shaped_text_get_objects**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_objects>`

Returns array of inline objects.

classref-item-separator

classref-method

`Orientation<enum_TextServer_Orientation>` **\_shaped_text_get_orientation**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_orientation>`

Returns text orientation.

classref-item-separator

classref-method

`RID<class_RID>` **\_shaped_text_get_parent**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_parent>`

Returns the parent buffer from which the substring originates.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_get_preserve_control**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_preserve_control>`

Returns `true` if text buffer is configured to display control characters.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_get_preserve_invalid**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_preserve_invalid>`

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **\_shaped_text_get_range**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_range>`

Returns substring buffer character range in the parent buffer.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **\_shaped_text_get_selection**(shaped: `RID<class_RID>`, start: `int<class_int>`, end: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_selection>`

Returns selection rectangles for the specified character range.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **\_shaped_text_get_size**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_size>`

Returns size of the text.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_spacing**(shaped: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_spacing>`

Returns extra spacing added between glyphs or lines in pixels.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_get_trim_pos**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_trim_pos>`

Returns the position of the overrun trim.

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_get_underline_position**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_get_underline_thickness**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_underline_thickness>`

Returns thickness of the underline.

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_get_width**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_width>`

Returns width (for horizontal layout) or height (for vertical) of the text.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_shaped_text_get_word_breaks**(shaped: `RID<class_RID>`, grapheme_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`\], skip_grapheme_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_get_word_breaks>`

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_has_object**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_has_object>`

Returns `true` if an object with `key` is embedded in this shaped text buffer.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_hit_test_grapheme**(shaped: `RID<class_RID>`, coord: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_hit_test_grapheme>`

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_hit_test_position**(shaped: `RID<class_RID>`, coord: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_hit_test_position>`

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_is_ready**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_is_ready>`

Returns `true` if buffer is successfully shaped.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_next_character_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_next_character_pos>`

Returns composite character end position closest to the `pos`.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_next_grapheme_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_next_grapheme_pos>`

Returns grapheme end position closest to the `pos`.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_overrun_trim_to_width**(shaped: `RID<class_RID>`, width: `float<class_float>`, trim_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_overrun_trim_to_width>`

Trims text if it exceeds the given width.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_prev_character_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_prev_character_pos>`

Returns composite character start position closest to the `pos`.

classref-item-separator

classref-method

`int<class_int>` **\_shaped_text_prev_grapheme_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_prev_grapheme_pos>`

Returns grapheme start position closest to the `pos`.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_resize_object**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>`, baseline: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_resize_object>`

Sets new size and alignment of embedded object.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_bidi_override**(shaped: `RID<class_RID>`, override: `Array<class_Array>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_bidi_override>`

Overrides BiDi for the structured text.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_custom_ellipsis**(shaped: `RID<class_RID>`, char: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_custom_ellipsis>`

Sets ellipsis character used for text clipping.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_custom_punctuation**(shaped: `RID<class_RID>`, punct: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_custom_punctuation>`

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_direction**(shaped: `RID<class_RID>`, direction: `Direction<enum_TextServer_Direction>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_direction>`

Sets desired text direction. If set to `TextServer.DIRECTION_AUTO<class_TextServer_constant_DIRECTION_AUTO>`, direction will be detected based on the buffer contents and current locale.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_orientation**(shaped: `RID<class_RID>`, orientation: `Orientation<enum_TextServer_Orientation>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_orientation>`

Sets desired text orientation.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_preserve_control**(shaped: `RID<class_RID>`, enabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_preserve_control>`

If set to `true` text buffer will display control characters.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_preserve_invalid**(shaped: `RID<class_RID>`, enabled: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_preserve_invalid>`

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

classref-item-separator

classref-method

`void (No return value.)` **\_shaped_text_set_spacing**(shaped: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`, value: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_set_spacing>`

Sets extra spacing added between glyphs or lines in pixels.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_shape**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_shape>`

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

classref-item-separator

classref-method

`const Glyph*` **\_shaped_text_sort_logical**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_TextServerExtension_private_method__shaped_text_sort_logical>`

Returns text glyphs in the logical order.

classref-item-separator

classref-method

`RID<class_RID>` **\_shaped_text_substr**(shaped: `RID<class_RID>`, start: `int<class_int>`, length: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__shaped_text_substr>`

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

classref-item-separator

classref-method

`float<class_float>` **\_shaped_text_tab_align**(shaped: `RID<class_RID>`, tab_stops: `PackedFloat32Array<class_PackedFloat32Array>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_tab_align>`

Aligns shaped text to the given tab-stops.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_update_breaks**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_update_breaks>`

Updates break points in the shaped text. This method is called by default implementation of text breaking functions.

classref-item-separator

classref-method

`bool<class_bool>` **\_shaped_text_update_justification_ops**(shaped: `RID<class_RID>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__shaped_text_update_justification_ops>`

Updates justification points in the shaped text. This method is called by default implementation of text justification functions.

classref-item-separator

classref-method

`bool<class_bool>` **\_spoof_check**(string: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__spoof_check>`

Returns `true` if `string` is likely to be an attempt at confusing the reader.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_string_get_character_breaks**(string: `String<class_String>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__string_get_character_breaks>`

Returns array of the composite character boundaries.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_string_get_word_breaks**(string: `String<class_String>`, language: `String<class_String>`, chars_per_line: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__string_get_word_breaks>`

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

classref-item-separator

classref-method

`String<class_String>` **\_string_to_lower**(string: `String<class_String>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__string_to_lower>`

Returns the string converted to `lowercase`.

classref-item-separator

classref-method

`String<class_String>` **\_string_to_title**(string: `String<class_String>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__string_to_title>`

Returns the string converted to `Title Case`.

classref-item-separator

classref-method

`String<class_String>` **\_string_to_upper**(string: `String<class_String>`, language: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__string_to_upper>`

Returns the string converted to `UPPERCASE`.

classref-item-separator

classref-method

`String<class_String>` **\_strip_diacritics**(string: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__strip_diacritics>`

Strips diacritics from the string.

classref-item-separator

classref-method

`String<class_String>` **\_tag_to_name**(tag: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerExtension_private_method__tag_to_name>`

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.

classref-item-separator

classref-method

`void (No return value.)` **\_unreference_oversampling_level**(oversampling: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextServerExtension_private_method__unreference_oversampling_level>`

Decreases the reference count of the specified oversampling level, and frees the font cache for oversampling level when the reference count reaches zero. This method is called by `Viewport<class_Viewport>`, and should not be used directly.