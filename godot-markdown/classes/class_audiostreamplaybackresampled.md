github_url
hide

# AudioStreamPlaybackResampled

**Inherits:** `AudioStreamPlayback<class_AudioStreamPlayback>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AudioStreamGeneratorPlayback<class_AudioStreamGeneratorPlayback>`, `AudioStreamPlaybackOggVorbis<class_AudioStreamPlaybackOggVorbis>`

Playback class used for resampled `AudioStream<class_AudioStream>`s.

classref-introduction-group

## Description

Playback class used to mix an `AudioStream<class_AudioStream>`'s audio samples to `AudioServer.get_mix_rate()<class_AudioServer_method_get_mix_rate>` using cubic interpolation.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **\_get_stream_sampling_rate**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlaybackResampled_private_method__get_stream_sampling_rate>`

Returns an `AudioStream<class_AudioStream>`'s sample rate, in Hz. Used to perform resampling.

classref-item-separator

classref-method

`int<class_int>` **\_mix_resampled**(dst_buffer: `AudioFrame*`, frame_count: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_AudioStreamPlaybackResampled_private_method__mix_resampled>`

Called by `begin_resample()<class_AudioStreamPlaybackResampled_method_begin_resample>` to mix an `AudioStream<class_AudioStream>` to `AudioServer.get_mix_rate()<class_AudioServer_method_get_mix_rate>`. Uses `_get_stream_sampling_rate()<class_AudioStreamPlaybackResampled_private_method__get_stream_sampling_rate>` as the source sample rate. Returns the number of mixed frames.

classref-item-separator

classref-method

`void (No return value.)` **begin_resample**() `🔗<class_AudioStreamPlaybackResampled_method_begin_resample>`

Called when an `AudioStream<class_AudioStream>` is played. Clears the cubic interpolation history and starts mixing by calling `_mix_resampled()<class_AudioStreamPlaybackResampled_private_method__mix_resampled>`.