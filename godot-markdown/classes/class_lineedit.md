github_url
hide

# LineEdit

**Inherits:** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

An input field for single-line text.

classref-introduction-group

## Description

**LineEdit** provides an input field for editing a single line of text.

- When the **LineEdit** control is focused using the keyboard arrow keys, it will only gain focus and not enter edit mode.
- To enter edit mode, click on the control with the mouse, see also `keep_editing_on_text_submit<class_LineEdit_property_keep_editing_on_text_submit>`.
- To exit edit mode, press `ui_text_submit` or `ui_cancel` (by default `Escape`) actions.
- Check `edit()<class_LineEdit_method_edit>`, `unedit()<class_LineEdit_method_unedit>`, `is_editing()<class_LineEdit_method_is_editing>`, and `editing_toggled<class_LineEdit_signal_editing_toggled>` for more information.

While entering text, it is possible to insert special characters using Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold `Alt` and type the codepoint on the numpad. For example, to enter the character `á` (U+00E1), hold `Alt` and type `+E1` on the numpad (the leading zeroes can be omitted).
- To enter OEM codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (OEM 160), hold `Alt` and type `160` on the numpad.
- To enter Windows codepoints, hold `Alt` and type the code on the numpad. For example, to enter the character `á` (Windows 0225), hold `Alt` and type `0`, `2`, `2`, `5` on the numpad. The leading zero here must **not** be omitted, as this is how Windows codepoints are distinguished from OEM codepoints.

**Important:**

- Focusing the **LineEdit** with `ui_focus_next` (by default `Tab`) or `ui_focus_prev` (by default `Shift + Tab`) or `Control.grab_focus()<class_Control_method_grab_focus>` still enters edit mode (for compatibility).

**LineEdit** features many built-in shortcuts that are always available (`Ctrl` here maps to `Cmd` on macOS):

- `Ctrl + C`: Copy
- `Ctrl + X`: Cut
- `Ctrl + V` or `Ctrl + Y`: Paste/"yank"
- `Ctrl + Z`: Undo
- `Ctrl + ~`: Swap input direction.
- `Ctrl + Shift + Z`: Redo
- `Ctrl + U`: Delete text from the caret position to the beginning of the line
- `Ctrl + K`: Delete text from the caret position to the end of the line
- `Ctrl + A`: Select all text
- `Up Arrow`/`Down Arrow`: Move the caret to the beginning/end of the line

On macOS, some extra keyboard shortcuts are available:

- `Cmd + F`: Same as `Right Arrow`, move the caret one character right
- `Cmd + B`: Same as `Left Arrow`, move the caret one character left
- `Cmd + P`: Same as `Up Arrow`, move the caret to the previous line
- `Cmd + N`: Same as `Down Arrow`, move the caret to the next line
- `Cmd + D`: Same as `Delete`, delete the character on the right side of caret
- `Cmd + H`: Same as `Backspace`, delete the character on the left side of the caret
- `Cmd + A`: Same as `Home`, move the caret to the beginning of the line
- `Cmd + E`: Same as `End`, move the caret to the end of the line
- `Cmd + Left Arrow`: Same as `Home`, move the caret to the beginning of the line
- `Cmd + Right Arrow`: Same as `End`, move the caret to the end of the line

**Note:** Caret movement shortcuts listed above are not affected by `shortcut_keys_enabled<class_LineEdit_property_shortcut_keys_enabled>`.

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

**editing_toggled**(toggled_on: `bool<class_bool>`) `🔗<class_LineEdit_signal_editing_toggled>`

Emitted when the **LineEdit** switches in or out of edit mode.

classref-item-separator

classref-signal

**text_change_rejected**(rejected_substring: `String<class_String>`) `🔗<class_LineEdit_signal_text_change_rejected>`

Emitted when appending text that overflows the `max_length<class_LineEdit_property_max_length>`. The appended text is truncated to fit `max_length<class_LineEdit_property_max_length>`, and the part that couldn't fit is passed as the `rejected_substring` argument.

classref-item-separator

classref-signal

**text_changed**(new_text: `String<class_String>`) `🔗<class_LineEdit_signal_text_changed>`

Emitted when the text changes.

classref-item-separator

classref-signal

**text_submitted**(new_text: `String<class_String>`) `🔗<class_LineEdit_signal_text_submitted>`

Emitted when the user presses the `ui_text_submit` action (by default: `Enter` or `Kp Enter`) while the **LineEdit** has focus.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **MenuItems**: `🔗<enum_LineEdit_MenuItems>`

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_COPY** = `1`

Copies the selected text.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the caret's position).

Non-printable escape characters are automatically stripped from the OS clipboard via `String.strip_escapes()<class_String_method_strip_escapes>`.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_CLEAR** = `3`

Erases the whole **LineEdit** text.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_SELECT_ALL** = `4`

Selects the whole **LineEdit** text.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_UNDO** = `5`

Undoes the previous action.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_REDO** = `6`

Reverse the last undo action.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_SUBMENU_TEXT_DIR** = `7`

ID of "Text Writing Direction" submenu.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_DISPLAY_UCC** = `12`

Toggles control character display.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_SUBMENU_INSERT_UCC** = `13`

ID of "Insert Control Character" submenu.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

classref-enumeration-constant

`MenuItems<enum_LineEdit_MenuItems>` **MENU_MAX** = `31`

Represents the size of the `MenuItems<enum_LineEdit_MenuItems>` enum.

classref-item-separator

classref-enumeration

enum **VirtualKeyboardType**: `🔗<enum_LineEdit_VirtualKeyboardType>`

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email addresses.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should disable autocomplete and autocapitalization.

**Note:** This is not supported on Web. Instead, this behaves identically to `KEYBOARD_TYPE_DEFAULT<class_LineEdit_constant_KEYBOARD_TYPE_DEFAULT>`.

classref-enumeration-constant

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

classref-item-separator

classref-enumeration

enum **ExpandMode**: `🔗<enum_LineEdit_ExpandMode>`

classref-enumeration-constant

`ExpandMode<enum_LineEdit_ExpandMode>` **EXPAND_MODE_ORIGINAL_SIZE** = `0`

Use the original size for the right icon.

classref-enumeration-constant

`ExpandMode<enum_LineEdit_ExpandMode>` **EXPAND_MODE_FIT_TO_TEXT** = `1`

Scale the right icon's size to match the size of the text.

classref-enumeration-constant

`ExpandMode<enum_LineEdit_ExpandMode>` **EXPAND_MODE_FIT_TO_LINE_EDIT** = `2`

Scale the right icon to fit the LineEdit.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **alignment** = `0` `🔗<class_LineEdit_property_alignment>`

classref-property-setget

- `void (No return value.)` **set_horizontal_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_horizontal_alignment**()

The text's horizontal alignment.

classref-item-separator

classref-property

`bool<class_bool>` **backspace_deletes_composite_character_enabled** = `false` `🔗<class_LineEdit_property_backspace_deletes_composite_character_enabled>`

classref-property-setget

- `void (No return value.)` **set_backspace_deletes_composite_character_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_backspace_deletes_composite_character_enabled**()

If `true` and `caret_mid_grapheme<class_LineEdit_property_caret_mid_grapheme>` is `false`, backspace deletes an entire composite character such as ❤️‍🩹, instead of deleting part of the composite character.

classref-item-separator

classref-property

`bool<class_bool>` **caret_blink** = `false` `🔗<class_LineEdit_property_caret_blink>`

classref-property-setget

- `void (No return value.)` **set_caret_blink_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_caret_blink_enabled**()

If `true`, makes the caret blink.

classref-item-separator

classref-property

`float<class_float>` **caret_blink_interval** = `0.65` `🔗<class_LineEdit_property_caret_blink_interval>`

classref-property-setget

- `void (No return value.)` **set_caret_blink_interval**(value: `float<class_float>`)
- `float<class_float>` **get_caret_blink_interval**()

The interval at which the caret blinks (in seconds).

classref-item-separator

classref-property

`int<class_int>` **caret_column** = `0` `🔗<class_LineEdit_property_caret_column>`

classref-property-setget

- `void (No return value.)` **set_caret_column**(value: `int<class_int>`)
- `int<class_int>` **get_caret_column**()

The caret's column position inside the **LineEdit**. When set, the text may scroll to accommodate it.

classref-item-separator

classref-property

`bool<class_bool>` **caret_force_displayed** = `false` `🔗<class_LineEdit_property_caret_force_displayed>`

classref-property-setget

- `void (No return value.)` **set_caret_force_displayed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_caret_force_displayed**()

If `true`, the **LineEdit** will always show the caret, even if not editing or focus is lost.

classref-item-separator

classref-property

`bool<class_bool>` **caret_mid_grapheme** = `false` `🔗<class_LineEdit_property_caret_mid_grapheme>`

classref-property-setget

- `void (No return value.)` **set_caret_mid_grapheme_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_caret_mid_grapheme_enabled**()

Allow moving caret, selecting and removing the individual composite character components.

**Note:** `Backspace` is always removing individual composite character components.

classref-item-separator

classref-property

`bool<class_bool>` **clear_button_enabled** = `false` `🔗<class_LineEdit_property_clear_button_enabled>`

classref-property-setget

- `void (No return value.)` **set_clear_button_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_clear_button_enabled**()

If `true`, the **LineEdit** will show a clear button if `text<class_LineEdit_property_text>` is not empty, which can be used to clear the text quickly.

classref-item-separator

classref-property

`bool<class_bool>` **context_menu_enabled** = `true` `🔗<class_LineEdit_property_context_menu_enabled>`

classref-property-setget

- `void (No return value.)` **set_context_menu_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_context_menu_enabled**()

If `true`, the context menu will appear when right-clicked.

classref-item-separator

classref-property

`bool<class_bool>` **deselect_on_focus_loss_enabled** = `true` `🔗<class_LineEdit_property_deselect_on_focus_loss_enabled>`

classref-property-setget

- `void (No return value.)` **set_deselect_on_focus_loss_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_deselect_on_focus_loss_enabled**()

If `true`, the selected text will be deselected when focus is lost.

classref-item-separator

classref-property

`bool<class_bool>` **drag_and_drop_selection_enabled** = `true` `🔗<class_LineEdit_property_drag_and_drop_selection_enabled>`

classref-property-setget

- `void (No return value.)` **set_drag_and_drop_selection_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text.

classref-item-separator

classref-property

`bool<class_bool>` **draw_control_chars** = `false` `🔗<class_LineEdit_property_draw_control_chars>`

classref-property-setget

- `void (No return value.)` **set_draw_control_chars**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_draw_control_chars**()

If `true`, control characters are displayed.

classref-item-separator

classref-property

`bool<class_bool>` **editable** = `true` `🔗<class_LineEdit_property_editable>`

classref-property-setget

- `void (No return value.)` **set_editable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editable**()

If `false`, existing text cannot be modified and new text cannot be added.

classref-item-separator

classref-property

`bool<class_bool>` **emoji_menu_enabled** = `true` `🔗<class_LineEdit_property_emoji_menu_enabled>`

classref-property-setget

- `void (No return value.)` **set_emoji_menu_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_emoji_menu_enabled**()

If `true`, "Emoji and Symbols" menu is enabled.

classref-item-separator

classref-property

`bool<class_bool>` **expand_to_text_length** = `false` `🔗<class_LineEdit_property_expand_to_text_length>`

classref-property-setget

- `void (No return value.)` **set_expand_to_text_length_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_expand_to_text_length_enabled**()

If `true`, the **LineEdit** width will increase to stay longer than the `text<class_LineEdit_property_text>`. It will **not** compress if the `text<class_LineEdit_property_text>` is shortened.

classref-item-separator

classref-property

`bool<class_bool>` **flat** = `false` `🔗<class_LineEdit_property_flat>`

classref-property-setget

- `void (No return value.)` **set_flat**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_flat**()

If `true`, the **LineEdit** doesn't display decoration.

classref-item-separator

classref-property

`ExpandMode<enum_LineEdit_ExpandMode>` **icon_expand_mode** = `0` `🔗<class_LineEdit_property_icon_expand_mode>`

classref-property-setget

- `void (No return value.)` **set_icon_expand_mode**(value: `ExpandMode<enum_LineEdit_ExpandMode>`)
- `ExpandMode<enum_LineEdit_ExpandMode>` **get_icon_expand_mode**()

Define the scaling behavior of the `right_icon<class_LineEdit_property_right_icon>`.

classref-item-separator

classref-property

`bool<class_bool>` **keep_editing_on_text_submit** = `false` `🔗<class_LineEdit_property_keep_editing_on_text_submit>`

classref-property-setget

- `void (No return value.)` **set_keep_editing_on_text_submit**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_editing_kept_on_text_submit**()

If `true`, the **LineEdit** will not exit edit mode when text is submitted by pressing `ui_text_submit` action (by default: `Enter` or `Kp Enter`).

classref-item-separator

classref-property

`String<class_String>` **language** = `""` `🔗<class_LineEdit_property_language>`

classref-property-setget

- `void (No return value.)` **set_language**(value: `String<class_String>`)
- `String<class_String>` **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

classref-item-separator

classref-property

`int<class_int>` **max_length** = `0` `🔗<class_LineEdit_property_max_length>`

classref-property-setget

- `void (No return value.)` **set_max_length**(value: `int<class_int>`)
- `int<class_int>` **get_max_length**()

Maximum number of characters that can be entered inside the **LineEdit**. If `0`, there is no limit.

When a limit is defined, characters that would exceed `max_length<class_LineEdit_property_max_length>` are truncated. This happens both for existing `text<class_LineEdit_property_text>` contents when setting the max length, or for new text inserted in the **LineEdit**, including pasting.

If any input text is truncated, the `text_change_rejected<class_LineEdit_signal_text_change_rejected>` signal is emitted with the truncated substring as a parameter:

gdscript

text = "Hello world" max_length = 5 \# text becomes "Hello". max_length = 10 text += " goodbye" \# text becomes "Hello good". \# text_change_rejected is emitted with "bye" as a parameter.

csharp

Text = "Hello world"; MaxLength = 5; // Text becomes "Hello". MaxLength = 10; Text += " goodbye"; // Text becomes "Hello good". // text_change_rejected is emitted with "bye" as a parameter.

classref-item-separator

classref-property

`bool<class_bool>` **middle_mouse_paste_enabled** = `true` `🔗<class_LineEdit_property_middle_mouse_paste_enabled>`

classref-property-setget

- `void (No return value.)` **set_middle_mouse_paste_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_middle_mouse_paste_enabled**()

If `false`, using middle mouse button to paste clipboard will be disabled.

**Note:** This method is only implemented on Linux.

classref-item-separator

classref-property

`String<class_String>` **placeholder_text** = `""` `🔗<class_LineEdit_property_placeholder_text>`

classref-property-setget

- `void (No return value.)` **set_placeholder**(value: `String<class_String>`)
- `String<class_String>` **get_placeholder**()

Text shown when the **LineEdit** is empty. It is **not** the **LineEdit**'s default value (see `text<class_LineEdit_property_text>`).

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **right_icon** `🔗<class_LineEdit_property_right_icon>`

classref-property-setget

- `void (No return value.)` **set_right_icon**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_right_icon**()

Sets the icon that will appear in the right end of the **LineEdit** if there's no `text<class_LineEdit_property_text>`, or always, if `clear_button_enabled<class_LineEdit_property_clear_button_enabled>` is set to `false`.

classref-item-separator

classref-property

`float<class_float>` **right_icon_scale** = `1.0` `🔗<class_LineEdit_property_right_icon_scale>`

classref-property-setget

- `void (No return value.)` **set_right_icon_scale**(value: `float<class_float>`)
- `float<class_float>` **get_right_icon_scale**()

Scale ratio of the icon when `icon_expand_mode<class_LineEdit_property_icon_expand_mode>` is set to `EXPAND_MODE_FIT_TO_LINE_EDIT<class_LineEdit_constant_EXPAND_MODE_FIT_TO_LINE_EDIT>`.

classref-item-separator

classref-property

`bool<class_bool>` **secret** = `false` `🔗<class_LineEdit_property_secret>`

classref-property-setget

- `void (No return value.)` **set_secret**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_secret**()

If `true`, every character is replaced with the secret character (see `secret_character<class_LineEdit_property_secret_character>`).

classref-item-separator

classref-property

`String<class_String>` **secret_character** = `"•"` `🔗<class_LineEdit_property_secret_character>`

classref-property-setget

- `void (No return value.)` **set_secret_character**(value: `String<class_String>`)
- `String<class_String>` **get_secret_character**()

The character to use to mask secret input. Only a single character can be used as the secret character. If it is longer than one character, only the first one will be used. If it is empty, a space will be used instead.

classref-item-separator

classref-property

`bool<class_bool>` **select_all_on_focus** = `false` `🔗<class_LineEdit_property_select_all_on_focus>`

classref-property-setget

- `void (No return value.)` **set_select_all_on_focus**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_select_all_on_focus**()

If `true`, the **LineEdit** will select the whole text when it gains focus.

classref-item-separator

classref-property

`bool<class_bool>` **selecting_enabled** = `true` `🔗<class_LineEdit_property_selecting_enabled>`

classref-property-setget

- `void (No return value.)` **set_selecting_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_selecting_enabled**()

If `false`, it's impossible to select the text using mouse nor keyboard.

classref-item-separator

classref-property

`bool<class_bool>` **shortcut_keys_enabled** = `true` `🔗<class_LineEdit_property_shortcut_keys_enabled>`

classref-property-setget

- `void (No return value.)` **set_shortcut_keys_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_shortcut_keys_enabled**()

If `true`, shortcut keys for context menu items are enabled, even if the context menu is disabled.

classref-item-separator

classref-property

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **structured_text_bidi_override** = `0` `🔗<class_LineEdit_property_structured_text_bidi_override>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override**(value: `StructuredTextParser<enum_TextServer_StructuredTextParser>`)
- `StructuredTextParser<enum_TextServer_StructuredTextParser>` **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

classref-item-separator

classref-property

`Array<class_Array>` **structured_text_bidi_override_options** = `[]` `🔗<class_LineEdit_property_structured_text_bidi_override_options>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override_options**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

classref-item-separator

classref-property

`String<class_String>` **text** = `""` `🔗<class_LineEdit_property_text>`

classref-property-setget

- `void (No return value.)` **set_text**(value: `String<class_String>`)
- `String<class_String>` **get_text**()

String value of the **LineEdit**.

**Note:** Changing text using this property won't emit the `text_changed<class_LineEdit_signal_text_changed>` signal.

classref-item-separator

classref-property

`TextDirection<enum_Control_TextDirection>` **text_direction** = `0` `🔗<class_LineEdit_property_text_direction>`

classref-property-setget

- `void (No return value.)` **set_text_direction**(value: `TextDirection<enum_Control_TextDirection>`)
- `TextDirection<enum_Control_TextDirection>` **get_text_direction**()

Base text writing direction.

classref-item-separator

classref-property

`bool<class_bool>` **virtual_keyboard_enabled** = `true` `🔗<class_LineEdit_property_virtual_keyboard_enabled>`

classref-property-setget

- `void (No return value.)` **set_virtual_keyboard_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_virtual_keyboard_enabled**()

If `true`, the native virtual keyboard is enabled on platforms that support it.

classref-item-separator

classref-property

`bool<class_bool>` **virtual_keyboard_show_on_focus** = `true` `🔗<class_LineEdit_property_virtual_keyboard_show_on_focus>`

classref-property-setget

- `void (No return value.)` **set_virtual_keyboard_show_on_focus**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_virtual_keyboard_show_on_focus**()

If `true`, the native virtual keyboard is shown on focus events on platforms that support it.

classref-item-separator

classref-property

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **virtual_keyboard_type** = `0` `🔗<class_LineEdit_property_virtual_keyboard_type>`

classref-property-setget

- `void (No return value.)` **set_virtual_keyboard_type**(value: `VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`)
- `VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>` **get_virtual_keyboard_type**()

Specifies the type of virtual keyboard to show.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **apply_ime**() `🔗<class_LineEdit_method_apply_ime>`

Applies text from the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) and closes the IME if it is open.

classref-item-separator

classref-method

`void (No return value.)` **cancel_ime**() `🔗<class_LineEdit_method_cancel_ime>`

Closes the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME) if it is open. Any text in the IME will be lost.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_LineEdit_method_clear>`

Erases the **LineEdit**'s `text<class_LineEdit_property_text>`.

classref-item-separator

classref-method

`void (No return value.)` **delete_char_at_caret**() `🔗<class_LineEdit_method_delete_char_at_caret>`

Deletes one character at the caret's current position (equivalent to pressing `Delete`).

classref-item-separator

classref-method

`void (No return value.)` **delete_text**(from_column: `int<class_int>`, to_column: `int<class_int>`) `🔗<class_LineEdit_method_delete_text>`

Deletes a section of the `text<class_LineEdit_property_text>` going from position `from_column` to `to_column`. Both parameters should be within the text's length.

classref-item-separator

classref-method

`void (No return value.)` **deselect**() `🔗<class_LineEdit_method_deselect>`

Clears the current selection.

classref-item-separator

classref-method

`void (No return value.)` **edit**(hide_focus: `bool<class_bool>` = false) `🔗<class_LineEdit_method_edit>`

Allows entering edit mode whether the **LineEdit** is focused or not. If `hide_focus` is `true`, the focused state will not be shown (see `Control.grab_focus()<class_Control_method_grab_focus>`).

See also `keep_editing_on_text_submit<class_LineEdit_property_keep_editing_on_text_submit>`.

classref-item-separator

classref-method

`PopupMenu<class_PopupMenu>` **get_menu**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_get_menu>`

Returns the `PopupMenu<class_PopupMenu>` of this **LineEdit**. By default, this menu is displayed when right-clicking on the **LineEdit**.

You can add custom menu items or remove standard ones. Make sure your IDs don't conflict with the standard ones (see `MenuItems<enum_LineEdit_MenuItems>`). For example:

gdscript

func ready():
var menu = get_menu() \# Remove all items after "Redo". menu.item_count = menu.get_item_index(MENU_REDO) + 1 \# Add custom items. menu.add_separator() menu.add_item("Insert Date", MENU_MAX + 1) \# Connect callback. menu.id_pressed.connect(on_item_pressed)

func on_item_pressed(id):
if id == MENU_MAX + 1:
insert_text_at_caret(Time.get_date_string_from_system())

csharp

public override void Ready() { var menu = GetMenu(); // Remove all items after "Redo". menu.ItemCount = menu.GetItemIndex(LineEdit.MenuItems.Redo) + 1; // Add custom items. menu.AddSeparator(); menu.AddItem("Insert Date", LineEdit.MenuItems.Max + 1); // Add event handler. menu.IdPressed += OnItemPressed; }

public void OnItemPressed(int id) { if (id == LineEdit.MenuItems.Max + 1) { InsertTextAtCaret(Time.GetDateStringFromSystem()); } }

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `Window.visible<class_Window_property_visible>` property.

classref-item-separator

classref-method

`int<class_int>` **get_next_composite_character_column**(column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_get_next_composite_character_column>`

Returns the correct column at the end of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the start of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_next_composite_character_column(get_caret_column())`

classref-item-separator

classref-method

`int<class_int>` **get_previous_composite_character_column**(column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_get_previous_composite_character_column>`

Returns the correct column at the start of a composite character like ❤️‍🩹 (mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is comprised of more than one Unicode code point, if the caret is at the end of the composite character. Also returns the correct column with the caret at mid grapheme and for non-composite characters.

**Note:** To check at caret location use `get_previous_composite_character_column(get_caret_column())`

classref-item-separator

classref-method

`float<class_float>` **get_scroll_offset**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_get_scroll_offset>`

Returns the scroll offset due to `caret_column<class_LineEdit_property_caret_column>`, as a number of characters.

classref-item-separator

classref-method

`String<class_String>` **get_selected_text**() `🔗<class_LineEdit_method_get_selected_text>`

Returns the text inside the selection.

classref-item-separator

classref-method

`int<class_int>` **get_selection_from_column**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_get_selection_from_column>`

Returns the selection begin column.

classref-item-separator

classref-method

`int<class_int>` **get_selection_to_column**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_get_selection_to_column>`

Returns the selection end column.

classref-item-separator

classref-method

`bool<class_bool>` **has_ime_text**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_has_ime_text>`

Returns `true` if the user has text in the [Input Method Editor](https://en.wikipedia.org/wiki/Input_method) (IME).

classref-item-separator

classref-method

`bool<class_bool>` **has_redo**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_has_redo>`

Returns `true` if a "redo" action is available.

classref-item-separator

classref-method

`bool<class_bool>` **has_selection**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_has_selection>`

Returns `true` if the user has selected text.

classref-item-separator

classref-method

`bool<class_bool>` **has_undo**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_has_undo>`

Returns `true` if an "undo" action is available.

classref-item-separator

classref-method

`void (No return value.)` **insert_text_at_caret**(text: `String<class_String>`) `🔗<class_LineEdit_method_insert_text_at_caret>`

Inserts `text` at the caret. If the resulting value is longer than `max_length<class_LineEdit_property_max_length>`, nothing happens.

classref-item-separator

classref-method

`bool<class_bool>` **is_editing**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_is_editing>`

Returns whether the **LineEdit** is being edited.

classref-item-separator

classref-method

`bool<class_bool>` **is_menu_visible**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LineEdit_method_is_menu_visible>`

Returns whether the menu is visible. Use this instead of `get_menu().visible` to improve performance (so the creation of the menu is avoided).

classref-item-separator

classref-method

`void (No return value.)` **menu_option**(option: `int<class_int>`) `🔗<class_LineEdit_method_menu_option>`

Executes a given action as defined in the `MenuItems<enum_LineEdit_MenuItems>` enum.

classref-item-separator

classref-method

`void (No return value.)` **select**(from: `int<class_int>` = 0, to: `int<class_int>` = -1) `🔗<class_LineEdit_method_select>`

Selects characters inside **LineEdit** between `from` and `to`. By default, `from` is at the beginning and `to` at the end.

gdscript

text = "Welcome" select() \# Will select "Welcome". select(4) \# Will select "ome". select(2, 5) \# Will select "lco".

csharp

Text = "Welcome"; Select(); // Will select "Welcome". Select(4); // Will select "ome". Select(2, 5); // Will select "lco".

classref-item-separator

classref-method

`void (No return value.)` **select_all**() `🔗<class_LineEdit_method_select_all>`

Selects the whole `String<class_String>`.

classref-item-separator

classref-method

`void (No return value.)` **unedit**() `🔗<class_LineEdit_method_unedit>`

Allows exiting edit mode while preserving focus.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **caret_color** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_LineEdit_theme_color_caret_color>`

Color of the **LineEdit**'s caret (text cursor). This can be set to a fully transparent color to hide the caret entirely.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **clear_button_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_LineEdit_theme_color_clear_button_color>`

Color used as default tint for the clear button.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **clear_button_color_pressed** = `Color(1, 1, 1, 1)` `🔗<class_LineEdit_theme_color_clear_button_color_pressed>`

Color used for the clear button when it's pressed.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_LineEdit_theme_color_font_color>`

Default font color.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_outline_color** = `Color(0, 0, 0, 1)` `🔗<class_LineEdit_theme_color_font_outline_color>`

The tint of text outline of the **LineEdit**.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)` `🔗<class_LineEdit_theme_color_font_placeholder_color>`

Font color for `placeholder_text<class_LineEdit_property_placeholder_text>`.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_selected_color** = `Color(1, 1, 1, 1)` `🔗<class_LineEdit_theme_color_font_selected_color>`

Font color for selected text (inside the selection rectangle).

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_uneditable_color** = `Color(0.875, 0.875, 0.875, 0.5)` `🔗<class_LineEdit_theme_color_font_uneditable_color>`

Font color when editing is disabled.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **selection_color** = `Color(0.5, 0.5, 0.5, 1)` `🔗<class_LineEdit_theme_color_selection_color>`

Color of the selection rectangle.

classref-item-separator

classref-themeproperty

`int<class_int>` **caret_width** = `1` `🔗<class_LineEdit_theme_constant_caret_width>`

The caret's width in pixels. Greater values can be used to improve accessibility by ensuring the caret is easily visible, or to ensure consistency with a large font size.

classref-item-separator

classref-themeproperty

`int<class_int>` **minimum_character_width** = `4` `🔗<class_LineEdit_theme_constant_minimum_character_width>`

Minimum horizontal space for the text (not counting the clear button and content margins). This value is measured in count of 'M' characters (i.e. this number of 'M' characters can be displayed without scrolling).

classref-item-separator

classref-themeproperty

`int<class_int>` **outline_size** = `0` `🔗<class_LineEdit_theme_constant_outline_size>`

The size of the text outline.

**Note:** If using a font with `FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>` enabled, its `FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the value of `outline_size<class_LineEdit_theme_constant_outline_size>` for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **font** `🔗<class_LineEdit_theme_font_font>`

Font used for the text.

classref-item-separator

classref-themeproperty

`int<class_int>` **font_size** `🔗<class_LineEdit_theme_font_size_font_size>`

Font size of the **LineEdit**'s text.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **clear** `🔗<class_LineEdit_theme_icon_clear>`

Texture for the clear button. See `clear_button_enabled<class_LineEdit_property_clear_button_enabled>`.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **focus** `🔗<class_LineEdit_theme_style_focus>`

Background used when **LineEdit** has GUI focus. The `focus<class_LineEdit_theme_style_focus>` `StyleBox<class_StyleBox>` is displayed *over* the base `StyleBox<class_StyleBox>`, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the base `StyleBox<class_StyleBox>` remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **normal** `🔗<class_LineEdit_theme_style_normal>`

Default background for the **LineEdit**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **read_only** `🔗<class_LineEdit_theme_style_read_only>`

Background used when **LineEdit** is in read-only mode (`editable<class_LineEdit_property_editable>` is set to `false`).