github_url
hide

# VisualShaderNodeCompare

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A comparison function for common types within the visual shader graph.

classref-introduction-group

## Description

Compares `a` and `b` of `type<class_VisualShaderNodeCompare_property_type>` by `function<class_VisualShaderNodeCompare_property_function>`. Returns a boolean scalar. Translates to `if` instruction in shader code.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ComparisonType**: `🔗<enum_VisualShaderNodeCompare_ComparisonType>`

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_SCALAR** = `0`

A floating-point scalar.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_SCALAR_INT** = `1`

An integer scalar.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_SCALAR_UINT** = `2`

An unsigned integer scalar.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_VECTOR_2D** = `3`

A 2D vector type.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_VECTOR_3D** = `4`

A 3D vector type.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_VECTOR_4D** = `5`

A 4D vector type.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_BOOLEAN** = `6`

A boolean type.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_TRANSFORM** = `7`

A transform (`mat4`) type.

classref-enumeration-constant

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **CTYPE_MAX** = `8`

Represents the size of the `ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` enum.

classref-item-separator

classref-enumeration

enum **Function**: `🔗<enum_VisualShaderNodeCompare_Function>`

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_EQUAL** = `0`

Comparison for equality (`a == b`).

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_NOT_EQUAL** = `1`

Comparison for inequality (`a != b`).

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_GREATER_THAN** = `2`

Comparison for greater than (`a > b`). Cannot be used if `type<class_VisualShaderNodeCompare_property_type>` set to `CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>` or `CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`.

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_GREATER_THAN_EQUAL** = `3`

Comparison for greater than or equal (`a >= b`). Cannot be used if `type<class_VisualShaderNodeCompare_property_type>` set to `CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>` or `CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`.

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_LESS_THAN** = `4`

Comparison for less than (`a < b`). Cannot be used if `type<class_VisualShaderNodeCompare_property_type>` set to `CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>` or `CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`.

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_LESS_THAN_EQUAL** = `5`

Comparison for less than or equal (`a <= b`). Cannot be used if `type<class_VisualShaderNodeCompare_property_type>` set to `CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>` or `CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`.

classref-enumeration-constant

`Function<enum_VisualShaderNodeCompare_Function>` **FUNC_MAX** = `6`

Represents the size of the `Function<enum_VisualShaderNodeCompare_Function>` enum.

classref-item-separator

classref-enumeration

enum **Condition**: `🔗<enum_VisualShaderNodeCompare_Condition>`

classref-enumeration-constant

`Condition<enum_VisualShaderNodeCompare_Condition>` **COND_ALL** = `0`

The result will be `true` if all components in the vector satisfy the comparison condition.

classref-enumeration-constant

`Condition<enum_VisualShaderNodeCompare_Condition>` **COND_ANY** = `1`

The result will be `true` if any component in the vector satisfies the comparison condition.

classref-enumeration-constant

`Condition<enum_VisualShaderNodeCompare_Condition>` **COND_MAX** = `2`

Represents the size of the `Condition<enum_VisualShaderNodeCompare_Condition>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Condition<enum_VisualShaderNodeCompare_Condition>` **condition** = `0` `🔗<class_VisualShaderNodeCompare_property_condition>`

classref-property-setget

- `void (No return value.)` **set_condition**(value: `Condition<enum_VisualShaderNodeCompare_Condition>`)
- `Condition<enum_VisualShaderNodeCompare_Condition>` **get_condition**()

Extra condition which is applied if `type<class_VisualShaderNodeCompare_property_type>` is set to `CTYPE_VECTOR_3D<class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_3D>`.

classref-item-separator

classref-property

`Function<enum_VisualShaderNodeCompare_Function>` **function** = `0` `🔗<class_VisualShaderNodeCompare_property_function>`

classref-property-setget

- `void (No return value.)` **set_function**(value: `Function<enum_VisualShaderNodeCompare_Function>`)
- `Function<enum_VisualShaderNodeCompare_Function>` **get_function**()

A comparison function.

classref-item-separator

classref-property

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **type** = `0` `🔗<class_VisualShaderNodeCompare_property_type>`

classref-property-setget

- `void (No return value.)` **set_comparison_type**(value: `ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`)
- `ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>` **get_comparison_type**()

The type to be used in the comparison.