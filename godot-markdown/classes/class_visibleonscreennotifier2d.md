github_url
hide

# VisibleOnScreenNotifier2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `VisibleOnScreenEnabler2D<class_VisibleOnScreenEnabler2D>`

A rectangular region of 2D space that detects whether it is visible on screen.

classref-introduction-group

## Description

**VisibleOnScreenNotifier2D** represents a rectangular region of 2D space. When any part of this region becomes visible on screen or in a viewport, it will emit a `screen_entered<class_VisibleOnScreenNotifier2D_signal_screen_entered>` signal, and likewise it will emit a `screen_exited<class_VisibleOnScreenNotifier2D_signal_screen_exited>` signal when no part of it remains visible.

If you want a node to be enabled automatically when this region is visible on screen, use `VisibleOnScreenEnabler2D<class_VisibleOnScreenEnabler2D>`.

**Note:** **VisibleOnScreenNotifier2D** uses the render culling code to determine whether it's visible on screen, so it won't function unless `CanvasItem.visible<class_CanvasItem_property_visible>` is set to `true`.

classref-introduction-group

## Tutorials

- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**screen_entered**() `🔗<class_VisibleOnScreenNotifier2D_signal_screen_entered>`

Emitted when the VisibleOnScreenNotifier2D enters the screen.

classref-item-separator

classref-signal

**screen_exited**() `🔗<class_VisibleOnScreenNotifier2D_signal_screen_exited>`

Emitted when the VisibleOnScreenNotifier2D exits the screen.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Rect2<class_Rect2>` **rect** = `Rect2(-10, -10, 20, 20)` `🔗<class_VisibleOnScreenNotifier2D_property_rect>`

classref-property-setget

- `void (No return value.)` **set_rect**(value: `Rect2<class_Rect2>`)
- `Rect2<class_Rect2>` **get_rect**()

The VisibleOnScreenNotifier2D's bounding rectangle.

classref-item-separator

classref-property

`bool<class_bool>` **show_rect** = `true` `🔗<class_VisibleOnScreenNotifier2D_property_show_rect>`

classref-property-setget

- `void (No return value.)` **set_show_rect**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_showing_rect**()

If `true`, shows the rectangle area of `rect<class_VisibleOnScreenNotifier2D_property_rect>` in the editor with a translucent magenta fill. Unlike changing the visibility of the VisibleOnScreenNotifier2D, this does not affect the screen culling detection.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_on_screen**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_VisibleOnScreenNotifier2D_method_is_on_screen>`

If `true`, the bounding rectangle is on the screen.

**Note:** It takes one frame for the **VisibleOnScreenNotifier2D**'s visibility to be determined once added to the scene tree, so this method will always return `false` right after it is instantiated, before the draw pass.