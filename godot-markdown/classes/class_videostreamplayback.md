github_url
hide

# VideoStreamPlayback

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Internal class used by `VideoStream<class_VideoStream>` to manage playback state when played from a `VideoStreamPlayer<class_VideoStreamPlayer>`.

classref-introduction-group

## Description

This class is intended to be overridden by video decoder extensions with custom implementations of `VideoStream<class_VideoStream>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **\_get_channels**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__get_channels>`

Returns the number of audio channels.

classref-item-separator

classref-method

`float<class_float>` **\_get_length**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__get_length>`

Returns the video duration in seconds, if known, or 0 if unknown.

classref-item-separator

classref-method

`int<class_int>` **\_get_mix_rate**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__get_mix_rate>`

Returns the audio sample rate used for mixing.

classref-item-separator

classref-method

`float<class_float>` **\_get_playback_position**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__get_playback_position>`

Return the current playback timestamp. Called in response to the `VideoStreamPlayer.stream_position<class_VideoStreamPlayer_property_stream_position>` getter.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **\_get_texture**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__get_texture>`

Allocates a `Texture2D<class_Texture2D>` in which decoded video frames will be drawn.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_paused**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__is_paused>`

Returns the paused status, as set by `_set_paused()<class_VideoStreamPlayback_private_method__set_paused>`.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_playing**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VideoStreamPlayback_private_method__is_playing>`

Returns the playback state, as determined by calls to `_play()<class_VideoStreamPlayback_private_method__play>` and `_stop()<class_VideoStreamPlayback_private_method__stop>`.

classref-item-separator

classref-method

`void (No return value.)` **\_play**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_VideoStreamPlayback_private_method__play>`

Called in response to `VideoStreamPlayer.autoplay<class_VideoStreamPlayer_property_autoplay>` or `VideoStreamPlayer.play()<class_VideoStreamPlayer_method_play>`. Note that manual playback may also invoke `_stop()<class_VideoStreamPlayback_private_method__stop>` multiple times before this method is called. `_is_playing()<class_VideoStreamPlayback_private_method__is_playing>` should return `true` once playing.

classref-item-separator

classref-method

`void (No return value.)` **\_seek**(time: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_VideoStreamPlayback_private_method__seek>`

Seeks to `time` seconds. Called in response to the `VideoStreamPlayer.stream_position<class_VideoStreamPlayer_property_stream_position>` setter.

classref-item-separator

classref-method

`void (No return value.)` **\_set_audio_track**(idx: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_VideoStreamPlayback_private_method__set_audio_track>`

Select the audio track `idx`. Called when playback starts, and in response to the `VideoStreamPlayer.audio_track<class_VideoStreamPlayer_property_audio_track>` setter.

classref-item-separator

classref-method

`void (No return value.)` **\_set_paused**(paused: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_VideoStreamPlayback_private_method__set_paused>`

Set the paused status of video playback. `_is_paused()<class_VideoStreamPlayback_private_method__is_paused>` must return `paused`. Called in response to the `VideoStreamPlayer.paused<class_VideoStreamPlayer_property_paused>` setter.

classref-item-separator

classref-method

`void (No return value.)` **\_stop**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_VideoStreamPlayback_private_method__stop>`

Stops playback. May be called multiple times before `_play()<class_VideoStreamPlayback_private_method__play>`, or in response to `VideoStreamPlayer.stop()<class_VideoStreamPlayer_method_stop>`. `_is_playing()<class_VideoStreamPlayback_private_method__is_playing>` should return `false` once stopped.

classref-item-separator

classref-method

`void (No return value.)` **\_update**(delta: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_VideoStreamPlayback_private_method__update>`

Ticks video playback for `delta` seconds. Called every frame as long as both `_is_paused()<class_VideoStreamPlayback_private_method__is_paused>` and `_is_playing()<class_VideoStreamPlayback_private_method__is_playing>` return `true`.

classref-item-separator

classref-method

`int<class_int>` **mix_audio**(num_frames: `int<class_int>`, buffer: `PackedFloat32Array<class_PackedFloat32Array>` = PackedFloat32Array(), offset: `int<class_int>` = 0) `🔗<class_VideoStreamPlayback_method_mix_audio>`

Render `num_frames` audio frames (of `_get_channels()<class_VideoStreamPlayback_private_method__get_channels>` floats each) from `buffer`, starting from index `offset` in the array. Returns the number of audio frames rendered, or -1 on error.