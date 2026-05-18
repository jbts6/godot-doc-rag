github_url
hide

# AudioEffectCompressor

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a downward compressor audio effect to an audio bus.

Allows control of the dynamic range via a volume threshold and timing controls.

classref-introduction-group

## Description

A "compressor" decreases the volume of sounds when it exceeds a certain volume threshold level.

A compressor can have many uses in a mix:

- To compress the whole volume in the Master bus (although an `AudioEffectHardLimiter<class_AudioEffectHardLimiter>` is probably better).
- To ensure balance of voice audio clips.
- To sidechain, using another bus as a trigger. This decreases the volume of the bus it is attached to, by using the volume from another audio bus for threshold detection. This technique is common in video game mixing to decrease the volume of music and SFX while voices are being heard. This effect is also known as "ducking".
- To accentuate transients by using a long attack, letting sounds exceed the volume threshold level for a short period before compressing them. This can be used to make SFX more punchy.

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

`float<class_float>` **attack_us** = `20.0` `🔗<class_AudioEffectCompressor_property_attack_us>`

classref-property-setget

- `void (No return value.)` **set_attack_us**(value: `float<class_float>`)
- `float<class_float>` **get_attack_us**()

Compressor's reaction time when the audio exceeds the volume threshold level, in microseconds. Value can range from 20 to 2000.

classref-item-separator

classref-property

`float<class_float>` **gain** = `0.0` `🔗<class_AudioEffectCompressor_property_gain>`

classref-property-setget

- `void (No return value.)` **set_gain**(value: `float<class_float>`)
- `float<class_float>` **get_gain**()

Gain of the audio signal, in dB. Value can range from -20 to 20.

classref-item-separator

classref-property

`float<class_float>` **mix** = `1.0` `🔗<class_AudioEffectCompressor_property_mix>`

classref-property-setget

- `void (No return value.)` **set_mix**(value: `float<class_float>`)
- `float<class_float>` **get_mix**()

Balance between the original audio and the compressed audio. Value can range from 0 (totally dry) to 1 (totally wet).

classref-item-separator

classref-property

`float<class_float>` **ratio** = `4.0` `🔗<class_AudioEffectCompressor_property_ratio>`

classref-property-setget

- `void (No return value.)` **set_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_ratio**()

Amount of compression applied to the audio once it passes the volume threshold level. The higher the ratio, the stronger the compression applied to audio signals that pass the volume threshold level. Value can range from 1 to 48.

classref-item-separator

classref-property

`float<class_float>` **release_ms** = `250.0` `🔗<class_AudioEffectCompressor_property_release_ms>`

classref-property-setget

- `void (No return value.)` **set_release_ms**(value: `float<class_float>`)
- `float<class_float>` **get_release_ms**()

Compressor's delay time to stop decreasing the volume after the it falls below the volume threshold level, in milliseconds. Value can range from 20 to 2000.

classref-item-separator

classref-property

`StringName<class_StringName>` **sidechain** = `&""` `🔗<class_AudioEffectCompressor_property_sidechain>`

classref-property-setget

- `void (No return value.)` **set_sidechain**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_sidechain**()

Audio bus to use for the volume threshold detection.

classref-item-separator

classref-property

`float<class_float>` **threshold** = `0.0` `🔗<class_AudioEffectCompressor_property_threshold>`

classref-property-setget

- `void (No return value.)` **set_threshold**(value: `float<class_float>`)
- `float<class_float>` **get_threshold**()

The volume level above which compression is applied to the audio, in dB. Value can range from -60 to 0.