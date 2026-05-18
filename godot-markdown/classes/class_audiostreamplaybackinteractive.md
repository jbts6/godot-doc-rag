github_url
hide

# AudioStreamPlaybackInteractive

**Inherits:** `AudioStreamPlayback<class_AudioStreamPlayback>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Playback component of `AudioStreamInteractive<class_AudioStreamInteractive>`.

classref-introduction-group

## Description

Playback component of `AudioStreamInteractive<class_AudioStreamInteractive>`. Contains functions to change the currently played clip.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_current_clip_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamPlaybackInteractive_method_get_current_clip_index>`

Return the index of the currently playing clip. You can use this to get the name of the currently playing clip with `AudioStreamInteractive.get_clip_name()<class_AudioStreamInteractive_method_get_clip_name>`.

**Example:** Get the currently playing clip name from inside an `AudioStreamPlayer<class_AudioStreamPlayer>` node.

gdscript

var playing_clip_name = stream.get_clip_name(get_stream_playback().get_current_clip_index())

classref-item-separator

classref-method

`void (No return value.)` **switch_to_clip**(clip_index: `int<class_int>`) `🔗<class_AudioStreamPlaybackInteractive_method_switch_to_clip>`

Switch to a clip (by index).

classref-item-separator

classref-method

`void (No return value.)` **switch_to_clip_by_name**(clip_name: `StringName<class_StringName>`) `🔗<class_AudioStreamPlaybackInteractive_method_switch_to_clip_by_name>`

Switch to a clip (by name).