github_url
hide

# TextEdit

**Inherits:** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `CodeEdit<class_CodeEdit>`

A multiline text editor.

classref-introduction-group

## Description

A multiline text editor. It also has limited facilities for editing code, such as syntax highlighting support. For more advanced facilities for editing code, see `CodeEdit<class_CodeEdit>`.

While entering text, it is possible to insert special characters using Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold `Alt` and type the codepoint on the numpad. For example, to enter the character `á` (U+00E1), hold `Alt` and type `+E1` on the numpad (the leading zeroes can be omitted).
- To enter OEM codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (OEM 160), hold `Alt` and type `160` on the numpad.
- To enter Windows codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (Windows 0225), hold `Alt` and type `0`, `2`, `2`, `5` on the numpad. The leading zero here must **not** be omitted, as this is how Windows codepoints are distinguished from OEM codepoints.

**Note:** Most viewport, caret, and edit methods contain a `caret_index` argument for `caret_multiple<class_TextEdit_property_caret_multiple>` support. The argument should be one of the following: `-1` for all carets, `0` for the main caret, or greater than `0` for secondary carets in the order they were created.

**Note:** When holding down `Alt`, the vertical scroll wheel will scroll 5 times as fast as it would normally do. This also works in the Godot script editor.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**caret_changed**() `🔗<class_TextEdit_signal_caret_changed>`

Emitted when any caret changes position.

classref-item-separator

classref-signal

**gutter_added**() `🔗<class_TextEdit_signal_gutter_added>`

Emitted when a gutter is added.

classref-item-separator

classref-signal

**gutter_clicked**(line: `int<class_int>`, gutter: `int<class_int>`) `🔗<class_TextEdit_signal_gutter_clicked>`

Emitted when a gutter is clicked.

classref-item-separator

classref-signal

**gutter_removed**() `🔗<class_TextEdit_signal_gutter_removed>`

Emitted when a gutter is removed.

classref-item-separator

classref-signal

**lines_edited_from**(from_line: `int<class_int>`, to_line: `int<class_int>`) `🔗<class_TextEdit_signal_lines_edited_from>`

Emitted immediately when the text changes.

When text is added `from_line` will be less than `to_line`. On a remove `to_line` will be less than `from_line`.

classref-item-separator

classref-signal

**text_changed**() `🔗<class_TextEdit_signal_text_changed>`

Emitted when the text changes.

classref-item-separator

classref-signal

**text_set**() `🔗<class_TextEdit_signal_text_set>`

Emitted when `clear()<class_TextEdit_method_clear>` is called or `text<class_TextEdit_property_text>` is set.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **MenuItems**: `🔗<enum_TextEdit_MenuItems>`

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_COPY** = `1`

Copies the selected text.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the cursor's position).

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_CLEAR** = `3`

Erases the whole **TextEdit** text.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_SELECT_ALL** = `4`

Selects the whole **TextEdit** text.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_UNDO** = `5`

Undoes the previous action.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_REDO** = `6`

Redoes the previous action.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_SUBMENU_TEXT_DIR** = `7`

ID of "Text Writing Direction" submenu.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_DISPLAY_UCC** = `12`

Toggles control character display.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_SUBMENU_INSERT_UCC** = `13`

ID of "Insert Control Character" submenu.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

classref-enumeration-constant

`MenuItems<enum_TextEdit_MenuItems>` **MENU_MAX** = `31`

Represents the size of the `MenuItems<enum_TextEdit_MenuItems>` enum.

classref-item-separator

classref-enumeration

enum **EditAction**: `🔗<enum_TextEdit_EditAction>`

classref-enumeration-constant

`EditAction<enum_TextEdit_EditAction>` **ACTION_NONE** = `0`

No current action.

classref-enumeration-constant

`EditAction<enum_TextEdit_EditAction>` **ACTION_TYPING** = `1`

A typing action.

classref-enumeration-constant

`EditAction<enum_TextEdit_EditAction>` **ACTION_BACKSPACE** = `2`

A backwards delete action.

classref-enumeration-constant

`EditAction<enum_TextEdit_EditAction>` **ACTION_DELETE** = `3`

A forward delete action.

classref-item-separator

classref-enumeration

enum **SearchFlags**: `🔗<enum_TextEdit_SearchFlags>`

classref-enumeration-constant

`SearchFlags<enum_TextEdit_SearchFlags>` **SEARCH_MATCH_CASE** = `1`

Match case when searching.

classref-enumeration-constant

`SearchFlags<enum_TextEdit_SearchFlags>` **SEARCH_WHOLE_WORDS** = `2`

Match whole words when searching.

classref-enumeration-constant

`SearchFlags<enum_TextEdit_SearchFlags>` **SEARCH_BACKWARDS** = `4`

Search from end to beginning.

classref-item-separator

classref-enumeration

enum **CaretType**: `🔗<enum_TextEdit_CaretType>`

classref-enumeration-constant

`CaretType<enum_TextEdit_CaretType>` **CARET_TYPE_LINE** = `0`

Vertical line caret.

classref-enumeration-constant

`CaretType<enum_TextEdit_CaretType>` **CARET_TYPE_BLOCK** = `1`

Block caret.

classref-item-separator

classref-enumeration

enum **SelectionMode**: `🔗<enum_TextEdit_SelectionMode>`

classref-enumeration-constant

`SelectionMode<enum_TextEdit_SelectionMode>` **SELECTION_MODE_NONE** = `0`

Not selecting.

classref-enumeration-constant

`SelectionMode<enum_TextEdit_SelectionMode>` **SELECTION_MODE_SHIFT** = `1`

Select as if `shift` is pressed.

classref-enumeration-constant

`SelectionMode<enum_TextEdit_SelectionMode>` **SELECTION_MODE_POINTER** = `2`

Select single characters as if the user single clicked.

classref-enumeration-constant

`SelectionMode<enum_TextEdit_SelectionMode>` **SELECTION_MODE_WORD** = `3`

Select whole words as if the user double clicked.

classref-enumeration-constant

`SelectionMode<enum_TextEdit_SelectionMode>` **SELECTION_MODE_LINE** = `4`

Select whole lines as if the user triple clicked.

classref-item-separator

classref-enumeration

enum **LineWrappingMode**: `🔗<enum_TextEdit_LineWrappingMode>`

classref-enumeration-constant

`LineWrappingMode<enum_TextEdit_LineWrappingMode>` **LINE_WRAPPING_NONE** = `0`

Line wrapping is disabled.

classref-enumeration-constant

`LineWrappingMode<enum_TextEdit_LineWrappingMode>` **LINE_WRAPPING_BOUNDARY** = `1`

Line wrapping occurs at the control boundary, beyond what would normally be visible.

classref-item-separator

classref-enumeration

enum **GutterType**: `🔗<enum_TextEdit_GutterType>`

classref-enumeration-constant

`GutterType<enum_TextEdit_GutterType>` **GUTTER_TYPE_STRING** = `0`

When a gutter is set to string using `set_gutter_type()<class_TextEdit_method_set_gutter_type>`, it is used to contain text set via the `set_line_gutter_text()<class_TextEdit_method_set_line_gutter_text>` method.

classref-enumeration-constant

`GutterType<enum_TextEdit_GutterType>` **GUTTER_TYPE_ICON** = `1`

When a gutter is set to icon using `set_gutter_type()<class_TextEdit_method_set_gutter_type>`, it is used to contain an icon set via the `set_line_gutter_icon()<class_TextEdit_method_set_line_gutter_icon>` method.

classref-enumeration-constant

`GutterType<enum_TextEdit_GutterType>` **GUTTER_TYPE_CUSTOM** = `2`

When a gutter is set to custom using `set_gutter_type()<class_TextEdit_method_set_gutter_type>`, it is used to contain custom visuals controlled by a callback method set via the `set_gutter_custom_draw()<class_TextEdit_method_set_gutter_custom_draw>` method.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`AutowrapMode<enum_TextServer_AutowrapMode>` **autowrap_mode** = `3` `🔗<class_TextEdit_property_autowrap_mode>`

classref-property-setget

- `void (No return value.)` **set_autowrap_mode**(value: `AutowrapMode<enum_TextServer_AutowrapMode>`)
- `AutowrapMode<enum_TextServer_AutowrapMode>` **get_autowrap_mode**()

If `wrap_mode<class_TextEdit_property_wrap_mode>` is set to `LINE_WRAPPING_BOUNDARY<class_TextEdit_constant_LINE_WRAPPING_BOUNDARY>`, sets text wrapping mode.

classref-item-separator

classref-property

`bool<class_bool>` **backspace_deletes_composite_character_enabled** = `false` `🔗<class_TextEdit_property_backspace_deletes_composite_character_enabled>`

classref-property-setget

- `void (No return value.)` **set_backspace_deletes_composite_character_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_backspace_deletes_composite_character_enabled**()

If `true` and `caret_mid_grapheme<class_TextEdit_property_caret_mid_grapheme>` is `false`, backspace deletes an entire composite character such as ❤️‍🩹, instead of deleting part of the composite character.

classref-item-separator

classref-property

`bool<class_bool>` **caret_blink** = `false` `🔗<class_TextEdit_property_caret_blink>`

classref-property-setget

- `void (No return value.)` **set_caret_blink_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_caret_blink_enabled**()

If `true`, makes the caret blink.

classref-item-separator

classref-property

`float<class_float>` **caret_blink_interval** = `0.65` `🔗<class_TextEdit_property_caret_blink_interval>`

classref-property-setget

- `void (No return value.)` **set_caret_blink_interval**(value: `float<class_float>`)
- `float<class_float>` **get_caret_blink_interval**()

The interval at which the caret blinks (in seconds).

classref-item-separator

classref-property

`bool<class_bool>` **caret_draw_when_editable_disabled** = `false` `🔗<class_TextEdit_property_caret_draw_when_editable_disabled>`

classref-property-setget

- `void (No return value.)` **set_draw_caret_when_editable_disabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_caret_when_editable_disabled**()

If `true`, caret will be visible when `editable<class_TextEdit_property_editable>` is disabled.

classref-item-separator

classref-property

`bool<class_bool>` **caret_mid_grapheme** = `false` `🔗<class_TextEdit_property_caret_mid_grapheme>`

classref-property-setget

- `void (No return value.)` **set_caret_mid_grapheme_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_caret_mid_grapheme_enabled**()

Allow moving caret, selecting and removing the individual composite character components.

**Note:** `Backspace` is always removing individual composite character components.

classref-item-separator

classref-property

`bool<class_bool>` **caret_move_on_right_click** = `true` `🔗<class_TextEdit_property_caret_move_on_right_click>`

classref-property-setget

- `void (No return value.)` **set_move_caret_on_right_click_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_move_caret_on_right_click_enabled**()

If `true`, a right-click moves the caret at the mouse position before displaying the context menu.

If `false`, the context menu ignores mouse location.

classref-item-separator

classref-property

`bool<class_bool>` **caret_multiple** = `true` `🔗<class_TextEdit_property_caret_multiple>`

classref-property-setget

- `void (No return value.)` **set_multiple_carets_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_multiple_carets_enabled**()

If `true`, multiple carets are allowed. Left-clicking with `Alt` adds a new caret. See `add_caret()<class_TextEdit_method_add_caret>` and `get_caret_count()<class_TextEdit_method_get_caret_count>`.

classref-item-separator

classref-property

`CaretType<enum_TextEdit_CaretType>` **caret_type** = `0` `🔗<class_TextEdit_property_caret_type>`

classref-property-setget

- `void (No return value.)` **set_caret_type**(value: `CaretType<enum_TextEdit_CaretType>`)
- `CaretType<enum_TextEdit_CaretType>` **get_caret_type**()

Set the type of caret to draw.

classref-item-separator

classref-property

`bool<class_bool>` **context_menu_enabled** = `true` `🔗<class_TextEdit_property_context_menu_enabled>`

classref-property-setget

- `void (No return value.)` **set_context_menu_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_context_menu_enabled**()

If `true`, a right-click displays the context menu.

classref-item-separator

classref-property

`String<class_String>` **custom_word_separators** = `""` `🔗<class_TextEdit_property_custom_word_separators>`

classref-property-setget

- `void (No return value.)` **set_custom_word_separators**(value: `String<class_String>`)
- `String<class_String>` **get_custom_word_separators**()

The characters to consider as word delimiters if `use_custom_word_separators<class_TextEdit_property_use_custom_word_separators>` is `true`. The characters should be defined without separation, for example `#_!`.

classref-item-separator

classref-property

`bool<class_bool>` **deselect_on_focus_loss_enabled** = `true` `🔗<class_TextEdit_property_deselect_on_focus_loss_enabled>`

classref-property-setget

- `void (No return value.)` **set_deselect_on_focus_loss_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_deselect_on_focus_loss_enabled**()

If `true`, the selected text will be deselected when focus is lost.

classref-item-separator

classref-property

`bool<class_bool>` **drag_and_drop_selection_enabled** = `true` `🔗<class_TextEdit_property_drag_and_drop_selection_enabled>`

classref-property-setget

- `void (No return value.)` **set_drag_and_drop_selection_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text. Text can still be dropped from other sources.

classref-item-separator

classref-property

`bool<class_bool>` **draw_control_chars** = `false` `🔗<class_TextEdit_property_draw_control_chars>`

classref-property-setget

- `void (No return value.)` **set_draw_control_chars**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_draw_control_chars**()

If `true`, control characters are displayed.

classref-item-separator

classref-property

`bool<class_bool>` **draw_spaces** = `false` `🔗<class_TextEdit_property_draw_spaces>`

classref-property-setget

- `void (No return value.)` **set_draw_spaces**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_spaces**()

If `true`, the "space" character will have a visible representation.

classref-item-separator

classref-property

`bool<class_bool>` **draw_tabs** = `false` `🔗<class_TextEdit_property_draw_tabs>`

classref-property-setget

- `void (No return value.)` **set_draw_tabs**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_tabs**()

If `true`, the "tab" character will have a visible representation.

classref-item-separator

classref-property

`bool<class_bool>` **editable** = `true` `🔗<class_TextEdit_property_editable>`

classref-property-setget

- `void (No return value.)` **set_editable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editable**()

If `false`, existing text cannot be modified and new text cannot be added.

classref-item-separator

classref-property

`bool<class_bool>` **emoji_menu_enabled** = `true` `🔗<class_TextEdit_property_emoji_menu_enabled>`

classref-property-setget

- `void (No return value.)` **set_emoji_menu_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_emoji_menu_enabled**()

If `true`, "Emoji and Symbols" menu is enabled.

classref-item-separator

classref-property

`bool<class_bool>` **empty_selection_clipboard_enabled** = `true` `🔗<class_TextEdit_property_empty_selection_clipboard_enabled>`

classref-property-setget

- `void (No return value.)` **set_empty_selection_clipboard_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_empty_selection_clipboard_enabled**()

If `true`, copying or cutting without a selection is performed on all lines with a caret. Otherwise, copy and cut require a selection.

classref-item-separator

classref-property

`bool<class_bool>` **highlight_all_occurrences** = `false` `🔗<class_TextEdit_property_highlight_all_occurrences>`

classref-property-setget

- `void (No return value.)` **set_highlight_all_occurrences**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_highlight_all_occurrences_enabled**()

If `true`, all occurrences of the selected text will be highlighted.

classref-item-separator

classref-property

`bool<class_bool>` **highlight_current_line** = `false` `🔗<class_TextEdit_property_highlight_current_line>`

classref-property-setget

- `void (No return value.)` **set_highlight_current_line**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_highlight_current_line_enabled**()

If `true`, the line containing the cursor is highlighted.

classref-item-separator

classref-property

`bool<class_bool>` **indent_wrapped_lines** = `false` `🔗<class_TextEdit_property_indent_wrapped_lines>`

classref-property-setget

- `void (No return value.)` **set_indent_wrapped_lines**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_indent_wrapped_lines**()

If `true`, all wrapped lines are indented to the same amount as the unwrapped line.

classref-item-separator

classref-property

`String<class_String>` **language** = `""` `🔗<class_TextEdit_property_language>`

classref-property-setget

- `void (No return value.)` **set_language**(value: `String<class_String>`)
- `String<class_String>` **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

classref-item-separator

classref-property

`bool<class_bool>` **middle_mouse_paste_enabled** = `true` `🔗<class_TextEdit_property_middle_mouse_paste_enabled>`

classref-property-setget

- `void (No return value.)` **set_middle_mouse_paste_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_middle_mouse_paste_enabled**()

If `false`, using middle mouse button to paste clipboard will be disabled.

**Note:** This method is only implemented on Linux.

classref-item-separator

classref-property

`bool<class_bool>` **minimap_draw** = `false` `🔗<class_TextEdit_property_minimap_draw>`

classref-property-setget

- `void (No return value.)` **set_draw_minimap**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_minimap**()

If `true`, a minimap is shown, providing an outline of your source code. The minimap uses a fixed-width text size.

classref-item-separator

classref-property

`int<class_int>` **minimap_width** = `80` `🔗<class_TextEdit_property_minimap_width>`

classref-property-setget

- `void (No return value.)` **set_minimap_width**(value: `int<class_int>`)
- `int<class_int>` **get_minimap_width**()

The width, in pixels, of the minimap.

classref-item-separator

classref-property

`String<class_String>` **placeholder_text** = `""` `🔗<class_TextEdit_property_placeholder_text>`

classref-property-setget

- `void (No return value.)` **set_placeholder**(value: `String<class_String>`)
- `String<class_String>` **get_placeholder**()

Text shown when the **TextEdit** is empty. It is **not** the **TextEdit**'s default value (see `text<class_TextEdit_property_text>`).

classref-item-separator

classref-property

`bool<class_bool>` **scroll_fit_content_height** = `false` `🔗<class_TextEdit_property_scroll_fit_content_height>`

classref-property-setget

- `void (No return value.)` **set_fit_content_height_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_fit_content_height_enabled**()

If `true`, **TextEdit** fits its minimum height to the number of visible lines instead of scrolling vertically. If a maximum height is set (for example via `Control.custom_maximum_size<class_Control_property_custom_maximum_size>`) and content exceeds it, a vertical scrollbar is shown.

classref-item-separator

classref-property

`bool<class_bool>` **scroll_fit_content_width** = `false` `🔗<class_TextEdit_property_scroll_fit_content_width>`

classref-property-setget

- `void (No return value.)` **set_fit_content_width_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_fit_content_width_enabled**()

If `true`, **TextEdit** fits its minimum width to the widest line instead of scrolling horizontally. If a maximum width is set (for example via `Control.custom_maximum_size<class_Control_property_custom_maximum_size>`) and content exceeds it, a horizontal scrollbar is shown.

classref-item-separator

classref-property

`int<class_int>` **scroll_horizontal** = `0` `🔗<class_TextEdit_property_scroll_horizontal>`

classref-property-setget

- `void (No return value.)` **set_h_scroll**(value: `int<class_int>`)
- `int<class_int>` **get_h_scroll**()

If there is a horizontal scrollbar, this determines the current horizontal scroll value in pixels.

classref-item-separator

classref-property

`bool<class_bool>` **scroll_past_end_of_file** = `false` `🔗<class_TextEdit_property_scroll_past_end_of_file>`

classref-property-setget

- `void (No return value.)` **set_scroll_past_end_of_file_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_scroll_past_end_of_file_enabled**()

Allow scrolling past the last line into "virtual" space.

classref-item-separator

classref-property

`bool<class_bool>` **scroll_smooth** = `false` `🔗<class_TextEdit_property_scroll_smooth>`

classref-property-setget

- `void (No return value.)` **set_smooth_scroll_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_smooth_scroll_enabled**()

Scroll smoothly over the text rather than jumping to the next location.

classref-item-separator

classref-property

`float<class_float>` **scroll_v_scroll_speed** = `80.0` `🔗<class_TextEdit_property_scroll_v_scroll_speed>`

classref-property-setget

- `void (No return value.)` **set_v_scroll_speed**(value: `float<class_float>`)
- `float<class_float>` **get_v_scroll_speed**()

Sets the scroll speed with the minimap or when `scroll_smooth<class_TextEdit_property_scroll_smooth>` is enabled.

classref-item-separator

classref-property

`float<class_float>` **scroll_vertical** = `0.0` `🔗<class_TextEdit_property_scroll_vertical>`

classref-property-setget

- `void (No return value.)` **set_v_scroll**(value: `float<class_float>`)
- `float<class_float>` **get_v_scroll**()

If there is a vertical scrollbar, this determines the current vertical scroll value in line numbers, starting at 0 for the top line.

classref-item-separator

classref-property

`bool<class_bool>` **selecting_enabled** = `true` `🔗<class_TextEdit_property_selecting_enabled>`

classref-property-setget

- `void (No return value.)` **set_selecting_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_selecting_enabled**()

If `true`, text can be selected.

If `false`, text can not be selected by the user or by the `select()<class_TextEdit_method_select>` or `select_all()<class_TextEdit_method_select_all>` methods.

classref-item-separator

classref-property

`bool<class_bool>` **shortcut_keys_enabled** = `true` `🔗<class_TextEdit_property_shortcut_keys_enabled>`

classref-property-setget

- `void (No return value.)` **set_shortcut_keys_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_shortcut_keys_enabled**()

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

classref-item-separator

classref-property

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **structured_text_bidi_override** = `0` `🔗<class_TextEdit_property_structured_text_bidi_override>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override**(value: `StructuredTextParser<enum_TextServer_StructuredTextParser>`)
- `StructuredTextParser<enum_TextServer_StructuredTextParser>` **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

classref-item-separator

classref-property

`Array<class_Array>` **structured_text_bidi_override_options** = `[]` `🔗<class_TextEdit_property_structured_text_bidi_override_options>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override_options**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

classref-item-separator

classref-property

`SyntaxHighlighter<class_SyntaxHighlighter>` **syntax_highlighter** `🔗<class_TextEdit_property_syntax_highlighter>`

classref-property-setget

- `void (No return value.)` **set_syntax_highlighter**(value: `SyntaxHighlighter<class_SyntaxHighlighter>`)
- `SyntaxHighlighter<class_SyntaxHighlighter>` **get_syntax_highlighter**()

The syntax highlighter to use.

**Note:** A `SyntaxHighlighter<class_SyntaxHighlighter>` instance should not be used across multiple **TextEdit** nodes.

classref-item-separator

classref-property

`bool<class_bool>` **tab_input_mode** = `true` `🔗<class_TextEdit_property_tab_input_mode>`

classref-property-setget

- `void (No return value.)` **set_tab_input_mode**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_tab_input_mode**()

If `true`, `ProjectSettings.input/ui_text_indent<class_ProjectSettings_property_input/ui_text_indent>` input `Tab` character, otherwise it moves keyboard focus to the next `Control<class_Control>` in the scene.

classref-item-separator

classref-property

`String<class_String>` **text** = `""` `🔗<class_TextEdit_property_text>`

classref-property-setget

- `void (No return value.)` **set_text**(value: `String<class_String>`)
- `String<class_String>` **get_text**()

String value of the **TextEdit**.

classref-item-separator

classref-property

`TextDirection<enum_Control_TextDirection>` **text_direction** = `0` `🔗<class_TextEdit_property_text_direction>`

classref-property-setget

- `void (No return value.)` **set_text_direction**(value: `TextDirection<enum_Control_TextDirection>`)
- `TextDirection<enum_Control_TextDirection>` **get_text_direction**()

Base text writing direction.

classref-item-separator

classref-property

`bool<class_bool>` **use_custom_word_separators** = `false` `🔗<class_TextEdit_property_use_custom_word_separators>`

classref-property-setget

- `void (No return value.)` **set_use_custom_word_separators**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_custom_word_separators_enabled**()

If `false`, using `Ctrl + Left` or `Ctrl + Right` (`Cmd + Left` or `Cmd + Right` on macOS) bindings will use the behavior of `use_default_word_separators<class_TextEdit_property_use_default_word_separators>`. If `true`, it will also stop the caret if a character within `custom_word_separators<class_TextEdit_property_custom_word_separators>` is detected. Useful for subword moving. This behavior also will be applied to the behavior of text selection.

classref-item-separator

classref-property

`bool<class_bool>` **use_default_word_separators** = `true` `🔗<class_TextEdit_property_use_default_word_separators>`

classref-property-setget

- `void (No return value.)` **set_use_default_word_separators**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_default_word_separators_enabled**()

If `false`, using `Ctrl + Left` or `Ctrl + Right` (`Cmd + Left` or `Cmd + Right` on macOS) bindings will stop moving caret only if a space or punctuation is detected. If `true`, it will also stop the caret if a character is part of `` !"#$%&'()*+,-./:;<=>?@[\]^`{|}~ ``, the Unicode General Punctuation table, or the Unicode CJK Punctuation table. Useful for subword moving. This behavior also will be applied to the behavior of text selection.

classref-item-separator

classref-property

`bool<class_bool>` **virtual_keyboard_enabled** = `true` `🔗<class_TextEdit_property_virtual_keyboard_enabled>`

classref-property-setget

- `void (No return value.)` **set_virtual_keyboard_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_virtual_keyboard_enabled**()

If `true`, the native virtual keyboard is enabled on platforms that support it.

classref-item-separator

classref-property

`bool<class_bool>` **virtual_keyboard_show_on_focus** = `true` `🔗<class_TextEdit_property_virtual_keyboard_show_on_focus>`

classref-property-setget

- `void (No return value.)` **set_virtual_keyboard_show_on_focus**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_virtual_keyboard_show_on_focus**()

If `true`, the native virtual keyboard is shown on focus events on platforms that support it.

classref-item-separator

classref-property

`LineWrappingMode<enum_TextEdit_LineWrappingMode>` **wrap_mode** = `0` `🔗<class_TextEdit_property_wrap_mode>`

classref-property-setget

- `void (No return value.)` **set_line_wrapping_mode**(value: `LineWrappingMode<enum_TextEdit_LineWrappingMode>`)
- `LineWrappingMode<enum_TextEdit_LineWrappingMode>` **get_line_wrapping_mode**()

Sets the line wrapping mode to use.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_backspace**(caret_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextEdit_private_method__backspace>`

Override this method to define what happens when the user presses the backspace key.

classref-item-separator

classref-method

`void (No return value.)` **\_copy**(caret_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextEdit_private_method__copy>`

Override this method to define what happens when the user performs a copy operation.

classref-item-separator

classref-method

`void (No return value.)` **\_cut**(caret_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextEdit_private_method__cut>`

Override this method to define what happens when the user performs a cut operation.

classref-item-separator

classref-method

`void (No return value.)` **\_handle_unicode_input**(unicode_char: `int<class_int>`, caret_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextEdit_private_method__handle_unicode_input>`

Override this method to define what happens when the user types in the provided key `unicode_char`.

classref-item-separator

classref-method

`void (No return value.)` **\_paste**(caret_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextEdit_private_method__paste>`

Override this method to define what happens when the user performs a paste operation.

classref-item-separator

classref-method

`void (No return value.)` **\_paste_primary_clipboard**(caret_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_TextEdit_private_method__paste_primary_clipboard>`

Override this method to define what happens when the user performs a paste operation with middle mouse button.

**Note:** This method is only implemented on Linux.

classref-item-separator

classref-method

`int<class_int>` **add_caret**(line: `int<class_int>`, column: `int<class_int>`) `🔗<class_TextEdit_method_add_caret>`

Adds a new caret at the given location. Returns the index of the new caret, or `-1` if the location is invalid.

classref-item-separator

classref-method

`void (No return value.)` **add_caret_at_carets**(below: `bool<class_bool>`) `🔗<class_TextEdit_method_add_caret_at_carets>`

Adds an additional caret above or below every caret. If `below` is `true` the new caret will be added below and above otherwise.

classref-item-separator

classref-method

`void (No return value.)` **add_gutter**(at: `int<class_int>` = -1) `🔗<class_TextEdit_method_add_gutter>`

Register a new gutter to this **TextEdit**. Use `at` to have a specific gutter order. A value of `-1` appends the gutter to the right.

classref-item-separator

classref-method

`void (No return value.)` **add_selection_for_next_occurrence**() `🔗<class_TextEdit_method_add_selection_for_next_occurrence>`

Adds a selection and a caret for the next occurrence of the current selection. If there is no active selection, selects word under caret.

classref-item-separator

classref-method

`void (No return value.)` **adjust_carets_after_edit**(caret: `int<class_int>`, from_line: `int<class_int>`, from_col: `int<class_int>`, to_line: `int<class_int>`, to_col: `int<class_int>`) `🔗<class_TextEdit_method_adjust_carets_after_edit>`

**Deprecated:** No longer necessary since methods now adjust carets themselves.

This method does nothing.

classref-item-separator

classref-method

`void (No return value.)` **adjust_viewport_to_caret**(caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_adjust_viewport_to_caret>`

Adjust the viewport so the caret is visible.

classref-item-separator

classref-method

`void (No return value.)` **apply_ime**() `🔗<class_TextEdit_method_apply_ime>`

Applies text from the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) to each caret and closes the IME if it is open.

classref-item-separator

classref-method

`void (No return value.)` **backspace**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_backspace>`

Called when the user presses the backspace key. Can be overridden with `_backspace()<class_TextEdit_private_method__backspace>`.

classref-item-separator

classref-method

`void (No return value.)` **begin_complex_operation**() `🔗<class_TextEdit_method_begin_complex_operation>`

Starts a multipart edit. All edits will be treated as one action until `end_complex_operation()<class_TextEdit_method_end_complex_operation>` is called.

classref-item-separator

classref-method

`void (No return value.)` **begin_multicaret_edit**() `🔗<class_TextEdit_method_begin_multicaret_edit>`

Starts an edit for multiple carets. The edit must be ended with `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`. Multicaret edits can be used to edit text at multiple carets and delay merging the carets until the end, so the caret indexes aren't affected immediately. `begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>` and `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>` can be nested, and the merge will happen at the last `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`.

    begin_complex_operation()
    begin_multicaret_edit()
    for i in range(get_caret_count()):
        if multicaret_edit_ignore_caret(i):
            continue
        # Logic here.
    end_multicaret_edit()
    end_complex_operation()

classref-item-separator

classref-method

`void (No return value.)` **cancel_ime**() `🔗<class_TextEdit_method_cancel_ime>`

Closes the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) if it is open. Any text in the IME will be lost.

classref-item-separator

classref-method

`void (No return value.)` **center_viewport_to_caret**(caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_center_viewport_to_caret>`

Centers the viewport on the line the editing caret is at. This also resets the `scroll_horizontal<class_TextEdit_property_scroll_horizontal>` value to `0`.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_TextEdit_method_clear>`

Performs a full reset of **TextEdit**, including undo history.

classref-item-separator

classref-method

`void (No return value.)` **clear_undo_history**() `🔗<class_TextEdit_method_clear_undo_history>`

Clears the undo history.

classref-item-separator

classref-method

`void (No return value.)` **collapse_carets**(from_line: `int<class_int>`, from_column: `int<class_int>`, to_line: `int<class_int>`, to_column: `int<class_int>`, inclusive: `bool<class_bool>` = false) `🔗<class_TextEdit_method_collapse_carets>`

Collapse all carets in the given range to the `from_line` and `from_column` position.

`inclusive` applies to both ends.

If `is_in_mulitcaret_edit()<class_TextEdit_method_is_in_mulitcaret_edit>` is `true`, carets that are collapsed will be `true` for `multicaret_edit_ignore_caret()<class_TextEdit_method_multicaret_edit_ignore_caret>`.

`merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>` will be called if any carets were collapsed.

classref-item-separator

classref-method

`void (No return value.)` **copy**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_copy>`

Copies the current text selection. Can be overridden with `_copy()<class_TextEdit_private_method__copy>`.

classref-item-separator

classref-method

`void (No return value.)` **cut**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_cut>`

Cut's the current selection. Can be overridden with `_cut()<class_TextEdit_private_method__cut>`.

classref-item-separator

classref-method

`void (No return value.)` **delete_selection**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_delete_selection>`

Deletes the selected text.

classref-item-separator

classref-method

`void (No return value.)` **deselect**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_deselect>`

Deselects the current selection.

classref-item-separator

classref-method

`void (No return value.)` **end_action**() `🔗<class_TextEdit_method_end_action>`

Marks the end of steps in the current action started with `start_action()<class_TextEdit_method_start_action>`.

classref-item-separator

classref-method

`void (No return value.)` **end_complex_operation**() `🔗<class_TextEdit_method_end_complex_operation>`

Ends a multipart edit, started with `begin_complex_operation()<class_TextEdit_method_begin_complex_operation>`. If called outside a complex operation, the current operation is pushed onto the undo/redo stack.

classref-item-separator

classref-method

`void (No return value.)` **end_multicaret_edit**() `🔗<class_TextEdit_method_end_multicaret_edit>`

Ends an edit for multiple carets, that was started with `begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>`. If this was the last `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>` and `merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>` was called, carets will be merged.

classref-item-separator

classref-method

`int<class_int>` **get_caret_column**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_caret_column>`

Returns the column the editing caret is at.

classref-item-separator

classref-method

`int<class_int>` **get_caret_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_caret_count>`

Returns the number of carets in this **TextEdit**.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_caret_draw_pos**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_caret_draw_pos>`

Returns the caret pixel draw position.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_caret_index_edit_order**() `🔗<class_TextEdit_method_get_caret_index_edit_order>`

**Deprecated:** Carets no longer need to be edited in any specific order. If the carets need to be sorted, use `get_sorted_carets()<class_TextEdit_method_get_sorted_carets>` instead.

Returns a list of caret indexes in their edit order, this done from bottom to top. Edit order refers to the way actions such as `insert_text_at_caret()<class_TextEdit_method_insert_text_at_caret>` are applied.

classref-item-separator

classref-method

`int<class_int>` **get_caret_line**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_caret_line>`

Returns the line the editing caret is on.

classref-item-separator

classref-method

`int<class_int>` **get_caret_wrap_index**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_caret_wrap_index>`

Returns the wrap index the editing caret is on.

classref-item-separator

classref-method

`int<class_int>` **get_first_non_whitespace_column**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_first_non_whitespace_column>`

Returns the first column containing a non-whitespace character on the given line. If there is only whitespace, returns the number of characters.

classref-item-separator

classref-method

`int<class_int>` **get_first_visible_line**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_first_visible_line>`

Returns the first visible line.

classref-item-separator

classref-method

`int<class_int>` **get_gutter_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_gutter_count>`

Returns the number of gutters registered.

classref-item-separator

classref-method

`String<class_String>` **get_gutter_name**(gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_gutter_name>`

Returns the name of the gutter at the given index.

classref-item-separator

classref-method

`GutterType<enum_TextEdit_GutterType>` **get_gutter_type**(gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_gutter_type>`

Returns the type of the gutter at the given index. Gutters can contain icons, text, or custom visuals.

classref-item-separator

classref-method

`int<class_int>` **get_gutter_width**(gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_gutter_width>`

Returns the width of the gutter at the given index.

classref-item-separator

classref-method

`HScrollBar<class_HScrollBar>` **get_h_scroll_bar**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_h_scroll_bar>`

Returns the `HScrollBar<class_HScrollBar>` used by **TextEdit**.

classref-item-separator

classref-method

`int<class_int>` **get_indent_level**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_indent_level>`

Returns the indent level of the given line. This is the number of spaces and tabs at the beginning of the line, with the tabs taking the tab size into account (see `get_tab_size()<class_TextEdit_method_get_tab_size>`).

classref-item-separator

classref-method

`int<class_int>` **get_last_full_visible_line**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_last_full_visible_line>`

Returns the last visible line. Use `get_last_full_visible_line_wrap_index()<class_TextEdit_method_get_last_full_visible_line_wrap_index>` for the wrap index.

classref-item-separator

classref-method

`int<class_int>` **get_last_full_visible_line_wrap_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_last_full_visible_line_wrap_index>`

Returns the last visible wrap index of the last visible line.

classref-item-separator

classref-method

`int<class_int>` **get_last_unhidden_line**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_last_unhidden_line>`

Returns the last unhidden line in the entire **TextEdit**.

classref-item-separator

classref-method

`String<class_String>` **get_line**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line>`

Returns the text of a specific line.

classref-item-separator

classref-method

`Color<class_Color>` **get_line_background_color**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_background_color>`

Returns the custom background color of the given line. If no color is set, returns `Color(0, 0, 0, 0)`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_line_column_at_pos**(position: `Vector2i<class_Vector2i>`, clamp_line: `bool<class_bool>` = true, clamp_column: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_column_at_pos>`

Returns the line and column at the given position. In the returned vector, `x` is the column and `y` is the line.

If `clamp_line` is `false` and `position` is below the last line, `Vector2i(-1, -1)` is returned.

If `clamp_column` is `false` and `position` is outside the column range of the line, `Vector2i(-1, -1)` is returned.

classref-item-separator

classref-method

`int<class_int>` **get_line_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_count>`

Returns the number of lines in the text.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_line_gutter_icon**(line: `int<class_int>`, gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_gutter_icon>`

Returns the icon currently in `gutter` at `line`. This only works when the gutter type is `GUTTER_TYPE_ICON<class_TextEdit_constant_GUTTER_TYPE_ICON>` (see `set_gutter_type()<class_TextEdit_method_set_gutter_type>`).

classref-item-separator

classref-method

`Color<class_Color>` **get_line_gutter_item_color**(line: `int<class_int>`, gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_gutter_item_color>`

Returns the color currently in `gutter` at `line`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_line_gutter_metadata**(line: `int<class_int>`, gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_gutter_metadata>`

Returns the metadata currently in `gutter` at `line`.

classref-item-separator

classref-method

`String<class_String>` **get_line_gutter_text**(line: `int<class_int>`, gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_gutter_text>`

Returns the text currently in `gutter` at `line`. This only works when the gutter type is `GUTTER_TYPE_STRING<class_TextEdit_constant_GUTTER_TYPE_STRING>` (see `set_gutter_type()<class_TextEdit_method_set_gutter_type>`).

classref-item-separator

classref-method

`int<class_int>` **get_line_height**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_height>`

Returns the maximum value of the line height among all lines.

**Note:** The return value is influenced by `line_spacing<class_TextEdit_theme_constant_line_spacing>` and `font_size<class_TextEdit_theme_font_size_font_size>`. And it will not be less than `1`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Vector2i<class_Vector2i>`\] **get_line_ranges_from_carets**(only_selections: `bool<class_bool>` = false, merge_adjacent: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_ranges_from_carets>`

Returns an `Array<class_Array>` of line ranges where `x` is the first line and `y` is the last line. All lines within these ranges will have a caret on them or be part of a selection. Each line will only be part of one line range, even if it has multiple carets on it.

If a selection's end column (`get_selection_to_column()<class_TextEdit_method_get_selection_to_column>`) is at column `0`, that line will not be included. If a selection begins on the line after another selection ends and `merge_adjacent` is `true`, or they begin and end on the same line, one line range will include both selections.

classref-item-separator

classref-method

`int<class_int>` **get_line_width**(line: `int<class_int>`, wrap_index: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_width>`

Returns the width in pixels of the `wrap_index` on `line`.

classref-item-separator

classref-method

`String<class_String>` **get_line_with_ime**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_with_ime>`

Returns line text as it is currently displayed, including IME composition string.

classref-item-separator

classref-method

`int<class_int>` **get_line_wrap_count**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_wrap_count>`

Returns the number of times the given line is wrapped.

classref-item-separator

classref-method

`int<class_int>` **get_line_wrap_index_at_column**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_wrap_index_at_column>`

Returns the wrap index of the given column on the given line. This ranges from `0` to `get_line_wrap_count()<class_TextEdit_method_get_line_wrap_count>`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_line_wrapped_text**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_line_wrapped_text>`

Returns an array of `String<class_String>`s representing each wrapped index.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_local_mouse_pos**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_local_mouse_pos>`

Returns the local mouse position adjusted for the text direction.

classref-item-separator

classref-method

`PopupMenu<class_PopupMenu>` **get_menu**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_menu>`

Returns the `PopupMenu<class_PopupMenu>` of this **TextEdit**. By default, this menu is displayed when right-clicking on the **TextEdit**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see `MenuItems<enum_TextEdit_MenuItems>`). For example:

gdscript

func ready():
var menu = get_menu() \# Remove all items after "Redo". menu.item_count = menu.get_item_index(MENU_REDO) + 1 \# Add custom items. menu.add_separator() menu.add_item("Insert Date", MENU_MAX + 1) \# Connect callback. menu.id_pressed.connect(on_item_pressed)

func on_item_pressed(id):
if id == MENU_MAX + 1:
insert_text_at_caret(Time.get_date_string_from_system())

csharp

public override void Ready() { var menu = GetMenu(); // Remove all items after "Redo". menu.ItemCount = menu.GetItemIndex(TextEdit.MenuItems.Redo) + 1; // Add custom items. menu.AddSeparator(); menu.AddItem("Insert Date", TextEdit.MenuItems.Max + 1); // Add event handler. menu.IdPressed += OnItemPressed; }

public void OnItemPressed(int id) { if (id == TextEdit.MenuItems.Max + 1) { InsertTextAtCaret(Time.GetDateStringFromSystem()); } }

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `Window.visible<class_Window_property_visible>` property.

classref-item-separator

classref-method

`int<class_int>` **get_minimap_line_at_pos**(position: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_minimap_line_at_pos>`

Returns the equivalent minimap line at `position`.

classref-item-separator

classref-method

`int<class_int>` **get_minimap_visible_lines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_minimap_visible_lines>`

Returns the number of lines that may be drawn on the minimap.

classref-item-separator

classref-method

`int<class_int>` **get_next_composite_character_column**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_next_composite_character_column>`

Returns the correct column at the end of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the start of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_next_composite_character_column(get_caret_line(), get_caret_column())`

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_next_visible_line_index_offset_from**(line: `int<class_int>`, wrap_index: `int<class_int>`, visible_amount: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_next_visible_line_index_offset_from>`

Similar to `get_next_visible_line_offset_from()<class_TextEdit_method_get_next_visible_line_offset_from>`, but takes into account the line wrap indexes. In the returned vector, `x` is the line, `y` is the wrap index.

classref-item-separator

classref-method

`int<class_int>` **get_next_visible_line_offset_from**(line: `int<class_int>`, visible_amount: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_next_visible_line_offset_from>`

Returns the count to the next visible line from `line` to `line + visible_amount`. Can also count backwards. For example if a **TextEdit** has 5 lines with lines 2 and 3 hidden, calling this with `line = 1, visible_amount = 1` would return 3.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_pos_at_line_column**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_pos_at_line_column>`

Returns the local position for the given `line` and `column`. If `x` or `y` of the returned vector equal `-1`, the position is outside of the viewable area of the control.

**Note:** The Y position corresponds to the bottom side of the line. Use `get_rect_at_line_column()<class_TextEdit_method_get_rect_at_line_column>` to get the top side position.

classref-item-separator

classref-method

`int<class_int>` **get_previous_composite_character_column**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_previous_composite_character_column>`

Returns the correct column at the start of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the end of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_previous_composite_character_column(get_caret_line(), get_caret_column())`

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **get_rect_at_line_column**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_rect_at_line_column>`

Returns the local position and size for the grapheme at the given `line` and `column`. If `x` or `y` position of the returned rect equal `-1`, the position is outside of the viewable area of the control.

**Note:** The Y position of the returned rect corresponds to the top side of the line, unlike `get_pos_at_line_column()<class_TextEdit_method_get_pos_at_line_column>` which returns the bottom side.

classref-item-separator

classref-method

`int<class_int>` **get_saved_version**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_saved_version>`

Returns the last tagged saved version from `tag_saved_version()<class_TextEdit_method_tag_saved_version>`.

classref-item-separator

classref-method

`float<class_float>` **get_scroll_pos_for_line**(line: `int<class_int>`, wrap_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_scroll_pos_for_line>`

Returns the scroll position for `wrap_index` of `line`.

classref-item-separator

classref-method

`String<class_String>` **get_selected_text**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_get_selected_text>`

Returns the text inside the selection of a caret, or all the carets if `caret_index` is its default value `-1`.

classref-item-separator

classref-method

`int<class_int>` **get_selection_at_line_column**(line: `int<class_int>`, column: `int<class_int>`, include_edges: `bool<class_bool>` = true, only_selections: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_at_line_column>`

Returns the caret index of the selection at the given `line` and `column`, or `-1` if there is none.

If `include_edges` is `false`, the position must be inside the selection and not at either end. If `only_selections` is `false`, carets without a selection will also be considered.

classref-item-separator

classref-method

`int<class_int>` **get_selection_column**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_column>`

**Deprecated:** Use `get_selection_origin_column()<class_TextEdit_method_get_selection_origin_column>` instead.

Returns the original start column of the selection.

classref-item-separator

classref-method

`int<class_int>` **get_selection_from_column**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_from_column>`

Returns the selection begin column. Returns the caret column if there is no selection.

classref-item-separator

classref-method

`int<class_int>` **get_selection_from_line**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_from_line>`

Returns the selection begin line. Returns the caret line if there is no selection.

classref-item-separator

classref-method

`int<class_int>` **get_selection_line**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_line>`

**Deprecated:** Use `get_selection_origin_line()<class_TextEdit_method_get_selection_origin_line>` instead.

Returns the original start line of the selection.

classref-item-separator

classref-method

`SelectionMode<enum_TextEdit_SelectionMode>` **get_selection_mode**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_mode>`

Returns the current selection mode.

classref-item-separator

classref-method

`int<class_int>` **get_selection_origin_column**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_origin_column>`

Returns the origin column of the selection. This is the opposite end from the caret.

classref-item-separator

classref-method

`int<class_int>` **get_selection_origin_line**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_origin_line>`

Returns the origin line of the selection. This is the opposite end from the caret.

classref-item-separator

classref-method

`int<class_int>` **get_selection_to_column**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_to_column>`

Returns the selection end column. Returns the caret column if there is no selection.

classref-item-separator

classref-method

`int<class_int>` **get_selection_to_line**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_selection_to_line>`

Returns the selection end line. Returns the caret line if there is no selection.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_sorted_carets**(include_ignored_carets: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_sorted_carets>`

Returns the carets sorted by selection beginning from lowest line and column to highest (from top to bottom of text).

If `include_ignored_carets` is `false`, carets from `multicaret_edit_ignore_caret()<class_TextEdit_method_multicaret_edit_ignore_caret>` will be ignored.

classref-item-separator

classref-method

`int<class_int>` **get_tab_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_tab_size>`

Returns the **TextEdit**'s' tab size.

classref-item-separator

classref-method

`int<class_int>` **get_total_gutter_width**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_total_gutter_width>`

Returns the total width of all gutters and internal padding.

classref-item-separator

classref-method

`int<class_int>` **get_total_visible_line_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_total_visible_line_count>`

Returns the total number of lines in the text. This includes wrapped lines and excludes folded lines. If `wrap_mode<class_TextEdit_property_wrap_mode>` is set to `LINE_WRAPPING_NONE<class_TextEdit_constant_LINE_WRAPPING_NONE>` and no lines are folded (see `CodeEdit.is_line_folded()<class_CodeEdit_method_is_line_folded>`) then this is equivalent to `get_line_count()<class_TextEdit_method_get_line_count>`. See `get_visible_line_count_in_range()<class_TextEdit_method_get_visible_line_count_in_range>` for a limited range of lines.

classref-item-separator

classref-method

`VScrollBar<class_VScrollBar>` **get_v_scroll_bar**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_v_scroll_bar>`

Returns the `VScrollBar<class_VScrollBar>` of the **TextEdit**.

classref-item-separator

classref-method

`int<class_int>` **get_version**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_version>`

Returns the current version of the **TextEdit**. The version is a count of recorded operations by the undo/redo history.

classref-item-separator

classref-method

`int<class_int>` **get_visible_line_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_visible_line_count>`

Returns the number of lines that can visually fit, rounded down, based on this control's height.

classref-item-separator

classref-method

`int<class_int>` **get_visible_line_count_in_range**(from_line: `int<class_int>`, to_line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_visible_line_count_in_range>`

Returns the total number of lines between `from_line` and `to_line` (inclusive) in the text. This includes wrapped lines and excludes folded lines. If the range covers all lines it is equivalent to `get_total_visible_line_count()<class_TextEdit_method_get_total_visible_line_count>`.

classref-item-separator

classref-method

`String<class_String>` **get_word_at_pos**(position: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_word_at_pos>`

Returns the word at `position`.

classref-item-separator

classref-method

`String<class_String>` **get_word_under_caret**(caret_index: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_get_word_under_caret>`

Returns a `String<class_String>` text with the word under the caret's location.

classref-item-separator

classref-method

`bool<class_bool>` **has_ime_text**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_has_ime_text>`

Returns `true` if the user has text in the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME).

classref-item-separator

classref-method

`bool<class_bool>` **has_redo**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_has_redo>`

Returns `true` if a "redo" action is available.

classref-item-separator

classref-method

`bool<class_bool>` **has_selection**(caret_index: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_has_selection>`

Returns `true` if the user has selected text.

classref-item-separator

classref-method

`bool<class_bool>` **has_undo**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_has_undo>`

Returns `true` if an "undo" action is available.

classref-item-separator

classref-method

`void (No return value.)` **insert_line_at**(line: `int<class_int>`, text: `String<class_String>`) `🔗<class_TextEdit_method_insert_line_at>`

Inserts a new line with `text` at `line`.

classref-item-separator

classref-method

`void (No return value.)` **insert_text**(text: `String<class_String>`, line: `int<class_int>`, column: `int<class_int>`, before_selection_begin: `bool<class_bool>` = true, before_selection_end: `bool<class_bool>` = false) `🔗<class_TextEdit_method_insert_text>`

Inserts the `text` at `line` and `column`.

If `before_selection_begin` is `true`, carets and selections that begin at `line` and `column` will moved to the end of the inserted text, along with all carets after it.

If `before_selection_end` is `true`, selections that end at `line` and `column` will be extended to the end of the inserted text. These parameters can be used to insert text inside of or outside of selections.

classref-item-separator

classref-method

`void (No return value.)` **insert_text_at_caret**(text: `String<class_String>`, caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_insert_text_at_caret>`

Insert the specified text at the caret position.

classref-item-separator

classref-method

`bool<class_bool>` **is_caret_after_selection_origin**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_caret_after_selection_origin>`

Returns `true` if the caret of the selection is after the selection origin. This can be used to determine the direction of the selection.

classref-item-separator

classref-method

`bool<class_bool>` **is_caret_visible**(caret_index: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_caret_visible>`

Returns `true` if the caret is visible, `false` otherwise. A caret will be considered hidden if it is outside the scrollable area when scrolling is enabled.

**Note:** `is_caret_visible()<class_TextEdit_method_is_caret_visible>` does not account for a caret being off-screen if it is still within the scrollable area. It will return `true` even if the caret is off-screen as long as it meets **TextEdit**'s own conditions for being visible. This includes uses of `scroll_fit_content_width<class_TextEdit_property_scroll_fit_content_width>` and `scroll_fit_content_height<class_TextEdit_property_scroll_fit_content_height>` that cause the **TextEdit** to expand beyond the viewport's bounds.

**Note:** This method does *not* guarantee an accurate visibility check immediately after setting the caret position. The correct value may only be available in the next frame after the **TextEdit** has finished drawing. This also applies to any operation that causes the **TextEdit** to change in size.

classref-item-separator

classref-method

`bool<class_bool>` **is_dragging_cursor**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_dragging_cursor>`

Returns `true` if the user is dragging their mouse for scrolling, selecting, or text dragging.

classref-item-separator

classref-method

`bool<class_bool>` **is_gutter_clickable**(gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_gutter_clickable>`

Returns `true` if the gutter at the given index is clickable. See `set_gutter_clickable()<class_TextEdit_method_set_gutter_clickable>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_gutter_drawn**(gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_gutter_drawn>`

Returns `true` if the gutter at the given index is currently drawn. See `set_gutter_draw()<class_TextEdit_method_set_gutter_draw>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_gutter_overwritable**(gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_gutter_overwritable>`

Returns `true` if the gutter at the given index is overwritable. See `set_gutter_overwritable()<class_TextEdit_method_set_gutter_overwritable>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_in_mulitcaret_edit**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_in_mulitcaret_edit>`

Returns `true` if a `begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>` has been called and `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>` has not yet been called.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_gutter_clickable**(line: `int<class_int>`, gutter: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_line_gutter_clickable>`

Returns `true` if the gutter at the given index on the given line is clickable. See `set_line_gutter_clickable()<class_TextEdit_method_set_line_gutter_clickable>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_in_viewport**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_line_in_viewport>`

Returns `true` if the given line is within the scope of the scrollable area of the viewport.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_wrapped**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_line_wrapped>`

Returns if the given line is wrapped.

classref-item-separator

classref-method

`bool<class_bool>` **is_menu_visible**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_menu_visible>`

Returns `true` if the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided). See `get_menu()<class_TextEdit_method_get_menu>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_mouse_over_selection**(edges: `bool<class_bool>`, caret_index: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_mouse_over_selection>`

Returns `true` if the mouse is over a selection. If `edges` is `true`, the edges are considered part of the selection.

classref-item-separator

classref-method

`bool<class_bool>` **is_overtype_mode_enabled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_is_overtype_mode_enabled>`

Returns `true` if overtype mode is enabled. See `set_overtype_mode_enabled()<class_TextEdit_method_set_overtype_mode_enabled>`.

classref-item-separator

classref-method

`void (No return value.)` **menu_option**(option: `int<class_int>`) `🔗<class_TextEdit_method_menu_option>`

Executes a given action as defined in the `MenuItems<enum_TextEdit_MenuItems>` enum.

classref-item-separator

classref-method

`void (No return value.)` **merge_gutters**(from_line: `int<class_int>`, to_line: `int<class_int>`) `🔗<class_TextEdit_method_merge_gutters>`

Merge the gutters from `from_line` into `to_line`. Only overwritable gutters will be copied. See `set_gutter_overwritable()<class_TextEdit_method_set_gutter_overwritable>`.

classref-item-separator

classref-method

`void (No return value.)` **merge_overlapping_carets**() `🔗<class_TextEdit_method_merge_overlapping_carets>`

Merges any overlapping carets. Will favor the newest caret, or the caret with a selection.

If `is_in_mulitcaret_edit()<class_TextEdit_method_is_in_mulitcaret_edit>` is `true`, the merge will be queued to happen at the end of the multicaret edit. See `begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>` and `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`.

**Note:** This is not called when a caret changes position but after certain actions, so it is possible to get into a state where carets overlap.

classref-item-separator

classref-method

`bool<class_bool>` **multicaret_edit_ignore_caret**(caret_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_multicaret_edit_ignore_caret>`

Returns `true` if the given `caret_index` should be ignored as part of a multicaret edit. See `begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>` and `end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`. Carets that should be ignored are ones that were part of removed text and will likely be merged at the end of the edit, or carets that were added during the edit.

It is recommended to `continue` within a loop iterating on multiple carets if a caret should be ignored.

classref-item-separator

classref-method

`void (No return value.)` **paste**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_paste>`

Paste at the current location. Can be overridden with `_paste()<class_TextEdit_private_method__paste>`.

classref-item-separator

classref-method

`void (No return value.)` **paste_primary_clipboard**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_paste_primary_clipboard>`

Pastes the primary clipboard.

classref-item-separator

classref-method

`void (No return value.)` **redo**() `🔗<class_TextEdit_method_redo>`

Perform redo operation.

classref-item-separator

classref-method

`void (No return value.)` **remove_caret**(caret: `int<class_int>`) `🔗<class_TextEdit_method_remove_caret>`

Removes the given caret index.

**Note:** This can result in adjustment of all other caret indices.

classref-item-separator

classref-method

`void (No return value.)` **remove_gutter**(gutter: `int<class_int>`) `🔗<class_TextEdit_method_remove_gutter>`

Removes the gutter at the given index.

classref-item-separator

classref-method

`void (No return value.)` **remove_line_at**(line: `int<class_int>`, move_carets_down: `bool<class_bool>` = true) `🔗<class_TextEdit_method_remove_line_at>`

Removes the line of text at `line`. Carets on this line will attempt to match their previous visual x position.

If `move_carets_down` is `true` carets will move to the next line down, otherwise carets will move up.

classref-item-separator

classref-method

`void (No return value.)` **remove_secondary_carets**() `🔗<class_TextEdit_method_remove_secondary_carets>`

Removes all additional carets.

classref-item-separator

classref-method

`void (No return value.)` **remove_text**(from_line: `int<class_int>`, from_column: `int<class_int>`, to_line: `int<class_int>`, to_column: `int<class_int>`) `🔗<class_TextEdit_method_remove_text>`

Removes text between the given positions.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **search**(text: `String<class_String>`, flags: `int<class_int>`, from_line: `int<class_int>`, from_column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextEdit_method_search>`

Perform a search inside the text. Search flags can be specified in the `SearchFlags<enum_TextEdit_SearchFlags>` enum.

In the returned vector, `x` is the column, `y` is the line. If no results are found, both are equal to `-1`.

gdscript

var result = search("print", SEARCH_WHOLE_WORDS, 0, 0) if result.x != -1: \# Result found. var line_number = result.y var column_number = result.x

csharp

Vector2I result = Search("print", (uint)TextEdit.SearchFlags.WholeWords, 0, 0); if (result.X != -1) { // Result found. int lineNumber = result.Y; int columnNumber = result.X; }

classref-item-separator

classref-method

`void (No return value.)` **select**(origin_line: `int<class_int>`, origin_column: `int<class_int>`, caret_line: `int<class_int>`, caret_column: `int<class_int>`, caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_select>`

Selects text from `origin_line` and `origin_column` to `caret_line` and `caret_column` for the given `caret_index`. This moves the selection origin and the caret. If the positions are the same, the selection will be deselected.

If `selecting_enabled<class_TextEdit_property_selecting_enabled>` is `false`, no selection will occur.

**Note:** If supporting multiple carets this will not check for any overlap. See `merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`.

classref-item-separator

classref-method

`void (No return value.)` **select_all**() `🔗<class_TextEdit_method_select_all>`

Select all the text.

If `selecting_enabled<class_TextEdit_property_selecting_enabled>` is `false`, no selection will occur.

classref-item-separator

classref-method

`void (No return value.)` **select_word_under_caret**(caret_index: `int<class_int>` = -1) `🔗<class_TextEdit_method_select_word_under_caret>`

Selects the word under the caret.

classref-item-separator

classref-method

`void (No return value.)` **set_caret_column**(column: `int<class_int>`, adjust_viewport: `bool<class_bool>` = true, caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_caret_column>`

Moves the caret to the specified `column` index.

If `adjust_viewport` is `true`, the viewport will center at the caret position after the move occurs.

**Note:** If supporting multiple carets this will not check for any overlap. See `merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`.

classref-item-separator

classref-method

`void (No return value.)` **set_caret_line**(line: `int<class_int>`, adjust_viewport: `bool<class_bool>` = true, can_be_hidden: `bool<class_bool>` = true, wrap_index: `int<class_int>` = 0, caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_caret_line>`

Moves the caret to the specified `line` index. The caret column will be moved to the same visual position it was at the last time `set_caret_column()<class_TextEdit_method_set_caret_column>` was called, or clamped to the end of the line.

If `adjust_viewport` is `true`, the viewport will center at the caret position after the move occurs.

If `can_be_hidden` is `true`, the specified `line` can be hidden.

If `wrap_index` is `-1`, the caret column will be clamped to the `line`'s length. If `wrap_index` is greater than `-1`, the column will be moved to attempt to match the visual x position on the line's `wrap_index` to the position from the last time `set_caret_column()<class_TextEdit_method_set_caret_column>` was called.

**Note:** If supporting multiple carets this will not check for any overlap. See `merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`.

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_clickable**(gutter: `int<class_int>`, clickable: `bool<class_bool>`) `🔗<class_TextEdit_method_set_gutter_clickable>`

If `true`, the mouse cursor will change to a pointing hand (`Control.CURSOR_POINTING_HAND<class_Control_constant_CURSOR_POINTING_HAND>`) when hovering over the gutter at the given index. See `is_gutter_clickable()<class_TextEdit_method_is_gutter_clickable>` and `set_line_gutter_clickable()<class_TextEdit_method_set_line_gutter_clickable>`.

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_custom_draw**(column: `int<class_int>`, draw_callback: `Callable<class_Callable>`) `🔗<class_TextEdit_method_set_gutter_custom_draw>`

Set a custom draw callback for the gutter at the given index. `draw_callback` must take the following arguments: A line index `int<class_int>`, a gutter index `int<class_int>`, and an area `Rect2<class_Rect2>`. This callback only works when the gutter type is `GUTTER_TYPE_CUSTOM<class_TextEdit_constant_GUTTER_TYPE_CUSTOM>` (see `set_gutter_type()<class_TextEdit_method_set_gutter_type>`).

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_draw**(gutter: `int<class_int>`, draw: `bool<class_bool>`) `🔗<class_TextEdit_method_set_gutter_draw>`

If `true`, the gutter at the given index is drawn. The gutter type (`set_gutter_type()<class_TextEdit_method_set_gutter_type>`) determines how it is drawn. See `is_gutter_drawn()<class_TextEdit_method_is_gutter_drawn>`.

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_name**(gutter: `int<class_int>`, name: `String<class_String>`) `🔗<class_TextEdit_method_set_gutter_name>`

Sets the name of the gutter at the given index.

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_overwritable**(gutter: `int<class_int>`, overwritable: `bool<class_bool>`) `🔗<class_TextEdit_method_set_gutter_overwritable>`

If `true`, the line data of the gutter at the given index can be overridden when using `merge_gutters()<class_TextEdit_method_merge_gutters>`. See `is_gutter_overwritable()<class_TextEdit_method_is_gutter_overwritable>`.

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_type**(gutter: `int<class_int>`, type: `GutterType<enum_TextEdit_GutterType>`) `🔗<class_TextEdit_method_set_gutter_type>`

Sets the type of gutter at the given index. Gutters can contain icons, text, or custom visuals.

classref-item-separator

classref-method

`void (No return value.)` **set_gutter_width**(gutter: `int<class_int>`, width: `int<class_int>`) `🔗<class_TextEdit_method_set_gutter_width>`

Set the width of the gutter at the given index.

classref-item-separator

classref-method

`void (No return value.)` **set_line**(line: `int<class_int>`, new_text: `String<class_String>`) `🔗<class_TextEdit_method_set_line>`

Sets the text for a specific `line`.

Carets on the line will attempt to keep their visual x position.

classref-item-separator

classref-method

`void (No return value.)` **set_line_as_center_visible**(line: `int<class_int>`, wrap_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_line_as_center_visible>`

Positions the `wrap_index` of `line` at the center of the viewport.

classref-item-separator

classref-method

`void (No return value.)` **set_line_as_first_visible**(line: `int<class_int>`, wrap_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_line_as_first_visible>`

Positions the `wrap_index` of `line` at the top of the viewport.

classref-item-separator

classref-method

`void (No return value.)` **set_line_as_last_visible**(line: `int<class_int>`, wrap_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_line_as_last_visible>`

Positions the `wrap_index` of `line` at the bottom of the viewport.

classref-item-separator

classref-method

`void (No return value.)` **set_line_background_color**(line: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_TextEdit_method_set_line_background_color>`

Sets the custom background color of the given line. If transparent, this color is applied on top of the default background color (See `background_color<class_TextEdit_theme_color_background_color>`). If set to `Color(0, 0, 0, 0)`, no additional color is applied.

classref-item-separator

classref-method

`void (No return value.)` **set_line_gutter_clickable**(line: `int<class_int>`, gutter: `int<class_int>`, clickable: `bool<class_bool>`) `🔗<class_TextEdit_method_set_line_gutter_clickable>`

If `clickable` is `true`, makes the `gutter` on the given `line` clickable. This is like `set_gutter_clickable()<class_TextEdit_method_set_gutter_clickable>`, but for a single line. If `is_gutter_clickable()<class_TextEdit_method_is_gutter_clickable>` is `true`, this will not have any effect. See `is_line_gutter_clickable()<class_TextEdit_method_is_line_gutter_clickable>` and `gutter_clicked<class_TextEdit_signal_gutter_clicked>`.

classref-item-separator

classref-method

`void (No return value.)` **set_line_gutter_icon**(line: `int<class_int>`, gutter: `int<class_int>`, icon: `Texture2D<class_Texture2D>`) `🔗<class_TextEdit_method_set_line_gutter_icon>`

Sets the icon for `gutter` on `line` to `icon`. This only works when the gutter type is `GUTTER_TYPE_ICON<class_TextEdit_constant_GUTTER_TYPE_ICON>` (see `set_gutter_type()<class_TextEdit_method_set_gutter_type>`).

classref-item-separator

classref-method

`void (No return value.)` **set_line_gutter_item_color**(line: `int<class_int>`, gutter: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_TextEdit_method_set_line_gutter_item_color>`

Sets the color for `gutter` on `line` to `color`.

classref-item-separator

classref-method

`void (No return value.)` **set_line_gutter_metadata**(line: `int<class_int>`, gutter: `int<class_int>`, metadata: `Variant<class_Variant>`) `🔗<class_TextEdit_method_set_line_gutter_metadata>`

Sets the metadata for `gutter` on `line` to `metadata`.

classref-item-separator

classref-method

`void (No return value.)` **set_line_gutter_text**(line: `int<class_int>`, gutter: `int<class_int>`, text: `String<class_String>`) `🔗<class_TextEdit_method_set_line_gutter_text>`

Sets the text for `gutter` on `line` to `text`. This only works when the gutter type is `GUTTER_TYPE_STRING<class_TextEdit_constant_GUTTER_TYPE_STRING>` (see `set_gutter_type()<class_TextEdit_method_set_gutter_type>`).

classref-item-separator

classref-method

`void (No return value.)` **set_overtype_mode_enabled**(enabled: `bool<class_bool>`) `🔗<class_TextEdit_method_set_overtype_mode_enabled>`

If `true`, enables overtype mode. In this mode, typing overrides existing text instead of inserting text. The `ProjectSettings.input/ui_text_toggle_insert_mode<class_ProjectSettings_property_input/ui_text_toggle_insert_mode>` action toggles overtype mode. See `is_overtype_mode_enabled()<class_TextEdit_method_is_overtype_mode_enabled>`.

classref-item-separator

classref-method

`void (No return value.)` **set_search_flags**(flags: `int<class_int>`) `🔗<class_TextEdit_method_set_search_flags>`

Sets the search `flags`. This is used with `set_search_text()<class_TextEdit_method_set_search_text>` to highlight occurrences of the searched text. Search flags can be specified from the `SearchFlags<enum_TextEdit_SearchFlags>` enum.

classref-item-separator

classref-method

`void (No return value.)` **set_search_text**(search_text: `String<class_String>`) `🔗<class_TextEdit_method_set_search_text>`

Sets the search text. See `set_search_flags()<class_TextEdit_method_set_search_flags>`.

classref-item-separator

classref-method

`void (No return value.)` **set_selection_mode**(mode: `SelectionMode<enum_TextEdit_SelectionMode>`) `🔗<class_TextEdit_method_set_selection_mode>`

Sets the current selection mode.

classref-item-separator

classref-method

`void (No return value.)` **set_selection_origin_column**(column: `int<class_int>`, caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_selection_origin_column>`

Sets the selection origin column to the `column` for the given `caret_index`. If the selection origin is moved to the caret position, the selection will deselect.

classref-item-separator

classref-method

`void (No return value.)` **set_selection_origin_line**(line: `int<class_int>`, can_be_hidden: `bool<class_bool>` = true, wrap_index: `int<class_int>` = -1, caret_index: `int<class_int>` = 0) `🔗<class_TextEdit_method_set_selection_origin_line>`

Sets the selection origin line to the `line` for the given `caret_index`. If the selection origin is moved to the caret position, the selection will deselect.

If `can_be_hidden` is `false`, The line will be set to the nearest unhidden line below or above.

If `wrap_index` is `-1`, the selection origin column will be clamped to the `line`'s length. If `wrap_index` is greater than `-1`, the column will be moved to attempt to match the visual x position on the line's `wrap_index` to the position from the last time `set_selection_origin_column()<class_TextEdit_method_set_selection_origin_column>` or `select()<class_TextEdit_method_select>` was called.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_size**(size: `int<class_int>`) `🔗<class_TextEdit_method_set_tab_size>`

Sets the tab size for the **TextEdit** to use.

classref-item-separator

classref-method

`void (No return value.)` **set_tooltip_request_func**(callback: `Callable<class_Callable>`) `🔗<class_TextEdit_method_set_tooltip_request_func>`

Provide custom tooltip text. The callback method must take the following args: `hovered_word: String`.

classref-item-separator

classref-method

`void (No return value.)` **skip_selection_for_next_occurrence**() `🔗<class_TextEdit_method_skip_selection_for_next_occurrence>`

Moves a selection and a caret for the next occurrence of the current selection. If there is no active selection, moves to the next occurrence of the word under caret.

classref-item-separator

classref-method

`void (No return value.)` **start_action**(action: `EditAction<enum_TextEdit_EditAction>`) `🔗<class_TextEdit_method_start_action>`

Starts an action, will end the current action if `action` is different.

An action will also end after a call to `end_action()<class_TextEdit_method_end_action>`, after `ProjectSettings.gui/timers/text_edit_idle_detect_sec<class_ProjectSettings_property_gui/timers/text_edit_idle_detect_sec>` is triggered or a new undoable step outside the `start_action()<class_TextEdit_method_start_action>` and `end_action()<class_TextEdit_method_end_action>` calls.

classref-item-separator

classref-method

`void (No return value.)` **swap_lines**(from_line: `int<class_int>`, to_line: `int<class_int>`) `🔗<class_TextEdit_method_swap_lines>`

Swaps the two lines. Carets will be swapped with the lines.

classref-item-separator

classref-method

`void (No return value.)` **tag_saved_version**() `🔗<class_TextEdit_method_tag_saved_version>`

Tag the current version as saved.

classref-item-separator

classref-method

`void (No return value.)` **undo**() `🔗<class_TextEdit_method_undo>`

Perform undo operation.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **background_color** = `Color(0, 0, 0, 0)` `🔗<class_TextEdit_theme_color_background_color>`

Sets the background `Color<class_Color>` of this **TextEdit**.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **caret_background_color** = `Color(0, 0, 0, 1)` `🔗<class_TextEdit_theme_color_caret_background_color>`

`Color<class_Color>` of the text behind the caret when using a block caret.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **caret_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_TextEdit_theme_color_caret_color>`

`Color<class_Color>` of the caret. This can be set to a fully transparent color to hide the caret entirely.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **current_line_color** = `Color(0.25, 0.25, 0.26, 0.8)` `🔗<class_TextEdit_theme_color_current_line_color>`

Background `Color<class_Color>` of the line containing the caret.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_TextEdit_theme_color_font_color>`

Sets the font `Color<class_Color>`.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_outline_color** = `Color(0, 0, 0, 1)` `🔗<class_TextEdit_theme_color_font_outline_color>`

The tint of text outline of the **TextEdit**.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)` `🔗<class_TextEdit_theme_color_font_placeholder_color>`

Font color for `placeholder_text<class_TextEdit_property_placeholder_text>`.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_readonly_color** = `Color(0.875, 0.875, 0.875, 0.5)` `🔗<class_TextEdit_theme_color_font_readonly_color>`

Sets the font `Color<class_Color>` when `editable<class_TextEdit_property_editable>` is disabled.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_selected_color** = `Color(0, 0, 0, 0)` `🔗<class_TextEdit_theme_color_font_selected_color>`

Sets the `Color<class_Color>` of the selected text. If equal to `Color(0, 0, 0, 0)`, it will be ignored.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **search_result_border_color** = `Color(0.3, 0.3, 0.3, 0.4)` `🔗<class_TextEdit_theme_color_search_result_border_color>`

`Color<class_Color>` of the border around text that matches the search query.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **search_result_color** = `Color(0.3, 0.3, 0.3, 1)` `🔗<class_TextEdit_theme_color_search_result_color>`

`Color<class_Color>` behind the text that matches the search query.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **selection_color** = `Color(0.5, 0.5, 0.5, 1)` `🔗<class_TextEdit_theme_color_selection_color>`

Sets the highlight `Color<class_Color>` of text selections.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **word_highlighted_color** = `Color(0.5, 0.5, 0.5, 0.25)` `🔗<class_TextEdit_theme_color_word_highlighted_color>`

Sets the highlight `Color<class_Color>` of multiple occurrences. `highlight_all_occurrences<class_TextEdit_property_highlight_all_occurrences>` has to be enabled.

classref-item-separator

classref-themeproperty

`int<class_int>` **caret_width** = `1` `🔗<class_TextEdit_theme_constant_caret_width>`

The caret's width in pixels. Greater values can be used to improve accessibility by ensuring the caret is easily visible, or to ensure consistency with a large font size. If set to `0` or lower, the caret width is automatically set to 1 pixel and multiplied by the display scaling factor.

classref-item-separator

classref-themeproperty

`int<class_int>` **line_spacing** = `4` `🔗<class_TextEdit_theme_constant_line_spacing>`

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

classref-item-separator

classref-themeproperty

`int<class_int>` **outline_size** = `0` `🔗<class_TextEdit_theme_constant_outline_size>`

The size of the text outline.

**Note:** If using a font with `FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>` enabled, its `FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the value of `outline_size<class_TextEdit_theme_constant_outline_size>` for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

classref-item-separator

classref-themeproperty

`int<class_int>` **wrap_offset** = `10` `🔗<class_TextEdit_theme_constant_wrap_offset>`

Sets an additional margin for line wrapping width.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **font** `🔗<class_TextEdit_theme_font_font>`

Sets the default `Font<class_Font>`.

classref-item-separator

classref-themeproperty

`int<class_int>` **font_size** `🔗<class_TextEdit_theme_font_size_font_size>`

Sets default font size.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **space** `🔗<class_TextEdit_theme_icon_space>`

Sets a custom `Texture2D<class_Texture2D>` for space text characters.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **tab** `🔗<class_TextEdit_theme_icon_tab>`

Sets a custom `Texture2D<class_Texture2D>` for tab text characters.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **focus** `🔗<class_TextEdit_theme_style_focus>`

Sets the `StyleBox<class_StyleBox>` when in focus. The `focus<class_TextEdit_theme_style_focus>` `StyleBox<class_StyleBox>` is displayed *over* the base `StyleBox<class_StyleBox>`, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the base `StyleBox<class_StyleBox>` remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **normal** `🔗<class_TextEdit_theme_style_normal>`

Sets the `StyleBox<class_StyleBox>` of this **TextEdit**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **read_only** `🔗<class_TextEdit_theme_style_read_only>`

Sets the `StyleBox<class_StyleBox>` of this **TextEdit** when `editable<class_TextEdit_property_editable>` is disabled.