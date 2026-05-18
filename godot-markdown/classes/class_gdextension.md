github_url
hide

# GDExtension

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A native library for GDExtension.

classref-introduction-group

## Description

The **GDExtension** resource type represents a [shared library](https://en.wikipedia.org/wiki/Shared_library) which can expand the functionality of the engine. The `GDExtensionManager<class_GDExtensionManager>` singleton is responsible for loading, reloading, and unloading **GDExtension** resources.

**Note:** GDExtension itself is not a scripting language and has no relation to `GDScript<class_GDScript>` resources.

classref-introduction-group

## Tutorials

- `GDExtension overview <../engine_details/engine_api/gdextension/what_is_gdextension>`
- `GDExtension example in C++ <../tutorials/scripting/cpp/gdextension_cpp_example>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **InitializationLevel**: `🔗<enum_GDExtension_InitializationLevel>`

classref-enumeration-constant

`InitializationLevel<enum_GDExtension_InitializationLevel>` **INITIALIZATION_LEVEL_CORE** = `0`

The library is initialized at the same time as the core features of the engine.

classref-enumeration-constant

`InitializationLevel<enum_GDExtension_InitializationLevel>` **INITIALIZATION_LEVEL_SERVERS** = `1`

The library is initialized at the same time as the engine's servers (such as `RenderingServer<class_RenderingServer>` or `PhysicsServer3D<class_PhysicsServer3D>`).

classref-enumeration-constant

`InitializationLevel<enum_GDExtension_InitializationLevel>` **INITIALIZATION_LEVEL_SCENE** = `2`

The library is initialized at the same time as the engine's scene-related classes.

classref-enumeration-constant

`InitializationLevel<enum_GDExtension_InitializationLevel>` **INITIALIZATION_LEVEL_EDITOR** = `3`

The library is initialized at the same time as the engine's editor classes. Only happens when loading the GDExtension in the editor.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`InitializationLevel<enum_GDExtension_InitializationLevel>` **get_minimum_library_initialization_level**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDExtension_method_get_minimum_library_initialization_level>`

Returns the lowest level required for this extension to be properly initialized (see the `InitializationLevel<enum_GDExtension_InitializationLevel>` enum).

classref-item-separator

classref-method

`bool<class_bool>` **is_library_open**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDExtension_method_is_library_open>`

Returns `true` if this extension's library has been opened.