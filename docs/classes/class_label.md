github_url
hide

# Label

**Inherits:** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A control for displaying plain text.

classref-introduction-group

## Description

A control for displaying plain text. It gives you control over the horizontal and vertical alignment and can wrap the text inside the node's bounding rectangle. It doesn't support bold, italics, or other rich text formatting. For that, use `RichTextLabel<class_RichTextLabel>` instead.

**Note:** A single Label node is not designed to display huge amounts of text. To display large amounts of text in a single node, consider using `RichTextLabel<class_RichTextLabel>` instead as it supports features like an integrated scroll bar and threading. `RichTextLabel<class_RichTextLabel>` generally performs better when displaying large amounts of text (several pages or more).

classref-introduction-group

## Tutorials

- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`AutowrapMode<enum_TextServer_AutowrapMode>` **autowrap_mode** = `0` `🔗<class_Label_property_autowrap_mode>`

classref-property-setget

- `void (No return value.)` **set_autowrap_mode**(value: `AutowrapMode<enum_TextServer_AutowrapMode>`)
- `AutowrapMode<enum_TextServer_AutowrapMode>` **get_autowrap_mode**()

If set to something other than `TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`, the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

**Note:** Labels with autowrapping enabled must have a custom maximum width configured to work correctly, either through the Label's own `Control.custom_maximum_size<class_Control_property_custom_maximum_size>` or as a result of a propagated maximum size from a parent Control with `Control.propagate_maximum_size<class_Control_property_propagate_maximum_size>` enabled.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\] **autowrap_trim_flags** = `192` `🔗<class_Label_property_autowrap_trim_flags>`

classref-property-setget

- `void (No return value.)` **set_autowrap_trim_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See `TextServer.BREAK_TRIM_START_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES>` and `TextServer.BREAK_TRIM_END_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES>` for more info.

classref-item-separator

classref-property

`bool<class_bool>` **clip_text** = `false` `🔗<class_Label_property_clip_text>`

classref-property-setget

- `void (No return value.)` **set_clip_text**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_clipping_text**()

If `true`, the Label only shows the text that fits inside its bounding rectangle and will clip text horizontally.

classref-item-separator

classref-property

`String<class_String>` **ellipsis_char** = `"…"` `🔗<class_Label_property_ellipsis_char>`

classref-property-setget

- `void (No return value.)` **set_ellipsis_char**(value: `String<class_String>`)
- `String<class_String>` **get_ellipsis_char**()

Ellipsis character used for text clipping.

classref-item-separator

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **horizontal_alignment** = `0` `🔗<class_Label_property_horizontal_alignment>`

classref-property-setget

- `void (No return value.)` **set_horizontal_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **justification_flags** = `163` `🔗<class_Label_property_justification_flags>`

classref-property-setget

- `void (No return value.)` **set_justification_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **get_justification_flags**()

Line fill alignment rules.

classref-item-separator

classref-property

`LabelSettings<class_LabelSettings>` **label_settings** `🔗<class_Label_property_label_settings>`

classref-property-setget

- `void (No return value.)` **set_label_settings**(value: `LabelSettings<class_LabelSettings>`)
- `LabelSettings<class_LabelSettings>` **get_label_settings**()

A `LabelSettings<class_LabelSettings>` resource that can be shared between multiple **Label** nodes. Takes priority over theme properties.

classref-item-separator

classref-property

`String<class_String>` **language** = `""` `🔗<class_Label_property_language>`

classref-property-setget

- `void (No return value.)` **set_language**(value: `String<class_String>`)
- `String<class_String>` **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

classref-item-separator

classref-property

`int<class_int>` **lines_skipped** = `0` `🔗<class_Label_property_lines_skipped>`

classref-property-setget

- `void (No return value.)` **set_lines_skipped**(value: `int<class_int>`)
- `int<class_int>` **get_lines_skipped**()

The number of the lines ignored and not displayed from the start of the `text<class_Label_property_text>` value.

classref-item-separator

classref-property

`int<class_int>` **max_lines_visible** = `-1` `🔗<class_Label_property_max_lines_visible>`

classref-property-setget

- `void (No return value.)` **set_max_lines_visible**(value: `int<class_int>`)
- `int<class_int>` **get_max_lines_visible**()

Limits the lines of text the node shows on screen.

classref-item-separator

classref-property

`String<class_String>` **paragraph_separator** = `"\\n"` `🔗<class_Label_property_paragraph_separator>`

classref-property-setget

- `void (No return value.)` **set_paragraph_separator**(value: `String<class_String>`)
- `String<class_String>` **get_paragraph_separator**()

String used as a paragraph separator. Each paragraph is processed independently, in its own BiDi context.

classref-item-separator

classref-property

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **structured_text_bidi_override** = `0` `🔗<class_Label_property_structured_text_bidi_override>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override**(value: `StructuredTextParser<enum_TextServer_StructuredTextParser>`)
- `StructuredTextParser<enum_TextServer_StructuredTextParser>` **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

classref-item-separator

classref-property

`Array<class_Array>` **structured_text_bidi_override_options** = `[]` `🔗<class_Label_property_structured_text_bidi_override_options>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override_options**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

classref-item-separator

classref-property

`PackedFloat32Array<class_PackedFloat32Array>` **tab_stops** = `PackedFloat32Array()` `🔗<class_Label_property_tab_stops>`

classref-property-setget

- `void (No return value.)` **set_tab_stops**(value: `PackedFloat32Array<class_PackedFloat32Array>`)
- `PackedFloat32Array<class_PackedFloat32Array>` **get_tab_stops**()

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedFloat32Array<class_PackedFloat32Array>` for more details.

classref-item-separator

classref-property

`String<class_String>` **text** = `""` `🔗<class_Label_property_text>`

classref-property-setget

- `void (No return value.)` **set_text**(value: `String<class_String>`)
- `String<class_String>` **get_text**()

The text to display on screen.

classref-item-separator

classref-property

`TextDirection<enum_Control_TextDirection>` **text_direction** = `0` `🔗<class_Label_property_text_direction>`

classref-property-setget

- `void (No return value.)` **set_text_direction**(value: `TextDirection<enum_Control_TextDirection>`)
- `TextDirection<enum_Control_TextDirection>` **get_text_direction**()

Base text writing direction.

classref-item-separator

classref-property

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **text_overrun_behavior** = `0` `🔗<class_Label_property_text_overrun_behavior>`

classref-property-setget

- `void (No return value.)` **set_text_overrun_behavior**(value: `OverrunBehavior<enum_TextServer_OverrunBehavior>`)
- `OverrunBehavior<enum_TextServer_OverrunBehavior>` **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the node's bounding rectangle.

classref-item-separator

classref-property

`bool<class_bool>` **uppercase** = `false` `🔗<class_Label_property_uppercase>`

classref-property-setget

- `void (No return value.)` **set_uppercase**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

classref-item-separator

classref-property

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **vertical_alignment** = `0` `🔗<class_Label_property_vertical_alignment>`

classref-property-setget

- `void (No return value.)` **set_vertical_alignment**(value: `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`)
- `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, bottom, and fill.

classref-item-separator

classref-property

`int<class_int>` **visible_characters** = `-1` `🔗<class_Label_property_visible_characters>`

classref-property-setget

- `void (No return value.)` **set_visible_characters**(value: `int<class_int>`)
- `int<class_int>` **get_visible_characters**()

The number of characters to display. If set to `-1`, all characters are displayed. This can be useful when animating the text appearing in a dialog box.

**Note:** Setting this property updates `visible_ratio<class_Label_property_visible_ratio>` accordingly.

**Note:** Characters are counted as Unicode codepoints. A single visible grapheme may contain multiple codepoints (e.g. certain emoji use three codepoints). A single codepoint may contain two UTF-16 characters, which are used in C# strings.

classref-item-separator

classref-property

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **visible_characters_behavior** = `0` `🔗<class_Label_property_visible_characters_behavior>`

classref-property-setget

- `void (No return value.)` **set_visible_characters_behavior**(value: `VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`)
- `VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **get_visible_characters_behavior**()

The clipping behavior when `visible_characters<class_Label_property_visible_characters>` or `visible_ratio<class_Label_property_visible_ratio>` is set.

classref-item-separator

classref-property

`float<class_float>` **visible_ratio** = `1.0` `🔗<class_Label_property_visible_ratio>`

classref-property-setget

- `void (No return value.)` **set_visible_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_visible_ratio**()

The fraction of characters to display, relative to the total number of characters (see `get_total_character_count()<class_Label_method_get_total_character_count>`). If set to `1.0`, all characters are displayed. If set to `0.5`, only half of the characters will be displayed. This can be useful when animating the text appearing in a dialog box.

**Note:** Setting this property updates `visible_characters<class_Label_property_visible_characters>` accordingly.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Rect2<class_Rect2>` **get_character_bounds**(pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Label_method_get_character_bounds>`

Returns the bounding rectangle of the character at position `pos` in the label's local coordinate system. If the character is a non-visual character or `pos` is outside the valid range, an empty `Rect2<class_Rect2>` is returned. If the character is a part of a composite grapheme, the bounding rectangle of the whole grapheme is returned.

classref-item-separator

classref-method

`int<class_int>` **get_line_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Label_method_get_line_count>`

Returns the number of lines of text the Label has.

classref-item-separator

classref-method

`int<class_int>` **get_line_height**(line: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Label_method_get_line_height>`

Returns the height of the line `line`.

If `line` is set to `-1`, returns the biggest line height.

If there are no lines, returns font size in pixels.

classref-item-separator

classref-method

`int<class_int>` **get_total_character_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Label_method_get_total_character_count>`

Returns the total number of printable characters in the text (excluding spaces and newlines).

classref-item-separator

classref-method

`int<class_int>` **get_visible_line_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Label_method_get_visible_line_count>`

Returns the number of lines shown. Useful if the **Label**'s height cannot currently display all lines.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **font_color** = `Color(1, 1, 1, 1)` `🔗<class_Label_theme_color_font_color>`

Default text `Color<class_Color>` of the **Label**.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_outline_color** = `Color(0, 0, 0, 1)` `🔗<class_Label_theme_color_font_outline_color>`

The color of text outline.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_shadow_color** = `Color(0, 0, 0, 0)` `🔗<class_Label_theme_color_font_shadow_color>`

`Color<class_Color>` of the text's shadow effect.

classref-item-separator

classref-themeproperty

`int<class_int>` **line_spacing** = `3` `🔗<class_Label_theme_constant_line_spacing>`

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

classref-item-separator

classref-themeproperty

`int<class_int>` **outline_size** = `0` `🔗<class_Label_theme_constant_outline_size>`

Text outline size.

**Note:** If using a font with `FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>` enabled, its `FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the value of `outline_size<class_Label_theme_constant_outline_size>` for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

**Note:** Using a value that is larger than half the font size is not recommended, as the font outline may fail to be fully closed in this case.

classref-item-separator

classref-themeproperty

`int<class_int>` **paragraph_spacing** = `0` `🔗<class_Label_theme_constant_paragraph_spacing>`

Vertical space between paragraphs. Added on top of `line_spacing<class_Label_theme_constant_line_spacing>`.

classref-item-separator

classref-themeproperty

`int<class_int>` **shadow_offset_x** = `1` `🔗<class_Label_theme_constant_shadow_offset_x>`

The horizontal offset of the text's shadow.

classref-item-separator

classref-themeproperty

`int<class_int>` **shadow_offset_y** = `1` `🔗<class_Label_theme_constant_shadow_offset_y>`

The vertical offset of the text's shadow.

classref-item-separator

classref-themeproperty

`int<class_int>` **shadow_outline_size** = `1` `🔗<class_Label_theme_constant_shadow_outline_size>`

The size of the shadow outline.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **font** `🔗<class_Label_theme_font_font>`

`Font<class_Font>` used for the **Label**'s text.

classref-item-separator

classref-themeproperty

`int<class_int>` **font_size** `🔗<class_Label_theme_font_size_font_size>`

Font size of the **Label**'s text.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **focus** `🔗<class_Label_theme_style_focus>`

`StyleBox<class_StyleBox>` used when the **Label** is focused (when used with assistive apps).

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **normal** `🔗<class_Label_theme_style_normal>`

Background `StyleBox<class_StyleBox>` for the **Label**.