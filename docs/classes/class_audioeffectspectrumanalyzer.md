github_url
hide

# AudioEffectSpectrumAnalyzer

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Creates an `AudioEffectInstance<class_AudioEffectInstance>` which performs frequency analysis and exposes results to be accessed in real-time.

classref-introduction-group

## Description

Calculates a Fourier Transform of the audio signal. This effect does not alter the audio. Can be used for creating real-time audio visualizations, like a spectrogram.

This resource configures an `AudioEffectSpectrumAnalyzerInstance<class_AudioEffectSpectrumAnalyzerInstance>`, which performs the actual analysis at runtime. An instance should be obtained with `AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>` to make use of this effect.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FFTSize**: `🔗<enum_AudioEffectSpectrumAnalyzer_FFTSize>`

classref-enumeration-constant

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.

classref-enumeration-constant

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **FFT_SIZE_MAX** = `5`

Represents the size of the `FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **buffer_length** = `2.0` `🔗<class_AudioEffectSpectrumAnalyzer_property_buffer_length>`

classref-property-setget

- `void (No return value.)` **set_buffer_length**(value: `float<class_float>`)
- `float<class_float>` **get_buffer_length**()

The length of the buffer to keep, in seconds. Higher values keep data around for longer, but require more memory. Value can range from 0.1 to 4.

classref-item-separator

classref-property

`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **fft_size** = `2` `🔗<class_AudioEffectSpectrumAnalyzer_property_fft_size>`

classref-property-setget

- `void (No return value.)` **set_fft_size**(value: `FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>`)
- `FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` **get_fft_size**()

The size of the [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) buffer. Higher values smooth out the spectrum analysis over time, but have greater latency. The effects of this higher latency are especially noticeable with sudden amplitude changes.