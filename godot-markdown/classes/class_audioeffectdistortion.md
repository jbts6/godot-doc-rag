github_url
hide

# AudioEffectDistortion

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a distortion audio effect to an audio bus.

Remaps audio samples using a nonlinear function to achieve a distorted sound.

classref-introduction-group

## Description

A "distortion" effect modifies the waveform via a nonlinear mathematical function (see available ones in `Mode<enum_AudioEffectDistortion_Mode>`), based on the amplitude of the waveform's samples.

**Note:** In a nonlinear function, an input sample at *x* amplitude value, will either have its amplitude increased or decreased to a *y* value, based on the function value at *x*, which is why even at the same `drive<class_AudioEffectDistortion_property_drive>`, the output sound will vary depending on the input's volume. To change the volume while maintaining the output waveform, use `post_gain<class_AudioEffectDistortion_property_post_gain>`.

In this effect, each type is a different nonlinear function. The different types available are: clip, atan, lofi (bitcrush), overdrive, and waveshape. Every distortion type available here is symmetric: negative amplitude values are affected the same way as positive ones.

Although distortion will always change frequency content, usually by introducing high harmonics, different distortion types offer a range of sound qualities; from "soft" and "warm", to "crunchy" and "abrasive".

For games, it can help simulate sound coming from some saturated device or speaker very efficiently. It can also help the audio stand out in a mix, by introducing higher frequencies and increasing the volume.

**Note:** Although usually imperceptible, an enabled distortion effect still changes the sound even when `drive<class_AudioEffectDistortion_property_drive>` is set to 0. This is not a bug. If this behavior is undesirable, consider disabling the effect using `AudioServer.set_bus_effect_enabled()<class_AudioServer_method_set_bus_effect_enabled>`.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Mode**: `🔗<enum_AudioEffectDistortion_Mode>`

classref-enumeration-constant

`Mode<enum_AudioEffectDistortion_Mode>` **MODE_CLIP** = `0`

Flattens the waveform at 0 dB in a sharp manner. `drive<class_AudioEffectDistortion_property_drive>` increases amplitude of samples exponentially. This mode functions as a hard clipper if `drive<class_AudioEffectDistortion_property_drive>` is set to 0, and is the only mode that clips audio signals at 0 dB.

classref-enumeration-constant

`Mode<enum_AudioEffectDistortion_Mode>` **MODE_ATAN** = `1`

Flattens the waveform in a smooth manner, following an arctangent curve. The audio decreases in volume, before flattening peaks to `PI * 4.0` (linear value), if it was normalized beforehand.

classref-enumeration-constant

`Mode<enum_AudioEffectDistortion_Mode>` **MODE_LOFI** = `2`

Decreases audio bit depth to achieve a low-resolution audio signal, going from 16-bit to 2-bit. Can be used to emulate the sound of early digital audio devices.

classref-enumeration-constant

`Mode<enum_AudioEffectDistortion_Mode>` **MODE_OVERDRIVE** = `3`

Emulates the warm distortion produced by a field effect transistor, which is commonly used in solid-state musical instrument amplifiers. `drive<class_AudioEffectDistortion_property_drive>` has no effect in this mode.

classref-enumeration-constant

`Mode<enum_AudioEffectDistortion_Mode>` **MODE_WAVESHAPE** = `4`

Flattens the waveform in a smooth manner, until it reaches a sharp peak at `drive = 1`, following a generic absolute sigmoid function.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **drive** = `0.0` `🔗<class_AudioEffectDistortion_property_drive>`

classref-property-setget

- `void (No return value.)` **set_drive**(value: `float<class_float>`)
- `float<class_float>` **get_drive**()

Distortion intensity. Controls how much of the input audio is affected by the distortion curve by moving from a linear function to a nonlinear one. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **keep_hf_hz** = `16000.0` `🔗<class_AudioEffectDistortion_property_keep_hf_hz>`

classref-property-setget

- `void (No return value.)` **set_keep_hf_hz**(value: `float<class_float>`)
- `float<class_float>` **get_keep_hf_hz**()

High-pass filter, in Hz. Frequencies higher than this value will not be affected by the distortion. Value can range from 1 to 20000.

classref-item-separator

classref-property

`Mode<enum_AudioEffectDistortion_Mode>` **mode** = `0` `🔗<class_AudioEffectDistortion_property_mode>`

classref-property-setget

- `void (No return value.)` **set_mode**(value: `Mode<enum_AudioEffectDistortion_Mode>`)
- `Mode<enum_AudioEffectDistortion_Mode>` **get_mode**()

Distortion type. Changes the nonlinear function used to distort the waveform. See `Mode<enum_AudioEffectDistortion_Mode>`.

classref-item-separator

classref-property

`float<class_float>` **post_gain** = `0.0` `🔗<class_AudioEffectDistortion_property_post_gain>`

classref-property-setget

- `void (No return value.)` **set_post_gain**(value: `float<class_float>`)
- `float<class_float>` **get_post_gain**()

Gain after the effect, in dB. Value can range from -80 to 24.

classref-item-separator

classref-property

`float<class_float>` **pre_gain** = `0.0` `🔗<class_AudioEffectDistortion_property_pre_gain>`

classref-property-setget

- `void (No return value.)` **set_pre_gain**(value: `float<class_float>`)
- `float<class_float>` **get_pre_gain**()

Gain before the effect, in dB. Value can range from -60 to 60.