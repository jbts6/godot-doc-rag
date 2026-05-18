github_url
hide

# TextureProgressBar

**Inherits:** `Range<class_Range>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Texture-based progress bar. Useful for loading screens and life or stamina bars.

classref-introduction-group

## Description

TextureProgressBar works like `ProgressBar<class_ProgressBar>`, but uses up to 3 textures instead of Godot's `Theme<class_Theme>` resource. It can be used to create horizontal, vertical and radial progress bars.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FillMode**: `🔗<enum_TextureProgressBar_FillMode>`

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_LEFT_TO_RIGHT** = `0`

The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills from left to right.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_RIGHT_TO_LEFT** = `1`

The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills from right to left.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_TOP_TO_BOTTOM** = `2`

The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills from top to bottom.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_BOTTOM_TO_TOP** = `3`

The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills from bottom to top.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_CLOCKWISE** = `4`

Turns the node into a radial bar. The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills clockwise. See `radial_center_offset<class_TextureProgressBar_property_radial_center_offset>`, `radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>` and `radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>` to control the way the bar fills up.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_COUNTER_CLOCKWISE** = `5`

Turns the node into a radial bar. The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills counterclockwise. See `radial_center_offset<class_TextureProgressBar_property_radial_center_offset>`, `radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>` and `radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>` to control the way the bar fills up.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_BILINEAR_LEFT_AND_RIGHT** = `6`

The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills from the center, expanding both towards the left and the right.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_BILINEAR_TOP_AND_BOTTOM** = `7`

The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills from the center, expanding both towards the top and the bottom.

classref-enumeration-constant

`FillMode<enum_TextureProgressBar_FillMode>` **FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE** = `8`

Turns the node into a radial bar. The `texture_progress<class_TextureProgressBar_property_texture_progress>` fills radially from the center, expanding both clockwise and counterclockwise. See `radial_center_offset<class_TextureProgressBar_property_radial_center_offset>`, `radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>` and `radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>` to control the way the bar fills up.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **fill_mode** = `0` `🔗<class_TextureProgressBar_property_fill_mode>`

classref-property-setget

- `void (No return value.)` **set_fill_mode**(value: `int<class_int>`)
- `int<class_int>` **get_fill_mode**()

The fill direction. See `FillMode<enum_TextureProgressBar_FillMode>` for possible values.

classref-item-separator

classref-property

`bool<class_bool>` **nine_patch_stretch** = `false` `🔗<class_TextureProgressBar_property_nine_patch_stretch>`

classref-property-setget

- `void (No return value.)` **set_nine_patch_stretch**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_nine_patch_stretch**()

If `true`, Godot treats the bar's textures like in `NinePatchRect<class_NinePatchRect>`. Use the `stretch_margin_*` properties like `stretch_margin_bottom<class_TextureProgressBar_property_stretch_margin_bottom>` to set up the nine patch's 3×3 grid. When using a radial `fill_mode<class_TextureProgressBar_property_fill_mode>`, this setting will only enable stretching for `texture_progress<class_TextureProgressBar_property_texture_progress>`, while `texture_under<class_TextureProgressBar_property_texture_under>` and `texture_over<class_TextureProgressBar_property_texture_over>` will be treated like in `NinePatchRect<class_NinePatchRect>`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **radial_center_offset** = `Vector2(0, 0)` `🔗<class_TextureProgressBar_property_radial_center_offset>`

classref-property-setget

- `void (No return value.)` **set_radial_center_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_radial_center_offset**()

Offsets `texture_progress<class_TextureProgressBar_property_texture_progress>` if `fill_mode<class_TextureProgressBar_property_fill_mode>` is `FILL_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE>`, `FILL_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE>`, or `FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE>`.

**Note:** The effective radial center always stays within the `texture_progress<class_TextureProgressBar_property_texture_progress>` bounds. If you need to move it outside the texture's bounds, modify the `texture_progress<class_TextureProgressBar_property_texture_progress>` to contain additional empty space where needed.

classref-item-separator

classref-property

`float<class_float>` **radial_fill_degrees** = `360.0` `🔗<class_TextureProgressBar_property_radial_fill_degrees>`

classref-property-setget

- `void (No return value.)` **set_fill_degrees**(value: `float<class_float>`)
- `float<class_float>` **get_fill_degrees**()

Upper limit for the fill of `texture_progress<class_TextureProgressBar_property_texture_progress>` if `fill_mode<class_TextureProgressBar_property_fill_mode>` is `FILL_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE>`, `FILL_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE>`, or `FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE>`. When the node's `value` is equal to its `max_value`, the texture fills up to this angle.

See `Range.value<class_Range_property_value>`, `Range.max_value<class_Range_property_max_value>`.

classref-item-separator

classref-property

`float<class_float>` **radial_initial_angle** = `0.0` `🔗<class_TextureProgressBar_property_radial_initial_angle>`

classref-property-setget

- `void (No return value.)` **set_radial_initial_angle**(value: `float<class_float>`)
- `float<class_float>` **get_radial_initial_angle**()

Starting angle for the fill of `texture_progress<class_TextureProgressBar_property_texture_progress>` if `fill_mode<class_TextureProgressBar_property_fill_mode>` is `FILL_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE>`, `FILL_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_COUNTER_CLOCKWISE>`, or `FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE<class_TextureProgressBar_constant_FILL_CLOCKWISE_AND_COUNTER_CLOCKWISE>`. When the node's `value` is equal to its `min_value`, the texture doesn't show up at all. When the `value` increases, the texture fills and tends towards `radial_fill_degrees<class_TextureProgressBar_property_radial_fill_degrees>`.

**Note:** `radial_initial_angle<class_TextureProgressBar_property_radial_initial_angle>` is wrapped between `0` and `360` degrees (inclusive).

classref-item-separator

classref-property

`int<class_int>` **stretch_margin_bottom** = `0` `🔗<class_TextureProgressBar_property_stretch_margin_bottom>`

classref-property-setget

- `void (No return value.)` **set_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`, value: `int<class_int>`)
- `int<class_int>` **get_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The height of the 9-patch's bottom row. A margin of 16 means the 9-slice's bottom corners and side will have a height of 16 pixels. You can set all 4 margin values individually to create panels with non-uniform borders. Only effective if `nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>` is `true`.

classref-item-separator

classref-property

`int<class_int>` **stretch_margin_left** = `0` `🔗<class_TextureProgressBar_property_stretch_margin_left>`

classref-property-setget

- `void (No return value.)` **set_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`, value: `int<class_int>`)
- `int<class_int>` **get_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The width of the 9-patch's left column. Only effective if `nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>` is `true`.

classref-item-separator

classref-property

`int<class_int>` **stretch_margin_right** = `0` `🔗<class_TextureProgressBar_property_stretch_margin_right>`

classref-property-setget

- `void (No return value.)` **set_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`, value: `int<class_int>`)
- `int<class_int>` **get_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The width of the 9-patch's right column. Only effective if `nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>` is `true`.

classref-item-separator

classref-property

`int<class_int>` **stretch_margin_top** = `0` `🔗<class_TextureProgressBar_property_stretch_margin_top>`

classref-property-setget

- `void (No return value.)` **set_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`, value: `int<class_int>`)
- `int<class_int>` **get_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The height of the 9-patch's top row. Only effective if `nine_patch_stretch<class_TextureProgressBar_property_nine_patch_stretch>` is `true`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture_over** `🔗<class_TextureProgressBar_property_texture_over>`

classref-property-setget

- `void (No return value.)` **set_over_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_over_texture**()

`Texture2D<class_Texture2D>` that draws over the progress bar. Use it to add highlights or an upper-frame that hides part of `texture_progress<class_TextureProgressBar_property_texture_progress>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture_progress** `🔗<class_TextureProgressBar_property_texture_progress>`

classref-property-setget

- `void (No return value.)` **set_progress_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_progress_texture**()

`Texture2D<class_Texture2D>` that clips based on the node's `value` and `fill_mode<class_TextureProgressBar_property_fill_mode>`. As `value` increased, the texture fills up. It shows entirely when `value` reaches `max_value`. It doesn't show at all if `value` is equal to `min_value`.

The `value` property comes from `Range<class_Range>`. See `Range.value<class_Range_property_value>`, `Range.min_value<class_Range_property_min_value>`, `Range.max_value<class_Range_property_max_value>`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **texture_progress_offset** = `Vector2(0, 0)` `🔗<class_TextureProgressBar_property_texture_progress_offset>`

classref-property-setget

- `void (No return value.)` **set_texture_progress_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_texture_progress_offset**()

The offset of `texture_progress<class_TextureProgressBar_property_texture_progress>`. Useful for `texture_over<class_TextureProgressBar_property_texture_over>` and `texture_under<class_TextureProgressBar_property_texture_under>` with fancy borders, to avoid transparent margins in your progress texture.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture_under** `🔗<class_TextureProgressBar_property_texture_under>`

classref-property-setget

- `void (No return value.)` **set_under_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_under_texture**()

`Texture2D<class_Texture2D>` that draws under the progress bar. The bar's background.

classref-item-separator

classref-property

`Color<class_Color>` **tint_over** = `Color(1, 1, 1, 1)` `🔗<class_TextureProgressBar_property_tint_over>`

classref-property-setget

- `void (No return value.)` **set_tint_over**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_tint_over**()

Multiplies the color of the bar's `texture_over<class_TextureProgressBar_property_texture_over>` texture. The effect is similar to `CanvasItem.modulate<class_CanvasItem_property_modulate>`, except it only affects this specific texture instead of the entire node.

classref-item-separator

classref-property

`Color<class_Color>` **tint_progress** = `Color(1, 1, 1, 1)` `🔗<class_TextureProgressBar_property_tint_progress>`

classref-property-setget

- `void (No return value.)` **set_tint_progress**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_tint_progress**()

Multiplies the color of the bar's `texture_progress<class_TextureProgressBar_property_texture_progress>` texture.

classref-item-separator

classref-property

`Color<class_Color>` **tint_under** = `Color(1, 1, 1, 1)` `🔗<class_TextureProgressBar_property_tint_under>`

classref-property-setget

- `void (No return value.)` **set_tint_under**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_tint_under**()

Multiplies the color of the bar's `texture_under<class_TextureProgressBar_property_texture_under>` texture.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TextureProgressBar_method_get_stretch_margin>`

Returns the stretch margin with the specified index. See `stretch_margin_bottom<class_TextureProgressBar_property_stretch_margin_bottom>` and related properties.

classref-item-separator

classref-method

`void (No return value.)` **set_stretch_margin**(margin: `Side<enum_@GlobalScope_Side>`, value: `int<class_int>`) `🔗<class_TextureProgressBar_method_set_stretch_margin>`

Sets the stretch margin with the specified index. See `stretch_margin_bottom<class_TextureProgressBar_property_stretch_margin_bottom>` and related properties.