github_url
hide

# ResourceImporterMP3

**Inherits:** `ResourceImporter<class_ResourceImporter>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Imports an MP3 audio file for playback.

classref-introduction-group

## Description

MP3 is a lossy audio format, with worse audio quality compared to `ResourceImporterOggVorbis<class_ResourceImporterOggVorbis>` at a given bitrate.

In most cases, it's recommended to use Ogg Vorbis over MP3. However, if you're using an MP3 sound source with no higher quality source available, then it's recommended to use the MP3 file directly to avoid double lossy compression.

MP3 requires more CPU to decode than `ResourceImporterWAV<class_ResourceImporterWAV>`. If you need to play a lot of simultaneous sounds, it's recommended to use WAV for those sounds instead, especially if targeting low-end devices.

classref-introduction-group

## Tutorials

- `Importing audio samples <../tutorials/assets_pipeline/importing_audio_samples>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **bar_beats** = `4` `🔗<class_ResourceImporterMP3_property_bar_beats>`

The number of beats within a single bar in the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for `bar_beats<class_ResourceImporterMP3_property_bar_beats>` is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

classref-item-separator

classref-property

`int<class_int>` **beat_count** = `0` `🔗<class_ResourceImporterMP3_property_beat_count>`

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for `beat_count<class_ResourceImporterMP3_property_beat_count>` is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

classref-item-separator

classref-property

`float<class_float>` **bpm** = `0` `🔗<class_ResourceImporterMP3_property_bpm>`

The tempo of the audio track, measured in beats per minute. This should match the BPM measure that was used to compose the track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for `bpm<class_ResourceImporterMP3_property_bpm>` is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.

classref-item-separator

classref-property

`bool<class_bool>` **loop** = `false` `🔗<class_ResourceImporterMP3_property_loop>`

If enabled, the audio will begin playing either from the beginning or from `loop_offset<class_ResourceImporterMP3_property_loop_offset>`, after playback ends by either reaching the end of the audio or reaching the end of the last beat according to the amount specified in `beat_count<class_ResourceImporterMP3_property_beat_count>`.

**Note:** In `AudioStreamPlayer<class_AudioStreamPlayer>`, the `AudioStreamPlayer.finished<class_AudioStreamPlayer_signal_finished>` signal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.

classref-item-separator

classref-property

`float<class_float>` **loop_offset** = `0` `🔗<class_ResourceImporterMP3_property_loop_offset>`

Determines where audio will start to loop after playback reaches the end of the audio. This can be used to only loop a part of the audio file, which is useful for some ambient sounds or music. The value is determined in seconds relative to the beginning of the audio. A value of `0.0` will loop the entire audio file.

Only has an effect if `loop<class_ResourceImporterMP3_property_loop>` is `true`.

A more convenient editor for `loop_offset<class_ResourceImporterMP3_property_loop_offset>` is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.