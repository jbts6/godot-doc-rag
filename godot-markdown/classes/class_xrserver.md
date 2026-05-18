github_url
hide

# XRServer

**Inherits:** `Object<class_Object>`

Server for AR and VR features.

classref-introduction-group

## Description

The AR/VR server is the heart of our Advanced and Virtual Reality solution and handles all the processing.

classref-introduction-group

## Tutorials

- `XR documentation index <../tutorials/xr/index>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**interface_added**(interface_name: `StringName<class_StringName>`) `🔗<class_XRServer_signal_interface_added>`

Emitted when a new interface has been added.

classref-item-separator

classref-signal

**interface_removed**(interface_name: `StringName<class_StringName>`) `🔗<class_XRServer_signal_interface_removed>`

Emitted when an interface is removed.

classref-item-separator

classref-signal

**reference_frame_changed**() `🔗<class_XRServer_signal_reference_frame_changed>`

Emitted when the reference frame transform changes.

classref-item-separator

classref-signal

**tracker_added**(tracker_name: `StringName<class_StringName>`, type: `int<class_int>`) `🔗<class_XRServer_signal_tracker_added>`

Emitted when a new tracker has been added. If you don't use a fixed number of controllers or if you're using `XRAnchor3D<class_XRAnchor3D>`s for an AR solution, it is important to react to this signal to add the appropriate `XRController3D<class_XRController3D>` or `XRAnchor3D<class_XRAnchor3D>` nodes related to this new tracker.

classref-item-separator

classref-signal

**tracker_removed**(tracker_name: `StringName<class_StringName>`, type: `int<class_int>`) `🔗<class_XRServer_signal_tracker_removed>`

Emitted when a tracker is removed. You should remove any `XRController3D<class_XRController3D>` or `XRAnchor3D<class_XRAnchor3D>` points if applicable. This is not mandatory, the nodes simply become inactive and will be made active again when a new tracker becomes available (i.e. a new controller is switched on that takes the place of the previous one).

classref-item-separator

classref-signal

**tracker_updated**(tracker_name: `StringName<class_StringName>`, type: `int<class_int>`) `🔗<class_XRServer_signal_tracker_updated>`

Emitted when an existing tracker has been updated. This can happen if the user switches controllers.

classref-item-separator

classref-signal

**world_origin_changed**() `🔗<class_XRServer_signal_world_origin_changed>`

Emitted when the world origin transform changes.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **TrackerType**: `🔗<enum_XRServer_TrackerType>`

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_HEAD** = `1`

The tracker tracks the location of the player's head. This is usually a location centered between the player's eyes. Note that for handheld AR devices this can be the current location of the device.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_CONTROLLER** = `2`

The tracker tracks the location of a controller.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_BASESTATION** = `4`

The tracker tracks the location of a base station.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_ANCHOR** = `8`

The tracker tracks the location and size of an AR anchor.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_HAND** = `16`

The tracker tracks the location and joints of a hand.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_BODY** = `32`

The tracker tracks the location and joints of a body.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_FACE** = `64`

The tracker tracks the expressions of a face.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_ANY_KNOWN** = `127`

Used internally to filter trackers of any known type.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_UNKNOWN** = `128`

Used internally if we haven't set the tracker type yet.

classref-enumeration-constant

`TrackerType<enum_XRServer_TrackerType>` **TRACKER_ANY** = `255`

Used internally to select all trackers.

classref-item-separator

classref-enumeration

enum **RotationMode**: `🔗<enum_XRServer_RotationMode>`

classref-enumeration-constant

`RotationMode<enum_XRServer_RotationMode>` **RESET_FULL_ROTATION** = `0`

Fully reset the orientation of the HMD. Regardless of what direction the user is looking to in the real world. The user will look dead ahead in the virtual world.

classref-enumeration-constant

`RotationMode<enum_XRServer_RotationMode>` **RESET_BUT_KEEP_TILT** = `1`

Resets the orientation but keeps the tilt of the device. So if we're looking down, we keep looking down but heading will be reset.

classref-enumeration-constant

`RotationMode<enum_XRServer_RotationMode>` **DONT_RESET_ROTATION** = `2`

Does not reset the orientation of the HMD, only the position of the player gets centered.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **camera_locked_to_origin** = `false` `🔗<class_XRServer_property_camera_locked_to_origin>`

classref-property-setget

- `void (No return value.)` **set_camera_locked_to_origin**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_camera_locked_to_origin**()

If set to `true`, the scene will be rendered as if the camera is locked to the `XROrigin3D<class_XROrigin3D>`.

**Note:** This doesn't provide a very comfortable experience for users. This setting exists for doing benchmarking or automated testing, where you want to control what is rendered via code.

classref-item-separator

classref-property

`XRInterface<class_XRInterface>` **primary_interface** `🔗<class_XRServer_property_primary_interface>`

classref-property-setget

- `void (No return value.)` **set_primary_interface**(value: `XRInterface<class_XRInterface>`)
- `XRInterface<class_XRInterface>` **get_primary_interface**()

The primary `XRInterface<class_XRInterface>` currently bound to the **XRServer**.

classref-item-separator

classref-property

`Transform3D<class_Transform3D>` **world_origin** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` `🔗<class_XRServer_property_world_origin>`

classref-property-setget

- `void (No return value.)` **set_world_origin**(value: `Transform3D<class_Transform3D>`)
- `Transform3D<class_Transform3D>` **get_world_origin**()

The current origin of our tracking space in the virtual world. This is used by the renderer to properly position the camera with new tracking data.

**Note:** This property is managed by the current `XROrigin3D<class_XROrigin3D>` node. It is exposed for access from GDExtensions.

classref-item-separator

classref-property

`float<class_float>` **world_scale** = `1.0` `🔗<class_XRServer_property_world_scale>`

classref-property-setget

- `void (No return value.)` **set_world_scale**(value: `float<class_float>`)
- `float<class_float>` **get_world_scale**()

The scale of the game world compared to the real world. By default, most AR/VR platforms assume that 1 game unit corresponds to 1 real world meter.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_interface**(interface: `XRInterface<class_XRInterface>`) `🔗<class_XRServer_method_add_interface>`

Registers an `XRInterface<class_XRInterface>` object.

classref-item-separator

classref-method

`void (No return value.)` **add_tracker**(tracker: `XRTracker<class_XRTracker>`) `🔗<class_XRServer_method_add_tracker>`

Registers a new `XRTracker<class_XRTracker>` that tracks a physical object.

classref-item-separator

classref-method

`void (No return value.)` **center_on_hmd**(rotation_mode: `RotationMode<enum_XRServer_RotationMode>`, keep_height: `bool<class_bool>`) `🔗<class_XRServer_method_center_on_hmd>`

This is an important function to understand correctly. AR and VR platforms all handle positioning slightly differently.

For platforms that do not offer spatial tracking, our origin point `(0, 0, 0)` is the location of our HMD, but you have little control over the direction the player is facing in the real world.

For platforms that do offer spatial tracking, our origin point depends very much on the system. For OpenVR, our origin point is usually the center of the tracking space, on the ground. For other platforms, it's often the location of the tracking camera.

This method allows you to center your tracker on the location of the HMD. It will take the current location of the HMD and use that to adjust all your tracking data; in essence, realigning the real world to your player's current position in the game world.

For this method to produce usable results, tracking information must be available. This often takes a few frames after starting your game.

You should call this method after a few seconds have passed. For example, when the user requests a realignment of the display holding a designated button on a controller for a short period of time, or when implementing a teleport mechanism.

classref-item-separator

classref-method

`void (No return value.)` **clear_reference_frame**() `🔗<class_XRServer_method_clear_reference_frame>`

Clears the reference frame that was set by previous calls to `center_on_hmd()<class_XRServer_method_center_on_hmd>`.

classref-item-separator

classref-method

`XRInterface<class_XRInterface>` **find_interface**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRServer_method_find_interface>`

Finds an interface by its `name`. For example, if your project uses capabilities of an AR/VR platform, you can find the interface for that platform by name and initialize it.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_hmd_transform**() `🔗<class_XRServer_method_get_hmd_transform>`

Returns the primary interface's transformation.

classref-item-separator

classref-method

`XRInterface<class_XRInterface>` **get_interface**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRServer_method_get_interface>`

Returns the interface registered at the given `idx` index in the list of interfaces.

classref-item-separator

classref-method

`int<class_int>` **get_interface_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRServer_method_get_interface_count>`

Returns the number of interfaces currently registered with the AR/VR server. If your project supports multiple AR/VR platforms, you can look through the available interface, and either present the user with a selection or simply try to initialize each interface and use the first one that returns `true`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_interfaces**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRServer_method_get_interfaces>`

Returns a list of available interfaces the ID and name of each interface.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_reference_frame**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRServer_method_get_reference_frame>`

Returns the reference frame transform. Mostly used internally and exposed for GDExtension build interfaces.

classref-item-separator

classref-method

`XRTracker<class_XRTracker>` **get_tracker**(tracker_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_XRServer_method_get_tracker>`

Returns the positional tracker with the given `tracker_name`.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_trackers**(tracker_types: `int<class_int>`) `🔗<class_XRServer_method_get_trackers>`

Returns a dictionary of trackers for `tracker_types`.

classref-item-separator

classref-method

`void (No return value.)` **remove_interface**(interface: `XRInterface<class_XRInterface>`) `🔗<class_XRServer_method_remove_interface>`

Removes this `interface`.

classref-item-separator

classref-method

`void (No return value.)` **remove_tracker**(tracker: `XRTracker<class_XRTracker>`) `🔗<class_XRServer_method_remove_tracker>`

Removes this `tracker`.