github_url
hide

# Generic6DOFJoint3D

**Inherits:** `Joint3D<class_Joint3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A physics joint that allows for complex movement and rotation between two 3D physics bodies.

classref-introduction-group

## Description

The **Generic6DOFJoint3D** (6 Degrees Of Freedom) joint allows for implementing custom types of joints by locking the rotation and translation of certain axes.

The first 3 DOF represent the linear motion of the physics bodies and the last 3 DOF represent the angular motion of the physics bodies. Each axis can be either locked, or limited.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Param**: `🔗<enum_Generic6DOFJoint3D_Param>`

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_LOWER_LIMIT** = `0`

The minimum difference between the pivot points' axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_UPPER_LIMIT** = `1`

The maximum difference between the pivot points' axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_LIMIT_SOFTNESS** = `2`

A factor applied to the movement across the axes. The lower, the slower the movement.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_RESTITUTION** = `3`

The amount of restitution on the axes' movement. The lower, the more momentum gets lost.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_DAMPING** = `4`

The amount of damping that happens at the linear motion across the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_MOTOR_TARGET_VELOCITY** = `5`

The velocity the linear motor will try to reach.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_MOTOR_FORCE_LIMIT** = `6`

The maximum force the linear motor will apply while trying to reach the velocity target.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_SPRING_STIFFNESS** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_SPRING_DAMPING** = `8`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_LINEAR_SPRING_EQUILIBRIUM_POINT** = `9`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_LOWER_LIMIT** = `10`

The minimum rotation in negative direction to break loose and rotate around the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_UPPER_LIMIT** = `11`

The minimum rotation in positive direction to break loose and rotate around the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_LIMIT_SOFTNESS** = `12`

The speed of all rotations across the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_DAMPING** = `13`

The amount of rotational damping across the axes. The lower, the more damping occurs.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_RESTITUTION** = `14`

The amount of rotational restitution across the axes. The lower, the more restitution occurs.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_FORCE_LIMIT** = `15`

The maximum amount of force that can occur, when rotating around the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_ERP** = `16`

When rotating across the axes, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_MOTOR_TARGET_VELOCITY** = `17`

Target speed for the motor at the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_MOTOR_FORCE_LIMIT** = `18`

Maximum acceleration for the motor at the axes.

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_SPRING_STIFFNESS** = `19`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_SPRING_DAMPING** = `20`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_ANGULAR_SPRING_EQUILIBRIUM_POINT** = `21`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Param<enum_Generic6DOFJoint3D_Param>` **PARAM_MAX** = `22`

Represents the size of the `Param<enum_Generic6DOFJoint3D_Param>` enum.

classref-item-separator

classref-enumeration

enum **Flag**: `🔗<enum_Generic6DOFJoint3D_Flag>`

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_ENABLE_LINEAR_LIMIT** = `0`

If enabled, linear motion is possible within the given limits.

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_ENABLE_ANGULAR_LIMIT** = `1`

If enabled, rotational motion is possible within the given limits.

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_ENABLE_LINEAR_SPRING** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_ENABLE_ANGULAR_SPRING** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_ENABLE_MOTOR** = `4`

If enabled, there is a rotational motor across these axes.

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_ENABLE_LINEAR_MOTOR** = `5`

If enabled, there is a linear motor across these axes.

classref-enumeration-constant

`Flag<enum_Generic6DOFJoint3D_Flag>` **FLAG_MAX** = `6`

Represents the size of the `Flag<enum_Generic6DOFJoint3D_Flag>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **angular_limit_x/damping** = `1.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/damping>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of rotational damping across the X axis.

The lower, the longer an impulse from one side takes to travel to the other side.

classref-item-separator

classref-property

`bool<class_bool>` **angular_limit_x/enabled** = `true` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, rotation across the X axis is limited.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_x/erp** = `0.5` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/erp>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

When rotating across the X axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_x/force_limit** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum amount of force that can occur, when rotating around the X axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_x/lower_angle** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/lower_angle>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation in negative direction to break loose and rotate around the X axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_x/restitution** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/restitution>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of rotational restitution across the X axis. The lower, the more restitution occurs.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_x/softness** = `0.5` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/softness>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed of all rotations across the X axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_x/upper_angle** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_x/upper_angle>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation in positive direction to break loose and rotate around the X axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/damping** = `1.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/damping>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of rotational damping across the Y axis. The lower, the more damping occurs.

classref-item-separator

classref-property

`bool<class_bool>` **angular_limit_y/enabled** = `true` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, rotation across the Y axis is limited.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/erp** = `0.5` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/erp>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

When rotating across the Y axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/force_limit** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum amount of force that can occur, when rotating around the Y axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/lower_angle** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/lower_angle>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation in negative direction to break loose and rotate around the Y axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/restitution** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/restitution>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of rotational restitution across the Y axis. The lower, the more restitution occurs.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/softness** = `0.5` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/softness>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed of all rotations across the Y axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_y/upper_angle** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_y/upper_angle>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation in positive direction to break loose and rotate around the Y axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/damping** = `1.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/damping>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of rotational damping across the Z axis. The lower, the more damping occurs.

classref-item-separator

classref-property

`bool<class_bool>` **angular_limit_z/enabled** = `true` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, rotation across the Z axis is limited.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/erp** = `0.5` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/erp>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

When rotating across the Z axis, this error tolerance factor defines how much the correction gets slowed down. The lower, the slower.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/force_limit** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum amount of force that can occur, when rotating around the Z axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/lower_angle** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/lower_angle>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation in negative direction to break loose and rotate around the Z axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/restitution** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/restitution>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of rotational restitution across the Z axis. The lower, the more restitution occurs.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/softness** = `0.5` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/softness>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed of all rotations across the Z axis.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_z/upper_angle** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_limit_z/upper_angle>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum rotation in positive direction to break loose and rotate around the Z axis.

classref-item-separator

classref-property

`bool<class_bool>` **angular_motor_x/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_angular_motor_x/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, a rotating motor at the X axis is enabled.

classref-item-separator

classref-property

`float<class_float>` **angular_motor_x/force_limit** = `300.0` `🔗<class_Generic6DOFJoint3D_property_angular_motor_x/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum acceleration for the motor at the X axis.

classref-item-separator

classref-property

`float<class_float>` **angular_motor_x/target_velocity** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_motor_x/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Target speed for the motor at the X axis.

classref-item-separator

classref-property

`bool<class_bool>` **angular_motor_y/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_angular_motor_y/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, a rotating motor at the Y axis is enabled.

classref-item-separator

classref-property

`float<class_float>` **angular_motor_y/force_limit** = `300.0` `🔗<class_Generic6DOFJoint3D_property_angular_motor_y/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum acceleration for the motor at the Y axis.

classref-item-separator

classref-property

`float<class_float>` **angular_motor_y/target_velocity** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_motor_y/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Target speed for the motor at the Y axis.

classref-item-separator

classref-property

`bool<class_bool>` **angular_motor_z/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_angular_motor_z/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, a rotating motor at the Z axis is enabled.

classref-item-separator

classref-property

`float<class_float>` **angular_motor_z/force_limit** = `300.0` `🔗<class_Generic6DOFJoint3D_property_angular_motor_z/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum acceleration for the motor at the Z axis.

classref-item-separator

classref-property

`float<class_float>` **angular_motor_z/target_velocity** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_motor_z/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Target speed for the motor at the Z axis.

classref-item-separator

classref-property

`float<class_float>` **angular_spring_x/damping** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_x/damping>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`bool<class_bool>` **angular_spring_x/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_angular_spring_x/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_x/equilibrium_point** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_x/equilibrium_point>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_x/stiffness** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_x/stiffness>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_y/damping** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_y/damping>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`bool<class_bool>` **angular_spring_y/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_angular_spring_y/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_y/equilibrium_point** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_y/equilibrium_point>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_y/stiffness** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_y/stiffness>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_z/damping** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_z/damping>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`bool<class_bool>` **angular_spring_z/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_angular_spring_z/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_z/equilibrium_point** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_z/equilibrium_point>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **angular_spring_z/stiffness** = `0.0` `🔗<class_Generic6DOFJoint3D_property_angular_spring_z/stiffness>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_limit_x/damping** = `1.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_x/damping>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of damping that happens at the X motion.

classref-item-separator

classref-property

`bool<class_bool>` **linear_limit_x/enabled** = `true` `🔗<class_Generic6DOFJoint3D_property_linear_limit_x/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the linear motion across the X axis is limited.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_x/lower_distance** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_x/lower_distance>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum difference between the pivot points' X axis.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_x/restitution** = `0.5` `🔗<class_Generic6DOFJoint3D_property_linear_limit_x/restitution>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of restitution on the X axis movement. The lower, the more momentum gets lost.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_x/softness** = `0.7` `🔗<class_Generic6DOFJoint3D_property_linear_limit_x/softness>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

A factor applied to the movement across the X axis. The lower, the slower the movement.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_x/upper_distance** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_x/upper_distance>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum difference between the pivot points' X axis.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_y/damping** = `1.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_y/damping>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of damping that happens at the Y motion.

classref-item-separator

classref-property

`bool<class_bool>` **linear_limit_y/enabled** = `true` `🔗<class_Generic6DOFJoint3D_property_linear_limit_y/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the linear motion across the Y axis is limited.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_y/lower_distance** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_y/lower_distance>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum difference between the pivot points' Y axis.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_y/restitution** = `0.5` `🔗<class_Generic6DOFJoint3D_property_linear_limit_y/restitution>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of restitution on the Y axis movement. The lower, the more momentum gets lost.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_y/softness** = `0.7` `🔗<class_Generic6DOFJoint3D_property_linear_limit_y/softness>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

A factor applied to the movement across the Y axis. The lower, the slower the movement.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_y/upper_distance** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_y/upper_distance>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum difference between the pivot points' Y axis.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_z/damping** = `1.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_z/damping>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of damping that happens at the Z motion.

classref-item-separator

classref-property

`bool<class_bool>` **linear_limit_z/enabled** = `true` `🔗<class_Generic6DOFJoint3D_property_linear_limit_z/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the linear motion across the Z axis is limited.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_z/lower_distance** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_z/lower_distance>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The minimum difference between the pivot points' Z axis.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_z/restitution** = `0.5` `🔗<class_Generic6DOFJoint3D_property_linear_limit_z/restitution>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The amount of restitution on the Z axis movement. The lower, the more momentum gets lost.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_z/softness** = `0.7` `🔗<class_Generic6DOFJoint3D_property_linear_limit_z/softness>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

A factor applied to the movement across the Z axis. The lower, the slower the movement.

classref-item-separator

classref-property

`float<class_float>` **linear_limit_z/upper_distance** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_limit_z/upper_distance>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum difference between the pivot points' Z axis.

classref-item-separator

classref-property

`bool<class_bool>` **linear_motor_x/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_linear_motor_x/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, then there is a linear motor on the X axis. It will attempt to reach the target velocity while staying within the force limits.

classref-item-separator

classref-property

`float<class_float>` **linear_motor_x/force_limit** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_motor_x/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum force the linear motor can apply on the X axis while trying to reach the target velocity.

classref-item-separator

classref-property

`float<class_float>` **linear_motor_x/target_velocity** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_motor_x/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed that the linear motor will attempt to reach on the X axis.

classref-item-separator

classref-property

`bool<class_bool>` **linear_motor_y/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_linear_motor_y/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, then there is a linear motor on the Y axis. It will attempt to reach the target velocity while staying within the force limits.

classref-item-separator

classref-property

`float<class_float>` **linear_motor_y/force_limit** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_motor_y/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum force the linear motor can apply on the Y axis while trying to reach the target velocity.

classref-item-separator

classref-property

`float<class_float>` **linear_motor_y/target_velocity** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_motor_y/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed that the linear motor will attempt to reach on the Y axis.

classref-item-separator

classref-property

`bool<class_bool>` **linear_motor_z/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_linear_motor_z/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, then there is a linear motor on the Z axis. It will attempt to reach the target velocity while staying within the force limits.

classref-item-separator

classref-property

`float<class_float>` **linear_motor_z/force_limit** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_motor_z/force_limit>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum force the linear motor can apply on the Z axis while trying to reach the target velocity.

classref-item-separator

classref-property

`float<class_float>` **linear_motor_z/target_velocity** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_motor_z/target_velocity>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The speed that the linear motor will attempt to reach on the Z axis.

classref-item-separator

classref-property

`float<class_float>` **linear_spring_x/damping** = `0.01` `🔗<class_Generic6DOFJoint3D_property_linear_spring_x/damping>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`bool<class_bool>` **linear_spring_x/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_linear_spring_x/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_x/equilibrium_point** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_spring_x/equilibrium_point>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_x/stiffness** = `0.01` `🔗<class_Generic6DOFJoint3D_property_linear_spring_x/stiffness>`

classref-property-setget

- `void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_y/damping** = `0.01` `🔗<class_Generic6DOFJoint3D_property_linear_spring_y/damping>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`bool<class_bool>` **linear_spring_y/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_linear_spring_y/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_y/equilibrium_point** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_spring_y/equilibrium_point>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_y/stiffness** = `0.01` `🔗<class_Generic6DOFJoint3D_property_linear_spring_y/stiffness>`

classref-property-setget

- `void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_z/damping** = `0.01` `🔗<class_Generic6DOFJoint3D_property_linear_spring_z/damping>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`bool<class_bool>` **linear_spring_z/enabled** = `false` `🔗<class_Generic6DOFJoint3D_property_linear_spring_z/enabled>`

classref-property-setget

- `void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`)
- `bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_z/equilibrium_point** = `0.0` `🔗<class_Generic6DOFJoint3D_property_linear_spring_z/equilibrium_point>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`float<class_float>` **linear_spring_z/stiffness** = `0.01` `🔗<class_Generic6DOFJoint3D_property_linear_spring_z/stiffness>`

classref-property-setget

- `void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`)
- `float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **get_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Generic6DOFJoint3D_method_get_flag_x>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **get_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Generic6DOFJoint3D_method_get_flag_y>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`bool<class_bool>` **get_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Generic6DOFJoint3D_method_get_flag_z>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **get_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Generic6DOFJoint3D_method_get_param_x>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **get_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Generic6DOFJoint3D_method_get_param_y>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`float<class_float>` **get_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Generic6DOFJoint3D_method_get_param_z>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_flag_x**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`) `🔗<class_Generic6DOFJoint3D_method_set_flag_x>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_flag_y**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`) `🔗<class_Generic6DOFJoint3D_method_set_flag_y>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_flag_z**(flag: `Flag<enum_Generic6DOFJoint3D_Flag>`, value: `bool<class_bool>`) `🔗<class_Generic6DOFJoint3D_method_set_flag_z>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_param_x**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`) `🔗<class_Generic6DOFJoint3D_method_set_param_x>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_param_y**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`) `🔗<class_Generic6DOFJoint3D_method_set_param_y>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_param_z**(param: `Param<enum_Generic6DOFJoint3D_Param>`, value: `float<class_float>`) `🔗<class_Generic6DOFJoint3D_method_set_param_z>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!