github_url
hide

# EngineDebugger

**Inherits:** `Object<class_Object>`

Exposes the internal debugger.

classref-introduction-group

## Description

**EngineDebugger** handles the communication between the editor and the running game. It is active in the running game. Messages can be sent/received through it. It also manages the profilers.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_breakpoints**() `🔗<class_EngineDebugger_method_clear_breakpoints>`

Clears all breakpoints.

classref-item-separator

classref-method

`void (No return value.)` **debug**(can_continue: `bool<class_bool>` = true, is_error_breakpoint: `bool<class_bool>` = false) `🔗<class_EngineDebugger_method_debug>`

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

classref-item-separator

classref-method

`int<class_int>` **get_depth**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EngineDebugger_method_get_depth>`

**Experimental:** This method may be changed or removed in future versions.

Returns the current debug depth.

classref-item-separator

classref-method

`int<class_int>` **get_lines_left**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EngineDebugger_method_get_lines_left>`

**Experimental:** This method may be changed or removed in future versions.

Returns the number of lines that remain.

classref-item-separator

classref-method

`bool<class_bool>` **has_capture**(name: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_has_capture>`

Returns `true` if a capture with the given name is present otherwise `false`.

classref-item-separator

classref-method

`bool<class_bool>` **has_profiler**(name: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_has_profiler>`

Returns `true` if a profiler with the given name is present otherwise `false`.

classref-item-separator

classref-method

`void (No return value.)` **insert_breakpoint**(line: `int<class_int>`, source: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_insert_breakpoint>`

Inserts a new breakpoint with the given `source` and `line`.

classref-item-separator

classref-method

`bool<class_bool>` **is_active**() `🔗<class_EngineDebugger_method_is_active>`

Returns `true` if the debugger is active otherwise `false`.

classref-item-separator

classref-method

`bool<class_bool>` **is_breakpoint**(line: `int<class_int>`, source: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EngineDebugger_method_is_breakpoint>`

Returns `true` if the given `source` and `line` represent an existing breakpoint.

classref-item-separator

classref-method

`bool<class_bool>` **is_profiling**(name: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_is_profiling>`

Returns `true` if a profiler with the given name is present and active otherwise `false`.

classref-item-separator

classref-method

`bool<class_bool>` **is_skipping_breakpoints**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EngineDebugger_method_is_skipping_breakpoints>`

Returns `true` if the debugger is skipping breakpoints otherwise `false`.

classref-item-separator

classref-method

`void (No return value.)` **line_poll**() `🔗<class_EngineDebugger_method_line_poll>`

Forces a processing loop of debugger events. The purpose of this method is just processing events every now and then when the script might get too busy, so that bugs like infinite loops can be caught.

classref-item-separator

classref-method

`void (No return value.)` **profiler_add_frame_data**(name: `StringName<class_StringName>`, data: `Array<class_Array>`) `🔗<class_EngineDebugger_method_profiler_add_frame_data>`

Calls the `add` callable of the profiler with given `name` and `data`.

classref-item-separator

classref-method

`void (No return value.)` **profiler_enable**(name: `StringName<class_StringName>`, enable: `bool<class_bool>`, arguments: `Array<class_Array>` = \[\]) `🔗<class_EngineDebugger_method_profiler_enable>`

Calls the `toggle` callable of the profiler with given `name` and `arguments`. Enables/Disables the same profiler depending on `enable` argument.

classref-item-separator

classref-method

`void (No return value.)` **register_message_capture**(name: `StringName<class_StringName>`, callable: `Callable<class_Callable>`) `🔗<class_EngineDebugger_method_register_message_capture>`

Registers a message capture with given `name`. If `name` is "my_message" then messages starting with "my_message:" will be called with the given callable.

The callable must accept a message string and a data array as argument. The callable should return `true` if the message is recognized.

**Note:** The callable will receive the message with the prefix stripped, unlike `EditorDebuggerPlugin._capture()<class_EditorDebuggerPlugin_private_method__capture>`. See the `EditorDebuggerPlugin<class_EditorDebuggerPlugin>` description for an example.

classref-item-separator

classref-method

`void (No return value.)` **register_profiler**(name: `StringName<class_StringName>`, profiler: `EngineProfiler<class_EngineProfiler>`) `🔗<class_EngineDebugger_method_register_profiler>`

Registers a profiler with the given `name`. See `EngineProfiler<class_EngineProfiler>` for more information.

classref-item-separator

classref-method

`void (No return value.)` **remove_breakpoint**(line: `int<class_int>`, source: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_remove_breakpoint>`

Removes a breakpoint with the given `source` and `line`.

classref-item-separator

classref-method

`void (No return value.)` **script_debug**(language: `ScriptLanguage<class_ScriptLanguage>`, can_continue: `bool<class_bool>` = true, is_error_breakpoint: `bool<class_bool>` = false) `🔗<class_EngineDebugger_method_script_debug>`

Starts a debug break in script execution, optionally specifying whether the program can continue based on `can_continue` and whether the break was due to a breakpoint.

classref-item-separator

classref-method

`void (No return value.)` **send_message**(message: `String<class_String>`, data: `Array<class_Array>`) `🔗<class_EngineDebugger_method_send_message>`

Sends a message with given `message` and `data` array.

classref-item-separator

classref-method

`void (No return value.)` **set_depth**(depth: `int<class_int>`) `🔗<class_EngineDebugger_method_set_depth>`

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging depth.

classref-item-separator

classref-method

`void (No return value.)` **set_lines_left**(lines: `int<class_int>`) `🔗<class_EngineDebugger_method_set_lines_left>`

**Experimental:** This method may be changed or removed in future versions.

Sets the current debugging lines that remain.

classref-item-separator

classref-method

`void (No return value.)` **unregister_message_capture**(name: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_unregister_message_capture>`

Unregisters the message capture with given `name`.

classref-item-separator

classref-method

`void (No return value.)` **unregister_profiler**(name: `StringName<class_StringName>`) `🔗<class_EngineDebugger_method_unregister_profiler>`

Unregisters a profiler with given `name`.