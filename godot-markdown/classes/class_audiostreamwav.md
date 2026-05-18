github_url
hide

# AudioStreamWAV

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Stores audio data loaded from WAV files.

classref-introduction-group

## Description

AudioStreamWAV stores sound samples loaded from WAV files. To play the stored sound, use an `AudioStreamPlayer<class_AudioStreamPlayer>` (for non-positional audio) or `AudioStreamPlayer2D<class_AudioStreamPlayer2D>`/`AudioStreamPlayer3D<class_AudioStreamPlayer3D>` (for positional audio). The sound can be looped.

This class can also be used to store dynamically-generated PCM audio data. See also `AudioStreamGenerator<class_AudioStreamGenerator>` for procedural audio generation.

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

## Enumerations

classref-enumeration

enum **Format**: `🔗<enum_AudioStreamWAV_Format>`

classref-enumeration-constant

`Format<enum_AudioStreamWAV_Format>` **FORMAT_8_BITS** = `0`

8-bit PCM audio codec.

classref-enumeration-constant

`Format<enum_AudioStreamWAV_Format>` **FORMAT_16_BITS** = `1`

16-bit PCM audio codec.

classref-enumeration-constant

`Format<enum_AudioStreamWAV_Format>` **FORMAT_IMA_ADPCM** = `2`

Audio is lossily compressed as IMA ADPCM.

classref-enumeration-constant

`Format<enum_AudioStreamWAV_Format>` **FORMAT_QOA** = `3`

Audio is lossily compressed as [Quite OK Audio](https://qoaformat.org/).

classref-item-separator

classref-enumeration

enum **LoopMode**: `🔗<enum_AudioStreamWAV_LoopMode>`

classref-enumeration-constant

`LoopMode<enum_AudioStreamWAV_LoopMode>` **LOOP_DISABLED** = `0`

Audio does not loop.

classref-enumeration-constant

`LoopMode<enum_AudioStreamWAV_LoopMode>` **LOOP_FORWARD** = `1`

Audio loops the data between `loop_begin<class_AudioStreamWAV_property_loop_begin>` and `loop_end<class_AudioStreamWAV_property_loop_end>`, playing forward only.

classref-enumeration-constant

`LoopMode<enum_AudioStreamWAV_LoopMode>` **LOOP_PINGPONG** = `2`

Audio loops the data between `loop_begin<class_AudioStreamWAV_property_loop_begin>` and `loop_end<class_AudioStreamWAV_property_loop_end>`, playing back and forth.

classref-enumeration-constant

`LoopMode<enum_AudioStreamWAV_LoopMode>` **LOOP_BACKWARD** = `3`

Audio loops the data between `loop_begin<class_AudioStreamWAV_property_loop_begin>` and `loop_end<class_AudioStreamWAV_property_loop_end>`, playing backward only.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedByteArray<class_PackedByteArray>` **data** = `PackedByteArray()` `🔗<class_AudioStreamWAV_property_data>`

classref-property-setget

- `void (No return value.)` **set_data**(value: `PackedByteArray<class_PackedByteArray>`)
- `PackedByteArray<class_PackedByteArray>` **get_data**()

Contains the audio data in bytes.

**Note:** If `format<class_AudioStreamWAV_property_format>` is set to `FORMAT_8_BITS<class_AudioStreamWAV_constant_FORMAT_8_BITS>`, this property expects signed 8-bit PCM data. To convert from unsigned 8-bit PCM, subtract 128 from each byte.

**Note:** If `format<class_AudioStreamWAV_property_format>` is set to `FORMAT_QOA<class_AudioStreamWAV_constant_FORMAT_QOA>`, this property expects data from a full QOA file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedByteArray<class_PackedByteArray>` for more details.

classref-item-separator

classref-property

`Format<enum_AudioStreamWAV_Format>` **format** = `0` `🔗<class_AudioStreamWAV_property_format>`

classref-property-setget

- `void (No return value.)` **set_format**(value: `Format<enum_AudioStreamWAV_Format>`)
- `Format<enum_AudioStreamWAV_Format>` **get_format**()

Audio format.

classref-item-separator

classref-property

`int<class_int>` **loop_begin** = `0` `🔗<class_AudioStreamWAV_property_loop_begin>`

classref-property-setget

- `void (No return value.)` **set_loop_begin**(value: `int<class_int>`)
- `int<class_int>` **get_loop_begin**()

The loop start point (in number of samples, relative to the beginning of the stream).

classref-item-separator

classref-property

`int<class_int>` **loop_end** = `0` `🔗<class_AudioStreamWAV_property_loop_end>`

classref-property-setget

- `void (No return value.)` **set_loop_end**(value: `int<class_int>`)
- `int<class_int>` **get_loop_end**()

The loop end point (in number of samples, relative to the beginning of the stream).

classref-item-separator

classref-property

`LoopMode<enum_AudioStreamWAV_LoopMode>` **loop_mode** = `0` `🔗<class_AudioStreamWAV_property_loop_mode>`

classref-property-setget

- `void (No return value.)` **set_loop_mode**(value: `LoopMode<enum_AudioStreamWAV_LoopMode>`)
- `LoopMode<enum_AudioStreamWAV_LoopMode>` **get_loop_mode**()

The loop mode.

classref-item-separator

classref-property

`int<class_int>` **mix_rate** = `44100` `🔗<class_AudioStreamWAV_property_mix_rate>`

classref-property-setget

- `void (No return value.)` **set_mix_rate**(value: `int<class_int>`)
- `int<class_int>` **get_mix_rate**()

The sample rate for mixing this audio. Higher values require more storage space, but result in better quality.

In games, common sample rates in use are `11025`, `16000`, `22050`, `32000`, `44100`, and `48000`.

According to the [Nyquist-Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem), there is no quality difference to human hearing when going past 40,000 Hz (since most humans can only hear up to ~20,000 Hz, often less). If you are using lower-pitched sounds such as voices, lower sample rates such as `32000` or `22050` may be usable with no loss in quality.

classref-item-separator

classref-property

`bool<class_bool>` **stereo** = `false` `🔗<class_AudioStreamWAV_property_stereo>`

classref-property-setget

- `void (No return value.)` **set_stereo**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_stereo**()

If `true`, audio is stereo.

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **tags** = `{}` `🔗<class_AudioStreamWAV_property_tags>`

classref-property-setget

- `void (No return value.)` **set_tags**(value: `Dictionary<class_Dictionary>`)
- `Dictionary<class_Dictionary>` **get_tags**()

Contains user-defined tags if found in the WAV data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

**Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

**Note:** Only WAV files using a `LIST` chunk with an identifier of `INFO` to encode the tags are currently supported.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AudioStreamWAV<class_AudioStreamWAV>` **load_from_buffer**(stream_data: `PackedByteArray<class_PackedByteArray>`, options: `Dictionary<class_Dictionary>` = {}) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_AudioStreamWAV_method_load_from_buffer>`

Creates a new **AudioStreamWAV** instance from the given buffer. The buffer must contain WAV data.

The keys and values of `options` match the properties of `ResourceImporterWAV<class_ResourceImporterWAV>`. The usage of `options` is identical to `load_from_file()<class_AudioStreamWAV_method_load_from_file>`.

classref-item-separator

classref-method

`AudioStreamWAV<class_AudioStreamWAV>` **load_from_file**(path: `String<class_String>`, options: `Dictionary<class_Dictionary>` = {}) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_AudioStreamWAV_method_load_from_file>`

Creates a new **AudioStreamWAV** instance from the given file path. The file must be in WAV format.

The keys and values of `options` match the properties of `ResourceImporterWAV<class_ResourceImporterWAV>`.

**Example:** Load the first file dropped as a WAV and play it:

    @onready var audio_player = $AudioStreamPlayer

    func _ready():
        get_window().files_dropped.connect(_on_files_dropped)

    func _on_files_dropped(files):
        if files[0].get_extension() == "wav":
            audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                    "force/max_rate": true,
                    "force/max_rate_hz": 11025
                })
            audio_player.play()

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **save_to_wav**(path: `String<class_String>`) `🔗<class_AudioStreamWAV_method_save_to_wav>`

Saves the AudioStreamWAV as a WAV file to `path`. Samples with IMA ADPCM or Quite OK Audio formats can't be saved.

**Note:** A `.wav` extension is automatically appended to `path` if it is missing.