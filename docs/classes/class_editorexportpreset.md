github_url
hide

# EditorExportPreset

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Export preset configuration.

classref-introduction-group

## Description

Represents the configuration of an export preset, as created by the editor's export dialog. An **EditorExportPreset** instance is intended to be used a read-only configuration passed to the `EditorExportPlatform<class_EditorExportPlatform>` methods when exporting the project.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ExportFilter**: `🔗<enum_EditorExportPreset_ExportFilter>`

classref-enumeration-constant

`ExportFilter<enum_EditorExportPreset_ExportFilter>` **EXPORT_ALL_RESOURCES** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ExportFilter<enum_EditorExportPreset_ExportFilter>` **EXPORT_SELECTED_SCENES** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ExportFilter<enum_EditorExportPreset_ExportFilter>` **EXPORT_SELECTED_RESOURCES** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ExportFilter<enum_EditorExportPreset_ExportFilter>` **EXCLUDE_SELECTED_RESOURCES** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ExportFilter<enum_EditorExportPreset_ExportFilter>` **EXPORT_CUSTOMIZED** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-enumeration

enum **FileExportMode**: `🔗<enum_EditorExportPreset_FileExportMode>`

classref-enumeration-constant

`FileExportMode<enum_EditorExportPreset_FileExportMode>` **MODE_FILE_NOT_CUSTOMIZED** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`FileExportMode<enum_EditorExportPreset_FileExportMode>` **MODE_FILE_STRIP** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`FileExportMode<enum_EditorExportPreset_FileExportMode>` **MODE_FILE_KEEP** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`FileExportMode<enum_EditorExportPreset_FileExportMode>` **MODE_FILE_REMOVE** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-enumeration

enum **ScriptExportMode**: `🔗<enum_EditorExportPreset_ScriptExportMode>`

classref-enumeration-constant

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>` **MODE_SCRIPT_TEXT** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>` **MODE_SCRIPT_BINARY_TOKENS** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>` **MODE_SCRIPT_BINARY_TOKENS_COMPRESSED** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **are_advanced_options_enabled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_are_advanced_options_enabled>`

Returns `true` if the "Advanced" toggle is enabled in the export dialog.

classref-item-separator

classref-method

`String<class_String>` **get_custom_features**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_custom_features>`

Returns a comma-separated list of custom features added to this preset, as a string. See `Feature tags <../tutorials/export/feature_tags>` in the documentation for more information.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_customized_files**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_customized_files>`

Returns a dictionary of files selected in the "Resources" tab of the export dialog. The dictionary's keys are file paths, and its values are the corresponding export modes: `"strip"`, `"keep"`, or `"remove"`. See also `get_file_export_mode()<class_EditorExportPreset_method_get_file_export_mode>`.

classref-item-separator

classref-method

`int<class_int>` **get_customized_files_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_customized_files_count>`

Returns the number of files selected in the "Resources" tab of the export dialog.

classref-item-separator

classref-method

`bool<class_bool>` **get_encrypt_directory**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_encrypt_directory>`

Returns `true` if PCK directory encryption is enabled in the export dialog.

classref-item-separator

classref-method

`bool<class_bool>` **get_encrypt_pck**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_encrypt_pck>`

Returns `true` if PCK encryption is enabled in the export dialog.

classref-item-separator

classref-method

`String<class_String>` **get_encryption_ex_filter**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_encryption_ex_filter>`

Returns file filters to exclude during PCK encryption.

classref-item-separator

classref-method

`String<class_String>` **get_encryption_in_filter**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_encryption_in_filter>`

Returns file filters to include during PCK encryption.

classref-item-separator

classref-method

`String<class_String>` **get_encryption_key**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_encryption_key>`

Returns PCK encryption key.

classref-item-separator

classref-method

`String<class_String>` **get_exclude_filter**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_exclude_filter>`

Returns file filters to exclude during export.

classref-item-separator

classref-method

`ExportFilter<enum_EditorExportPreset_ExportFilter>` **get_export_filter**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_export_filter>`

Returns export file filter mode selected in the "Resources" tab of the export dialog.

classref-item-separator

classref-method

`String<class_String>` **get_export_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_export_path>`

Returns export target path.

classref-item-separator

classref-method

`FileExportMode<enum_EditorExportPreset_FileExportMode>` **get_file_export_mode**(path: `String<class_String>`, default: `FileExportMode<enum_EditorExportPreset_FileExportMode>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_file_export_mode>`

Returns file export mode for the specified file.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_files_to_export**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_files_to_export>`

Returns array of files to export.

classref-item-separator

classref-method

`String<class_String>` **get_include_filter**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_include_filter>`

Returns file filters to include during export.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_or_env**(name: `StringName<class_StringName>`, env_var: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_or_env>`

Returns export option value or value of environment variable if it is set.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_patches**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_patches>`

Returns the list of packs on which to base a patch export on.

classref-item-separator

classref-method

`String<class_String>` **get_preset_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_preset_name>`

Returns this export preset's name.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_project_setting**(name: `StringName<class_StringName>`) `🔗<class_EditorExportPreset_method_get_project_setting>`

Returns the value of the setting identified by `name` using export preset feature tag overrides instead of current OS features.

classref-item-separator

classref-method

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>` **get_script_export_mode**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_script_export_mode>`

Returns the export mode used by GDScript files. `0` for "Text", `1` for "Binary tokens", and `2` for "Compressed binary tokens (smaller files)".

classref-item-separator

classref-method

`String<class_String>` **get_version**(name: `StringName<class_StringName>`, windows_version: `bool<class_bool>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_get_version>`

Returns the preset's version number, or fall back to the `ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>` project setting if set to an empty string.

If `windows_version` is `true`, formats the returned version number to be compatible with Windows executable metadata.

classref-item-separator

classref-method

`bool<class_bool>` **has**(property: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_has>`

Returns `true` if the preset has the property named `property`.

classref-item-separator

classref-method

`bool<class_bool>` **has_export_file**(path: `String<class_String>`) `🔗<class_EditorExportPreset_method_has_export_file>`

Returns `true` if the file at the specified `path` will be exported.

classref-item-separator

classref-method

`bool<class_bool>` **is_dedicated_server**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_is_dedicated_server>`

Returns `true` if the dedicated server export mode is selected in the export dialog.

classref-item-separator

classref-method

`bool<class_bool>` **is_runnable**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPreset_method_is_runnable>`

Returns `true` if the "Runnable" toggle is enabled in the export dialog.