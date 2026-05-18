github_url
hide

# SpriteFrames

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Sprite frame library for AnimatedSprite2D and AnimatedSprite3D.

classref-introduction-group

## Description

Sprite frame library for an `AnimatedSprite2D<class_AnimatedSprite2D>` or `AnimatedSprite3D<class_AnimatedSprite3D>` node. Contains frames and animation data for playback.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **LoopMode**: `🔗<enum_SpriteFrames_LoopMode>`

classref-enumeration-constant

`LoopMode<enum_SpriteFrames_LoopMode>` **LOOP_NONE** = `0`

The animation plays once and stops when it reaches the end, or the start if played in reverse.

classref-enumeration-constant

`LoopMode<enum_SpriteFrames_LoopMode>` **LOOP_LINEAR** = `1`

The animation restarts from the beginning when it reaches the end, or from the end if played in reverse, repeating continuously.

classref-enumeration-constant

`LoopMode<enum_SpriteFrames_LoopMode>` **LOOP_PINGPONG** = `2`

The animation alternates direction each time it reaches the end or start, playing forward and then in reverse repeatedly.

**Note:** Both `AnimatedSprite2D<class_AnimatedSprite2D>` and `AnimatedSprite3D<class_AnimatedSprite3D>` play the first/last frame for its duration only once at each end of the animation loop (instead of twice, once per forward/backward animation direction).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_animation**(anim: `StringName<class_StringName>`) `🔗<class_SpriteFrames_method_add_animation>`

Adds a new `anim` animation to the library.

classref-item-separator

classref-method

`void (No return value.)` **add_frame**(anim: `StringName<class_StringName>`, texture: `Texture2D<class_Texture2D>`, duration: `float<class_float>` = 1.0, at_position: `int<class_int>` = -1) `🔗<class_SpriteFrames_method_add_frame>`

Adds a frame to the `anim` animation. If `at_position` is `-1`, the frame will be added to the end of the animation. `duration` specifies the relative duration, see `get_frame_duration()<class_SpriteFrames_method_get_frame_duration>` for details.

classref-item-separator

classref-method

`void (No return value.)` **clear**(anim: `StringName<class_StringName>`) `🔗<class_SpriteFrames_method_clear>`

Removes all frames from the `anim` animation.

classref-item-separator

classref-method

`void (No return value.)` **clear_all**() `🔗<class_SpriteFrames_method_clear_all>`

Removes all animations. An empty `default` animation will be created.

classref-item-separator

classref-method

`void (No return value.)` **duplicate_animation**(anim_from: `StringName<class_StringName>`, anim_to: `StringName<class_StringName>`) `🔗<class_SpriteFrames_method_duplicate_animation>`

Duplicates the animation `anim_from` to a new animation named `anim_to`. Fails if `anim_to` already exists, or if `anim_from` does not exist.

classref-item-separator

classref-method

`bool<class_bool>` **get_animation_loop**(anim: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_animation_loop>`

**Deprecated:** Use `get_animation_loop_mode()<class_SpriteFrames_method_get_animation_loop_mode>` instead.

Returns `true` if `get_animation_loop_mode(anim) == LOOP_LINEAR`. Otherwise, returns `false`.

classref-item-separator

classref-method

`LoopMode<enum_SpriteFrames_LoopMode>` **get_animation_loop_mode**(anim: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_animation_loop_mode>`

Returns the loop mode for the `anim` animation.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_animation_names**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_animation_names>`

Returns an array containing the names associated to each animation. Values are placed in alphabetical order.

classref-item-separator

classref-method

`float<class_float>` **get_animation_speed**(anim: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_animation_speed>`

Returns the speed in frames per second for the `anim` animation.

classref-item-separator

classref-method

`int<class_int>` **get_frame_count**(anim: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_frame_count>`

Returns the number of frames for the `anim` animation.

classref-item-separator

classref-method

`float<class_float>` **get_frame_duration**(anim: `StringName<class_StringName>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_frame_duration>`

Returns a relative duration of the frame `idx` in the `anim` animation (defaults to `1.0`). For example, a frame with a duration of `2.0` is displayed twice as long as a frame with a duration of `1.0`. You can calculate the absolute duration (in seconds) of a frame using the following formula:

    absolute_duration = relative_duration / (animation_fps * abs(playing_speed))

In this example, `playing_speed` refers to either `AnimatedSprite2D.get_playing_speed()<class_AnimatedSprite2D_method_get_playing_speed>` or `AnimatedSprite3D.get_playing_speed()<class_AnimatedSprite3D_method_get_playing_speed>`.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_frame_texture**(anim: `StringName<class_StringName>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_get_frame_texture>`

Returns the texture of the frame `idx` in the `anim` animation.

classref-item-separator

classref-method

`bool<class_bool>` **has_animation**(anim: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpriteFrames_method_has_animation>`

Returns `true` if the `anim` animation exists.

classref-item-separator

classref-method

`void (No return value.)` **remove_animation**(anim: `StringName<class_StringName>`) `🔗<class_SpriteFrames_method_remove_animation>`

Removes the `anim` animation.

classref-item-separator

classref-method

`void (No return value.)` **remove_frame**(anim: `StringName<class_StringName>`, idx: `int<class_int>`) `🔗<class_SpriteFrames_method_remove_frame>`

Removes the `anim` animation's frame `idx`.

classref-item-separator

classref-method

`void (No return value.)` **rename_animation**(anim: `StringName<class_StringName>`, newname: `StringName<class_StringName>`) `🔗<class_SpriteFrames_method_rename_animation>`

Changes the `anim` animation's name to `newname`.

classref-item-separator

classref-method

`void (No return value.)` **set_animation_loop**(anim: `StringName<class_StringName>`, loop: `bool<class_bool>`) `🔗<class_SpriteFrames_method_set_animation_loop>`

**Deprecated:** Use `set_animation_loop_mode()<class_SpriteFrames_method_set_animation_loop_mode>` instead.

If `loop` is `false` equivalent to `set_animation_loop_mode(LOOP_NONE)`.

If `loop` is `true` equivalent to `set_animation_loop_mode(LOOP_LINEAR)`.

classref-item-separator

classref-method

`void (No return value.)` **set_animation_loop_mode**(anim: `StringName<class_StringName>`, loop_mode: `LoopMode<enum_SpriteFrames_LoopMode>`) `🔗<class_SpriteFrames_method_set_animation_loop_mode>`

Sets the `loop_mode` for the `anim` animation.

classref-item-separator

classref-method

`void (No return value.)` **set_animation_speed**(anim: `StringName<class_StringName>`, fps: `float<class_float>`) `🔗<class_SpriteFrames_method_set_animation_speed>`

Sets the speed for the `anim` animation in frames per second.

classref-item-separator

classref-method

`void (No return value.)` **set_frame**(anim: `StringName<class_StringName>`, idx: `int<class_int>`, texture: `Texture2D<class_Texture2D>`, duration: `float<class_float>` = 1.0) `🔗<class_SpriteFrames_method_set_frame>`

Sets the `texture` and the `duration` of the frame `idx` in the `anim` animation. `duration` specifies the relative duration, see `get_frame_duration()<class_SpriteFrames_method_get_frame_duration>` for details.