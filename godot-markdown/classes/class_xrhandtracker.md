github_url
hide

# XRHandTracker

**Inherits:** `XRPositionalTracker<class_XRPositionalTracker>` **\<** `XRTracker<class_XRTracker>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A tracked hand in XR.

classref-introduction-group

## Description

A hand tracking system will create an instance of this object and add it to the `XRServer<class_XRServer>`. This tracking system will then obtain skeleton data, convert it to the Godot Humanoid hand skeleton and store this data on the **XRHandTracker** object.

Use `XRHandModifier3D<class_XRHandModifier3D>` to animate a hand mesh using hand tracking data.

classref-introduction-group

## Tutorials

- `XR documentation index <../tutorials/xr/index>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **HandTrackingSource**: `🔗<enum_XRHandTracker_HandTrackingSource>`

classref-enumeration-constant

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **HAND_TRACKING_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown.

classref-enumeration-constant

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **HAND_TRACKING_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking data is unobstructed, meaning that an accurate method of hand tracking is used. These include optical hand tracking, data gloves, etc.

classref-enumeration-constant

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **HAND_TRACKING_SOURCE_CONTROLLER** = `2`

The source of hand tracking data is a controller, meaning that joint positions are inferred from controller inputs.

classref-enumeration-constant

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **HAND_TRACKING_SOURCE_NOT_TRACKED** = `3`

No hand tracking data is tracked, this either means the hand is obscured, the controller is turned off, or tracking is not supported for the current input type.

classref-enumeration-constant

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **HAND_TRACKING_SOURCE_MAX** = `4`

Represents the size of the `HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` enum.

classref-item-separator

classref-enumeration

enum **HandJoint**: `🔗<enum_XRHandTracker_HandJoint>`

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_PALM** = `0`

Palm joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_WRIST** = `1`

Wrist joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_THUMB_PHALANX_PROXIMAL** = `3`

Thumb phalanx proximal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_THUMB_PHALANX_DISTAL** = `4`

Thumb phalanx distal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_INDEX_FINGER_METACARPAL** = `6`

Index finger metacarpal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL** = `7`

Index finger phalanx proximal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL** = `9`

Index finger phalanx distal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_INDEX_FINGER_TIP** = `10`

Index finger tip joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_MIDDLE_FINGER_METACARPAL** = `11`

Middle finger metacarpal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `12`

Middle finger phalanx proximal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL** = `14`

Middle finger phalanx distal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_MIDDLE_FINGER_TIP** = `15`

Middle finger tip joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_RING_FINGER_METACARPAL** = `16`

Ring finger metacarpal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL** = `17`

Ring finger phalanx proximal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_RING_FINGER_PHALANX_DISTAL** = `19`

Ring finger phalanx distal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_RING_FINGER_TIP** = `20`

Ring finger tip joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_PINKY_FINGER_METACARPAL** = `21`

Pinky finger metacarpal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL** = `24`

Pinky finger phalanx distal joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_PINKY_FINGER_TIP** = `25`

Pinky finger tip joint.

classref-enumeration-constant

`HandJoint<enum_XRHandTracker_HandJoint>` **HAND_JOINT_MAX** = `26`

Represents the size of the `HandJoint<enum_XRHandTracker_HandJoint>` enum.

classref-item-separator

classref-enumeration

flags **HandJointFlags**: `🔗<enum_XRHandTracker_HandJointFlags>`

classref-enumeration-constant

`HandJointFlags<enum_XRHandTracker_HandJointFlags>` **HAND_JOINT_FLAG_ORIENTATION_VALID** = `1`

The hand joint's orientation data is valid.

classref-enumeration-constant

`HandJointFlags<enum_XRHandTracker_HandJointFlags>` **HAND_JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The hand joint's orientation is actively tracked. May not be set if tracking has been temporarily lost.

classref-enumeration-constant

`HandJointFlags<enum_XRHandTracker_HandJointFlags>` **HAND_JOINT_FLAG_POSITION_VALID** = `4`

The hand joint's position data is valid.

classref-enumeration-constant

`HandJointFlags<enum_XRHandTracker_HandJointFlags>` **HAND_JOINT_FLAG_POSITION_TRACKED** = `8`

The hand joint's position is actively tracked. May not be set if tracking has been temporarily lost.

classref-enumeration-constant

`HandJointFlags<enum_XRHandTracker_HandJointFlags>` **HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID** = `16`

The hand joint's linear velocity data is valid.

classref-enumeration-constant

`HandJointFlags<enum_XRHandTracker_HandJointFlags>` **HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID** = `32`

The hand joint's angular velocity data is valid.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **hand_tracking_source** = `0` `🔗<class_XRHandTracker_property_hand_tracking_source>`

classref-property-setget

- `void (No return value.)` **set_hand_tracking_source**(value: `HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`)
- `HandTrackingSource<enum_XRHandTracker_HandTrackingSource>` **get_hand_tracking_source**()

The source of the hand tracking data.

classref-item-separator

classref-property

`bool<class_bool>` **has_tracking_data** = `false` `🔗<class_XRHandTracker_property_has_tracking_data>`

classref-property-setget

- `void (No return value.)` **set_has_tracking_data**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_has_tracking_data**()

If `true`, the hand tracking data is valid.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Vector3<class_Vector3>` **get_hand_joint_angular_velocity**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRHandTracker_method_get_hand_joint_angular_velocity>`

Returns the angular velocity for the given hand joint.

classref-item-separator

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`HandJointFlags<enum_XRHandTracker_HandJointFlags>`\] **get_hand_joint_flags**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRHandTracker_method_get_hand_joint_flags>`

Returns flags about the validity of the tracking data for the given hand joint.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_hand_joint_linear_velocity**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRHandTracker_method_get_hand_joint_linear_velocity>`

Returns the linear velocity for the given hand joint.

classref-item-separator

classref-method

`float<class_float>` **get_hand_joint_radius**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRHandTracker_method_get_hand_joint_radius>`

Returns the radius of the given hand joint.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_hand_joint_transform**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRHandTracker_method_get_hand_joint_transform>`

Returns the transform for the given hand joint.

classref-item-separator

classref-method

`void (No return value.)` **set_hand_joint_angular_velocity**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`, angular_velocity: `Vector3<class_Vector3>`) `🔗<class_XRHandTracker_method_set_hand_joint_angular_velocity>`

Sets the angular velocity for the given hand joint.

classref-item-separator

classref-method

`void (No return value.)` **set_hand_joint_flags**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`HandJointFlags<enum_XRHandTracker_HandJointFlags>`\]) `🔗<class_XRHandTracker_method_set_hand_joint_flags>`

Sets flags about the validity of the tracking data for the given hand joint.

classref-item-separator

classref-method

`void (No return value.)` **set_hand_joint_linear_velocity**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`, linear_velocity: `Vector3<class_Vector3>`) `🔗<class_XRHandTracker_method_set_hand_joint_linear_velocity>`

Sets the linear velocity for the given hand joint.

classref-item-separator

classref-method

`void (No return value.)` **set_hand_joint_radius**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`, radius: `float<class_float>`) `🔗<class_XRHandTracker_method_set_hand_joint_radius>`

Sets the radius of the given hand joint.

classref-item-separator

classref-method

`void (No return value.)` **set_hand_joint_transform**(joint: `HandJoint<enum_XRHandTracker_HandJoint>`, transform: `Transform3D<class_Transform3D>`) `🔗<class_XRHandTracker_method_set_hand_joint_transform>`

Sets the transform for the given hand joint.