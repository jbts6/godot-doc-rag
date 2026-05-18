github_url
hide

# TextLine

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Holds a line of text.

classref-introduction-group

## Description

Abstraction over `TextServer<class_TextServer>` for handling a single line of text.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **alignment** = `0` `🔗<class_TextLine_property_alignment>`

classref-property-setget

- `void (No return value.)` **set_horizontal_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_horizontal_alignment**()

Sets text alignment within the line as if the line was horizontal.

classref-item-separator

classref-property

`Direction<enum_TextServer_Direction>` **direction** = `0` `🔗<class_TextLine_property_direction>`

classref-property-setget

- `void (No return value.)` **set_direction**(value: `Direction<enum_TextServer_Direction>`)
- `Direction<enum_TextServer_Direction>` **get_direction**()

Text writing direction.

classref-item-separator

classref-property

`String<class_String>` **ellipsis_char** = `"…"` `🔗<class_TextLine_property_ellipsis_char>`

classref-property-setget

- `void (No return value.)` **set_ellipsis_char**(value: `String<class_String>`)
- `String<class_String>` **get_ellipsis_char**()

Ellipsis character used for text clipping.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **flags** = `3` `🔗<class_TextLine_property_flags>`

classref-property-setget

- `void (No return value.)` **set_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **get_flags**()

Line alignment rules. For more info see `TextServer<class_TextServer>`.

classref-item-separator

classref-property

`Orientation<enum_TextServer_Orientation>` **orientation** = `0` `🔗<class_TextLine_property_orientation>`

classref-property-setget

- `void (No return value.)` **set_orientation**(value: `Orientation<enum_TextServer_Orientation>`)
- `Orientation<enum_TextServer_Orientation>` **get_orientation**()

Text orientation.

classref-item-separator

classref-property

`bool<class_bool>` **preserve_control** = `false` `🔗<class_TextLine_property_preserve_control>`

classref-property-setget

- `void (No return value.)` **set_preserve_control**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_preserve_control**()

If set to `true` text will display control characters.

classref-item-separator

classref-property

`bool<class_bool>` **preserve_invalid** = `true` `🔗<class_TextLine_property_preserve_invalid>`

classref-property-setget

- `void (No return value.)` **set_preserve_invalid**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_preserve_invalid**()

If set to `true` text will display invalid characters.

classref-item-separator

classref-property

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **text_overrun_behavior** = `3` `🔗<class_TextLine_property_text_overrun_behavior>`

classref-property-setget

- `void (No return value.)` **set_text_overrun_behavior**(value: `OverrunBehavior<enum_TextServer_OverrunBehavior>`)
- `OverrunBehavior<enum_TextServer_OverrunBehavior>` **get_text_overrun_behavior**()

The clipping behavior when the text exceeds the text line's set width.

classref-item-separator

classref-property

`float<class_float>` **width** = `-1.0` `🔗<class_TextLine_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `float<class_float>`)
- `float<class_float>` **get_width**()

Text line width.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **add_object**(key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, length: `int<class_int>` = 1, baseline: `float<class_float>` = 0.0) `🔗<class_TextLine_method_add_object>`

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

classref-item-separator

classref-method

`bool<class_bool>` **add_string**(text: `String<class_String>`, font: `Font<class_Font>`, font_size: `int<class_int>`, language: `String<class_String>` = "", meta: `Variant<class_Variant>` = null) `🔗<class_TextLine_method_add_string>`

Adds text span and font to draw it.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_TextLine_method_clear>`

Clears text line (removes text and inline objects).

classref-item-separator

classref-method

`void (No return value.)` **draw**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_draw>`

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`void (No return value.)` **draw_outline**(canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, outline_size: `int<class_int>` = 1, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_draw_outline>`

Draw text into a canvas item at a given position, with `color`. `pos` specifies the top left corner of the bounding box. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

classref-item-separator

classref-method

`TextLine<class_TextLine>` **duplicate**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_duplicate>`

Duplicates this **TextLine**.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **get_inferred_direction**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_inferred_direction>`

Returns the text writing direction inferred by the BiDi algorithm.

classref-item-separator

classref-method

`float<class_float>` **get_line_ascent**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_line_ascent>`

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

classref-item-separator

classref-method

`float<class_float>` **get_line_descent**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_line_descent>`

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

classref-item-separator

classref-method

`float<class_float>` **get_line_underline_position**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_line_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **get_line_underline_thickness**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_line_underline_thickness>`

Returns thickness of the underline.

classref-item-separator

classref-method

`float<class_float>` **get_line_width**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_line_width>`

Returns width (for horizontal layout) or height (for vertical) of the text.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **get_object_rect**(key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_object_rect>`

Returns bounding rectangle of the inline object.

classref-item-separator

classref-method

`Array<class_Array>` **get_objects**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_objects>`

Returns array of inline objects.

classref-item-separator

classref-method

`RID<class_RID>` **get_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_rid>`

Returns TextServer buffer RID.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_get_size>`

Returns size of the bounding box of the text.

classref-item-separator

classref-method

`bool<class_bool>` **has_object**(key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_has_object>`

Returns `true` if an object with `key` is embedded in this line.

classref-item-separator

classref-method

`int<class_int>` **hit_test**(coords: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextLine_method_hit_test>`

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

classref-item-separator

classref-method

`bool<class_bool>` **resize_object**(key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, baseline: `float<class_float>` = 0.0) `🔗<class_TextLine_method_resize_object>`

Sets new size and alignment of embedded object.

classref-item-separator

classref-method

`void (No return value.)` **set_bidi_override**(override: `Array<class_Array>`) `🔗<class_TextLine_method_set_bidi_override>`

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

classref-item-separator

classref-method

`void (No return value.)` **tab_align**(tab_stops: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_TextLine_method_tab_align>`

Aligns text to the given tab-stops.