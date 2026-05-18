github_url
hide

# OpenXRHapticVibration

**Inherits:** `OpenXRHapticBase<class_OpenXRHapticBase>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Vibration haptic feedback.

classref-introduction-group

## Description

This haptic feedback resource makes it possible to define a vibration based haptic feedback pulse that can be triggered through actions in the OpenXR action map.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **amplitude** = `1.0` `🔗<class_OpenXRHapticVibration_property_amplitude>`

classref-property-setget

- `void (No return value.)` **set_amplitude**(value: `float<class_float>`)
- `float<class_float>` **get_amplitude**()

The amplitude of the pulse between `0.0` and `1.0`.

classref-item-separator

classref-property

`int<class_int>` **duration** = `-1` `🔗<class_OpenXRHapticVibration_property_duration>`

classref-property-setget

- `void (No return value.)` **set_duration**(value: `int<class_int>`)
- `int<class_int>` **get_duration**()

The duration of the pulse in nanoseconds. Use `-1` for a minimum duration pulse for the current XR runtime.

classref-item-separator

classref-property

`float<class_float>` **frequency** = `0.0` `🔗<class_OpenXRHapticVibration_property_frequency>`

classref-property-setget

- `void (No return value.)` **set_frequency**(value: `float<class_float>`)
- `float<class_float>` **get_frequency**()

The frequency of the pulse in Hz. `0.0` will let the XR runtime chose an optimal frequency for the device used.