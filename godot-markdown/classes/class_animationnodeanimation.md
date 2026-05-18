github_url
hide

# AnimationNodeAnimation

**Inherits:** `AnimationRootNode<class_AnimationRootNode>` **\<** `AnimationNode<class_AnimationNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

An input animation for an `AnimationNodeBlendTree<class_AnimationNodeBlendTree>`.

classref-introduction-group

## Description

A resource to add to an `AnimationNodeBlendTree<class_AnimationNodeBlendTree>`. Only has one output port using the `animation<class_AnimationNodeAnimation_property_animation>` property. Used as an input for `AnimationNode<class_AnimationNode>`s that blend animations together.

classref-introduction-group

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **PlayMode**: `🔗<enum_AnimationNodeAnimation_PlayMode>`

classref-enumeration-constant

`PlayMode<enum_AnimationNodeAnimation_PlayMode>` **PLAY_MODE_FORWARD** = `0`

Plays animation in forward direction.

classref-enumeration-constant

`PlayMode<enum_AnimationNodeAnimation_PlayMode>` **PLAY_MODE_BACKWARD** = `1`

Plays animation in backward direction.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **advance_on_start** = `false` `🔗<class_AnimationNodeAnimation_property_advance_on_start>`

classref-property-setget

- `void (No return value.)` **set_advance_on_start**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_advance_on_start**()

If `true`, on receiving a request to play an animation from the start, the first frame is not drawn, but only processed, and playback starts from the next frame.

See also the notes of `AnimationPlayer.play()<class_AnimationPlayer_method_play>`.

classref-item-separator

classref-property

`StringName<class_StringName>` **animation** = `&""` `🔗<class_AnimationNodeAnimation_property_animation>`

classref-property-setget

- `void (No return value.)` **set_animation**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_animation**()

Animation to use as an output. It is one of the animations provided by `AnimationTree.anim_player<class_AnimationTree_property_anim_player>`.

classref-item-separator

classref-property

`LoopMode<enum_Animation_LoopMode>` **loop_mode** `🔗<class_AnimationNodeAnimation_property_loop_mode>`

classref-property-setget

- `void (No return value.)` **set_loop_mode**(value: `LoopMode<enum_Animation_LoopMode>`)
- `LoopMode<enum_Animation_LoopMode>` **get_loop_mode**()

If `use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>` is `true`, override the loop settings of the original `Animation<class_Animation>` resource with the value.

**Note:** If the `Animation.loop_mode<class_Animation_property_loop_mode>` isn't set to looping, the `Animation.track_set_interpolation_loop_wrap()<class_Animation_method_track_set_interpolation_loop_wrap>` option will not be respected. If you cannot get the expected behavior, consider duplicating the `Animation<class_Animation>` resource and changing the loop settings.

classref-item-separator

classref-property

`PlayMode<enum_AnimationNodeAnimation_PlayMode>` **play_mode** = `0` `🔗<class_AnimationNodeAnimation_property_play_mode>`

classref-property-setget

- `void (No return value.)` **set_play_mode**(value: `PlayMode<enum_AnimationNodeAnimation_PlayMode>`)
- `PlayMode<enum_AnimationNodeAnimation_PlayMode>` **get_play_mode**()

Determines the playback direction of the animation.

classref-item-separator

classref-property

`float<class_float>` **start_offset** `🔗<class_AnimationNodeAnimation_property_start_offset>`

classref-property-setget

- `void (No return value.)` **set_start_offset**(value: `float<class_float>`)
- `float<class_float>` **get_start_offset**()

If `use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>` is `true`, offset the start position of the animation.

This is useful for adjusting which foot steps first in 3D walking animations.

classref-item-separator

classref-property

`bool<class_bool>` **stretch_time_scale** `🔗<class_AnimationNodeAnimation_property_stretch_time_scale>`

classref-property-setget

- `void (No return value.)` **set_stretch_time_scale**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_stretching_time_scale**()

If `true`, scales the time so that the length specified in `timeline_length<class_AnimationNodeAnimation_property_timeline_length>` is one cycle.

This is useful for matching the periods of walking and running animations.

If `false`, the original animation length is respected. If you set the loop to `loop_mode<class_AnimationNodeAnimation_property_loop_mode>`, the animation will loop in `timeline_length<class_AnimationNodeAnimation_property_timeline_length>`.

classref-item-separator

classref-property

`float<class_float>` **timeline_length** `🔗<class_AnimationNodeAnimation_property_timeline_length>`

classref-property-setget

- `void (No return value.)` **set_timeline_length**(value: `float<class_float>`)
- `float<class_float>` **get_timeline_length**()

The length of the custom timeline.

If `stretch_time_scale<class_AnimationNodeAnimation_property_stretch_time_scale>` is `true`, scales the animation to this length.

classref-item-separator

classref-property

`bool<class_bool>` **use_custom_timeline** = `false` `🔗<class_AnimationNodeAnimation_property_use_custom_timeline>`

classref-property-setget

- `void (No return value.)` **set_use_custom_timeline**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_custom_timeline**()

If `true`, `AnimationNode<class_AnimationNode>` provides an animation based on the `Animation<class_Animation>` resource with some parameters adjusted.