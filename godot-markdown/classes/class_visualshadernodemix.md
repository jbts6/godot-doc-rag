github_url
hide

# VisualShaderNodeMix

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Linearly interpolates between two values within the visual shader graph.

classref-introduction-group

## Description

Translates to `mix(a, b, weight)` in the shader language.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpType**: `🔗<enum_VisualShaderNodeMix_OpType>`

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_VECTOR_2D_SCALAR** = `2`

The `a` and `b` ports use a 2D vector type. The `weight` port uses a scalar type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_VECTOR_3D** = `3`

A 3D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_VECTOR_3D_SCALAR** = `4`

The `a` and `b` ports use a 3D vector type. The `weight` port uses a scalar type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_VECTOR_4D_SCALAR** = `6`

The `a` and `b` ports use a 4D vector type. The `weight` port uses a scalar type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMix_OpType>` **OP_TYPE_MAX** = `7`

Represents the size of the `OpType<enum_VisualShaderNodeMix_OpType>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpType<enum_VisualShaderNodeMix_OpType>` **op_type** = `0` `🔗<class_VisualShaderNodeMix_property_op_type>`

classref-property-setget

- `void (No return value.)` **set_op_type**(value: `OpType<enum_VisualShaderNodeMix_OpType>`)
- `OpType<enum_VisualShaderNodeMix_OpType>` **get_op_type**()

A type of operands and returned value.