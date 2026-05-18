github_url
hide

# GDScriptLanguageProtocol

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `JSONRPC<class_JSONRPC>` **\<** `Object<class_Object>`

GDScript language server.

classref-introduction-group

## Description

Provides access to certain features that are implemented in the language server.

**Note:** This class is not a language server client that can be used to access LSP functionality. It only provides access to a limited set of features that is implemented using the same technical foundation as the language server.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`GDScriptTextDocument<class_GDScriptTextDocument>` **get_text_document**() `🔗<class_GDScriptLanguageProtocol_method_get_text_document>`

**Deprecated:** `GDScriptTextDocument<class_GDScriptTextDocument>` is deprecated.

Returns the language server's `GDScriptTextDocument<class_GDScriptTextDocument>` instance.

classref-item-separator

classref-method

`GDScriptWorkspace<class_GDScriptWorkspace>` **get_workspace**() `🔗<class_GDScriptLanguageProtocol_method_get_workspace>`

Returns the language server's `GDScriptWorkspace<class_GDScriptWorkspace>` instance.

classref-item-separator

classref-method

`Variant<class_Variant>` **initialize**(params: `Dictionary<class_Dictionary>`) `🔗<class_GDScriptLanguageProtocol_method_initialize>`

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

classref-item-separator

classref-method

`void (No return value.)` **initialized**(params: `Variant<class_Variant>`) `🔗<class_GDScriptLanguageProtocol_method_initialized>`

**Deprecated:** Accessing LSP endpoints directly might lead to unwanted side effects. Connect to the server via TCP, like a regular language server client.

classref-item-separator

classref-method

`bool<class_bool>` **is_initialized**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDScriptLanguageProtocol_method_is_initialized>`

Returns `true` if the language server was initialized by a language server client, `false` otherwise.

classref-item-separator

classref-method

`bool<class_bool>` **is_smart_resolve_enabled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GDScriptLanguageProtocol_method_is_smart_resolve_enabled>`

Returns `true` if the language server is providing the smart resolve feature, `false` otherwise. The feature can be configured through the editor settings.

classref-item-separator

classref-method

`void (No return value.)` **notify_client**(method: `String<class_String>`, params: `Variant<class_Variant>` = null, client_id: `int<class_int>` = -1) `🔗<class_GDScriptLanguageProtocol_method_notify_client>`

**Deprecated:** Might result in unwanted side effects for connected clients.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **on_client_connected**() `🔗<class_GDScriptLanguageProtocol_method_on_client_connected>`

**Deprecated:** Might result in unwanted side effects for connected clients.

classref-item-separator

classref-method

`void (No return value.)` **on_client_disconnected**(client_id: `int<class_int>`) `🔗<class_GDScriptLanguageProtocol_method_on_client_disconnected>`

**Deprecated:** Might result in unwanted side effects for connected clients.