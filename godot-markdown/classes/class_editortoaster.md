github_url
hide

# EditorToaster

**Inherits:** `HBoxContainer<class_HBoxContainer>` **\<** `BoxContainer<class_BoxContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Manages toast notifications within the editor.

classref-introduction-group

## Description

This object manages the functionality and display of toast notifications within the editor, ensuring immediate and informative alerts are presented to the user.

**Note:** This class shouldn't be instantiated directly. Instead, access the singleton using `EditorInterface.get_editor_toaster()<class_EditorInterface_method_get_editor_toaster>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Severity**: `🔗<enum_EditorToaster_Severity>`

classref-enumeration-constant

`Severity<enum_EditorToaster_Severity>` **SEVERITY_INFO** = `0`

Toast will display with an INFO severity.

classref-enumeration-constant

`Severity<enum_EditorToaster_Severity>` **SEVERITY_WARNING** = `1`

Toast will display with a WARNING severity and have a corresponding color.

classref-enumeration-constant

`Severity<enum_EditorToaster_Severity>` **SEVERITY_ERROR** = `2`

Toast will display with an ERROR severity and have a corresponding color.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **push_toast**(message: `String<class_String>`, severity: `Severity<enum_EditorToaster_Severity>` = 0, tooltip: `String<class_String>` = "") `🔗<class_EditorToaster_method_push_toast>`

Pushes a toast notification to the editor for display.