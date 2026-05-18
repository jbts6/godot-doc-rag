github_url
hide

# AudioEffectDelay

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a delay audio effect to an audio bus.

Emulates an echo by playing the input audio back after a period of time.

classref-introduction-group

## Description

A "delay" effect plays the input audio signal back after a period of time. Each repetition is called a "delay tap" or simply "tap". Delay taps may be played back multiple times to create the sound of a repeating, decaying echo. Delay effects range from a subtle echo to a pronounced blending of previous sounds with new sounds.

See also `AudioEffectReverb<class_AudioEffectReverb>` for a blurry, continuous echo.

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

`float<class_float>` **dry** = `1.0` `🔗<class_AudioEffectDelay_property_dry>`

classref-property-setget

- `void (No return value.)` **set_dry**(value: `float<class_float>`)
- `float<class_float>` **get_dry**()

The volume ratio of the original audio. Value can range from 0 to 1.

classref-item-separator

classref-property

`bool<class_bool>` **feedback_active** = `false` `🔗<class_AudioEffectDelay_property_feedback_active>`

classref-property-setget

- `void (No return value.)` **set_feedback_active**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_feedback_active**()

If `true`, feedback is enabled, repeating taps after they are played.

classref-item-separator

classref-property

`float<class_float>` **feedback_delay_ms** = `340.0` `🔗<class_AudioEffectDelay_property_feedback_delay_ms>`

classref-property-setget

- `void (No return value.)` **set_feedback_delay_ms**(value: `float<class_float>`)
- `float<class_float>` **get_feedback_delay_ms**()

Feedback delay time in milliseconds. Value can range from 0 to 1500.

classref-item-separator

classref-property

`float<class_float>` **feedback_level_db** = `-6.0` `🔗<class_AudioEffectDelay_property_feedback_level_db>`

classref-property-setget

- `void (No return value.)` **set_feedback_level_db**(value: `float<class_float>`)
- `float<class_float>` **get_feedback_level_db**()

Gain for feedback, in dB. Value can range from -60 to 0.

classref-item-separator

classref-property

`float<class_float>` **feedback_lowpass** = `16000.0` `🔗<class_AudioEffectDelay_property_feedback_lowpass>`

classref-property-setget

- `void (No return value.)` **set_feedback_lowpass**(value: `float<class_float>`)
- `float<class_float>` **get_feedback_lowpass**()

Low-pass filter for feedback, in Hz. Frequencies above this value are filtered out. Value can range from 1 to 16000.

classref-item-separator

classref-property

`bool<class_bool>` **tap1_active** = `true` `🔗<class_AudioEffectDelay_property_tap1_active>`

classref-property-setget

- `void (No return value.)` **set_tap1_active**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_tap1_active**()

If `true`, the first tap will be enabled.

classref-item-separator

classref-property

`float<class_float>` **tap1_delay_ms** = `250.0` `🔗<class_AudioEffectDelay_property_tap1_delay_ms>`

classref-property-setget

- `void (No return value.)` **set_tap1_delay_ms**(value: `float<class_float>`)
- `float<class_float>` **get_tap1_delay_ms**()

First tap delay time in milliseconds, compared to the original audio. Value can range from 0 to 1500.

classref-item-separator

classref-property

`float<class_float>` **tap1_level_db** = `-6.0` `🔗<class_AudioEffectDelay_property_tap1_level_db>`

classref-property-setget

- `void (No return value.)` **set_tap1_level_db**(value: `float<class_float>`)
- `float<class_float>` **get_tap1_level_db**()

Gain for the first tap, in dB. Value can range from -60 to 0.

classref-item-separator

classref-property

`float<class_float>` **tap1_pan** = `0.2` `🔗<class_AudioEffectDelay_property_tap1_pan>`

classref-property-setget

- `void (No return value.)` **set_tap1_pan**(value: `float<class_float>`)
- `float<class_float>` **get_tap1_pan**()

Pan position for the first tap. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.

classref-item-separator

classref-property

`bool<class_bool>` **tap2_active** = `true` `🔗<class_AudioEffectDelay_property_tap2_active>`

classref-property-setget

- `void (No return value.)` **set_tap2_active**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_tap2_active**()

If `true`, the second tap will be enabled.

classref-item-separator

classref-property

`float<class_float>` **tap2_delay_ms** = `500.0` `🔗<class_AudioEffectDelay_property_tap2_delay_ms>`

classref-property-setget

- `void (No return value.)` **set_tap2_delay_ms**(value: `float<class_float>`)
- `float<class_float>` **get_tap2_delay_ms**()

Second tap delay time in milliseconds, compared to the original audio. Value can range from 0 to 1500.

classref-item-separator

classref-property

`float<class_float>` **tap2_level_db** = `-12.0` `🔗<class_AudioEffectDelay_property_tap2_level_db>`

classref-property-setget

- `void (No return value.)` **set_tap2_level_db**(value: `float<class_float>`)
- `float<class_float>` **get_tap2_level_db**()

Gain for the second tap, in dB. Value can range from -60 to 0.

classref-item-separator

classref-property

`float<class_float>` **tap2_pan** = `-0.4` `🔗<class_AudioEffectDelay_property_tap2_pan>`

classref-property-setget

- `void (No return value.)` **set_tap2_pan**(value: `float<class_float>`)
- `float<class_float>` **get_tap2_pan**()

Pan position for the second tap. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.