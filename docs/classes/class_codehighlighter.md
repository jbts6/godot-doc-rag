github_url
hide

# CodeHighlighter

**Inherits:** `SyntaxHighlighter<class_SyntaxHighlighter>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A syntax highlighter intended for code.

classref-introduction-group

## Description

By adjusting various properties of this resource, you can change the colors of strings, comments, numbers, and other text patterns inside a `TextEdit<class_TextEdit>` control.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Dictionary<class_Dictionary>` **color_regions** = `{}` `🔗<class_CodeHighlighter_property_color_regions>`

classref-property-setget

- `void (No return value.)` **set_color_regions**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_color_regions**()

Sets the color regions. All existing regions will be removed. The `Dictionary<class_Dictionary>` key is the region start and end key, separated by a space. The value is the region color.

classref-item-separator

classref-property

`Color<class_Color>` **function_color** = `Color(0, 0, 0, 1)` `🔗<class_CodeHighlighter_property_function_color>`

classref-property-setget

- `void (No return value.)` **set_function_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_function_color**()

Sets color for functions. A function is a non-keyword string followed by a '('.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **keyword_colors** = `{}` `🔗<class_CodeHighlighter_property_keyword_colors>`

classref-property-setget

- `void (No return value.)` **set_keyword_colors**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_keyword_colors**()

Sets the keyword colors. All existing keywords will be removed. The `Dictionary<class_Dictionary>` key is the keyword. The value is the keyword color.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **member_keyword_colors** = `{}` `🔗<class_CodeHighlighter_property_member_keyword_colors>`

classref-property-setget

- `void (No return value.)` **set_member_keyword_colors**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_member_keyword_colors**()

Sets the member keyword colors. All existing member keyword will be removed. The `Dictionary<class_Dictionary>` key is the member keyword. The value is the member keyword color.

classref-item-separator

classref-property

`Color<class_Color>` **member_variable_color** = `Color(0, 0, 0, 1)` `🔗<class_CodeHighlighter_property_member_variable_color>`

classref-property-setget

- `void (No return value.)` **set_member_variable_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_member_variable_color**()

Sets color for member variables. A member variable is non-keyword, non-function string proceeded with a '.'.

classref-item-separator

classref-property

`Color<class_Color>` **number_color** = `Color(0, 0, 0, 1)` `🔗<class_CodeHighlighter_property_number_color>`

classref-property-setget

- `void (No return value.)` **set_number_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_number_color**()

Sets the color for numbers.

classref-item-separator

classref-property

`Color<class_Color>` **symbol_color** = `Color(0, 0, 0, 1)` `🔗<class_CodeHighlighter_property_symbol_color>`

classref-property-setget

- `void (No return value.)` **set_symbol_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_symbol_color**()

Sets the color for symbols.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_color_region**(start_key: `String<class_String>`, end_key: `String<class_String>`, color: `Color<class_Color>`, line_only: `bool<class_bool>` = false) `🔗<class_CodeHighlighter_method_add_color_region>`

Adds a color region (such as for comments or strings) from `start_key` to `end_key`. Both keys should be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty `String<class_String>`, the region does not carry over to the next line.

classref-item-separator

classref-method

`void (No return value.)` **add_keyword_color**(keyword: `String<class_String>`, color: `Color<class_Color>`) `🔗<class_CodeHighlighter_method_add_keyword_color>`

Sets the color for a keyword.

The keyword cannot contain any symbols except '\_'.

classref-item-separator

classref-method

`void (No return value.)` **add_member_keyword_color**(member_keyword: `String<class_String>`, color: `Color<class_Color>`) `🔗<class_CodeHighlighter_method_add_member_keyword_color>`

Sets the color for a member keyword.

The member keyword cannot contain any symbols except '\_'.

It will not be highlighted if preceded by a '.'.

classref-item-separator

classref-method

`void (No return value.)` **clear_color_regions**() `🔗<class_CodeHighlighter_method_clear_color_regions>`

Removes all color regions.

classref-item-separator

classref-method

`void (No return value.)` **clear_keyword_colors**() `🔗<class_CodeHighlighter_method_clear_keyword_colors>`

Removes all keywords.

classref-item-separator

classref-method

`void (No return value.)` **clear_member_keyword_colors**() `🔗<class_CodeHighlighter_method_clear_member_keyword_colors>`

Removes all member keywords.

classref-item-separator

classref-method

`Color<class_Color>` **get_keyword_color**(keyword: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeHighlighter_method_get_keyword_color>`

Returns the color for a keyword.

classref-item-separator

classref-method

`Color<class_Color>` **get_member_keyword_color**(member_keyword: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeHighlighter_method_get_member_keyword_color>`

Returns the color for a member keyword.

classref-item-separator

classref-method

`bool<class_bool>` **has_color_region**(start_key: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeHighlighter_method_has_color_region>`

Returns `true` if the start key exists, else `false`.

classref-item-separator

classref-method

`bool<class_bool>` **has_keyword_color**(keyword: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeHighlighter_method_has_keyword_color>`

Returns `true` if the keyword exists, else `false`.

classref-item-separator

classref-method

`bool<class_bool>` **has_member_keyword_color**(member_keyword: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CodeHighlighter_method_has_member_keyword_color>`

Returns `true` if the member keyword exists, else `false`.

classref-item-separator

classref-method

`void (No return value.)` **remove_color_region**(start_key: `String<class_String>`) `🔗<class_CodeHighlighter_method_remove_color_region>`

Removes the color region that uses that start key.

classref-item-separator

classref-method

`void (No return value.)` **remove_keyword_color**(keyword: `String<class_String>`) `🔗<class_CodeHighlighter_method_remove_keyword_color>`

Removes the keyword.

classref-item-separator

classref-method

`void (No return value.)` **remove_member_keyword_color**(member_keyword: `String<class_String>`) `🔗<class_CodeHighlighter_method_remove_member_keyword_color>`

Removes the member keyword.