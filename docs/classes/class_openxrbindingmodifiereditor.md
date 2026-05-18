github_url
hide

# OpenXRBindingModifierEditor

**Inherits:** `PanelContainer<class_PanelContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Binding modifier editor.

classref-introduction-group

## Description

This is the default binding modifier editor used in the OpenXR action map.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**binding_modifier_removed**(binding_modifier_editor: `Object<class_Object>`) `🔗<class_OpenXRBindingModifierEditor_signal_binding_modifier_removed>`

Signal emitted when the user presses the delete binding modifier button for this modifier.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`OpenXRBindingModifier<class_OpenXRBindingModifier>` **get_binding_modifier**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRBindingModifierEditor_method_get_binding_modifier>`

Returns the `OpenXRBindingModifier<class_OpenXRBindingModifier>` currently being edited.

classref-item-separator

classref-method

`void (No return value.)` **setup**(action_map: `OpenXRActionMap<class_OpenXRActionMap>`, binding_modifier: `OpenXRBindingModifier<class_OpenXRBindingModifier>`) `🔗<class_OpenXRBindingModifierEditor_method_setup>`

Setup this editor for the provided `action_map` and `binding_modifier`.