github_url
hide

# PinJoint3D

**Inherits:** `Joint3D<class_Joint3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate.

classref-introduction-group

## Description

A physics joint that attaches two 3D physics bodies at a single point, allowing them to freely rotate. For example, a `RigidBody3D<class_RigidBody3D>` can be attached to a `StaticBody3D<class_StaticBody3D>` to create a pendulum or a seesaw.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Param**: `🔗<enum_PinJoint3D_Param>`

classref-enumeration-constant

`Param<enum_PinJoint3D_Param>` **PARAM_BIAS** = `0`

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

classref-enumeration-constant

`Param<enum_PinJoint3D_Param>` **PARAM_DAMPING** = `1`

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

classref-enumeration-constant

`Param<enum_PinJoint3D_Param>` **PARAM_IMPULSE_CLAMP** = `2`

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **params/bias** = `0.3` `🔗<class_PinJoint3D_property_params/bias>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_PinJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_PinJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The force with which the pinned objects stay in positional relation to each other. The higher, the stronger.

classref-item-separator

classref-property

`float<class_float>` **params/damping** = `1.0` `🔗<class_PinJoint3D_property_params/damping>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_PinJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_PinJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The force with which the pinned objects stay in velocity relation to each other. The higher, the stronger.

classref-item-separator

classref-property

`float<class_float>` **params/impulse_clamp** = `0.0` `🔗<class_PinJoint3D_property_params/impulse_clamp>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_PinJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_PinJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If above 0, this value is the maximum value for an impulse that this Joint3D produces.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_param**(param: `Param<enum_PinJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PinJoint3D_method_get_param>`

Returns the value of the specified parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_param**(param: `Param<enum_PinJoint3D_Param>`, value: `float<class_float>`) `🔗<class_PinJoint3D_method_set_param>`

Sets the value of the specified parameter.