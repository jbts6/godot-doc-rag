github_url
hide

# AudioStreamPlaylist

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

`AudioStream<class_AudioStream>` that includes sub-streams and plays them back like a playlist.

classref-introduction-group

## Description

An audio stream that can play back sub-streams in sequence. Streams can be added to the Playlist with `set_list_stream()<class_AudioStreamPlaylist_method_set_list_stream>`, and shuffled with `shuffle<class_AudioStreamPlaylist_property_shuffle>`.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**MAX_STREAMS** = `64` `🔗<class_AudioStreamPlaylist_constant_MAX_STREAMS>`

Maximum amount of streams supported in the playlist.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **fade_time** = `0.3` `🔗<class_AudioStreamPlaylist_property_fade_time>`

classref-property-setget

- `void (No return value.)` **set_fade_time**(value: `float<class_float>`)
- `float<class_float>` **get_fade_time**()

Fade time used when a stream ends, when going to the next one. Streams are expected to have an extra bit of audio after the end to help with fading.

classref-item-separator

classref-property

`bool<class_bool>` **loop** = `true` `🔗<class_AudioStreamPlaylist_property_loop>`

classref-property-setget

- `void (No return value.)` **set_loop**(value: `bool<class_bool>`)
- `bool<class_bool>` **has_loop**()

If `true`, the playlist will loop, otherwise the playlist will end when the last stream is finished.

classref-item-separator

classref-property

`bool<class_bool>` **shuffle** = `false` `🔗<class_AudioStreamPlaylist_property_shuffle>`

classref-property-setget

- `void (No return value.)` **set_shuffle**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_shuffle**()

If `true`, the playlist will shuffle each time playback starts and each time it loops.

classref-item-separator

classref-property

`int<class_int>` **stream_count** = `0` `🔗<class_AudioStreamPlaylist_property_stream_count>`

classref-property-setget

- `void (No return value.)` **set_stream_count**(value: `int<class_int>`)
- `int<class_int>` **get_stream_count**()

Amount of streams in the playlist.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_bpm**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlaylist_method_get_bpm>`

Returns the BPM of the playlist, which can vary depending on the clip being played.

classref-item-separator

classref-method

`AudioStream<class_AudioStream>` **get_list_stream**(stream_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlaylist_method_get_list_stream>`

Returns the stream at playback position index.

classref-item-separator

classref-method

`void (No return value.)` **set_list_stream**(stream_index: `int<class_int>`, audio_stream: `AudioStream<class_AudioStream>`) `🔗<class_AudioStreamPlaylist_method_set_list_stream>`

Sets the stream at playback position index.