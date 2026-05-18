github_url
hide

# AudioEffectBandLimitFilter

**Inherits:** `AudioEffectFilter<class_AudioEffectFilter>` **\<** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a band-limit filter to an audio bus.

classref-introduction-group

## Description

A "band-limit" filter attenuates the frequencies at `AudioEffectFilter.cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`, and allows frequencies outside the frequency threshold to pass unchanged. It is a wider and weaker version of `AudioEffectNotchFilter<class_AudioEffectNotchFilter>`, and is the opposite of `AudioEffectBandPassFilter<class_AudioEffectBandPassFilter>`.

This filter can be used to give more room for other sounds to play at that frequency.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`