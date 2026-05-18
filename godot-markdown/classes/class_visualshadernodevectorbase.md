github_url
hide

# VisualShaderNodeVectorBase

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `VisualShaderNodeFaceForward<class_VisualShaderNodeFaceForward>`, `VisualShaderNodeVectorCompose<class_VisualShaderNodeVectorCompose>`, `VisualShaderNodeVectorDecompose<class_VisualShaderNodeVectorDecompose>`, `VisualShaderNodeVectorDistance<class_VisualShaderNodeVectorDistance>`, `VisualShaderNodeVectorFunc<class_VisualShaderNodeVectorFunc>`, `VisualShaderNodeVectorLen<class_VisualShaderNodeVectorLen>`, `VisualShaderNodeVectorOp<class_VisualShaderNodeVectorOp>`, `VisualShaderNodeVectorRefract<class_VisualShaderNodeVectorRefract>`

A base type for the nodes that perform vector operations within the visual shader graph.

classref-introduction-group

## Description

This is an abstract class. See the derived types for descriptions of the possible operations.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpType**: `🔗<enum_VisualShaderNodeVectorBase_OpType>`

classref-enumeration-constant

`OpType<enum_VisualShaderNodeVectorBase_OpType>` **OP_TYPE_VECTOR_2D** = `0`

A 2D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeVectorBase_OpType>` **OP_TYPE_VECTOR_3D** = `1`

A 3D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeVectorBase_OpType>` **OP_TYPE_VECTOR_4D** = `2`

A 4D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeVectorBase_OpType>` **OP_TYPE_MAX** = `3`

Represents the size of the `OpType<enum_VisualShaderNodeVectorBase_OpType>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpType<enum_VisualShaderNodeVectorBase_OpType>` **op_type** = `1` `🔗<class_VisualShaderNodeVectorBase_property_op_type>`

classref-property-setget

- `void (No return value.)` **set_op_type**(value: `OpType<enum_VisualShaderNodeVectorBase_OpType>`)
- `OpType<enum_VisualShaderNodeVectorBase_OpType>` **get_op_type**()

A vector type that this operation is performed on.