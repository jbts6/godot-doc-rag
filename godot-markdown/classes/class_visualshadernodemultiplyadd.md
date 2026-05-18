github_url
hide

# VisualShaderNodeMultiplyAdd

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Performs a fused multiply-add operation within the visual shader graph.

classref-introduction-group

## Description

Uses three operands to compute `(a * b + c)` expression.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpType**: `🔗<enum_VisualShaderNodeMultiplyAdd_OpType>`

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **OP_TYPE_SCALAR** = `0`

A floating-point scalar type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **OP_TYPE_MAX** = `4`

Represents the size of the `OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **op_type** = `0` `🔗<class_VisualShaderNodeMultiplyAdd_property_op_type>`

classref-property-setget

- `void (No return value.)` **set_op_type**(value: `OpType<enum_VisualShaderNodeMultiplyAdd_OpType>`)
- `OpType<enum_VisualShaderNodeMultiplyAdd_OpType>` **get_op_type**()

A type of operands and returned value.