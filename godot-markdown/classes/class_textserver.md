github_url
hide

# TextServer

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `TextServerExtension<class_TextServerExtension>`

A server interface for font management and text rendering.

classref-introduction-group

## Description

**TextServer** is the API backend for managing fonts and rendering text.

**Note:** This is a low-level API, consider using `TextLine<class_TextLine>`, `TextParagraph<class_TextParagraph>`, and `Font<class_Font>` classes instead.

This is an abstract class, so to get the currently active **TextServer** instance, use the following code:

gdscript

var ts = TextServerManager.get_primary_interface()

csharp

var ts = TextServerManager.GetPrimaryInterface();

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FontAntialiasing**: `🔗<enum_TextServer_FontAntialiasing>`

classref-enumeration-constant

`FontAntialiasing<enum_TextServer_FontAntialiasing>` **FONT_ANTIALIASING_NONE** = `0`

Font glyphs are rasterized as 1-bit bitmaps.

classref-enumeration-constant

`FontAntialiasing<enum_TextServer_FontAntialiasing>` **FONT_ANTIALIASING_GRAY** = `1`

Font glyphs are rasterized as 8-bit grayscale anti-aliased bitmaps.

classref-enumeration-constant

`FontAntialiasing<enum_TextServer_FontAntialiasing>` **FONT_ANTIALIASING_LCD** = `2`

Font glyphs are rasterized for LCD screens.

LCD subpixel layout is determined by the value of the `ProjectSettings.gui/theme/lcd_subpixel_layout<class_ProjectSettings_property_gui/theme/lcd_subpixel_layout>` setting.

LCD subpixel anti-aliasing mode is suitable only for rendering horizontal, unscaled text in 2D.

classref-item-separator

classref-enumeration

enum **FontLCDSubpixelLayout**: `🔗<enum_TextServer_FontLCDSubpixelLayout>`

classref-enumeration-constant

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` **FONT_LCD_SUBPIXEL_LAYOUT_NONE** = `0`

Unknown or unsupported subpixel layout, LCD subpixel antialiasing is disabled.

classref-enumeration-constant

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` **FONT_LCD_SUBPIXEL_LAYOUT_HRGB** = `1`

Horizontal RGB subpixel layout.

classref-enumeration-constant

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` **FONT_LCD_SUBPIXEL_LAYOUT_HBGR** = `2`

Horizontal BGR subpixel layout.

classref-enumeration-constant

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` **FONT_LCD_SUBPIXEL_LAYOUT_VRGB** = `3`

Vertical RGB subpixel layout.

classref-enumeration-constant

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` **FONT_LCD_SUBPIXEL_LAYOUT_VBGR** = `4`

Vertical BGR subpixel layout.

classref-enumeration-constant

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` **FONT_LCD_SUBPIXEL_LAYOUT_MAX** = `5`

Represents the size of the `FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>` enum.

classref-item-separator

classref-enumeration

enum **Direction**: `🔗<enum_TextServer_Direction>`

classref-enumeration-constant

`Direction<enum_TextServer_Direction>` **DIRECTION_AUTO** = `0`

Text direction is determined based on contents and current locale.

classref-enumeration-constant

`Direction<enum_TextServer_Direction>` **DIRECTION_LTR** = `1`

Text is written from left to right.

classref-enumeration-constant

`Direction<enum_TextServer_Direction>` **DIRECTION_RTL** = `2`

Text is written from right to left.

classref-enumeration-constant

`Direction<enum_TextServer_Direction>` **DIRECTION_INHERITED** = `3`

Text writing direction is the same as base string writing direction. Used for BiDi override only.

classref-item-separator

classref-enumeration

enum **Orientation**: `🔗<enum_TextServer_Orientation>`

classref-enumeration-constant

`Orientation<enum_TextServer_Orientation>` **ORIENTATION_HORIZONTAL** = `0`

Text is written horizontally.

classref-enumeration-constant

`Orientation<enum_TextServer_Orientation>` **ORIENTATION_VERTICAL** = `1`

Left to right text is written vertically from top to bottom.

Right to left text is written vertically from bottom to top.

classref-item-separator

classref-enumeration

flags **JustificationFlag**: `🔗<enum_TextServer_JustificationFlag>`

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_NONE** = `0`

Do not justify text.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_KASHIDA** = `1`

Justify text by adding and removing kashidas.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_WORD_BOUND** = `2`

Justify text by changing width of the spaces between the words.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_TRIM_EDGE_SPACES** = `4`

Remove trailing and leading spaces from the justified text.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_AFTER_LAST_TAB** = `8`

Only apply justification to the part of the text after the last tab.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_CONSTRAIN_ELLIPSIS** = `16`

Apply justification to the trimmed line with ellipsis.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_SKIP_LAST_LINE** = `32`

Do not apply justification to the last line of the paragraph.

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS** = `64`

Do not apply justification to the last line of the paragraph with visible characters (takes precedence over `JUSTIFICATION_SKIP_LAST_LINE<class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE>`).

classref-enumeration-constant

`JustificationFlag<enum_TextServer_JustificationFlag>` **JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE** = `128`

Always apply justification to the paragraphs with a single line (`JUSTIFICATION_SKIP_LAST_LINE<class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE>` and `JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS<class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS>` are ignored).

classref-item-separator

classref-enumeration

enum **AutowrapMode**: `🔗<enum_TextServer_AutowrapMode>`

classref-enumeration-constant

`AutowrapMode<enum_TextServer_AutowrapMode>` **AUTOWRAP_OFF** = `0`

Autowrap is disabled.

classref-enumeration-constant

`AutowrapMode<enum_TextServer_AutowrapMode>` **AUTOWRAP_ARBITRARY** = `1`

Wraps the text inside the node's bounding rectangle by allowing to break lines at arbitrary positions, which is useful when very limited space is available.

classref-enumeration-constant

`AutowrapMode<enum_TextServer_AutowrapMode>` **AUTOWRAP_WORD** = `2`

Wraps the text inside the node's bounding rectangle by soft-breaking between words.

classref-enumeration-constant

`AutowrapMode<enum_TextServer_AutowrapMode>` **AUTOWRAP_WORD_SMART** = `3`

Behaves similarly to `AUTOWRAP_WORD<class_TextServer_constant_AUTOWRAP_WORD>`, but force-breaks a word if that single word does not fit in one line.

classref-item-separator

classref-enumeration

flags **LineBreakFlag**: `🔗<enum_TextServer_LineBreakFlag>`

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_NONE** = `0`

Do not break the line.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_MANDATORY** = `1`

Break the line at the line mandatory break characters (e.g. `"\n"`).

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_WORD_BOUND** = `2`

Break the line between the words.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_GRAPHEME_BOUND** = `4`

Break the line between any unconnected graphemes.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_ADAPTIVE** = `8`

Should be used only in conjunction with `BREAK_WORD_BOUND<class_TextServer_constant_BREAK_WORD_BOUND>`, break the line between any unconnected graphemes, if it's impossible to break it between the words.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_TRIM_EDGE_SPACES** = `16`

**Deprecated:** Use `BREAK_TRIM_START_EDGE_SPACES | BREAK_TRIM_END_EDGE_SPACES` instead.

Remove edge spaces from the broken line segments.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_TRIM_INDENT** = `32`

Subtract first line indentation width from all lines after the first one.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_TRIM_START_EDGE_SPACES** = `64`

Remove spaces and line break characters from the start of broken line segments.

E.g, after line breaking, the second segment of the following text `test  \n  next`, is `next` if the flag is set, and `next` if it is not.

classref-enumeration-constant

`LineBreakFlag<enum_TextServer_LineBreakFlag>` **BREAK_TRIM_END_EDGE_SPACES** = `128`

Remove spaces and line break characters from the end of broken line segments.

E.g, after line breaking, the first segment of the following text `test  \n  next`, is `test` if the flag is set, and `test  \n` if it is not.

classref-item-separator

classref-enumeration

enum **VisibleCharactersBehavior**: `🔗<enum_TextServer_VisibleCharactersBehavior>`

classref-enumeration-constant

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **VC_CHARS_BEFORE_SHAPING** = `0`

Trims text before the shaping. e.g, increasing `Label.visible_characters<class_Label_property_visible_characters>` or `RichTextLabel.visible_characters<class_RichTextLabel_property_visible_characters>` value is visually identical to typing the text.

**Note:** In this mode, trimmed text is not processed at all. It is not accounted for in line breaking and size calculations.

classref-enumeration-constant

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **VC_CHARS_AFTER_SHAPING** = `1`

Displays glyphs that are mapped to the first `Label.visible_characters<class_Label_property_visible_characters>` or `RichTextLabel.visible_characters<class_RichTextLabel_property_visible_characters>` characters from the beginning of the text.

classref-enumeration-constant

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **VC_GLYPHS_AUTO** = `2`

Displays `Label.visible_ratio<class_Label_property_visible_ratio>` or `RichTextLabel.visible_ratio<class_RichTextLabel_property_visible_ratio>` glyphs, starting from the left or from the right, depending on `Control.layout_direction<class_Control_property_layout_direction>` value.

classref-enumeration-constant

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **VC_GLYPHS_LTR** = `3`

Displays `Label.visible_ratio<class_Label_property_visible_ratio>` or `RichTextLabel.visible_ratio<class_RichTextLabel_property_visible_ratio>` glyphs, starting from the left.

classref-enumeration-constant

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>` **VC_GLYPHS_RTL** = `4`

Displays `Label.visible_ratio<class_Label_property_visible_ratio>` or `RichTextLabel.visible_ratio<class_RichTextLabel_property_visible_ratio>` glyphs, starting from the right.

classref-item-separator

classref-enumeration

enum **OverrunBehavior**: `🔗<enum_TextServer_OverrunBehavior>`

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_NO_TRIMMING** = `0`

No text trimming is performed.

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_TRIM_CHAR** = `1`

Trims the text per character.

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_TRIM_WORD** = `2`

Trims the text per word.

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_TRIM_ELLIPSIS** = `3`

Trims the text per character and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_TRIM_WORD_ELLIPSIS** = `4`

Trims the text per word and adds an ellipsis to indicate that parts are hidden if trimmed text is 6 characters or longer.

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_TRIM_ELLIPSIS_FORCE** = `5`

Trims the text per character and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.

classref-enumeration-constant

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **OVERRUN_TRIM_WORD_ELLIPSIS_FORCE** = `6`

Trims the text per word and adds an ellipsis to indicate that parts are hidden regardless of trimmed text length.

classref-item-separator

classref-enumeration

flags **TextOverrunFlag**: `🔗<enum_TextServer_TextOverrunFlag>`

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_NO_TRIM** = `0`

No trimming is performed.

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_TRIM** = `1`

Trims the text when it exceeds the given width.

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_TRIM_WORD_ONLY** = `2`

Trims the text per word instead of per grapheme.

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_ADD_ELLIPSIS** = `4`

Determines whether an ellipsis should be added at the end of the text.

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_ENFORCE_ELLIPSIS** = `8`

Determines whether the ellipsis at the end of the text is enforced and may not be hidden.

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_JUSTIFICATION_AWARE** = `16`

Accounts for the text being justified before attempting to trim it (see `JustificationFlag<enum_TextServer_JustificationFlag>`).

classref-enumeration-constant

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>` **OVERRUN_SHORT_STRING_ELLIPSIS** = `32`

Determines whether the ellipsis should be added regardless of the string length, otherwise it is added only if the string is 6 characters or longer.

classref-item-separator

classref-enumeration

flags **GraphemeFlag**: `🔗<enum_TextServer_GraphemeFlag>`

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_VALID** = `1`

Grapheme is supported by the font, and can be drawn.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_RTL** = `2`

Grapheme is part of right-to-left or bottom-to-top run.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_VIRTUAL** = `4`

Grapheme is not part of source text, it was added by justification process.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_SPACE** = `8`

Grapheme is whitespace.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_BREAK_HARD** = `16`

Grapheme is mandatory break point (e.g. `"\n"`).

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_BREAK_SOFT** = `32`

Grapheme is optional break point (e.g. space).

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_TAB** = `64`

Grapheme is the tabulation character.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_ELONGATION** = `128`

Grapheme is kashida.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_PUNCTUATION** = `256`

Grapheme is punctuation character.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_UNDERSCORE** = `512`

Grapheme is underscore character.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_CONNECTED** = `1024`

Grapheme is connected to the previous grapheme. Breaking line before this grapheme is not safe.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL** = `2048`

It is safe to insert a U+0640 before this grapheme for elongation.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_EMBEDDED_OBJECT** = `4096`

Grapheme is an object replacement character for the embedded object.

classref-enumeration-constant

`GraphemeFlag<enum_TextServer_GraphemeFlag>` **GRAPHEME_IS_SOFT_HYPHEN** = `8192`

Grapheme is a soft hyphen.

classref-item-separator

classref-enumeration

enum **Hinting**: `🔗<enum_TextServer_Hinting>`

classref-enumeration-constant

`Hinting<enum_TextServer_Hinting>` **HINTING_NONE** = `0`

Disables font hinting (smoother but less crisp).

classref-enumeration-constant

`Hinting<enum_TextServer_Hinting>` **HINTING_LIGHT** = `1`

Use the light font hinting mode.

classref-enumeration-constant

`Hinting<enum_TextServer_Hinting>` **HINTING_NORMAL** = `2`

Use the default font hinting mode (crisper but less smooth).

**Note:** This hinting mode changes both horizontal and vertical glyph metrics. If applied to monospace font, some glyphs might have different width.

classref-item-separator

classref-enumeration

enum **SubpixelPositioning**: `🔗<enum_TextServer_SubpixelPositioning>`

classref-enumeration-constant

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **SUBPIXEL_POSITIONING_DISABLED** = `0`

Glyph horizontal position is rounded to the whole pixel size, each glyph is rasterized once.

classref-enumeration-constant

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **SUBPIXEL_POSITIONING_AUTO** = `1`

Glyph horizontal position is rounded based on font size.

- To one quarter of the pixel size if font size is smaller or equal to `SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE<class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE>`.
- To one half of the pixel size if font size is smaller or equal to `SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE<class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE>`.
- To the whole pixel size for larger fonts.

classref-enumeration-constant

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **SUBPIXEL_POSITIONING_ONE_HALF** = `2`

Glyph horizontal position is rounded to one half of the pixel size, each glyph is rasterized up to two times.

classref-enumeration-constant

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **SUBPIXEL_POSITIONING_ONE_QUARTER** = `3`

Glyph horizontal position is rounded to one quarter of the pixel size, each glyph is rasterized up to four times.

classref-enumeration-constant

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE** = `20`

Maximum font size which will use "one half of the pixel" subpixel positioning in `SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>` mode.

classref-enumeration-constant

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE** = `16`

Maximum font size which will use "one quarter of the pixel" subpixel positioning in `SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>` mode.

classref-item-separator

classref-enumeration

enum **Feature**: `🔗<enum_TextServer_Feature>`

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_SIMPLE_LAYOUT** = `1`

TextServer supports simple text layouts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_BIDI_LAYOUT** = `2`

TextServer supports bidirectional text layouts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_VERTICAL_LAYOUT** = `4`

TextServer supports vertical layouts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_SHAPING** = `8`

TextServer supports complex text shaping.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_KASHIDA_JUSTIFICATION** = `16`

TextServer supports justification using kashidas.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_BREAK_ITERATORS** = `32`

TextServer supports complex line/word breaking rules (e.g. dictionary based).

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_FONT_BITMAP** = `64`

TextServer supports loading bitmap fonts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_FONT_DYNAMIC** = `128`

TextServer supports loading dynamic (TrueType, OpeType, etc.) fonts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_FONT_MSDF** = `256`

TextServer supports multichannel signed distance field dynamic font rendering.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_FONT_SYSTEM** = `512`

TextServer supports loading system fonts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_FONT_VARIABLE** = `1024`

TextServer supports variable fonts.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION** = `2048`

TextServer supports locale dependent and context sensitive case conversion.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_USE_SUPPORT_DATA** = `4096`

TextServer require external data file for some features, see `load_support_data()<class_TextServer_method_load_support_data>`.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_UNICODE_IDENTIFIERS** = `8192`

TextServer supports UAX \#31 identifier validation, see `is_valid_identifier()<class_TextServer_method_is_valid_identifier>`.

classref-enumeration-constant

`Feature<enum_TextServer_Feature>` **FEATURE_UNICODE_SECURITY** = `16384`

TextServer supports [Unicode Technical Report \#36](https://unicode.org/reports/tr36/) and [Unicode Technical Standard \#39](https://unicode.org/reports/tr39/) based spoof detection features.

classref-item-separator

classref-enumeration

enum **ContourPointTag**: `🔗<enum_TextServer_ContourPointTag>`

classref-enumeration-constant

`ContourPointTag<enum_TextServer_ContourPointTag>` **CONTOUR_CURVE_TAG_ON** = `1`

Contour point is on the curve.

classref-enumeration-constant

`ContourPointTag<enum_TextServer_ContourPointTag>` **CONTOUR_CURVE_TAG_OFF_CONIC** = `0`

Contour point isn't on the curve, but serves as a control point for a conic (quadratic) Bézier arc.

classref-enumeration-constant

`ContourPointTag<enum_TextServer_ContourPointTag>` **CONTOUR_CURVE_TAG_OFF_CUBIC** = `2`

Contour point isn't on the curve, but serves as a control point for a cubic Bézier arc.

classref-item-separator

classref-enumeration

enum **SpacingType**: `🔗<enum_TextServer_SpacingType>`

classref-enumeration-constant

`SpacingType<enum_TextServer_SpacingType>` **SPACING_GLYPH** = `0`

Spacing for each glyph.

classref-enumeration-constant

`SpacingType<enum_TextServer_SpacingType>` **SPACING_SPACE** = `1`

Spacing for the space character.

classref-enumeration-constant

`SpacingType<enum_TextServer_SpacingType>` **SPACING_TOP** = `2`

Spacing at the top of the line.

classref-enumeration-constant

`SpacingType<enum_TextServer_SpacingType>` **SPACING_BOTTOM** = `3`

Spacing at the bottom of the line.

classref-enumeration-constant

`SpacingType<enum_TextServer_SpacingType>` **SPACING_MAX** = `4`

Represents the size of the `SpacingType<enum_TextServer_SpacingType>` enum.

classref-item-separator

classref-enumeration

flags **FontStyle**: `🔗<enum_TextServer_FontStyle>`

classref-enumeration-constant

`FontStyle<enum_TextServer_FontStyle>` **FONT_BOLD** = `1`

Font is bold.

classref-enumeration-constant

`FontStyle<enum_TextServer_FontStyle>` **FONT_ITALIC** = `2`

Font is italic or oblique.

classref-enumeration-constant

`FontStyle<enum_TextServer_FontStyle>` **FONT_FIXED_WIDTH** = `4`

Font has fixed-width characters (also known as monospace).

classref-item-separator

classref-enumeration

enum **StructuredTextParser**: `🔗<enum_TextServer_StructuredTextParser>`

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_DEFAULT** = `0`

Use default Unicode BiDi algorithm.

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_URI** = `1`

BiDi override for URI.

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_FILE** = `2`

BiDi override for file path.

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_EMAIL** = `3`

BiDi override for email.

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_LIST** = `4`

BiDi override for lists. Structured text options: list separator `String<class_String>`.

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_GDSCRIPT** = `5`

BiDi override for GDScript.

classref-enumeration-constant

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **STRUCTURED_TEXT_CUSTOM** = `6`

User defined structured text BiDi override function.

classref-item-separator

classref-enumeration

enum **FixedSizeScaleMode**: `🔗<enum_TextServer_FixedSizeScaleMode>`

classref-enumeration-constant

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **FIXED_SIZE_SCALE_DISABLE** = `0`

Bitmap font is not scaled.

classref-enumeration-constant

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **FIXED_SIZE_SCALE_INTEGER_ONLY** = `1`

Bitmap font is scaled to the closest integer multiple of the font's fixed size. This is the recommended option for pixel art fonts.

classref-enumeration-constant

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **FIXED_SIZE_SCALE_ENABLED** = `2`

Bitmap font is scaled to an arbitrary (fractional) size. This is the recommended option for non-pixel art fonts.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **create_font**() `🔗<class_TextServer_method_create_font>`

Creates a new, empty font cache entry resource. To free the resulting resource, use the `free_rid()<class_TextServer_method_free_rid>` method.

classref-item-separator

classref-method

`RID<class_RID>` **create_font_linked_variation**(font_rid: `RID<class_RID>`) `🔗<class_TextServer_method_create_font_linked_variation>`

Creates a new variation existing font which is reusing the same glyph cache and font data. To free the resulting resource, use the `free_rid()<class_TextServer_method_free_rid>` method.

classref-item-separator

classref-method

`RID<class_RID>` **create_shaped_text**(direction: `Direction<enum_TextServer_Direction>` = 0, orientation: `Orientation<enum_TextServer_Orientation>` = 0) `🔗<class_TextServer_method_create_shaped_text>`

Creates a new buffer for complex text layout, with the given `direction` and `orientation`. To free the resulting buffer, use `free_rid()<class_TextServer_method_free_rid>` method.

**Note:** Direction is ignored if server does not support `FEATURE_BIDI_LAYOUT<class_TextServer_constant_FEATURE_BIDI_LAYOUT>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

**Note:** Orientation is ignored if server does not support `FEATURE_VERTICAL_LAYOUT<class_TextServer_constant_FEATURE_VERTICAL_LAYOUT>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

classref-item-separator

classref-method

`void (No return value.)` **draw_hex_code_box**(canvas: `RID<class_RID>`, size: `int<class_int>`, pos: `Vector2<class_Vector2>`, index: `int<class_int>`, color: `Color<class_Color>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_draw_hex_code_box>`

Draws box displaying character hexadecimal code. Used for replacing missing characters.

classref-item-separator

classref-method

`void (No return value.)` **font_clear_glyphs**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `🔗<class_TextServer_method_font_clear_glyphs>`

Removes all rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use `font_remove_texture()<class_TextServer_method_font_remove_texture>` to remove them manually.

classref-item-separator

classref-method

`void (No return value.)` **font_clear_kerning_map**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `🔗<class_TextServer_method_font_clear_kerning_map>`

Removes all kerning overrides.

classref-item-separator

classref-method

`void (No return value.)` **font_clear_size_cache**(font_rid: `RID<class_RID>`) `🔗<class_TextServer_method_font_clear_size_cache>`

Removes all font sizes from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **font_clear_system_fallback_cache**() `🔗<class_TextServer_method_font_clear_system_fallback_cache>`

Frees all automatically loaded system fonts.

classref-item-separator

classref-method

`void (No return value.)` **font_clear_textures**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `🔗<class_TextServer_method_font_clear_textures>`

Removes all textures from font cache entry.

**Note:** This function will not remove glyphs associated with the texture, use `font_remove_glyph()<class_TextServer_method_font_remove_glyph>` to remove them manually.

classref-item-separator

classref-method

`void (No return value.)` **font_draw_glyph**(font_rid: `RID<class_RID>`, canvas: `RID<class_RID>`, size: `int<class_int>`, pos: `Vector2<class_Vector2>`, index: `int<class_int>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_draw_glyph>`

Draws single glyph into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Glyph index is specific to the font, use glyphs indices returned by `shaped_text_get_glyphs()<class_TextServer_method_shaped_text_get_glyphs>` or `font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`.

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

classref-item-separator

classref-method

`void (No return value.)` **font_draw_glyph_outline**(font_rid: `RID<class_RID>`, canvas: `RID<class_RID>`, size: `int<class_int>`, outline_size: `int<class_int>`, pos: `Vector2<class_Vector2>`, index: `int<class_int>`, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_draw_glyph_outline>`

Draws single glyph outline of size `outline_size` into a canvas item at the position, using `font_rid` at the size `size`. If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

**Note:** Glyph index is specific to the font, use glyphs indices returned by `shaped_text_get_glyphs()<class_TextServer_method_shaped_text_get_glyphs>` or `font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`.

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

classref-item-separator

classref-method

`FontAntialiasing<enum_TextServer_FontAntialiasing>` **font_get_antialiasing**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_antialiasing>`

Returns font anti-aliasing mode.

classref-item-separator

classref-method

`float<class_float>` **font_get_ascent**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_ascent>`

Returns the font ascent (number of pixels above the baseline).

classref-item-separator

classref-method

`float<class_float>` **font_get_baseline_offset**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_baseline_offset>`

Returns extra baseline offset (as a fraction of font height).

classref-item-separator

classref-method

`int<class_int>` **font_get_char_from_glyph_index**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_char_from_glyph_index>`

Returns character code associated with `glyph_index`, or `0` if `glyph_index` is invalid. See `font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`.

classref-item-separator

classref-method

`float<class_float>` **font_get_descent**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_descent>`

Returns the font descent (number of pixels below the baseline).

classref-item-separator

classref-method

`bool<class_bool>` **font_get_disable_embedded_bitmaps**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_disable_embedded_bitmaps>`

Returns whether the font's embedded bitmap loading is disabled.

classref-item-separator

classref-method

`float<class_float>` **font_get_embolden**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_embolden>`

Returns font embolden strength.

classref-item-separator

classref-method

`int<class_int>` **font_get_face_count**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_face_count>`

Returns number of faces in the TrueType / OpenType collection.

classref-item-separator

classref-method

`int<class_int>` **font_get_face_index**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_face_index>`

Returns an active face index in the TrueType / OpenType collection.

classref-item-separator

classref-method

`int<class_int>` **font_get_fixed_size**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_fixed_size>`

Returns bitmap font fixed size.

classref-item-separator

classref-method

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>` **font_get_fixed_size_scale_mode**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_fixed_size_scale_mode>`

Returns bitmap font scaling mode.

classref-item-separator

classref-method

`bool<class_bool>` **font_get_generate_mipmaps**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_generate_mipmaps>`

Returns `true` if font texture mipmap generation is enabled.

classref-item-separator

classref-method

`float<class_float>` **font_get_global_oversampling**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_global_oversampling>`

**Deprecated:** Use `Viewport<class_Viewport>` oversampling, or the `oversampling` argument of the `draw_*` methods instead.

This method does nothing and always returns `1.0`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **font_get_glyph_advance**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_advance>`

Returns glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **font_get_glyph_contours**(font: `RID<class_RID>`, size: `int<class_int>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_contours>`

Returns outline contours of the glyph as a `Dictionary<class_Dictionary>` with the following contents:

`points` - `PackedVector3Array<class_PackedVector3Array>`, containing outline points. `x` and `y` are point coordinates. `z` is the type of the point, using the `ContourPointTag<enum_TextServer_ContourPointTag>` values.

`contours` - `PackedInt32Array<class_PackedInt32Array>`, containing indices the end points of each contour.

`orientation` - `bool<class_bool>`, contour orientation. If `true`, clockwise contours must be filled.

- Two successive `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>` points indicate a line segment.
- One `CONTOUR_CURVE_TAG_OFF_CONIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC>` point between two `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>` points indicates a single conic (quadratic) Bézier arc.
- Two `CONTOUR_CURVE_TAG_OFF_CUBIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CUBIC>` points between two `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>` points indicate a single cubic Bézier arc.
- Two successive `CONTOUR_CURVE_TAG_OFF_CONIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC>` points indicate two successive conic (quadratic) Bézier arcs with a virtual `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>` point at their middle.
- Each contour is closed. The last point of a contour uses the first point of a contour as its next point, and vice versa. The first point can be `CONTOUR_CURVE_TAG_OFF_CONIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC>` point.

classref-item-separator

classref-method

`int<class_int>` **font_get_glyph_index**(font_rid: `RID<class_RID>`, size: `int<class_int>`, char: `int<class_int>`, variation_selector: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_index>`

Returns the glyph index of a `char`, optionally modified by the `variation_selector`. See `font_get_char_from_glyph_index()<class_TextServer_method_font_get_char_from_glyph_index>`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **font_get_glyph_list**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_list>`

Returns list of rendered glyphs in the cache entry.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **font_get_glyph_offset**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_offset>`

Returns glyph offset from the baseline.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **font_get_glyph_size**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_size>`

Returns size of the glyph.

classref-item-separator

classref-method

`int<class_int>` **font_get_glyph_texture_idx**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_texture_idx>`

Returns index of the cache texture containing the glyph.

classref-item-separator

classref-method

`RID<class_RID>` **font_get_glyph_texture_rid**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_texture_rid>`

Returns resource ID of the cache texture containing the glyph.

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **font_get_glyph_texture_size**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_texture_size>`

Returns size of the cache texture containing the glyph.

**Note:** If there are pending glyphs to render, calling this function might trigger the texture cache update.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **font_get_glyph_uv_rect**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_glyph_uv_rect>`

Returns rectangle in the cache texture containing the glyph.

classref-item-separator

classref-method

`Hinting<enum_TextServer_Hinting>` **font_get_hinting**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_hinting>`

Returns the font hinting mode. Used by dynamic fonts only.

classref-item-separator

classref-method

`bool<class_bool>` **font_get_keep_rounding_remainders**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_keep_rounding_remainders>`

Returns glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **font_get_kerning**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_kerning>`

Returns kerning for the pair of glyphs.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **font_get_kerning_list**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_kerning_list>`

Returns list of the kerning overrides.

classref-item-separator

classref-method

`bool<class_bool>` **font_get_language_support_override**(font_rid: `RID<class_RID>`, language: `String<class_String>`) `🔗<class_TextServer_method_font_get_language_support_override>`

Returns `true` if support override is enabled for the `language`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **font_get_language_support_overrides**(font_rid: `RID<class_RID>`) `🔗<class_TextServer_method_font_get_language_support_overrides>`

Returns list of language support overrides.

classref-item-separator

classref-method

`int<class_int>` **font_get_msdf_pixel_range**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_msdf_pixel_range>`

Returns the width of the range around the shape between the minimum and maximum representable signed distance.

classref-item-separator

classref-method

`int<class_int>` **font_get_msdf_size**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_msdf_size>`

Returns source font size used to generate MSDF textures.

classref-item-separator

classref-method

`String<class_String>` **font_get_name**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_name>`

Returns font family name.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **font_get_opentype_feature_overrides**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_opentype_feature_overrides>`

Returns font OpenType feature set override.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **font_get_ot_name_strings**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_ot_name_strings>`

Returns `Dictionary<class_Dictionary>` with OpenType font name strings (localized font names, version, description, license information, sample text, etc.).

classref-item-separator

classref-method

`float<class_float>` **font_get_oversampling**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_oversampling>`

Returns oversampling factor override. If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See `Viewport.oversampling<class_Viewport_property_oversampling>`. This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

classref-item-separator

classref-method

`PackedColorArray<class_PackedColorArray>` **font_get_palette_colors**(font_rid: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_palette_colors>`

Returns the array in the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors. Colors can be overridden using `font_set_palette_custom_colors()<class_TextServer_method_font_set_palette_custom_colors>`.

classref-item-separator

classref-method

`int<class_int>` **font_get_palette_count**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_palette_count>`

Returns the number of predefined color palettes. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

classref-item-separator

classref-method

`PackedColorArray<class_PackedColorArray>` **font_get_palette_custom_colors**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_palette_custom_colors>`

Returns array of custom colors to override predefined palette.

classref-item-separator

classref-method

`String<class_String>` **font_get_palette_name**(font_rid: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_palette_name>`

Returns the name of the predefined color palette at `index`. Palette contains all colors used to render font glyphs. Each palette has the same number of colors.

classref-item-separator

classref-method

`float<class_float>` **font_get_scale**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_scale>`

Returns scaling factor of the color bitmap font.

classref-item-separator

classref-method

`bool<class_bool>` **font_get_script_support_override**(font_rid: `RID<class_RID>`, script: `String<class_String>`) `🔗<class_TextServer_method_font_get_script_support_override>`

Returns `true` if support override is enabled for the `script`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **font_get_script_support_overrides**(font_rid: `RID<class_RID>`) `🔗<class_TextServer_method_font_get_script_support_overrides>`

Returns list of script support overrides.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **font_get_size_cache_info**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_size_cache_info>`

Returns font cache information, each entry contains the following fields: `Vector2i size_px` - font size in pixels, `float viewport_oversampling` - viewport oversampling factor, `int glyphs` - number of rendered glyphs, `int textures` - number of used textures, `int textures_size` - size of texture data in bytes.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **font_get_size_cache_list**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_size_cache_list>`

Returns list of the font sizes in the cache. Each size is `Vector2i<class_Vector2i>` with font size and outline size.

classref-item-separator

classref-method

`int<class_int>` **font_get_spacing**(font_rid: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_spacing>`

Returns the spacing for `spacing` in pixels (not relative to the font size).

classref-item-separator

classref-method

`int<class_int>` **font_get_stretch**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_stretch>`

Returns font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

classref-item-separator

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\] **font_get_style**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_style>`

Returns font style flags.

classref-item-separator

classref-method

`String<class_String>` **font_get_style_name**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_style_name>`

Returns font style name.

classref-item-separator

classref-method

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>` **font_get_subpixel_positioning**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_subpixel_positioning>`

Returns font subpixel glyph positioning mode.

classref-item-separator

classref-method

`String<class_String>` **font_get_supported_chars**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_supported_chars>`

Returns a string containing all the characters available in the font.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **font_get_supported_glyphs**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_supported_glyphs>`

Returns an array containing all glyph indices in the font.

classref-item-separator

classref-method

`int<class_int>` **font_get_texture_count**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_texture_count>`

Returns number of textures used by font cache entry.

classref-item-separator

classref-method

`Image<class_Image>` **font_get_texture_image**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_texture_image>`

Returns font cache texture image data.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **font_get_texture_offsets**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_texture_offsets>`

Returns array containing glyph packing data.

classref-item-separator

classref-method

`Transform2D<class_Transform2D>` **font_get_transform**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_transform>`

Returns 2D transform applied to the font outlines.

classref-item-separator

classref-method

`float<class_float>` **font_get_underline_position**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **font_get_underline_thickness**(font_rid: `RID<class_RID>`, size: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_underline_thickness>`

Returns thickness of the underline in pixels.

classref-item-separator

classref-method

`int<class_int>` **font_get_used_palette**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_used_palette>`

Returns used palette index.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **font_get_variation_coordinates**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_variation_coordinates>`

Returns variation coordinates for the specified font cache entry. See `font_supported_variation_list()<class_TextServer_method_font_supported_variation_list>` for more info.

classref-item-separator

classref-method

`int<class_int>` **font_get_weight**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_get_weight>`

Returns weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

classref-item-separator

classref-method

`bool<class_bool>` **font_has_char**(font_rid: `RID<class_RID>`, char: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_has_char>`

Returns `true` if a Unicode `char` is available in the font.

classref-item-separator

classref-method

`bool<class_bool>` **font_is_allow_system_fallback**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_is_allow_system_fallback>`

Returns `true` if system fonts can be automatically used as fallbacks.

classref-item-separator

classref-method

`bool<class_bool>` **font_is_force_autohinter**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_is_force_autohinter>`

Returns `true` if auto-hinting is supported and preferred over font built-in hinting. Used by dynamic fonts only.

classref-item-separator

classref-method

`bool<class_bool>` **font_is_language_supported**(font_rid: `RID<class_RID>`, language: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_is_language_supported>`

Returns `true` if the font supports the given language (as a [ISO 639](https://en.wikipedia.org/wiki/ISO_639-1) code).

classref-item-separator

classref-method

`bool<class_bool>` **font_is_modulate_color_glyphs**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_is_modulate_color_glyphs>`

Returns `true` if color modulation is applied when drawing the font's colored glyphs.

classref-item-separator

classref-method

`bool<class_bool>` **font_is_multichannel_signed_distance_field**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_is_multichannel_signed_distance_field>`

Returns `true` if glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data.

classref-item-separator

classref-method

`bool<class_bool>` **font_is_script_supported**(font_rid: `RID<class_RID>`, script: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_is_script_supported>`

Returns `true` if the font supports the given script (as a [ISO 15924](https://en.wikipedia.org/wiki/ISO_15924) code).

classref-item-separator

classref-method

`void (No return value.)` **font_remove_glyph**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`) `🔗<class_TextServer_method_font_remove_glyph>`

Removes specified rendered glyph information from the cache entry.

**Note:** This function will not remove textures associated with the glyphs, use `font_remove_texture()<class_TextServer_method_font_remove_texture>` to remove them manually.

classref-item-separator

classref-method

`void (No return value.)` **font_remove_kerning**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`) `🔗<class_TextServer_method_font_remove_kerning>`

Removes kerning override for the pair of glyphs.

classref-item-separator

classref-method

`void (No return value.)` **font_remove_language_support_override**(font_rid: `RID<class_RID>`, language: `String<class_String>`) `🔗<class_TextServer_method_font_remove_language_support_override>`

Remove language support override.

classref-item-separator

classref-method

`void (No return value.)` **font_remove_script_support_override**(font_rid: `RID<class_RID>`, script: `String<class_String>`) `🔗<class_TextServer_method_font_remove_script_support_override>`

Removes script support override.

classref-item-separator

classref-method

`void (No return value.)` **font_remove_size_cache**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`) `🔗<class_TextServer_method_font_remove_size_cache>`

Removes specified font size from the cache entry.

classref-item-separator

classref-method

`void (No return value.)` **font_remove_texture**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`) `🔗<class_TextServer_method_font_remove_texture>`

Removes specified texture from the cache entry.

**Note:** This function will not remove glyphs associated with the texture, remove them manually, using `font_remove_glyph()<class_TextServer_method_font_remove_glyph>`.

classref-item-separator

classref-method

`void (No return value.)` **font_render_glyph**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, index: `int<class_int>`) `🔗<class_TextServer_method_font_render_glyph>`

Renders specified glyph to the font cache texture.

classref-item-separator

classref-method

`void (No return value.)` **font_render_range**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, start: `int<class_int>`, end: `int<class_int>`) `🔗<class_TextServer_method_font_render_range>`

Renders the range of characters to the font cache texture.

classref-item-separator

classref-method

`void (No return value.)` **font_set_allow_system_fallback**(font_rid: `RID<class_RID>`, allow_system_fallback: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_allow_system_fallback>`

If set to `true`, system fonts can be automatically used as fallbacks.

classref-item-separator

classref-method

`void (No return value.)` **font_set_antialiasing**(font_rid: `RID<class_RID>`, antialiasing: `FontAntialiasing<enum_TextServer_FontAntialiasing>`) `🔗<class_TextServer_method_font_set_antialiasing>`

Sets font anti-aliasing mode.

classref-item-separator

classref-method

`void (No return value.)` **font_set_ascent**(font_rid: `RID<class_RID>`, size: `int<class_int>`, ascent: `float<class_float>`) `🔗<class_TextServer_method_font_set_ascent>`

Sets the font ascent (number of pixels above the baseline).

classref-item-separator

classref-method

`void (No return value.)` **font_set_baseline_offset**(font_rid: `RID<class_RID>`, baseline_offset: `float<class_float>`) `🔗<class_TextServer_method_font_set_baseline_offset>`

Sets extra baseline offset (as a fraction of font height).

classref-item-separator

classref-method

`void (No return value.)` **font_set_data**(font_rid: `RID<class_RID>`, data: `PackedByteArray<class_PackedByteArray>`) `🔗<class_TextServer_method_font_set_data>`

Sets font source data, e.g contents of the dynamic font source file.

classref-item-separator

classref-method

`void (No return value.)` **font_set_descent**(font_rid: `RID<class_RID>`, size: `int<class_int>`, descent: `float<class_float>`) `🔗<class_TextServer_method_font_set_descent>`

Sets the font descent (number of pixels below the baseline).

classref-item-separator

classref-method

`void (No return value.)` **font_set_disable_embedded_bitmaps**(font_rid: `RID<class_RID>`, disable_embedded_bitmaps: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_disable_embedded_bitmaps>`

If set to `true`, embedded font bitmap loading is disabled (bitmap-only and color fonts ignore this property).

classref-item-separator

classref-method

`void (No return value.)` **font_set_embolden**(font_rid: `RID<class_RID>`, strength: `float<class_float>`) `🔗<class_TextServer_method_font_set_embolden>`

Sets font embolden strength. If `strength` is not equal to zero, emboldens the font outlines. Negative values reduce the outline thickness.

classref-item-separator

classref-method

`void (No return value.)` **font_set_face_index**(font_rid: `RID<class_RID>`, face_index: `int<class_int>`) `🔗<class_TextServer_method_font_set_face_index>`

Sets an active face index in the TrueType / OpenType collection.

classref-item-separator

classref-method

`void (No return value.)` **font_set_fixed_size**(font_rid: `RID<class_RID>`, fixed_size: `int<class_int>`) `🔗<class_TextServer_method_font_set_fixed_size>`

Sets bitmap font fixed size. If set to value greater than zero, same cache entry will be used for all font sizes.

classref-item-separator

classref-method

`void (No return value.)` **font_set_fixed_size_scale_mode**(font_rid: `RID<class_RID>`, fixed_size_scale_mode: `FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`) `🔗<class_TextServer_method_font_set_fixed_size_scale_mode>`

Sets bitmap font scaling mode. This property is used only if `fixed_size` is greater than zero.

classref-item-separator

classref-method

`void (No return value.)` **font_set_force_autohinter**(font_rid: `RID<class_RID>`, force_autohinter: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_force_autohinter>`

If set to `true` auto-hinting is preferred over font built-in hinting.

classref-item-separator

classref-method

`void (No return value.)` **font_set_generate_mipmaps**(font_rid: `RID<class_RID>`, generate_mipmaps: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_generate_mipmaps>`

If set to `true` font texture mipmap generation is enabled.

classref-item-separator

classref-method

`void (No return value.)` **font_set_global_oversampling**(oversampling: `float<class_float>`) `🔗<class_TextServer_method_font_set_global_oversampling>`

**Deprecated:** Use `Viewport<class_Viewport>` oversampling, or the `oversampling` argument of the `draw_*` methods instead.

This method does nothing.

classref-item-separator

classref-method

`void (No return value.)` **font_set_glyph_advance**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph: `int<class_int>`, advance: `Vector2<class_Vector2>`) `🔗<class_TextServer_method_font_set_glyph_advance>`

Sets glyph advance (offset of the next glyph).

**Note:** Advance for glyphs outlines is the same as the base glyph advance and is not saved.

classref-item-separator

classref-method

`void (No return value.)` **font_set_glyph_offset**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, offset: `Vector2<class_Vector2>`) `🔗<class_TextServer_method_font_set_glyph_offset>`

Sets glyph offset from the baseline.

classref-item-separator

classref-method

`void (No return value.)` **font_set_glyph_size**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, gl_size: `Vector2<class_Vector2>`) `🔗<class_TextServer_method_font_set_glyph_size>`

Sets size of the glyph.

classref-item-separator

classref-method

`void (No return value.)` **font_set_glyph_texture_idx**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, texture_idx: `int<class_int>`) `🔗<class_TextServer_method_font_set_glyph_texture_idx>`

Sets index of the cache texture containing the glyph.

classref-item-separator

classref-method

`void (No return value.)` **font_set_glyph_uv_rect**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, glyph: `int<class_int>`, uv_rect: `Rect2<class_Rect2>`) `🔗<class_TextServer_method_font_set_glyph_uv_rect>`

Sets rectangle in the cache texture containing the glyph.

classref-item-separator

classref-method

`void (No return value.)` **font_set_hinting**(font_rid: `RID<class_RID>`, hinting: `Hinting<enum_TextServer_Hinting>`) `🔗<class_TextServer_method_font_set_hinting>`

Sets font hinting mode. Used by dynamic fonts only.

classref-item-separator

classref-method

`void (No return value.)` **font_set_keep_rounding_remainders**(font_rid: `RID<class_RID>`, keep_rounding_remainders: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_keep_rounding_remainders>`

Sets glyph position rounding behavior. If set to `true`, when aligning glyphs to the pixel boundaries rounding remainders are accumulated to ensure more uniform glyph distribution. This setting has no effect if subpixel positioning is enabled.

classref-item-separator

classref-method

`void (No return value.)` **font_set_kerning**(font_rid: `RID<class_RID>`, size: `int<class_int>`, glyph_pair: `Vector2i<class_Vector2i>`, kerning: `Vector2<class_Vector2>`) `🔗<class_TextServer_method_font_set_kerning>`

Sets kerning for the pair of glyphs.

classref-item-separator

classref-method

`void (No return value.)` **font_set_language_support_override**(font_rid: `RID<class_RID>`, language: `String<class_String>`, supported: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_language_support_override>`

Adds override for `font_is_language_supported()<class_TextServer_method_font_is_language_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **font_set_modulate_color_glyphs**(font_rid: `RID<class_RID>`, modulate: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_modulate_color_glyphs>`

If set to `true`, color modulation is applied when drawing colored glyphs, otherwise it's applied to the monochrome glyphs only.

classref-item-separator

classref-method

`void (No return value.)` **font_set_msdf_pixel_range**(font_rid: `RID<class_RID>`, msdf_pixel_range: `int<class_int>`) `🔗<class_TextServer_method_font_set_msdf_pixel_range>`

Sets the width of the range around the shape between the minimum and maximum representable signed distance.

classref-item-separator

classref-method

`void (No return value.)` **font_set_msdf_size**(font_rid: `RID<class_RID>`, msdf_size: `int<class_int>`) `🔗<class_TextServer_method_font_set_msdf_size>`

Sets source font size used to generate MSDF textures.

classref-item-separator

classref-method

`void (No return value.)` **font_set_multichannel_signed_distance_field**(font_rid: `RID<class_RID>`, msdf: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_multichannel_signed_distance_field>`

If set to `true`, glyphs of all sizes are rendered using single multichannel signed distance field generated from the dynamic font vector data. MSDF rendering allows displaying the font at any scaling factor without blurriness, and without incurring a CPU cost when the font size changes (since the font no longer needs to be rasterized on the CPU). As a downside, font hinting is not available with MSDF. The lack of font hinting may result in less crisp and less readable fonts at small sizes.

**Note:** MSDF font rendering does not render glyphs with overlapping shapes correctly. Overlapping shapes are not valid per the OpenType standard, but are still commonly found in many font files, especially those converted by Google Fonts. To avoid issues with overlapping glyphs, consider downloading the font file directly from the type foundry instead of relying on Google Fonts.

classref-item-separator

classref-method

`void (No return value.)` **font_set_name**(font_rid: `RID<class_RID>`, name: `String<class_String>`) `🔗<class_TextServer_method_font_set_name>`

Sets the font family name.

classref-item-separator

classref-method

`void (No return value.)` **font_set_opentype_feature_overrides**(font_rid: `RID<class_RID>`, overrides: `Dictionary<class_Dictionary>`) `🔗<class_TextServer_method_font_set_opentype_feature_overrides>`

Sets font OpenType feature set override.

classref-item-separator

classref-method

`void (No return value.)` **font_set_oversampling**(font_rid: `RID<class_RID>`, oversampling: `float<class_float>`) `🔗<class_TextServer_method_font_set_oversampling>`

If set to a positive value, overrides the oversampling factor of the viewport this font is used in. See `Viewport.oversampling<class_Viewport_property_oversampling>`. This value doesn't override the `oversampling` parameter of `draw_*` methods. Used by dynamic fonts only.

classref-item-separator

classref-method

`void (No return value.)` **font_set_palette_custom_colors**(font_rid: `RID<class_RID>`, colors: `PackedColorArray<class_PackedColorArray>`) `🔗<class_TextServer_method_font_set_palette_custom_colors>`

Sets array of custom colors to override predefined palette. Set to empty array to reset overrides. Use `Color(0, 0, 0, 0)`, to keep predefined palette color at specific position.

classref-item-separator

classref-method

`void (No return value.)` **font_set_scale**(font_rid: `RID<class_RID>`, size: `int<class_int>`, scale: `float<class_float>`) `🔗<class_TextServer_method_font_set_scale>`

Sets scaling factor of the color bitmap font.

classref-item-separator

classref-method

`void (No return value.)` **font_set_script_support_override**(font_rid: `RID<class_RID>`, script: `String<class_String>`, supported: `bool<class_bool>`) `🔗<class_TextServer_method_font_set_script_support_override>`

Adds override for `font_is_script_supported()<class_TextServer_method_font_is_script_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **font_set_spacing**(font_rid: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`, value: `int<class_int>`) `🔗<class_TextServer_method_font_set_spacing>`

Sets the spacing for `spacing` to `value` in pixels (not relative to the font size).

classref-item-separator

classref-method

`void (No return value.)` **font_set_stretch**(font_rid: `RID<class_RID>`, weight: `int<class_int>`) `🔗<class_TextServer_method_font_set_stretch>`

Sets font stretch amount, compared to a normal width. A percentage value between `50%` and `200%`.

**Note:** This value is used for font matching only and will not affect font rendering. Use `font_set_face_index()<class_TextServer_method_font_set_face_index>`, `font_set_variation_coordinates()<class_TextServer_method_font_set_variation_coordinates>`, or `font_set_transform()<class_TextServer_method_font_set_transform>` instead.

classref-item-separator

classref-method

`void (No return value.)` **font_set_style**(font_rid: `RID<class_RID>`, style: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`FontStyle<enum_TextServer_FontStyle>`\]) `🔗<class_TextServer_method_font_set_style>`

Sets the font style flags.

**Note:** This value is used for font matching only and will not affect font rendering. Use `font_set_face_index()<class_TextServer_method_font_set_face_index>`, `font_set_variation_coordinates()<class_TextServer_method_font_set_variation_coordinates>`, `font_set_embolden()<class_TextServer_method_font_set_embolden>`, or `font_set_transform()<class_TextServer_method_font_set_transform>` instead.

classref-item-separator

classref-method

`void (No return value.)` **font_set_style_name**(font_rid: `RID<class_RID>`, name: `String<class_String>`) `🔗<class_TextServer_method_font_set_style_name>`

Sets the font style name.

classref-item-separator

classref-method

`void (No return value.)` **font_set_subpixel_positioning**(font_rid: `RID<class_RID>`, subpixel_positioning: `SubpixelPositioning<enum_TextServer_SubpixelPositioning>`) `🔗<class_TextServer_method_font_set_subpixel_positioning>`

Sets font subpixel glyph positioning mode.

classref-item-separator

classref-method

`void (No return value.)` **font_set_texture_image**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`, image: `Image<class_Image>`) `🔗<class_TextServer_method_font_set_texture_image>`

Sets font cache texture image data.

classref-item-separator

classref-method

`void (No return value.)` **font_set_texture_offsets**(font_rid: `RID<class_RID>`, size: `Vector2i<class_Vector2i>`, texture_index: `int<class_int>`, offset: `PackedInt32Array<class_PackedInt32Array>`) `🔗<class_TextServer_method_font_set_texture_offsets>`

Sets array containing glyph packing data.

classref-item-separator

classref-method

`void (No return value.)` **font_set_transform**(font_rid: `RID<class_RID>`, transform: `Transform2D<class_Transform2D>`) `🔗<class_TextServer_method_font_set_transform>`

Sets 2D transform, applied to the font outlines, can be used for slanting, flipping, and rotating glyphs.

For example, to simulate italic typeface by slanting, apply the following transform `Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)`.

classref-item-separator

classref-method

`void (No return value.)` **font_set_underline_position**(font_rid: `RID<class_RID>`, size: `int<class_int>`, underline_position: `float<class_float>`) `🔗<class_TextServer_method_font_set_underline_position>`

Sets pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`void (No return value.)` **font_set_underline_thickness**(font_rid: `RID<class_RID>`, size: `int<class_int>`, underline_thickness: `float<class_float>`) `🔗<class_TextServer_method_font_set_underline_thickness>`

Sets thickness of the underline in pixels.

classref-item-separator

classref-method

`void (No return value.)` **font_set_used_palette**(font_rid: `RID<class_RID>`, index: `int<class_int>`) `🔗<class_TextServer_method_font_set_used_palette>`

Sets used palette index.

classref-item-separator

classref-method

`void (No return value.)` **font_set_variation_coordinates**(font_rid: `RID<class_RID>`, variation_coordinates: `Dictionary<class_Dictionary>`) `🔗<class_TextServer_method_font_set_variation_coordinates>`

Sets variation coordinates for the specified font cache entry. See `font_supported_variation_list()<class_TextServer_method_font_supported_variation_list>` for more info.

classref-item-separator

classref-method

`void (No return value.)` **font_set_weight**(font_rid: `RID<class_RID>`, weight: `int<class_int>`) `🔗<class_TextServer_method_font_set_weight>`

Sets weight (boldness) of the font. A value in the `100...999` range, normal font weight is `400`, bold font weight is `700`.

**Note:** This value is used for font matching only and will not affect font rendering. Use `font_set_face_index()<class_TextServer_method_font_set_face_index>`, `font_set_variation_coordinates()<class_TextServer_method_font_set_variation_coordinates>`, or `font_set_embolden()<class_TextServer_method_font_set_embolden>` instead.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **font_supported_feature_list**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_supported_feature_list>`

Returns the dictionary of the supported OpenType features.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **font_supported_variation_list**(font_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_font_supported_variation_list>`

Returns the dictionary of the supported OpenType variation coordinates.

classref-item-separator

classref-method

`String<class_String>` **format_number**(number: `String<class_String>`, language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_format_number>`

**Deprecated:** Use `TranslationServer.format_number()<class_TranslationServer_method_format_number>` instead.

Converts a number from Western Arabic (0..9) to the numeral system used in the given `language`.

If `language` is an empty string, the active locale will be used.

classref-item-separator

classref-method

`void (No return value.)` **free_rid**(rid: `RID<class_RID>`) `🔗<class_TextServer_method_free_rid>`

Frees an object created by this **TextServer**.

classref-item-separator

classref-method

`int<class_int>` **get_features**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_get_features>`

Returns text server features, see `Feature<enum_TextServer_Feature>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_hex_code_box_size**(size: `int<class_int>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_get_hex_code_box_size>`

Returns size of the replacement character (box with character hexadecimal code that is drawn in place of invalid characters).

classref-item-separator

classref-method

`String<class_String>` **get_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_get_name>`

Returns the name of the server interface.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **get_support_data**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_get_support_data>`

Returns default TextServer database (e.g. ICU break iterators and dictionaries).

classref-item-separator

classref-method

`String<class_String>` **get_support_data_filename**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_get_support_data_filename>`

Returns default TextServer database (e.g. ICU break iterators and dictionaries) filename.

classref-item-separator

classref-method

`String<class_String>` **get_support_data_info**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_get_support_data_info>`

Returns TextServer database (e.g. ICU break iterators and dictionaries) description.

classref-item-separator

classref-method

`bool<class_bool>` **has**(rid: `RID<class_RID>`) `🔗<class_TextServer_method_has>`

Returns `true` if `rid` is valid resource owned by this text server.

classref-item-separator

classref-method

`bool<class_bool>` **has_feature**(feature: `Feature<enum_TextServer_Feature>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_has_feature>`

Returns `true` if the server supports a feature.

classref-item-separator

classref-method

`int<class_int>` **is_confusable**(string: `String<class_String>`, dict: `PackedStringArray<class_PackedStringArray>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_is_confusable>`

Returns index of the first string in `dict` which is visually confusable with the `string`, or `-1` if none is found.

**Note:** This method doesn't detect invisible characters, for spoof detection use it in combination with `spoof_check()<class_TextServer_method_spoof_check>`.

**Note:** Always returns `-1` if the server does not support the `FEATURE_UNICODE_SECURITY<class_TextServer_constant_FEATURE_UNICODE_SECURITY>` feature.

classref-item-separator

classref-method

`bool<class_bool>` **is_locale_right_to_left**(locale: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_is_locale_right_to_left>`

Returns `true` if locale is right-to-left.

classref-item-separator

classref-method

`bool<class_bool>` **is_locale_using_support_data**(locale: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_is_locale_using_support_data>`

Returns `true` if the locale requires text server support data for line/word breaking.

classref-item-separator

classref-method

`bool<class_bool>` **is_valid_identifier**(string: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_is_valid_identifier>`

Returns `true` if `string` is a valid identifier.

If the text server supports the `FEATURE_UNICODE_IDENTIFIERS<class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS>` feature, a valid identifier must:

- Conform to normalization form C.
- Begin with a Unicode character of class XID_Start or `"_"`.
- May contain Unicode characters of class XID_Continue in the other positions.
- Use UAX \#31 recommended scripts only (mixed scripts are allowed).

If the `FEATURE_UNICODE_IDENTIFIERS<class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS>` feature is not supported, a valid identifier must:

- Begin with a Unicode character of class XID_Start or `"_"`.
- May contain Unicode characters of class XID_Continue in the other positions.

classref-item-separator

classref-method

`bool<class_bool>` **is_valid_letter**(unicode: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_is_valid_letter>`

Returns `true` if the given code point is a valid letter, i.e. it belongs to the Unicode category "L".

classref-item-separator

classref-method

`bool<class_bool>` **load_support_data**(filename: `String<class_String>`) `🔗<class_TextServer_method_load_support_data>`

Loads optional TextServer database (e.g. ICU break iterators and dictionaries).

**Note:** This function should be called before any other TextServer functions used, otherwise it won't have any effect.

classref-item-separator

classref-method

`int<class_int>` **name_to_tag**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_name_to_tag>`

Converts the given readable name of a feature, variation, script, or language to an OpenType tag.

classref-item-separator

classref-method

`String<class_String>` **parse_number**(number: `String<class_String>`, language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_parse_number>`

**Deprecated:** Use `TranslationServer.parse_number()<class_TranslationServer_method_parse_number>` instead.

Converts `number` from the numeral system used in the given `language` to Western Arabic (0..9).

If `language` is an empty string, the active locale will be used.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector3i<class_Vector3i>`\] **parse_structured_text**(parser_type: `StructuredTextParser<enum_TextServer_StructuredTextParser>`, args: `Array<class_Array>`, text: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_parse_structured_text>`

Default implementation of the BiDi algorithm override function.

classref-item-separator

classref-method

`String<class_String>` **percent_sign**(language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_percent_sign>`

**Deprecated:** Use `TranslationServer.get_percent_sign()<class_TranslationServer_method_get_percent_sign>` instead.

Returns the percent sign used in the given `language`.

If `language` is an empty string, the active locale will be used.

classref-item-separator

classref-method

`bool<class_bool>` **save_support_data**(filename: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_save_support_data>`

Saves optional TextServer database (e.g. ICU break iterators and dictionaries) to the file.

**Note:** This function is used by during project export, to include TextServer database.

classref-item-separator

classref-method

`int<class_int>` **shaped_get_run_count**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_count>`

Returns the number of uniform text runs in the buffer.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **shaped_get_run_direction**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_direction>`

Returns the direction of the `index` text run (in visual order).

classref-item-separator

classref-method

`RID<class_RID>` **shaped_get_run_font_rid**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_font_rid>`

Returns the font RID of the `index` text run (in visual order).

classref-item-separator

classref-method

`int<class_int>` **shaped_get_run_font_size**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_font_size>`

Returns the font size of the `index` text run (in visual order).

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **shaped_get_run_glyph_range**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_glyph_range>`

Returns the glyph range of the `index` text run (in visual order).

classref-item-separator

classref-method

`String<class_String>` **shaped_get_run_language**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_language>`

Returns the language of the `index` text run (in visual order).

classref-item-separator

classref-method

`Variant<class_Variant>` **shaped_get_run_object**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_object>`

Returns the embedded object of the `index` text run (in visual order).

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **shaped_get_run_range**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_range>`

Returns the source text range of the `index` text run (in visual order).

classref-item-separator

classref-method

`String<class_String>` **shaped_get_run_text**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_run_text>`

Returns the source text of the `index` text run (in visual order).

classref-item-separator

classref-method

`int<class_int>` **shaped_get_span_count**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_span_count>`

Returns number of text spans added using `shaped_text_add_string()<class_TextServer_method_shaped_text_add_string>` or `shaped_text_add_object()<class_TextServer_method_shaped_text_add_object>`.

classref-item-separator

classref-method

`Variant<class_Variant>` **shaped_get_span_embedded_object**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_span_embedded_object>`

Returns text embedded object key.

classref-item-separator

classref-method

`Variant<class_Variant>` **shaped_get_span_meta**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_span_meta>`

Returns text span metadata.

classref-item-separator

classref-method

`Variant<class_Variant>` **shaped_get_span_object**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_span_object>`

Returns the text span embedded object key.

classref-item-separator

classref-method

`String<class_String>` **shaped_get_span_text**(shaped: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_span_text>`

Returns the text span source text.

classref-item-separator

classref-method

`String<class_String>` **shaped_get_text**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_get_text>`

Returns the text buffer source text, including object replacement characters.

classref-item-separator

classref-method

`void (No return value.)` **shaped_set_span_update_font**(shaped: `RID<class_RID>`, index: `int<class_int>`, fonts: `Array<class_Array>`\[`RID<class_RID>`\], size: `int<class_int>`, opentype_features: `Dictionary<class_Dictionary>` = {}) `🔗<class_TextServer_method_shaped_set_span_update_font>`

Changes text span font, font size, and OpenType features, without changing the text.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_add_object**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, length: `int<class_int>` = 1, baseline: `float<class_float>` = 0.0) `🔗<class_TextServer_method_shaped_text_add_object>`

Adds inline object to the text buffer, `key` must be unique. In the text, object is represented as `length` object replacement characters.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_add_string**(shaped: `RID<class_RID>`, text: `String<class_String>`, fonts: `Array<class_Array>`\[`RID<class_RID>`\], size: `int<class_int>`, opentype_features: `Dictionary<class_Dictionary>` = {}, language: `String<class_String>` = "", meta: `Variant<class_Variant>` = null) `🔗<class_TextServer_method_shaped_text_add_string>`

Adds text span and font to draw it to the text buffer.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_clear**(rid: `RID<class_RID>`) `🔗<class_TextServer_method_shaped_text_clear>`

Clears text buffer (removes text and inline objects).

classref-item-separator

classref-method

`int<class_int>` **shaped_text_closest_character_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_closest_character_pos>`

Returns composite character position closest to the `pos`.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_draw**(shaped: `RID<class_RID>`, canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, clip_l: `float<class_float>` = -1, clip_r: `float<class_float>` = -1, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_draw>`

Draw shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

`clip_l` and `clip_r` are offsets relative to `pos`, going to the right in horizontal layout and downward in vertical layout. If `clip_l` is not negative, glyphs starting before the offset are clipped. If `clip_r` is not negative, glyphs ending after the offset are clipped.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_draw_outline**(shaped: `RID<class_RID>`, canvas: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, clip_l: `float<class_float>` = -1, clip_r: `float<class_float>` = -1, outline_size: `int<class_int>` = 1, color: `Color<class_Color>` = Color(1, 1, 1, 1), oversampling: `float<class_float>` = 0.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_draw_outline>`

Draw the outline of the shaped text into a canvas item at a given position, with `color`. `pos` specifies the leftmost point of the baseline (for horizontal layout) or topmost point of the baseline (for vertical layout). If `oversampling` is greater than zero, it is used as font oversampling factor, otherwise viewport oversampling settings are used.

`clip_l` and `clip_r` are offsets relative to `pos`, going to the right in horizontal layout and downward in vertical layout. If `clip_l` is not negative, glyphs starting before the offset are clipped. If `clip_r` is not negative, glyphs ending after the offset are clipped.

classref-item-separator

classref-method

`RID<class_RID>` **shaped_text_duplicate**(rid: `RID<class_RID>`) `🔗<class_TextServer_method_shaped_text_duplicate>`

Duplicates shaped text buffer.

classref-item-separator

classref-method

`float<class_float>` **shaped_text_fit_to_width**(shaped: `RID<class_RID>`, width: `float<class_float>`, justification_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] = 3) `🔗<class_TextServer_method_shaped_text_fit_to_width>`

Adjusts text width to fit to specified width, returns new text width.

classref-item-separator

classref-method

`float<class_float>` **shaped_text_get_ascent**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_ascent>`

Returns the text ascent (number of pixels above the baseline for horizontal layout or to the left of baseline for vertical).

**Note:** Overall ascent can be higher than font ascent, if some glyphs are displaced from the baseline.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **shaped_text_get_carets**(shaped: `RID<class_RID>`, position: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_carets>`

Returns shapes of the carets corresponding to the character offset `position` in the text. Returned caret shape is 1 pixel wide rectangle.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **shaped_text_get_character_breaks**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_character_breaks>`

Returns array of the composite character boundaries.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_custom_ellipsis**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_custom_ellipsis>`

Returns ellipsis character used for text clipping.

classref-item-separator

classref-method

`String<class_String>` **shaped_text_get_custom_punctuation**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_custom_punctuation>`

Returns custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

classref-item-separator

classref-method

`float<class_float>` **shaped_text_get_descent**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_descent>`

Returns the text descent (number of pixels below the baseline for horizontal layout or to the right of baseline for vertical).

**Note:** Overall descent can be higher than font descent, if some glyphs are displaced from the baseline.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **shaped_text_get_direction**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_direction>`

Returns direction of the text.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **shaped_text_get_dominant_direction_in_range**(shaped: `RID<class_RID>`, start: `int<class_int>`, end: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_dominant_direction_in_range>`

Returns dominant direction of in the range of text.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_ellipsis_glyph_count**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_ellipsis_glyph_count>`

Returns number of glyphs in the ellipsis.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **shaped_text_get_ellipsis_glyphs**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_ellipsis_glyphs>`

Returns array of the glyphs in the ellipsis.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_ellipsis_pos**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_ellipsis_pos>`

Returns position of the ellipsis.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_glyph_count**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_glyph_count>`

Returns number of glyphs in the buffer.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **shaped_text_get_glyphs**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_glyphs>`

Returns an array of glyphs in the visual order.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **shaped_text_get_grapheme_bounds**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_grapheme_bounds>`

Returns composite character's bounds as offsets from the start of the line.

classref-item-separator

classref-method

`Direction<enum_TextServer_Direction>` **shaped_text_get_inferred_direction**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_inferred_direction>`

Returns direction of the text, inferred by the BiDi algorithm.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **shaped_text_get_line_breaks**(shaped: `RID<class_RID>`, width: `float<class_float>`, start: `int<class_int>` = 0, break_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\] = 3) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_line_breaks>`

Breaks text to the lines and returns character ranges for each line.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **shaped_text_get_line_breaks_adv**(shaped: `RID<class_RID>`, width: `PackedFloat32Array<class_PackedFloat32Array>`, start: `int<class_int>` = 0, once: `bool<class_bool>` = true, break_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`\] = 3) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_line_breaks_adv>`

Breaks text to the lines and columns. Returns character ranges for each segment.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_object_glyph**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_object_glyph>`

Returns the glyph index of the inline object.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **shaped_text_get_object_range**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_object_range>`

Returns the character range of the inline object.

classref-item-separator

classref-method

`Rect2<class_Rect2>` **shaped_text_get_object_rect**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_object_rect>`

Returns bounding rectangle of the inline object.

classref-item-separator

classref-method

`Array<class_Array>` **shaped_text_get_objects**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_objects>`

Returns array of inline objects.

classref-item-separator

classref-method

`Orientation<enum_TextServer_Orientation>` **shaped_text_get_orientation**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_orientation>`

Returns text orientation.

classref-item-separator

classref-method

`RID<class_RID>` **shaped_text_get_parent**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_parent>`

Returns the parent buffer from which the substring originates.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_get_preserve_control**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_preserve_control>`

Returns `true` if text buffer is configured to display control characters.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_get_preserve_invalid**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_preserve_invalid>`

Returns `true` if text buffer is configured to display hexadecimal codes in place of invalid characters.

**Note:** If set to `false`, nothing is displayed in place of invalid characters.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **shaped_text_get_range**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_range>`

Returns substring buffer character range in the parent buffer.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **shaped_text_get_selection**(shaped: `RID<class_RID>`, start: `int<class_int>`, end: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_selection>`

Returns selection rectangles for the specified character range.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **shaped_text_get_size**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_size>`

Returns size of the text.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_spacing**(shaped: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_spacing>`

Returns extra spacing added between glyphs or lines in pixels.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_get_trim_pos**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_trim_pos>`

Returns the position of the overrun trim.

classref-item-separator

classref-method

`float<class_float>` **shaped_text_get_underline_position**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_underline_position>`

Returns pixel offset of the underline below the baseline.

classref-item-separator

classref-method

`float<class_float>` **shaped_text_get_underline_thickness**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_underline_thickness>`

Returns thickness of the underline.

classref-item-separator

classref-method

`float<class_float>` **shaped_text_get_width**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_width>`

Returns width (for horizontal layout) or height (for vertical) of the text.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **shaped_text_get_word_breaks**(shaped: `RID<class_RID>`, grapheme_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`\] = 264, skip_grapheme_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`\] = 4) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_get_word_breaks>`

Breaks text into words and returns array of character ranges. Use `grapheme_flags` to set what characters are used for breaking.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_has_object**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_has_object>`

Returns `true` if an object with `key` is embedded in this shaped text buffer.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_has_visible_chars**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_has_visible_chars>`

Returns `true` if text buffer contains any visible characters.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_hit_test_grapheme**(shaped: `RID<class_RID>`, coords: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_hit_test_grapheme>`

Returns grapheme index at the specified pixel offset at the baseline, or `-1` if none is found.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_hit_test_position**(shaped: `RID<class_RID>`, coords: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_hit_test_position>`

Returns caret character offset at the specified pixel offset at the baseline. This function always returns a valid position.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_is_ready**(shaped: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_is_ready>`

Returns `true` if buffer is successfully shaped.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_next_character_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_next_character_pos>`

Returns composite character end position closest to the `pos`.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_next_grapheme_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_next_grapheme_pos>`

Returns grapheme end position closest to the `pos`.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_overrun_trim_to_width**(shaped: `RID<class_RID>`, width: `float<class_float>` = 0, overrun_trim_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`\] = 0) `🔗<class_TextServer_method_shaped_text_overrun_trim_to_width>`

Trims text if it exceeds the given width.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_prev_character_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_prev_character_pos>`

Returns composite character start position closest to the `pos`.

classref-item-separator

classref-method

`int<class_int>` **shaped_text_prev_grapheme_pos**(shaped: `RID<class_RID>`, pos: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_prev_grapheme_pos>`

Returns grapheme start position closest to the `pos`.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_resize_object**(shaped: `RID<class_RID>`, key: `Variant<class_Variant>`, size: `Vector2<class_Vector2>`, inline_align: `InlineAlignment<enum_@GlobalScope_InlineAlignment>` = 5, baseline: `float<class_float>` = 0.0) `🔗<class_TextServer_method_shaped_text_resize_object>`

Sets new size and alignment of embedded object.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_bidi_override**(shaped: `RID<class_RID>`, override: `Array<class_Array>`) `🔗<class_TextServer_method_shaped_text_set_bidi_override>`

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi algorithm will be used on each range separately.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_custom_ellipsis**(shaped: `RID<class_RID>`, char: `int<class_int>`) `🔗<class_TextServer_method_shaped_text_set_custom_ellipsis>`

Sets ellipsis character used for text clipping.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_custom_punctuation**(shaped: `RID<class_RID>`, punct: `String<class_String>`) `🔗<class_TextServer_method_shaped_text_set_custom_punctuation>`

Sets custom punctuation character list, used for word breaking. If set to empty string, server defaults are used.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_direction**(shaped: `RID<class_RID>`, direction: `Direction<enum_TextServer_Direction>` = 0) `🔗<class_TextServer_method_shaped_text_set_direction>`

Sets desired text direction. If set to `DIRECTION_AUTO<class_TextServer_constant_DIRECTION_AUTO>`, direction will be detected based on the buffer contents and current locale.

**Note:** Direction is ignored if server does not support `FEATURE_BIDI_LAYOUT<class_TextServer_constant_FEATURE_BIDI_LAYOUT>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_orientation**(shaped: `RID<class_RID>`, orientation: `Orientation<enum_TextServer_Orientation>` = 0) `🔗<class_TextServer_method_shaped_text_set_orientation>`

Sets desired text orientation.

**Note:** Orientation is ignored if server does not support `FEATURE_VERTICAL_LAYOUT<class_TextServer_constant_FEATURE_VERTICAL_LAYOUT>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_preserve_control**(shaped: `RID<class_RID>`, enabled: `bool<class_bool>`) `🔗<class_TextServer_method_shaped_text_set_preserve_control>`

If set to `true` text buffer will display control characters.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_preserve_invalid**(shaped: `RID<class_RID>`, enabled: `bool<class_bool>`) `🔗<class_TextServer_method_shaped_text_set_preserve_invalid>`

If set to `true` text buffer will display invalid characters as hexadecimal codes, otherwise nothing is displayed.

classref-item-separator

classref-method

`void (No return value.)` **shaped_text_set_spacing**(shaped: `RID<class_RID>`, spacing: `SpacingType<enum_TextServer_SpacingType>`, value: `int<class_int>`) `🔗<class_TextServer_method_shaped_text_set_spacing>`

Sets extra spacing added between glyphs or lines in pixels.

classref-item-separator

classref-method

`bool<class_bool>` **shaped_text_shape**(shaped: `RID<class_RID>`) `🔗<class_TextServer_method_shaped_text_shape>`

Shapes buffer if it's not shaped. Returns `true` if the string is shaped successfully.

**Note:** It is not necessary to call this function manually, buffer will be shaped automatically as soon as any of its output data is requested.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **shaped_text_sort_logical**(shaped: `RID<class_RID>`) `🔗<class_TextServer_method_shaped_text_sort_logical>`

Returns text glyphs in the logical order.

classref-item-separator

classref-method

`RID<class_RID>` **shaped_text_substr**(shaped: `RID<class_RID>`, start: `int<class_int>`, length: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_shaped_text_substr>`

Returns text buffer for the substring of the text in the `shaped` text buffer (including inline objects).

classref-item-separator

classref-method

`float<class_float>` **shaped_text_tab_align**(shaped: `RID<class_RID>`, tab_stops: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_TextServer_method_shaped_text_tab_align>`

Aligns shaped text to the given tab-stops.

classref-item-separator

classref-method

`bool<class_bool>` **spoof_check**(string: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_spoof_check>`

Returns `true` if `string` is likely to be an attempt at confusing the reader.

**Note:** Always returns `false` if the server does not support the `FEATURE_UNICODE_SECURITY<class_TextServer_constant_FEATURE_UNICODE_SECURITY>` feature.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **string_get_character_breaks**(string: `String<class_String>`, language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_string_get_character_breaks>`

Returns array of the composite character boundaries.

    var ts = TextServerManager.get_primary_interface()
    print(ts.string_get_character_breaks("Test ❤️‍🔥 Test")) # Prints [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14]

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **string_get_word_breaks**(string: `String<class_String>`, language: `String<class_String>` = "", chars_per_line: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_string_get_word_breaks>`

Returns an array of the word break boundaries. Elements in the returned array are the offsets of the start and end of words. Therefore the length of the array is always even.

When `chars_per_line` is greater than zero, line break boundaries are returned instead.

    var ts = TextServerManager.get_primary_interface()
    # Corresponds to the substrings "The", "Godot", "Engine", and "4".
    print(ts.string_get_word_breaks("The Godot Engine, 4")) # Prints [0, 3, 4, 9, 10, 16, 18, 19]
    # Corresponds to the substrings "The", "Godot", "Engin", and "e, 4".
    print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 5)) # Prints [0, 3, 4, 9, 10, 15, 15, 19]
    # Corresponds to the substrings "The Godot" and "Engine, 4".
    print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 10)) # Prints [0, 9, 10, 19]

classref-item-separator

classref-method

`String<class_String>` **string_to_lower**(string: `String<class_String>`, language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_string_to_lower>`

Returns the string converted to `lowercase`.

**Note:** Casing is locale dependent and context sensitive if server support `FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION<class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

**Note:** The result may be longer or shorter than the original.

classref-item-separator

classref-method

`String<class_String>` **string_to_title**(string: `String<class_String>`, language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_string_to_title>`

Returns the string converted to `Title Case`.

**Note:** Casing is locale dependent and context sensitive if server support `FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION<class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

**Note:** The result may be longer or shorter than the original.

classref-item-separator

classref-method

`String<class_String>` **string_to_upper**(string: `String<class_String>`, language: `String<class_String>` = "") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_string_to_upper>`

Returns the string converted to `UPPERCASE`.

**Note:** Casing is locale dependent and context sensitive if server support `FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION<class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION>` feature (supported by `TextServerAdvanced<class_TextServerAdvanced>`).

**Note:** The result may be longer or shorter than the original.

classref-item-separator

classref-method

`String<class_String>` **strip_diacritics**(string: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_strip_diacritics>`

Strips diacritics from the string.

**Note:** The result may be longer or shorter than the original.

classref-item-separator

classref-method

`String<class_String>` **tag_to_name**(tag: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServer_method_tag_to_name>`

Converts the given OpenType tag to the readable name of a feature, variation, script, or language.