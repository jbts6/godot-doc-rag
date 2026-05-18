github_url
hide

# EngineProfiler

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Base class for creating custom profilers.

classref-introduction-group

## Description

This class can be used to implement custom profilers that are able to interact with the engine and editor debugger.

See `EngineDebugger<class_EngineDebugger>` and `EditorDebuggerPlugin<class_EditorDebuggerPlugin>` for more information.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_add_frame**(data: `Array<class_Array>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EngineProfiler_private_method__add_frame>`

Called when data is added to profiler using `EngineDebugger.profiler_add_frame_data()<class_EngineDebugger_method_profiler_add_frame_data>`.

classref-item-separator

classref-method

`void (No return value.)` **\_tick**(frame_time: `float<class_float>`, process_time: `float<class_float>`, physics_time: `float<class_float>`, physics_frame_time: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EngineProfiler_private_method__tick>`

Called once every engine iteration when the profiler is active with information about the current frame. All time values are in seconds. Lower values represent faster processing times and are therefore considered better.

classref-item-separator

classref-method

`void (No return value.)` **\_toggle**(enable: `bool<class_bool>`, options: `Array<class_Array>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EngineProfiler_private_method__toggle>`

Called when the profiler is enabled/disabled, along with a set of `options`.