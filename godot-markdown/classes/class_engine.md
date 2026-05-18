github_url
hide

# Engine

**Inherits:** `Object<class_Object>`

Provides access to engine properties.

classref-introduction-group

## Description

The **Engine** singleton allows you to query and modify the project's run-time parameters, such as frames per second, time scale, and others. It also stores information about the current build of Godot, such as the current version.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **max_fps** = `0` `🔗<class_Engine_property_max_fps>`

classref-property-setget

- `void (No return value.)` **set_max_fps**(value: `int<class_int>`)
- `int<class_int>` **get_max_fps**()

The maximum number of frames that can be rendered every second (FPS). A value of `0` means the framerate is uncapped.

Limiting the FPS can be useful to reduce the host machine's power consumption, which reduces heat, noise emissions, and improves battery life.

If `ProjectSettings.display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>` is **Enabled** or **Adaptive**, the setting takes precedence and the max FPS number cannot exceed the monitor's refresh rate. See also `DisplayServer.screen_get_refresh_rate()<class_DisplayServer_method_screen_get_refresh_rate>`.

If `ProjectSettings.display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>` is **Enabled**, on monitors with variable refresh rate enabled (G-Sync/FreeSync), using an FPS limit a few frames lower than the monitor's refresh rate will [reduce input lag while avoiding tearing](https://blurbusters.com/howto-low-lag-vsync-on/). At higher refresh rates, the difference between the FPS limit and the monitor refresh rate should be increased to ensure frames to account for timing inaccuracies. The optimal formula for the FPS limit value in this scenario is `r - (r * r) / 3600.0`, where `r` is the monitor's refresh rate.

**Note:** The actual number of frames per second may still be below this value if the CPU or GPU cannot keep up with the project's logic and rendering.

**Note:** If `ProjectSettings.display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>` is **Disabled**, limiting the FPS to a high value that can be consistently reached on the system can reduce input lag compared to an uncapped framerate. Since this works by ensuring the GPU load is lower than 100%, this latency reduction is only effective in GPU-bottlenecked scenarios, not CPU-bottlenecked scenarios.

classref-item-separator

classref-property

`int<class_int>` **max_physics_steps_per_frame** = `8` `🔗<class_Engine_property_max_physics_steps_per_frame>`

classref-property-setget

- `void (No return value.)` **set_max_physics_steps_per_frame**(value: `int<class_int>`)
- `int<class_int>` **get_max_physics_steps_per_frame**()

The maximum number of physics steps that can be simulated each rendered frame.

**Note:** The default value is tuned to prevent expensive physics simulations from triggering even more expensive simulations indefinitely. However, the game will appear to slow down if the rendering FPS is less than `1 / max_physics_steps_per_frame` of `physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`. This occurs even if `delta` is consistently used in physics calculations. To avoid this, increase `max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>` if you have increased `physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>` significantly above its default value.

classref-item-separator

classref-property

`float<class_float>` **physics_jitter_fix** = `0.5` `🔗<class_Engine_property_physics_jitter_fix>`

classref-property-setget

- `void (No return value.)` **set_physics_jitter_fix**(value: `float<class_float>`)
- `float<class_float>` **get_physics_jitter_fix**()

How much physics ticks are synchronized with real time. If `0` or less, the ticks are fully synchronized. Higher values cause the in-game clock to deviate more from the real clock, but they smooth out framerate jitters.

**Note:** The default value of `0.5` should be good enough for most cases; values above `2` could cause the game to react to dropped frames with a noticeable delay and are not recommended.

**Note:** When using a custom physics interpolation solution, or within a network game, it's recommended to disable the physics jitter fix by setting this property to `0`.

classref-item-separator

classref-property

`int<class_int>` **physics_ticks_per_second** = `60` `🔗<class_Engine_property_physics_ticks_per_second>`

classref-property-setget

- `void (No return value.)` **set_physics_ticks_per_second**(value: `int<class_int>`)
- `int<class_int>` **get_physics_ticks_per_second**()

The number of fixed iterations per second. This controls how often physics simulation and the `Node._physics_process()<class_Node_private_method__physics_process>` method are run.

CPU usage scales approximately with the physics tick rate. However, at very low tick rates (usually below 30), physics behavior can break down. Input can also become less responsive at low tick rates as there can be a gap between input being registered, and the response on the next physics tick. High tick rates give more accurate physics simulation, particularly for fast moving objects. For example, racing games may benefit from increasing the tick rate above the default 60.

See also `max_fps<class_Engine_property_max_fps>` and `ProjectSettings.physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`.

**Note:** Only `max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>` physics ticks may be simulated per rendered frame at most. If more physics ticks have to be simulated per rendered frame to keep up with rendering, the project will appear to slow down (even if `delta` is used consistently in physics calculations). Therefore, it is recommended to also increase `max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>` if increasing `physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>` significantly above its default value.

**Note:** Consider enabling `physics interpolation <../tutorials/physics/interpolation/index>` if you change `physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>` to a value that is not a multiple of `60`. Using physics interpolation will avoid jittering when the monitor refresh rate and physics update rate don't exactly match.

classref-item-separator

classref-property

`bool<class_bool>` **print_error_messages** = `true` `🔗<class_Engine_property_print_error_messages>`

classref-property-setget

- `void (No return value.)` **set_print_error_messages**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_printing_error_messages**()

If `false`, stops printing error and warning messages to the console and editor Output log. This can be used to hide error and warning messages during unit test suite runs. This property is equivalent to the `ProjectSettings.application/run/disable_stderr<class_ProjectSettings_property_application/run/disable_stderr>` project setting.

**Note:** This property does not impact the editor's Errors tab when running a project from the editor.

**Warning:** If set to `false` anywhere in the project, important error messages may be hidden even if they are emitted from other scripts. In a `@tool` script, this will also impact the editor itself. Do *not* report bugs before ensuring error messages are enabled (as they are by default).

classref-item-separator

classref-property

`bool<class_bool>` **print_to_stdout** = `true` `🔗<class_Engine_property_print_to_stdout>`

classref-property-setget

- `void (No return value.)` **set_print_to_stdout**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_printing_to_stdout**()

If `false`, stops printing messages (for example using `@GlobalScope.print()<class_@GlobalScope_method_print>`) to the console, log files, and editor Output log. This property is equivalent to the `ProjectSettings.application/run/disable_stdout<class_ProjectSettings_property_application/run/disable_stdout>` project setting.

**Note:** This does not stop printing errors or warnings produced by scripts to the console or log files, for more details see `print_error_messages<class_Engine_property_print_error_messages>`.

classref-item-separator

classref-property

`float<class_float>` **time_scale** = `1.0` `🔗<class_Engine_property_time_scale>`

classref-property-setget

- `void (No return value.)` **set_time_scale**(value: `float<class_float>`)
- `float<class_float>` **get_time_scale**()

The speed multiplier at which the in-game clock updates, compared to real time. For example, if set to `2.0` the game runs twice as fast, and if set to `0.5` the game runs half as fast.

This value affects `Timer<class_Timer>`, `SceneTreeTimer<class_SceneTreeTimer>`, and all other simulations that make use of `delta` time (such as `Node._process()<class_Node_private_method__process>` and `Node._physics_process()<class_Node_private_method__physics_process>`).

**Note:** It's recommended to keep this property above `0.0`, as the game may behave unexpectedly otherwise.

**Note:** This does not affect audio playback speed. Use `AudioServer.playback_speed_scale<class_AudioServer_property_playback_speed_scale>` to adjust audio playback speed independently of `time_scale<class_Engine_property_time_scale>`.

**Note:** This does not automatically adjust `physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`. With values above `1.0` physics simulation may become less precise, as each physics tick will stretch over a larger period of engine time. If you're modifying `time_scale<class_Engine_property_time_scale>` to speed up simulation by a large factor, consider also increasing `physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>` to make the simulation more reliable.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Array<class_Array>`\[`ScriptBacktrace<class_ScriptBacktrace>`\] **capture_script_backtraces**(include_variables: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_capture_script_backtraces>`

Captures and returns backtraces from all registered script languages.

By default, the returned `ScriptBacktrace<class_ScriptBacktrace>` will only contain stack frames in editor builds and debug builds. To enable them for release builds as well, you need to enable `ProjectSettings.debug/settings/gdscript/always_track_call_stacks<class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks>`.

If `include_variables` is `true`, the backtrace will also include the names and values of any global variables (e.g. autoload singletons) at the point of the capture, as well as local variables and class member variables at each stack frame. This will however will only be respected when running the game with a debugger attached, like when running the game from the editor. To enable it for export builds as well, you need to enable `ProjectSettings.debug/settings/gdscript/always_track_local_variables<class_ProjectSettings_property_debug/settings/gdscript/always_track_local_variables>`.

**Warning:** When `include_variables` is `true`, any captured variables can potentially (e.g. with GDScript backtraces) be their actual values, including any object references. This means that storing such a `ScriptBacktrace<class_ScriptBacktrace>` will prevent those objects from being deallocated, so it's generally recommended not to do so.

classref-item-separator

classref-method

`String<class_String>` **get_architecture_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_architecture_name>`

Returns the name of the CPU architecture the Godot binary was built for. Possible return values include `"x86_64"`, `"x86_32"`, `"arm64"`, `"arm32"`, `"rv64"`, `"ppc64"`, `"loongarch64"`, `"wasm64"`, and `"wasm32"`.

To detect whether the current build is 64-bit, or the type of architecture, don't use the architecture name. Instead, use `OS.has_feature()<class_OS_method_has_feature>` to check for the `"64"` feature tag, or tags such as `"x86"` or `"arm"`. See the `Feature Tags <../tutorials/export/feature_tags>` documentation for more details.

**Note:** This method does *not* return the name of the system's CPU architecture (like `OS.get_processor_name()<class_OS_method_get_processor_name>`). For example, when running an `x86_32` Godot binary on an `x86_64` system, the returned value will still be `"x86_32"`.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_author_info**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_author_info>`

Returns the engine author information as a `Dictionary<class_Dictionary>`, where each entry is an `Array<class_Array>` of strings with the names of notable contributors to the Godot Engine: `lead_developers`, `founders`, `project_managers`, and `developers`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_copyright_info**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_copyright_info>`

Returns an `Array<class_Array>` of dictionaries with copyright information for every component of Godot's source code.

Every `Dictionary<class_Dictionary>` contains a `name` identifier, and a `parts` array of dictionaries. It describes the component in detail with the following entries:

- `files` - `Array<class_Array>` of file paths from the source code affected by this component;
- `copyright` - `Array<class_Array>` of owners of this component;
- `license` - The license applied to this component (such as "\`Expat \<https://en.wikipedia.org/wiki/MIT_License#Ambiguity_and_variants\>\`\_\_" or "\`CC-BY-4.0 \<https://creativecommons.org/licenses/by/4.0/\>\`\_\_").

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_donor_info**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_donor_info>`

Returns a `Dictionary<class_Dictionary>` of categorized donor names. Each entry is an `Array<class_Array>` of strings:

{`platinum_sponsors`, `gold_sponsors`, `silver_sponsors`, `bronze_sponsors`, `mini_sponsors`, `gold_donors`, `silver_donors`, `bronze_donors`}

classref-item-separator

classref-method

`int<class_int>` **get_frames_drawn**() `🔗<class_Engine_method_get_frames_drawn>`

Returns the total number of frames drawn since the engine started.

**Note:** On headless platforms, or if rendering is disabled with `--disable-render-loop` via command line, this method always returns `0`. See also `get_process_frames()<class_Engine_method_get_process_frames>`.

classref-item-separator

classref-method

`float<class_float>` **get_frames_per_second**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_frames_per_second>`

Returns the average frames rendered every second (FPS), also known as the framerate.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_license_info**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_license_info>`

Returns a `Dictionary<class_Dictionary>` of licenses used by Godot and included third party components. Each entry is a license name (such as "\`Expat \<https://en.wikipedia.org/wiki/MIT_License#Ambiguity_and_variants\>\`\_\_") and its associated text.

classref-item-separator

classref-method

`String<class_String>` **get_license_text**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_license_text>`

Returns the full Godot license text.

classref-item-separator

classref-method

`MainLoop<class_MainLoop>` **get_main_loop**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_main_loop>`

Returns the instance of the `MainLoop<class_MainLoop>`. This is usually the main `SceneTree<class_SceneTree>` and is the same as `Node.get_tree()<class_Node_method_get_tree>`.

**Note:** The type instantiated as the main loop can changed with `ProjectSettings.application/run/main_loop_type<class_ProjectSettings_property_application/run/main_loop_type>`.

classref-item-separator

classref-method

`int<class_int>` **get_physics_frames**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_physics_frames>`

Returns the total number of frames passed since the engine started. This number is increased every **physics frame**. See also `get_process_frames()<class_Engine_method_get_process_frames>`.

This method can be used to run expensive logic less often without relying on a `Timer<class_Timer>`:

gdscript

func physics_process(delta):
if Engine.get_physics_frames() % 2 == 0:
pass \# Run expensive logic only once every 2 physics frames here.

csharp

public override void PhysicsProcess(double delta) { base.\_PhysicsProcess(delta);

> if (Engine.GetPhysicsFrames() % 2 == 0) { // Run expensive logic only once every 2 physics frames here. }

}

classref-item-separator

classref-method

`float<class_float>` **get_physics_interpolation_fraction**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_physics_interpolation_fraction>`

Returns the fraction through the current physics tick we are at the time of rendering the frame. This can be used to implement fixed timestep interpolation.

classref-item-separator

classref-method

`int<class_int>` **get_process_frames**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_process_frames>`

Returns the total number of frames passed since the engine started. This number is increased every **process frame**, regardless of whether the render loop is enabled. See also `get_frames_drawn()<class_Engine_method_get_frames_drawn>` and `get_physics_frames()<class_Engine_method_get_physics_frames>`.

This method can be used to run expensive logic less often without relying on a `Timer<class_Timer>`:

gdscript

func process(delta):
if Engine.get_process_frames() % 5 == 0:
pass \# Run expensive logic only once every 5 process (render) frames here.

csharp

public override void Process(double delta) { base.\_Process(delta);

> if (Engine.GetProcessFrames() % 5 == 0) { // Run expensive logic only once every 5 process (render) frames here. }

}

classref-item-separator

classref-method

`ScriptLanguage<class_ScriptLanguage>` **get_script_language**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_script_language>`

Returns an instance of a `ScriptLanguage<class_ScriptLanguage>` with the given `index`.

classref-item-separator

classref-method

`int<class_int>` **get_script_language_count**() `🔗<class_Engine_method_get_script_language_count>`

Returns the number of available script languages. Use with `get_script_language()<class_Engine_method_get_script_language>`.

classref-item-separator

classref-method

`Object<class_Object>` **get_singleton**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_singleton>`

Returns the global singleton with the given `name`, or `null` if it does not exist. Often used for plugins. See also `has_singleton()<class_Engine_method_has_singleton>` and `get_singleton_list()<class_Engine_method_get_singleton_list>`.

**Note:** Global singletons are not the same as autoloaded nodes, which are configurable in the project settings.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_singleton_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_singleton_list>`

Returns a list of names of all available global singletons. See also `get_singleton()<class_Engine_method_get_singleton>`.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_version_info**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_version_info>`

Returns the current engine version information as a `Dictionary<class_Dictionary>` containing the following entries:

- `major` - Major version number as an int;
- `minor` - Minor version number as an int;
- `patch` - Patch version number as an int;
- `hex` - Full version encoded as a hexadecimal int with one byte (2 hex digits) per number (see example below);
- `status` - Status (such as "beta", "rc1", "rc2", "stable", etc.) as a String;
- `build` - Build name (e.g. "custom_build") as a String;
- `hash` - Full Git commit hash as a String;
- `timestamp` - Holds the Git commit date UNIX timestamp in seconds as an int, or `0` if unavailable;
- `string` - `major`, `minor`, `patch`, `status`, and `build` in a single String.

The `hex` value is encoded as follows, from left to right: one byte for the major, one byte for the minor, one byte for the patch version. For example, "3.1.12" would be `0x03010C`.

**Note:** The `hex` value is still an `int<class_int>` internally, and printing it will give you its decimal representation, which is not particularly meaningful. Use hexadecimal literals for quick version comparisons from code:

gdscript

if Engine.get_version_info().hex \>= 0x040100:
pass \# Do things specific to version 4.1 or later.

else:
pass \# Do things specific to versions before 4.1.

csharp

if ((int)Engine.GetVersionInfo()\["hex"\] \>= 0x040100) { // Do things specific to version 4.1 or later. } else { // Do things specific to versions before 4.1. }

classref-item-separator

classref-method

`String<class_String>` **get_write_movie_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_get_write_movie_path>`

Returns the path to the `MovieWriter<class_MovieWriter>`'s output file, or an empty string if the engine wasn't started in Movie Maker mode. The default path can be changed in `ProjectSettings.editor/movie_writer/movie_file<class_ProjectSettings_property_editor/movie_writer/movie_file>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_singleton**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_has_singleton>`

Returns `true` if a singleton with the given `name` exists in the global scope. See also `get_singleton()<class_Engine_method_get_singleton>`.

gdscript

print(Engine.has_singleton("OS")) \# Prints true print(Engine.has_singleton("Engine")) \# Prints true print(Engine.has_singleton("AudioServer")) \# Prints true print(Engine.has_singleton("Unknown")) \# Prints false

csharp

GD.Print(Engine.HasSingleton("OS")); // Prints True GD.Print(Engine.HasSingleton("Engine")); // Prints True GD.Print(Engine.HasSingleton("AudioServer")); // Prints True GD.Print(Engine.HasSingleton("Unknown")); // Prints False

**Note:** Global singletons are not the same as autoloaded nodes, which are configurable in the project settings.

classref-item-separator

classref-method

`bool<class_bool>` **is_editor_hint**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_is_editor_hint>`

Returns `true` if the script is currently running inside the editor, otherwise returns `false`. This is useful for `@tool` scripts to conditionally draw editor helpers, or prevent accidentally running "game" code that would affect the scene state while in the editor:

gdscript

if Engine.is_editor_hint():
draw_gizmos()

else:
simulate_physics()

csharp

if (Engine.IsEditorHint())
DrawGizmos();

else
SimulatePhysics();

See `Running code in the editor <../tutorials/plugins/running_code_in_the_editor>` in the documentation for more information.

**Note:** To detect whether the script is running on an editor *build* (such as when pressing `F5`), use `OS.has_feature()<class_OS_method_has_feature>` with the `"editor"` argument instead. `OS.has_feature("editor")` evaluate to `true` both when the script is running in the editor and when running the project from the editor, but returns `false` when run from an exported project.

classref-item-separator

classref-method

`bool<class_bool>` **is_embedded_in_editor**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_is_embedded_in_editor>`

Returns `true` if the engine is running embedded in the editor. This is useful to prevent attempting to update window mode or window flags that are not supported when running the project embedded in the editor.

classref-item-separator

classref-method

`bool<class_bool>` **is_in_physics_frame**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Engine_method_is_in_physics_frame>`

Returns `true` if the engine is inside the fixed physics process step of the main loop.

    func _enter_tree():
        # Depending on when the node is added to the tree,
        # prints either "true" or "false".
        print(Engine.is_in_physics_frame())

    func _process(delta):
        print(Engine.is_in_physics_frame()) # Prints false

    func _physics_process(delta):
        print(Engine.is_in_physics_frame()) # Prints true

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **register_script_language**(language: `ScriptLanguage<class_ScriptLanguage>`) `🔗<class_Engine_method_register_script_language>`

Registers a `ScriptLanguage<class_ScriptLanguage>` instance to be available with `ScriptServer`.

Returns:

- `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success;
- `@GlobalScope.ERR_UNAVAILABLE<class_@GlobalScope_constant_ERR_UNAVAILABLE>` if `ScriptServer` has reached the limit and cannot register any new language;
- `@GlobalScope.ERR_ALREADY_EXISTS<class_@GlobalScope_constant_ERR_ALREADY_EXISTS>` if `ScriptServer` already contains a language with similar extension/name/type.

classref-item-separator

classref-method

`void (No return value.)` **register_singleton**(name: `StringName<class_StringName>`, instance: `Object<class_Object>`) `🔗<class_Engine_method_register_singleton>`

Registers the given `Object<class_Object>` `instance` as a singleton, available globally under `name`. Useful for plugins.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **unregister_script_language**(language: `ScriptLanguage<class_ScriptLanguage>`) `🔗<class_Engine_method_unregister_script_language>`

Unregisters the `ScriptLanguage<class_ScriptLanguage>` instance from `ScriptServer`.

Returns:

- `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success;
- `@GlobalScope.ERR_DOES_NOT_EXIST<class_@GlobalScope_constant_ERR_DOES_NOT_EXIST>` if the language is not registered in `ScriptServer`.

classref-item-separator

classref-method

`void (No return value.)` **unregister_singleton**(name: `StringName<class_StringName>`) `🔗<class_Engine_method_unregister_singleton>`

Removes the singleton registered under `name`. The singleton object is *not* freed. Only works with user-defined singletons registered with `register_singleton()<class_Engine_method_register_singleton>`.