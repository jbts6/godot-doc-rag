github_url
hide

# PinJoint2D

**Inherits:** `Joint2D<class_Joint2D>` **\<** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A physics joint that attaches two 2D physics bodies at a single point, allowing them to freely rotate.

classref-introduction-group

## Description

A physics joint that attaches two 2D physics bodies at a single point, allowing them to freely rotate. For example, a `RigidBody2D<class_RigidBody2D>` can be attached to a `StaticBody2D<class_StaticBody2D>` to create a pendulum or a seesaw.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **angular_limit_enabled** = `false` `🔗<class_PinJoint2D_property_angular_limit_enabled>`

classref-property-setget

- `void (No return value.)` **set_angular_limit_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_angular_limit_enabled**()

If `true`, the pin maximum and minimum rotation, defined by `angular_limit_lower<class_PinJoint2D_property_angular_limit_lower>` and `angular_limit_upper<class_PinJoint2D_property_angular_limit_upper>` are applied.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_lower** = `0.0` `🔗<class_PinJoint2D_property_angular_limit_lower>`

classref-property-setget

- `void (No return value.)` **set_angular_limit_lower**(value: `float<class_float>`)
- `float<class_float>` **get_angular_limit_lower**()

The minimum rotation. Only active if `angular_limit_enabled<class_PinJoint2D_property_angular_limit_enabled>` is `true`.

classref-item-separator

classref-property

`float<class_float>` **angular_limit_upper** = `0.0` `🔗<class_PinJoint2D_property_angular_limit_upper>`

classref-property-setget

- `void (No return value.)` **set_angular_limit_upper**(value: `float<class_float>`)
- `float<class_float>` **get_angular_limit_upper**()

The maximum rotation. Only active if `angular_limit_enabled<class_PinJoint2D_property_angular_limit_enabled>` is `true`.

classref-item-separator

classref-property

`bool<class_bool>` **motor_enabled** = `false` `🔗<class_PinJoint2D_property_motor_enabled>`

classref-property-setget

- `void (No return value.)` **set_motor_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_motor_enabled**()

When activated, a motor turns the pin.

classref-item-separator

classref-property

`float<class_float>` **motor_target_velocity** = `0.0` `🔗<class_PinJoint2D_property_motor_target_velocity>`

classref-property-setget

- `void (No return value.)` **set_motor_target_velocity**(value: `float<class_float>`)
- `float<class_float>` **get_motor_target_velocity**()

Target speed for the motor. In radians per second.

classref-item-separator

classref-property

`float<class_float>` **softness** = `0.0` `🔗<class_PinJoint2D_property_softness>`

classref-property-setget

- `void (No return value.)` **set_softness**(value: `float<class_float>`)
- `float<class_float>` **get_softness**()

The higher this value, the more the bond to the pinned partner can flex.