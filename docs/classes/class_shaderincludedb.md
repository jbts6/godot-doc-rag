github_url
hide

# ShaderIncludeDB

**Inherits:** `Object<class_Object>`

Internal database of built in shader include files.

classref-introduction-group

## Description

This object contains shader fragments from Godot's internal shaders. These can be used when access to internal uniform buffers and/or internal functions is required for instance when composing compositor effects or compute shaders. Only fragments for the current rendering device are loaded.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_built_in_include_file**(filename: `String<class_String>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_ShaderIncludeDB_method_get_built_in_include_file>`

Returns the code for the built-in shader fragment. You can also access this in your shader code through `#include "filename"`.

classref-item-separator

classref-method

`bool<class_bool>` **has_built_in_include_file**(filename: `String<class_String>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_ShaderIncludeDB_method_has_built_in_include_file>`

Returns `true` if an include file with this name exists.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **list_built_in_include_files**() `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_ShaderIncludeDB_method_list_built_in_include_files>`

Returns a list of built-in include files that are currently registered.