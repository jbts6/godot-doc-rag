github_url
hide

# AnimationNodeStateMachine

**Inherits:** `AnimationRootNode<class_AnimationRootNode>` **\<** `AnimationNode<class_AnimationNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A state machine with multiple `AnimationRootNode<class_AnimationRootNode>`s, used by `AnimationTree<class_AnimationTree>`.

classref-introduction-group

## Description

Contains multiple `AnimationRootNode<class_AnimationRootNode>`s representing animation states, connected in a graph. State transitions can be configured to happen automatically or via code, using a shortest-path algorithm. Retrieve the `AnimationNodeStateMachinePlayback<class_AnimationNodeStateMachinePlayback>` object from the `AnimationTree<class_AnimationTree>` node to control it programmatically.

gdscript

var state_machine = \$AnimationTree.get("parameters/playback") state_machine.travel("some_state")

csharp

var stateMachine = GetNode\<AnimationTree\>("AnimationTree").Get("parameters/playback") as AnimationNodeStateMachinePlayback; stateMachine.Travel("some_state");

classref-introduction-group

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **StateMachineType**: `🔗<enum_AnimationNodeStateMachine_StateMachineType>`

classref-enumeration-constant

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>` **STATE_MACHINE_TYPE_ROOT** = `0`

Seeking to the beginning is treated as playing from the start state. Transition to the end state is treated as exiting the state machine.

classref-enumeration-constant

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>` **STATE_MACHINE_TYPE_NESTED** = `1`

Seeking to the beginning is treated as seeking to the beginning of the animation in the current state. Transition to the end state, or the absence of transitions in each state, is treated as exiting the state machine.

classref-enumeration-constant

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>` **STATE_MACHINE_TYPE_GROUPED** = `2`

This is a grouped state machine that can be controlled from a parent state machine. It does not work independently. There must be a state machine with `state_machine_type<class_AnimationNodeStateMachine_property_state_machine_type>` of `STATE_MACHINE_TYPE_ROOT<class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_ROOT>` or `STATE_MACHINE_TYPE_NESTED<class_AnimationNodeStateMachine_constant_STATE_MACHINE_TYPE_NESTED>` in the parent or ancestor.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **allow_transition_to_self** = `false` `🔗<class_AnimationNodeStateMachine_property_allow_transition_to_self>`

classref-property-setget

- `void (No return value.)` **set_allow_transition_to_self**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_allow_transition_to_self**()

If `true`, allows teleport to the self state with `AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`. When the reset option is enabled in `AnimationNodeStateMachinePlayback.travel()<class_AnimationNodeStateMachinePlayback_method_travel>`, the animation is restarted. If `false`, nothing happens on the teleportation to the self state.

classref-item-separator

classref-property

`bool<class_bool>` **reset_ends** = `false` `🔗<class_AnimationNodeStateMachine_property_reset_ends>`

classref-property-setget

- `void (No return value.)` **set_reset_ends**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_ends_reset**()

If `true`, treat the cross-fade to the start and end nodes as a blend with the RESET animation.

In most cases, when additional cross-fades are performed in the parent `AnimationNode<class_AnimationNode>` of the state machine, setting this property to `false` and matching the cross-fade time of the parent `AnimationNode<class_AnimationNode>` and the state machine's start node and end node gives good results.

classref-item-separator

classref-property

`StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>` **state_machine_type** = `0` `🔗<class_AnimationNodeStateMachine_property_state_machine_type>`

classref-property-setget

- `void (No return value.)` **set_state_machine_type**(value: `StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`)
- `StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>` **get_state_machine_type**()

This property can define the process of transitions for different use cases. See also `StateMachineType<enum_AnimationNodeStateMachine_StateMachineType>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_node**(name: `StringName<class_StringName>`, node: `AnimationNode<class_AnimationNode>`, position: `Vector2<class_Vector2>` = Vector2(0, 0)) `🔗<class_AnimationNodeStateMachine_method_add_node>`

Adds a new animation node to the graph. The `position` is used for display in the editor.

classref-item-separator

classref-method

`void (No return value.)` **add_transition**(from: `StringName<class_StringName>`, to: `StringName<class_StringName>`, transition: `AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>`) `🔗<class_AnimationNodeStateMachine_method_add_transition>`

Adds a transition between the given animation nodes.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_graph_offset**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_graph_offset>`

Returns the draw offset of the graph. Used for display in the editor.

classref-item-separator

classref-method

`AnimationNode<class_AnimationNode>` **get_node**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_node>`

Returns the animation node with the given name.

classref-item-separator

classref-method

`Array<class_Array>`\[`StringName<class_StringName>`\] **get_node_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_node_list>`

Returns a list containing the names of all animation nodes in this state machine.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_node_name**(node: `AnimationNode<class_AnimationNode>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_node_name>`

Returns the given animation node's name.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_node_position**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_node_position>`

Returns the given animation node's coordinates. Used for display in the editor.

classref-item-separator

classref-method

`AnimationNodeStateMachineTransition<class_AnimationNodeStateMachineTransition>` **get_transition**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_transition>`

Returns the given transition.

classref-item-separator

classref-method

`int<class_int>` **get_transition_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_transition_count>`

Returns the number of connections in the graph.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_transition_from**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_transition_from>`

Returns the given transition's start node.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_transition_to**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_get_transition_to>`

Returns the given transition's end node.

classref-item-separator

classref-method

`bool<class_bool>` **has_node**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_has_node>`

Returns `true` if the graph contains the given animation node.

classref-item-separator

classref-method

`bool<class_bool>` **has_transition**(from: `StringName<class_StringName>`, to: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AnimationNodeStateMachine_method_has_transition>`

Returns `true` if there is a transition between the given animation nodes.

classref-item-separator

classref-method

`void (No return value.)` **remove_node**(name: `StringName<class_StringName>`) `🔗<class_AnimationNodeStateMachine_method_remove_node>`

Deletes the given animation node from the graph.

classref-item-separator

classref-method

`void (No return value.)` **remove_transition**(from: `StringName<class_StringName>`, to: `StringName<class_StringName>`) `🔗<class_AnimationNodeStateMachine_method_remove_transition>`

Deletes the transition between the two specified animation nodes.

classref-item-separator

classref-method

`void (No return value.)` **remove_transition_by_index**(idx: `int<class_int>`) `🔗<class_AnimationNodeStateMachine_method_remove_transition_by_index>`

Deletes the given transition by index.

classref-item-separator

classref-method

`void (No return value.)` **rename_node**(name: `StringName<class_StringName>`, new_name: `StringName<class_StringName>`) `🔗<class_AnimationNodeStateMachine_method_rename_node>`

Renames the given animation node.

classref-item-separator

classref-method

`void (No return value.)` **replace_node**(name: `StringName<class_StringName>`, node: `AnimationNode<class_AnimationNode>`) `🔗<class_AnimationNodeStateMachine_method_replace_node>`

Replaces the given animation node with a new animation node.

classref-item-separator

classref-method

`void (No return value.)` **set_graph_offset**(offset: `Vector2<class_Vector2>`) `🔗<class_AnimationNodeStateMachine_method_set_graph_offset>`

Sets the draw offset of the graph. Used for display in the editor.

classref-item-separator

classref-method

`void (No return value.)` **set_node_position**(name: `StringName<class_StringName>`, position: `Vector2<class_Vector2>`) `🔗<class_AnimationNodeStateMachine_method_set_node_position>`

Sets the animation node's coordinates. Used for display in the editor.