github_url
hide

# AudioEffectFilter

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AudioEffectBandLimitFilter<class_AudioEffectBandLimitFilter>`, `AudioEffectBandPassFilter<class_AudioEffectBandPassFilter>`, `AudioEffectHighPassFilter<class_AudioEffectHighPassFilter>`, `AudioEffectHighShelfFilter<class_AudioEffectHighShelfFilter>`, `AudioEffectLowPassFilter<class_AudioEffectLowPassFilter>`, `AudioEffectLowShelfFilter<class_AudioEffectLowShelfFilter>`, `AudioEffectNotchFilter<class_AudioEffectNotchFilter>`

Base class for filters. Use effects that inherit this class instead of using it directly.

classref-introduction-group

## Description

A "filter" controls the gain of frequencies, using `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` as a frequency threshold. Filters can help to give room for each sound, and create interesting effects.

There are different types of filter that inherit this class:

Shelf filters: `AudioEffectLowShelfFilter<class_AudioEffectLowShelfFilter>` and `AudioEffectHighShelfFilter<class_AudioEffectHighShelfFilter>`

Band-pass and notch filters: `AudioEffectBandPassFilter<class_AudioEffectBandPassFilter>`, `AudioEffectBandLimitFilter<class_AudioEffectBandLimitFilter>`, and `AudioEffectNotchFilter<class_AudioEffectNotchFilter>`

Low/high-pass filters: `AudioEffectLowPassFilter<class_AudioEffectLowPassFilter>` and `AudioEffectHighPassFilter<class_AudioEffectHighPassFilter>`

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FilterDB**: `🔗<enum_AudioEffectFilter_FilterDB>`

classref-enumeration-constant

`FilterDB<enum_AudioEffectFilter_FilterDB>` **FILTER_6DB** = `0`

Cutting off at 6 dB per octave. One octave is twice the frequency above `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`, or half the frequency below `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`.

classref-enumeration-constant

`FilterDB<enum_AudioEffectFilter_FilterDB>` **FILTER_12DB** = `1`

Cutting off at 12 dB per octave. One octave is twice the frequency above `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`, or half the frequency below `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`.

classref-enumeration-constant

`FilterDB<enum_AudioEffectFilter_FilterDB>` **FILTER_18DB** = `2`

Cutting off at 18 dB per octave. One octave is twice the frequency above `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`, or half the frequency below `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`.

classref-enumeration-constant

`FilterDB<enum_AudioEffectFilter_FilterDB>` **FILTER_24DB** = `3`

Cutting off at 24 dB per octave. One octave is twice the frequency above `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`, or half the frequency below `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **cutoff_hz** = `2000.0` `🔗<class_AudioEffectFilter_property_cutoff_hz>`

classref-property-setget

- `void (No return value.)` **set_cutoff**(value: `float<class_float>`)
- `float<class_float>` **get_cutoff**()

Frequency threshold for the filter, in Hz. Value can range from 1 to 20500.

classref-item-separator

classref-property

`FilterDB<enum_AudioEffectFilter_FilterDB>` **db** = `0` `🔗<class_AudioEffectFilter_property_db>`

classref-property-setget

- `void (No return value.)` **set_db**(value: `FilterDB<enum_AudioEffectFilter_FilterDB>`)
- `FilterDB<enum_AudioEffectFilter_FilterDB>` **get_db**()

Steepness of the cutoff curve in dB per octave (twice the frequency above `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`, or half the frequency below `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>`), also known as the "order" of the filter. Higher orders have a more aggressive cutoff.

classref-item-separator

classref-property

`float<class_float>` **gain** = `1.0` `🔗<class_AudioEffectFilter_property_gain>`

classref-property-setget

- `void (No return value.)` **set_gain**(value: `float<class_float>`)
- `float<class_float>` **get_gain**()

Gain of the frequencies affected by the filter. This property is only available for `AudioEffectLowShelfFilter<class_AudioEffectLowShelfFilter>` and `AudioEffectHighShelfFilter<class_AudioEffectHighShelfFilter>`. Value can range from 0 to 4.

classref-item-separator

classref-property

`float<class_float>` **resonance** = `0.5` `🔗<class_AudioEffectFilter_property_resonance>`

classref-property-setget

- `void (No return value.)` **set_resonance**(value: `float<class_float>`)
- `float<class_float>` **get_resonance**()

Gain at or directly next to the `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` frequency threshold. Value can range from 0 to 1.

Its exact behavior depends on the selected filter type:

- For shelf filters, it accentuates or masks the order by increasing frequencies right next to the `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` frequency and decreasing frequencies on the opposite side.
- For the band-pass and notch filters, it widens or narrows the filter at the `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` frequency threshold.
- For low/high-pass filters, it increases or decreases frequencies at the `cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` frequency threshold.