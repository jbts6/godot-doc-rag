github_url
hide

# AudioStreamPlayer3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Plays positional sound in 3D space.

classref-introduction-group

## Description

Plays audio with positional sound effects, based on the relative position of the audio listener. Positional effects include distance attenuation, directionality, and the Doppler effect. For greater realism, a low-pass filter is applied to distant sounds. This can be disabled by setting `attenuation_filter_cutoff_hz<class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz>` to `20500`.

By default, audio is heard from the camera position. This can be changed by adding an `AudioListener3D<class_AudioListener3D>` node to the scene and enabling it by calling `AudioListener3D.make_current()<class_AudioListener3D_method_make_current>` on it.

See also `AudioStreamPlayer<class_AudioStreamPlayer>` to play a sound non-positionally.

**Note:** Hiding an **AudioStreamPlayer3D** node does not disable its audio output. To temporarily disable an **AudioStreamPlayer3D**'s audio output, set `volume_db<class_AudioStreamPlayer3D_property_volume_db>` to a very low value like `-100` (which isn't audible to human hearing).

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**finished**() `🔗<class_AudioStreamPlayer3D_signal_finished>`

Emitted when the audio stops playing.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **AttenuationModel**: `🔗<enum_AudioStreamPlayer3D_AttenuationModel>`

classref-enumeration-constant

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>` **ATTENUATION_INVERSE_DISTANCE** = `0`

Attenuation of loudness according to linear distance.

classref-enumeration-constant

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>` **ATTENUATION_INVERSE_SQUARE_DISTANCE** = `1`

Attenuation of loudness according to squared distance.

classref-enumeration-constant

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>` **ATTENUATION_LOGARITHMIC** = `2`

Attenuation of loudness according to logarithmic distance.

classref-enumeration-constant

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>` **ATTENUATION_DISABLED** = `3`

No attenuation of loudness according to distance. The sound will still be heard positionally, unlike an `AudioStreamPlayer<class_AudioStreamPlayer>`. `ATTENUATION_DISABLED<class_AudioStreamPlayer3D_constant_ATTENUATION_DISABLED>` can be combined with a `max_distance<class_AudioStreamPlayer3D_property_max_distance>` value greater than `0.0` to achieve linear attenuation clamped to a sphere of a defined size.

classref-item-separator

classref-enumeration

enum **DopplerTracking**: `🔗<enum_AudioStreamPlayer3D_DopplerTracking>`

classref-enumeration-constant

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>` **DOPPLER_TRACKING_DISABLED** = `0`

Disables doppler tracking.

classref-enumeration-constant

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>` **DOPPLER_TRACKING_IDLE_STEP** = `1`

Executes doppler tracking during process frames (see `Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`).

classref-enumeration-constant

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>` **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Executes doppler tracking during physics frames (see `Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **area_mask** = `0` `🔗<class_AudioStreamPlayer3D_property_area_mask>`

classref-property-setget

- `void (No return value.)` **set_area_mask**(value: `int<class_int>`)
- `int<class_int>` **get_area_mask**()

Determines which `Area3D<class_Area3D>` layers affect the sound for reverb and audio bus effects. Areas can be used to redirect `AudioStream<class_AudioStream>`s so that they play in a certain audio bus. An example of how you might use this is making a "water" area so that sounds played in the water are redirected through an audio bus to make them sound like they are being played underwater.

classref-item-separator

classref-property

`float<class_float>` **attenuation_filter_cutoff_hz** = `5000.0` `🔗<class_AudioStreamPlayer3D_property_attenuation_filter_cutoff_hz>`

classref-property-setget

- `void (No return value.)` **set_attenuation_filter_cutoff_hz**(value: `float<class_float>`)
- `float<class_float>` **get_attenuation_filter_cutoff_hz**()

The cutoff frequency of the attenuation low-pass filter, in Hz. A sound above this frequency is attenuated more than a sound below this frequency. To disable this effect, set this to `20500` as this frequency is above the human hearing limit.

classref-item-separator

classref-property

`float<class_float>` **attenuation_filter_db** = `-24.0` `🔗<class_AudioStreamPlayer3D_property_attenuation_filter_db>`

classref-property-setget

- `void (No return value.)` **set_attenuation_filter_db**(value: `float<class_float>`)
- `float<class_float>` **get_attenuation_filter_db**()

Amount how much the filter affects the loudness, in decibels.

classref-item-separator

classref-property

`AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>` **attenuation_model** = `0` `🔗<class_AudioStreamPlayer3D_property_attenuation_model>`

classref-property-setget

- `void (No return value.)` **set_attenuation_model**(value: `AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>`)
- `AttenuationModel<enum_AudioStreamPlayer3D_AttenuationModel>` **get_attenuation_model**()

Decides if audio should get quieter with distance linearly, quadratically, logarithmically, or not be affected by distance, effectively disabling attenuation.

classref-item-separator

classref-property

`bool<class_bool>` **autoplay** = `false` `🔗<class_AudioStreamPlayer3D_property_autoplay>`

classref-property-setget

- `void (No return value.)` **set_autoplay**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_autoplay_enabled**()

If `true`, audio plays when the AudioStreamPlayer3D node is added to scene tree.

classref-item-separator

classref-property

`StringName<class_StringName>` **bus** = `&"Master"` `🔗<class_AudioStreamPlayer3D_property_bus>`

classref-property-setget

- `void (No return value.)` **set_bus**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_bus**()

The bus on which this audio is playing.

**Note:** When setting this property, keep in mind that no validation is performed to see if the given name matches an existing bus. This is because audio bus layouts might be loaded after this property is set. If this given name can't be resolved at runtime, it will fall back to `"Master"`.

classref-item-separator

classref-property

`DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>` **doppler_tracking** = `0` `🔗<class_AudioStreamPlayer3D_property_doppler_tracking>`

classref-property-setget

- `void (No return value.)` **set_doppler_tracking**(value: `DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>`)
- `DopplerTracking<enum_AudioStreamPlayer3D_DopplerTracking>` **get_doppler_tracking**()

Decides in which step the Doppler effect should be calculated.

**Note:** If `doppler_tracking<class_AudioStreamPlayer3D_property_doppler_tracking>` is not `DOPPLER_TRACKING_DISABLED<class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED>` but the current `Camera3D<class_Camera3D>`/`AudioListener3D<class_AudioListener3D>` has doppler tracking disabled, the Doppler effect will be heard but will not take the movement of the current listener into account. If accurate Doppler effect is desired, doppler tracking should be enabled on both the **AudioStreamPlayer3D** and the current `Camera3D<class_Camera3D>`/`AudioListener3D<class_AudioListener3D>`.

classref-item-separator

classref-property

`float<class_float>` **emission_angle_degrees** = `45.0` `🔗<class_AudioStreamPlayer3D_property_emission_angle_degrees>`

classref-property-setget

- `void (No return value.)` **set_emission_angle**(value: `float<class_float>`)
- `float<class_float>` **get_emission_angle**()

The angle in which the audio reaches a listener unattenuated.

classref-item-separator

classref-property

`bool<class_bool>` **emission_angle_enabled** = `false` `🔗<class_AudioStreamPlayer3D_property_emission_angle_enabled>`

classref-property-setget

- `void (No return value.)` **set_emission_angle_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_emission_angle_enabled**()

If `true`, the audio should be attenuated according to the direction of the sound.

classref-item-separator

classref-property

`float<class_float>` **emission_angle_filter_attenuation_db** = `-12.0` `🔗<class_AudioStreamPlayer3D_property_emission_angle_filter_attenuation_db>`

classref-property-setget

- `void (No return value.)` **set_emission_angle_filter_attenuation_db**(value: `float<class_float>`)
- `float<class_float>` **get_emission_angle_filter_attenuation_db**()

Attenuation factor used if listener is outside of `emission_angle_degrees<class_AudioStreamPlayer3D_property_emission_angle_degrees>` and `emission_angle_enabled<class_AudioStreamPlayer3D_property_emission_angle_enabled>` is set, in decibels.

classref-item-separator

classref-property

`float<class_float>` **max_db** = `3.0` `🔗<class_AudioStreamPlayer3D_property_max_db>`

classref-property-setget

- `void (No return value.)` **set_max_db**(value: `float<class_float>`)
- `float<class_float>` **get_max_db**()

Sets the absolute maximum of the sound level, in decibels.

classref-item-separator

classref-property

`float<class_float>` **max_distance** = `0.0` `🔗<class_AudioStreamPlayer3D_property_max_distance>`

classref-property-setget

- `void (No return value.)` **set_max_distance**(value: `float<class_float>`)
- `float<class_float>` **get_max_distance**()

The distance past which the sound can no longer be heard at all. Only has an effect if set to a value greater than `0.0`. `max_distance<class_AudioStreamPlayer3D_property_max_distance>` works in tandem with `unit_size<class_AudioStreamPlayer3D_property_unit_size>`. However, unlike `unit_size<class_AudioStreamPlayer3D_property_unit_size>` whose behavior depends on the `attenuation_model<class_AudioStreamPlayer3D_property_attenuation_model>`, `max_distance<class_AudioStreamPlayer3D_property_max_distance>` always works in a linear fashion. This can be used to prevent the **AudioStreamPlayer3D** from requiring audio mixing when the listener is far away, which saves CPU resources.

classref-item-separator

classref-property

`int<class_int>` **max_polyphony** = `1` `🔗<class_AudioStreamPlayer3D_property_max_polyphony>`

classref-property-setget

- `void (No return value.)` **set_max_polyphony**(value: `int<class_int>`)
- `int<class_int>` **get_max_polyphony**()

The maximum number of sounds this node can play at the same time. Playing additional sounds after this value is reached will cut off the oldest sounds.

classref-item-separator

classref-property

`float<class_float>` **panning_strength** = `1.0` `🔗<class_AudioStreamPlayer3D_property_panning_strength>`

classref-property-setget

- `void (No return value.)` **set_panning_strength**(value: `float<class_float>`)
- `float<class_float>` **get_panning_strength**()

Scales the panning strength for this node by multiplying the base `ProjectSettings.audio/general/3d_panning_strength<class_ProjectSettings_property_audio/general/3d_panning_strength>` by this factor. If the product is `0.0` then stereo panning is disabled and the volume is the same for all channels. If the product is `1.0` then one of the channels will be muted when the sound is located exactly to the left (or right) of the listener.

Two speaker stereo arrangements implement the [WebAudio standard for StereoPannerNode Panning](https://webaudio.github.io/web-audio-api/#stereopanner-algorithm) where the volume is cosine of half the azimuth angle to the ear.

For other speaker arrangements such as the 5.1 and 7.1 the SPCAP (Speaker-Placement Correction Amplitude) algorithm is implemented.

classref-item-separator

classref-property

`float<class_float>` **pitch_scale** = `1.0` `🔗<class_AudioStreamPlayer3D_property_pitch_scale>`

classref-property-setget

- `void (No return value.)` **set_pitch_scale**(value: `float<class_float>`)
- `float<class_float>` **get_pitch_scale**()

The pitch and the tempo of the audio, as a multiplier of the audio sample's sample rate.

classref-item-separator

classref-property

`PlaybackType<enum_AudioServer_PlaybackType>` **playback_type** = `0` `🔗<class_AudioStreamPlayer3D_property_playback_type>`

classref-property-setget

- `void (No return value.)` **set_playback_type**(value: `PlaybackType<enum_AudioServer_PlaybackType>`)
- `PlaybackType<enum_AudioServer_PlaybackType>` **get_playback_type**()

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.

classref-item-separator

classref-property

`bool<class_bool>` **playing** = `false` `🔗<class_AudioStreamPlayer3D_property_playing>`

classref-property-setget

- `void (No return value.)` **set_playing**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_playing**()

If `true`, audio is playing or is queued to be played (see `play()<class_AudioStreamPlayer3D_method_play>`).

classref-item-separator

classref-property

`AudioStream<class_AudioStream>` **stream** `🔗<class_AudioStreamPlayer3D_property_stream>`

classref-property-setget

- `void (No return value.)` **set_stream**(value: `AudioStream<class_AudioStream>`)
- `AudioStream<class_AudioStream>` **get_stream**()

The `AudioStream<class_AudioStream>` resource to be played.

classref-item-separator

classref-property

`bool<class_bool>` **stream_paused** = `false` `🔗<class_AudioStreamPlayer3D_property_stream_paused>`

classref-property-setget

- `void (No return value.)` **set_stream_paused**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_stream_paused**()

If `true`, the playback is paused. You can resume it by setting `stream_paused<class_AudioStreamPlayer3D_property_stream_paused>` to `false`.

classref-item-separator

classref-property

`float<class_float>` **unit_size** = `10.0` `🔗<class_AudioStreamPlayer3D_property_unit_size>`

classref-property-setget

- `void (No return value.)` **set_unit_size**(value: `float<class_float>`)
- `float<class_float>` **get_unit_size**()

The factor for the attenuation effect. Higher values make the sound audible over a larger distance.

classref-item-separator

classref-property

`float<class_float>` **volume_db** = `0.0` `🔗<class_AudioStreamPlayer3D_property_volume_db>`

classref-property-setget

- `void (No return value.)` **set_volume_db**(value: `float<class_float>`)
- `float<class_float>` **get_volume_db**()

The base sound level before attenuation, in decibels.

classref-item-separator

classref-property

`float<class_float>` **volume_linear** `🔗<class_AudioStreamPlayer3D_property_volume_linear>`

classref-property-setget

- `void (No return value.)` **set_volume_linear**(value: `float<class_float>`)
- `float<class_float>` **get_volume_linear**()

The base sound level before attenuation, as a linear value.

**Note:** This member modifies `volume_db<class_AudioStreamPlayer3D_property_volume_db>` for convenience. The returned value is equivalent to the result of `@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>` on `volume_db<class_AudioStreamPlayer3D_property_volume_db>`. Setting this member is equivalent to setting `volume_db<class_AudioStreamPlayer3D_property_volume_db>` to the result of `@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>` on a value.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_playback_position**() `🔗<class_AudioStreamPlayer3D_method_get_playback_position>`

Returns the position in the `AudioStream<class_AudioStream>`.

classref-item-separator

classref-method

`AudioStreamPlayback<class_AudioStreamPlayback>` **get_stream_playback**() `🔗<class_AudioStreamPlayer3D_method_get_stream_playback>`

Returns the `AudioStreamPlayback<class_AudioStreamPlayback>` object associated with this **AudioStreamPlayer3D**.

classref-item-separator

classref-method

`bool<class_bool>` **has_stream_playback**() `🔗<class_AudioStreamPlayer3D_method_has_stream_playback>`

Returns whether the `AudioStreamPlayer<class_AudioStreamPlayer>` can return the `AudioStreamPlayback<class_AudioStreamPlayback>` object or not.

classref-item-separator

classref-method

`void (No return value.)` **play**(from_position: `float<class_float>` = 0.0) `🔗<class_AudioStreamPlayer3D_method_play>`

Queues the audio to play on the next physics frame, from the given position `from_position`, in seconds.

classref-item-separator

classref-method

`void (No return value.)` **seek**(to_position: `float<class_float>`) `🔗<class_AudioStreamPlayer3D_method_seek>`

Sets the position from which audio will be played, in seconds.

classref-item-separator

classref-method

`void (No return value.)` **stop**() `🔗<class_AudioStreamPlayer3D_method_stop>`

Stops the audio.