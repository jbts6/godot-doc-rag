github_url
hide

# AudioStream

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AudioStreamGenerator<class_AudioStreamGenerator>`, `AudioStreamInteractive<class_AudioStreamInteractive>`, `AudioStreamMicrophone<class_AudioStreamMicrophone>`, `AudioStreamMP3<class_AudioStreamMP3>`, `AudioStreamOggVorbis<class_AudioStreamOggVorbis>`, `AudioStreamPlaylist<class_AudioStreamPlaylist>`, `AudioStreamPolyphonic<class_AudioStreamPolyphonic>`, `AudioStreamRandomizer<class_AudioStreamRandomizer>`, `AudioStreamSynchronized<class_AudioStreamSynchronized>`, `AudioStreamWAV<class_AudioStreamWAV>`

Base class for audio streams.

classref-introduction-group

## Description

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via `AudioStreamWAV<class_AudioStreamWAV>`), Ogg (via `AudioStreamOggVorbis<class_AudioStreamOggVorbis>`), and MP3 (via `AudioStreamMP3<class_AudioStreamMP3>`) file formats.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`
- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**parameter_list_changed**() `🔗<class_AudioStream_signal_parameter_list_changed>`

Signal to be emitted to notify when the parameter list changed.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **\_get_bar_beats**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_bar_beats>`

Override this method to return the bar beats of this stream.

classref-item-separator

classref-method

`int<class_int>` **\_get_beat_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_beat_count>`

Overridable method. Should return the total number of beats of this audio stream. Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate (`AudioStreamWAV.mix_rate<class_AudioStreamWAV_property_mix_rate>`, for example).

classref-item-separator

classref-method

`float<class_float>` **\_get_bpm**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_bpm>`

Overridable method. Should return the tempo of this audio stream, in beats per minute (BPM). Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate (`AudioStreamWAV.mix_rate<class_AudioStreamWAV_property_mix_rate>`, for example).

classref-item-separator

classref-method

`float<class_float>` **\_get_length**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_length>`

Override this method to customize the returned value of `get_length()<class_AudioStream_method_get_length>`. Should return the length of this audio stream, in seconds.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_get_parameter_list**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_parameter_list>`

Return the controllable parameters of this stream. This array contains dictionaries with a property info description format (see `Object.get_property_list()<class_Object_method_get_property_list>`). Additionally, the default value for this parameter must be added tho each dictionary in "default_value" field.

classref-item-separator

classref-method

`String<class_String>` **\_get_stream_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_stream_name>`

Override this method to customize the name assigned to this audio stream. Unused by the engine.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **\_get_tags**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__get_tags>`

Override this method to customize the tags for this audio stream. Should return a `Dictionary<class_Dictionary>` of strings with the tag as the key and its content as the value.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date`.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_loop**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__has_loop>`

Override this method to return `true` if this stream has a loop.

classref-item-separator

classref-method

`AudioStreamPlayback<class_AudioStreamPlayback>` **\_instantiate_playback**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__instantiate_playback>`

Override this method to customize the returned value of `instantiate_playback()<class_AudioStream_method_instantiate_playback>`. Should return a new `AudioStreamPlayback<class_AudioStreamPlayback>` created when the stream is played (such as by an `AudioStreamPlayer<class_AudioStreamPlayer>`).

classref-item-separator

classref-method

`bool<class_bool>` **\_is_monophonic**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_private_method__is_monophonic>`

Override this method to customize the returned value of `is_monophonic()<class_AudioStream_method_is_monophonic>`. Should return `true` if this audio stream only supports one channel.

classref-item-separator

classref-method

`bool<class_bool>` **can_be_sampled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_method_can_be_sampled>`

**Experimental:** This method may be changed or removed in future versions.

Returns if the current **AudioStream** can be used as a sample. Only static streams can be sampled.

classref-item-separator

classref-method

`AudioSample<class_AudioSample>` **generate_sample**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_method_generate_sample>`

**Experimental:** This method may be changed or removed in future versions.

Generates an `AudioSample<class_AudioSample>` based on the current stream.

classref-item-separator

classref-method

`float<class_float>` **get_length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_method_get_length>`

Returns the length of the audio stream in seconds. If this stream is an `AudioStreamRandomizer<class_AudioStreamRandomizer>`, returns the length of the last played stream. If this stream has an indefinite length (such as for `AudioStreamGenerator<class_AudioStreamGenerator>` and `AudioStreamMicrophone<class_AudioStreamMicrophone>`), returns `0.0`.

classref-item-separator

classref-method

`AudioStreamPlayback<class_AudioStreamPlayback>` **instantiate_playback**() `🔗<class_AudioStream_method_instantiate_playback>`

Returns a newly created `AudioStreamPlayback<class_AudioStreamPlayback>` intended to play this audio stream. Useful for when you want to extend `_instantiate_playback()<class_AudioStream_private_method__instantiate_playback>` but call `instantiate_playback()<class_AudioStream_method_instantiate_playback>` from an internally held AudioStream subresource. An example of this can be found in the source code for `AudioStreamRandomPitch::instantiate_playback`.

classref-item-separator

classref-method

`bool<class_bool>` **is_meta_stream**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_method_is_meta_stream>`

Returns `true` if the stream is a collection of other streams, `false` otherwise.

classref-item-separator

classref-method

`bool<class_bool>` **is_monophonic**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStream_method_is_monophonic>`

Returns `true` if this audio stream only supports one channel (*monophony*), or `false` if the audio stream supports two or more channels (*polyphony*).