github_url
hide

# GDScriptWorkspace

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Workspace related language server functionality.

classref-introduction-group

## Description

Provides language server functionality related to the workspace.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **apply_new_signal**(obj: `Object<class_Object>`, function: `String<class_String>`, args: `PackedStringArray<class_PackedStringArray>`) `🔗<class_GDScriptWorkspace_method_apply_new_signal>`

**Deprecated:** Might result in unwanted side effects for connected clients.

classref-item-separator

classref-method

`void (No return value.)` **didDeleteFiles**(params: `Dictionary<class_Dictionary>`) `🔗<class_GDScriptWorkspace_method_didDeleteFiles>`

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **generate_script_api**(path: `String<class_String>`) `🔗<class_GDScriptWorkspace_method_generate_script_api>`

Returns the interface of the script in a machine-readable format.

classref-item-separator

classref-method

`String<class_String>` **get_file_path**(uri: `String<class_String>`) `🔗<class_GDScriptWorkspace_method_get_file_path>`

Converts a URI to a file path.

classref-item-separator

classref-method

`String<class_String>` **get_file_uri**(path: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDScriptWorkspace_method_get_file_uri>`

Converts a file path to a URI.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **parse_local_script**(path: `String<class_String>`) `🔗<class_GDScriptWorkspace_method_parse_local_script>`

**Deprecated:** Might result in unwanted side effects for connected clients.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **parse_script**(path: `String<class_String>`, content: `String<class_String>`) `🔗<class_GDScriptWorkspace_method_parse_script>`

**Deprecated:** Might result in unwanted side effects for connected clients.

classref-item-separator

classref-method

`void (No return value.)` **publish_diagnostics**(path: `String<class_String>`) `🔗<class_GDScriptWorkspace_method_publish_diagnostics>`

**Deprecated:** Might result in unwanted side effects for connected clients.