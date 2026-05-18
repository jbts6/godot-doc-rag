github_url
hide

# ResourceFormatSaver

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Saves a specific resource type to a file.

classref-introduction-group

## Description

The engine can save resources when you do it from the editor, or when you use the `ResourceSaver<class_ResourceSaver>` singleton. This is accomplished thanks to multiple **ResourceFormatSaver**s, each handling its own format and called automatically by the engine.

By default, Godot saves resources as `.tres` (text-based), `.res` (binary) or another built-in format, but you can choose to create your own format by extending this class. Be sure to respect the documented return types and values. You should give it a global class name with `class_name` for it to be registered. Like built-in ResourceFormatSavers, it will be called automatically when saving resources of its recognized type(s). You may also implement a `ResourceFormatLoader<class_ResourceFormatLoader>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_recognized_extensions**(resource: `Resource<class_Resource>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ResourceFormatSaver_private_method__get_recognized_extensions>`

Returns the list of extensions available for saving the resource object, provided it is recognized (see `_recognize()<class_ResourceFormatSaver_private_method__recognize>`).

classref-item-separator

classref-method

`bool<class_bool>` **\_recognize**(resource: `Resource<class_Resource>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ResourceFormatSaver_private_method__recognize>`

Returns whether the given resource object can be saved by this saver.

classref-item-separator

classref-method

`bool<class_bool>` **\_recognize_path**(resource: `Resource<class_Resource>`, path: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ResourceFormatSaver_private_method__recognize_path>`

Returns `true` if this saver handles a given save path and `false` otherwise.

If this method is not implemented, the default behavior returns whether the path's extension is within the ones provided by `_get_recognized_extensions()<class_ResourceFormatSaver_private_method__get_recognized_extensions>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_save**(resource: `Resource<class_Resource>`, path: `String<class_String>`, flags: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_ResourceFormatSaver_private_method__save>`

Saves the given resource object to a file at the target `path`. `flags` is a bitmask composed with `SaverFlags<enum_ResourceSaver_SaverFlags>` constants.

Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success, or an `Error<enum_@GlobalScope_Error>` constant in case of failure.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_set_uid**(path: `String<class_String>`, uid: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_ResourceFormatSaver_private_method__set_uid>`

Sets a new UID for the resource at the given `path`. Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success, or an `Error<enum_@GlobalScope_Error>` constant in case of failure.