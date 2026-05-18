github_url
hide

# VisualShaderNodeIntFunc

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A scalar integer function to be used within the visual shader graph.

classref-introduction-group

## Description

Accept an integer scalar (`x`) to the input port and transform it according to `function<class_VisualShaderNodeIntFunc_property_function>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Function**: `🔗<enum_VisualShaderNodeIntFunc_Function>`

classref-enumeration-constant

`Function<enum_VisualShaderNodeIntFunc_Function>` **FUNC_ABS** = `0`

Returns the absolute value of the parameter. Translates to `abs(x)` in the Godot Shader Language.

classref-enumeration-constant

`Function<enum_VisualShaderNodeIntFunc_Function>` **FUNC_NEGATE** = `1`

Negates the `x` using `-(x)`.

classref-enumeration-constant

`Function<enum_VisualShaderNodeIntFunc_Function>` **FUNC_SIGN** = `2`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot Shader Language.

classref-enumeration-constant

`Function<enum_VisualShaderNodeIntFunc_Function>` **FUNC_BITWISE_NOT** = `3`

Returns the result of bitwise `NOT` operation on the integer. Translates to `~a` in the Godot Shader Language.

classref-enumeration-constant

`Function<enum_VisualShaderNodeIntFunc_Function>` **FUNC_MAX** = `4`

Represents the size of the `Function<enum_VisualShaderNodeIntFunc_Function>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Function<enum_VisualShaderNodeIntFunc_Function>` **function** = `2` `🔗<class_VisualShaderNodeIntFunc_property_function>`

classref-property-setget

- `void (No return value.)` **set_function**(value: `Function<enum_VisualShaderNodeIntFunc_Function>`)
- `Function<enum_VisualShaderNodeIntFunc_Function>` **get_function**()

A function to be applied to the scalar.