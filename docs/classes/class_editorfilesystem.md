github_url
hide

# EditorFileSystem

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

Resource filesystem, as the editor sees it.

classref-introduction-group

## Description

This object holds information of all resources in the filesystem, their types, etc.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using `EditorInterface.get_resource_filesystem()<class_EditorInterface_method_get_resource_filesystem>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**filesystem_changed**() `🔗<class_EditorFileSystem_signal_filesystem_changed>`

Emitted if the filesystem changed.

classref-item-separator

classref-signal

**resources_reimported**(resources: `PackedStringArray<class_PackedStringArray>`) `🔗<class_EditorFileSystem_signal_resources_reimported>`

Emitted if a resource is reimported.

classref-item-separator

classref-signal

**resources_reimporting**(resources: `PackedStringArray<class_PackedStringArray>`) `🔗<class_EditorFileSystem_signal_resources_reimporting>`

Emitted before a resource is reimported.

classref-item-separator

classref-signal

**resources_reload**(resources: `PackedStringArray<class_PackedStringArray>`) `🔗<class_EditorFileSystem_signal_resources_reload>`

Emitted if at least one resource is reloaded when the filesystem is scanned.

classref-item-separator

classref-signal

**script_classes_updated**() `🔗<class_EditorFileSystem_signal_script_classes_updated>`

Emitted when the list of global script classes gets updated.

classref-item-separator

classref-signal

**sources_changed**(exist: `bool<class_bool>`) `🔗<class_EditorFileSystem_signal_sources_changed>`

Emitted if the source of any imported file changed.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_file_type**(path: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystem_method_get_file_type>`

Returns the resource type of the file, given the full path. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

classref-item-separator

classref-method

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` **get_filesystem**() `🔗<class_EditorFileSystem_method_get_filesystem>`

Gets the root directory object.

classref-item-separator

classref-method

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` **get_filesystem_path**(path: `String<class_String>`) `🔗<class_EditorFileSystem_method_get_filesystem_path>`

Returns a view into the filesystem at `path`.

classref-item-separator

classref-method

`float<class_float>` **get_scanning_progress**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystem_method_get_scanning_progress>`

Returns the scan progress for 0 to 1 if the FS is being scanned.

classref-item-separator

classref-method

`bool<class_bool>` **is_importing**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystem_method_is_importing>`

Returns `true` if resources are currently being imported.

classref-item-separator

classref-method

`bool<class_bool>` **is_scanning**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystem_method_is_scanning>`

Returns `true` if the filesystem is being scanned.

classref-item-separator

classref-method

`void (No return value.)` **reimport_files**(files: `PackedStringArray<class_PackedStringArray>`) `🔗<class_EditorFileSystem_method_reimport_files>`

Reimports a set of files. Call this if these files or their `.import` files were directly edited by script or an external program.

If the file type changed or the file was newly created, use `update_file()<class_EditorFileSystem_method_update_file>` or `scan()<class_EditorFileSystem_method_scan>`.

**Note:** This function blocks until the import is finished. However, the main loop iteration, including timers and `Node._process()<class_Node_private_method__process>`, will occur during the import process due to progress bar updates. Avoid calls to `reimport_files()<class_EditorFileSystem_method_reimport_files>` or `scan()<class_EditorFileSystem_method_scan>` while an import is in progress.

classref-item-separator

classref-method

`void (No return value.)` **scan**() `🔗<class_EditorFileSystem_method_scan>`

Scan the filesystem for changes.

classref-item-separator

classref-method

`void (No return value.)` **scan_sources**() `🔗<class_EditorFileSystem_method_scan_sources>`

Check if the source of any imported resource changed.

classref-item-separator

classref-method

`void (No return value.)` **update_file**(path: `String<class_String>`) `🔗<class_EditorFileSystem_method_update_file>`

Add a file in an existing directory, or schedule file information to be updated on editor restart. Can be used to update text files saved by an external program.

This will not import the file. To reimport, call `reimport_files()<class_EditorFileSystem_method_reimport_files>` or `scan()<class_EditorFileSystem_method_scan>` methods.