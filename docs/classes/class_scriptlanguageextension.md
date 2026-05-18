github_url
hide

# ScriptLanguageExtension

**Inherits:** `ScriptLanguage<class_ScriptLanguage>` **\<** `Object<class_Object>`

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **LookupResultType**: `🔗<enum_ScriptLanguageExtension_LookupResultType>`

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_SCRIPT_LOCATION** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_CONSTANT** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_PROPERTY** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_METHOD** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_SIGNAL** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_ENUM** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_TBD_GLOBALSCOPE** = `7`

**Deprecated:** This constant may be changed or removed in future versions.

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_CLASS_ANNOTATION** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_LOCAL_CONSTANT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_LOCAL_VARIABLE** = `10`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`LookupResultType<enum_ScriptLanguageExtension_LookupResultType>` **LOOKUP_RESULT_MAX** = `11`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-enumeration

enum **CodeCompletionLocation**: `🔗<enum_ScriptLanguageExtension_CodeCompletionLocation>`

classref-enumeration-constant

`CodeCompletionLocation<enum_ScriptLanguageExtension_CodeCompletionLocation>` **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g. a local variable. Subsequent value of location represent options from the outer class, the exact value represent how far they are (in terms of inner classes).

classref-enumeration-constant

`CodeCompletionLocation<enum_ScriptLanguageExtension_CodeCompletionLocation>` **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to the location of the code completion query. Perform a bitwise OR with the class depth (e.g. `0` for the local class, `1` for the parent, `2` for the grandparent, etc.) to store the depth of an option in the class or a parent class.

classref-enumeration-constant

`CodeCompletionLocation<enum_ScriptLanguageExtension_CodeCompletionLocation>` **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived class (e.g. Autoload Singletons).

classref-enumeration-constant

`CodeCompletionLocation<enum_ScriptLanguageExtension_CodeCompletionLocation>` **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum constants - e.g. built-in classes.

classref-item-separator

classref-enumeration

enum **CodeCompletionKind**: `🔗<enum_ScriptLanguageExtension_CodeCompletionKind>`

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_CLASS** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_FUNCTION** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_SIGNAL** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_VARIABLE** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_MEMBER** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_ENUM** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_CONSTANT** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_NODE_PATH** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_FILE_PATH** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_PLAIN_TEXT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_KEYWORD** = `10`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`CodeCompletionKind<enum_ScriptLanguageExtension_CodeCompletionKind>` **CODE_COMPLETION_KIND_MAX** = `11`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_add_global_constant**(name: `StringName<class_StringName>`, value: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__add_global_constant>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_add_named_global_constant**(name: `StringName<class_StringName>`, value: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__add_named_global_constant>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_auto_indent_code**(code: `String<class_String>`, from_line: `int<class_int>`, to_line: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__auto_indent_code>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_can_inherit_from_file**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__can_inherit_from_file>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_can_make_function**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__can_make_function>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_complete_code**(code: `String<class_String>`, path: `String<class_String>`, owner: `Object<class_Object>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__complete_code>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Object<class_Object>` **\_create_script**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__create_script>`

**Deprecated:** This method is not called by the engine.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_debug_get_current_stack_info**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_current_stack_info>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_debug_get_error**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_error>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_debug_get_globals**(max_subitems: `int<class_int>`, max_depth: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_globals>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_debug_get_stack_level_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_count>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_debug_get_stack_level_function**(level: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_function>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void*` **\_debug_get_stack_level_instance**(level: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_instance>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_debug_get_stack_level_line**(level: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_line>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_debug_get_stack_level_locals**(level: `int<class_int>`, max_subitems: `int<class_int>`, max_depth: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_locals>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_debug_get_stack_level_members**(level: `int<class_int>`, max_subitems: `int<class_int>`, max_depth: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_members>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_debug_get_stack_level_source**(level: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__debug_get_stack_level_source>`

Returns the source associated with a given debug stack position.

classref-item-separator

classref-method

`String<class_String>` **\_debug_parse_stack_level_expression**(level: `int<class_int>`, expression: `String<class_String>`, max_subitems: `int<class_int>`, max_depth: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__debug_parse_stack_level_expression>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_find_function**(function: `String<class_String>`, code: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__find_function>`

Returns the line where the function is defined in the code, or `-1` if the function is not present.

classref-item-separator

classref-method

`void (No return value.)` **\_finish**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__finish>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_frame**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__frame>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_get_built_in_templates**(object: `StringName<class_StringName>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_built_in_templates>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_comment_delimiters**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_comment_delimiters>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_doc_comment_delimiters**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_doc_comment_delimiters>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_get_extension**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_extension>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_get_global_class_name**(path: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_global_class_name>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_get_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_name>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_get_public_annotations**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_public_annotations>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_get_public_constants**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_public_constants>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_get_public_functions**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_public_functions>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_recognized_extensions**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_recognized_extensions>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_reserved_words**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_reserved_words>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_string_delimiters**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_string_delimiters>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_get_type**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__get_type>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_handles_global_class_type**(type: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__handles_global_class_type>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_has_named_classes**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__has_named_classes>`

**Deprecated:** This method is not called by the engine.

classref-item-separator

classref-method

`void (No return value.)` **\_init**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__init>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_is_control_flow_keyword**(keyword: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__is_control_flow_keyword>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_is_using_templates**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__is_using_templates>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_lookup_code**(code: `String<class_String>`, symbol: `String<class_String>`, path: `String<class_String>`, owner: `Object<class_Object>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__lookup_code>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_make_function**(class_name: `String<class_String>`, function_name: `String<class_String>`, function_args: `PackedStringArray<class_PackedStringArray>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__make_function>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Script<class_Script>` **\_make_template**(template: `String<class_String>`, class_name: `String<class_String>`, base_class_name: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__make_template>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_open_in_external_editor**(script: `Script<class_Script>`, line: `int<class_int>`, column: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__open_in_external_editor>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_overrides_external_editor**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__overrides_external_editor>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`ScriptNameCasing<enum_ScriptLanguage_ScriptNameCasing>` **\_preferred_file_name_casing**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__preferred_file_name_casing>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_profiling_get_accumulated_data**(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__profiling_get_accumulated_data>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **\_profiling_get_frame_data**(info_array: `ScriptLanguageExtensionProfilingInfo*`, info_max: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__profiling_get_frame_data>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_profiling_set_save_native_calls**(enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__profiling_set_save_native_calls>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_profiling_start**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__profiling_start>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_profiling_stop**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__profiling_stop>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_reload_all_scripts**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__reload_all_scripts>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_reload_scripts**(scripts: `Array<class_Array>`, soft_reload: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__reload_scripts>`

Reloads all `scripts` from disk and the specifics of how that happens is **ScriptLanguageExtension** specific.

classref-item-separator

classref-method

`void (No return value.)` **\_reload_tool_script**(script: `Script<class_Script>`, soft_reload: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__reload_tool_script>`

Reloads the given `script` from disk and the specifics of how that happens is **ScriptLanguageExtension** specific.

classref-item-separator

classref-method

`void (No return value.)` **\_remove_named_global_constant**(name: `StringName<class_StringName>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__remove_named_global_constant>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_supports_builtin_mode**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__supports_builtin_mode>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **\_supports_documentation**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__supports_documentation>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_thread_enter**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__thread_enter>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_thread_exit**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_ScriptLanguageExtension_private_method__thread_exit>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_validate**(script: `String<class_String>`, path: `String<class_String>`, validate_functions: `bool<class_bool>`, validate_errors: `bool<class_bool>`, validate_warnings: `bool<class_bool>`, validate_safe_lines: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__validate>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`String<class_String>` **\_validate_path**(path: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptLanguageExtension_private_method__validate_path>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!