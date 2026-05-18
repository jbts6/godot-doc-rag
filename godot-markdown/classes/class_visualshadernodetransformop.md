github_url
hide

# VisualShaderNodeTransformOp

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `Transform3D<class_Transform3D>` operator to be used within the visual shader graph.

classref-introduction-group

## Description

Applies `operator<class_VisualShaderNodeTransformOp_property_operator>` to two transform (4×4 matrices) inputs.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Operator**: `🔗<enum_VisualShaderNodeTransformOp_Operator>`

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_AxB** = `0`

Multiplies transform `a` by the transform `b`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_BxA** = `1`

Multiplies transform `b` by the transform `a`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_AxB_COMP** = `2`

Performs a component-wise multiplication of transform `a` by the transform `b`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_BxA_COMP** = `3`

Performs a component-wise multiplication of transform `b` by the transform `a`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_ADD** = `4`

Adds two transforms.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_A_MINUS_B** = `5`

Subtracts the transform `a` from the transform `b`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_B_MINUS_A** = `6`

Subtracts the transform `b` from the transform `a`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_A_DIV_B** = `7`

Divides the transform `a` by the transform `b`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_B_DIV_A** = `8`

Divides the transform `b` by the transform `a`.

classref-enumeration-constant

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **OP_MAX** = `9`

Represents the size of the `Operator<enum_VisualShaderNodeTransformOp_Operator>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Operator<enum_VisualShaderNodeTransformOp_Operator>` **operator** = `0` `🔗<class_VisualShaderNodeTransformOp_property_operator>`

classref-property-setget

- `void (No return value.)` **set_operator**(value: `Operator<enum_VisualShaderNodeTransformOp_Operator>`)
- `Operator<enum_VisualShaderNodeTransformOp_Operator>` **get_operator**()

The type of the operation to be performed on the transforms.