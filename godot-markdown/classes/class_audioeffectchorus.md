github_url
hide

# AudioEffectChorus

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a chorus audio effect to an audio bus.

Gives the impression of multiple audio sources.

classref-introduction-group

## Description

A "chorus" effect creates multiple copies of the original audio (called "voices") with variations in pitch, and layers on top of the original, giving the impression that the sound comes from multiple sources. This creates spectral and spatial movement.

Each voice is played a short period of time after the original audio, controlled by `delay`. An internal low-frequency oscillator (LFO) controls their pitch, and `depth` controls the LFO's maximum amount.

In the real world, this kind of effect is found in pianos, choirs, and instrument ensembles.

This effect can also be used to widen mono audio and make digital sounds have a more natural or analog quality.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **dry** = `1.0` `🔗<class_AudioEffectChorus_property_dry>`

classref-property-setget

- `void (No return value.)` **set_dry**(value: `float<class_float>`)
- `float<class_float>` **get_dry**()

The volume ratio of the original audio. Value can range from 0 to 1.

classref-item-separator

classref-property

`float<class_float>` **voice/1/cutoff_hz** = `8000.0` `🔗<class_AudioEffectChorus_property_voice/1/cutoff_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_cutoff_hz**(voice_idx: `int<class_int>`, cutoff_hz: `float<class_float>`)
- `float<class_float>` **get_voice_cutoff_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The frequency threshold of the voice's low-pass filter in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/1/delay_ms** = `15.0` `🔗<class_AudioEffectChorus_property_voice/1/delay_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_delay_ms**(voice_idx: `int<class_int>`, delay_ms: `float<class_float>`)
- `float<class_float>` **get_voice_delay_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The delay of the voice in milliseconds, compared to the original audio.

classref-item-separator

classref-property

`float<class_float>` **voice/1/depth_ms** = `2.0` `🔗<class_AudioEffectChorus_property_voice/1/depth_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_depth_ms**(voice_idx: `int<class_int>`, depth_ms: `float<class_float>`)
- `float<class_float>` **get_voice_depth_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The depth of the voice's low-frequency oscillator in milliseconds.

classref-item-separator

classref-property

`float<class_float>` **voice/1/level_db** = `0.0` `🔗<class_AudioEffectChorus_property_voice/1/level_db>`

classref-property-setget

- `void (No return value.)` **set_voice_level_db**(voice_idx: `int<class_int>`, level_db: `float<class_float>`)
- `float<class_float>` **get_voice_level_db**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The gain of the voice in dB.

classref-item-separator

classref-property

`float<class_float>` **voice/1/pan** = `-0.5` `🔗<class_AudioEffectChorus_property_voice/1/pan>`

classref-property-setget

- `void (No return value.)` **set_voice_pan**(voice_idx: `int<class_int>`, pan: `float<class_float>`)
- `float<class_float>` **get_voice_pan**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The pan position of the voice.

classref-item-separator

classref-property

`float<class_float>` **voice/1/rate_hz** = `0.8` `🔗<class_AudioEffectChorus_property_voice/1/rate_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_rate_hz**(voice_idx: `int<class_int>`, rate_hz: `float<class_float>`)
- `float<class_float>` **get_voice_rate_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The rate of the voice's low-frequency oscillator in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/2/cutoff_hz** = `8000.0` `🔗<class_AudioEffectChorus_property_voice/2/cutoff_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_cutoff_hz**(voice_idx: `int<class_int>`, cutoff_hz: `float<class_float>`)
- `float<class_float>` **get_voice_cutoff_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The frequency threshold of the voice's low-pass filter in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/2/delay_ms** = `20.0` `🔗<class_AudioEffectChorus_property_voice/2/delay_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_delay_ms**(voice_idx: `int<class_int>`, delay_ms: `float<class_float>`)
- `float<class_float>` **get_voice_delay_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The delay of the voice in milliseconds, compared to the original audio.

classref-item-separator

classref-property

`float<class_float>` **voice/2/depth_ms** = `3.0` `🔗<class_AudioEffectChorus_property_voice/2/depth_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_depth_ms**(voice_idx: `int<class_int>`, depth_ms: `float<class_float>`)
- `float<class_float>` **get_voice_depth_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The depth of the voice's low-frequency oscillator in milliseconds.

classref-item-separator

classref-property

`float<class_float>` **voice/2/level_db** = `0.0` `🔗<class_AudioEffectChorus_property_voice/2/level_db>`

classref-property-setget

- `void (No return value.)` **set_voice_level_db**(voice_idx: `int<class_int>`, level_db: `float<class_float>`)
- `float<class_float>` **get_voice_level_db**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The gain of the voice in dB.

classref-item-separator

classref-property

`float<class_float>` **voice/2/pan** = `0.5` `🔗<class_AudioEffectChorus_property_voice/2/pan>`

classref-property-setget

- `void (No return value.)` **set_voice_pan**(voice_idx: `int<class_int>`, pan: `float<class_float>`)
- `float<class_float>` **get_voice_pan**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The pan position of the voice.

classref-item-separator

classref-property

`float<class_float>` **voice/2/rate_hz** = `1.2` `🔗<class_AudioEffectChorus_property_voice/2/rate_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_rate_hz**(voice_idx: `int<class_int>`, rate_hz: `float<class_float>`)
- `float<class_float>` **get_voice_rate_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The rate of the voice's low-frequency oscillator in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/3/cutoff_hz** `🔗<class_AudioEffectChorus_property_voice/3/cutoff_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_cutoff_hz**(voice_idx: `int<class_int>`, cutoff_hz: `float<class_float>`)
- `float<class_float>` **get_voice_cutoff_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The frequency threshold of the voice's low-pass filter in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/3/delay_ms** `🔗<class_AudioEffectChorus_property_voice/3/delay_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_delay_ms**(voice_idx: `int<class_int>`, delay_ms: `float<class_float>`)
- `float<class_float>` **get_voice_delay_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The delay of the voice in milliseconds, compared to the original audio.

classref-item-separator

classref-property

`float<class_float>` **voice/3/depth_ms** `🔗<class_AudioEffectChorus_property_voice/3/depth_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_depth_ms**(voice_idx: `int<class_int>`, depth_ms: `float<class_float>`)
- `float<class_float>` **get_voice_depth_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The depth of the voice's low-frequency oscillator in milliseconds.

classref-item-separator

classref-property

`float<class_float>` **voice/3/level_db** `🔗<class_AudioEffectChorus_property_voice/3/level_db>`

classref-property-setget

- `void (No return value.)` **set_voice_level_db**(voice_idx: `int<class_int>`, level_db: `float<class_float>`)
- `float<class_float>` **get_voice_level_db**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The gain of the voice in dB.

classref-item-separator

classref-property

`float<class_float>` **voice/3/pan** `🔗<class_AudioEffectChorus_property_voice/3/pan>`

classref-property-setget

- `void (No return value.)` **set_voice_pan**(voice_idx: `int<class_int>`, pan: `float<class_float>`)
- `float<class_float>` **get_voice_pan**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The pan position of the voice.

classref-item-separator

classref-property

`float<class_float>` **voice/3/rate_hz** `🔗<class_AudioEffectChorus_property_voice/3/rate_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_rate_hz**(voice_idx: `int<class_int>`, rate_hz: `float<class_float>`)
- `float<class_float>` **get_voice_rate_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The rate of the voice's low-frequency oscillator in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/4/cutoff_hz** `🔗<class_AudioEffectChorus_property_voice/4/cutoff_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_cutoff_hz**(voice_idx: `int<class_int>`, cutoff_hz: `float<class_float>`)
- `float<class_float>` **get_voice_cutoff_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The frequency threshold of the voice's low-pass filter in Hz.

classref-item-separator

classref-property

`float<class_float>` **voice/4/delay_ms** `🔗<class_AudioEffectChorus_property_voice/4/delay_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_delay_ms**(voice_idx: `int<class_int>`, delay_ms: `float<class_float>`)
- `float<class_float>` **get_voice_delay_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The delay of the voice in milliseconds, compared to the original audio.

classref-item-separator

classref-property

`float<class_float>` **voice/4/depth_ms** `🔗<class_AudioEffectChorus_property_voice/4/depth_ms>`

classref-property-setget

- `void (No return value.)` **set_voice_depth_ms**(voice_idx: `int<class_int>`, depth_ms: `float<class_float>`)
- `float<class_float>` **get_voice_depth_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The depth of the voice's low-frequency oscillator in milliseconds.

classref-item-separator

classref-property

`float<class_float>` **voice/4/level_db** `🔗<class_AudioEffectChorus_property_voice/4/level_db>`

classref-property-setget

- `void (No return value.)` **set_voice_level_db**(voice_idx: `int<class_int>`, level_db: `float<class_float>`)
- `float<class_float>` **get_voice_level_db**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The gain of the voice in dB.

classref-item-separator

classref-property

`float<class_float>` **voice/4/pan** `🔗<class_AudioEffectChorus_property_voice/4/pan>`

classref-property-setget

- `void (No return value.)` **set_voice_pan**(voice_idx: `int<class_int>`, pan: `float<class_float>`)
- `float<class_float>` **get_voice_pan**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The pan position of the voice.

classref-item-separator

classref-property

`float<class_float>` **voice/4/rate_hz** `🔗<class_AudioEffectChorus_property_voice/4/rate_hz>`

classref-property-setget

- `void (No return value.)` **set_voice_rate_hz**(voice_idx: `int<class_int>`, rate_hz: `float<class_float>`)
- `float<class_float>` **get_voice_rate_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The rate of the voice's low-frequency oscillator in Hz.

classref-item-separator

classref-property

`int<class_int>` **voice_count** = `2` `🔗<class_AudioEffectChorus_property_voice_count>`

classref-property-setget

- `void (No return value.)` **set_voice_count**(value: `int<class_int>`)
- `int<class_int>` **get_voice_count**()

The number of voices in the effect. Value can range from 1 to 4.

classref-item-separator

classref-property

`float<class_float>` **wet** = `0.5` `🔗<class_AudioEffectChorus_property_wet>`

classref-property-setget

- `void (No return value.)` **set_wet**(value: `float<class_float>`)
- `float<class_float>` **get_wet**()

The volume ratio of all voices. Value can range from 0 to 1.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_voice_cutoff_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectChorus_method_get_voice_cutoff_hz>`

Returns the frequency threshold of a given `voice_idx`'s low-pass filter in Hz. Frequencies above this value are removed from the voice.

classref-item-separator

classref-method

`float<class_float>` **get_voice_delay_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectChorus_method_get_voice_delay_ms>`

Returns the delay of a given `voice_idx` in milliseconds, compared to the original audio.

classref-item-separator

classref-method

`float<class_float>` **get_voice_depth_ms**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectChorus_method_get_voice_depth_ms>`

Returns the depth of a given `voice_idx`'s low-frequency oscillator in milliseconds.

classref-item-separator

classref-method

`float<class_float>` **get_voice_level_db**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectChorus_method_get_voice_level_db>`

Returns the gain of a given `voice_idx` in dB.

classref-item-separator

classref-method

`float<class_float>` **get_voice_pan**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectChorus_method_get_voice_pan>`

Returns the pan position of a given `voice_idx`. Negative values mean the left channel, positive mean the right.

classref-item-separator

classref-method

`float<class_float>` **get_voice_rate_hz**(voice_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectChorus_method_get_voice_rate_hz>`

Returns the rate of a given `voice_idx`'s low-frequency oscillator in Hz.

classref-item-separator

classref-method

`void (No return value.)` **set_voice_cutoff_hz**(voice_idx: `int<class_int>`, cutoff_hz: `float<class_float>`) `🔗<class_AudioEffectChorus_method_set_voice_cutoff_hz>`

Sets the frequency threshold of a given `voice_idx`'s low-pass filter in Hz. Frequencies above `cutoff_hz` are removed from `voice_idx`. Value can range from 1 to 20500.

classref-item-separator

classref-method

`void (No return value.)` **set_voice_delay_ms**(voice_idx: `int<class_int>`, delay_ms: `float<class_float>`) `🔗<class_AudioEffectChorus_method_set_voice_delay_ms>`

Sets the delay of a given `voice_idx` in milliseconds, compared to the original audio. Value can range from 0 to 50.

classref-item-separator

classref-method

`void (No return value.)` **set_voice_depth_ms**(voice_idx: `int<class_int>`, depth_ms: `float<class_float>`) `🔗<class_AudioEffectChorus_method_set_voice_depth_ms>`

Sets the depth of a given `voice_idx`'s low-frequency oscillator in milliseconds. Value can range from 0 to 20.

classref-item-separator

classref-method

`void (No return value.)` **set_voice_level_db**(voice_idx: `int<class_int>`, level_db: `float<class_float>`) `🔗<class_AudioEffectChorus_method_set_voice_level_db>`

Sets the gain of a given `voice_idx` in dB. Value can range from -60 to 24.

classref-item-separator

classref-method

`void (No return value.)` **set_voice_pan**(voice_idx: `int<class_int>`, pan: `float<class_float>`) `🔗<class_AudioEffectChorus_method_set_voice_pan>`

Sets the pan position of a given `voice_idx`. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.

classref-item-separator

classref-method

`void (No return value.)` **set_voice_rate_hz**(voice_idx: `int<class_int>`, rate_hz: `float<class_float>`) `🔗<class_AudioEffectChorus_method_set_voice_rate_hz>`

Sets the rate of a given `voice_idx`'s low-frequency oscillator in Hz. Value can range from 0.1 to 20.