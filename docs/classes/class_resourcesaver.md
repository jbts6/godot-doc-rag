github_url
hide

# ResourceSaver

**Inherits:** `Object<class_Object>`

A singleton for saving `Resource<class_Resource>`s to the filesystem.

classref-introduction-group

## Description

A singleton for saving resource types to the filesystem.

It uses the many `ResourceFormatSaver<class_ResourceFormatSaver>` classes registered in the engine (either built-in or from a plugin) to save resource data to text-based (e.g. `.tres` or `.tscn`) or binary files (e.g. `.res` or `.scn`).

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

flags **SaverFlags**: `🔗<enum_ResourceSaver_SaverFlags>`

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_NONE** = `0`

No resource saving option.

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_RELATIVE_PATHS** = `1`

Save the resource with a path relative to the scene which uses it.

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_BUNDLE_RESOURCES** = `2`

Bundles external resources.

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_CHANGE_PATH** = `4`

Changes the `Resource.resource_path<class_Resource_property_resource_path>` of the saved resource to match its new location.

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_OMIT_EDITOR_PROPERTIES** = `8`

Do not save editor-specific metadata (identified by their `__editor` prefix).

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_SAVE_BIG_ENDIAN** = `16`

Save as big endian (see `FileAccess.big_endian<class_FileAccess_property_big_endian>`).

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_COMPRESS** = `32`

Compress the resource on save using `FileAccess.COMPRESSION_ZSTD<class_FileAccess_constant_COMPRESSION_ZSTD>`. Only available for binary resource types.

classref-enumeration-constant

`SaverFlags<enum_ResourceSaver_SaverFlags>` **FLAG_REPLACE_SUBRESOURCE_PATHS** = `64`

Take over the paths of the saved subresources (see `Resource.take_over_path()<class_Resource_method_take_over_path>`).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_resource_format_saver**(format_saver: `ResourceFormatSaver<class_ResourceFormatSaver>`, at_front: `bool<class_bool>` = false) `🔗<class_ResourceSaver_method_add_resource_format_saver>`

Registers a new `ResourceFormatSaver<class_ResourceFormatSaver>`. The ResourceSaver will use the ResourceFormatSaver as described in `save()<class_ResourceSaver_method_save>`.

This method is performed implicitly for ResourceFormatSavers written in GDScript (see `ResourceFormatSaver<class_ResourceFormatSaver>` for more information).

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_recognized_extensions**(type: `Resource<class_Resource>`) `🔗<class_ResourceSaver_method_get_recognized_extensions>`

Returns the list of extensions available for saving a resource of a given type.

classref-item-separator

classref-method

`int<class_int>` **get_resource_id_for_path**(path: `String<class_String>`, generate: `bool<class_bool>` = false) `🔗<class_ResourceSaver_method_get_resource_id_for_path>`

Returns the resource ID for the given path. If `generate` is `true`, a new resource ID will be generated if one for the path is not found. If `generate` is `false` and the path is not found, `ResourceUID.INVALID_ID<class_ResourceUID_constant_INVALID_ID>` is returned.

classref-item-separator

classref-method

`void (No return value.)` **remove_resource_format_saver**(format_saver: `ResourceFormatSaver<class_ResourceFormatSaver>`) `🔗<class_ResourceSaver_method_remove_resource_format_saver>`

Unregisters the given `ResourceFormatSaver<class_ResourceFormatSaver>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **save**(resource: `Resource<class_Resource>`, path: `String<class_String>` = "", flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`SaverFlags<enum_ResourceSaver_SaverFlags>`\] = 0) `🔗<class_ResourceSaver_method_save>`

Saves a resource to disk to the given path, using a `ResourceFormatSaver<class_ResourceFormatSaver>` that recognizes the resource object. If `path` is empty, **ResourceSaver** will try to use `Resource.resource_path<class_Resource_property_resource_path>`.

The `flags` bitmask can be specified to customize the save behavior.

Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success.

**Note:** When the project is running, any generated UID associated with the resource will not be saved as the required code is only executed in editor mode.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **set_uid**(resource: `String<class_String>`, uid: `int<class_int>`) `🔗<class_ResourceSaver_method_set_uid>`

Sets the UID of the given `resource` path to `uid`. You can generate a new UID using `ResourceUID.create_id()<class_ResourceUID_method_create_id>`.

Since resources will normally get a UID automatically, this method is only useful in very specific cases.