github_url
hide

# OpenXRDpadBindingModifier

**Inherits:** `OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>` **\<** `OpenXRBindingModifier<class_OpenXRBindingModifier>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

The DPad binding modifier converts an axis input to a dpad output.

classref-introduction-group

## Description

The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction will be added to the interaction profile. When bound to actions the DPad emulation will be activated. You should **not** combine dpad inputs with normal inputs in the same action set for the same control, this will result in an error being returned when suggested bindings are submitted to OpenXR.

See [XR_EXT_dpad_binding](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding) for in-depth details.

**Note:** If the DPad binding modifier extension is enabled, all dpad binding paths will be available in the action map. Adding the modifier to an interaction profile allows you to further customize the behavior.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpenXRActionSet<class_OpenXRActionSet>` **action_set** `🔗<class_OpenXRDpadBindingModifier_property_action_set>`

classref-property-setget

- `void (No return value.)` **set_action_set**(value: `OpenXRActionSet<class_OpenXRActionSet>`)
- `OpenXRActionSet<class_OpenXRActionSet>` **get_action_set**()

Action set for which this dpad binding modifier is active.

classref-item-separator

classref-property

`float<class_float>` **center_region** = `0.1` `🔗<class_OpenXRDpadBindingModifier_property_center_region>`

classref-property-setget

- `void (No return value.)` **set_center_region**(value: `float<class_float>`)
- `float<class_float>` **get_center_region**()

Center region in which our center position of our dpad return `true`.

classref-item-separator

classref-property

`String<class_String>` **input_path** = `""` `🔗<class_OpenXRDpadBindingModifier_property_input_path>`

classref-property-setget

- `void (No return value.)` **set_input_path**(value: `String<class_String>`)
- `String<class_String>` **get_input_path**()

Input path for this dpad binding modifier.

classref-item-separator

classref-property

`bool<class_bool>` **is_sticky** = `false` `🔗<class_OpenXRDpadBindingModifier_property_is_sticky>`

classref-property-setget

- `void (No return value.)` **set_is_sticky**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_is_sticky**()

If `false`, when the joystick enters a new dpad zone this becomes `true`.

If `true`, when the joystick remains in active dpad zone, this remains `true` even if we overlap with another zone.

classref-item-separator

classref-property

`OpenXRHapticBase<class_OpenXRHapticBase>` **off_haptic** `🔗<class_OpenXRDpadBindingModifier_property_off_haptic>`

classref-property-setget

- `void (No return value.)` **set_off_haptic**(value: `OpenXRHapticBase<class_OpenXRHapticBase>`)
- `OpenXRHapticBase<class_OpenXRHapticBase>` **get_off_haptic**()

Haptic pulse to emit when the user releases the input.

classref-item-separator

classref-property

`OpenXRHapticBase<class_OpenXRHapticBase>` **on_haptic** `🔗<class_OpenXRDpadBindingModifier_property_on_haptic>`

classref-property-setget

- `void (No return value.)` **set_on_haptic**(value: `OpenXRHapticBase<class_OpenXRHapticBase>`)
- `OpenXRHapticBase<class_OpenXRHapticBase>` **get_on_haptic**()

Haptic pulse to emit when the user presses the input.

classref-item-separator

classref-property

`float<class_float>` **threshold** = `0.6` `🔗<class_OpenXRDpadBindingModifier_property_threshold>`

classref-property-setget

- `void (No return value.)` **set_threshold**(value: `float<class_float>`)
- `float<class_float>` **get_threshold**()

When our input value is equal or larger than this value, our dpad in that direction becomes `true`. It stays `true` until it falls under the `threshold_released<class_OpenXRDpadBindingModifier_property_threshold_released>` value.

classref-item-separator

classref-property

`float<class_float>` **threshold_released** = `0.4` `🔗<class_OpenXRDpadBindingModifier_property_threshold_released>`

classref-property-setget

- `void (No return value.)` **set_threshold_released**(value: `float<class_float>`)
- `float<class_float>` **get_threshold_released**()

When our input value falls below this, our output becomes `false`.

classref-item-separator

classref-property

`float<class_float>` **wedge_angle** = `1.5707964` `🔗<class_OpenXRDpadBindingModifier_property_wedge_angle>`

classref-property-setget

- `void (No return value.)` **set_wedge_angle**(value: `float<class_float>`)
- `float<class_float>` **get_wedge_angle**()

The angle of each wedge that identifies the 4 directions of the emulated dpad.