github_url
hide

# StatusIndicator

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

Application status indicator (aka notification area icon).

**Note:** Status indicator is implemented on macOS and Windows.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**pressed**(mouse_button: `int<class_int>`, mouse_position: `Vector2i<class_Vector2i>`) `🔗<class_StatusIndicator_signal_pressed>`

Emitted when the status indicator is pressed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Texture2D<class_Texture2D>` **icon** `🔗<class_StatusIndicator_property_icon>`

classref-property-setget

- `void (No return value.)` **set_icon**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_icon**()

Status indicator icon.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **menu** = `NodePath("")` `🔗<class_StatusIndicator_property_menu>`

classref-property-setget

- `void (No return value.)` **set_menu**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_menu**()

Status indicator native popup menu. If this is set, the `pressed<class_StatusIndicator_signal_pressed>` signal is not emitted.

**Note:** Native popup is only supported if `NativeMenu<class_NativeMenu>` supports `NativeMenu.FEATURE_POPUP_MENU<class_NativeMenu_constant_FEATURE_POPUP_MENU>` feature.

classref-item-separator

classref-property

`String<class_String>` **tooltip** = `""` `🔗<class_StatusIndicator_property_tooltip>`

classref-property-setget

- `void (No return value.)` **set_tooltip**(value: `String<class_String>`)
- `String<class_String>` **get_tooltip**()

Status indicator tooltip.

classref-item-separator

classref-property

`bool<class_bool>` **visible** = `true` `🔗<class_StatusIndicator_property_visible>`

classref-property-setget

- `void (No return value.)` **set_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_visible**()

If `true`, the status indicator is visible.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Rect2<class_Rect2>` **get_rect**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StatusIndicator_method_get_rect>`

Returns the status indicator rectangle in screen coordinates. If this status indicator is not visible, returns an empty `Rect2<class_Rect2>`.