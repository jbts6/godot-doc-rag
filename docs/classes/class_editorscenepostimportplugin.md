github_url
hide

# EditorScenePostImportPlugin

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Plugin to control and modifying the process of importing a scene.

classref-introduction-group

## Description

This plugin type exists to modify the process of importing scenes, allowing to change the content as well as add importer options at every stage of the process.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **InternalImportCategory**: `🔗<enum_EditorScenePostImportPlugin_InternalImportCategory>`

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_NODE** = `0`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_MESH_3D_NODE** = `1`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_MESH** = `2`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_MATERIAL** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_ANIMATION** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_ANIMATION_NODE** = `5`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_SKELETON_3D_NODE** = `6`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`InternalImportCategory<enum_EditorScenePostImportPlugin_InternalImportCategory>` **INTERNAL_IMPORT_CATEGORY_MAX** = `7`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_get_import_options**(path: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorScenePostImportPlugin_private_method__get_import_options>`

Override to add general import options. These will appear in the main import dock on the editor. Add options via `add_import_option()<class_EditorScenePostImportPlugin_method_add_import_option>` and `add_import_option_advanced()<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`.

classref-item-separator

classref-method

`void (No return value.)` **\_get_internal_import_options**(category: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`

Override to add internal import options. These will appear in the 3D scene import dialog. Add options via `add_import_option()<class_EditorScenePostImportPlugin_method_add_import_option>` and `add_import_option_advanced()<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_get_internal_option_update_view_required**(category: `int<class_int>`, option: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorScenePostImportPlugin_private_method__get_internal_option_update_view_required>`

Should return `true` if the 3D view of the import dialog needs to update when changing the given option.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_get_internal_option_visibility**(category: `int<class_int>`, for_animation: `bool<class_bool>`, option: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorScenePostImportPlugin_private_method__get_internal_option_visibility>`

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

classref-item-separator

classref-method

`Variant<class_Variant>` **\_get_option_visibility**(path: `String<class_String>`, for_animation: `bool<class_bool>`, option: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorScenePostImportPlugin_private_method__get_option_visibility>`

Should return `true` to show the given option, `false` to hide the given option, or `null` to ignore.

classref-item-separator

classref-method

`void (No return value.)` **\_internal_process**(category: `int<class_int>`, base_node: `Node<class_Node>`, node: `Node<class_Node>`, resource: `Resource<class_Resource>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorScenePostImportPlugin_private_method__internal_process>`

Process a specific node or resource for a given category.

classref-item-separator

classref-method

`void (No return value.)` **\_post_process**(scene: `Node<class_Node>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorScenePostImportPlugin_private_method__post_process>`

Post-process the scene. This function is called after the final scene has been configured.

classref-item-separator

classref-method

`void (No return value.)` **\_pre_process**(scene: `Node<class_Node>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorScenePostImportPlugin_private_method__pre_process>`

Pre-process the scene. This function is called right after the scene format loader loaded the scene and no changes have been made.

Pre-process may be used to adjust internal import options in the `"nodes"`, `"meshes"`, `"animations"` or `"materials"` keys inside `get_option_value("_subresources")`.

classref-item-separator

classref-method

`void (No return value.)` **add_import_option**(name: `String<class_String>`, value: `Variant<class_Variant>`) `🔗<class_EditorScenePostImportPlugin_method_add_import_option>`

Add a specific import option (name and default value only). This function can only be called from `_get_import_options()<class_EditorScenePostImportPlugin_private_method__get_import_options>` and `_get_internal_import_options()<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`.

classref-item-separator

classref-method

`void (No return value.)` **add_import_option_advanced**(type: `Variant.Type<enum_@GlobalScope_Variant.Type>`, name: `String<class_String>`, default_value: `Variant<class_Variant>`, hint: `PropertyHint<enum_@GlobalScope_PropertyHint>` = 0, hint_string: `String<class_String>` = "", usage_flags: `int<class_int>` = 6) `🔗<class_EditorScenePostImportPlugin_method_add_import_option_advanced>`

Add a specific import option. This function can only be called from `_get_import_options()<class_EditorScenePostImportPlugin_private_method__get_import_options>` and `_get_internal_import_options()<class_EditorScenePostImportPlugin_private_method__get_internal_import_options>`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_option_value**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorScenePostImportPlugin_method_get_option_value>`

Query the value of an option. This function can only be called from those querying visibility, or processing.