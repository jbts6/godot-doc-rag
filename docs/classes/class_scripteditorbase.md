github_url
hide

# ScriptEditorBase

**Inherits:** `VBoxContainer<class_VBoxContainer>` **\<** `BoxContainer<class_BoxContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Base editor for editing scripts in the `ScriptEditor<class_ScriptEditor>`.

classref-introduction-group

## Description

Base editor for editing scripts in the `ScriptEditor<class_ScriptEditor>`. This does not include documentation items.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**edited_script_changed**() `🔗<class_ScriptEditorBase_signal_edited_script_changed>`

Emitted after script validation.

classref-item-separator

classref-signal

**go_to_help**(what: `String<class_String>`) `🔗<class_ScriptEditorBase_signal_go_to_help>`

Emitted when the user requests a specific documentation page.

classref-item-separator

classref-signal

**go_to_method**(script: `Object<class_Object>`, method: `String<class_String>`) `🔗<class_ScriptEditorBase_signal_go_to_method>`

Emitted when the user requests to view a specific method of a script, similar to `request_open_script_at_line<class_ScriptEditorBase_signal_request_open_script_at_line>`.

classref-item-separator

classref-signal

**name_changed**() `🔗<class_ScriptEditorBase_signal_name_changed>`

Emitted after script validation or when the edited resource has changed.

classref-item-separator

classref-signal

**replace_in_files_requested**(text: `String<class_String>`) `🔗<class_ScriptEditorBase_signal_replace_in_files_requested>`

Emitted when the user request to find and replace text in the file system.

classref-item-separator

classref-signal

**request_help**(topic: `String<class_String>`) `🔗<class_ScriptEditorBase_signal_request_help>`

Emitted when the user requests contextual help.

classref-item-separator

classref-signal

**request_open_script_at_line**(script: `Object<class_Object>`, line: `int<class_int>`) `🔗<class_ScriptEditorBase_signal_request_open_script_at_line>`

Emitted when the user requests to view a specific line of a script, similar to `go_to_method<class_ScriptEditorBase_signal_go_to_method>`.

classref-item-separator

classref-signal

**request_save_history**() `🔗<class_ScriptEditorBase_signal_request_save_history>`

Emitted when the user contextual goto and the item is in the same script.

classref-item-separator

classref-signal

**request_save_previous_state**(state: `Dictionary<class_Dictionary>`) `🔗<class_ScriptEditorBase_signal_request_save_previous_state>`

Emitted when the user changes current script or moves caret by 10 or more columns within the same script.

classref-item-separator

classref-signal

**search_in_files_requested**(text: `String<class_String>`) `🔗<class_ScriptEditorBase_signal_search_in_files_requested>`

Emitted when the user request to search text in the file system.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_syntax_highlighter**(highlighter: `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`) `🔗<class_ScriptEditorBase_method_add_syntax_highlighter>`

Adds an `EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` to the open script.

classref-item-separator

classref-method

`Control<class_Control>` **get_base_editor**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ScriptEditorBase_method_get_base_editor>`

Returns the underlying `Control<class_Control>` used for editing scripts. For text scripts, this is a `CodeEdit<class_CodeEdit>`.