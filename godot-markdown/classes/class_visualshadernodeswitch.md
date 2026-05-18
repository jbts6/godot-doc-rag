github_url
hide

# VisualShaderNodeSwitch

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A selector function for use within the visual shader graph.

classref-introduction-group

## Description

Returns an associated value of the `op_type<class_VisualShaderNodeSwitch_property_op_type>` type if the provided boolean value is `true` or `false`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpType**: `🔗<enum_VisualShaderNodeSwitch_OpType>`

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_FLOAT** = `0`

A floating-point scalar.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_INT** = `1`

An integer scalar.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_UINT** = `2`

An unsigned integer scalar.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_VECTOR_2D** = `3`

A 2D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_VECTOR_3D** = `4`

A 3D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_VECTOR_4D** = `5`

A 4D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_BOOLEAN** = `6`

A boolean type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_TRANSFORM** = `7`

A transform type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeSwitch_OpType>` **OP_TYPE_MAX** = `8`

Represents the size of the `OpType<enum_VisualShaderNodeSwitch_OpType>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpType<enum_VisualShaderNodeSwitch_OpType>` **op_type** = `0` `🔗<class_VisualShaderNodeSwitch_property_op_type>`

classref-property-setget

- `void (No return value.)` **set_op_type**(value: `OpType<enum_VisualShaderNodeSwitch_OpType>`)
- `OpType<enum_VisualShaderNodeSwitch_OpType>` **get_op_type**()

A type of operands and returned value.