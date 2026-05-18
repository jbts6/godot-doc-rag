github_url
hide

# AudioEffectPhaser

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a phaser audio effect to an audio bus.

Creates several notch and peak filters that sweep across the spectrum.

classref-introduction-group

## Description

A "phaser" effect creates a copy of the original audio that phase-rotates differently across the entire frequency spectrum, with the use of a series of all-pass filter stages (6 in this effect). This copy modulates with a low-frequency oscillator and combines with the original audio, resulting in peaks and troughs that sweep across the spectrum.

This effect can be used to create a "glassy" or "bubbly" sound.

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

`float<class_float>` **depth** = `1.0` `🔗<class_AudioEffectPhaser_property_depth>`

classref-property-setget

- `void (No return value.)` **set_depth**(value: `float<class_float>`)
- `float<class_float>` **get_depth**()

Intensity of the effect. Value can range from 0.1 to 4.0.

classref-item-separator

classref-property

`float<class_float>` **feedback** = `0.7` `🔗<class_AudioEffectPhaser_property_feedback>`

classref-property-setget

- `void (No return value.)` **set_feedback**(value: `float<class_float>`)
- `float<class_float>` **get_feedback**()

The volume ratio of the filtered audio that is fed back to the all-pass filters. The higher the value, the sharper and louder the peak filters created by the effect. Value can range from 0.1 to 0.9.

classref-item-separator

classref-property

`float<class_float>` **range_max_hz** = `1600.0` `🔗<class_AudioEffectPhaser_property_range_max_hz>`

classref-property-setget

- `void (No return value.)` **set_range_max_hz**(value: `float<class_float>`)
- `float<class_float>` **get_range_max_hz**()

Determines the maximum frequency affected by the low-frequency oscillator modulations, in Hz. Value can range from 10 to 10000.

classref-item-separator

classref-property

`float<class_float>` **range_min_hz** = `440.0` `🔗<class_AudioEffectPhaser_property_range_min_hz>`

classref-property-setget

- `void (No return value.)` **set_range_min_hz**(value: `float<class_float>`)
- `float<class_float>` **get_range_min_hz**()

Determines the minimum frequency affected by the low-frequency oscillator modulations, in Hz. Value can range from 10 to 10000.

classref-item-separator

classref-property

`float<class_float>` **rate_hz** = `0.5` `🔗<class_AudioEffectPhaser_property_rate_hz>`

classref-property-setget

- `void (No return value.)` **set_rate_hz**(value: `float<class_float>`)
- `float<class_float>` **get_rate_hz**()

Adjusts the rate in Hz at which the effect sweeps up and down across the frequency range. Value can range from 0.01 to 20.