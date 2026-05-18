github_url
hide

# AudioStreamPlayer

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

A node for audio playback.

classref-introduction-group

## Description

The **AudioStreamPlayer** node plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.

To use this node, `stream<class_AudioStreamPlayer_property_stream>` needs to be set to a valid `AudioStream<class_AudioStream>` resource. Playing more than one sound at the same time is also supported, see `max_polyphony<class_AudioStreamPlayer_property_max_polyphony>`.

If you need to play audio at a specific position, use `AudioStreamPlayer2D<class_AudioStreamPlayer2D>` or `AudioStreamPlayer3D<class_AudioStreamPlayer3D>` instead.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- [Audio Device Changer Demo](https://godotengine.org/asset-library/asset/2758)
- [Audio Generator Demo](https://godotengine.org/asset-library/asset/2759)
- [Audio Microphone Record Demo](https://godotengine.org/asset-library/asset/2760)
- [Audio Spectrum Visualizer Demo](https://godotengine.org/asset-library/asset/2762)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**finished**() `🔗<class_AudioStreamPlayer_signal_finished>`

Emitted when a sound finishes playing without interruptions. This signal is *not* emitted when calling `stop()<class_AudioStreamPlayer_method_stop>`, or when exiting the tree while sounds are playing.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **MixTarget**: `🔗<enum_AudioStreamPlayer_MixTarget>`

classref-enumeration-constant

`MixTarget<enum_AudioStreamPlayer_MixTarget>` **MIX_TARGET_STEREO** = `0`

The audio will be played only on the first channel. This is the default.

classref-enumeration-constant

`MixTarget<enum_AudioStreamPlayer_MixTarget>` **MIX_TARGET_SURROUND** = `1`

The audio will be played on all surround channels.

classref-enumeration-constant

`MixTarget<enum_AudioStreamPlayer_MixTarget>` **MIX_TARGET_CENTER** = `2`

The audio will be played on the second channel, which is usually the center.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **autoplay** = `false` `🔗<class_AudioStreamPlayer_property_autoplay>`

classref-property-setget

- `void (No return value.)` **set_autoplay**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_autoplay_enabled**()

If `true`, this node calls `play()<class_AudioStreamPlayer_method_play>` when entering the tree.

classref-item-separator

classref-property

`StringName<class_StringName>` **bus** = `&"Master"` `🔗<class_AudioStreamPlayer_property_bus>`

classref-property-setget

- `void (No return value.)` **set_bus**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_bus**()

The target bus name. All sounds from this node will be playing on this bus.

**Note:** At runtime, if no bus with the given name exists, all sounds will fall back on `"Master"`. See also `AudioServer.get_bus_name()<class_AudioServer_method_get_bus_name>`.

classref-item-separator

classref-property

`int<class_int>` **max_polyphony** = `1` `🔗<class_AudioStreamPlayer_property_max_polyphony>`

classref-property-setget

- `void (No return value.)` **set_max_polyphony**(value: `int<class_int>`)
- `int<class_int>` **get_max_polyphony**()

The maximum number of sounds this node can play at the same time. Calling `play()<class_AudioStreamPlayer_method_play>` after this value is reached will cut off the oldest sounds.

classref-item-separator

classref-property

`MixTarget<enum_AudioStreamPlayer_MixTarget>` **mix_target** = `0` `🔗<class_AudioStreamPlayer_property_mix_target>`

classref-property-setget

- `void (No return value.)` **set_mix_target**(value: `MixTarget<enum_AudioStreamPlayer_MixTarget>`)
- `MixTarget<enum_AudioStreamPlayer_MixTarget>` **get_mix_target**()

The mix target channels. Has no effect when two speakers or less are detected (see `SpeakerMode<enum_AudioServer_SpeakerMode>`).

classref-item-separator

classref-property

`float<class_float>` **pitch_scale** = `1.0` `🔗<class_AudioStreamPlayer_property_pitch_scale>`

classref-property-setget

- `void (No return value.)` **set_pitch_scale**(value: `float<class_float>`)
- `float<class_float>` **get_pitch_scale**()

The audio's pitch and tempo, as a multiplier of the `stream<class_AudioStreamPlayer_property_stream>`'s sample rate. A value of `2.0` doubles the audio's pitch, while a value of `0.5` halves the pitch.

classref-item-separator

classref-property

`PlaybackType<enum_AudioServer_PlaybackType>` **playback_type** = `0` `🔗<class_AudioStreamPlayer_property_playback_type>`

classref-property-setget

- `void (No return value.)` **set_playback_type**(value: `PlaybackType<enum_AudioServer_PlaybackType>`)
- `PlaybackType<enum_AudioServer_PlaybackType>` **get_playback_type**()

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

classref-item-separator

classref-property

`bool<class_bool>` **playing** = `false` `🔗<class_AudioStreamPlayer_property_playing>`

classref-property-setget

- `void (No return value.)` **set_playing**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_playing**()

If `true`, this node is playing sounds. Setting this property has the same effect as `play()<class_AudioStreamPlayer_method_play>` and `stop()<class_AudioStreamPlayer_method_stop>`.

classref-item-separator

classref-property

`AudioStream<class_AudioStream>` **stream** `🔗<class_AudioStreamPlayer_property_stream>`

classref-property-setget

- `void (No return value.)` **set_stream**(value: `AudioStream<class_AudioStream>`)
- `AudioStream<class_AudioStream>` **get_stream**()

The `AudioStream<class_AudioStream>` resource to be played. Setting this property stops all currently playing sounds. If left empty, the **AudioStreamPlayer** does not work.

classref-item-separator

classref-property

`bool<class_bool>` **stream_paused** = `false` `🔗<class_AudioStreamPlayer_property_stream_paused>`

classref-property-setget

- `void (No return value.)` **set_stream_paused**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_stream_paused**()

If `true`, the sounds are paused. Setting `stream_paused<class_AudioStreamPlayer_property_stream_paused>` to `false` resumes all sounds.

**Note:** This property is automatically changed when exiting or entering the tree, or this node is paused (see `Node.process_mode<class_Node_property_process_mode>`).

classref-item-separator

classref-property

`float<class_float>` **volume_db** = `0.0` `🔗<class_AudioStreamPlayer_property_volume_db>`

classref-property-setget

- `void (No return value.)` **set_volume_db**(value: `float<class_float>`)
- `float<class_float>` **get_volume_db**()

Volume of sound, in decibels. This is an offset of the `stream<class_AudioStreamPlayer_property_stream>`'s volume.

**Note:** To convert between decibel and linear energy (like most volume sliders do), use `volume_linear<class_AudioStreamPlayer_property_volume_linear>`, or `@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>` and `@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>`.

classref-item-separator

classref-property

`float<class_float>` **volume_linear** `🔗<class_AudioStreamPlayer_property_volume_linear>`

classref-property-setget

- `void (No return value.)` **set_volume_linear**(value: `float<class_float>`)
- `float<class_float>` **get_volume_linear**()

Volume of sound, as a linear value.

**Note:** This member modifies `volume_db<class_AudioStreamPlayer_property_volume_db>` for convenience. The returned value is equivalent to the result of `@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>` on `volume_db<class_AudioStreamPlayer_property_volume_db>`. Setting this member is equivalent to setting `volume_db<class_AudioStreamPlayer_property_volume_db>` to the result of `@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>` on a value.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_playback_position**() `🔗<class_AudioStreamPlayer_method_get_playback_position>`

Returns the position in the `AudioStream<class_AudioStream>` of the latest sound, in seconds. Returns `0.0` if no sounds are playing.

**Note:** The position is not always accurate, as the `AudioServer<class_AudioServer>` does not mix audio every processed frame. To get more accurate results, add `AudioServer.get_time_since_last_mix()<class_AudioServer_method_get_time_since_last_mix>` to the returned position.

**Note:** This method always returns `0.0` if the `stream<class_AudioStreamPlayer_property_stream>` is an `AudioStreamInteractive<class_AudioStreamInteractive>`, since it can have multiple clips playing at once.

classref-item-separator

classref-method

`AudioStreamPlayback<class_AudioStreamPlayback>` **get_stream_playback**() `🔗<class_AudioStreamPlayer_method_get_stream_playback>`

Returns the latest `AudioStreamPlayback<class_AudioStreamPlayback>` of this node, usually the most recently created by `play()<class_AudioStreamPlayer_method_play>`. If no sounds are playing, this method fails and returns an empty playback.

classref-item-separator

classref-method

`bool<class_bool>` **has_stream_playback**() `🔗<class_AudioStreamPlayer_method_has_stream_playback>`

Returns `true` if any sound is active, even if `stream_paused<class_AudioStreamPlayer_property_stream_paused>` is set to `true`. See also `playing<class_AudioStreamPlayer_property_playing>` and `get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>`.

classref-item-separator

classref-method

`void (No return value.)` **play**(from_position: `float<class_float>` = 0.0) `🔗<class_AudioStreamPlayer_method_play>`

Plays a sound from the beginning, or the given `from_position` in seconds.

classref-item-separator

classref-method

`void (No return value.)` **seek**(to_position: `float<class_float>`) `🔗<class_AudioStreamPlayer_method_seek>`

Restarts all sounds to be played from the given `to_position`, in seconds. Does nothing if no sounds are playing.

classref-item-separator

classref-method

`void (No return value.)` **stop**() `🔗<class_AudioStreamPlayer_method_stop>`

Stops all sounds from this node.