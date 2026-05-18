github_url
hide

# AudioStreamRandomizer

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Wraps a pool of audio streams with pitch and volume shifting.

classref-introduction-group

## Description

Picks a random AudioStream from the pool, depending on the playback mode, and applies random pitch shifting and volume shifting during playback.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **PlaybackMode**: `🔗<enum_AudioStreamRandomizer_PlaybackMode>`

classref-enumeration-constant

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>` **PLAYBACK_RANDOM_NO_REPEATS** = `0`

Pick a stream at random according to the probability weights chosen for each stream, but avoid playing the same stream twice in a row whenever possible. If only 1 sound is present in the pool, the same sound will always play, effectively allowing repeats to occur.

classref-enumeration-constant

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>` **PLAYBACK_RANDOM** = `1`

Pick a stream at random according to the probability weights chosen for each stream. If only 1 sound is present in the pool, the same sound will always play.

classref-enumeration-constant

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>` **PLAYBACK_SEQUENTIAL** = `2`

Play streams in the order they appear in the stream pool. If only 1 sound is present in the pool, the same sound will always play.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>` **playback_mode** = `0` `🔗<class_AudioStreamRandomizer_property_playback_mode>`

classref-property-setget

- `void (No return value.)` **set_playback_mode**(value: `PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>`)
- `PlaybackMode<enum_AudioStreamRandomizer_PlaybackMode>` **get_playback_mode**()

Controls how this AudioStreamRandomizer picks which AudioStream to play next.

classref-item-separator

classref-property

`float<class_float>` **random_pitch** = `1.0` `🔗<class_AudioStreamRandomizer_property_random_pitch>`

classref-property-setget

- `void (No return value.)` **set_random_pitch**(value: `float<class_float>`)
- `float<class_float>` **get_random_pitch**()

The largest possible frequency multiplier of the random pitch variation. Pitch will be randomly chosen within a range of `1.0 / random_pitch` and `random_pitch`. A value of `1.0` means no variation. A value of `2.0` means pitch will be randomized between double and half.

**Note:** Setting this property also sets `random_pitch_semitones<class_AudioStreamRandomizer_property_random_pitch_semitones>`.

classref-item-separator

classref-property

`float<class_float>` **random_pitch_semitones** = `0.0` `🔗<class_AudioStreamRandomizer_property_random_pitch_semitones>`

classref-property-setget

- `void (No return value.)` **set_random_pitch_semitones**(value: `float<class_float>`)
- `float<class_float>` **get_random_pitch_semitones**()

The largest possible distance, in semitones, of the random pitch variation. A value of `0.0` means no variation.

**Note:** Setting this property also sets `random_pitch<class_AudioStreamRandomizer_property_random_pitch>`.

classref-item-separator

classref-property

`float<class_float>` **random_volume_offset_db** = `0.0` `🔗<class_AudioStreamRandomizer_property_random_volume_offset_db>`

classref-property-setget

- `void (No return value.)` **set_random_volume_offset_db**(value: `float<class_float>`)
- `float<class_float>` **get_random_volume_offset_db**()

The intensity of random volume variation. Volume will be increased or decreased by a random value up to `random_volume_offset_db`. A value of `0.0` means no variation. A value of `3.0` means volume will be randomized between `-3.0 dB` and `+3.0 dB`.

classref-item-separator

classref-property

`AudioStream<class_AudioStream>` **stream\_{index}/stream** `🔗<class_AudioStreamRandomizer_property_stream_{index}/stream>`

The `AudioStream<class_AudioStream>` at `index`.

**Note:** `index` is a value in the `0 .. streams_count - 1` range.

classref-item-separator

classref-property

`float<class_float>` **stream\_{index}/weight** = `1.0` `🔗<class_AudioStreamRandomizer_property_stream_{index}/weight>`

The probability weight of the `AudioStream<class_AudioStream>` at `index`.

**Note:** `index` is a value in the `0 .. streams_count - 1` range.

classref-item-separator

classref-property

`int<class_int>` **streams_count** = `0` `🔗<class_AudioStreamRandomizer_property_streams_count>`

classref-property-setget

- `void (No return value.)` **set_streams_count**(value: `int<class_int>`)
- `int<class_int>` **get_streams_count**()

The number of streams in the stream pool.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_stream**(index: `int<class_int>`, stream: `AudioStream<class_AudioStream>`, weight: `float<class_float>` = 1.0) `🔗<class_AudioStreamRandomizer_method_add_stream>`

Insert a stream at the specified index. If the index is less than zero, the insertion occurs at the end of the underlying pool.

classref-item-separator

classref-method

`AudioStream<class_AudioStream>` **get_stream**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamRandomizer_method_get_stream>`

Returns the stream at the specified index.

classref-item-separator

classref-method

`float<class_float>` **get_stream_probability_weight**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamRandomizer_method_get_stream_probability_weight>`

Returns the probability weight associated with the stream at the given index.

classref-item-separator

classref-method

`void (No return value.)` **move_stream**(index_from: `int<class_int>`, index_to: `int<class_int>`) `🔗<class_AudioStreamRandomizer_method_move_stream>`

Move a stream from one index to another.

classref-item-separator

classref-method

`void (No return value.)` **remove_stream**(index: `int<class_int>`) `🔗<class_AudioStreamRandomizer_method_remove_stream>`

Remove the stream at the specified index.

classref-item-separator

classref-method

`void (No return value.)` **set_stream**(index: `int<class_int>`, stream: `AudioStream<class_AudioStream>`) `🔗<class_AudioStreamRandomizer_method_set_stream>`

Set the AudioStream at the specified index.

classref-item-separator

classref-method

`void (No return value.)` **set_stream_probability_weight**(index: `int<class_int>`, weight: `float<class_float>`) `🔗<class_AudioStreamRandomizer_method_set_stream_probability_weight>`

Set the probability weight of the stream at the specified index. The higher this value, the more likely that the randomizer will choose this stream during random playback modes.