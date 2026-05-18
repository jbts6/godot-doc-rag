github_url
hide

# StyleBoxTexture

**Inherits:** `StyleBox<class_StyleBox>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A texture-based nine-patch `StyleBox<class_StyleBox>`.

classref-introduction-group

## Description

A texture-based nine-patch `StyleBox<class_StyleBox>`, in a way similar to `NinePatchRect<class_NinePatchRect>`. This stylebox performs a 3×3 scaling of a texture, where only the center cell is fully stretched. This makes it possible to design bordered styles regardless of the stylebox's size.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **AxisStretchMode**: `🔗<enum_StyleBoxTexture_AxisStretchMode>`

classref-enumeration-constant

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **AXIS_STRETCH_MODE_STRETCH** = `0`

Stretch the stylebox's texture. This results in visible distortion unless the texture size matches the stylebox's size perfectly.

classref-enumeration-constant

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **AXIS_STRETCH_MODE_TILE** = `1`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system.

classref-enumeration-constant

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **AXIS_STRETCH_MODE_TILE_FIT** = `2`

Repeats the stylebox's texture to match the stylebox's size according to the nine-patch system. Unlike `AXIS_STRETCH_MODE_TILE<class_StyleBoxTexture_constant_AXIS_STRETCH_MODE_TILE>`, the texture may be slightly stretched to make the nine-patch texture tile seamlessly.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **axis_stretch_horizontal** = `0` `🔗<class_StyleBoxTexture_property_axis_stretch_horizontal>`

classref-property-setget

- `void (No return value.)` **set_h_axis_stretch_mode**(value: `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`)
- `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **get_h_axis_stretch_mode**()

Controls how the stylebox's texture will be stretched or tiled horizontally.

classref-item-separator

classref-property

`AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **axis_stretch_vertical** = `0` `🔗<class_StyleBoxTexture_property_axis_stretch_vertical>`

classref-property-setget

- `void (No return value.)` **set_v_axis_stretch_mode**(value: `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>`)
- `AxisStretchMode<enum_StyleBoxTexture_AxisStretchMode>` **get_v_axis_stretch_mode**()

Controls how the stylebox's texture will be stretched or tiled vertically.

classref-item-separator

classref-property

`bool<class_bool>` **draw_center** = `true` `🔗<class_StyleBoxTexture_property_draw_center>`

classref-property-setget

- `void (No return value.)` **set_draw_center**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_draw_center_enabled**()

If `true`, the nine-patch texture's center tile will be drawn.

classref-item-separator

classref-property

`float<class_float>` **expand_margin_bottom** = `0.0` `🔗<class_StyleBoxTexture_property_expand_margin_bottom>`

classref-property-setget

- `void (No return value.)` **set_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Expands the bottom margin of this style box when drawing, causing it to be drawn larger than requested.

classref-item-separator

classref-property

`float<class_float>` **expand_margin_left** = `0.0` `🔗<class_StyleBoxTexture_property_expand_margin_left>`

classref-property-setget

- `void (No return value.)` **set_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Expands the left margin of this style box when drawing, causing it to be drawn larger than requested.

classref-item-separator

classref-property

`float<class_float>` **expand_margin_right** = `0.0` `🔗<class_StyleBoxTexture_property_expand_margin_right>`

classref-property-setget

- `void (No return value.)` **set_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Expands the right margin of this style box when drawing, causing it to be drawn larger than requested.

classref-item-separator

classref-property

`float<class_float>` **expand_margin_top** = `0.0` `🔗<class_StyleBoxTexture_property_expand_margin_top>`

classref-property-setget

- `void (No return value.)` **set_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Expands the top margin of this style box when drawing, causing it to be drawn larger than requested.

classref-item-separator

classref-property

`Color<class_Color>` **modulate_color** = `Color(1, 1, 1, 1)` `🔗<class_StyleBoxTexture_property_modulate_color>`

classref-property-setget

- `void (No return value.)` **set_modulate**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_modulate**()

Modulates the color of the texture when this style box is drawn.

classref-item-separator

classref-property

`Rect2<class_Rect2>` **region_rect** = `Rect2(0, 0, 0, 0)` `🔗<class_StyleBoxTexture_property_region_rect>`

classref-property-setget

- `void (No return value.)` **set_region_rect**(value: `Rect2<class_Rect2>`)
- `Rect2<class_Rect2>` **get_region_rect**()

The region to use from the `texture<class_StyleBoxTexture_property_texture>`.

This is equivalent to first wrapping the `texture<class_StyleBoxTexture_property_texture>` in an `AtlasTexture<class_AtlasTexture>` with the same region.

If empty (`Rect2(0, 0, 0, 0)`), the whole `texture<class_StyleBoxTexture_property_texture>` is used.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_StyleBoxTexture_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

The texture to use when drawing this style box.

classref-item-separator

classref-property

`float<class_float>` **texture_margin_bottom** = `0.0` `🔗<class_StyleBoxTexture_property_texture_margin_bottom>`

classref-property-setget

- `void (No return value.)` **set_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Increases the bottom margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the bottom border of the 3×3 box.

This is also the value used as fallback for `StyleBox.content_margin_bottom<class_StyleBox_property_content_margin_bottom>` if it is negative.

classref-item-separator

classref-property

`float<class_float>` **texture_margin_left** = `0.0` `🔗<class_StyleBoxTexture_property_texture_margin_left>`

classref-property-setget

- `void (No return value.)` **set_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Increases the left margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the left border of the 3×3 box.

This is also the value used as fallback for `StyleBox.content_margin_left<class_StyleBox_property_content_margin_left>` if it is negative.

classref-item-separator

classref-property

`float<class_float>` **texture_margin_right** = `0.0` `🔗<class_StyleBoxTexture_property_texture_margin_right>`

classref-property-setget

- `void (No return value.)` **set_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Increases the right margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the right border of the 3×3 box.

This is also the value used as fallback for `StyleBox.content_margin_right<class_StyleBox_property_content_margin_right>` if it is negative.

classref-item-separator

classref-property

`float<class_float>` **texture_margin_top** = `0.0` `🔗<class_StyleBoxTexture_property_texture_margin_top>`

classref-property-setget

- `void (No return value.)` **set_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`)
- `float<class_float>` **get_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Increases the top margin of the 3×3 texture box.

A higher value means more of the source texture is considered to be part of the top border of the 3×3 box.

This is also the value used as fallback for `StyleBox.content_margin_top<class_StyleBox_property_content_margin_top>` if it is negative.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StyleBoxTexture_method_get_expand_margin>`

Returns the expand margin size of the specified `Side<enum_@GlobalScope_Side>`.

classref-item-separator

classref-method

`float<class_float>` **get_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StyleBoxTexture_method_get_texture_margin>`

Returns the margin size of the specified `Side<enum_@GlobalScope_Side>`.

classref-item-separator

classref-method

`void (No return value.)` **set_expand_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`) `🔗<class_StyleBoxTexture_method_set_expand_margin>`

Sets the expand margin to `size` pixels for the specified `Side<enum_@GlobalScope_Side>`.

classref-item-separator

classref-method

`void (No return value.)` **set_expand_margin_all**(size: `float<class_float>`) `🔗<class_StyleBoxTexture_method_set_expand_margin_all>`

Sets the expand margin to `size` pixels for all sides.

classref-item-separator

classref-method

`void (No return value.)` **set_texture_margin**(margin: `Side<enum_@GlobalScope_Side>`, size: `float<class_float>`) `🔗<class_StyleBoxTexture_method_set_texture_margin>`

Sets the margin to `size` pixels for the specified `Side<enum_@GlobalScope_Side>`.

classref-item-separator

classref-method

`void (No return value.)` **set_texture_margin_all**(size: `float<class_float>`) `🔗<class_StyleBoxTexture_method_set_texture_margin_all>`

Sets the margin to `size` pixels for all sides.