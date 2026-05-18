github_url
hide

# Line2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A 2D polyline that can optionally be textured.

classref-introduction-group

## Description

This node draws a 2D polyline, i.e. a shape consisting of several points connected by segments. **Line2D** is not a mathematical polyline, i.e. the segments are not infinitely thin. It is intended for rendering and it can be colored and optionally textured.

**Warning:** Certain configurations may be impossible to draw nicely, such as very sharp angles. In these situations, the node uses fallback drawing logic to look decent.

**Note:** **Line2D** is drawn using a 2D mesh.

classref-introduction-group

## Tutorials

- [Matrix Transform Demo](https://godotengine.org/asset-library/asset/2787)
- [2.5D Game Demo](https://godotengine.org/asset-library/asset/2783)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **LineJointMode**: `🔗<enum_Line2D_LineJointMode>`

classref-enumeration-constant

`LineJointMode<enum_Line2D_LineJointMode>` **LINE_JOINT_SHARP** = `0`

Makes the polyline's joints pointy, connecting the sides of the two segments by extending them until they intersect. If the rotation of a joint is too big (based on `sharp_limit<class_Line2D_property_sharp_limit>`), the joint falls back to `LINE_JOINT_BEVEL<class_Line2D_constant_LINE_JOINT_BEVEL>` to prevent very long miters.

classref-enumeration-constant

`LineJointMode<enum_Line2D_LineJointMode>` **LINE_JOINT_BEVEL** = `1`

Makes the polyline's joints bevelled/chamfered, connecting the sides of the two segments with a simple line.

classref-enumeration-constant

`LineJointMode<enum_Line2D_LineJointMode>` **LINE_JOINT_ROUND** = `2`

Makes the polyline's joints rounded, connecting the sides of the two segments with an arc. The detail of this arc depends on `round_precision<class_Line2D_property_round_precision>`.

classref-item-separator

classref-enumeration

enum **LineCapMode**: `🔗<enum_Line2D_LineCapMode>`

classref-enumeration-constant

`LineCapMode<enum_Line2D_LineCapMode>` **LINE_CAP_NONE** = `0`

Draws no line cap.

classref-enumeration-constant

`LineCapMode<enum_Line2D_LineCapMode>` **LINE_CAP_BOX** = `1`

Draws the line cap as a box, slightly extending the first/last segment.

classref-enumeration-constant

`LineCapMode<enum_Line2D_LineCapMode>` **LINE_CAP_ROUND** = `2`

Draws the line cap as a semicircle attached to the first/last segment.

classref-item-separator

classref-enumeration

enum **LineTextureMode**: `🔗<enum_Line2D_LineTextureMode>`

classref-enumeration-constant

`LineTextureMode<enum_Line2D_LineTextureMode>` **LINE_TEXTURE_NONE** = `0`

Takes the left pixels of the texture and renders them over the whole polyline.

classref-enumeration-constant

`LineTextureMode<enum_Line2D_LineTextureMode>` **LINE_TEXTURE_TILE** = `1`

Tiles the texture over the polyline. `CanvasItem.texture_repeat<class_CanvasItem_property_texture_repeat>` of the **Line2D** node must be `CanvasItem.TEXTURE_REPEAT_ENABLED<class_CanvasItem_constant_TEXTURE_REPEAT_ENABLED>` or `CanvasItem.TEXTURE_REPEAT_MIRROR<class_CanvasItem_constant_TEXTURE_REPEAT_MIRROR>` for it to work properly.

classref-enumeration-constant

`LineTextureMode<enum_Line2D_LineTextureMode>` **LINE_TEXTURE_STRETCH** = `2`

Stretches the texture across the polyline. `CanvasItem.texture_repeat<class_CanvasItem_property_texture_repeat>` of the **Line2D** node must be `CanvasItem.TEXTURE_REPEAT_DISABLED<class_CanvasItem_constant_TEXTURE_REPEAT_DISABLED>` for best results.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **antialiased** = `false` `🔗<class_Line2D_property_antialiased>`

classref-property-setget

- `void (No return value.)` **set_antialiased**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_antialiased**()

If `true`, the polyline's border will be anti-aliased.

**Note:** **Line2D** is not accelerated by batching when being anti-aliased.

classref-item-separator

classref-property

`LineCapMode<enum_Line2D_LineCapMode>` **begin_cap_mode** = `0` `🔗<class_Line2D_property_begin_cap_mode>`

classref-property-setget

- `void (No return value.)` **set_begin_cap_mode**(value: `LineCapMode<enum_Line2D_LineCapMode>`)
- `LineCapMode<enum_Line2D_LineCapMode>` **get_begin_cap_mode**()

The style of the beginning of the polyline, if `closed<class_Line2D_property_closed>` is `false`.

classref-item-separator

classref-property

`bool<class_bool>` **closed** = `false` `🔗<class_Line2D_property_closed>`

classref-property-setget

- `void (No return value.)` **set_closed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_closed**()

If `true` and the polyline has more than 2 points, the last point and the first one will be connected by a segment.

**Note:** The shape of the closing segment is not guaranteed to be seamless if a `width_curve<class_Line2D_property_width_curve>` is provided.

**Note:** The joint between the closing segment and the first segment is drawn first and it samples the `gradient<class_Line2D_property_gradient>` and the `width_curve<class_Line2D_property_width_curve>` at the beginning. This is an implementation detail that might change in a future version.

classref-item-separator

classref-property

`Color<class_Color>` **default_color** = `Color(1, 1, 1, 1)` `🔗<class_Line2D_property_default_color>`

classref-property-setget

- `void (No return value.)` **set_default_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_default_color**()

The color of the polyline. Will not be used if a gradient is set.

classref-item-separator

classref-property

`LineCapMode<enum_Line2D_LineCapMode>` **end_cap_mode** = `0` `🔗<class_Line2D_property_end_cap_mode>`

classref-property-setget

- `void (No return value.)` **set_end_cap_mode**(value: `LineCapMode<enum_Line2D_LineCapMode>`)
- `LineCapMode<enum_Line2D_LineCapMode>` **get_end_cap_mode**()

The style of the end of the polyline, if `closed<class_Line2D_property_closed>` is `false`.

classref-item-separator

classref-property

`Gradient<class_Gradient>` **gradient** `🔗<class_Line2D_property_gradient>`

classref-property-setget

- `void (No return value.)` **set_gradient**(value: `Gradient<class_Gradient>`)
- `Gradient<class_Gradient>` **get_gradient**()

The gradient is drawn through the whole line from start to finish. The `default_color<class_Line2D_property_default_color>` will not be used if this property is set.

classref-item-separator

classref-property

`LineJointMode<enum_Line2D_LineJointMode>` **joint_mode** = `0` `🔗<class_Line2D_property_joint_mode>`

classref-property-setget

- `void (No return value.)` **set_joint_mode**(value: `LineJointMode<enum_Line2D_LineJointMode>`)
- `LineJointMode<enum_Line2D_LineJointMode>` **get_joint_mode**()

The style of the connections between segments of the polyline.

classref-item-separator

classref-property

`PackedVector2Array<class_PackedVector2Array>` **points** = `PackedVector2Array()` `🔗<class_Line2D_property_points>`

classref-property-setget

- `void (No return value.)` **set_points**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_points**()

The points of the polyline, interpreted in local 2D coordinates. Segments are drawn between the adjacent points in this array.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.

classref-item-separator

classref-property

`int<class_int>` **round_precision** = `8` `🔗<class_Line2D_property_round_precision>`

classref-property-setget

- `void (No return value.)` **set_round_precision**(value: `int<class_int>`)
- `int<class_int>` **get_round_precision**()

The smoothness used for rounded joints and caps. Higher values result in smoother corners, but are more demanding to render and update.

classref-item-separator

classref-property

`float<class_float>` **sharp_limit** = `2.0` `🔗<class_Line2D_property_sharp_limit>`

classref-property-setget

- `void (No return value.)` **set_sharp_limit**(value: `float<class_float>`)
- `float<class_float>` **get_sharp_limit**()

Determines the miter limit of the polyline. Normally, when `joint_mode<class_Line2D_property_joint_mode>` is set to `LINE_JOINT_SHARP<class_Line2D_constant_LINE_JOINT_SHARP>`, sharp angles fall back to using the logic of `LINE_JOINT_BEVEL<class_Line2D_constant_LINE_JOINT_BEVEL>` joints to prevent very long miters. Higher values of this property mean that the fallback to a bevel joint will happen at sharper angles.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_Line2D_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

The texture used for the polyline. Uses `texture_mode<class_Line2D_property_texture_mode>` for drawing style.

classref-item-separator

classref-property

`LineTextureMode<enum_Line2D_LineTextureMode>` **texture_mode** = `0` `🔗<class_Line2D_property_texture_mode>`

classref-property-setget

- `void (No return value.)` **set_texture_mode**(value: `LineTextureMode<enum_Line2D_LineTextureMode>`)
- `LineTextureMode<enum_Line2D_LineTextureMode>` **get_texture_mode**()

The style to render the `texture<class_Line2D_property_texture>` of the polyline.

classref-item-separator

classref-property

`float<class_float>` **width** = `10.0` `🔗<class_Line2D_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `float<class_float>`)
- `float<class_float>` **get_width**()

The polyline's width.

classref-item-separator

classref-property

`Curve<class_Curve>` **width_curve** `🔗<class_Line2D_property_width_curve>`

classref-property-setget

- `void (No return value.)` **set_curve**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_curve**()

The polyline's width curve. The width of the polyline over its length will be equivalent to the value of the width curve over its domain. The width curve should be a unit `Curve<class_Curve>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_point**(position: `Vector2<class_Vector2>`, index: `int<class_int>` = -1) `🔗<class_Line2D_method_add_point>`

Adds a point with the specified `position` relative to the polyline's own position. If no `index` is provided, the new point will be added to the end of the points array.

If `index` is given, the new point is inserted before the existing point identified by index `index`. The indices of the points after the new point get increased by 1. The provided `index` must not exceed the number of existing points in the polyline. See `get_point_count()<class_Line2D_method_get_point_count>`.

classref-item-separator

classref-method

`void (No return value.)` **clear_points**() `🔗<class_Line2D_method_clear_points>`

Removes all points from the polyline, making it empty.

classref-item-separator

classref-method

`int<class_int>` **get_point_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Line2D_method_get_point_count>`

Returns the number of points in the polyline.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_point_position**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Line2D_method_get_point_position>`

Returns the position of the point at index `index`.

classref-item-separator

classref-method

`void (No return value.)` **remove_point**(index: `int<class_int>`) `🔗<class_Line2D_method_remove_point>`

Removes the point at index `index` from the polyline.

classref-item-separator

classref-method

`void (No return value.)` **set_point_position**(index: `int<class_int>`, position: `Vector2<class_Vector2>`) `🔗<class_Line2D_method_set_point_position>`

Overwrites the position of the point at the given `index` with the supplied `position`.