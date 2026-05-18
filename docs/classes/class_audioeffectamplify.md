github_url
hide

# AudioEffectAmplify

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a volume manipulation audio effect to an audio bus.

classref-introduction-group

## Description

Increases or decreases the volume being routed through the audio bus.

classref-introduction-group

## Tutorials

- `Audio buses <../tutorials/audio/audio_buses>`
- `Audio effects <../tutorials/audio/audio_effects>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **volume_db** = `0.0` `🔗<class_AudioEffectAmplify_property_volume_db>`

classref-property-setget

- `void (No return value.)` **set_volume_db**(value: `float<class_float>`)
- `float<class_float>` **get_volume_db**()

Amount of amplification in dB. Positive values make the sound louder, negative values make it quieter. Value can range from -80 to 24.

classref-item-separator

classref-property

`float<class_float>` **volume_linear** `🔗<class_AudioEffectAmplify_property_volume_linear>`

classref-property-setget

- `void (No return value.)` **set_volume_linear**(value: `float<class_float>`)
- `float<class_float>` **get_volume_linear**()

Amount of amplification as a linear value.

**Note:** This member modifies `volume_db<class_AudioEffectAmplify_property_volume_db>` for convenience. The returned value is equivalent to the result of `@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>` on `volume_db<class_AudioEffectAmplify_property_volume_db>`. Setting this member is equivalent to setting `volume_db<class_AudioEffectAmplify_property_volume_db>` to the result of `@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>` on a value.