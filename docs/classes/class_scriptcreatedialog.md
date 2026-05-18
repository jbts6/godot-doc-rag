github_url
hide

# ScriptCreateDialog

**Inherits:** `ConfirmationDialog<class_ConfirmationDialog>` **\<** `AcceptDialog<class_AcceptDialog>` **\<** `Window<class_Window>` **\<** `Viewport<class_Viewport>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Godot editor's popup dialog for creating new `Script<class_Script>` files.

classref-introduction-group

## Description

The **ScriptCreateDialog** creates script files according to a given template for a given scripting language. The standard use is to configure its fields prior to calling one of the `Window.popup()<class_Window_method_popup>` methods.

gdscript

func ready():
var dialog = ScriptCreateDialog.new(); dialog.config("Node", "res://new_node.gd") \# For in-engine types. dialog.config(""res://base_node.gd"", "res://derived_node.gd") \# For script types. dialog.popup_centered()

csharp

public override void Ready() { var dialog = new ScriptCreateDialog(); dialog.Config("Node", "res://NewNode.cs"); // For in-engine types. dialog.Config(""res://BaseNode.cs"", "res://DerivedNode.cs"); // For script types. dialog.PopupCentered(); }

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**script_created**(script: `Script<class_Script>`) `🔗<class_ScriptCreateDialog_signal_script_created>`

Emitted when the user clicks the OK button.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **config**(inherits: `String<class_String>`, path: `String<class_String>`, built_in_enabled: `bool<class_bool>` = true, load_enabled: `bool<class_bool>` = true) `🔗<class_ScriptCreateDialog_method_config>`

Prefills required fields to configure the ScriptCreateDialog for use.