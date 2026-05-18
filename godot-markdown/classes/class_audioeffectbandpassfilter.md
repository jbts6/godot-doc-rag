github_url
hide

# AudioEffectBandPassFilter

**Inherits:** `AudioEffectFilter<class_AudioEffectFilter>` **\<** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a band-pass filter to an audio bus.

classref-introduction-group

## Description

A "band-pass" filter allows the frequencies at `AudioEffectFilter.cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` to pass unchanged, and attenuates frequencies outside the frequency threshold. It is the opposite of `AudioEffectBandLimitFilter<class_AudioEffectBandLimitFilter>` and `AudioEffectNotchFilter<class_AudioEffectNotchFilter>`.

This filter can be used to emulate sounds coming from weak speakers.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`