github_url
hide

# AudioEffectEQ

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AudioEffectEQ10<class_AudioEffectEQ10>`, `AudioEffectEQ21<class_AudioEffectEQ21>`, `AudioEffectEQ6<class_AudioEffectEQ6>`

Base class for audio equalizers (EQ). Gives you control over frequencies.

Use it to create a custom equalizer if `AudioEffectEQ6<class_AudioEffectEQ6>`, `AudioEffectEQ10<class_AudioEffectEQ10>`, or `AudioEffectEQ21<class_AudioEffectEQ21>` don't fit your needs.

classref-introduction-group

## Description

An "equalizer" gives you control over the gain of frequencies in the entire spectrum, by allowing their adjustment through bands. A band is a point in the frequency spectrum, and each band means a division of the spectrum that can be adjusted.

Use equalizers to compensate for existing deficiencies in the audio, make room for other elements, or remove undesirable frequencies. AudioEffectEQs are useful on the Master bus to balance the entire mix or give it more character. They are also useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be disabled when headphones are plugged in).

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_band_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectEQ_method_get_band_count>`

Returns the number of bands of the equalizer.

classref-item-separator

classref-method

`float<class_float>` **get_band_gain_db**(band_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectEQ_method_get_band_gain_db>`

Returns the band's gain at the specified index, in dB.

classref-item-separator

classref-method

`void (No return value.)` **set_band_gain_db**(band_idx: `int<class_int>`, volume_db: `float<class_float>`) `🔗<class_AudioEffectEQ_method_set_band_gain_db>`

Sets band's gain at the specified index, in dB.