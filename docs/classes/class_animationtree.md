github_url
hide

# AnimationTree

**Inherits:** `AnimationMixer<class_AnimationMixer>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A node used for advanced animation transitions in an `AnimationPlayer<class_AnimationPlayer>`.

classref-introduction-group

## Description

A node used for advanced animation transitions in an `AnimationPlayer<class_AnimationPlayer>`.

**Note:** When linked with an `AnimationPlayer<class_AnimationPlayer>`, several properties and methods of the corresponding `AnimationPlayer<class_AnimationPlayer>` will not function as expected. Playback and transitions should be handled using only the **AnimationTree** and its constituent `AnimationNode<class_AnimationNode>`(s). The `AnimationPlayer<class_AnimationPlayer>` node should be used solely for adding, deleting, and editing animations.

classref-introduction-group

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**animation_player_changed**() `🔗<class_AnimationTree_signal_animation_player_changed>`

Emitted when the `anim_player<class_AnimationTree_property_anim_player>` is changed.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **AnimationProcessCallback**: `🔗<enum_AnimationTree_AnimationProcessCallback>`

classref-enumeration-constant

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>` **ANIMATION_PROCESS_PHYSICS** = `0`

**Deprecated:** See `AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS>`.

classref-enumeration-constant

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>` **ANIMATION_PROCESS_IDLE** = `1`

**Deprecated:** See `AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_IDLE<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_IDLE>`.

classref-enumeration-constant

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>` **ANIMATION_PROCESS_MANUAL** = `2`

**Deprecated:** See `AnimationMixer.ANIMATION_CALLBACK_MODE_PROCESS_MANUAL<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_MANUAL>`.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`NodePath<class_NodePath>` **advance_expression_base_node** = `NodePath(".")` `🔗<class_AnimationTree_property_advance_expression_base_node>`

classref-property-setget

- `void (No return value.)` **set_advance_expression_base_node**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_advance_expression_base_node**()

The path to the `Node<class_Node>` used to evaluate the `AnimationNode<class_AnimationNode>` `Expression<class_Expression>` if one is not explicitly specified internally.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **anim_player** = `NodePath("")` `🔗<class_AnimationTree_property_anim_player>`

classref-property-setget

- `void (No return value.)` **set_animation_player**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_animation_player**()

The path to the `AnimationPlayer<class_AnimationPlayer>` used for animating.

classref-item-separator

classref-property

`AnimationRootNode<class_AnimationRootNode>` **tree_root** `🔗<class_AnimationTree_property_tree_root>`

classref-property-setget

- `void (No return value.)` **set_tree_root**(value: `AnimationRootNode<class_AnimationRootNode>`)
- `AnimationRootNode<class_AnimationRootNode>` **get_tree_root**()

The root animation node of this **AnimationTree**. See `AnimationRootNode<class_AnimationRootNode>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>` **get_process_callback**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationTree_method_get_process_callback>`

**Deprecated:** Use `AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>` instead.

Returns the process notification in which to update animations.

classref-item-separator

classref-method

`void (No return value.)` **set_process_callback**(mode: `AnimationProcessCallback<enum_AnimationTree_AnimationProcessCallback>`) `🔗<class_AnimationTree_method_set_process_callback>`

**Deprecated:** Use `AnimationMixer.callback_mode_process<class_AnimationMixer_property_callback_mode_process>` instead.

Sets the process notification in which to update animations.