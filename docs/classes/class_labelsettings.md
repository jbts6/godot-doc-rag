github_url
hide

# LabelSettings

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Provides common settings to customize the text in a `Label<class_Label>`.

classref-introduction-group

## Description

**LabelSettings** is a resource that provides common settings to customize the text in a `Label<class_Label>`. It will take priority over the properties defined in `Control.theme<class_Control_property_theme>`. The resource can be shared between multiple labels and changed on the fly, so it's convenient and flexible way to setup text style.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Font<class_Font>` **font** `🔗<class_LabelSettings_property_font>`

classref-property-setget

- `void (No return value.)` **set_font**(value: `Font<class_Font>`)
- `Font<class_Font>` **get_font**()

`Font<class_Font>` used for the text.

classref-item-separator

classref-property

`Color<class_Color>` **font_color** = `Color(1, 1, 1, 1)` `🔗<class_LabelSettings_property_font_color>`

classref-property-setget

- `void (No return value.)` **set_font_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_font_color**()

Color of the text.

classref-item-separator

classref-property

`int<class_int>` **font_size** = `16` `🔗<class_LabelSettings_property_font_size>`

classref-property-setget

- `void (No return value.)` **set_font_size**(value: `int<class_int>`)
- `int<class_int>` **get_font_size**()

Size of the text.

classref-item-separator

classref-property

`float<class_float>` **line_spacing** = `3.0` `🔗<class_LabelSettings_property_line_spacing>`

classref-property-setget

- `void (No return value.)` **set_line_spacing**(value: `float<class_float>`)
- `float<class_float>` **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

classref-item-separator

classref-property

`Color<class_Color>` **outline_color** = `Color(1, 1, 1, 1)` `🔗<class_LabelSettings_property_outline_color>`

classref-property-setget

- `void (No return value.)` **set_outline_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_outline_color**()

The color of the outline.

classref-item-separator

classref-property

`int<class_int>` **outline_size** = `0` `🔗<class_LabelSettings_property_outline_size>`

classref-property-setget

- `void (No return value.)` **set_outline_size**(value: `int<class_int>`)
- `int<class_int>` **get_outline_size**()

Text outline size.

classref-item-separator

classref-property

`float<class_float>` **paragraph_spacing** = `0.0` `🔗<class_LabelSettings_property_paragraph_spacing>`

classref-property-setget

- `void (No return value.)` **set_paragraph_spacing**(value: `float<class_float>`)
- `float<class_float>` **get_paragraph_spacing**()

Vertical space between paragraphs. Added on top of `line_spacing<class_LabelSettings_property_line_spacing>`.

classref-item-separator

classref-property

`Color<class_Color>` **shadow_color** = `Color(0, 0, 0, 0)` `🔗<class_LabelSettings_property_shadow_color>`

classref-property-setget

- `void (No return value.)` **set_shadow_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_shadow_color**()

Color of the shadow effect. If alpha is `0`, no shadow will be drawn.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **shadow_offset** = `Vector2(1, 1)` `🔗<class_LabelSettings_property_shadow_offset>`

classref-property-setget

- `void (No return value.)` **set_shadow_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_shadow_offset**()

Offset of the shadow effect, in pixels.

classref-item-separator

classref-property

`int<class_int>` **shadow_size** = `1` `🔗<class_LabelSettings_property_shadow_size>`

classref-property-setget

- `void (No return value.)` **set_shadow_size**(value: `int<class_int>`)
- `int<class_int>` **get_shadow_size**()

Size of the shadow effect.

classref-item-separator

classref-property

`int<class_int>` **stacked_outline_count** = `0` `🔗<class_LabelSettings_property_stacked_outline_count>`

classref-property-setget

- `void (No return value.)` **set_stacked_outline_count**(value: `int<class_int>`)
- `int<class_int>` **get_stacked_outline_count**()

The number of stacked outlines.

classref-item-separator

classref-property

`Color<class_Color>` **stacked_outline\_{index}/color** = `Color(0, 0, 0, 1)` `🔗<class_LabelSettings_property_stacked_outline_{index}/color>`

The color of the outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_outline_count - 1` range.

classref-item-separator

classref-property

`int<class_int>` **stacked_outline\_{index}/size** = `0` `🔗<class_LabelSettings_property_stacked_outline_{index}/size>`

The size of the outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_outline_count - 1` range.

classref-item-separator

classref-property

`int<class_int>` **stacked_shadow_count** = `0` `🔗<class_LabelSettings_property_stacked_shadow_count>`

classref-property-setget

- `void (No return value.)` **set_stacked_shadow_count**(value: `int<class_int>`)
- `int<class_int>` **get_stacked_shadow_count**()

The number of stacked shadows.

classref-item-separator

classref-property

`Color<class_Color>` **stacked_shadow\_{index}/color** = `Color(0, 0, 0, 1)` `🔗<class_LabelSettings_property_stacked_shadow_{index}/color>`

The color of the shadow at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **stacked_shadow\_{index}/offset** = `Vector2i(1, 1)` `🔗<class_LabelSettings_property_stacked_shadow_{index}/offset>`

The offset of the shadow at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

classref-item-separator

classref-property

`int<class_int>` **stacked_shadow\_{index}/outline_size** = `0` `🔗<class_LabelSettings_property_stacked_shadow_{index}/outline_size>`

The size of the shadow outline at `index`.

**Note:** `index` is a value in the `0 .. stacked_shadow_count - 1` range.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_stacked_outline**(index: `int<class_int>` = -1) `🔗<class_LabelSettings_method_add_stacked_outline>`

Adds a new stacked outline to the label at the given `index`. If `index` is `-1`, the new stacked outline will be added at the end of the list.

classref-item-separator

classref-method

`void (No return value.)` **add_stacked_shadow**(index: `int<class_int>` = -1) `🔗<class_LabelSettings_method_add_stacked_shadow>`

Adds a new stacked shadow to the label at the given `index`. If `index` is `-1`, the new stacked shadow will be added at the end of the list.

classref-item-separator

classref-method

`Color<class_Color>` **get_stacked_outline_color**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LabelSettings_method_get_stacked_outline_color>`

Returns the color of the stacked outline at `index`.

classref-item-separator

classref-method

`int<class_int>` **get_stacked_outline_size**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LabelSettings_method_get_stacked_outline_size>`

Returns the size of the stacked outline at `index`.

classref-item-separator

classref-method

`Color<class_Color>` **get_stacked_shadow_color**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LabelSettings_method_get_stacked_shadow_color>`

Returns the color of the stacked shadow at `index`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_stacked_shadow_offset**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LabelSettings_method_get_stacked_shadow_offset>`

Returns the offset of the stacked shadow at `index`.

classref-item-separator

classref-method

`int<class_int>` **get_stacked_shadow_outline_size**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_LabelSettings_method_get_stacked_shadow_outline_size>`

Returns the outline size of the stacked shadow at `index`.

classref-item-separator

classref-method

`void (No return value.)` **move_stacked_outline**(from_index: `int<class_int>`, to_position: `int<class_int>`) `🔗<class_LabelSettings_method_move_stacked_outline>`

Moves the stacked outline at index `from_index` to the given position `to_position` in the array.

classref-item-separator

classref-method

`void (No return value.)` **move_stacked_shadow**(from_index: `int<class_int>`, to_position: `int<class_int>`) `🔗<class_LabelSettings_method_move_stacked_shadow>`

Moves the stacked shadow at index `from_index` to the given position `to_position` in the array.

classref-item-separator

classref-method

`void (No return value.)` **remove_stacked_outline**(index: `int<class_int>`) `🔗<class_LabelSettings_method_remove_stacked_outline>`

Removes the stacked outline at index `index`.

classref-item-separator

classref-method

`void (No return value.)` **remove_stacked_shadow**(index: `int<class_int>`) `🔗<class_LabelSettings_method_remove_stacked_shadow>`

Removes the stacked shadow at index `index`.

classref-item-separator

classref-method

`void (No return value.)` **set_stacked_outline_color**(index: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_LabelSettings_method_set_stacked_outline_color>`

Sets the color of the stacked outline identified by the given `index` to `color`.

classref-item-separator

classref-method

`void (No return value.)` **set_stacked_outline_size**(index: `int<class_int>`, size: `int<class_int>`) `🔗<class_LabelSettings_method_set_stacked_outline_size>`

Sets the size of the stacked outline identified by the given `index` to `size`.

classref-item-separator

classref-method

`void (No return value.)` **set_stacked_shadow_color**(index: `int<class_int>`, color: `Color<class_Color>`) `🔗<class_LabelSettings_method_set_stacked_shadow_color>`

Sets the color of the stacked shadow identified by the given `index` to `color`.

classref-item-separator

classref-method

`void (No return value.)` **set_stacked_shadow_offset**(index: `int<class_int>`, offset: `Vector2<class_Vector2>`) `🔗<class_LabelSettings_method_set_stacked_shadow_offset>`

Sets the offset of the stacked shadow identified by the given `index` to `offset`.

classref-item-separator

classref-method

`void (No return value.)` **set_stacked_shadow_outline_size**(index: `int<class_int>`, size: `int<class_int>`) `🔗<class_LabelSettings_method_set_stacked_shadow_outline_size>`

Sets the outline size of the stacked shadow identified by the given `index` to `size`.