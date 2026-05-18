github_url
hide

# AudioEffectReverb

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a reverberation audio effect to an audio bus.

Emulates an echo by playing a blurred version of the input audio.

classref-introduction-group

## Description

A "reverb" effect plays the input audio back continuously, decaying over a period of time. It simulates sounds in different kinds of spaces, ranging from small rooms, to big caverns.

See also `AudioEffectDelay<class_AudioEffectDelay>` for a non-blurry type of echo.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **damping** = `0.5` `🔗<class_AudioEffectReverb_property_damping>`

classref-property-setget

- `void (No return value.)` **set_damping**(value: `float<class_float>`)
- `float<class_float>` **get_damping**()

Defines how reflective the imaginary room's walls are. The more reflective, the more high frequency content the reverb has. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **dry** = `1.0` `🔗<class_AudioEffectReverb_property_dry>`

classref-property-setget

- `void (No return value.)` **set_dry**(value: `float<class_float>`)
- `float<class_float>` **get_dry**()

The volume ratio of the original audio. At 0, only the modified audio is outputted. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **hipass** = `0.0` `🔗<class_AudioEffectReverb_property_hipass>`

classref-property-setget

- `void (No return value.)` **set_hpf**(value: `float<class_float>`)
- `float<class_float>` **get_hpf**()

High-pass filter allows frequencies higher than a certain cutoff threshold and attenuates frequencies lower than the cutoff threshold. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **predelay_feedback** = `0.4` `🔗<class_AudioEffectReverb_property_predelay_feedback>`

classref-property-setget

- `void (No return value.)` **set_predelay_feedback**(value: `float<class_float>`)
- `float<class_float>` **get_predelay_feedback**()

Gain of early reflection copies. At higher values, early reflection copies are louder and ring out for longer. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **predelay_msec** = `150.0` `🔗<class_AudioEffectReverb_property_predelay_msec>`

classref-property-setget

- `void (No return value.)` **set_predelay_msec**(value: `float<class_float>`)
- `float<class_float>` **get_predelay_msec**()

Time between the original audio and the early reflections of the reverb signal, in milliseconds. Value can range from 20 to 500.

classref-item-separator

classref-property

`float<class_float>` **room_size** = `0.8` `🔗<class_AudioEffectReverb_property_room_size>`

classref-property-setget

- `void (No return value.)` **set_room_size**(value: `float<class_float>`)
- `float<class_float>` **get_room_size**()

Dimensions of simulated room. Bigger means more echoes. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **spread** = `1.0` `🔗<class_AudioEffectReverb_property_spread>`

classref-property-setget

- `void (No return value.)` **set_spread**(value: `float<class_float>`)
- `float<class_float>` **get_spread**()

Widens or narrows the stereo image of the reverb tail. At 1, it fully widens. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **wet** = `0.5` `🔗<class_AudioEffectReverb_property_wet>`

classref-property-setget

- `void (No return value.)` **set_wet**(value: `float<class_float>`)
- `float<class_float>` **get_wet**()

The volume ratio of the modified audio. At 0, only the original audio is outputted. Value can range from 0 to 1.