github_url
hide

# VScrollBar

**Inherits:** `ScrollBar<class_ScrollBar>` **\<** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A vertical scrollbar that goes from top (min) to bottom (max).

classref-introduction-group

## Description

A vertical scrollbar, typically used to navigate through content that extends beyond the visible height of a control. It is a `Range<class_Range>`-based control and goes from top (min) to bottom (max). Note that this direction is the opposite of `VSlider<class_VSlider>`'s.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`int<class_int>` **padding_left** = `0` `🔗<class_VScrollBar_theme_constant_padding_left>`

Padding between the left of the `ScrollBar.scroll<class_ScrollBar_theme_style_scroll>` element and the `ScrollBar.grabber<class_ScrollBar_theme_style_grabber>`.

**Note:** To apply vertical padding, modify the top/bottom content margins of `ScrollBar.scroll<class_ScrollBar_theme_style_scroll>` instead.

classref-item-separator

classref-themeproperty

`int<class_int>` **padding_right** = `0` `🔗<class_VScrollBar_theme_constant_padding_right>`

Padding between the right of the `ScrollBar.scroll<class_ScrollBar_theme_style_scroll>` element and the `ScrollBar.grabber<class_ScrollBar_theme_style_grabber>`.

**Note:** To apply vertical padding, modify the top/bottom content margins of `ScrollBar.scroll<class_ScrollBar_theme_style_scroll>` instead.