github_url
hide

# Popup

**Inherits:** `Window<class_Window>` **\<** `Viewport<class_Viewport>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `PopupMenu<class_PopupMenu>`, `PopupPanel<class_PopupPanel>`

Base class for contextual windows and panels with fixed position.

classref-introduction-group

## Description

**Popup** is a base class for contextual windows and panels with fixed position. It's a modal by default (see `Window.popup_window<class_Window_property_popup_window>`) and provides methods for implementing custom popup behavior.

**Note:** **Popup** is invisible by default. To make it visible, call one of the `popup_*` methods from `Window<class_Window>` on the node, such as `Window.popup_centered_clamped()<class_Window_method_popup_centered_clamped>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**popup_hide**() `🔗<class_Popup_signal_popup_hide>`

Emitted when the popup is hidden.