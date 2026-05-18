github_url
hide

# MarginContainer

**Inherits:** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `EditorDock<class_EditorDock>`

A container that keeps a margin around its child controls.

classref-introduction-group

## Description

**MarginContainer** adds an adjustable margin on each side of its child controls. The margins are added around all children, not around each individual one. To control the **MarginContainer**'s margins, use the `margin_*` theme properties listed below.

**Note:** The margin sizes are theme overrides, not normal properties. This is an example of how to change them in code:

gdscript

\# This code sample assumes the current script is extending MarginContainer. var margin_value = 100 add_theme_constant_override("margin_top", margin_value) add_theme_constant_override("margin_left", margin_value) add_theme_constant_override("margin_bottom", margin_value) add_theme_constant_override("margin_right", margin_value)

csharp

// This code sample assumes the current script is extending MarginContainer. int marginValue = 100; AddThemeConstantOverride("margin_top", marginValue); AddThemeConstantOverride("margin_left", marginValue); AddThemeConstantOverride("margin_bottom", marginValue); AddThemeConstantOverride("margin_right", marginValue);

classref-introduction-group

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`int<class_int>` **margin_bottom** = `0` `🔗<class_MarginContainer_theme_constant_margin_bottom>`

Offsets towards the inside direct children of the container by this amount of pixels from the bottom.

classref-item-separator

classref-themeproperty

`int<class_int>` **margin_left** = `0` `🔗<class_MarginContainer_theme_constant_margin_left>`

Offsets towards the inside direct children of the container by this amount of pixels from the left.

classref-item-separator

classref-themeproperty

`int<class_int>` **margin_right** = `0` `🔗<class_MarginContainer_theme_constant_margin_right>`

Offsets towards the inside direct children of the container by this amount of pixels from the right.

classref-item-separator

classref-themeproperty

`int<class_int>` **margin_top** = `0` `🔗<class_MarginContainer_theme_constant_margin_top>`

Offsets towards the inside direct children of the container by this amount of pixels from the top.