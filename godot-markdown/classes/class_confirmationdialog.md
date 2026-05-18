github_url
hide

# ConfirmationDialog

**Inherits:** `AcceptDialog<class_AcceptDialog>` **\<** `Window<class_Window>` **\<** `Viewport<class_Viewport>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `EditorCommandPalette<class_EditorCommandPalette>`, `FileDialog<class_FileDialog>`, `ScriptCreateDialog<class_ScriptCreateDialog>`

A dialog used for confirmation of actions.

classref-introduction-group

## Description

A dialog used for confirmation of actions. This window is similar to `AcceptDialog<class_AcceptDialog>`, but pressing its Cancel button can have a different outcome from pressing the OK button. The order of the two buttons varies depending on the host OS.

To get cancel action, you can use:

gdscript

get_cancel_button().pressed.connect(on_canceled)

csharp

GetCancelButton().Pressed += OnCanceled;

**Note:** `AcceptDialog<class_AcceptDialog>` is invisible by default. To make it visible, call one of the `popup_*` methods from `Window<class_Window>` on the node, such as `Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **cancel_button_text** = `"Cancel"` `🔗<class_ConfirmationDialog_property_cancel_button_text>`

classref-property-setget

- `void (No return value.)` **set_cancel_button_text**(value: `String<class_String>`)
- `String<class_String>` **get_cancel_button_text**()

The text displayed by the cancel button (see `get_cancel_button()<class_ConfirmationDialog_method_get_cancel_button>`).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Button<class_Button>` **get_cancel_button**() `🔗<class_ConfirmationDialog_method_get_cancel_button>`

Returns the cancel button.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `CanvasItem.visible<class_CanvasItem_property_visible>` property.