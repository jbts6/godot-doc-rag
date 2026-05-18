github_url
hide

# ReferenceRect

**Inherits:** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A rectangular box for designing UIs.

classref-introduction-group

## Description

A rectangular box that displays only a colored border around its rectangle (see `Control.get_rect()<class_Control_method_get_rect>`). It can be used to visualize the extents of a `Control<class_Control>` node, for testing purposes.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **border_color** = `Color(1, 0, 0, 1)` `🔗<class_ReferenceRect_property_border_color>`

classref-property-setget

- `void (No return value.)` **set_border_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_border_color**()

Sets the border color of the **ReferenceRect**.

classref-item-separator

classref-property

`float<class_float>` **border_width** = `1.0` `🔗<class_ReferenceRect_property_border_width>`

classref-property-setget

- `void (No return value.)` **set_border_width**(value: `float<class_float>`)
- `float<class_float>` **get_border_width**()

Sets the border width of the **ReferenceRect**. The border grows both inwards and outwards with respect to the rectangle box.

classref-item-separator

classref-property

`bool<class_bool>` **editor_only** = `true` `🔗<class_ReferenceRect_property_editor_only>`

classref-property-setget

- `void (No return value.)` **set_editor_only**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_editor_only**()

If `true`, the **ReferenceRect** will only be visible while in editor. Otherwise, **ReferenceRect** will be visible in the running project.