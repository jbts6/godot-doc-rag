github_url
hide

# VisualShaderNodeParticleRandomness

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Visual shader node for randomizing particle values.

classref-introduction-group

## Description

Randomness node will output pseudo-random values of the given type based on the specified minimum and maximum values.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpType**: `🔗<enum_VisualShaderNodeParticleRandomness_OpType>`

classref-enumeration-constant

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **OP_TYPE_MAX** = `4`

Represents the size of the `OpType<enum_VisualShaderNodeParticleRandomness_OpType>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **op_type** = `0` `🔗<class_VisualShaderNodeParticleRandomness_property_op_type>`

classref-property-setget

- `void (No return value.)` **set_op_type**(value: `OpType<enum_VisualShaderNodeParticleRandomness_OpType>`)
- `OpType<enum_VisualShaderNodeParticleRandomness_OpType>` **get_op_type**()

A type of operands and returned value.