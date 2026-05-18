github_url
hide

# ShaderInclude

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A snippet of shader code to be included in a `Shader<class_Shader>` with `#include`.

classref-introduction-group

## Description

A shader include file, saved with the `.gdshaderinc` extension. This class allows you to define a custom shader snippet that can be included in a `Shader<class_Shader>` by using the preprocessor directive `#include`, followed by the file path (e.g. `#include "res://shader_lib.gdshaderinc"`). The snippet doesn't have to be a valid shader on its own.

classref-introduction-group

## Tutorials

- `Shader preprocessor <../tutorials/shaders/shader_reference/shader_preprocessor>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **code** = `""` `🔗<class_ShaderInclude_property_code>`

classref-property-setget

- `void (No return value.)` **set_code**(value: `String<class_String>`)
- `String<class_String>` **get_code**()

Returns the code of the shader include file. The returned text is what the user has written, not the full generated code used internally.