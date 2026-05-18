github_url
hide

# AudioEffectPanner

**Inherits:** `AudioEffect<class_AudioEffect>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Adds a panner audio effect to an audio bus.

Pans the sound left or right.

classref-introduction-group

## Description

Determines how much of the audio signal is sent to the left and right channels. This helps with audio spatialization, giving sounds distinct places in a mix.

`AudioStreamPlayer2D<class_AudioStreamPlayer2D>` and `AudioStreamPlayer3D<class_AudioStreamPlayer3D>` handle panning automatically, following where the source of the sound is on the screen.

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

`float<class_float>` **pan** = `0.0` `🔗<class_AudioEffectPanner_property_pan>`

classref-property-setget

- `void (No return value.)` **set_pan**(value: `float<class_float>`)
- `float<class_float>` **get_pan**()

Pan position. Negative values pan the sound to the left, positive pan to the right. Value can range from -1 to 1.