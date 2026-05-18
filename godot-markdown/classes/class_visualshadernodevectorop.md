github_url
hide

# VisualShaderNodeVectorOp

**Inherits:** `VisualShaderNodeVectorBase<class_VisualShaderNodeVectorBase>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A vector operator to be used within the visual shader graph.

classref-introduction-group

## Description

A visual shader node for use of vector operators. Operates on vector `a` and vector `b`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Operator**: `🔗<enum_VisualShaderNodeVectorOp_Operator>`

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_ADD** = `0`

Adds two vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_SUB** = `1`

Subtracts a vector from a vector.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_MUL** = `2`

Multiplies two vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_DIV** = `3`

Divides vector by vector.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_MOD** = `4`

Returns the remainder of the two vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_POW** = `5`

Returns the value of the first parameter raised to the power of the second, for each component of the vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_MAX** = `6`

Returns the greater of two values, for each component of the vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_MIN** = `7`

Returns the lesser of two values, for each component of the vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_CROSS** = `8`

Calculates the cross product of two vectors.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_ATAN2** = `9`

Returns the arc-tangent of the parameters.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_REFLECT** = `10`

Returns the vector that points in the direction of reflection. `a` is incident vector and `b` is the normal vector.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_STEP** = `11`

Vector step operator. Returns `0.0` if `a` is smaller than `b` and `1.0` otherwise.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **OP_ENUM_SIZE** = `12`

Represents the size of the `Operator<enum_VisualShaderNodeVectorOp_Operator>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Operator<enum_VisualShaderNodeVectorOp_Operator>` **operator** = `0` `🔗<class_VisualShaderNodeVectorOp_property_operator>`

classref-property-setget

- `void (No return value.)` **set_operator**(value: `Operator<enum_VisualShaderNodeVectorOp_Operator>`)
- `Operator<enum_VisualShaderNodeVectorOp_Operator>` **get_operator**()

The operator to be used.