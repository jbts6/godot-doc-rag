github_url
hide

# EditorSyntaxHighlighter

**Inherits:** `SyntaxHighlighter<class_SyntaxHighlighter>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `GDScriptSyntaxHighlighter<class_GDScriptSyntaxHighlighter>`

Base class for `SyntaxHighlighter<class_SyntaxHighlighter>` used by the `ScriptEditor<class_ScriptEditor>`.

classref-introduction-group

## Description

Base class that all `SyntaxHighlighter<class_SyntaxHighlighter>`s used by the `ScriptEditor<class_ScriptEditor>` extend from.

Add a syntax highlighter to an individual script by calling `ScriptEditorBase.add_syntax_highlighter()<class_ScriptEditorBase_method_add_syntax_highlighter>`. To apply to all scripts on open, call `ScriptEditor.register_syntax_highlighter()<class_ScriptEditor_method_register_syntax_highlighter>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>` **\_create**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorSyntaxHighlighter_private_method__create>`

Virtual method which creates a new instance of the syntax highlighter.

classref-item-separator

classref-method

`String<class_String>` **\_get_name**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorSyntaxHighlighter_private_method__get_name>`

Virtual method which can be overridden to return the syntax highlighter name.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_supported_languages**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorSyntaxHighlighter_private_method__get_supported_languages>`

Virtual method which can be overridden to return the supported language names.