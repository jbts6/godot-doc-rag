github_url
hide

# OpenXRAnalogThresholdModifier

**Inherits:** `OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>` **\<** `OpenXRBindingModifier<class_OpenXRBindingModifier>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

classref-introduction-group

## Description

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

See [XR_VALVE_analog_threshold](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VALVE_analog_threshold) for in-depth details.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpenXRHapticBase<class_OpenXRHapticBase>` **off_haptic** `🔗<class_OpenXRAnalogThresholdModifier_property_off_haptic>`

classref-property-setget

- `void (No return value.)` **set_off_haptic**(value: `OpenXRHapticBase<class_OpenXRHapticBase>`)
- `OpenXRHapticBase<class_OpenXRHapticBase>` **get_off_haptic**()

Haptic pulse to emit when the user releases the input.

classref-item-separator

classref-property

`float<class_float>` **off_threshold** = `0.4` `🔗<class_OpenXRAnalogThresholdModifier_property_off_threshold>`

classref-property-setget

- `void (No return value.)` **set_off_threshold**(value: `float<class_float>`)
- `float<class_float>` **get_off_threshold**()

When our input value falls below this, our output becomes `false`.

classref-item-separator

classref-property

`OpenXRHapticBase<class_OpenXRHapticBase>` **on_haptic** `🔗<class_OpenXRAnalogThresholdModifier_property_on_haptic>`

classref-property-setget

- `void (No return value.)` **set_on_haptic**(value: `OpenXRHapticBase<class_OpenXRHapticBase>`)
- `OpenXRHapticBase<class_OpenXRHapticBase>` **get_on_haptic**()

Haptic pulse to emit when the user presses the input.

classref-item-separator

classref-property

`float<class_float>` **on_threshold** = `0.6` `🔗<class_OpenXRAnalogThresholdModifier_property_on_threshold>`

classref-property-setget

- `void (No return value.)` **set_on_threshold**(value: `float<class_float>`)
- `float<class_float>` **get_on_threshold**()

When our input value is equal or larger than this value, our output becomes `true`. It stays `true` until it falls under the `off_threshold<class_OpenXRAnalogThresholdModifier_property_off_threshold>` value.