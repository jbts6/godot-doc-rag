github_url
hide

# TouchScreenButton

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Button for touch screen devices for gameplay use.

classref-introduction-group

## Description

TouchScreenButton allows you to create on-screen buttons for touch devices. It's intended for gameplay use, such as a unit you have to touch to move. Unlike `Button<class_Button>`, TouchScreenButton supports multitouch out of the box. Several TouchScreenButtons can be pressed at the same time with touch input.

This node inherits from `Node2D<class_Node2D>`. Unlike with `Control<class_Control>` nodes, you cannot set anchors on it. If you want to create menus or user interfaces, you may want to use `Button<class_Button>` nodes instead. To make button nodes react to touch events, you can enable `ProjectSettings.input_devices/pointing/emulate_mouse_from_touch<class_ProjectSettings_property_input_devices/pointing/emulate_mouse_from_touch>` in the Project Settings.

You can configure TouchScreenButton to be visible only on touch devices, helping you develop your game both for desktop and mobile devices.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**pressed**() `🔗<class_TouchScreenButton_signal_pressed>`

Emitted when the button is pressed (down).

classref-item-separator

classref-signal

**released**() `🔗<class_TouchScreenButton_signal_released>`

Emitted when the button is released (up).

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **VisibilityMode**: `🔗<enum_TouchScreenButton_VisibilityMode>`

classref-enumeration-constant

`VisibilityMode<enum_TouchScreenButton_VisibilityMode>` **VISIBILITY_ALWAYS** = `0`

Always visible.

classref-enumeration-constant

`VisibilityMode<enum_TouchScreenButton_VisibilityMode>` **VISIBILITY_TOUCHSCREEN_ONLY** = `1`

Visible on touch screens only.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **action** = `""` `🔗<class_TouchScreenButton_property_action>`

classref-property-setget

- `void (No return value.)` **set_action**(value: `String<class_String>`)
- `String<class_String>` **get_action**()

The button's action. Actions can be handled with `InputEventAction<class_InputEventAction>`.

classref-item-separator

classref-property

`BitMap<class_BitMap>` **bitmask** `🔗<class_TouchScreenButton_property_bitmask>`

classref-property-setget

- `void (No return value.)` **set_bitmask**(value: `BitMap<class_BitMap>`)
- `BitMap<class_BitMap>` **get_bitmask**()

The button's bitmask.

classref-item-separator

classref-property

`bool<class_bool>` **passby_press** = `false` `🔗<class_TouchScreenButton_property_passby_press>`

classref-property-setget

- `void (No return value.)` **set_passby_press**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_passby_press_enabled**()

If `true`, the `pressed<class_TouchScreenButton_signal_pressed>` and `released<class_TouchScreenButton_signal_released>` signals are emitted whenever a pressed finger goes in and out of the button, even if the pressure started outside the active area of the button.

**Note:** This is a "pass-by" (not "bypass") press mode.

classref-item-separator

classref-property

`Shape2D<class_Shape2D>` **shape** `🔗<class_TouchScreenButton_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Shape2D<class_Shape2D>`)
- `Shape2D<class_Shape2D>` **get_shape**()

The button's shape.

classref-item-separator

classref-property

`bool<class_bool>` **shape_centered** = `true` `🔗<class_TouchScreenButton_property_shape_centered>`

classref-property-setget

- `void (No return value.)` **set_shape_centered**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_shape_centered**()

If `true`, the button's shape is centered in the provided texture. If no texture is used, this property has no effect.

classref-item-separator

classref-property

`bool<class_bool>` **shape_visible** = `true` `🔗<class_TouchScreenButton_property_shape_visible>`

classref-property-setget

- `void (No return value.)` **set_shape_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_shape_visible**()

If `true`, the button's shape is visible in the editor.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture_normal** `🔗<class_TouchScreenButton_property_texture_normal>`

classref-property-setget

- `void (No return value.)` **set_texture_normal**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture_normal**()

The button's texture for the normal state.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture_pressed** `🔗<class_TouchScreenButton_property_texture_pressed>`

classref-property-setget

- `void (No return value.)` **set_texture_pressed**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture_pressed**()

The button's texture for the pressed state.

classref-item-separator

classref-property

`VisibilityMode<enum_TouchScreenButton_VisibilityMode>` **visibility_mode** = `0` `🔗<class_TouchScreenButton_property_visibility_mode>`

classref-property-setget

- `void (No return value.)` **set_visibility_mode**(value: `VisibilityMode<enum_TouchScreenButton_VisibilityMode>`)
- `VisibilityMode<enum_TouchScreenButton_VisibilityMode>` **get_visibility_mode**()

The button's visibility mode.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_pressed**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TouchScreenButton_method_is_pressed>`

Returns `true` if this button is currently pressed.