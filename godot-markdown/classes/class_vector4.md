github_url
hide

# Vector4

A 4D vector using floating-point coordinates.

classref-introduction-group

## Description

A 4-element structure that can be used to represent 4D coordinates or any other quadruplet of numeric values.

It uses floating-point coordinates. By default, these floating-point values use 32-bit precision, unlike `float<class_float>` which is always 64-bit. If double precision is needed, compile the engine with the option `precision=double`.

See `Vector4i<class_Vector4i>` for its integer counterpart.

**Note:** In a boolean context, a Vector4 will evaluate to `false` if it's equal to `Vector4(0, 0, 0, 0)`. Otherwise, a Vector4 will always evaluate to `true`.

classref-reftable-group

## Properties

classref-reftable-group

## Constructors

classref-reftable-group

## Methods

classref-reftable-group

## Operators

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Axis**: `🔗<enum_Vector4_Axis>`

classref-enumeration-constant

`Axis<enum_Vector4_Axis>` **AXIS_X** = `0`

Enumerated value for the X axis. Returned by `max_axis_index()<class_Vector4_method_max_axis_index>` and `min_axis_index()<class_Vector4_method_min_axis_index>`.

classref-enumeration-constant

`Axis<enum_Vector4_Axis>` **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by `max_axis_index()<class_Vector4_method_max_axis_index>` and `min_axis_index()<class_Vector4_method_min_axis_index>`.

classref-enumeration-constant

`Axis<enum_Vector4_Axis>` **AXIS_Z** = `2`

Enumerated value for the Z axis. Returned by `max_axis_index()<class_Vector4_method_max_axis_index>` and `min_axis_index()<class_Vector4_method_min_axis_index>`.

classref-enumeration-constant

`Axis<enum_Vector4_Axis>` **AXIS_W** = `3`

Enumerated value for the W axis. Returned by `max_axis_index()<class_Vector4_method_max_axis_index>` and `min_axis_index()<class_Vector4_method_min_axis_index>`.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**ZERO** = `Vector4(0, 0, 0, 0)` `🔗<class_Vector4_constant_ZERO>`

Zero vector, a vector with all components set to `0`.

classref-constant

**ONE** = `Vector4(1, 1, 1, 1)` `🔗<class_Vector4_constant_ONE>`

One vector, a vector with all components set to `1`.

classref-constant

**INF** = `Vector4(inf, inf, inf, inf)` `🔗<class_Vector4_constant_INF>`

Infinity vector, a vector with all components set to `@GDScript.INF<class_@GDScript_constant_INF>`.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **w** = `0.0` `🔗<class_Vector4_property_w>`

The vector's W component. Also accessible by using the index position `[3]`.

classref-item-separator

classref-property

`float<class_float>` **x** = `0.0` `🔗<class_Vector4_property_x>`

The vector's X component. Also accessible by using the index position `[0]`.

classref-item-separator

classref-property

`float<class_float>` **y** = `0.0` `🔗<class_Vector4_property_y>`

The vector's Y component. Also accessible by using the index position `[1]`.

classref-item-separator

classref-property

`float<class_float>` **z** = `0.0` `🔗<class_Vector4_property_z>`

The vector's Z component. Also accessible by using the index position `[2]`.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Vector4<class_Vector4>` **Vector4**() `🔗<class_Vector4_constructor_Vector4>`

Constructs a default-initialized **Vector4** with all components set to `0`.

classref-item-separator

classref-constructor

`Vector4<class_Vector4>` **Vector4**(from: `Vector4<class_Vector4>`)

Constructs a **Vector4** as a copy of the given **Vector4**.

classref-item-separator

classref-constructor

`Vector4<class_Vector4>` **Vector4**(from: `Vector4i<class_Vector4i>`)

Constructs a new **Vector4** from the given `Vector4i<class_Vector4i>`.

classref-item-separator

classref-constructor

`Vector4<class_Vector4>` **Vector4**(x: `float<class_float>`, y: `float<class_float>`, z: `float<class_float>`, w: `float<class_float>`)

Returns a **Vector4** with the given components.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Vector4<class_Vector4>` **abs**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_abs>`

Returns a new vector with all components in absolute values (i.e. positive).

classref-item-separator

classref-method

`Vector4<class_Vector4>` **ceil**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_ceil>`

Returns a new vector with all components rounded up (towards positive infinity).

classref-item-separator

classref-method

`Vector4<class_Vector4>` **clamp**(min: `Vector4<class_Vector4>`, max: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_clamp>`

Returns a new vector with all components clamped between the components of `min` and `max`, by running `@GlobalScope.clamp()<class_@GlobalScope_method_clamp>` on each component.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **clampf**(min: `float<class_float>`, max: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_clampf>`

Returns a new vector with all components clamped between `min` and `max`, by running `@GlobalScope.clamp()<class_@GlobalScope_method_clamp>` on each component.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **cubic_interpolate**(b: `Vector4<class_Vector4>`, pre_a: `Vector4<class_Vector4>`, post_b: `Vector4<class_Vector4>`, weight: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_cubic_interpolate>`

Performs a cubic interpolation between this vector and `b` using `pre_a` and `post_b` as handles, and returns the result at position `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **cubic_interpolate_in_time**(b: `Vector4<class_Vector4>`, pre_a: `Vector4<class_Vector4>`, post_b: `Vector4<class_Vector4>`, weight: `float<class_float>`, b_t: `float<class_float>`, pre_a_t: `float<class_float>`, post_b_t: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_cubic_interpolate_in_time>`

Performs a cubic interpolation between this vector and `b` using `pre_a` and `post_b` as handles, and returns the result at position `weight`. `weight` is on the range of 0.0 to 1.0, representing the amount of interpolation.

It can perform smoother interpolation than `cubic_interpolate()<class_Vector4_method_cubic_interpolate>` by the time values.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **direction_to**(to: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_direction_to>`

Returns the normalized vector pointing from this vector to `to`. This is equivalent to using `(b - a).normalized()`.

classref-item-separator

classref-method

`float<class_float>` **distance_squared_to**(to: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_distance_squared_to>`

Returns the squared [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

This method runs faster than `distance_to()<class_Vector4_method_distance_to>`, so prefer it if you need to compare vectors or need the squared distance for some formula.

classref-item-separator

classref-method

`float<class_float>` **distance_to**(to: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_distance_to>`

Returns the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

classref-item-separator

classref-method

`float<class_float>` **dot**(with: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_dot>`

Returns the dot product of this vector and `with`.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **floor**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_floor>`

Returns a new vector with all components rounded down (towards negative infinity).

classref-item-separator

classref-method

`Vector4<class_Vector4>` **inverse**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_inverse>`

Returns the inverse of the vector. This is the same as `Vector4(1.0 / v.x, 1.0 / v.y, 1.0 / v.z, 1.0 / v.w)`.

classref-item-separator

classref-method

`bool<class_bool>` **is_equal_approx**(to: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_is_equal_approx>`

Returns `true` if this vector and `to` are approximately equal, by running `@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` on each component.

classref-item-separator

classref-method

`bool<class_bool>` **is_finite**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_is_finite>`

Returns `true` if this vector is finite, by calling `@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>` on each component.

classref-item-separator

classref-method

`bool<class_bool>` **is_normalized**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_is_normalized>`

Returns `true` if the vector is normalized, i.e. its length is approximately equal to 1.

classref-item-separator

classref-method

`bool<class_bool>` **is_zero_approx**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_is_zero_approx>`

Returns `true` if this vector's values are approximately zero, by running `@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>` on each component.

This method is faster than using `is_equal_approx()<class_Vector4_method_is_equal_approx>` with one value as a zero vector.

classref-item-separator

classref-method

`float<class_float>` **length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_length>`

Returns the length (magnitude) of this vector.

classref-item-separator

classref-method

`float<class_float>` **length_squared**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_length_squared>`

Returns the squared length (squared magnitude) of this vector.

This method runs faster than `length()<class_Vector4_method_length>`, so prefer it if you need to compare vectors or need the squared distance for some formula.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **lerp**(to: `Vector4<class_Vector4>`, weight: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_lerp>`

Returns the result of the linear interpolation between this vector and `to` by amount `weight`. `weight` is on the range of `0.0` to `1.0`, representing the amount of interpolation.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **max**(with: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_max>`

Returns the component-wise maximum of this and `with`, equivalent to `Vector4(maxf(x, with.x), maxf(y, with.y), maxf(z, with.z), maxf(w, with.w))`.

classref-item-separator

classref-method

`int<class_int>` **max_axis_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_max_axis_index>`

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns `AXIS_X<class_Vector4_constant_AXIS_X>`.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **maxf**(with: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_maxf>`

Returns the component-wise maximum of this and `with`, equivalent to `Vector4(maxf(x, with), maxf(y, with), maxf(z, with), maxf(w, with))`.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **min**(with: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_min>`

Returns the component-wise minimum of this and `with`, equivalent to `Vector4(minf(x, with.x), minf(y, with.y), minf(z, with.z), minf(w, with.w))`.

classref-item-separator

classref-method

`int<class_int>` **min_axis_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_min_axis_index>`

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns `AXIS_W<class_Vector4_constant_AXIS_W>`.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **minf**(with: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_minf>`

Returns the component-wise minimum of this and `with`, equivalent to `Vector4(minf(x, with), minf(y, with), minf(z, with), minf(w, with))`.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **normalized**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_normalized>`

Returns the result of scaling the vector to unit length. Equivalent to `v / v.length()`. Returns `(0, 0, 0, 0)` if `v.length() == 0`. See also `is_normalized()<class_Vector4_method_is_normalized>`.

**Note:** This function may return incorrect values if the input vector length is near zero.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **posmod**(mod: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_posmod>`

Returns a vector composed of the `@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>` of this vector's components and `mod`.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **posmodv**(modv: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_posmodv>`

Returns a vector composed of the `@GlobalScope.fposmod()<class_@GlobalScope_method_fposmod>` of this vector's components and `modv`'s components.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **round**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_round>`

Returns a new vector with all components rounded to the nearest integer, with halfway cases rounded away from zero.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **sign**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_sign>`

Returns a new vector with each component set to `1.0` if it's positive, `-1.0` if it's negative, and `0.0` if it's zero. The result is identical to calling `@GlobalScope.sign()<class_@GlobalScope_method_sign>` on each component.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **snapped**(step: `Vector4<class_Vector4>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_snapped>`

Returns a new vector with each component snapped to the nearest multiple of the corresponding component in `step`. This can also be used to round the components to an arbitrary number of decimals.

classref-item-separator

classref-method

`Vector4<class_Vector4>` **snappedf**(step: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector4_method_snappedf>`

Returns a new vector with each component snapped to the nearest multiple of `step`. This can also be used to round the components to an arbitrary number of decimals.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_neq_Vector4>`

Returns `true` if the vectors are not equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Vector4_method_is_equal_approx>` instead, which is more reliable.

**Note:** Vectors with `@GDScript.NAN<class_@GDScript_constant_NAN>` elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `Projection<class_Projection>`) `🔗<class_Vector4_operator_mul_Projection>`

Transforms (multiplies) the **Vector4** by the transpose of the given `Projection<class_Projection>` matrix.

For transforming by inverse of a projection `projection.inverse() * vector` can be used instead. See `Projection.inverse()<class_Projection_method_inverse>`.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_mul_Vector4>`

Multiplies each component of the **Vector4** by the components of the given **Vector4**.

    print(Vector4(10, 20, 30, 40) * Vector4(3, 4, 5, 6)) # Prints (30.0, 80.0, 150.0, 240.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `float<class_float>`) `🔗<class_Vector4_operator_mul_float>`

Multiplies each component of the **Vector4** by the given `float<class_float>`.

    print(Vector4(10, 20, 30, 40) * 2) # Prints (20.0, 40.0, 60.0, 80.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `int<class_int>`) `🔗<class_Vector4_operator_mul_int>`

Multiplies each component of the **Vector4** by the given `int<class_int>`.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator +**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_sum_Vector4>`

Adds each component of the **Vector4** by the components of the given **Vector4**.

    print(Vector4(10, 20, 30, 40) + Vector4(3, 4, 5, 6)) # Prints (13.0, 24.0, 35.0, 46.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator -**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_dif_Vector4>`

Subtracts each component of the **Vector4** by the components of the given **Vector4**.

    print(Vector4(10, 20, 30, 40) - Vector4(3, 4, 5, 6)) # Prints (7.0, 16.0, 25.0, 34.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator /**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_div_Vector4>`

Divides each component of the **Vector4** by the components of the given **Vector4**.

    print(Vector4(10, 20, 30, 40) / Vector4(2, 5, 3, 4)) # Prints (5.0, 4.0, 10.0, 10.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator /**(right: `float<class_float>`) `🔗<class_Vector4_operator_div_float>`

Divides each component of the **Vector4** by the given `float<class_float>`.

    print(Vector4(10, 20, 30, 40) / 2) # Prints (5.0, 10.0, 15.0, 20.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator /**(right: `int<class_int>`) `🔗<class_Vector4_operator_div_int>`

Divides each component of the **Vector4** by the given `int<class_int>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_lt_Vector4>`

Compares two **Vector4** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

**Note:** Vectors with `@GDScript.NAN<class_@GDScript_constant_NAN>` elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<=**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_lte_Vector4>`

Compares two **Vector4** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

**Note:** Vectors with `@GDScript.NAN<class_@GDScript_constant_NAN>` elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_eq_Vector4>`

Returns `true` if the vectors are exactly equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Vector4_method_is_equal_approx>` instead, which is more reliable.

**Note:** Vectors with `@GDScript.NAN<class_@GDScript_constant_NAN>` elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_gt_Vector4>`

Compares two **Vector4** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

**Note:** Vectors with `@GDScript.NAN<class_@GDScript_constant_NAN>` elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>=**(right: `Vector4<class_Vector4>`) `🔗<class_Vector4_operator_gte_Vector4>`

Compares two **Vector4** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors, Z values of the two vectors, and then with the W values. This operator is useful for sorting vectors.

**Note:** Vectors with `@GDScript.NAN<class_@GDScript_constant_NAN>` elements don't behave the same as other vectors. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`float<class_float>` **operator \[\]**(index: `int<class_int>`) `🔗<class_Vector4_operator_idx_int>`

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, `v[1]` is equivalent to `v.y`, `v[2]` is equivalent to `v.z`, and `v[3]` is equivalent to `v.w`.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator unary+**() `🔗<class_Vector4_operator_unplus>`

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator unary-**() `🔗<class_Vector4_operator_unminus>`

Returns the negative value of the **Vector4**. This is the same as writing `Vector4(-v.x, -v.y, -v.z, -v.w)`. This operation flips the direction of the vector while keeping the same magnitude. With floats, the number zero can be either positive or negative.