github_url
hide

# Timer

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

A countdown timer.

classref-introduction-group

## Description

The **Timer** node is a countdown timer and is the simplest way to handle time-based logic in the engine. When a timer reaches the end of its `wait_time<class_Timer_property_wait_time>`, it will emit the `timeout<class_Timer_signal_timeout>` signal.

After a timer enters the scene tree, it can be manually started with `start()<class_Timer_method_start>`. A timer node is also started automatically if `autostart<class_Timer_property_autostart>` is `true`.

Without requiring much code, a timer node can be added and configured in the editor. The `timeout<class_Timer_signal_timeout>` signal it emits can also be connected through the Signals dock in the editor:

    func _on_timer_timeout():
        print("Time to attack!")

**Note:** To create a one-shot timer without instantiating a node, use `SceneTree.create_timer()<class_SceneTree_method_create_timer>`.

**Note:** Timers are affected by `Engine.time_scale<class_Engine_property_time_scale>` unless `ignore_time_scale<class_Timer_property_ignore_time_scale>` is `true`. The higher the time scale, the sooner timers will end. How often a timer processes may depend on the framerate or `Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`.

classref-introduction-group

## Tutorials

- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**timeout**() `🔗<class_Timer_signal_timeout>`

Emitted when the timer reaches the end.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **TimerProcessCallback**: `🔗<enum_Timer_TimerProcessCallback>`

classref-enumeration-constant

`TimerProcessCallback<enum_Timer_TimerProcessCallback>` **TIMER_PROCESS_PHYSICS** = `0`

Update the timer every physics process frame (see `Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`).

classref-enumeration-constant

`TimerProcessCallback<enum_Timer_TimerProcessCallback>` **TIMER_PROCESS_IDLE** = `1`

Update the timer every process (rendered) frame (see `Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **autostart** = `false` `🔗<class_Timer_property_autostart>`

classref-property-setget

- `void (No return value.)` **set_autostart**(value: `bool<class_bool>`)
- `bool<class_bool>` **has_autostart**()

If `true`, the timer will start immediately when it enters the scene tree.

**Note:** After the timer enters the tree, this property is automatically set to `false`.

**Note:** This property does nothing when the timer is running in the editor.

classref-item-separator

classref-property

`bool<class_bool>` **ignore_time_scale** = `false` `🔗<class_Timer_property_ignore_time_scale>`

classref-property-setget

- `void (No return value.)` **set_ignore_time_scale**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_ignoring_time_scale**()

If `true`, the timer will ignore `Engine.time_scale<class_Engine_property_time_scale>` and update with the real, elapsed time.

classref-item-separator

classref-property

`bool<class_bool>` **one_shot** = `false` `🔗<class_Timer_property_one_shot>`

classref-property-setget

- `void (No return value.)` **set_one_shot**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_one_shot**()

If `true`, the timer will stop after reaching the end. Otherwise, as by default, the timer will automatically restart.

classref-item-separator

classref-property

`bool<class_bool>` **paused** `🔗<class_Timer_property_paused>`

classref-property-setget

- `void (No return value.)` **set_paused**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_paused**()

If `true`, the timer is paused. A paused timer does not process until this property is set back to `false`, even when `start()<class_Timer_method_start>` is called. See also `stop()<class_Timer_method_stop>`.

classref-item-separator

classref-property

`TimerProcessCallback<enum_Timer_TimerProcessCallback>` **process_callback** = `1` `🔗<class_Timer_property_process_callback>`

classref-property-setget

- `void (No return value.)` **set_timer_process_callback**(value: `TimerProcessCallback<enum_Timer_TimerProcessCallback>`)
- `TimerProcessCallback<enum_Timer_TimerProcessCallback>` **get_timer_process_callback**()

Specifies when the timer is updated during the main loop.

classref-item-separator

classref-property

`float<class_float>` **time_left** `🔗<class_Timer_property_time_left>`

classref-property-setget

- `float<class_float>` **get_time_left**()

The timer's remaining time in seconds. This is always `0` if the timer is stopped.

**Note:** This property is read-only and cannot be modified. It is based on `wait_time<class_Timer_property_wait_time>`.

classref-item-separator

classref-property

`float<class_float>` **wait_time** = `1.0` `🔗<class_Timer_property_wait_time>`

classref-property-setget

- `void (No return value.)` **set_wait_time**(value: `float<class_float>`)
- `float<class_float>` **get_wait_time**()

The time required for the timer to end, in seconds. This property can also be set every time `start()<class_Timer_method_start>` is called.

**Note:** Timers can only process once per physics or process frame (depending on the `process_callback<class_Timer_property_process_callback>`). An unstable framerate may cause the timer to end inconsistently, which is especially noticeable if the wait time is lower than roughly `0.05` seconds. For very short timers, it is recommended to write your own code instead of using a **Timer** node. Timers are also affected by `Engine.time_scale<class_Engine_property_time_scale>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_stopped**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Timer_method_is_stopped>`

Returns `true` if the timer is stopped or has not started.

classref-item-separator

classref-method

`void (No return value.)` **start**(time_sec: `float<class_float>` = -1) `🔗<class_Timer_method_start>`

Starts the timer, or resets the timer if it was started already. Fails if the timer is not inside the scene tree. If `time_sec` is greater than `0`, this value is used for the `wait_time<class_Timer_property_wait_time>`.

**Note:** This method does not resume a paused timer. See `paused<class_Timer_property_paused>`.

classref-item-separator

classref-method

`void (No return value.)` **stop**() `🔗<class_Timer_method_stop>`

Stops the timer. See also `paused<class_Timer_property_paused>`. Unlike `start()<class_Timer_method_start>`, this can safely be called if the timer is not inside the scene tree.

**Note:** Calling `stop()<class_Timer_method_stop>` does not emit the `timeout<class_Timer_signal_timeout>` signal, as the timer is not considered to have timed out. If this is desired, use `$Timer.timeout.emit()` after calling `stop()<class_Timer_method_stop>` to manually emit the signal.