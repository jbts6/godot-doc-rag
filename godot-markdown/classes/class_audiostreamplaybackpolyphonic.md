github_url
hide

# AudioStreamPlaybackPolyphonic

**Inherits:** `AudioStreamPlayback<class_AudioStreamPlayback>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Playback instance for `AudioStreamPolyphonic<class_AudioStreamPolyphonic>`.

classref-introduction-group

## Description

Playback instance for `AudioStreamPolyphonic<class_AudioStreamPolyphonic>`. After setting the `stream` property of `AudioStreamPlayer<class_AudioStreamPlayer>`, `AudioStreamPlayer2D<class_AudioStreamPlayer2D>`, or `AudioStreamPlayer3D<class_AudioStreamPlayer3D>`, the playback instance can be obtained by calling `AudioStreamPlayer.get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>`, `AudioStreamPlayer2D.get_stream_playback()<class_AudioStreamPlayer2D_method_get_stream_playback>` or `AudioStreamPlayer3D.get_stream_playback()<class_AudioStreamPlayer3D_method_get_stream_playback>` methods.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**INVALID_ID** = `-1` `🔗<class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID>`

Returned by `play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>` in case it could not allocate a stream for playback.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_stream_playing**(stream: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlaybackPolyphonic_method_is_stream_playing>`

Returns `true` if the stream associated with the given integer ID is still playing. Check `play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>` for information on when this ID becomes invalid.

classref-item-separator

classref-method

`int<class_int>` **play_stream**(stream: `AudioStream<class_AudioStream>`, from_offset: `float<class_float>` = 0, volume_db: `float<class_float>` = 0, pitch_scale: `float<class_float>` = 1.0, playback_type: `PlaybackType<enum_AudioServer_PlaybackType>` = 0, bus: `StringName<class_StringName>` = &"Master") `🔗<class_AudioStreamPlaybackPolyphonic_method_play_stream>`

Play an `AudioStream<class_AudioStream>` at a given offset, volume, pitch scale, playback type, and bus. Playback starts immediately.

The return value is a unique integer ID that is associated to this playback stream and which can be used to control it.

This ID becomes invalid when the stream ends (if it does not loop), when the **AudioStreamPlaybackPolyphonic** is stopped, or when `stop_stream()<class_AudioStreamPlaybackPolyphonic_method_stop_stream>` is called.

This function returns `INVALID_ID<class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID>` if the amount of streams currently playing equals `AudioStreamPolyphonic.polyphony<class_AudioStreamPolyphonic_property_polyphony>`. If you need a higher amount of maximum polyphony, raise this value.

classref-item-separator

classref-method

`void (No return value.)` **set_stream_pitch_scale**(stream: `int<class_int>`, pitch_scale: `float<class_float>`) `🔗<class_AudioStreamPlaybackPolyphonic_method_set_stream_pitch_scale>`

Change the stream pitch scale. The `stream` argument is an integer ID returned by `play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`.

classref-item-separator

classref-method

`void (No return value.)` **set_stream_volume**(stream: `int<class_int>`, volume_db: `float<class_float>`) `🔗<class_AudioStreamPlaybackPolyphonic_method_set_stream_volume>`

Change the stream volume (in db). The `stream` argument is an integer ID returned by `play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`.

classref-item-separator

classref-method

`void (No return value.)` **stop_stream**(stream: `int<class_int>`) `🔗<class_AudioStreamPlaybackPolyphonic_method_stop_stream>`

Stop a stream. The `stream` argument is an integer ID returned by `play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>`, which becomes invalid after calling this function.