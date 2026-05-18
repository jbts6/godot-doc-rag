github_url
hide

# XRPose

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

This object contains all data related to a pose on a tracked object.

classref-introduction-group

## Description

XR runtimes often identify multiple locations on devices such as controllers that are spatially tracked.

Orientation, location, linear velocity and angular velocity are all provided for each pose by the XR runtime. This object contains this state of a pose.

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

enum **TrackingConfidence**: `🔗<enum_XRPose_TrackingConfidence>`

classref-enumeration-constant

`TrackingConfidence<enum_XRPose_TrackingConfidence>` **XR_TRACKING_CONFIDENCE_NONE** = `0`

No tracking information is available for this pose.

classref-enumeration-constant

`TrackingConfidence<enum_XRPose_TrackingConfidence>` **XR_TRACKING_CONFIDENCE_LOW** = `1`

Tracking information may be inaccurate or estimated. For example, with inside out tracking this would indicate a controller may be (partially) obscured.

classref-enumeration-constant

`TrackingConfidence<enum_XRPose_TrackingConfidence>` **XR_TRACKING_CONFIDENCE_HIGH** = `2`

Tracking information is considered accurate and up to date.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector3<class_Vector3>` **angular_velocity** = `Vector3(0, 0, 0)` `🔗<class_XRPose_property_angular_velocity>`

classref-property-setget

- `void (No return value.)` **set_angular_velocity**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_angular_velocity**()

The angular velocity for this pose.

classref-item-separator

classref-property

`bool<class_bool>` **has_tracking_data** = `false` `🔗<class_XRPose_property_has_tracking_data>`

classref-property-setget

- `void (No return value.)` **set_has_tracking_data**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_has_tracking_data**()

If `true` our tracking data is up to date. If `false` we're no longer receiving new tracking data and our state is whatever that last valid state was.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **linear_velocity** = `Vector3(0, 0, 0)` `🔗<class_XRPose_property_linear_velocity>`

classref-property-setget

- `void (No return value.)` **set_linear_velocity**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_linear_velocity**()

The linear velocity of this pose.

classref-item-separator

classref-property

`StringName<class_StringName>` **name** = `&""` `🔗<class_XRPose_property_name>`

classref-property-setget

- `void (No return value.)` **set_name**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_name**()

The name of this pose. Usually, this name is derived from an action map set up by the user. Godot also suggests some pose names that `XRInterface<class_XRInterface>` objects are expected to implement:

- `root` is the root location, often used for tracked objects that do not have further nodes.
- `aim` is the tip of a controller with its orientation pointing outwards, often used for raycasts.
- `grip` is the location where the user grips the controller.
- `skeleton` is the root location for a hand mesh, when using hand tracking and an animated skeleton is supplied by the XR runtime.

classref-item-separator

classref-property

`TrackingConfidence<enum_XRPose_TrackingConfidence>` **tracking_confidence** = `0` `🔗<class_XRPose_property_tracking_confidence>`

classref-property-setget

- `void (No return value.)` **set_tracking_confidence**(value: `TrackingConfidence<enum_XRPose_TrackingConfidence>`)
- `TrackingConfidence<enum_XRPose_TrackingConfidence>` **get_tracking_confidence**()

The tracking confidence for this pose, provides insight on how accurate the spatial positioning of this record is.

classref-item-separator

classref-property

`Transform3D<class_Transform3D>` **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` `🔗<class_XRPose_property_transform>`

classref-property-setget

- `void (No return value.)` **set_transform**(value: `Transform3D<class_Transform3D>`)
- `Transform3D<class_Transform3D>` **get_transform**()

The transform containing the original and transform as reported by the XR runtime.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Transform3D<class_Transform3D>` **get_adjusted_transform**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRPose_method_get_adjusted_transform>`

Returns the `transform<class_XRPose_property_transform>` with world scale and our reference frame applied. This is the transform used to position `XRNode3D<class_XRNode3D>` objects.