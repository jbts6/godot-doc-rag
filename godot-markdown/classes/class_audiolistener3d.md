github_url
hide

# AudioListener3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Overrides the location sounds are heard from.

classref-introduction-group

## Description

Once added to the scene tree and enabled using `make_current()<class_AudioListener3D_method_make_current>`, this node will override the location sounds are heard from. This can be used to listen from a location different from the `Camera3D<class_Camera3D>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DopplerTracking**: `🔗<enum_AudioListener3D_DopplerTracking>`

classref-enumeration-constant

`DopplerTracking<enum_AudioListener3D_DopplerTracking>` **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) simulation (default).

classref-enumeration-constant

`DopplerTracking<enum_AudioListener3D_DopplerTracking>` **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's `AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>`).

classref-enumeration-constant

`DopplerTracking<enum_AudioListener3D_DopplerTracking>` **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this listener compared to those objects affect how audio is perceived (changing the audio's `AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>`).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`DopplerTracking<enum_AudioListener3D_DopplerTracking>` **doppler_tracking** = `0` `🔗<class_AudioListener3D_property_doppler_tracking>`

classref-property-setget

- `void (No return value.)` **set_doppler_tracking**(value: `DopplerTracking<enum_AudioListener3D_DopplerTracking>`)
- `DopplerTracking<enum_AudioListener3D_DopplerTracking>` **get_doppler_tracking**()

If not `DOPPLER_TRACKING_DISABLED<class_AudioListener3D_constant_DOPPLER_TRACKING_DISABLED>`, this listener will simulate the [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) for objects changed in particular `_process` methods.

**Note:** The Doppler effect will only be heard on `AudioStreamPlayer3D<class_AudioStreamPlayer3D>`s if `AudioStreamPlayer3D.doppler_tracking<class_AudioStreamPlayer3D_property_doppler_tracking>` is not set to `AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED<class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_current**() `🔗<class_AudioListener3D_method_clear_current>`

Disables the listener to use the current camera's listener instead.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_listener_transform**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioListener3D_method_get_listener_transform>`

Returns the listener's global orthonormalized `Transform3D<class_Transform3D>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_current**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioListener3D_method_is_current>`

Returns `true` if the listener was made current using `make_current()<class_AudioListener3D_method_make_current>`, `false` otherwise.

**Note:** There may be more than one AudioListener3D marked as "current" in the scene tree, but only the one that was made current last will be used.

classref-item-separator

classref-method

`void (No return value.)` **make_current**() `🔗<class_AudioListener3D_method_make_current>`

Enables the listener. This will override the current camera's listener.