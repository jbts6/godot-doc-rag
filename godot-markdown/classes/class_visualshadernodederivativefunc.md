github_url
hide

# VisualShaderNodeDerivativeFunc

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Calculates a derivative within the visual shader graph.

classref-introduction-group

## Description

This node is only available in `Fragment` and `Light` visual shaders.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpType**: `🔗<enum_VisualShaderNodeDerivativeFunc_OpType>`

classref-enumeration-constant

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

classref-enumeration-constant

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **OP_TYPE_MAX** = `4`

Represents the size of the `OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` enum.

classref-item-separator

classref-enumeration

enum **Function**: `🔗<enum_VisualShaderNodeDerivativeFunc_Function>`

classref-enumeration-constant

`Function<enum_VisualShaderNodeDerivativeFunc_Function>` **FUNC_SUM** = `0`

Sum of absolute derivative in `x` and `y`.

classref-enumeration-constant

`Function<enum_VisualShaderNodeDerivativeFunc_Function>` **FUNC_X** = `1`

Derivative in `x` using local differencing.

classref-enumeration-constant

`Function<enum_VisualShaderNodeDerivativeFunc_Function>` **FUNC_Y** = `2`

Derivative in `y` using local differencing.

classref-enumeration-constant

`Function<enum_VisualShaderNodeDerivativeFunc_Function>` **FUNC_MAX** = `3`

Represents the size of the `Function<enum_VisualShaderNodeDerivativeFunc_Function>` enum.

classref-item-separator

classref-enumeration

enum **Precision**: `🔗<enum_VisualShaderNodeDerivativeFunc_Precision>`

classref-enumeration-constant

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` **PRECISION_NONE** = `0`

No precision is specified, the GPU driver is allowed to use whatever level of precision it chooses. This is the default option and is equivalent to using `dFdx()` or `dFdy()` in text shaders.

classref-enumeration-constant

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` **PRECISION_COARSE** = `1`

The derivative will be calculated using the current fragment's neighbors (which may not include the current fragment). This tends to be faster than using `PRECISION_FINE<class_VisualShaderNodeDerivativeFunc_constant_PRECISION_FINE>`, but may not be suitable when more precision is needed. This is equivalent to using `dFdxCoarse()` or `dFdyCoarse()` in text shaders.

classref-enumeration-constant

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` **PRECISION_FINE** = `2`

The derivative will be calculated using the current fragment and its immediate neighbors. This tends to be slower than using `PRECISION_COARSE<class_VisualShaderNodeDerivativeFunc_constant_PRECISION_COARSE>`, but may be necessary when more precision is needed. This is equivalent to using `dFdxFine()` or `dFdyFine()` in text shaders.

classref-enumeration-constant

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` **PRECISION_MAX** = `3`

Represents the size of the `Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Function<enum_VisualShaderNodeDerivativeFunc_Function>` **function** = `0` `🔗<class_VisualShaderNodeDerivativeFunc_property_function>`

classref-property-setget

- `void (No return value.)` **set_function**(value: `Function<enum_VisualShaderNodeDerivativeFunc_Function>`)
- `Function<enum_VisualShaderNodeDerivativeFunc_Function>` **get_function**()

A derivative function type.

classref-item-separator

classref-property

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **op_type** = `0` `🔗<class_VisualShaderNodeDerivativeFunc_property_op_type>`

classref-property-setget

- `void (No return value.)` **set_op_type**(value: `OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`)
- `OpType<enum_VisualShaderNodeDerivativeFunc_OpType>` **get_op_type**()

A type of operands and returned value.

classref-item-separator

classref-property

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` **precision** = `0` `🔗<class_VisualShaderNodeDerivativeFunc_property_precision>`

classref-property-setget

- `void (No return value.)` **set_precision**(value: `Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`)
- `Precision<enum_VisualShaderNodeDerivativeFunc_Precision>` **get_precision**()

Sets the level of precision to use for the derivative function. When using the Compatibility renderer, this setting has no effect.