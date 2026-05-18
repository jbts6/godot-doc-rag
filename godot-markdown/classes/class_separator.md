github_url
hide

# Separator

**Inherits:** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `HSeparator<class_HSeparator>`, `VSeparator<class_VSeparator>`

Abstract base class for separators.

classref-introduction-group

## Description

Abstract base class for separators, used for separating other controls. **Separator**s are purely visual and normally drawn as a `StyleBoxLine<class_StyleBoxLine>`.

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`int<class_int>` **separation** = `0` `🔗<class_Separator_theme_constant_separation>`

The size of the area covered by the separator. Effectively works like a minimum width/height.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **separator** `🔗<class_Separator_theme_style_separator>`

The style for the separator line. Works best with `StyleBoxLine<class_StyleBoxLine>` (remember to enable `StyleBoxLine.vertical<class_StyleBoxLine_property_vertical>` for `VSeparator<class_VSeparator>`).