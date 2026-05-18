github_url
hide

# AudioEffectRecord

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Audio effect used for recording the sound from an audio bus.

classref-introduction-group

## Description

Allows the user to record the sound from an audio bus into an `AudioStreamWAV<class_AudioStreamWAV>`. When used on the Master audio bus, this includes all audio output by Godot.

Unlike `AudioEffectCapture<class_AudioEffectCapture>`, this effect encodes the recording with the given format (8-bit, 16-bit, or compressed) instead of giving access to the raw audio samples.

Can be used (with an `AudioStreamMicrophone<class_AudioStreamMicrophone>`) to record from a microphone.

**Note:** `ProjectSettings.audio/driver/enable_input<class_ProjectSettings_property_audio/driver/enable_input>` must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.

classref-introduction-group

## Tutorials

- `Recording with microphone <../tutorials/audio/recording_with_microphone>`
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Format<enum_AudioStreamWAV_Format>` **format** = `1` `🔗<class_AudioEffectRecord_property_format>`

classref-property-setget

- `void (No return value.)` **set_format**(value: `Format<enum_AudioStreamWAV_Format>`)
- `Format<enum_AudioStreamWAV_Format>` **get_format**()

Specifies the format in which the sample will be recorded.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AudioStreamWAV<class_AudioStreamWAV>` **get_recording**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectRecord_method_get_recording>`

Returns the recorded sample.

classref-item-separator

classref-method

`bool<class_bool>` **is_recording_active**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioEffectRecord_method_is_recording_active>`

Returns whether the recording is active or not.

classref-item-separator

classref-method

`void (No return value.)` **set_recording_active**(record: `bool<class_bool>`) `🔗<class_AudioEffectRecord_method_set_recording_active>`

If `true`, the sound will be recorded. Note that restarting the recording will remove the previously recorded sample.