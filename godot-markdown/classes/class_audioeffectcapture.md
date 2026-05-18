github_url
hide

# AudioEffectCapture

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Exposes audio samples from an audio bus in real-time, such that it can be accessed as data.

classref-introduction-group

## Description

Copies all audio frames, also known as "samples" or "audio samples", from the attached audio bus into its internal ring buffer. This effect does not alter the audio. Can be used for storing real-time audio data for playback, and for creating real-time audio visualizations, like an oscilloscope.

Application code should consume these audio frames from this ring buffer using `get_buffer()<class_AudioEffectCapture_method_get_buffer>` and process it as needed, for example to capture data from an `AudioStreamMicrophone<class_AudioStreamMicrophone>`, implement application-defined effects, or to transmit audio over the network. When capturing audio data from a microphone, the format of the samples will be stereo 32-bit floating-point PCM.

Unlike `AudioEffectRecord<class_AudioEffectRecord>`, this effect only returns the raw audio samples instead of encoding them into an `AudioStream<class_AudioStream>`.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **buffer_length** = `0.1` `🔗<class_AudioEffectCapture_property_buffer_length>`

classref-property-setget

- `void (No return value.)` **set_buffer_length**(value: `float<class_float>`)
- `float<class_float>` **get_buffer_length**()

Length of the internal ring buffer, in seconds. Higher values keep data around for longer, but require more memory. Value can range from 0.01 to 10.

**Note:** Setting the buffer length will have no effect if already initialized.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **can_get_buffer**(frames: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectCapture_method_can_get_buffer>`

Returns `true` if at least `frames` samples are available to read in the internal ring buffer.

classref-item-separator

classref-method

`void (No return value.)` **clear_buffer**() `🔗<class_AudioEffectCapture_method_clear_buffer>`

Clears the internal ring buffer.

**Note:** Calling this during a capture can cause the loss of samples which causes popping in the playback.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **get_buffer**(frames: `int<class_int>`) `🔗<class_AudioEffectCapture_method_get_buffer>`

Gets the next `frames` samples from the internal ring buffer.

Returns a `PackedVector2Array<class_PackedVector2Array>` containing exactly `frames` samples if available, or an empty `PackedVector2Array<class_PackedVector2Array>` if insufficient data was available.

The samples are signed floating-point PCM between `-1` and `1`. You will have to scale them if you want to use them as 8 or 16-bit integer samples. (`v = 0x7fff * samples[0].x`)

classref-item-separator

classref-method

`int<class_int>` **get_buffer_length_frames**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectCapture_method_get_buffer_length_frames>`

Returns the total size of the internal ring buffer in number of samples.

classref-item-separator

classref-method

`int<class_int>` **get_discarded_frames**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectCapture_method_get_discarded_frames>`

Returns the number of samples discarded from the audio bus due to full buffer.

classref-item-separator

classref-method

`int<class_int>` **get_frames_available**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectCapture_method_get_frames_available>`

Returns the number of samples available to read using `get_buffer()<class_AudioEffectCapture_method_get_buffer>`.

classref-item-separator

classref-method

`int<class_int>` **get_pushed_frames**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectCapture_method_get_pushed_frames>`

Returns the number of samples inserted from the audio bus.