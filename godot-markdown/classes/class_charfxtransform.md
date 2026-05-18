github_url
hide

# CharFXTransform

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Controls how an individual character will be displayed in a `RichTextEffect<class_RichTextEffect>`.

classref-introduction-group

## Description

By setting various properties on this object, you can control how individual characters will be displayed in a `RichTextEffect<class_RichTextEffect>`.

classref-introduction-group

## Tutorials

- `BBCode in RichTextLabel <../tutorials/ui/bbcode_in_richtextlabel>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **color** = `Color(0, 0, 0, 1)` `🔗<class_CharFXTransform_property_color>`

classref-property-setget

- `void (No return value.)` **set_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_color**()

The color the character will be drawn with.

classref-item-separator

classref-property

`float<class_float>` **elapsed_time** = `0.0` `🔗<class_CharFXTransform_property_elapsed_time>`

classref-property-setget

- `void (No return value.)` **set_elapsed_time**(value: `float<class_float>`)
- `float<class_float>` **get_elapsed_time**()

The time elapsed since the `RichTextLabel<class_RichTextLabel>` was added to the scene tree (in seconds). Time stops when the `RichTextLabel<class_RichTextLabel>` is paused (see `Node.process_mode<class_Node_property_process_mode>`). Resets when the text in the `RichTextLabel<class_RichTextLabel>` is changed.

**Note:** Time still passes while the `RichTextLabel<class_RichTextLabel>` is hidden.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **env** = `{}` `🔗<class_CharFXTransform_property_env>`

classref-property-setget

- `void (No return value.)` **set_environment**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_environment**()

Contains the arguments passed in the opening BBCode tag. By default, arguments are strings; if their contents match a type such as `bool<class_bool>`, `int<class_int>` or `float<class_float>`, they will be converted automatically. Color codes in the form `#rrggbb` or `#rgb` will be converted to an opaque `Color<class_Color>`. String arguments may not contain spaces, even if they're quoted. If present, quotes will also be present in the final string.

For example, the opening BBCode tag `[example foo=hello bar=true baz=42 color=#ffffff]` will map to the following `Dictionary<class_Dictionary>`:

    {"foo": "hello", "bar": true, "baz": 42, "color": Color(1, 1, 1, 1)}

classref-item-separator

classref-property

`RID<class_RID>` **font** = `RID()` `🔗<class_CharFXTransform_property_font>`

classref-property-setget

- `void (No return value.)` **set_font**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_font**()

`TextServer<class_TextServer>` RID of the font used to render glyph, this value can be used with `TextServer.font_*` methods to retrieve font information.

**Note:** Read-only. Setting this property won't affect drawing.

classref-item-separator

classref-property

`int<class_int>` **glyph_count** = `0` `🔗<class_CharFXTransform_property_glyph_count>`

classref-property-setget

- `void (No return value.)` **set_glyph_count**(value: `int<class_int>`)
- `int<class_int>` **get_glyph_count**()

Number of glyphs in the grapheme cluster. This value is set in the first glyph of a cluster.

**Note:** Read-only. Setting this property won't affect drawing.

classref-item-separator

classref-property

`int<class_int>` **glyph_flags** = `0` `🔗<class_CharFXTransform_property_glyph_flags>`

classref-property-setget

- `void (No return value.)` **set_glyph_flags**(value: `int<class_int>`)
- `int<class_int>` **get_glyph_flags**()

Glyph flags. See `GraphemeFlag<enum_TextServer_GraphemeFlag>` for more info.

**Note:** Read-only. Setting this property won't affect drawing.

classref-item-separator

classref-property

`int<class_int>` **glyph_index** = `0` `🔗<class_CharFXTransform_property_glyph_index>`

classref-property-setget

- `void (No return value.)` **set_glyph_index**(value: `int<class_int>`)
- `int<class_int>` **get_glyph_index**()

Glyph index specific to the `font<class_CharFXTransform_property_font>`. If you want to replace this glyph, use `TextServer.font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>` with `font<class_CharFXTransform_property_font>` to get a new glyph index for a single character.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **offset** = `Vector2(0, 0)` `🔗<class_CharFXTransform_property_offset>`

classref-property-setget

- `void (No return value.)` **set_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_offset**()

The position offset the character will be drawn with (in pixels).

classref-item-separator

classref-property

`bool<class_bool>` **outline** = `false` `🔗<class_CharFXTransform_property_outline>`

classref-property-setget

- `void (No return value.)` **set_outline**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_outline**()

If `true`, FX transform is called for outline drawing.

**Note:** Read-only. Setting this property won't affect drawing.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **range** = `Vector2i(0, 0)` `🔗<class_CharFXTransform_property_range>`

classref-property-setget

- `void (No return value.)` **set_range**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_range**()

Absolute character range in the string, corresponding to the glyph.

**Note:** Read-only. Setting this property won't affect drawing.

classref-item-separator

classref-property

`int<class_int>` **relative_index** = `0` `🔗<class_CharFXTransform_property_relative_index>`

classref-property-setget

- `void (No return value.)` **set_relative_index**(value: `int<class_int>`)
- `int<class_int>` **get_relative_index**()

The character offset of the glyph, relative to the current `RichTextEffect<class_RichTextEffect>` custom block.

**Note:** Read-only. Setting this property won't affect drawing.

classref-item-separator

classref-property

`Transform2D<class_Transform2D>` **transform** = `Transform2D(1, 0, 0, 1, 0, 0)` `🔗<class_CharFXTransform_property_transform>`

classref-property-setget

- `void (No return value.)` **set_transform**(value: `Transform2D<class_Transform2D>`)
- `Transform2D<class_Transform2D>` **get_transform**()

The current transform of the current glyph. It can be overridden (for example, by driving the position and rotation from a curve). You can also alter the existing value to apply transforms on top of other effects.

classref-item-separator

classref-property

`bool<class_bool>` **visible** = `true` `🔗<class_CharFXTransform_property_visible>`

classref-property-setget

- `void (No return value.)` **set_visibility**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_visible**()

If `true`, the character will be drawn. If `false`, the character will be hidden. Characters around hidden characters will reflow to take the space of hidden characters. If this is not desired, set their `color<class_CharFXTransform_property_color>` to `Color(1, 1, 1, 0)` instead.