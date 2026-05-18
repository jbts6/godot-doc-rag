github_url
hide

# AnimationLibrary

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Container for `Animation<class_Animation>` resources.

classref-introduction-group

## Description

An animation library stores a set of animations accessible through `StringName<class_StringName>` keys, for use with `AnimationPlayer<class_AnimationPlayer>` nodes.

classref-introduction-group

## Tutorials

- `Animation tutorial index <../tutorials/animation/index>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**animation_added**(anim_name: `StringName<class_StringName>`) `🔗<class_AnimationLibrary_signal_animation_added>`

Emitted when an `Animation<class_Animation>` is added, under the key `anim_name`.

classref-item-separator

classref-signal

**animation_changed**(anim_name: `StringName<class_StringName>`) `🔗<class_AnimationLibrary_signal_animation_changed>`

Emitted when there's a change in one of the animations, e.g. tracks are added, moved or have changed paths. `anim_name` is the key of the animation that was changed.

See also `Resource.changed<class_Resource_signal_changed>`, which this acts as a relay for.

classref-item-separator

classref-signal

**animation_removed**(anim_name: `StringName<class_StringName>`) `🔗<class_AnimationLibrary_signal_animation_removed>`

Emitted when an `Animation<class_Animation>` stored with the key `anim_name` is removed.

classref-item-separator

classref-signal

**animation_renamed**(old_name: `StringName<class_StringName>`, new_name: `StringName<class_StringName>`) `🔗<class_AnimationLibrary_signal_animation_renamed>`

Emitted when the key for an `Animation<class_Animation>` is changed, from `old_name` to `new_name`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Error<enum_@GlobalScope_Error>` **add_animation**(name: `StringName<class_StringName>`, animation: `Animation<class_Animation>`) `🔗<class_AnimationLibrary_method_add_animation>`

Adds the `animation` to the library, accessible by the key `name`.

classref-item-separator

classref-method

`Animation<class_Animation>` **get_animation**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationLibrary_method_get_animation>`

Returns the `Animation<class_Animation>` with the key `name`. If the animation does not exist, `null` is returned and an error is logged.

classref-item-separator

classref-method

`Array<class_Array>`\[`StringName<class_StringName>`\] **get_animation_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationLibrary_method_get_animation_list>`

Returns the keys for the `Animation<class_Animation>`s stored in the library.

classref-item-separator

classref-method

`int<class_int>` **get_animation_list_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationLibrary_method_get_animation_list_size>`

Returns the key count for the `Animation<class_Animation>`s stored in the library.

classref-item-separator

classref-method

`bool<class_bool>` **has_animation**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationLibrary_method_has_animation>`

Returns `true` if the library stores an `Animation<class_Animation>` with `name` as the key.

classref-item-separator

classref-method

`void (No return value.)` **remove_animation**(name: `StringName<class_StringName>`) `🔗<class_AnimationLibrary_method_remove_animation>`

Removes the `Animation<class_Animation>` with the key `name`.

classref-item-separator

classref-method

`void (No return value.)` **rename_animation**(name: `StringName<class_StringName>`, newname: `StringName<class_StringName>`) `🔗<class_AnimationLibrary_method_rename_animation>`

Changes the key of the `Animation<class_Animation>` associated with the key `name` to `newname`.