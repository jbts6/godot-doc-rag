github_url
hide

# FileSystemDock

**Inherits:** `EditorDock<class_EditorDock>` **\<** `MarginContainer<class_MarginContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Godot editor's dock for managing files in the project.

classref-introduction-group

## Description

This class is available only in `EditorPlugin<class_EditorPlugin>`s and can't be instantiated. You can access it using `EditorInterface.get_file_system_dock()<class_EditorInterface_method_get_file_system_dock>`.

While **FileSystemDock** doesn't expose any methods for file manipulation, it can listen for various file-related signals.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**display_mode_changed**() `🔗<class_FileSystemDock_signal_display_mode_changed>`

Emitted when the user switches file display mode or split mode.

classref-item-separator

classref-signal

**file_removed**(file: `String<class_String>`) `🔗<class_FileSystemDock_signal_file_removed>`

Emitted when the given `file` was removed.

classref-item-separator

classref-signal

**files_moved**(old_file: `String<class_String>`, new_file: `String<class_String>`) `🔗<class_FileSystemDock_signal_files_moved>`

Emitted when a file is moved from `old_file` path to `new_file` path.

classref-item-separator

classref-signal

**folder_color_changed**() `🔗<class_FileSystemDock_signal_folder_color_changed>`

Emitted when folders change color.

classref-item-separator

classref-signal

**folder_moved**(old_folder: `String<class_String>`, new_folder: `String<class_String>`) `🔗<class_FileSystemDock_signal_folder_moved>`

Emitted when a folder is moved from `old_folder` path to `new_folder` path.

classref-item-separator

classref-signal

**folder_removed**(folder: `String<class_String>`) `🔗<class_FileSystemDock_signal_folder_removed>`

Emitted when the given `folder` was removed.

classref-item-separator

classref-signal

**inherit**(file: `String<class_String>`) `🔗<class_FileSystemDock_signal_inherit>`

Emitted when a new scene is created that inherits the scene at `file` path.

classref-item-separator

classref-signal

**instantiate**(files: `PackedStringArray<class_PackedStringArray>`) `🔗<class_FileSystemDock_signal_instantiate>`

Emitted when the given scenes are being instantiated in the editor.

classref-item-separator

classref-signal

**resource_removed**(resource: `Resource<class_Resource>`) `🔗<class_FileSystemDock_signal_resource_removed>`

Emitted when an external `resource` had its file removed.

classref-item-separator

classref-signal

**selection_changed**() `🔗<class_FileSystemDock_signal_selection_changed>`

Emitted when the selection changes. Use `EditorInterface.get_selected_paths()<class_EditorInterface_method_get_selected_paths>` in the connected method to get the selected paths.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_resource_tooltip_plugin**(plugin: `EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`) `🔗<class_FileSystemDock_method_add_resource_tooltip_plugin>`

Registers a new `EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`.

classref-item-separator

classref-method

`void (No return value.)` **navigate_to_path**(path: `String<class_String>`) `🔗<class_FileSystemDock_method_navigate_to_path>`

Sets the given `path` as currently selected, ensuring that the selected file/directory is visible.

classref-item-separator

classref-method

`void (No return value.)` **remove_resource_tooltip_plugin**(plugin: `EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`) `🔗<class_FileSystemDock_method_remove_resource_tooltip_plugin>`

Removes an `EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`. Fails if the plugin wasn't previously added.