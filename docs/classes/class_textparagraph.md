github_url
hide

# TextParagraph

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Holds a paragraph of text.

classref-introduction-group

## Description

Abstraction over `TextServer<class_TextServer>` for handling a single paragraph of text.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **alignment** = `0` `🔗<class_TextParagraph_property_alignment>`

classref-property-setget

- `void (No return value.)` **set_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_alignment**()

Paragraph horizontal alignment.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\] **break_flags** = `3` `🔗<class_TextParagraph_property_break_flags>`

classref-property-setget

- `void (No return value.)` **set_break_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\] **get_break_flags**()

Line breaking rules. For more info see `TextServer<class_TextServer>`.

classref-item-separator

classref-property

`String<class_String>` **custom_punctuation** = `""` `🔗<class_TextParagraph_property_custom_punctuation>`

classref-property-setget

- `void (No return value.)` **set_custom_punctuation**(value: `String<class_String>`)
- `String<class_String>` **get_custom_punctuation**()

Custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

classref-item-separator

classref-property

`Direction<enum_TextServer_Direction>` **direction** = `0` `🔗<class_TextParagraph_property_direction>`

classref-property-setget

- `void (No return value.)` **set_direction**(value: `Direction<enum_TextServer_Direction>`)
- `Direction<enum_TextServer_Direction>` **get_direction**()

Text writing direction.

classref-item-separator

classref-property

`String<class_String>` **ellipsis_char** = `"…"` `🔗<class_TextParagraph_property_ellipsis_char>`

classref-property-setget

- `void (No return value.)` **set_ellipsis_char**(value: `String<class_String>`)
- `String<class_String>` **get_ellipsis_char**()

Ellipsis character used for text clipping.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **justification_flags** = `163` `🔗<class_TextParagraph_property_justification_flags>`

classref-property-setget

- `void (No return value.)` **set_justification_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **get_justification_flags**()

Line fill alignment rules.

classref-item-separator

classref-property

`float<class_float>` **line_spacing** = `0.0` `🔗<class_TextParagraph_property_line_spacing>`

classref-property-setget

- `void (No return value.)` **set_line_spacing**(value: `float<class_float>`)
- `float<class_float>` **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

classref-item-separator

classref-property

`int<class_int>` **max_lines_visible** = `-1` `🔗<class_TextParagraph_property_max_lines_visible>`

classref-property-setget

- `void (No return value.)` **set_max_lines_visible**(value: `int<class_int>`)
- `int<class_int>` **get_max_lines_visible**()

Limits the lines of text shown.

classref-item-separator

classref-property

`Orientation<enum_TextServer_Orientation>` **orientation** = `0` `🔗<class_TextParagraph_property_orientation>`

classref-property-setget

- `void (No return value.)` **set_orientation**(value: `Orientation<enum_TextServer_Orientation>`)
- `Orientation<enum_TextServer_Orientation>` **get_orientation**()

Text orientation.

classref-item-separator

classref-property

`bool<class_bool>` **preserve_control** = `false` `🔗<class_TextParagraph_property_preserve_control>`

classref-property-setget

- `void (No return value.)` **set_preserve_control**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_preserve_control**()

If set to `true` text will display control characters.

classref-item-separator

classref-property

`bool<class_bool>` **preserve_invalid** = `true` `🔗<class_TextParagraph_property_preserve_invalid>`

classref-property-setget

- `void (No return value.)` **set_preserve_invalid**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_preserve_invalid**()

If set to `true` text will display invalid characters.

classref-item-separator

classref-property

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **text_overrun_behavior** = `0` `🔗<class_TextParagraph_property_text_overrun_behavior>`

classref-property-setget

- `void (No return value.)` **set_text_overrun_behavior**(value: `OverrunBehavior<enum_TextServer_OverrunBehavior>`)
- `OverrunBehavior<enum_TextServer_OverrunBehavior>` **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the paragraph's set width.

classref-item-separator

classref-property

`float<class_float>` **width** = `-1.0` `🔗<class_TextParagraph_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `float<class_float>`)
- `float<class_float>` **get_width**()

Paragraph width.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **add_object**(key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, length: `int<class_int>` = 1, baseline: `float<class_float>` = 0.0) `🔗<class_TextParagraph_method_add_object>`

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

classref-item-separator

classref-method

`bool<class_bool>` **add_string**(text: `String<class_String>`, font: `Font<class_Font>`, font_size: `int<class_int>`, language: `String<class_String>` = "", meta: `Variant<class_Variant>` = null) `🔗<class_TextParagraph_method_add_string>`

Adds text span and font to draw it.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_TextParagraph_method_clear>`

Clears text paragraph (removes text and inline objects).

classref-item-separator

classref-method

`void (No return value.)` **clear_dropcap**() `🔗<class_TextParagraph_method_clear_dropcap>`

Removes dropcap.

classref-item-separator

classref-method

`void (No return value.)` **draw**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), dc_color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_draw>`

Draw all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **draw_dropcap**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_draw_dropcap>`

Draw drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **draw_dropcap_outline**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, outline_size: `int<class_int>` = 1, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_draw_dropcap_outline>`

Draw drop cap outline into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **draw_line**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, line: `int<class_int>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_draw_line>`

Draw single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **draw_line_outline**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, line: `int<class_int>`, outline_size: `int<class_int>` = 1, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_draw_line_outline>`

Draw outline of the single line of text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **draw_outline**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, outline_size: `int<class_int>` = 1, color: `Color<class_Color>` = Color(1, 1, 1, 1), dc_color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_draw_outline>`

Draw outlines of all lines of the text and drop cap into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`TextParagraph<class_TextParagraph>` **duplicate**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_duplicate>`

Duplicates this **TextParagraph**.

classref-item-separator

classref-method

`int<class_int>` **get_dropcap_lines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_dropcap_lines>`

Returns number of lines used by dropcap.

classref-item-separator

classref-method

`RID<class_RID>` **get_dropcap_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_dropcap_rid>`

Returns drop cap text buffer RID.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_dropcap_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_dropcap_size>`

Returns drop cap bounding box size.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **get_inferred_direction**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_inferred_direction>`

Returns the text writing direction inferred by the BiDi algorithm.

classref-item-separator

classref-method

`float<class_float>` **get_line_ascent**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_ascent>`

Returns the text line ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

classref-item-separator

classref-method

`int<class_int>` **get_line_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_count>`

Returns number of lines in the paragraph.

classref-item-separator

classref-method

`float<class_float>` **get_line_descent**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_descent>`

Returns the text line descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

classref-item-separator

classref-method

`Rect2<class_Rect2>` **get_line_object_rect**(line: `int<class_int>`, key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_object_rect>`

Returns bounding rectangle of the inline object.

classref-item-separator

classref-method

`Array<class_Array>` **get_line_objects**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_objects>`

Returns array of inline objects in the line.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_line_range**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_range>`

Returns character range of the line.

classref-item-separator

classref-method

`RID<class_RID>` **get_line_rid**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_rid>`

Returns TextServer line buffer RID.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_line_size**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_size>`

Returns size of the bounding box of the line of text. Returned size is rounded up.

classref-item-separator

classref-method

`float<class_float>` **get_line_underline_position**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **get_line_underline_thickness**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_underline_thickness>`

Returns thickness of the underline.

classref-item-separator

classref-method

`float<class_float>` **get_line_width**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_line_width>`

Returns width (for horizontal layout) or height (for vertical) of the line of text.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_non_wrapped_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_non_wrapped_size>`

Returns the size of the bounding box of the paragraph, without line breaks.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_range**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_range>`

Returns the character range of the paragraph.

classref-item-separator

classref-method

`RID<class_RID>` **get_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_rid>`

Returns TextServer full string buffer RID.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_get_size>`

Returns the size of the bounding box of the paragraph.

classref-item-separator

classref-method

`bool<class_bool>` **has_object**(key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_has_object>`

Returns `true` if an object with `key` is embedded in this shaped text buffer.

classref-item-separator

classref-method

`int<class_int>` **hit_test**(coords: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextParagraph_method_hit_test>`

Returns caret character offset at the specified coordinates. This function always returns a valid position.

classref-item-separator

classref-method

`bool<class_bool>` **resize_object**(key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, baseline: `float<class_float>` = 0.0) `🔗<class_TextParagraph_method_resize_object>`

Sets new size and alignment of embedded object.

classref-item-separator

classref-method

`void (No return value.)` **set_bidi_override**(override: `Array<class_Array>`) `🔗<class_TextParagraph_method_set_bidi_override>`

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

classref-item-separator

classref-method

`bool<class_bool>` **set_dropcap**(text: `String<class_String>`, font: `Font<class_Font>`, font_size: `int<class_int>`, dropcap_margins: `Rect2<class_Rect2>` = Rect2(0, 0, 0, 0), language: `String<class_String>` = "") `🔗<class_TextParagraph_method_set_dropcap>`

Sets drop cap, overrides previously set drop cap. Drop cap (dropped capital) is a decorative element at the beginning of a paragraph that is larger than the rest of the text.

classref-item-separator

classref-method

`void (No return value.)` **tab_align**(tab_stops: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_TextParagraph_method_tab_align>`

Aligns paragraph to the given tab-stops.