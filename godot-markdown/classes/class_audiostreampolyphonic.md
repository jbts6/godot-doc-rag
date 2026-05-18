github_url
hide

# AudioStreamPolyphonic

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

classref-introduction-group

## Description

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

Playback control is done via the `AudioStreamPlaybackPolyphonic<class_AudioStreamPlaybackPolyphonic>` instance set inside the player, which can be obtained via `AudioStreamPlayer.get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>`, `AudioStreamPlayer2D.get_stream_playback()<class_AudioStreamPlayer2D_method_get_stream_playback>` or `AudioStreamPlayer3D.get_stream_playback()<class_AudioStreamPlayer3D_method_get_stream_playback>` methods. Obtaining the playback instance is only valid after the `stream` property is set as an **AudioStreamPolyphonic** in those players.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **polyphony** = `32` `🔗<class_AudioStreamPolyphonic_property_polyphony>`

classref-property-setget

- `void (No return value.)` **set_polyphony**(value: `int<class_int>`)
- `int<class_int>` **get_polyphony**()

Maximum amount of simultaneous streams that can be played.