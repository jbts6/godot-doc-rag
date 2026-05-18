github_url
hide

# GDExtensionManager

**Inherits:** `Object<class_Object>`

Provides access to GDExtension functionality.

classref-introduction-group

## Description

The GDExtensionManager loads, initializes, and keeps track of all available `GDExtension<class_GDExtension>` libraries in the project.

**Note:** Do not worry about GDExtension unless you know what you are doing.

classref-introduction-group

## Tutorials

- `GDExtension overview <../engine_details/engine_api/gdextension/what_is_gdextension>`
- `GDExtension example in C++ <../tutorials/scripting/cpp/gdextension_cpp_example>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**extension_loaded**(extension: `GDExtension<class_GDExtension>`) `🔗<class_GDExtensionManager_signal_extension_loaded>`

Emitted after the editor has finished loading a new extension.

**Note:** This signal is only emitted in editor builds.

classref-item-separator

classref-signal

**extension_unloading**(extension: `GDExtension<class_GDExtension>`) `🔗<class_GDExtensionManager_signal_extension_unloading>`

Emitted before the editor starts unloading an extension.

**Note:** This signal is only emitted in editor builds.

classref-item-separator

classref-signal

**extensions_reloaded**() `🔗<class_GDExtensionManager_signal_extensions_reloaded>`

Emitted after the editor has finished reloading one or more extensions.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **LoadStatus**: `🔗<enum_GDExtensionManager_LoadStatus>`

classref-enumeration-constant

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **LOAD_STATUS_OK** = `0`

The extension has loaded successfully.

classref-enumeration-constant

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **LOAD_STATUS_FAILED** = `1`

The extension has failed to load, possibly because it does not exist or has missing dependencies.

classref-enumeration-constant

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **LOAD_STATUS_ALREADY_LOADED** = `2`

The extension has already been loaded.

classref-enumeration-constant

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **LOAD_STATUS_NOT_LOADED** = `3`

The extension has not been loaded.

classref-enumeration-constant

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **LOAD_STATUS_NEEDS_RESTART** = `4`

The extension requires the application to restart to fully load.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`GDExtension<class_GDExtension>` **get_extension**(path: `String<class_String>`) `🔗<class_GDExtensionManager_method_get_extension>`

Returns the `GDExtension<class_GDExtension>` at the given file `path`, or `null` if it has not been loaded or does not exist.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_loaded_extensions**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDExtensionManager_method_get_loaded_extensions>`

Returns the file paths of all currently loaded extensions.

classref-item-separator

classref-method

`bool<class_bool>` **is_extension_loaded**(path: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDExtensionManager_method_is_extension_loaded>`

Returns `true` if the extension at the given file `path` has already been loaded successfully. See also `get_loaded_extensions()<class_GDExtensionManager_method_get_loaded_extensions>`.

classref-item-separator

classref-method

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **load_extension**(path: `String<class_String>`) `🔗<class_GDExtensionManager_method_load_extension>`

Loads an extension by absolute file path. The `path` needs to point to a valid `GDExtension<class_GDExtension>`. Returns `LOAD_STATUS_OK<class_GDExtensionManager_constant_LOAD_STATUS_OK>` if successful.

classref-item-separator

classref-method

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **load_extension_from_function**(path: `String<class_String>`, init_func: `const GDExtensionInitializationFunction*`) `🔗<class_GDExtensionManager_method_load_extension_from_function>`

Loads the extension already in address space via the given path and initialization function. The `path` needs to be unique and start with `"libgodot://"`. Returns `LOAD_STATUS_OK<class_GDExtensionManager_constant_LOAD_STATUS_OK>` if successful.

classref-item-separator

classref-method

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **reload_extension**(path: `String<class_String>`) `🔗<class_GDExtensionManager_method_reload_extension>`

Reloads the extension at the given file path. The `path` needs to point to a valid `GDExtension<class_GDExtension>`, otherwise this method may return either `LOAD_STATUS_NOT_LOADED<class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED>` or `LOAD_STATUS_FAILED<class_GDExtensionManager_constant_LOAD_STATUS_FAILED>`.

**Note:** You can only reload extensions in the editor. In release builds, this method always fails and returns `LOAD_STATUS_FAILED<class_GDExtensionManager_constant_LOAD_STATUS_FAILED>`.

classref-item-separator

classref-method

`LoadStatus<enum_GDExtensionManager_LoadStatus>` **unload_extension**(path: `String<class_String>`) `🔗<class_GDExtensionManager_method_unload_extension>`

Unloads an extension by file path. The `path` needs to point to an already loaded `GDExtension<class_GDExtension>`, otherwise this method returns `LOAD_STATUS_NOT_LOADED<class_GDExtensionManager_constant_LOAD_STATUS_NOT_LOADED>`.