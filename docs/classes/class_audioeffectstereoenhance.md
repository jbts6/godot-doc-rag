github_url
hide

# AudioEffectStereoEnhance

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a stereo manipulation audio effect to an audio bus.

Controls gain of the side channels, and widens the stereo image.

classref-introduction-group

## Description

Adjusts gain of the left and right channels, and makes mono sounds stereo through phase shifting.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **pan_pullout** = `1.0` `🔗<class_AudioEffectStereoEnhance_property_pan_pullout>`

classref-property-setget

- `void (No return value.)` **set_pan_pullout**(value: `float<class_float>`)
- `float<class_float>` **get_pan_pullout**()

Gain of the side channels, if they exist. A value of 0 will downmix stereo to mono. Value can range from 0 to 4.

classref-item-separator

classref-property

`float<class_float>` **surround** = `0.0` `🔗<class_AudioEffectStereoEnhance_property_surround>`

classref-property-setget

- `void (No return value.)` **set_surround**(value: `float<class_float>`)
- `float<class_float>` **get_surround**()

Widens the stereo image through phase shifting in conjunction with `time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>`. Just pans sound to the left channel if `time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>` is 0. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **time_pullout_ms** = `0.0` `🔗<class_AudioEffectStereoEnhance_property_time_pullout_ms>`

classref-property-setget

- `void (No return value.)` **set_time_pullout**(value: `float<class_float>`)
- `float<class_float>` **get_time_pullout**()

Widens the stereo image through phase shifting in conjunction with `surround<class_AudioEffectStereoEnhance_property_surround>`. Just delays the right channel if `surround<class_AudioEffectStereoEnhance_property_surround>` is 0. Value is in milliseconds, and can range from 0 to 50.