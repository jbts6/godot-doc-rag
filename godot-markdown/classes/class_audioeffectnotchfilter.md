github_url
hide

# AudioEffectNotchFilter

**Inherits:** `AudioEffectFilter<class_AudioEffectFilter>` **\<** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a notch filter to an audio bus.

classref-introduction-group

## Description

A "notch" filter attenuates frequencies at `AudioEffectFilter.cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` and allows frequencies outside the frequency threshold to pass unchanged. It is a narrower and stronger version of `AudioEffectBandLimitFilter<class_AudioEffectBandLimitFilter>`, and is the opposite of `AudioEffectBandPassFilter<class_AudioEffectBandPassFilter>`.

This filter can be used to give more room for other sounds to play at that frequency. Because of how much it attenuates frequencies, it can also be used to completely remove undesired frequencies.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`