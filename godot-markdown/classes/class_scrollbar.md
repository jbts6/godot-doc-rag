github_url
hide

# ScrollBar

**Inherits:** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `HScrollBar<class_HScrollBar>`, `VScrollBar<class_VScrollBar>`

Abstract base class for scrollbars.

classref-introduction-group

## Description

Abstract base class for scrollbars, typically used to navigate through content that extends beyond the visible area of a control. Scrollbars are `Range<class_Range>`-based controls.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**scrolling**() `🔗<class_ScrollBar_signal_scrolling>`

Emitted when the scrollbar is being scrolled.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **custom_step** = `-1.0` `🔗<class_ScrollBar_property_custom_step>`

classref-property-setget

- `void (No return value.)` **set_custom_step**(value: `float<class_float>`)
- `float<class_float>` **get_custom_step**()

Overrides the step used when clicking increment and decrement buttons or when using arrow keys when the **ScrollBar** is focused.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Texture2D<class_Texture2D>` **decrement** `🔗<class_ScrollBar_theme_icon_decrement>`

Icon used as a button to scroll the **ScrollBar** left/up. Supports custom step using the `custom_step<class_ScrollBar_property_custom_step>` property.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **decrement_highlight** `🔗<class_ScrollBar_theme_icon_decrement_highlight>`

Displayed when the mouse cursor hovers over the decrement button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **decrement_pressed** `🔗<class_ScrollBar_theme_icon_decrement_pressed>`

Displayed when the decrement button is being pressed.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **increment** `🔗<class_ScrollBar_theme_icon_increment>`

Icon used as a button to scroll the **ScrollBar** right/down. Supports custom step using the `custom_step<class_ScrollBar_property_custom_step>` property.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **increment_highlight** `🔗<class_ScrollBar_theme_icon_increment_highlight>`

Displayed when the mouse cursor hovers over the increment button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **increment_pressed** `🔗<class_ScrollBar_theme_icon_increment_pressed>`

Displayed when the increment button is being pressed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **grabber** `🔗<class_ScrollBar_theme_style_grabber>`

Used as texture for the grabber, the draggable element representing current scroll.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **grabber_highlight** `🔗<class_ScrollBar_theme_style_grabber_highlight>`

Used when the mouse hovers over the grabber.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **grabber_pressed** `🔗<class_ScrollBar_theme_style_grabber_pressed>`

Used when the grabber is being dragged.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **scroll** `🔗<class_ScrollBar_theme_style_scroll>`

Used as background of this **ScrollBar**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **scroll_focus** `🔗<class_ScrollBar_theme_style_scroll_focus>`

Used as background when the **ScrollBar** has the GUI focus.