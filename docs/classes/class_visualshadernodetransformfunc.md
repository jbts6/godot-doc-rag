github_url
hide

# VisualShaderNodeTransformFunc

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Computes a `Transform3D<class_Transform3D>` function within the visual shader graph.

classref-introduction-group

## Description

Computes an inverse or transpose function on the provided `Transform3D<class_Transform3D>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Function**: `🔗<enum_VisualShaderNodeTransformFunc_Function>`

classref-enumeration-constant

`Function<enum_VisualShaderNodeTransformFunc_Function>` **FUNC_INVERSE** = `0`

Perform the inverse operation on the `Transform3D<class_Transform3D>` matrix.

classref-enumeration-constant

`Function<enum_VisualShaderNodeTransformFunc_Function>` **FUNC_TRANSPOSE** = `1`

Perform the transpose operation on the `Transform3D<class_Transform3D>` matrix.

classref-enumeration-constant

`Function<enum_VisualShaderNodeTransformFunc_Function>` **FUNC_MAX** = `2`

Represents the size of the `Function<enum_VisualShaderNodeTransformFunc_Function>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Function<enum_VisualShaderNodeTransformFunc_Function>` **function** = `0` `🔗<class_VisualShaderNodeTransformFunc_property_function>`

classref-property-setget

- `void (No return value.)` **set_function**(value: `Function<enum_VisualShaderNodeTransformFunc_Function>`)
- `Function<enum_VisualShaderNodeTransformFunc_Function>` **get_function**()

The function to be computed.