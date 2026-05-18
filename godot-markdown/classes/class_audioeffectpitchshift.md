github_url
hide

# AudioEffectPitchShift

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a pitch-shifting audio effect to an audio bus.

Raises or lowers the pitch of the input audio.

classref-introduction-group

## Description

Allows modulation of pitch without modifying speed. All frequencies can be raised or lowered with minimal effect on transients.

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

enum **FFTSize**: `🔗<enum_AudioEffectPitchShift_FFTSize>`

classref-enumeration-constant

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **FFT_SIZE_MAX** = `5`

Represents the size of the `FFTSize<enum_AudioEffectPitchShift_FFTSize>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`FFTSize<enum_AudioEffectPitchShift_FFTSize>` **fft_size** = `3` `🔗<class_AudioEffectPitchShift_property_fft_size>`

classref-property-setget

- `void (No return value.)` **set_fft_size**(value: `FFTSize<enum_AudioEffectPitchShift_FFTSize>`)
- `FFTSize<enum_AudioEffectPitchShift_FFTSize>` **get_fft_size**()

The size of the [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer. Higher values smooth out the effect over time, but have greater latency. The effects of this higher latency are especially noticeable on audio signals that have sudden amplitude changes.

classref-item-separator

classref-property

`int<class_int>` **oversampling** = `4` `🔗<class_AudioEffectPitchShift_property_oversampling>`

classref-property-setget

- `void (No return value.)` **set_oversampling**(value: `int<class_int>`)
- `int<class_int>` **get_oversampling**()

The oversampling factor to use. Higher values result in better quality, but are more demanding on the CPU and may cause audio cracking if the CPU can't keep up.

classref-item-separator

classref-property

`float<class_float>` **pitch_scale** = `1.0` `🔗<class_AudioEffectPitchShift_property_pitch_scale>`

classref-property-setget

- `void (No return value.)` **set_pitch_scale**(value: `float<class_float>`)
- `float<class_float>` **get_pitch_scale**()

The pitch scale to use. `1.0` is the default pitch and plays sounds unaffected. `pitch_scale<class_AudioEffectPitchShift_property_pitch_scale>` can range from 0 (infinitely low pitch, inaudible) to 16 (16 times higher than the initial pitch).