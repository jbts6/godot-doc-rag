github_url
hide

# ScriptBacktrace

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A captured backtrace of a specific script language.

classref-introduction-group

## Description

**ScriptBacktrace** holds an already captured backtrace of a specific script language, such as GDScript or C#, which are captured using `Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`.

See `ProjectSettings.debug/settings/gdscript/always_track_call_stacks<class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks>` and `ProjectSettings.debug/settings/gdscript/always_track_local_variables<class_ProjectSettings_property_debug/settings/gdscript/always_track_local_variables>` for ways of controlling the contents of this class.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **format**(indent_all: `int<class_int>` = 0, indent_frames: `int<class_int>` = 4) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_format>`

Converts the backtrace to a `String<class_String>`, where the entire string will be indented by `indent_all` number of spaces, and the individual stack frames will be additionally indented by `indent_frames` number of spaces.

**Note:** Calling `Object.to_string()<class_Object_method_to_string>` on a **ScriptBacktrace** will produce the same output as calling `format()<class_ScriptBacktrace_method_format>` with all parameters left at their default values.

classref-item-separator

classref-method

`int<class_int>` **get_frame_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_frame_count>`

Returns the number of stack frames in the backtrace.

classref-item-separator

classref-method

`String<class_String>` **get_frame_file**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_frame_file>`

Returns the file name of the call site represented by the stack frame at the specified index.

classref-item-separator

classref-method

`String<class_String>` **get_frame_function**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_frame_function>`

Returns the name of the function called at the stack frame at the specified index.

classref-item-separator

classref-method

`int<class_int>` **get_frame_line**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_frame_line>`

Returns the line number of the call site represented by the stack frame at the specified index.

classref-item-separator

classref-method

`int<class_int>` **get_global_variable_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_global_variable_count>`

Returns the number of global variables (e.g. autoload singletons) in the backtrace.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with `Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`.

classref-item-separator

classref-method

`String<class_String>` **get_global_variable_name**(variable_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_global_variable_name>`

Returns the name of the global variable at the specified index.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_global_variable_value**(variable_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_global_variable_value>`

Returns the value of the global variable at the specified index.

**Warning:** With GDScript backtraces, the returned `Variant<class_Variant>` will be the variable's actual value, including any object references. This means that storing the returned `Variant<class_Variant>` will prevent any such object from being deallocated, so it's generally recommended not to do so.

classref-item-separator

classref-method

`String<class_String>` **get_language_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_language_name>`

Returns the name of the script language that this backtrace was captured from.

classref-item-separator

classref-method

`int<class_int>` **get_local_variable_count**(frame_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_local_variable_count>`

Returns the number of local variables in the stack frame at the specified index.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with `Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`.

classref-item-separator

classref-method

`String<class_String>` **get_local_variable_name**(frame_index: `int<class_int>`, variable_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_local_variable_name>`

Returns the name of the local variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_local_variable_value**(frame_index: `int<class_int>`, variable_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_local_variable_value>`

Returns the value of the local variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

**Warning:** With GDScript backtraces, the returned `Variant<class_Variant>` will be the variable's actual value, including any object references. This means that storing the returned `Variant<class_Variant>` will prevent any such object from being deallocated, so it's generally recommended not to do so.

classref-item-separator

classref-method

`int<class_int>` **get_member_variable_count**(frame_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_member_variable_count>`

Returns the number of member variables in the stack frame at the specified index.

**Note:** This will be non-zero only if the `include_variables` parameter was `true` when capturing the backtrace with `Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`.

classref-item-separator

classref-method

`String<class_String>` **get_member_variable_name**(frame_index: `int<class_int>`, variable_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_member_variable_name>`

Returns the name of the member variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_member_variable_value**(frame_index: `int<class_int>`, variable_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_get_member_variable_value>`

Returns the value of the member variable at the specified `variable_index` in the stack frame at the specified `frame_index`.

**Warning:** With GDScript backtraces, the returned `Variant<class_Variant>` will be the variable's actual value, including any object references. This means that storing the returned `Variant<class_Variant>` will prevent any such object from being deallocated, so it's generally recommended not to do so.

classref-item-separator

classref-method

`bool<class_bool>` **is_empty**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptBacktrace_method_is_empty>`

Returns `true` if the backtrace has no stack frames.