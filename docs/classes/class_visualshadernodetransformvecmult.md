github_url
hide

# VisualShaderNodeTransformVecMult

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Multiplies a `Transform3D<class_Transform3D>` and a `Vector3<class_Vector3>` within the visual shader graph.

classref-introduction-group

## Description

A multiplication operation on a transform (4×4 matrix) and a vector, with support for different multiplication operators.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Operator**: `🔗<enum_VisualShaderNodeTransformVecMult_Operator>`

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **OP_AxB** = `0`

Multiplies transform `a` by the vector `b`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **OP_BxA** = `1`

Multiplies vector `b` by the transform `a`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **OP_3x3_AxB** = `2`

Multiplies transform `a` by the vector `b`, skipping the last row and column of the transform.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **OP_3x3_BxA** = `3`

Multiplies vector `b` by the transform `a`, skipping the last row and column of the transform.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **OP_MAX** = `4`

Represents the size of the `Operator<enum_VisualShaderNodeTransformVecMult_Operator>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **operator** = `0` `🔗<class_VisualShaderNodeTransformVecMult_property_operator>`

classref-property-setget

- `void (No return value.)` **set_operator**(value: `Operator<enum_VisualShaderNodeTransformVecMult_Operator>`)
- `Operator<enum_VisualShaderNodeTransformVecMult_Operator>` **get_operator**()

The multiplication type to be performed.