github_url
hide

# AcceptDialog

**Inherits:** `Window<class_Window>` **\<** `Viewport<class_Viewport>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `ConfirmationDialog<class_ConfirmationDialog>`

A base dialog used for user notification.

classref-introduction-group

## Description

The default use of **AcceptDialog** is to allow it to only be accepted or closed, with the same result. However, the `confirmed<class_AcceptDialog_signal_confirmed>` and `canceled<class_AcceptDialog_signal_canceled>` signals allow to make the two actions different, and the `add_button()<class_AcceptDialog_method_add_button>` method allows to add custom buttons and actions.

**Note:** **AcceptDialog** is invisible by default. To make it visible, call one of the `popup_*` methods from `Window<class_Window>` on the node, such as `Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**canceled**() `🔗<class_AcceptDialog_signal_canceled>`

Emitted when the dialog is closed or the button created with `add_cancel_button()<class_AcceptDialog_method_add_cancel_button>` is pressed.

classref-item-separator

classref-signal

**confirmed**() `🔗<class_AcceptDialog_signal_confirmed>`

Emitted when the dialog is accepted, i.e. the OK button is pressed.

classref-item-separator

classref-signal

**custom_action**(action: `StringName<class_StringName>`) `🔗<class_AcceptDialog_signal_custom_action>`

Emitted when a custom button with an action is pressed. See `add_button()<class_AcceptDialog_method_add_button>`.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **dialog_autowrap** = `false` `🔗<class_AcceptDialog_property_dialog_autowrap>`

classref-property-setget

- `void (No return value.)` **set_autowrap**(value: `bool<class_bool>`)
- `bool<class_bool>` **has_autowrap**()

Sets autowrapping for the text in the dialog.

classref-item-separator

classref-property

`bool<class_bool>` **dialog_close_on_escape** = `true` `🔗<class_AcceptDialog_property_dialog_close_on_escape>`

classref-property-setget

- `void (No return value.)` **set_close_on_escape**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_close_on_escape**()

If `true`, the dialog will be hidden when the `ui_close_dialog` action is pressed (by default, this action is bound to `Escape`, or `Cmd + W` on macOS).

classref-item-separator

classref-property

`bool<class_bool>` **dialog_hide_on_ok** = `true` `🔗<class_AcceptDialog_property_dialog_hide_on_ok>`

classref-property-setget

- `void (No return value.)` **set_hide_on_ok**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_hide_on_ok**()

If `true`, the dialog is hidden when the OK button is pressed. You can set it to `false` if you want to do e.g. input validation when receiving the `confirmed<class_AcceptDialog_signal_confirmed>` signal, and handle hiding the dialog in your own logic.

**Note:** Some nodes derived from this class can have a different default value, and potentially their own built-in logic overriding this setting. For example `FileDialog<class_FileDialog>` defaults to `false`, and has its own input validation code that is called when you press OK, which eventually hides the dialog if the input is valid. As such, this property can't be used in `FileDialog<class_FileDialog>` to disable hiding the dialog when pressing OK.

classref-item-separator

classref-property

`String<class_String>` **dialog_text** = `""` `🔗<class_AcceptDialog_property_dialog_text>`

classref-property-setget

- `void (No return value.)` **set_text**(value: `String<class_String>`)
- `String<class_String>` **get_text**()

The text displayed by the dialog.

classref-item-separator

classref-property

`String<class_String>` **ok_button_text** = `""` `🔗<class_AcceptDialog_property_ok_button_text>`

classref-property-setget

- `void (No return value.)` **set_ok_button_text**(value: `String<class_String>`)
- `String<class_String>` **get_ok_button_text**()

The text displayed by the OK button (see `get_ok_button()<class_AcceptDialog_method_get_ok_button>`). If empty, a default text will be used.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Button<class_Button>` **add_button**(text: `String<class_String>`, right: `bool<class_bool>` = false, action: `String<class_String>` = "") `🔗<class_AcceptDialog_method_add_button>`

Adds a button with label `text` and a custom `action` to the dialog and returns the created button.

If `action` is not empty, pressing the button will emit the `custom_action<class_AcceptDialog_signal_custom_action>` signal with the specified action string.

If `true`, `right` will place the button to the right of any sibling buttons.

You can use `remove_button()<class_AcceptDialog_method_remove_button>` method to remove a button created with this method from the dialog.

classref-item-separator

classref-method

`Button<class_Button>` **add_cancel_button**(name: `String<class_String>`) `🔗<class_AcceptDialog_method_add_cancel_button>`

Adds a button with label `name` and a cancel action to the dialog and returns the created button.

You can use `remove_button()<class_AcceptDialog_method_remove_button>` method to remove a button created with this method from the dialog.

classref-item-separator

classref-method

`Label<class_Label>` **get_label**() `🔗<class_AcceptDialog_method_get_label>`

Returns the label used for built-in text.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `CanvasItem.visible<class_CanvasItem_property_visible>` property.

classref-item-separator

classref-method

`Button<class_Button>` **get_ok_button**() `🔗<class_AcceptDialog_method_get_ok_button>`

Returns the OK `Button<class_Button>` instance.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `CanvasItem.visible<class_CanvasItem_property_visible>` property.

classref-item-separator

classref-method

`void (No return value.)` **register_text_enter**(line_edit: `LineEdit<class_LineEdit>`) `🔗<class_AcceptDialog_method_register_text_enter>`

Registers a `LineEdit<class_LineEdit>` in the dialog. When the enter key is pressed, the dialog will be accepted.

classref-item-separator

classref-method

`void (No return value.)` **remove_button**(button: `Button<class_Button>`) `🔗<class_AcceptDialog_method_remove_button>`

Removes the `button` from the dialog. Does NOT free the `button`. The `button` must be a `Button<class_Button>` added with `add_button()<class_AcceptDialog_method_add_button>` or `add_cancel_button()<class_AcceptDialog_method_add_cancel_button>` method. After removal, pressing the `button` will no longer emit this dialog's `custom_action<class_AcceptDialog_signal_custom_action>` or `canceled<class_AcceptDialog_signal_canceled>` signals.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`int<class_int>` **buttons_min_height** = `0` `🔗<class_AcceptDialog_theme_constant_buttons_min_height>`

The minimum height of each button in the bottom row (such as OK/Cancel) in pixels. This can be increased to make buttons with short texts easier to click/tap.

classref-item-separator

classref-themeproperty

`int<class_int>` **buttons_min_width** = `0` `🔗<class_AcceptDialog_theme_constant_buttons_min_width>`

The minimum width of each button in the bottom row (such as OK/Cancel) in pixels. This can be increased to make buttons with short texts easier to click/tap.

classref-item-separator

classref-themeproperty

`int<class_int>` **buttons_separation** = `10` `🔗<class_AcceptDialog_theme_constant_buttons_separation>`

The size of the vertical space between the dialog's content and the button row.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel** `🔗<class_AcceptDialog_theme_style_panel>`

The panel that fills the background of the window.