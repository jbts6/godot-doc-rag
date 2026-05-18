github_url
hide

# EditorExportPlatformExtension

**Inherits:** `EditorExportPlatform<class_EditorExportPlatform>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Base class for custom `EditorExportPlatform<class_EditorExportPlatform>` implementations (plugins).

classref-introduction-group

## Description

External `EditorExportPlatform<class_EditorExportPlatform>` implementations should inherit from this class.

To use `EditorExportPlatform<class_EditorExportPlatform>`, register it using the `EditorPlugin.add_export_platform()<class_EditorPlugin_method_add_export_platform>` method first.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **\_can_export**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__can_export>`

Returns `true` if the specified `preset` is valid and can be exported. Use `set_config_error()<class_EditorExportPlatformExtension_method_set_config_error>` and `set_config_missing_templates()<class_EditorExportPlatformExtension_method_set_config_missing_templates>` to set error details.

Usual implementations call `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>` and `_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>` to determine if exporting is possible.

classref-item-separator

classref-method

`void (No return value.)` **\_cleanup**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__cleanup>`

Called by the editor before platform is unregistered.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_export_pack**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`, path: `String<class_String>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__export_pack>`

Creates a PCK archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and PCK is selected as a file type.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_export_pack_patch**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`, path: `String<class_String>`, patches: `PackedStringArray<class_PackedStringArray>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__export_pack_patch>`

Creates a patch PCK archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and PCK is selected as a file type.

**Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_export_project**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`, path: `String<class_String>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_EditorExportPlatformExtension_private_method__export_project>`

Creates a full project at `path` for the specified `preset`.

This method is called when "Export" button is pressed in the export dialog.

This method implementation can call `EditorExportPlatform.save_pack()<class_EditorExportPlatform_method_save_pack>` or `EditorExportPlatform.save_zip()<class_EditorExportPlatform_method_save_zip>` to use default PCK/ZIP export process, or calls `EditorExportPlatform.export_project_files()<class_EditorExportPlatform_method_export_project_files>` and implement custom callback for processing each exported file.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_export_zip**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`, path: `String<class_String>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__export_zip>`

Create a ZIP archive at `path` for the specified `preset`.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" disabled, and ZIP is selected as a file type.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_export_zip_patch**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`, path: `String<class_String>`, patches: `PackedStringArray<class_PackedStringArray>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__export_zip_patch>`

Create a ZIP archive at `path` for the specified `preset`, containing only the files that have changed since the last patch.

This method is called when "Export PCK/ZIP" button is pressed in the export dialog, with "Export as Patch" enabled, and ZIP is selected as a file type.

**Note:** The patches provided in `patches` have already been loaded when this method is called and are merely provided as context. When empty the patches defined in the export preset have been loaded instead.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_binary_extensions**(preset: `EditorExportPreset<class_EditorExportPreset>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_binary_extensions>`

Returns array of supported binary extensions for the full project export.

classref-item-separator

classref-method

`String<class_String>` **\_get_debug_protocol**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_debug_protocol>`

Returns protocol used for remote debugging. Default implementation return `tcp://`.

classref-item-separator

classref-method

`String<class_String>` **\_get_device_architecture**(device: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_device_architecture>`

Returns device architecture for one-click deploy.

classref-item-separator

classref-method

`bool<class_bool>` **\_get_export_option_visibility**(preset: `EditorExportPreset<class_EditorExportPreset>`, option: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_export_option_visibility>`

Validates `option` and returns visibility for the specified `preset`. Default implementation return `true` for all options.

classref-item-separator

classref-method

`String<class_String>` **\_get_export_option_warning**(preset: `EditorExportPreset<class_EditorExportPreset>`, option: `StringName<class_StringName>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_export_option_warning>`

Validates `option` and returns warning message for the specified `preset`. Default implementation return empty string for all options.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_get_export_options**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_export_options>`

Returns a property list, as an `Array<class_Array>` of dictionaries. Each `Dictionary<class_Dictionary>` must at least contain the `name: StringName` and `type: Variant.Type` entries.

Additionally, the following keys are supported:

- `hint: PropertyHint`
- `hint_string: String`
- `usage: PropertyUsageFlags`
- `class_name: StringName`
- `default_value: Variant`, default value of the property.
- `update_visibility: bool`, if set to `true`, `_get_export_option_visibility()<class_EditorExportPlatformExtension_private_method__get_export_option_visibility>` is called for each property when this property is changed.
- `required: bool`, if set to `true`, this property warnings are critical, and should be resolved to make export possible. This value is a hint for the `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>` implementation, and not used by the engine directly.

See also `Object._get_property_list()<class_Object_private_method__get_property_list>`.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **\_get_logo**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_logo>`

Returns the platform logo displayed in the export dialog. The logo should be 32×32 pixels, adjusted for the current editor scale (see `EditorInterface.get_editor_scale()<class_EditorInterface_method_get_editor_scale>`).

classref-item-separator

classref-method

`String<class_String>` **\_get_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_name>`

Returns export platform name.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **\_get_option_icon**(device: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_option_icon>`

Returns the item icon for the specified `device` in the one-click deploy menu. The icon should be 16×16 pixels, adjusted for the current editor scale (see `EditorInterface.get_editor_scale()<class_EditorInterface_method_get_editor_scale>`).

classref-item-separator

classref-method

`String<class_String>` **\_get_option_label**(device: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_option_label>`

Returns one-click deploy menu item label for the specified `device`.

classref-item-separator

classref-method

`String<class_String>` **\_get_option_tooltip**(device: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_option_tooltip>`

Returns one-click deploy menu item tooltip for the specified `device`.

classref-item-separator

classref-method

`int<class_int>` **\_get_options_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_options_count>`

Returns the number of devices (or other options) available in the one-click deploy menu.

classref-item-separator

classref-method

`String<class_String>` **\_get_options_tooltip**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_options_tooltip>`

Returns tooltip of the one-click deploy menu button.

classref-item-separator

classref-method

`String<class_String>` **\_get_os_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_os_name>`

Returns target OS name.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_platform_features**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_platform_features>`

Returns array of platform specific features.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_preset_features**(preset: `EditorExportPreset<class_EditorExportPreset>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_preset_features>`

Returns array of platform specific features for the specified `preset`.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **\_get_run_icon**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__get_run_icon>`

Returns the icon of the one-click deploy menu button. The icon should be 16×16 pixels, adjusted for the current editor scale (see `EditorInterface.get_editor_scale()<class_EditorInterface_method_get_editor_scale>`).

classref-item-separator

classref-method

`bool<class_bool>` **\_has_valid_export_configuration**(preset: `EditorExportPreset<class_EditorExportPreset>`, debug: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`

Returns `true` if export configuration is valid.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_valid_project_configuration**(preset: `EditorExportPreset<class_EditorExportPreset>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>`

Returns `true` if project configuration is valid.

classref-item-separator

classref-method

`void (No return value.)` **\_initialize**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__initialize>`

Initializes the plugin. Called by the editor when platform is registered.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_executable**(path: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_private_method__is_executable>`

Returns `true` if specified file is a valid executable (native executable or script) for the target platform.

classref-item-separator

classref-method

`bool<class_bool>` **\_poll_export**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__poll_export>`

Returns `true` if one-click deploy options are changed and editor interface should be updated.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_run**(preset: `EditorExportPreset<class_EditorExportPreset>`, device: `int<class_int>`, debug_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__run>`

This method is called when `device` one-click deploy menu option is selected.

Implementation should export project to a temporary location, upload and run it on the specific `device`, or perform another action associated with the menu item.

classref-item-separator

classref-method

`bool<class_bool>` **\_should_update_export_options**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorExportPlatformExtension_private_method__should_update_export_options>`

Returns `true` if export options list is changed and presets should be updated.

classref-item-separator

classref-method

`String<class_String>` **get_config_error**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_method_get_config_error>`

Returns current configuration error message text. This method should be called only from the `_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`, `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`, or `_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>` implementations.

classref-item-separator

classref-method

`bool<class_bool>` **get_config_missing_templates**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_method_get_config_missing_templates>`

Returns `true` is export templates are missing from the current configuration. This method should be called only from the `_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`, `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`, or `_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>` implementations.

classref-item-separator

classref-method

`void (No return value.)` **set_config_error**(error_text: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_method_set_config_error>`

Sets current configuration error message text. This method should be called only from the `_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`, `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`, or `_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>` implementations.

classref-item-separator

classref-method

`void (No return value.)` **set_config_missing_templates**(missing_templates: `bool<class_bool>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorExportPlatformExtension_method_set_config_missing_templates>`

Set to `true` is export templates are missing from the current configuration. This method should be called only from the `_can_export()<class_EditorExportPlatformExtension_private_method__can_export>`, `_has_valid_export_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_export_configuration>`, or `_has_valid_project_configuration()<class_EditorExportPlatformExtension_private_method__has_valid_project_configuration>` implementations.