github_url
hide

# VisualShaderNodeVec4Constant

**Inherits:** `VisualShaderNodeConstant<class_VisualShaderNodeConstant>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 4D vector constant to be used within the visual shader graph.

classref-introduction-group

## Description

A constant 4D vector, which can be used as an input node.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Quaternion<class_Quaternion>` **constant** = `Quaternion(0, 0, 0, 1)` `🔗<class_VisualShaderNodeVec4Constant_property_constant>`

classref-property-setget

- `void (No return value.)` **set_constant**(value: `Quaternion<class_Quaternion>`)
- `Quaternion<class_Quaternion>` **get_constant**()

A 4D vector (represented as a `Quaternion<class_Quaternion>`) constant which represents the state of this node.