github_url
hide

# HingeJoint3D

**Inherits:** `Joint3D<class_Joint3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body.

classref-introduction-group

## Description

A physics joint that restricts the rotation of a 3D physics body around an axis relative to another physics body. For example, Body A can be a `StaticBody3D<class_StaticBody3D>` representing a door hinge that a `RigidBody3D<class_RigidBody3D>` rotates around.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Param**: `🔗<enum_HingeJoint3D_Param>`

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_BIAS** = `0`

The speed with which the two bodies get pulled together when they move in different directions.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_LIMIT_UPPER** = `1`

The maximum rotation. Only active if `angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>` is `true`.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_LIMIT_LOWER** = `2`

The minimum rotation. Only active if `angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>` is `true`.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_LIMIT_BIAS** = `3`

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_LIMIT_SOFTNESS** = `4`

**Deprecated:** This property is never used by the engine and is kept for compatibility purpose.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_LIMIT_RELAXATION** = `5`

The lower this value, the more the rotation gets slowed down.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_MOTOR_TARGET_VELOCITY** = `6`

Target speed for the motor.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_MOTOR_MAX_IMPULSE** = `7`

Maximum acceleration for the motor.

classref-enumeration-constant

`Param<enum_HingeJoint3D_Param>` **PARAM_MAX** = `8`

Represents the size of the `Param<enum_HingeJoint3D_Param>` enum.

classref-item-separator

classref-enumeration

enum **Flag**: `🔗<enum_HingeJoint3D_Flag>`

classref-enumeration-constant

`Flag<enum_HingeJoint3D_Flag>` **FLAG_USE_LIMIT** = `0`

If `true`, the hinges maximum and minimum rotation, defined by `angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>` and `angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>` has effects.

classref-enumeration-constant

`Flag<enum_HingeJoint3D_Flag>` **FLAG_ENABLE_MOTOR** = `1`

When activated, a motor turns the hinge.

classref-enumeration-constant

`Flag<enum_HingeJoint3D_Flag>` **FLAG_MAX** = `2`

Represents the size of the `Flag<enum_HingeJoint3D_Flag>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **angular_limit/bias** = `0.3` `🔗<class_HingeJoint3D_property_angular_limit/bias>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed with which the rotation across the axis perpendicular to the hinge gets corrected.

classref-item-separator

classref-property

`bool<class_bool>` **angular_limit/enable** = `false` `🔗<class_HingeJoint3D_property_angular_limit/enable>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the hinges maximum and minimum rotation, defined by `angular_limit/lower<class_HingeJoint3D_property_angular_limit/lower>` and `angular_limit/upper<class_HingeJoint3D_property_angular_limit/upper>` has effects.

classref-item-separator

classref-property

`float<class_float>` **angular_limit/lower** = `-1.5707964` `🔗<class_HingeJoint3D_property_angular_limit/lower>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation. Only active if `angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>` is `true`.

classref-item-separator

classref-property

`float<class_float>` **angular_limit/relaxation** = `1.0` `🔗<class_HingeJoint3D_property_angular_limit/relaxation>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The lower this value, the more the rotation gets slowed down.

classref-item-separator

classref-property

`float<class_float>` **angular_limit/softness** = `0.9` `🔗<class_HingeJoint3D_property_angular_limit/softness>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

**Deprecated:** This property is never set by the engine and is kept for compatibility purposes.

classref-item-separator

classref-property

`float<class_float>` **angular_limit/upper** = `1.5707964` `🔗<class_HingeJoint3D_property_angular_limit/upper>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum rotation. Only active if `angular_limit/enable<class_HingeJoint3D_property_angular_limit/enable>` is `true`.

classref-item-separator

classref-property

`bool<class_bool>` **motor/enable** = `false` `🔗<class_HingeJoint3D_property_motor/enable>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

When activated, a motor turns the hinge.

classref-item-separator

classref-property

`float<class_float>` **motor/max_impulse** = `1.0` `🔗<class_HingeJoint3D_property_motor/max_impulse>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum acceleration for the motor.

classref-item-separator

classref-property

`float<class_float>` **motor/target_velocity** = `1.0` `🔗<class_HingeJoint3D_property_motor/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Target speed for the motor.

classref-item-separator

classref-property

`float<class_float>` **params/bias** = `0.3` `🔗<class_HingeJoint3D_property_params/bias>`

classref-property-setget

- `void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed with which the two bodies get pulled together when they move in different directions.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **get_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_HingeJoint3D_method_get_flag>`

Returns the value of the specified flag.

classref-item-separator

classref-method

`float<class_float>` **get_param**(param: `Param<enum_HingeJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_HingeJoint3D_method_get_param>`

Returns the value of the specified parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_flag**(flag: `Flag<enum_HingeJoint3D_Flag>`, enabled: `bool<class_bool>`) `🔗<class_HingeJoint3D_method_set_flag>`

If `true`, enables the specified flag.

classref-item-separator

classref-method

`void (No return value.)` **set_param**(param: `Param<enum_HingeJoint3D_Param>`, value: `float<class_float>`) `🔗<class_HingeJoint3D_method_set_param>`

Sets the value of the specified parameter.