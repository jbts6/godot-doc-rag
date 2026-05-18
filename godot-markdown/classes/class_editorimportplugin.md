github_url
hide

# EditorImportPlugin

**Inherits:** `ResourceImporter<class_ResourceImporter>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Registers a custom resource importer in the editor. Use the class to parse any file and import it as a new resource type.

classref-introduction-group

## Description

**EditorImportPlugin**s provide a way to extend the editor's resource import functionality. Use them to import resources from custom files or to provide alternatives to the editor's existing importers.

EditorImportPlugins work by associating with specific file extensions and a resource type. See `_get_recognized_extensions()<class_EditorImportPlugin_private_method__get_recognized_extensions>` and `_get_resource_type()<class_EditorImportPlugin_private_method__get_resource_type>`. They may optionally specify some import presets that affect the import process. EditorImportPlugins are responsible for creating the resources and saving them in the `.godot/imported` directory (see `ProjectSettings.application/config/use_hidden_project_data_directory<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`).

Below is an example EditorImportPlugin that imports a `Mesh<class_Mesh>` from a file with the extension ".special" or ".spec":

gdscript

@tool extends EditorImportPlugin

func get_importer_name():
return "my.special.plugin"

func get_visible_name():
return "Special Mesh"

func get_recognized_extensions():
return \["special", "spec"\]

func get_save_extension():
return "mesh"

func get_resource_type():
return "Mesh"

func get_preset_count():
return 1

func get_preset_name(preset_index):
return "Default"

func get_import_options(path, preset_index):
return \[{"name": "my_option", "default_value": false}\]

func import(source_file, save_path, options, platform_variants, gen_files):
var file = FileAccess.open(source_file, FileAccess.READ) if file == null: return FAILED var mesh = ArrayMesh.new() \# Fill the Mesh with data read in "file", left as an exercise to the reader.

var filename = save_path + "." + get_save_extension() return ResourceSaver.save(mesh, filename)

csharp

using Godot;

public partial class MySpecialPlugin : EditorImportPlugin { public override string GetImporterName() { return "my.special.plugin"; }

> public override string GetVisibleName() { return "Special Mesh"; }
>
> public override string\[\] GetRecognizedExtensions() { return \["special", "spec"\]; }
>
> public override string GetSaveExtension() { return "mesh"; }
>
> public override string GetResourceType() { return "Mesh"; }
>
> public override int GetPresetCount() { return 1; }
>
> public override string GetPresetName(int presetIndex) { return "Default"; }
>
> public override Godot.Collections.Array\<Godot.Collections.Dictionary\> GetImportOptions(string path, int presetIndex) { return \[ new Godot.Collections.Dictionary { { "name", "myOption" }, { "default_value", false }, }, \]; }
>
> public override Error Import(string sourceFile, string savePath, Godot.Collections.Dictionary options, Godot.Collections.Array\<string\> platformVariants, Godot.Collections.Array\<string\> genFiles) { using var file = FileAccess.Open(sourceFile, FileAccess.ModeFlags.Read); if (file.GetError() != Error.Ok) { return Error.Failed; }
>
> > var mesh = new ArrayMesh(); // Fill the Mesh with data read in "file", left as an exercise to the reader. string filename = \$"{savePath}.{GetSaveExtension()}"; return ResourceSaver.Save(mesh, filename);
>
> }

}

To use **EditorImportPlugin**, register it using the `EditorPlugin.add_import_plugin()<class_EditorPlugin_method_add_import_plugin>` method first.

classref-introduction-group

## Tutorials

- `Import plugins <../tutorials/plugins/editor/import_plugins>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **\_can_import_threaded**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__can_import_threaded>`

Tells whether this importer can be run in parallel on threads, or, on the contrary, it's only safe for the editor to call it from the main thread, for one file at a time.

If this importer's implementation is thread-safe and can be run in parallel, override this with `true` to optimize for concurrency.

If not overridden, returns `false`.

classref-item-separator

classref-method

`int<class_int>` **\_get_format_version**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_format_version>`

Gets the format version of this importer. Increment this version when making incompatible changes to the format of the imported resources.

If not overridden, the format version is `0`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **\_get_import_options**(path: `String<class_String>`, preset_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_import_options>`

Gets the options and default values for the preset at this index. Returns an Array of Dictionaries with the following keys: `name`, `default_value`, `property_hint` (optional), `hint_string` (optional), `usage` (optional).

classref-item-separator

classref-method

`int<class_int>` **\_get_import_order**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_import_order>`

Gets the order of this importer to be run when importing resources. Importers with *lower* import orders will be called first, and higher values will be called later. Use this to ensure the importer runs after the dependencies are already imported. The default import order is `0` unless overridden by a specific importer. See `ImportOrder<enum_ResourceImporter_ImportOrder>` for some predefined values.

classref-item-separator

classref-method

`String<class_String>` **\_get_importer_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_importer_name>`

Gets the unique name of the importer.

classref-item-separator

classref-method

`bool<class_bool>` **\_get_option_visibility**(path: `String<class_String>`, option_name: `StringName<class_StringName>`, options: `Dictionary<class_Dictionary>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_option_visibility>`

Gets whether the import option specified by `option_name` should be visible in the Import dock. The default implementation always returns `true`, making all options visible. This is mainly useful for hiding options that depend on others if one of them is disabled.

gdscript

func get_option_visibility(path, option_name, options):
\# Only show the lossy quality setting if the compression mode is set to "Lossy". if option_name == "compress/lossy_quality" and options.has("compress/mode"): return int(options\["compress/mode"\]) == COMPRESS_LOSSY \# This is a constant that you set

return true

csharp

public override bool GetOptionVisibility(string path, StringName optionName, Godot.Collections.Dictionary options) { // Only show the lossy quality setting if the compression mode is set to "Lossy". if (optionName == "compress/lossy_quality" && options.ContainsKey("compress/mode")) { return (int)options\["compress/mode"\] == CompressLossy; // This is a constant you set }

> return true;

}

classref-item-separator

classref-method

`int<class_int>` **\_get_preset_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_preset_count>`

Gets the number of initial presets defined by the plugin. Use `_get_import_options()<class_EditorImportPlugin_private_method__get_import_options>` to get the default options for the preset and `_get_preset_name()<class_EditorImportPlugin_private_method__get_preset_name>` to get the name of the preset.

By default, there are no presets.

classref-item-separator

classref-method

`String<class_String>` **\_get_preset_name**(preset_index: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_preset_name>`

Gets the name of the options preset at this index.

classref-item-separator

classref-method

`float<class_float>` **\_get_priority**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_priority>`

Gets the priority of this plugin for the recognized extension. Higher priority plugins will be preferred. The default priority is `1.0`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_recognized_extensions**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_recognized_extensions>`

Gets the list of file extensions to associate with this loader (case-insensitive). e.g. `["obj"]`.

classref-item-separator

classref-method

`String<class_String>` **\_get_resource_type**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_resource_type>`

Gets the Godot resource type associated with this loader. e.g. `"Mesh"` or `"Animation"`.

classref-item-separator

classref-method

`String<class_String>` **\_get_save_extension**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_save_extension>`

Gets the extension used to save this resource in the `.godot/imported` directory (see `ProjectSettings.application/config/use_hidden_project_data_directory<class_ProjectSettings_property_application/config/use_hidden_project_data_directory>`).

classref-item-separator

classref-method

`String<class_String>` **\_get_visible_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__get_visible_name>`

Gets the name to display in the import window. You should choose this name as a continuation to "Import as", e.g. "Import as Special Mesh".

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_import**(source_file: `String<class_String>`, save_path: `String<class_String>`, options: `Dictionary<class_Dictionary>`, platform_variants: `Array<class_Array>`\[`String<class_String>`\], gen_files: `Array<class_Array>`\[`String<class_String>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorImportPlugin_private_method__import>`

Imports `source_file` with the import `options` specified. Should return `@GlobalScope.OK<class_@GlobalScope_constant_OK>` if the import is successful, other values indicate failure.

The imported resource is expected to be saved to `save_path + "." + _get_save_extension()`. If a different variant is preferred for a `feature tag <../tutorials/export/feature_tags>`, save the variant to `save_path + "." + tag + "." + _get_save_extension()` and add the feature tag to `platform_variants`.

If additional resource files are generated in the resource filesystem (`res://`), add their full path to `gen_files` so that the editor knows they depend on `source_file`.

This method must be overridden to do the actual importing work. See this class' description for an example of overriding this method.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **append_import_external_resource**(path: `String<class_String>`, custom_options: `Dictionary<class_Dictionary>` = {}, custom_importer: `String<class_String>` = "", generator_parameters: `Variant<class_Variant>` = null) `🔗<class_EditorImportPlugin_method_append_import_external_resource>`

This function can only be called during the `_import()<class_EditorImportPlugin_private_method__import>` callback and it allows manually importing resources from it. This is useful when the imported file generates external resources that require importing (as example, images). Custom parameters for the ".import" file can be passed via the `custom_options`. Additionally, in cases where multiple importers can handle a file, the `custom_importer` can be specified to force a specific one. This function performs a resource import and returns immediately with a success or error code. `generator_parameters` defines optional extra metadata which will be stored as `generator_parameters` in the `remap` section of the `.import` file, for example to store a md5 hash of the source data.