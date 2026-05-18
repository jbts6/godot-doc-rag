github_url
hide

# AudioStreamMP3

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

MP3 audio stream driver.

classref-introduction-group

## Description

MP3 audio stream driver. See `data<class_AudioStreamMP3_property_data>` if you want to load an MP3 file at run-time. More info can be found in `ResourceImporterMP3<class_ResourceImporterMP3>`.

**Note:** This class can optionally support legacy MP1 and MP2 formats, provided that the engine is compiled with the `minimp3_extra_formats=yes` SCons option. These extra formats are not enabled by default.

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

`int<class_int>` **bar_beats** = `4` `🔗<class_AudioStreamMP3_property_bar_beats>`

classref-property-setget

- `void (No return value.)` **set_bar_beats**(value: `int<class_int>`)
- `int<class_int>` **get_bar_beats**()

The number of beats within a single bar in the audio track.

classref-item-separator

classref-property

`int<class_int>` **beat_count** = `0` `🔗<class_AudioStreamMP3_property_beat_count>`

classref-property-setget

- `void (No return value.)` **set_beat_count**(value: `int<class_int>`)
- `int<class_int>` **get_beat_count**()

The length of the audio track, in beats. The actual duration of the audio file might be longer than what is indicated by this property. It defines the end of the audio for looping, `AudioStreamPlaylist<class_AudioStreamPlaylist>`, and `AudioStreamInteractive<class_AudioStreamInteractive>`.

classref-item-separator

classref-property

`float<class_float>` **bpm** = `0.0` `🔗<class_AudioStreamMP3_property_bpm>`

classref-property-setget

- `void (No return value.)` **set_bpm**(value: `float<class_float>`)
- `float<class_float>` **get_bpm**()

The tempo of the audio track, measured in beats per minute.

classref-item-separator

classref-property

`PackedByteArray<class_PackedByteArray>` **data** = `PackedByteArray()` `🔗<class_AudioStreamMP3_property_data>`

classref-property-setget

- `void (No return value.)` **set_data**(value: `PackedByteArray<class_PackedByteArray>`)
- `PackedByteArray<class_PackedByteArray>` **get_data**()

Contains the audio data in bytes.

You can load a file without having to import it beforehand using the code snippet below. Keep in mind that this snippet loads the whole file into memory and may not be ideal for huge files (hundreds of megabytes or more).

gdscript

func load_mp3(path):
var file = FileAccess.open(path, FileAccess.READ) var sound = AudioStreamMP3.new() sound.data = file.get_buffer(file.get_length()) return sound

csharp

public AudioStreamMP3 LoadMP3(string path) { using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read); var sound = new AudioStreamMP3(); sound.Data = file.GetBuffer(file.GetLength()); return sound; }

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedByteArray<class_PackedByteArray>` for more details.

classref-item-separator

classref-property

`bool<class_bool>` **loop** = `false` `🔗<class_AudioStreamMP3_property_loop>`

classref-property-setget

- `void (No return value.)` **set_loop**(value: `bool<class_bool>`)
- `bool<class_bool>` **has_loop**()

If `true`, the stream will play again from the specified `loop_offset<class_AudioStreamMP3_property_loop_offset>` once it reaches the end of the audio track, or once it reaches the end of the last beat according to the amount specified in `beat_count<class_AudioStreamMP3_property_beat_count>`. Useful for ambient sounds and background music.

classref-item-separator

classref-property

`float<class_float>` **loop_offset** = `0.0` `🔗<class_AudioStreamMP3_property_loop_offset>`

classref-property-setget

- `void (No return value.)` **set_loop_offset**(value: `float<class_float>`)
- `float<class_float>` **get_loop_offset**()

Time in seconds at which the stream starts after being looped.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AudioStreamMP3<class_AudioStreamMP3>` **load_from_buffer**(stream_data: `PackedByteArray<class_PackedByteArray>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_AudioStreamMP3_method_load_from_buffer>`

Creates a new **AudioStreamMP3** instance from the given buffer. The buffer must contain MP3 data.

classref-item-separator

classref-method

`AudioStreamMP3<class_AudioStreamMP3>` **load_from_file**(path: `String<class_String>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_AudioStreamMP3_method_load_from_file>`

Creates a new **AudioStreamMP3** instance from the given file path. The file must be in MP3 format.