github_url
hide

# EditorFeatureProfile

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

An editor feature profile which can be used to disable specific features.

classref-introduction-group

## Description

An editor feature profile can be used to disable specific features of the Godot editor. When disabled, the features won't appear in the editor, which makes the editor less cluttered. This is useful in education settings to reduce confusion or when working in a team. For example, artists and level designers could use a feature profile that disables the script editor to avoid accidentally making changes to files they aren't supposed to edit.

To manage editor feature profiles visually, use **Editor \> Manage Feature Profiles...** at the top of the editor window.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Feature**: `🔗<enum_EditorFeatureProfile_Feature>`

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_3D** = `0`

The 3D editor. If this feature is disabled, the 3D editor won't display but 3D nodes will still display in the Create New Node dialog.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_SCRIPT** = `1`

The Script tab, which contains the script editor and class reference browser. If this feature is disabled, the Script tab won't display.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_ASSET_LIB** = `2`

The Asset Store tab. If this feature is disabled, the Asset Store tab won't display.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_SCENE_TREE** = `3`

Scene tree editing. If this feature is disabled, the Scene tree dock will still be visible but will be read-only.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_NODE_DOCK** = `4`

**Deprecated:** Replaced by the Signals and Groups docks.

The Node dock. If this feature is disabled, signals and groups won't be visible and modifiable from the editor.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_FILESYSTEM_DOCK** = `5`

The FileSystem dock. If this feature is disabled, the FileSystem dock won't be visible.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_IMPORT_DOCK** = `6`

The Import dock. If this feature is disabled, the Import dock won't be visible.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_HISTORY_DOCK** = `7`

The History dock. If this feature is disabled, the History dock won't be visible.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_GAME** = `8`

The Game tab, which allows embedding the game window and selecting nodes by clicking inside of it. If this feature is disabled, the Game tab won't display.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_SIGNALS_DOCK** = `9`

The Signals dock. If this feature is disabled, signals won't be visible and modifiable from the editor.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_GROUPS_DOCK** = `10`

The Groups dock. If this feature is disabled, groups won't be visible and modifiable from the editor.

classref-enumeration-constant

`Feature<enum_EditorFeatureProfile_Feature>` **FEATURE_MAX** = `11`

Represents the size of the `Feature<enum_EditorFeatureProfile_Feature>` enum.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_feature_name**(feature: `Feature<enum_EditorFeatureProfile_Feature>`) `🔗<class_EditorFeatureProfile_method_get_feature_name>`

Returns the specified `feature`'s human-readable name.

classref-item-separator

classref-method

`bool<class_bool>` **is_class_disabled**(class_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFeatureProfile_method_is_class_disabled>`

Returns `true` if the class specified by `class_name` is disabled. When disabled, the class won't appear in the Create New Node dialog.

classref-item-separator

classref-method

`bool<class_bool>` **is_class_editor_disabled**(class_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFeatureProfile_method_is_class_editor_disabled>`

Returns `true` if editing for the class specified by `class_name` is disabled. When disabled, the class will still appear in the Create New Node dialog but the Inspector will be read-only when selecting a node that extends the class.

classref-item-separator

classref-method

`bool<class_bool>` **is_class_property_disabled**(class_name: `StringName<class_StringName>`, property: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFeatureProfile_method_is_class_property_disabled>`

Returns `true` if `property` is disabled in the class specified by `class_name`. When a property is disabled, it won't appear in the Inspector when selecting a node that extends the class specified by `class_name`.

classref-item-separator

classref-method

`bool<class_bool>` **is_feature_disabled**(feature: `Feature<enum_EditorFeatureProfile_Feature>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFeatureProfile_method_is_feature_disabled>`

Returns `true` if the `feature` is disabled. When a feature is disabled, it will disappear from the editor entirely.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **load_from_file**(path: `String<class_String>`) `🔗<class_EditorFeatureProfile_method_load_from_file>`

Loads an editor feature profile from a file. The file must follow the JSON format obtained by using the feature profile manager's **Export** button or the `save_to_file()<class_EditorFeatureProfile_method_save_to_file>` method.

**Note:** Feature profiles created via the user interface are loaded from the `feature_profiles` directory, as a file with the `.profile` extension. The editor configuration folder can be found by using `EditorPaths.get_config_dir()<class_EditorPaths_method_get_config_dir>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **save_to_file**(path: `String<class_String>`) `🔗<class_EditorFeatureProfile_method_save_to_file>`

Saves the editor feature profile to a file in JSON format. It can then be imported using the feature profile manager's **Import** button or the `load_from_file()<class_EditorFeatureProfile_method_load_from_file>` method.

**Note:** Feature profiles created via the user interface are saved in the `feature_profiles` directory, as a file with the `.profile` extension. The editor configuration folder can be found by using `EditorPaths.get_config_dir()<class_EditorPaths_method_get_config_dir>`.

classref-item-separator

classref-method

`void (No return value.)` **set_disable_class**(class_name: `StringName<class_StringName>`, disable: `bool<class_bool>`) `🔗<class_EditorFeatureProfile_method_set_disable_class>`

If `disable` is `true`, disables the class specified by `class_name`. When disabled, the class won't appear in the Create New Node dialog.

classref-item-separator

classref-method

`void (No return value.)` **set_disable_class_editor**(class_name: `StringName<class_StringName>`, disable: `bool<class_bool>`) `🔗<class_EditorFeatureProfile_method_set_disable_class_editor>`

If `disable` is `true`, disables editing for the class specified by `class_name`. When disabled, the class will still appear in the Create New Node dialog but the Inspector will be read-only when selecting a node that extends the class.

classref-item-separator

classref-method

`void (No return value.)` **set_disable_class_property**(class_name: `StringName<class_StringName>`, property: `StringName<class_StringName>`, disable: `bool<class_bool>`) `🔗<class_EditorFeatureProfile_method_set_disable_class_property>`

If `disable` is `true`, disables editing for `property` in the class specified by `class_name`. When a property is disabled, it won't appear in the Inspector when selecting a node that extends the class specified by `class_name`.

classref-item-separator

classref-method

`void (No return value.)` **set_disable_feature**(feature: `Feature<enum_EditorFeatureProfile_Feature>`, disable: `bool<class_bool>`) `🔗<class_EditorFeatureProfile_method_set_disable_feature>`

If `disable` is `true`, disables the editor feature specified in `feature`. When a feature is disabled, it will disappear from the editor entirely.