github_url
hide

# ConeTwistJoint3D

**Inherits:** `Joint3D<class_Joint3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint.

classref-introduction-group

## Description

A physics joint that connects two 3D physics bodies in a way that simulates a ball-and-socket joint. The twist axis is initiated as the X axis of the **ConeTwistJoint3D**. Once the physics bodies swing, the twist axis is calculated as the middle of the X axes of the joint in the local space of the two physics bodies. Useful for limbs like shoulders and hips, lamps hanging off a ceiling, etc.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Param**: `🔗<enum_ConeTwistJoint3D_Param>`

classref-enumeration-constant

`Param<enum_ConeTwistJoint3D_Param>` **PARAM_SWING_SPAN** = `0`

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

classref-enumeration-constant

`Param<enum_ConeTwistJoint3D_Param>` **PARAM_TWIST_SPAN** = `1`

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.

classref-enumeration-constant

`Param<enum_ConeTwistJoint3D_Param>` **PARAM_BIAS** = `2`

The speed with which the swing or twist will take place.

The higher, the faster.

classref-enumeration-constant

`Param<enum_ConeTwistJoint3D_Param>` **PARAM_SOFTNESS** = `3`

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.

classref-enumeration-constant

`Param<enum_ConeTwistJoint3D_Param>` **PARAM_RELAXATION** = `4`

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.

classref-enumeration-constant

`Param<enum_ConeTwistJoint3D_Param>` **PARAM_MAX** = `5`

Represents the size of the `Param<enum_ConeTwistJoint3D_Param>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **bias** = `0.3` `🔗<class_ConeTwistJoint3D_property_bias>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_ConeTwistJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_ConeTwistJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed with which the swing or twist will take place.

The higher, the faster.

classref-item-separator

classref-property

`float<class_float>` **relaxation** = `1.0` `🔗<class_ConeTwistJoint3D_property_relaxation>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_ConeTwistJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_ConeTwistJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Defines, how fast the swing- and twist-speed-difference on both sides gets synced.

classref-item-separator

classref-property

`float<class_float>` **softness** = `0.8` `🔗<class_ConeTwistJoint3D_property_softness>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_ConeTwistJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_ConeTwistJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The ease with which the joint starts to twist. If it's too low, it takes more force to start twisting the joint.

classref-item-separator

classref-property

`float<class_float>` **swing_span** = `0.7853982` `🔗<class_ConeTwistJoint3D_property_swing_span>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_ConeTwistJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_ConeTwistJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Swing is rotation from side to side, around the axis perpendicular to the twist axis.

The swing span defines, how much rotation will not get corrected along the swing axis.

Could be defined as looseness in the **ConeTwistJoint3D**.

If below 0.05, this behavior is locked.

classref-item-separator

classref-property

`float<class_float>` **twist_span** = `3.1415927` `🔗<class_ConeTwistJoint3D_property_twist_span>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_ConeTwistJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_ConeTwistJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Twist is the rotation around the twist axis, this value defined how far the joint can twist.

Twist is locked if below 0.05.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_param**(param: `Param<enum_ConeTwistJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ConeTwistJoint3D_method_get_param>`

Returns the value of the specified parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_param**(param: `Param<enum_ConeTwistJoint3D_Param>`, value: `float<class_float>`) `🔗<class_ConeTwistJoint3D_method_set_param>`

Sets the value of the specified parameter.