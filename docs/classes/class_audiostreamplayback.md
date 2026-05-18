github_url
hide

# AudioStreamPlayback

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AudioStreamPlaybackInteractive<class_AudioStreamPlaybackInteractive>`, `AudioStreamPlaybackPlaylist<class_AudioStreamPlaybackPlaylist>`, `AudioStreamPlaybackPolyphonic<class_AudioStreamPlaybackPolyphonic>`, `AudioStreamPlaybackResampled<class_AudioStreamPlaybackResampled>`, `AudioStreamPlaybackSynchronized<class_AudioStreamPlaybackSynchronized>`

Meta class for playing back audio.

classref-introduction-group

## Description

Can play, loop, pause a scroll through audio. See `AudioStream<class_AudioStream>` and `AudioStreamOggVorbis<class_AudioStreamOggVorbis>` for usage.

classref-introduction-group

## Tutorials

- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **\_get_loop_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_private_method__get_loop_count>`

Overridable method. Should return how many times this audio stream has looped. Most built-in playbacks always return `0`.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_get_parameter**(name: `StringName<class_StringName>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_private_method__get_parameter>`

Return the current value of a playback parameter by name (see `AudioStream._get_parameter_list()<class_AudioStream_private_method__get_parameter_list>`).

classref-item-separator

classref-method

`float<class_float>` **\_get_playback_position**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_private_method__get_playback_position>`

Overridable method. Should return the current progress along the audio stream, in seconds.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_playing**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_private_method__is_playing>`

Overridable method. Should return `true` if this playback is active and playing its audio stream.

classref-item-separator

classref-method

`int<class_int>` **\_mix**(buffer: `AudioFrame*`, rate_scale: `float<class_float>`, frames: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_AudioStreamPlayback_private_method__mix>`

Override this method to customize how the audio stream is mixed. This method is called even if the playback is not active.

**Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.

classref-item-separator

classref-method

`void (No return value.)` **\_seek**(position: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_AudioStreamPlayback_private_method__seek>`

Override this method to customize what happens when seeking this audio stream at the given `position`, such as by calling `AudioStreamPlayer.seek()<class_AudioStreamPlayer_method_seek>`.

classref-item-separator

classref-method

`void (No return value.)` **\_set_parameter**(name: `StringName<class_StringName>`, value: `Variant<class_Variant>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_AudioStreamPlayback_private_method__set_parameter>`

Set the current value of a playback parameter by name (see `AudioStream._get_parameter_list()<class_AudioStream_private_method__get_parameter_list>`).

classref-item-separator

classref-method

`void (No return value.)` **\_start**(from_pos: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_AudioStreamPlayback_private_method__start>`

Override this method to customize what happens when the playback starts at the given position, such as by calling `AudioStreamPlayer.play()<class_AudioStreamPlayer_method_play>`.

classref-item-separator

classref-method

`void (No return value.)` **\_stop**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_AudioStreamPlayback_private_method__stop>`

Override this method to customize what happens when the playback is stopped, such as by calling `AudioStreamPlayer.stop()<class_AudioStreamPlayer_method_stop>`.

classref-item-separator

classref-method

`void (No return value.)` **\_tag_used_streams**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_AudioStreamPlayback_private_method__tag_used_streams>`

Overridable method. Called whenever the audio stream is mixed if the playback is active and `AudioServer.set_enable_tagging_used_audio_streams()<class_AudioServer_method_set_enable_tagging_used_audio_streams>` has been set to `true`. Editor plugins may use this method to "tag" the current position along the audio stream and display it in a preview.

classref-item-separator

classref-method

`int<class_int>` **get_loop_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_method_get_loop_count>`

Returns the number of times the stream has looped.

classref-item-separator

classref-method

`float<class_float>` **get_playback_position**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_method_get_playback_position>`

Returns the current position in the stream, in seconds.

classref-item-separator

classref-method

`AudioSamplePlayback<class_AudioSamplePlayback>` **get_sample_playback**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_method_get_sample_playback>`

**Experimental:** This method may be changed or removed in future versions.

Returns the `AudioSamplePlayback<class_AudioSamplePlayback>` associated with this **AudioStreamPlayback** for playing back the audio sample of this stream.

classref-item-separator

classref-method

`bool<class_bool>` **is_playing**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlayback_method_is_playing>`

Returns `true` if the stream is playing.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **mix_audio**(rate_scale: `float<class_float>`, frames: `int<class_int>`) `🔗<class_AudioStreamPlayback_method_mix_audio>`

Mixes up to `frames` of audio from the stream from the current position, at a rate of `rate_scale`, advancing the stream.

Returns a `PackedVector2Array<class_PackedVector2Array>` where each element holds the left and right channel volume levels of each frame.

**Note:** Can return fewer frames than requested, make sure to use the size of the return value.

classref-item-separator

classref-method

`void (No return value.)` **seek**(time: `float<class_float>` = 0.0) `🔗<class_AudioStreamPlayback_method_seek>`

Seeks the stream at the given `time`, in seconds.

classref-item-separator

classref-method

`void (No return value.)` **set_sample_playback**(playback_sample: `AudioSamplePlayback<class_AudioSamplePlayback>`) `🔗<class_AudioStreamPlayback_method_set_sample_playback>`

**Experimental:** This method may be changed or removed in future versions.

Associates `AudioSamplePlayback<class_AudioSamplePlayback>` to this **AudioStreamPlayback** for playing back the audio sample of this stream.

classref-item-separator

classref-method

`void (No return value.)` **start**(from_pos: `float<class_float>` = 0.0) `🔗<class_AudioStreamPlayback_method_start>`

Starts the stream from the given `from_pos`, in seconds.

classref-item-separator

classref-method

`void (No return value.)` **stop**() `🔗<class_AudioStreamPlayback_method_stop>`

Stops the stream.