github_url
hide

# GodotInstance

**Inherits:** `Object<class_Object>`

Provides access to an embedded Godot instance.

classref-introduction-group

## Description

GodotInstance represents a running Godot instance that is controlled from an outside codebase, without a perpetual main loop. It is created by the C API `libgodot_create_godot_instance`. Only one may be created per process.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **focus_in**() `🔗<class_GodotInstance_method_focus_in>`

Notifies the instance that it is now in focus.

classref-item-separator

classref-method

`void (No return value.)` **focus_out**() `🔗<class_GodotInstance_method_focus_out>`

Notifies the instance that it is now not in focus.

classref-item-separator

classref-method

`bool<class_bool>` **is_started**() `🔗<class_GodotInstance_method_is_started>`

Returns `true` if this instance has been fully started.

classref-item-separator

classref-method

`bool<class_bool>` **iteration**() `🔗<class_GodotInstance_method_iteration>`

Runs a single iteration of the main loop. Returns `true` if the engine is attempting to quit.

classref-item-separator

classref-method

`void (No return value.)` **pause**() `🔗<class_GodotInstance_method_pause>`

Notifies the instance that it is going to be paused.

classref-item-separator

classref-method

`void (No return value.)` **resume**() `🔗<class_GodotInstance_method_resume>`

Notifies the instance that it is being resumed.

classref-item-separator

classref-method

`bool<class_bool>` **start**() `🔗<class_GodotInstance_method_start>`

Finishes this instance's startup sequence. Returns `true` on success.