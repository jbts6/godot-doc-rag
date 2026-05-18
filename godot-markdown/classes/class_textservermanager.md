github_url
hide

# TextServerManager

**Inherits:** `Object<class_Object>`

A singleton for managing `TextServer<class_TextServer>` implementations.

classref-introduction-group

## Description

**TextServerManager** is the API backend for loading, enumerating, and switching `TextServer<class_TextServer>`s.

**Note:** Switching text server at runtime is possible, but will invalidate all fonts and text buffers. Make sure to unload all controls, fonts, and themes before doing so.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**interface_added**(interface_name: `StringName<class_StringName>`) `🔗<class_TextServerManager_signal_interface_added>`

Emitted when a new interface has been added.

classref-item-separator

classref-signal

**interface_removed**(interface_name: `StringName<class_StringName>`) `🔗<class_TextServerManager_signal_interface_removed>`

Emitted when an interface is removed.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_interface**(interface: `TextServer<class_TextServer>`) `🔗<class_TextServerManager_method_add_interface>`

Registers a `TextServer<class_TextServer>` interface.

classref-item-separator

classref-method

`TextServer<class_TextServer>` **find_interface**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerManager_method_find_interface>`

Finds an interface by its `name`.

classref-item-separator

classref-method

`TextServer<class_TextServer>` **get_interface**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerManager_method_get_interface>`

Returns the interface registered at a given index.

classref-item-separator

classref-method

`int<class_int>` **get_interface_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerManager_method_get_interface_count>`

Returns the number of interfaces currently registered.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_interfaces**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerManager_method_get_interfaces>`

Returns a list of available interfaces, with the index and name of each interface.

classref-item-separator

classref-method

`TextServer<class_TextServer>` **get_primary_interface**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextServerManager_method_get_primary_interface>`

Returns the primary `TextServer<class_TextServer>` interface currently in use.

classref-item-separator

classref-method

`void (No return value.)` **remove_interface**(interface: `TextServer<class_TextServer>`) `🔗<class_TextServerManager_method_remove_interface>`

Removes an interface. All fonts and shaped text caches should be freed before removing an interface.

classref-item-separator

classref-method

`void (No return value.)` **set_primary_interface**(index: `TextServer<class_TextServer>`) `🔗<class_TextServerManager_method_set_primary_interface>`

Sets the primary `TextServer<class_TextServer>` interface.