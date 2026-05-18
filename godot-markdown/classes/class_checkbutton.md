github_url
hide

# CheckButton

**Inherits:** `Button<class_Button>` **\<** `BaseButton<class_BaseButton>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A button that represents a binary choice.

classref-introduction-group

## Description

**CheckButton** is a toggle button displayed as a check field. It's similar to `CheckBox<class_CheckBox>` in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckButton** when toggling it has an **immediate** effect on something. For example, it can be used when pressing it shows or hides advanced settings, without asking the user to confirm this action.

See also `BaseButton<class_BaseButton>` which contains common properties and methods associated with this node.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **button_checked_color** = `Color(1, 1, 1, 1)` `🔗<class_CheckButton_theme_color_button_checked_color>`

The color of the checked icon when the checkbox is pressed.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **button_unchecked_color** = `Color(1, 1, 1, 1)` `🔗<class_CheckButton_theme_color_button_unchecked_color>`

The color of the unchecked icon when the checkbox is not pressed.

classref-item-separator

classref-themeproperty

`int<class_int>` **check_v_offset** = `0` `🔗<class_CheckButton_theme_constant_check_v_offset>`

The vertical offset used when rendering the toggle icons (in pixels).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **checked** `🔗<class_CheckButton_theme_icon_checked>`

The icon to display when the **CheckButton** is checked (for left-to-right layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **checked_disabled** `🔗<class_CheckButton_theme_icon_checked_disabled>`

The icon to display when the **CheckButton** is checked and disabled (for left-to-right layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **checked_disabled_mirrored** `🔗<class_CheckButton_theme_icon_checked_disabled_mirrored>`

The icon to display when the **CheckButton** is checked and disabled (for right-to-left layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **checked_mirrored** `🔗<class_CheckButton_theme_icon_checked_mirrored>`

The icon to display when the **CheckButton** is checked (for right-to-left layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **unchecked** `🔗<class_CheckButton_theme_icon_unchecked>`

The icon to display when the **CheckButton** is unchecked (for left-to-right layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **unchecked_disabled** `🔗<class_CheckButton_theme_icon_unchecked_disabled>`

The icon to display when the **CheckButton** is unchecked and disabled (for left-to-right layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **unchecked_disabled_mirrored** `🔗<class_CheckButton_theme_icon_unchecked_disabled_mirrored>`

The icon to display when the **CheckButton** is unchecked and disabled (for right-to-left layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **unchecked_mirrored** `🔗<class_CheckButton_theme_icon_unchecked_mirrored>`

The icon to display when the **CheckButton** is unchecked (for right-to-left layouts).