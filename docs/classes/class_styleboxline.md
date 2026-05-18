github_url
hide

# StyleBoxLine

**Inherits:** `StyleBox<class_StyleBox>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `StyleBox<class_StyleBox>` that displays a single line of a given color and thickness.

classref-introduction-group

## Description

A `StyleBox<class_StyleBox>` that displays a single line of a given color and thickness. The line can be either horizontal or vertical. Useful for separators.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **color** = `Color(0, 0, 0, 1)` `🔗<class_StyleBoxLine_property_color>`

classref-property-setget

- `void (No return value.)` **set_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_color**()

The line's color.

classref-item-separator

classref-property

`float<class_float>` **grow_begin** = `1.0` `🔗<class_StyleBoxLine_property_grow_begin>`

classref-property-setget

- `void (No return value.)` **set_grow_begin**(value: `float<class_float>`)
- `float<class_float>` **get_grow_begin**()

The number of pixels the line will extend before the **StyleBoxLine**'s bounds. If set to a negative value, the line will begin inside the **StyleBoxLine**'s bounds.

classref-item-separator

classref-property

`float<class_float>` **grow_end** = `1.0` `🔗<class_StyleBoxLine_property_grow_end>`

classref-property-setget

- `void (No return value.)` **set_grow_end**(value: `float<class_float>`)
- `float<class_float>` **get_grow_end**()

The number of pixels the line will extend past the **StyleBoxLine**'s bounds. If set to a negative value, the line will end inside the **StyleBoxLine**'s bounds.

classref-item-separator

classref-property

`int<class_int>` **thickness** = `1` `🔗<class_StyleBoxLine_property_thickness>`

classref-property-setget

- `void (No return value.)` **set_thickness**(value: `int<class_int>`)
- `int<class_int>` **get_thickness**()

The line's thickness in pixels.

classref-item-separator

classref-property

`bool<class_bool>` **vertical** = `false` `🔗<class_StyleBoxLine_property_vertical>`

classref-property-setget

- `void (No return value.)` **set_vertical**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_vertical**()

If `true`, the line will be vertical. If `false`, the line will be horizontal.