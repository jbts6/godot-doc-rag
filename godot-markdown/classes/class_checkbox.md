github_url
hide

# CheckBox

**Inherits:** `Button<class_Button>` **\<** `BaseButton<class_BaseButton>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A button that represents a binary choice.

classref-introduction-group

## Description

**CheckBox** allows the user to choose one of only two possible options. It's similar to `CheckButton<class_CheckButton>` in functionality, but it has a different appearance. To follow established UX patterns, it's recommended to use **CheckBox** when toggling it has **no** immediate effect on something. For example, it could be used when toggling it will only do something once a confirmation button is pressed.

See also `BaseButton<class_BaseButton>` which contains common properties and methods associated with this node.

When `BaseButton.button_group<class_BaseButton_property_button_group>` specifies a `ButtonGroup<class_ButtonGroup>`, **CheckBox** changes its appearance to that of a radio button and uses the various `radio_*` theme properties.

classref-reftable-group

## Properties

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **checkbox_checked_color** = `Color(1, 1, 1, 1)` `🔗<class_CheckBox_theme_color_checkbox_checked_color>`

The color of the checked icon when the checkbox is pressed.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **checkbox_unchecked_color** = `Color(1, 1, 1, 1)` `🔗<class_CheckBox_theme_color_checkbox_unchecked_color>`

The color of the unchecked icon when the checkbox is not pressed.

classref-item-separator

classref-themeproperty

`int<class_int>` **check_v_offset** = `0` `🔗<class_CheckBox_theme_constant_check_v_offset>`

The vertical offset used when rendering the check icons (in pixels).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **checked** `🔗<class_CheckBox_theme_icon_checked>`

The check icon to display when the **CheckBox** is checked.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **checked_disabled** `🔗<class_CheckBox_theme_icon_checked_disabled>`

The check icon to display when the **CheckBox** is checked and is disabled.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **radio_checked** `🔗<class_CheckBox_theme_icon_radio_checked>`

The check icon to display when the **CheckBox** is configured as a radio button and is checked.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **radio_checked_disabled** `🔗<class_CheckBox_theme_icon_radio_checked_disabled>`

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **radio_unchecked** `🔗<class_CheckBox_theme_icon_radio_unchecked>`

The check icon to display when the **CheckBox** is configured as a radio button and is unchecked.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **radio_unchecked_disabled** `🔗<class_CheckBox_theme_icon_radio_unchecked_disabled>`

The check icon to display when the **CheckBox** is configured as a radio button, is disabled, and is unchecked.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **unchecked** `🔗<class_CheckBox_theme_icon_unchecked>`

The check icon to display when the **CheckBox** is unchecked.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **unchecked_disabled** `🔗<class_CheckBox_theme_icon_unchecked_disabled>`

The check icon to display when the **CheckBox** is unchecked and is disabled.