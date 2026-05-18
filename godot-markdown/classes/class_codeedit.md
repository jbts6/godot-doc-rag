github_url
hide

# CodeEdit

**Inherits:** `TextEdit<class_TextEdit>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A multiline text editor designed for editing code.

classref-introduction-group

## Description

CodeEdit is a specialized `TextEdit<class_TextEdit>` designed for editing plain text code files. It has many features commonly found in code editors such as line numbers, line folding, code completion, indent management, and string/comment management.

**Note:** Regardless of locale, **CodeEdit** will by default always use left-to-right text direction to correctly display source code.

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

**breakpoint_toggled**(line: `int<class_int>`) `🔗<class_CodeEdit_signal_breakpoint_toggled>`

Emitted when a breakpoint is added or removed from a line. If the line is removed via backspace, a signal is emitted at the old line.

classref-item-separator

classref-signal

**code_completion_requested**() `🔗<class_CodeEdit_signal_code_completion_requested>`

Emitted when the user requests code completion. This signal will not be sent if `_request_code_completion()<class_CodeEdit_private_method__request_code_completion>` is overridden or `code_completion_enabled<class_CodeEdit_property_code_completion_enabled>` is `false`.

classref-item-separator

classref-signal

**symbol_hovered**(symbol: `String<class_String>`, line: `int<class_int>`, column: `int<class_int>`) `🔗<class_CodeEdit_signal_symbol_hovered>`

Emitted when the user hovers over a symbol. Unlike `Control.mouse_entered<class_Control_signal_mouse_entered>`, this signal is not emitted immediately, but when the cursor is over the symbol for `ProjectSettings.gui/timers/tooltip_delay_sec<class_ProjectSettings_property_gui/timers/tooltip_delay_sec>` seconds.

**Note:** `symbol_tooltip_on_hover<class_CodeEdit_property_symbol_tooltip_on_hover>` must be `true` for this signal to be emitted.

classref-item-separator

classref-signal

**symbol_lookup**(symbol: `String<class_String>`, line: `int<class_int>`, column: `int<class_int>`) `🔗<class_CodeEdit_signal_symbol_lookup>`

Emitted when the user has clicked on a valid symbol.

classref-item-separator

classref-signal

**symbol_validate**(symbol: `String<class_String>`) `🔗<class_CodeEdit_signal_symbol_validate>`

Emitted when the user hovers over a symbol. The symbol should be validated and responded to, by calling `set_symbol_lookup_word_as_valid()<class_CodeEdit_method_set_symbol_lookup_word_as_valid>`.

**Note:** `symbol_lookup_on_click<class_CodeEdit_property_symbol_lookup_on_click>` must be `true` for this signal to be emitted.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **CodeCompletionKind**: `🔗<enum_CodeEdit_CodeCompletionKind>`

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_CLASS** = `0`

Marks the option as a class.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_FUNCTION** = `1`

Marks the option as a function.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_SIGNAL** = `2`

Marks the option as a Godot signal.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_VARIABLE** = `3`

Marks the option as a variable.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_MEMBER** = `4`

Marks the option as a member.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_ENUM** = `5`

Marks the option as an enum entry.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_CONSTANT** = `6`

Marks the option as a constant.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_NODE_PATH** = `7`

Marks the option as a Godot node path.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_FILE_PATH** = `8`

Marks the option as a file path.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_PLAIN_TEXT** = `9`

Marks the option as unclassified or plain text.

classref-enumeration-constant

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>` **KIND_KEYWORD** = `10`

Marks the option as a keyword.

classref-item-separator

classref-enumeration

enum **CodeCompletionLocation**: `🔗<enum_CodeEdit_CodeCompletionLocation>`

classref-enumeration-constant

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>` **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g. a local variable. Subsequent value of location represent options from the outer class, the exact value represent how far they are (in terms of inner classes).

classref-enumeration-constant

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>` **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to the location of the code completion query. Perform a bitwise OR with the class depth (e.g. `0` for the local class, `1` for the parent, `2` for the grandparent, etc.) to store the depth of an option in the class or a parent class.

classref-enumeration-constant

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>` **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived class (e.g. Autoload Singletons).

classref-enumeration-constant

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>` **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum constants - e.g. built-in classes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **auto_brace_completion_enabled** = `false` `🔗<class_CodeEdit_property_auto_brace_completion_enabled>`

classref-property-setget

- `void (No return value.)` **set_auto_brace_completion_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_auto_brace_completion_enabled**()

If `true`, uses `auto_brace_completion_pairs<class_CodeEdit_property_auto_brace_completion_pairs>` to automatically insert the closing brace when the opening brace is inserted by typing or autocompletion. Also automatically removes the closing brace when using backspace on the opening brace.

classref-item-separator

classref-property

`bool<class_bool>` **auto_brace_completion_highlight_matching** = `false` `🔗<class_CodeEdit_property_auto_brace_completion_highlight_matching>`

classref-property-setget

- `void (No return value.)` **set_highlight_matching_braces_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_highlight_matching_braces_enabled**()

If `true`, highlights brace pairs when the caret is on either one, using `auto_brace_completion_pairs<class_CodeEdit_property_auto_brace_completion_pairs>`. If matching, the pairs will be underlined. If a brace is unmatched, it is colored with `brace_mismatch_color<class_CodeEdit_theme_color_brace_mismatch_color>`.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **auto_brace_completion_pairs** = `{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }` `🔗<class_CodeEdit_property_auto_brace_completion_pairs>`

classref-property-setget

- `void (No return value.)` **set_auto_brace_completion_pairs**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_auto_brace_completion_pairs**()

Sets the brace pairs to be autocompleted. For each entry in the dictionary, the key is the opening brace and the value is the closing brace that matches it. A brace is a `String<class_String>` made of symbols. See `auto_brace_completion_enabled<class_CodeEdit_property_auto_brace_completion_enabled>` and `auto_brace_completion_highlight_matching<class_CodeEdit_property_auto_brace_completion_highlight_matching>`.

classref-item-separator

classref-property

`bool<class_bool>` **code_completion_enabled** = `false` `🔗<class_CodeEdit_property_code_completion_enabled>`

classref-property-setget

- `void (No return value.)` **set_code_completion_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_code_completion_enabled**()

If `true`, the `ProjectSettings.input/ui_text_completion_query<class_ProjectSettings_property_input/ui_text_completion_query>` action requests code completion. To handle it, see `_request_code_completion()<class_CodeEdit_private_method__request_code_completion>` or `code_completion_requested<class_CodeEdit_signal_code_completion_requested>`.

classref-item-separator

classref-property

`Array<class_Array>`\[`String<class_String>`\] **code_completion_prefixes** = `[]` `🔗<class_CodeEdit_property_code_completion_prefixes>`

classref-property-setget

- `void (No return value.)` **set_code_completion_prefixes**(value: `Array<class_Array>`\[`String<class_String>`\])
- `Array<class_Array>`\[`String<class_String>`\] **get_code_completion_prefixes**()

Sets prefixes that will trigger code completion.

classref-item-separator

classref-property

`Array<class_Array>`\[`String<class_String>`\] **delimiter_comments** = `[]` `🔗<class_CodeEdit_property_delimiter_comments>`

classref-property-setget

- `void (No return value.)` **set_comment_delimiters**(value: `Array<class_Array>`\[`String<class_String>`\])
- `Array<class_Array>`\[`String<class_String>`\] **get_comment_delimiters**()

Sets the comment delimiters. All existing comment delimiters will be removed.

classref-item-separator

classref-property

`Array<class_Array>`\[`String<class_String>`\] **delimiter_strings** = `["' '", "\" \""]` `🔗<class_CodeEdit_property_delimiter_strings>`

classref-property-setget

- `void (No return value.)` **set_string_delimiters**(value: `Array<class_Array>`\[`String<class_String>`\])
- `Array<class_Array>`\[`String<class_String>`\] **get_string_delimiters**()

Sets the string delimiters. All existing string delimiters will be removed.

classref-item-separator

classref-property

`bool<class_bool>` **gutters_draw_bookmarks** = `false` `🔗<class_CodeEdit_property_gutters_draw_bookmarks>`

classref-property-setget

- `void (No return value.)` **set_draw_bookmarks_gutter**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_bookmarks_gutter**()

If `true`, bookmarks are drawn in the gutter. This gutter is shared with breakpoints and executing lines. See `set_line_as_bookmarked()<class_CodeEdit_method_set_line_as_bookmarked>`.

classref-item-separator

classref-property

`bool<class_bool>` **gutters_draw_breakpoints_gutter** = `false` `🔗<class_CodeEdit_property_gutters_draw_breakpoints_gutter>`

classref-property-setget

- `void (No return value.)` **set_draw_breakpoints_gutter**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_breakpoints_gutter**()

If `true`, breakpoints are drawn in the gutter. This gutter is shared with bookmarks and executing lines. Clicking the gutter will toggle the breakpoint for the line, see `set_line_as_breakpoint()<class_CodeEdit_method_set_line_as_breakpoint>`.

classref-item-separator

classref-property

`bool<class_bool>` **gutters_draw_executing_lines** = `false` `🔗<class_CodeEdit_property_gutters_draw_executing_lines>`

classref-property-setget

- `void (No return value.)` **set_draw_executing_lines_gutter**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_executing_lines_gutter**()

If `true`, executing lines are marked in the gutter. This gutter is shared with breakpoints and bookmarks. See `set_line_as_executing()<class_CodeEdit_method_set_line_as_executing>`.

classref-item-separator

classref-property

`bool<class_bool>` **gutters_draw_fold_gutter** = `false` `🔗<class_CodeEdit_property_gutters_draw_fold_gutter>`

classref-property-setget

- `void (No return value.)` **set_draw_fold_gutter**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drawing_fold_gutter**()

If `true`, the fold gutter is drawn. In this gutter, the `can_fold_code_region<class_CodeEdit_theme_icon_can_fold_code_region>` icon is drawn for each foldable line (see `can_fold_line()<class_CodeEdit_method_can_fold_line>`) and the `folded_code_region<class_CodeEdit_theme_icon_folded_code_region>` icon is drawn for each folded line (see `is_line_folded()<class_CodeEdit_method_is_line_folded>`). These icons can be clicked to toggle the fold state, see `toggle_foldable_line()<class_CodeEdit_method_toggle_foldable_line>`. `line_folding<class_CodeEdit_property_line_folding>` must be `true` to show icons.

classref-item-separator

classref-property

`bool<class_bool>` **gutters_draw_line_numbers** = `false` `🔗<class_CodeEdit_property_gutters_draw_line_numbers>`

classref-property-setget

- `void (No return value.)` **set_draw_line_numbers**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_draw_line_numbers_enabled**()

If `true`, the line number gutter is drawn. Line numbers start at `1` and are incremented for each line of text. Clicking and dragging in the line number gutter will select entire lines of text.

classref-item-separator

classref-property

`int<class_int>` **gutters_line_numbers_min_digits** = `3` `🔗<class_CodeEdit_property_gutters_line_numbers_min_digits>`

classref-property-setget

- `void (No return value.)` **set_line_numbers_min_digits**(value: `int<class_int>`)
- `int<class_int>` **get_line_numbers_min_digits**()

The minimum width in digits reserved for the line number gutter.

classref-item-separator

classref-property

`bool<class_bool>` **gutters_zero_pad_line_numbers** = `false` `🔗<class_CodeEdit_property_gutters_zero_pad_line_numbers>`

classref-property-setget

- `void (No return value.)` **set_line_numbers_zero_padded**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_line_numbers_zero_padded**()

If `true`, line numbers drawn in the gutter are zero padded based on the total line count. Requires `gutters_draw_line_numbers<class_CodeEdit_property_gutters_draw_line_numbers>` to be set to `true`.

classref-item-separator

classref-property

`bool<class_bool>` **indent_automatic** = `false` `🔗<class_CodeEdit_property_indent_automatic>`

classref-property-setget

- `void (No return value.)` **set_auto_indent_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_auto_indent_enabled**()

If `true`, an extra indent is automatically inserted when a new line is added and a prefix in `indent_automatic_prefixes<class_CodeEdit_property_indent_automatic_prefixes>` is found. If a brace pair opening key is found, the matching closing brace will be moved to another new line (see `auto_brace_completion_pairs<class_CodeEdit_property_auto_brace_completion_pairs>`).

classref-item-separator

classref-property

`Array<class_Array>`\[`String<class_String>`\] **indent_automatic_prefixes** = `[":", "{", "[", "("]` `🔗<class_CodeEdit_property_indent_automatic_prefixes>`

classref-property-setget

- `void (No return value.)` **set_auto_indent_prefixes**(value: `Array<class_Array>`\[`String<class_String>`\])
- `Array<class_Array>`\[`String<class_String>`\] **get_auto_indent_prefixes**()

Prefixes to trigger an automatic indent. Used when `indent_automatic<class_CodeEdit_property_indent_automatic>` is set to `true`.

classref-item-separator

classref-property

`int<class_int>` **indent_size** = `4` `🔗<class_CodeEdit_property_indent_size>`

classref-property-setget

- `void (No return value.)` **set_indent_size**(value: `int<class_int>`)
- `int<class_int>` **get_indent_size**()

Size of the tabulation indent (one `Tab` press) in characters. If `indent_use_spaces<class_CodeEdit_property_indent_use_spaces>` is enabled the number of spaces to use.

classref-item-separator

classref-property

`bool<class_bool>` **indent_use_spaces** = `false` `🔗<class_CodeEdit_property_indent_use_spaces>`

classref-property-setget

- `void (No return value.)` **set_indent_using_spaces**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_indent_using_spaces**()

Use spaces instead of tabs for indentation.

classref-item-separator

classref-property

`bool<class_bool>` **line_folding** = `false` `🔗<class_CodeEdit_property_line_folding>`

classref-property-setget

- `void (No return value.)` **set_line_folding_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_line_folding_enabled**()

If `true`, lines can be folded. Otherwise, line folding methods like `fold_line()<class_CodeEdit_method_fold_line>` will not work and `can_fold_line()<class_CodeEdit_method_can_fold_line>` will always return `false`. See `gutters_draw_fold_gutter<class_CodeEdit_property_gutters_draw_fold_gutter>`.

classref-item-separator

classref-property

`Array<class_Array>`\[`int<class_int>`\] **line_length_guidelines** = `[]` `🔗<class_CodeEdit_property_line_length_guidelines>`

classref-property-setget

- `void (No return value.)` **set_line_length_guidelines**(value: `Array<class_Array>`\[`int<class_int>`\])
- `Array<class_Array>`\[`int<class_int>`\] **get_line_length_guidelines**()

Draws vertical lines at the provided columns. The first entry is considered a main hard guideline and is drawn more prominently.

classref-item-separator

classref-property

`bool<class_bool>` **symbol_lookup_on_click** = `false` `🔗<class_CodeEdit_property_symbol_lookup_on_click>`

classref-property-setget

- `void (No return value.)` **set_symbol_lookup_on_click_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_symbol_lookup_on_click_enabled**()

Set when a validated word from `symbol_validate<class_CodeEdit_signal_symbol_validate>` is clicked, the `symbol_lookup<class_CodeEdit_signal_symbol_lookup>` should be emitted.

classref-item-separator

classref-property

`bool<class_bool>` **symbol_tooltip_on_hover** = `false` `🔗<class_CodeEdit_property_symbol_tooltip_on_hover>`

classref-property-setget

- `void (No return value.)` **set_symbol_tooltip_on_hover_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_symbol_tooltip_on_hover_enabled**()

If `true`, the `symbol_hovered<class_CodeEdit_signal_symbol_hovered>` signal is emitted when hovering over a word.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_confirm_code_completion**(replace: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CodeEdit_private_method__confirm_code_completion>`

Override this method to define how the selected entry should be inserted. If `replace` is `true`, any existing text should be replaced.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_filter_code_completion_candidates**(candidates: `Array<class_Array>`\[`Dictionary<class_Dictionary>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_private_method__filter_code_completion_candidates>`

Override this method to define what items in `candidates` should be displayed.

Both `candidates` and the return is an `Array<class_Array>` of `Dictionary<class_Dictionary>`, see `get_code_completion_option()<class_CodeEdit_method_get_code_completion_option>` for `Dictionary<class_Dictionary>` content.

classref-item-separator

classref-method

`void (No return value.)` **\_request_code_completion**(force: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CodeEdit_private_method__request_code_completion>`

Override this method to define what happens when the user requests code completion. If `force` is `true`, any checks should be bypassed.

classref-item-separator

classref-method

`void (No return value.)` **add_auto_brace_completion_pair**(start_key: `String<class_String>`, end_key: `String<class_String>`) `🔗<class_CodeEdit_method_add_auto_brace_completion_pair>`

Adds a brace pair.

Both the start and end keys must be symbols. Only the start key has to be unique.

classref-item-separator

classref-method

`void (No return value.)` **add_code_completion_option**(type: `CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`, display_text: `String<class_String>`, insert_text: `String<class_String>`, text_color: `Color<class_Color>` = Color(1, 1, 1, 1), icon: `Resource<class_Resource>` = null, value: `Variant<class_Variant>` = null, location: `int<class_int>` = 1024) `🔗<class_CodeEdit_method_add_code_completion_option>`

Submits an item to the queue of potential candidates for the autocomplete menu. Call `update_code_completion_options()<class_CodeEdit_method_update_code_completion_options>` to update the list.

`location` indicates location of the option relative to the location of the code completion query. See `CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>` for how to set this value.

**Note:** This list will replace all current candidates.

classref-item-separator

classref-method

`void (No return value.)` **add_comment_delimiter**(start_key: `String<class_String>`, end_key: `String<class_String>`, line_only: `bool<class_bool>` = false) `🔗<class_CodeEdit_method_add_comment_delimiter>`

Adds a comment delimiter from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty `String<class_String>`, the region does not carry over to the next line.

classref-item-separator

classref-method

`void (No return value.)` **add_string_delimiter**(start_key: `String<class_String>`, end_key: `String<class_String>`, line_only: `bool<class_bool>` = false) `🔗<class_CodeEdit_method_add_string_delimiter>`

Defines a string delimiter from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty `String<class_String>`, the region does not carry over to the next line.

classref-item-separator

classref-method

`bool<class_bool>` **can_fold_line**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_can_fold_line>`

Returns `true` if the given line is foldable. A line is foldable if it is the start of a valid code region (see `get_code_region_start_tag()<class_CodeEdit_method_get_code_region_start_tag>`), if it is the start of a comment or string block, or if the next non-empty line is more indented (see `TextEdit.get_indent_level()<class_TextEdit_method_get_indent_level>`).

classref-item-separator

classref-method

`void (No return value.)` **cancel_code_completion**() `🔗<class_CodeEdit_method_cancel_code_completion>`

Cancels the autocomplete menu.

classref-item-separator

classref-method

`void (No return value.)` **clear_bookmarked_lines**() `🔗<class_CodeEdit_method_clear_bookmarked_lines>`

Clears all bookmarked lines.

classref-item-separator

classref-method

`void (No return value.)` **clear_breakpointed_lines**() `🔗<class_CodeEdit_method_clear_breakpointed_lines>`

Clears all breakpointed lines.

classref-item-separator

classref-method

`void (No return value.)` **clear_comment_delimiters**() `🔗<class_CodeEdit_method_clear_comment_delimiters>`

Removes all comment delimiters.

classref-item-separator

classref-method

`void (No return value.)` **clear_executing_lines**() `🔗<class_CodeEdit_method_clear_executing_lines>`

Clears all executed lines.

classref-item-separator

classref-method

`void (No return value.)` **clear_string_delimiters**() `🔗<class_CodeEdit_method_clear_string_delimiters>`

Removes all string delimiters.

classref-item-separator

classref-method

`void (No return value.)` **confirm_code_completion**(replace: `bool<class_bool>` = false) `🔗<class_CodeEdit_method_confirm_code_completion>`

Inserts the selected entry into the text. If `replace` is `true`, any existing text is replaced rather than merged.

classref-item-separator

classref-method

`void (No return value.)` **convert_indent**(from_line: `int<class_int>` = -1, to_line: `int<class_int>` = -1) `🔗<class_CodeEdit_method_convert_indent>`

Converts the indents of lines between `from_line` and `to_line` to tabs or spaces as set by `indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`.

Values of `-1` convert the entire text.

classref-item-separator

classref-method

`void (No return value.)` **create_code_region**() `🔗<class_CodeEdit_method_create_code_region>`

Creates a new code region with the selection. At least one single line comment delimiter have to be defined (see `add_comment_delimiter()<class_CodeEdit_method_add_comment_delimiter>`).

A code region is a part of code that is highlighted when folded and can help organize your script.

Code region start and end tags can be customized (see `set_code_region_tags()<class_CodeEdit_method_set_code_region_tags>`).

Code regions are delimited using start and end tags (respectively `region` and `endregion` by default) preceded by one line comment delimiter. (eg. `#region` and `#endregion`)

classref-item-separator

classref-method

`void (No return value.)` **delete_lines**() `🔗<class_CodeEdit_method_delete_lines>`

Deletes all lines that are selected or have a caret on them.

classref-item-separator

classref-method

`void (No return value.)` **do_indent**() `🔗<class_CodeEdit_method_do_indent>`

If there is no selection, indentation is inserted at the caret. Otherwise, the selected lines are indented like `indent_lines()<class_CodeEdit_method_indent_lines>`. Equivalent to the `ProjectSettings.input/ui_text_indent<class_ProjectSettings_property_input/ui_text_indent>` action. The indentation characters used depend on `indent_use_spaces<class_CodeEdit_property_indent_use_spaces>` and `indent_size<class_CodeEdit_property_indent_size>`.

classref-item-separator

classref-method

`void (No return value.)` **duplicate_lines**() `🔗<class_CodeEdit_method_duplicate_lines>`

Duplicates all lines currently selected with any caret. Duplicates the entire line beneath the current one no matter where the caret is within the line.

classref-item-separator

classref-method

`void (No return value.)` **duplicate_selection**() `🔗<class_CodeEdit_method_duplicate_selection>`

Duplicates all selected text and duplicates all lines with a caret on them.

classref-item-separator

classref-method

`void (No return value.)` **fold_all_lines**() `🔗<class_CodeEdit_method_fold_all_lines>`

Folds all lines that are possible to be folded (see `can_fold_line()<class_CodeEdit_method_can_fold_line>`).

classref-item-separator

classref-method

`void (No return value.)` **fold_line**(line: `int<class_int>`) `🔗<class_CodeEdit_method_fold_line>`

Folds the given line, if possible (see `can_fold_line()<class_CodeEdit_method_can_fold_line>`).

classref-item-separator

classref-method

`String<class_String>` **get_auto_brace_completion_close_key**(open_key: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_auto_brace_completion_close_key>`

Gets the matching auto brace close key for `open_key`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_bookmarked_lines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_bookmarked_lines>`

Gets all bookmarked lines.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_breakpointed_lines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_breakpointed_lines>`

Gets all breakpointed lines.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_code_completion_option**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_code_completion_option>`

Gets the completion option at `index`. The return `Dictionary<class_Dictionary>` has the following key-values:

`kind`: `CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`

`display_text`: Text that is shown on the autocomplete menu.

`insert_text`: Text that is to be inserted when this item is selected.

`font_color`: Color of the text on the autocomplete menu.

`icon`: Icon to draw on the autocomplete menu.

`default_value`: Value of the symbol.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_code_completion_options**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_code_completion_options>`

Gets all completion options, see `get_code_completion_option()<class_CodeEdit_method_get_code_completion_option>` for return content.

classref-item-separator

classref-method

`int<class_int>` **get_code_completion_selected_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_code_completion_selected_index>`

Gets the index of the current selected completion option.

classref-item-separator

classref-method

`String<class_String>` **get_code_region_end_tag**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_code_region_end_tag>`

Returns the code region end tag (without comment delimiter).

classref-item-separator

classref-method

`String<class_String>` **get_code_region_start_tag**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_code_region_start_tag>`

Returns the code region start tag (without comment delimiter).

classref-item-separator

classref-method

`String<class_String>` **get_delimiter_end_key**(delimiter_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_delimiter_end_key>`

Gets the end key for a string or comment region index.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_delimiter_end_position**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_delimiter_end_position>`

If `line` `column` is in a string or comment, returns the end position of the region. If not or no end could be found, both `Vector2<class_Vector2>` values will be `-1`.

classref-item-separator

classref-method

`String<class_String>` **get_delimiter_start_key**(delimiter_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_delimiter_start_key>`

Gets the start key for a string or comment region index.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_delimiter_start_position**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_delimiter_start_position>`

If `line` `column` is in a string or comment, returns the start position of the region. If not or no start could be found, both `Vector2<class_Vector2>` values will be `-1`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_executing_lines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_executing_lines>`

Gets all executing lines.

classref-item-separator

classref-method

`Array<class_Array>`\[`int<class_int>`\] **get_folded_lines**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_folded_lines>`

Returns all lines that are currently folded.

classref-item-separator

classref-method

`String<class_String>` **get_text_for_code_completion**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_text_for_code_completion>`

Returns the full text with char `0xFFFF` at the caret location.

classref-item-separator

classref-method

`String<class_String>` **get_text_for_symbol_lookup**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_text_for_symbol_lookup>`

Returns the full text with char `0xFFFF` at the cursor location.

classref-item-separator

classref-method

`String<class_String>` **get_text_with_cursor_char**(line: `int<class_int>`, column: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_get_text_with_cursor_char>`

Returns the full text with char `0xFFFF` at the specified location.

classref-item-separator

classref-method

`bool<class_bool>` **has_auto_brace_completion_close_key**(close_key: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_has_auto_brace_completion_close_key>`

Returns `true` if close key `close_key` exists.

classref-item-separator

classref-method

`bool<class_bool>` **has_auto_brace_completion_open_key**(open_key: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_has_auto_brace_completion_open_key>`

Returns `true` if open key `open_key` exists.

classref-item-separator

classref-method

`bool<class_bool>` **has_comment_delimiter**(start_key: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_has_comment_delimiter>`

Returns `true` if comment `start_key` exists.

classref-item-separator

classref-method

`bool<class_bool>` **has_string_delimiter**(start_key: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_has_string_delimiter>`

Returns `true` if string `start_key` exists.

classref-item-separator

classref-method

`void (No return value.)` **indent_lines**() `🔗<class_CodeEdit_method_indent_lines>`

Indents all lines that are selected or have a caret on them. Uses spaces or a tab depending on `indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`. See `unindent_lines()<class_CodeEdit_method_unindent_lines>`.

classref-item-separator

classref-method

`int<class_int>` **is_in_comment**(line: `int<class_int>`, column: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_in_comment>`

Returns delimiter index if `line` `column` is in a comment. If `column` is not provided, will return delimiter index if the entire `line` is a comment. Otherwise `-1`.

classref-item-separator

classref-method

`int<class_int>` **is_in_string**(line: `int<class_int>`, column: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_in_string>`

Returns the delimiter index if `line` `column` is in a string. If `column` is not provided, will return the delimiter index if the entire `line` is a string. Otherwise `-1`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_bookmarked**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_line_bookmarked>`

Returns `true` if the given line is bookmarked. See `set_line_as_bookmarked()<class_CodeEdit_method_set_line_as_bookmarked>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_breakpointed**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_line_breakpointed>`

Returns `true` if the given line is breakpointed. See `set_line_as_breakpoint()<class_CodeEdit_method_set_line_as_breakpoint>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_code_region_end**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_line_code_region_end>`

Returns `true` if the given line is a code region end. See `set_code_region_tags()<class_CodeEdit_method_set_code_region_tags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_code_region_start**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_line_code_region_start>`

Returns `true` if the given line is a code region start. See `set_code_region_tags()<class_CodeEdit_method_set_code_region_tags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_executing**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_line_executing>`

Returns `true` if the given line is marked as executing. See `set_line_as_executing()<class_CodeEdit_method_set_line_as_executing>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_line_folded**(line: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeEdit_method_is_line_folded>`

Returns `true` if the given line is folded. See `fold_line()<class_CodeEdit_method_fold_line>`.

classref-item-separator

classref-method

`void (No return value.)` **join_lines**(line_ending: `String<class_String>` = " ") `🔗<class_CodeEdit_method_join_lines>`

Joins all selected lines or lines containing a caret with their next line. Whitespace in between will be removed. If the next line has content, the `line_ending` will be inserted in between.

classref-item-separator

classref-method

`void (No return value.)` **move_lines_down**() `🔗<class_CodeEdit_method_move_lines_down>`

Moves all lines down that are selected or have a caret on them.

classref-item-separator

classref-method

`void (No return value.)` **move_lines_up**() `🔗<class_CodeEdit_method_move_lines_up>`

Moves all lines up that are selected or have a caret on them.

classref-item-separator

classref-method

`void (No return value.)` **remove_comment_delimiter**(start_key: `String<class_String>`) `🔗<class_CodeEdit_method_remove_comment_delimiter>`

Removes the comment delimiter with `start_key`.

classref-item-separator

classref-method

`void (No return value.)` **remove_string_delimiter**(start_key: `String<class_String>`) `🔗<class_CodeEdit_method_remove_string_delimiter>`

Removes the string delimiter with `start_key`.

classref-item-separator

classref-method

`void (No return value.)` **request_code_completion**(force: `bool<class_bool>` = false) `🔗<class_CodeEdit_method_request_code_completion>`

Emits `code_completion_requested<class_CodeEdit_signal_code_completion_requested>`, if `force` is `true` will bypass all checks. Otherwise will check that the caret is in a word or in front of a prefix. Will ignore the request if all current options are of type file path, node path, or signal.

classref-item-separator

classref-method

`void (No return value.)` **set_code_completion_selected_index**(index: `int<class_int>`) `🔗<class_CodeEdit_method_set_code_completion_selected_index>`

Sets the current selected completion option.

classref-item-separator

classref-method

`void (No return value.)` **set_code_hint**(code_hint: `String<class_String>`) `🔗<class_CodeEdit_method_set_code_hint>`

Sets the code hint text. Pass an empty string to clear.

classref-item-separator

classref-method

`void (No return value.)` **set_code_hint_draw_below**(draw_below: `bool<class_bool>`) `🔗<class_CodeEdit_method_set_code_hint_draw_below>`

If `true`, the code hint will draw below the main caret. If `false`, the code hint will draw above the main caret. See `set_code_hint()<class_CodeEdit_method_set_code_hint>`.

classref-item-separator

classref-method

`void (No return value.)` **set_code_region_tags**(start: `String<class_String>` = "region", end: `String<class_String>` = "endregion") `🔗<class_CodeEdit_method_set_code_region_tags>`

Sets the code region start and end tags (without comment delimiter).

classref-item-separator

classref-method

`void (No return value.)` **set_line_as_bookmarked**(line: `int<class_int>`, bookmarked: `bool<class_bool>`) `🔗<class_CodeEdit_method_set_line_as_bookmarked>`

Sets the given line as bookmarked. If `true` and `gutters_draw_bookmarks<class_CodeEdit_property_gutters_draw_bookmarks>` is `true`, draws the `bookmark<class_CodeEdit_theme_icon_bookmark>` icon in the gutter for this line. See `get_bookmarked_lines()<class_CodeEdit_method_get_bookmarked_lines>` and `is_line_bookmarked()<class_CodeEdit_method_is_line_bookmarked>`.

classref-item-separator

classref-method

`void (No return value.)` **set_line_as_breakpoint**(line: `int<class_int>`, breakpointed: `bool<class_bool>`) `🔗<class_CodeEdit_method_set_line_as_breakpoint>`

Sets the given line as a breakpoint. If `true` and `gutters_draw_breakpoints_gutter<class_CodeEdit_property_gutters_draw_breakpoints_gutter>` is `true`, draws the `breakpoint<class_CodeEdit_theme_icon_breakpoint>` icon in the gutter for this line. See `get_breakpointed_lines()<class_CodeEdit_method_get_breakpointed_lines>` and `is_line_breakpointed()<class_CodeEdit_method_is_line_breakpointed>`.

classref-item-separator

classref-method

`void (No return value.)` **set_line_as_executing**(line: `int<class_int>`, executing: `bool<class_bool>`) `🔗<class_CodeEdit_method_set_line_as_executing>`

Sets the given line as executing. If `true` and `gutters_draw_executing_lines<class_CodeEdit_property_gutters_draw_executing_lines>` is `true`, draws the `executing_line<class_CodeEdit_theme_icon_executing_line>` icon in the gutter for this line. See `get_executing_lines()<class_CodeEdit_method_get_executing_lines>` and `is_line_executing()<class_CodeEdit_method_is_line_executing>`.

classref-item-separator

classref-method

`void (No return value.)` **set_symbol_lookup_word_as_valid**(valid: `bool<class_bool>`) `🔗<class_CodeEdit_method_set_symbol_lookup_word_as_valid>`

Sets the symbol emitted by `symbol_validate<class_CodeEdit_signal_symbol_validate>` as a valid lookup.

classref-item-separator

classref-method

`void (No return value.)` **toggle_foldable_line**(line: `int<class_int>`) `🔗<class_CodeEdit_method_toggle_foldable_line>`

Toggle the folding of the code block at the given line.

classref-item-separator

classref-method

`void (No return value.)` **toggle_foldable_lines_at_carets**() `🔗<class_CodeEdit_method_toggle_foldable_lines_at_carets>`

Toggle the folding of the code block on all lines with a caret on them.

classref-item-separator

classref-method

`void (No return value.)` **unfold_all_lines**() `🔗<class_CodeEdit_method_unfold_all_lines>`

Unfolds all lines that are folded.

classref-item-separator

classref-method

`void (No return value.)` **unfold_line**(line: `int<class_int>`) `🔗<class_CodeEdit_method_unfold_line>`

Unfolds the given line if it is folded or if it is hidden under a folded line.

classref-item-separator

classref-method

`void (No return value.)` **unindent_lines**() `🔗<class_CodeEdit_method_unindent_lines>`

Unindents all lines that are selected or have a caret on them. Uses spaces or a tab depending on `indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`. Equivalent to the `ProjectSettings.input/ui_text_dedent<class_ProjectSettings_property_input/ui_text_dedent>` action. See `indent_lines()<class_CodeEdit_method_indent_lines>`.

classref-item-separator

classref-method

`void (No return value.)` **update_code_completion_options**(force: `bool<class_bool>`) `🔗<class_CodeEdit_method_update_code_completion_options>`

Submits all completion options added with `add_code_completion_option()<class_CodeEdit_method_add_code_completion_option>`. Will try to force the autocomplete menu to popup, if `force` is `true`.

**Note:** This will replace all current candidates.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **bookmark_color** = `Color(0.5, 0.64, 1, 0.8)` `🔗<class_CodeEdit_theme_color_bookmark_color>`

`Color<class_Color>` of the bookmark icon for bookmarked lines.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **brace_mismatch_color** = `Color(1, 0.2, 0.2, 1)` `🔗<class_CodeEdit_theme_color_brace_mismatch_color>`

`Color<class_Color>` of the text to highlight mismatched braces.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **breakpoint_color** = `Color(0.9, 0.29, 0.3, 1)` `🔗<class_CodeEdit_theme_color_breakpoint_color>`

`Color<class_Color>` of the breakpoint icon for bookmarked lines.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **code_folding_color** = `Color(0.8, 0.8, 0.8, 0.8)` `🔗<class_CodeEdit_theme_color_code_folding_color>`

`Color<class_Color>` for all icons related to line folding.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **completion_background_color** = `Color(0.17, 0.16, 0.2, 1)` `🔗<class_CodeEdit_theme_color_completion_background_color>`

Sets the background `Color<class_Color>` for the code completion popup.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **completion_existing_color** = `Color(0.87, 0.87, 0.87, 0.13)` `🔗<class_CodeEdit_theme_color_completion_existing_color>`

Background highlight `Color<class_Color>` for matching text in code completion options.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **completion_scroll_color** = `Color(1, 1, 1, 0.29)` `🔗<class_CodeEdit_theme_color_completion_scroll_color>`

`Color<class_Color>` of the scrollbar in the code completion popup.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **completion_scroll_hovered_color** = `Color(1, 1, 1, 0.4)` `🔗<class_CodeEdit_theme_color_completion_scroll_hovered_color>`

`Color<class_Color>` of the scrollbar in the code completion popup when hovered.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **completion_selected_color** = `Color(0.26, 0.26, 0.27, 1)` `🔗<class_CodeEdit_theme_color_completion_selected_color>`

Background highlight `Color<class_Color>` for the current selected option item in the code completion popup.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **executing_line_color** = `Color(0.98, 0.89, 0.27, 1)` `🔗<class_CodeEdit_theme_color_executing_line_color>`

`Color<class_Color>` of the executing icon for executing lines.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **folded_code_region_color** = `Color(0.68, 0.46, 0.77, 0.2)` `🔗<class_CodeEdit_theme_color_folded_code_region_color>`

`Color<class_Color>` of background line highlight for folded code region.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **line_length_guideline_color** = `Color(0.3, 0.5, 0.8, 0.1)` `🔗<class_CodeEdit_theme_color_line_length_guideline_color>`

`Color<class_Color>` of the main line length guideline, secondary guidelines will have 50% alpha applied.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **line_number_color** = `Color(0.67, 0.67, 0.67, 0.4)` `🔗<class_CodeEdit_theme_color_line_number_color>`

Sets the `Color<class_Color>` of line numbers.

classref-item-separator

classref-themeproperty

`int<class_int>` **completion_lines** = `7` `🔗<class_CodeEdit_theme_constant_completion_lines>`

Max number of options to display in the code completion popup at any one time.

classref-item-separator

classref-themeproperty

`int<class_int>` **completion_max_width** = `50` `🔗<class_CodeEdit_theme_constant_completion_max_width>`

Max width of options in the code completion popup. Options longer than this will be cut off.

classref-item-separator

classref-themeproperty

`int<class_int>` **completion_scroll_width** = `6` `🔗<class_CodeEdit_theme_constant_completion_scroll_width>`

Width of the scrollbar in the code completion popup.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **bookmark** `🔗<class_CodeEdit_theme_icon_bookmark>`

Sets a custom `Texture2D<class_Texture2D>` to draw in the bookmark gutter for bookmarked lines.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **breakpoint** `🔗<class_CodeEdit_theme_icon_breakpoint>`

Sets a custom `Texture2D<class_Texture2D>` to draw in the breakpoint gutter for breakpointed lines.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **can_fold** `🔗<class_CodeEdit_theme_icon_can_fold>`

Sets a custom `Texture2D<class_Texture2D>` to draw in the line folding gutter when a line can be folded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **can_fold_code_region** `🔗<class_CodeEdit_theme_icon_can_fold_code_region>`

Sets a custom `Texture2D<class_Texture2D>` to draw in the line folding gutter when a code region can be folded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **completion_color_bg** `🔗<class_CodeEdit_theme_icon_completion_color_bg>`

Background panel for the color preview box in autocompletion (visible when the color is translucent).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **executing_line** `🔗<class_CodeEdit_theme_icon_executing_line>`

Icon to draw in the executing gutter for executing lines.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **folded** `🔗<class_CodeEdit_theme_icon_folded>`

Sets a custom `Texture2D<class_Texture2D>` to draw in the line folding gutter when a line is folded and can be unfolded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **folded_code_region** `🔗<class_CodeEdit_theme_icon_folded_code_region>`

Sets a custom `Texture2D<class_Texture2D>` to draw in the line folding gutter when a code region is folded and can be unfolded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **folded_eol_icon** `🔗<class_CodeEdit_theme_icon_folded_eol_icon>`

Sets a custom `Texture2D<class_Texture2D>` to draw at the end of a folded line.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **completion** `🔗<class_CodeEdit_theme_style_completion>`

`StyleBox<class_StyleBox>` for the code completion popup.