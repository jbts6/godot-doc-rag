github_url
hide

# ScriptEditor

**Inherits:** `PanelContainer<class_PanelContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Godot editor's script editor.

classref-introduction-group

## Description

Godot editor's script editor.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using `EditorInterface.get_script_editor()<class_EditorInterface_method_get_script_editor>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**editor_script_changed**(script: `Script<class_Script>`) `🔗<class_ScriptEditor_signal_editor_script_changed>`

Emitted when user changed active script. Argument is a freshly activated `Script<class_Script>`.

classref-item-separator

classref-signal

**script_close**(script: `Script<class_Script>`) `🔗<class_ScriptEditor_signal_script_close>`

Emitted when editor is about to close the active script. Argument is a `Script<class_Script>` that is going to be closed.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_docs_from_script**(script: `Script<class_Script>`) `🔗<class_ScriptEditor_method_clear_docs_from_script>`

Removes the documentation for the given `script`.

**Note:** This should be called whenever the script is changed to keep the open documentation state up to date.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **close_file**(path: `String<class_String>`) `🔗<class_ScriptEditor_method_close_file>`

Closes the file at the given `path`, discarding any unsaved changes.

Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success or `@GlobalScope.ERR_FILE_NOT_FOUND<class_@GlobalScope_constant_ERR_FILE_NOT_FOUND>` if the file is not found.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_breakpoints**() `🔗<class_ScriptEditor_method_get_breakpoints>`

Returns array of breakpoints.

classref-item-separator

classref-method

`ScriptEditorBase<class_ScriptEditorBase>` **get_current_editor**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptEditor_method_get_current_editor>`

Returns the `ScriptEditorBase<class_ScriptEditorBase>` object that the user is currently editing.

classref-item-separator

classref-method

`Script<class_Script>` **get_current_script**() `🔗<class_ScriptEditor_method_get_current_script>`

Returns a `Script<class_Script>` that is currently active in editor.

classref-item-separator

classref-method

`Array<class_Array>`\[`ScriptEditorBase<class_ScriptEditorBase>`\] **get_open_script_editors**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptEditor_method_get_open_script_editors>`

Returns an array with all `ScriptEditorBase<class_ScriptEditorBase>` objects which are currently open in editor.

classref-item-separator

classref-method

`Array<class_Array>`\[`Script<class_Script>`\] **get_open_scripts**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptEditor_method_get_open_scripts>`

Returns an array with all `Script<class_Script>` objects which are currently open in editor.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_unsaved_files**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptEditor_method_get_unsaved_files>`

Returns an array of file paths of scripts with unsaved changes open in the editor.

classref-item-separator

classref-method

`void (No return value.)` **goto_help**(topic: `String<class_String>`) `🔗<class_ScriptEditor_method_goto_help>`

Opens help for the given topic. The `topic` is an encoded string that controls which class, method, constant, signal, annotation, property, or theme item should be focused.

The supported `topic` formats include `class_name:class`, `class_method `class_constant `class_signal `class_annotation `class_property and `class_theme_item where `class` is the class name, `method` is the method name, `constant` is the constant name, `signal` is the signal name, `annotation` is the annotation name, `property` is the property name, and `item` is the theme item.

    # Shows help for the Node class.
    class_name:Node
    # Shows help for the global min function.
    # Global objects are accessible in the `@GlobalScope` namespace, shown here.
    class_method:@GlobalScope:min
    # Shows help for get_viewport in the Node class.
    class_method:Node:get_viewport
    # Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
    class_constant:Input:MOUSE_BUTTON_MIDDLE
    # Shows help for the BaseButton signal pressed.
    class_signal:BaseButton:pressed
    # Shows help for the CanvasItem property visible.
    class_property:CanvasItem:visible
    # Shows help for the GDScript annotation export.
    # Annotations should be prefixed with the `@` symbol in the descriptor, as shown here.
    class_annotation:@GDScript:@export
    # Shows help for the GraphNode theme item named panel_selected.
    class_theme_item:GraphNode:panel_selected

classref-item-separator

classref-method

`void (No return value.)` **goto_line**(line_number: `int<class_int>`) `🔗<class_ScriptEditor_method_goto_line>`

Goes to the specified line in the current script.

classref-item-separator

classref-method

`void (No return value.)` **open_script_create_dialog**(base_name: `String<class_String>`, base_path: `String<class_String>`) `🔗<class_ScriptEditor_method_open_script_create_dialog>`

Opens the script create dialog. The script will extend `base_name`. The file extension can be omitted from `base_path`. It will be added based on the selected scripting language.

classref-item-separator

classref-method

`void (No return value.)` **register_syntax_highlighter**(syntax_highlighter: `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`) `🔗<class_ScriptEditor_method_register_syntax_highlighter>`

Registers the `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` to the editor, the `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` will be available on all open scripts.

**Note:** Does not apply to scripts that are already opened.

classref-item-separator

classref-method

`void (No return value.)` **reload_open_files**() `🔗<class_ScriptEditor_method_reload_open_files>`

Reloads all currently opened files. This should be used when opened files are changed outside of the script editor. The user may be prompted to resolve file conflicts, see `EditorSettings.text_editor/behavior/files/auto_reload_scripts_on_external_change<class_EditorSettings_property_text_editor/behavior/files/auto_reload_scripts_on_external_change>`.

classref-item-separator

classref-method

`void (No return value.)` **save_all_scripts**() `🔗<class_ScriptEditor_method_save_all_scripts>`

Saves all open scripts.

classref-item-separator

classref-method

`void (No return value.)` **unregister_syntax_highlighter**(syntax_highlighter: `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`) `🔗<class_ScriptEditor_method_unregister_syntax_highlighter>`

Unregisters the `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` from the editor.

**Note:** The `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` will still be applied to scripts that are already opened.

classref-item-separator

classref-method

`void (No return value.)` **update_docs_from_script**(script: `Script<class_Script>`) `🔗<class_ScriptEditor_method_update_docs_from_script>`

Updates the documentation for the given `script`.

**Note:** This should be called whenever the script is changed to keep the open documentation state up to date.