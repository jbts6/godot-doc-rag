github_url
hide

# AnimatedSprite3D

**Inherits:** `SpriteBase3D<class_SpriteBase3D>` **\<** `GeometryInstance3D<class_GeometryInstance3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

2D sprite node in 3D world, that can use multiple 2D textures for animation.

classref-introduction-group

## Description

**AnimatedSprite3D** is similar to the `Sprite3D<class_Sprite3D>` node, except it carries multiple textures as animation `sprite_frames<class_AnimatedSprite3D_property_sprite_frames>`. Animations are created using a `SpriteFrames<class_SpriteFrames>` resource, which allows you to import image files (or a folder containing said files) to provide the animation frames for the sprite. The `SpriteFrames<class_SpriteFrames>` resource can be configured in the editor via the SpriteFrames bottom panel.

classref-introduction-group

## Tutorials

- `2D Sprite animation (also applies to 3D) <../tutorials/2d/2d_sprite_animation>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**animation_changed**() `🔗<class_AnimatedSprite3D_signal_animation_changed>`

Emitted when `animation<class_AnimatedSprite3D_property_animation>` changes.

classref-item-separator

classref-signal

**animation_finished**() `🔗<class_AnimatedSprite3D_signal_animation_finished>`

Emitted when the animation reaches the end, or the start if it is played in reverse. When the animation finishes, it pauses the playback.

**Note:** This signal is not emitted if an animation is looping.

classref-item-separator

classref-signal

**animation_looped**() `🔗<class_AnimatedSprite3D_signal_animation_looped>`

Emitted when the animation loops.

classref-item-separator

classref-signal

**frame_changed**() `🔗<class_AnimatedSprite3D_signal_frame_changed>`

Emitted when `frame<class_AnimatedSprite3D_property_frame>` changes.

classref-item-separator

classref-signal

**sprite_frames_changed**() `🔗<class_AnimatedSprite3D_signal_sprite_frames_changed>`

Emitted when `sprite_frames<class_AnimatedSprite3D_property_sprite_frames>` changes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`StringName<class_StringName>` **animation** = `&"default"` `🔗<class_AnimatedSprite3D_property_animation>`

classref-property-setget

- `void (No return value.)` **set_animation**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_animation**()

The current animation from the `sprite_frames<class_AnimatedSprite3D_property_sprite_frames>` resource. If this value is changed, the `frame<class_AnimatedSprite3D_property_frame>` counter and the `frame_progress<class_AnimatedSprite3D_property_frame_progress>` are reset.

classref-item-separator

classref-property

`String<class_String>` **autoplay** = `""` `🔗<class_AnimatedSprite3D_property_autoplay>`

classref-property-setget

- `void (No return value.)` **set_autoplay**(value: `String<class_String>`)
- `String<class_String>` **get_autoplay**()

The key of the animation to play when the scene loads.

classref-item-separator

classref-property

`int<class_int>` **frame** = `0` `🔗<class_AnimatedSprite3D_property_frame>`

classref-property-setget

- `void (No return value.)` **set_frame**(value: `int<class_int>`)
- `int<class_int>` **get_frame**()

The displayed animation frame's index. Setting this property also resets `frame_progress<class_AnimatedSprite3D_property_frame_progress>`. If this is not desired, use `set_frame_and_progress()<class_AnimatedSprite3D_method_set_frame_and_progress>`.

classref-item-separator

classref-property

`float<class_float>` **frame_progress** = `0.0` `🔗<class_AnimatedSprite3D_property_frame_progress>`

classref-property-setget

- `void (No return value.)` **set_frame_progress**(value: `float<class_float>`)
- `float<class_float>` **get_frame_progress**()

The progress value between `0.0` and `1.0` until the current frame transitions to the next frame. If the animation is playing backwards, the value transitions from `1.0` to `0.0`.

classref-item-separator

classref-property

`float<class_float>` **speed_scale** = `1.0` `🔗<class_AnimatedSprite3D_property_speed_scale>`

classref-property-setget

- `void (No return value.)` **set_speed_scale**(value: `float<class_float>`)
- `float<class_float>` **get_speed_scale**()

The speed scaling ratio. For example, if this value is `1`, then the animation plays at normal speed. If it's `0.5`, then it plays at half speed. If it's `2`, then it plays at double speed.

If set to a negative value, the animation is played in reverse. If set to `0`, the animation will not advance.

classref-item-separator

classref-property

`SpriteFrames<class_SpriteFrames>` **sprite_frames** `🔗<class_AnimatedSprite3D_property_sprite_frames>`

classref-property-setget

- `void (No return value.)` **set_sprite_frames**(value: `SpriteFrames<class_SpriteFrames>`)
- `SpriteFrames<class_SpriteFrames>` **get_sprite_frames**()

The `SpriteFrames<class_SpriteFrames>` resource containing the animation(s). Allows you the option to load, edit, clear, make unique and save the states of the `SpriteFrames<class_SpriteFrames>` resource.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_playing_speed**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimatedSprite3D_method_get_playing_speed>`

Returns the actual playing speed of current animation or `0` if not playing. This speed is the `speed_scale<class_AnimatedSprite3D_property_speed_scale>` property multiplied by `custom_speed` argument specified when calling the `play()<class_AnimatedSprite3D_method_play>` method.

Returns a negative value if the current animation is playing backwards.

classref-item-separator

classref-method

`bool<class_bool>` **is_playing**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimatedSprite3D_method_is_playing>`

Returns `true` if an animation is currently playing (even if `speed_scale<class_AnimatedSprite3D_property_speed_scale>` and/or `custom_speed` are `0`).

classref-item-separator

classref-method

`void (No return value.)` **pause**() `🔗<class_AnimatedSprite3D_method_pause>`

Pauses the currently playing animation. The `frame<class_AnimatedSprite3D_property_frame>` and `frame_progress<class_AnimatedSprite3D_property_frame_progress>` will be kept and calling `play()<class_AnimatedSprite3D_method_play>` or `play_backwards()<class_AnimatedSprite3D_method_play_backwards>` without arguments will resume the animation from the current playback position.

See also `stop()<class_AnimatedSprite3D_method_stop>`.

classref-item-separator

classref-method

`void (No return value.)` **play**(name: `StringName<class_StringName>` = &"", custom_speed: `float<class_float>` = 1.0, from_end: `bool<class_bool>` = false) `🔗<class_AnimatedSprite3D_method_play>`

Plays the animation with key `name`. If `custom_speed` is negative and `from_end` is `true`, the animation will play backwards (which is equivalent to calling `play_backwards()<class_AnimatedSprite3D_method_play_backwards>`).

If this method is called with that same animation `name`, or with no `name` parameter, the assigned animation will resume playing if it was paused.

classref-item-separator

classref-method

`void (No return value.)` **play_backwards**(name: `StringName<class_StringName>` = &"") `🔗<class_AnimatedSprite3D_method_play_backwards>`

Plays the animation with key `name` in reverse.

This method is a shorthand for `play()<class_AnimatedSprite3D_method_play>` with `custom_speed = -1.0` and `from_end = true`, so see its description for more information.

classref-item-separator

classref-method

`void (No return value.)` **set_frame_and_progress**(frame: `int<class_int>`, progress: `float<class_float>`) `🔗<class_AnimatedSprite3D_method_set_frame_and_progress>`

Sets `frame<class_AnimatedSprite3D_property_frame>` and `frame_progress<class_AnimatedSprite3D_property_frame_progress>` to the given values. Unlike setting `frame<class_AnimatedSprite3D_property_frame>`, this method does not reset the `frame_progress<class_AnimatedSprite3D_property_frame_progress>` to `0.0` implicitly.

**Example:** Change the animation while keeping the same `frame<class_AnimatedSprite3D_property_frame>` and `frame_progress<class_AnimatedSprite3D_property_frame_progress>`:

gdscript

var current_frame = animated_sprite.get_frame() var current_progress = animated_sprite.get_frame_progress() animated_sprite.play("walk_another_skin") animated_sprite.set_frame_and_progress(current_frame, current_progress)

classref-item-separator

classref-method

`void (No return value.)` **stop**() `🔗<class_AnimatedSprite3D_method_stop>`

Stops the currently playing animation. The animation position is reset to `0` and the `custom_speed` is reset to `1.0`. See also `pause()<class_AnimatedSprite3D_method_pause>`.