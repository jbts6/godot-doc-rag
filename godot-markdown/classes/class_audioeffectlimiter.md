github_url
hide

# AudioEffectLimiter

**Deprecated:** Use `AudioEffectHardLimiter<class_AudioEffectHardLimiter>` instead.

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a soft-clip limiter audio effect to an audio bus.

classref-introduction-group

## Description

A "limiter" is an audio effect designed to stop audio signals from exceeding a specified volume threshold level, and usually works by decreasing the volume or soft-clipping the audio. Adding one in the Master bus is always recommended to prevent clipping when the volume goes above 0 dB.

Soft clipping starts to decrease the peaks a little below the volume threshold level and progressively increases its effect as the input volume increases such that the threshold level is never exceeded.

If hard clipping is desired, consider `AudioEffectDistortion.MODE_CLIP<class_AudioEffectDistortion_constant_MODE_CLIP>`.

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

`float<class_float>` **ceiling_db** = `-0.1` `🔗<class_AudioEffectLimiter_property_ceiling_db>`

classref-property-setget

- `void (No return value.)` **set_ceiling_db**(value: `float<class_float>`)
- `float<class_float>` **get_ceiling_db**()

The waveform's maximum allowed value, in dB. Value can range from -20 to -0.1.

classref-item-separator

classref-property

`float<class_float>` **soft_clip_db** = `2.0` `🔗<class_AudioEffectLimiter_property_soft_clip_db>`

classref-property-setget

- `void (No return value.)` **set_soft_clip_db**(value: `float<class_float>`)
- `float<class_float>` **get_soft_clip_db**()

Modifies the volume of the limited waves, in dB. Value can range from 0 to 6.

classref-item-separator

classref-property

`float<class_float>` **soft_clip_ratio** = `10.0` `🔗<class_AudioEffectLimiter_property_soft_clip_ratio>`

classref-property-setget

- `void (No return value.)` **set_soft_clip_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_soft_clip_ratio**()

This property has no effect on the audio. Use `AudioEffectHardLimiter<class_AudioEffectHardLimiter>` instead, as this Limiter effect is deprecated.

classref-item-separator

classref-property

`float<class_float>` **threshold_db** = `0.0` `🔗<class_AudioEffectLimiter_property_threshold_db>`

classref-property-setget

- `void (No return value.)` **set_threshold_db**(value: `float<class_float>`)
- `float<class_float>` **get_threshold_db**()

The volume threshold level from which the limiter begins to be active, in dB. Value can range from -30 to 0.