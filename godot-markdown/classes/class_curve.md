github_url
hide

# Curve

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A mathematical curve.

classref-introduction-group

## Description

This resource describes a mathematical curve by defining a set of points and tangents at each point. By default, it ranges between `0` and `1` on the X and Y axes, but these ranges can be changed.

Please note that many resources and nodes assume they are given *unit curves*. A unit curve is a curve whose domain (the X axis) is between `0` and `1`. Some examples of unit curve usage are `CPUParticles2D.angle_curve<class_CPUParticles2D_property_angle_curve>` and `Line2D.width_curve<class_Line2D_property_width_curve>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**domain_changed**() `🔗<class_Curve_signal_domain_changed>`

Emitted when `max_domain<class_Curve_property_max_domain>` or `min_domain<class_Curve_property_min_domain>` is changed.

classref-item-separator

classref-signal

**range_changed**() `🔗<class_Curve_signal_range_changed>`

Emitted when `max_value<class_Curve_property_max_value>` or `min_value<class_Curve_property_min_value>` is changed.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **TangentMode**: `🔗<enum_Curve_TangentMode>`

classref-enumeration-constant

`TangentMode<enum_Curve_TangentMode>` **TANGENT_FREE** = `0`

The tangent on this side of the point is user-defined.

classref-enumeration-constant

`TangentMode<enum_Curve_TangentMode>` **TANGENT_LINEAR** = `1`

The curve calculates the tangent on this side of the point as the slope halfway towards the adjacent point.

classref-enumeration-constant

`TangentMode<enum_Curve_TangentMode>` **TANGENT_MODE_COUNT** = `2`

The total number of available tangent modes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **bake_resolution** = `100` `🔗<class_Curve_property_bake_resolution>`

classref-property-setget

- `void (No return value.)` **set_bake_resolution**(value: `int<class_int>`)
- `int<class_int>` **get_bake_resolution**()

The number of points to include in the baked (i.e. cached) curve data.

classref-item-separator

classref-property

`float<class_float>` **max_domain** = `1.0` `🔗<class_Curve_property_max_domain>`

classref-property-setget

- `void (No return value.)` **set_max_domain**(value: `float<class_float>`)
- `float<class_float>` **get_max_domain**()

The maximum domain (x-coordinate) that points can have.

classref-item-separator

classref-property

`float<class_float>` **max_value** = `1.0` `🔗<class_Curve_property_max_value>`

classref-property-setget

- `void (No return value.)` **set_max_value**(value: `float<class_float>`)
- `float<class_float>` **get_max_value**()

The maximum value (y-coordinate) that points can have. Tangents can cause higher values between points.

classref-item-separator

classref-property

`float<class_float>` **min_domain** = `0.0` `🔗<class_Curve_property_min_domain>`

classref-property-setget

- `void (No return value.)` **set_min_domain**(value: `float<class_float>`)
- `float<class_float>` **get_min_domain**()

The minimum domain (x-coordinate) that points can have.

classref-item-separator

classref-property

`float<class_float>` **min_value** = `0.0` `🔗<class_Curve_property_min_value>`

classref-property-setget

- `void (No return value.)` **set_min_value**(value: `float<class_float>`)
- `float<class_float>` **get_min_value**()

The minimum value (y-coordinate) that points can have. Tangents can cause lower values between points.

classref-item-separator

classref-property

`int<class_int>` **point_count** = `0` `🔗<class_Curve_property_point_count>`

classref-property-setget

- `void (No return value.)` **set_point_count**(value: `int<class_int>`)
- `int<class_int>` **get_point_count**()

The number of points describing the curve.

classref-item-separator

classref-property

`int<class_int>` **point\_{index}/left_mode** = `0` `🔗<class_Curve_property_point_{index}/left_mode>`

The left `TangentMode<enum_Curve_TangentMode>` for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

classref-item-separator

classref-property

`float<class_float>` **point\_{index}/left_tangent** = `0.0` `🔗<class_Curve_property_point_{index}/left_tangent>`

The left tangent angle (in degrees) for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **point\_{index}/position** = `Vector2(0, 0)` `🔗<class_Curve_property_point_{index}/position>`

The position of the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

classref-item-separator

classref-property

`int<class_int>` **point\_{index}/right_mode** = `0` `🔗<class_Curve_property_point_{index}/right_mode>`

The right `TangentMode<enum_Curve_TangentMode>` for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

classref-item-separator

classref-property

`float<class_float>` **point\_{index}/right_tangent** = `0.0` `🔗<class_Curve_property_point_{index}/right_tangent>`

The right tangent angle (in degrees) for the point at `index`.

**Note:** `index` is a value in the `0 .. point_count - 1` range.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **add_point**(position: `Vector2<class_Vector2>`, left_tangent: `float<class_float>` = 0, right_tangent: `float<class_float>` = 0, left_mode: `TangentMode<enum_Curve_TangentMode>` = 0, right_mode: `TangentMode<enum_Curve_TangentMode>` = 0) `🔗<class_Curve_method_add_point>`

Adds a point to the curve. For each side, if the `*_mode` is `TANGENT_LINEAR<class_Curve_constant_TANGENT_LINEAR>`, the `*_tangent` angle (in degrees) uses the slope of the curve halfway to the adjacent point. Allows custom assignments to the `*_tangent` angle if `*_mode` is set to `TANGENT_FREE<class_Curve_constant_TANGENT_FREE>`.

classref-item-separator

classref-method

`void (No return value.)` **bake**() `🔗<class_Curve_method_bake>`

Recomputes the baked cache of points for the curve.

classref-item-separator

classref-method

`void (No return value.)` **clean_dupes**() `🔗<class_Curve_method_clean_dupes>`

Removes duplicate points, i.e. points that are less than 0.00001 units (engine epsilon value) away from their neighbor on the curve.

classref-item-separator

classref-method

`void (No return value.)` **clear_points**() `🔗<class_Curve_method_clear_points>`

Removes all points from the curve.

classref-item-separator

classref-method

`float<class_float>` **get_domain_range**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_domain_range>`

Returns the difference between `min_domain<class_Curve_property_min_domain>` and `max_domain<class_Curve_property_max_domain>`.

classref-item-separator

classref-method

`TangentMode<enum_Curve_TangentMode>` **get_point_left_mode**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_point_left_mode>`

Returns the left `TangentMode<enum_Curve_TangentMode>` for the point at `index`.

classref-item-separator

classref-method

`float<class_float>` **get_point_left_tangent**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_point_left_tangent>`

Returns the left tangent angle (in degrees) for the point at `index`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_point_position**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_point_position>`

Returns the curve coordinates for the point at `index`.

classref-item-separator

classref-method

`TangentMode<enum_Curve_TangentMode>` **get_point_right_mode**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_point_right_mode>`

Returns the right `TangentMode<enum_Curve_TangentMode>` for the point at `index`.

classref-item-separator

classref-method

`float<class_float>` **get_point_right_tangent**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_point_right_tangent>`

Returns the right tangent angle (in degrees) for the point at `index`.

classref-item-separator

classref-method

`float<class_float>` **get_value_range**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_get_value_range>`

Returns the difference between `min_value<class_Curve_property_min_value>` and `max_value<class_Curve_property_max_value>`.

classref-item-separator

classref-method

`void (No return value.)` **remove_point**(index: `int<class_int>`) `🔗<class_Curve_method_remove_point>`

Removes the point at `index` from the curve.

classref-item-separator

classref-method

`float<class_float>` **sample**(offset: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_sample>`

Returns the Y value for the point that would exist at the X position `offset` along the curve.

classref-item-separator

classref-method

`float<class_float>` **sample_baked**(offset: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Curve_method_sample_baked>`

Returns the Y value for the point that would exist at the X position `offset` along the curve using the baked cache. Bakes the curve's points if not already baked.

classref-item-separator

classref-method

`void (No return value.)` **set_point_left_mode**(index: `int<class_int>`, mode: `TangentMode<enum_Curve_TangentMode>`) `🔗<class_Curve_method_set_point_left_mode>`

Sets the left `TangentMode<enum_Curve_TangentMode>` for the point at `index` to `mode`.

classref-item-separator

classref-method

`void (No return value.)` **set_point_left_tangent**(index: `int<class_int>`, tangent: `float<class_float>`) `🔗<class_Curve_method_set_point_left_tangent>`

Sets the left tangent angle for the point at `index` to `tangent`.

classref-item-separator

classref-method

`int<class_int>` **set_point_offset**(index: `int<class_int>`, offset: `float<class_float>`) `🔗<class_Curve_method_set_point_offset>`

Sets the offset from `0.5`.

classref-item-separator

classref-method

`void (No return value.)` **set_point_right_mode**(index: `int<class_int>`, mode: `TangentMode<enum_Curve_TangentMode>`) `🔗<class_Curve_method_set_point_right_mode>`

Sets the right `TangentMode<enum_Curve_TangentMode>` for the point at `index` to `mode`.

classref-item-separator

classref-method

`void (No return value.)` **set_point_right_tangent**(index: `int<class_int>`, tangent: `float<class_float>`) `🔗<class_Curve_method_set_point_right_tangent>`

Sets the right tangent angle for the point at `index` to `tangent`.

classref-item-separator

classref-method

`void (No return value.)` **set_point_value**(index: `int<class_int>`, y: `float<class_float>`) `🔗<class_Curve_method_set_point_value>`

Assigns the vertical position `y` to the point at `index`.