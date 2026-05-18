github_url
hide

# AudioStreamOggVorbis

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A class representing an Ogg Vorbis audio stream.

classref-introduction-group

## Description

The AudioStreamOggVorbis class is a specialized `AudioStream<class_AudioStream>` for handling Ogg Vorbis file formats. It offers functionality for loading and playing back Ogg Vorbis files, as well as managing looping and other playback properties. More info can be found in `ResourceImporterOggVorbis<class_ResourceImporterOggVorbis>`.

This class is part of the audio stream system, which also supports WAV files through the `AudioStreamWAV<class_AudioStreamWAV>` class, and MP3 files through the `AudioStreamMP3<class_AudioStreamMP3>` class.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`
- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **bar_beats** = `4` `🔗<class_AudioStreamOggVorbis_property_bar_beats>`

classref-property-setget

- `void (No return value.)` **set_bar_beats**(value: `int<class_int>`)
- `int<class_int>` **get_bar_beats**()

The number of beats within a single bar in the audio track.

classref-item-separator

classref-property

`int<class_int>` **beat_count** = `0` `🔗<class_AudioStreamOggVorbis_property_beat_count>`

classref-property-setget

- `void (No return value.)` **set_beat_count**(value: `int<class_int>`)
- `int<class_int>` **get_beat_count**()

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. It defines the end of the audio for looping, `AudioStreamPlaylist<class_AudioStreamPlaylist>`, and `AudioStreamInteractive<class_AudioStreamInteractive>`.

classref-item-separator

classref-property

`float<class_float>` **bpm** = `0.0` `🔗<class_AudioStreamOggVorbis_property_bpm>`

classref-property-setget

- `void (No return value.)` **set_bpm**(value: `float<class_float>`)
- `float<class_float>` **get_bpm**()

The tempo of the audio track, measured in beats per minute.

classref-item-separator

classref-property

`bool<class_bool>` **loop** = `false` `🔗<class_AudioStreamOggVorbis_property_loop>`

classref-property-setget

- `void (No return value.)` **set_loop**(value: `bool<class_bool>`)
- `bool<class_bool>` **has_loop**()

If `true`, the stream will play again from the specified `loop_offset<class_AudioStreamOggVorbis_property_loop_offset>` once it reaches the end of the audio track, or once it reaches the end of the last beat according to the amount specified in `beat_count<class_AudioStreamOggVorbis_property_beat_count>`. Useful for ambient sounds and background music.

classref-item-separator

classref-property

`float<class_float>` **loop_offset** = `0.0` `🔗<class_AudioStreamOggVorbis_property_loop_offset>`

classref-property-setget

- `void (No return value.)` **set_loop_offset**(value: `float<class_float>`)
- `float<class_float>` **get_loop_offset**()

Time in seconds at which the stream starts after being looped.

classref-item-separator

classref-property

`OggPacketSequence<class_OggPacketSequence>` **packet_sequence** `🔗<class_AudioStreamOggVorbis_property_packet_sequence>`

classref-property-setget

- `void (No return value.)` **set_packet_sequence**(value: `OggPacketSequence<class_OggPacketSequence>`)
- `OggPacketSequence<class_OggPacketSequence>` **get_packet_sequence**()

Contains the raw Ogg data for this stream.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **tags** = `{}` `🔗<class_AudioStreamOggVorbis_property_tags>`

classref-property-setget

- `void (No return value.)` **set_tags**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_tags**()

Contains user-defined tags if found in the Ogg Vorbis data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

**Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AudioStreamOggVorbis<class_AudioStreamOggVorbis>` **load_from_buffer**(stream_data: `PackedByteArray<class_PackedByteArray>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_AudioStreamOggVorbis_method_load_from_buffer>`

Creates a new **AudioStreamOggVorbis** instance from the given buffer. The buffer must contain Ogg Vorbis data.

classref-item-separator

classref-method

`AudioStreamOggVorbis<class_AudioStreamOggVorbis>` **load_from_file**(path: `String<class_String>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_AudioStreamOggVorbis_method_load_from_file>`

Creates a new **AudioStreamOggVorbis** instance from the given file path. The file must be in Ogg Vorbis format.