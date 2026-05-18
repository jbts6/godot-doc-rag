github_url
hide

# RegExMatch

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Contains the results of a `RegEx<class_RegEx>` search.

classref-introduction-group

## Description

Contains the results of a single `RegEx<class_RegEx>` match returned by `RegEx.search()<class_RegEx_method_search>` and `RegEx.search_all()<class_RegEx_method_search_all>`. It can be used to find the position and range of the match and its capturing groups, and it can extract its substring for you.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Dictionary<class_Dictionary>` **names** = `{}` `🔗<class_RegExMatch_property_names>`

classref-property-setget

- `Dictionary<class_Dictionary>` **get_names**()

A dictionary of named groups and its corresponding group number. Only groups that were matched are included. If multiple groups have the same name, that name would refer to the first matching one.

classref-item-separator

classref-property

`PackedStringArray<class_PackedStringArray>` **strings** = `PackedStringArray()` `🔗<class_RegExMatch_property_strings>`

classref-property-setget

- `PackedStringArray<class_PackedStringArray>` **get_strings**()

An `Array<class_Array>` of the match and its capturing groups.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedStringArray<class_PackedStringArray>` for more details.

classref-item-separator

classref-property

`String<class_String>` **subject** = `""` `🔗<class_RegExMatch_property_subject>`

classref-property-setget

- `String<class_String>` **get_subject**()

The source string used with the search pattern to find this matching result.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_end**(name: `Variant<class_Variant>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RegExMatch_method_get_end>`

Returns the end position of the match within the source string. The end position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

classref-item-separator

classref-method

`int<class_int>` **get_group_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RegExMatch_method_get_group_count>`

Returns the number of capturing groups.

classref-item-separator

classref-method

`int<class_int>` **get_start**(name: `Variant<class_Variant>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RegExMatch_method_get_start>`

Returns the starting position of the match within the source string. The starting position of capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns -1 if the group did not match or doesn't exist.

classref-item-separator

classref-method

`String<class_String>` **get_string**(name: `Variant<class_Variant>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RegExMatch_method_get_string>`

Returns the substring of the match from the source string. Capturing groups can be retrieved by providing its group number as an integer or its string name (if it's a named group). The default value of 0 refers to the whole pattern.

Returns an empty string if the group did not match or doesn't exist.