github_url
hide

# Vector2i

A 2D vector using integer coordinates.

classref-introduction-group

## Description

A 2-element structure that can be used to represent 2D grid coordinates or any other pair of integers.

It uses integer coordinates and is therefore preferable to `Vector2<class_Vector2>` when exact precision is required. Note that the values are limited to 32 bits, and unlike `Vector2<class_Vector2>` this cannot be configured with an engine build option. Use `int<class_int>` or `PackedInt64Array<class_PackedInt64Array>` if 64-bit values are needed.

**Note:** In a boolean context, a Vector2i will evaluate to `false` if it's equal to `Vector2i(0, 0)`. Otherwise, a Vector2i will always evaluate to `true`.

classref-introduction-group

## Tutorials

- `Math documentation index <../tutorials/math/index>`
- `Vector math <../tutorials/math/vector_math>`
- [3Blue1Brown Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

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

enum **Axis**: `🔗<enum_Vector2i_Axis>`

classref-enumeration-constant

`Axis<enum_Vector2i_Axis>` **AXIS_X** = `0`

Enumerated value for the X axis. Returned by `max_axis_index()<class_Vector2i_method_max_axis_index>` and `min_axis_index()<class_Vector2i_method_min_axis_index>`.

classref-enumeration-constant

`Axis<enum_Vector2i_Axis>` **AXIS_Y** = `1`

Enumerated value for the Y axis. Returned by `max_axis_index()<class_Vector2i_method_max_axis_index>` and `min_axis_index()<class_Vector2i_method_min_axis_index>`.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**ZERO** = `Vector2i(0, 0)` `🔗<class_Vector2i_constant_ZERO>`

Zero vector, a vector with all components set to `0`.

classref-constant

**ONE** = `Vector2i(1, 1)` `🔗<class_Vector2i_constant_ONE>`

One vector, a vector with all components set to `1`.

classref-constant

**MIN** = `Vector2i(-2147483648, -2147483648)` `🔗<class_Vector2i_constant_MIN>`

Min vector, a vector with all components equal to `INT32_MIN`. Can be used as a negative integer equivalent of `Vector2.INF<class_Vector2_constant_INF>`.

classref-constant

**MAX** = `Vector2i(2147483647, 2147483647)` `🔗<class_Vector2i_constant_MAX>`

Max vector, a vector with all components equal to `INT32_MAX`. Can be used as an integer equivalent of `Vector2.INF<class_Vector2_constant_INF>`.

classref-constant

**LEFT** = `Vector2i(-1, 0)` `🔗<class_Vector2i_constant_LEFT>`

Left unit vector. Represents the direction of left.

classref-constant

**RIGHT** = `Vector2i(1, 0)` `🔗<class_Vector2i_constant_RIGHT>`

Right unit vector. Represents the direction of right.

classref-constant

**UP** = `Vector2i(0, -1)` `🔗<class_Vector2i_constant_UP>`

Up unit vector. Y is down in 2D, so this vector points -Y.

classref-constant

**DOWN** = `Vector2i(0, 1)` `🔗<class_Vector2i_constant_DOWN>`

Down unit vector. Y is down in 2D, so this vector points +Y.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **x** = `0` `🔗<class_Vector2i_property_x>`

The vector's X component. Also accessible by using the index position `[0]`.

classref-item-separator

classref-property

`int<class_int>` **y** = `0` `🔗<class_Vector2i_property_y>`

The vector's Y component. Also accessible by using the index position `[1]`.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Vector2i<class_Vector2i>` **Vector2i**() `🔗<class_Vector2i_constructor_Vector2i>`

Constructs a default-initialized **Vector2i** with all components set to `0`.

classref-item-separator

classref-constructor

`Vector2i<class_Vector2i>` **Vector2i**(from: `Vector2i<class_Vector2i>`)

Constructs a **Vector2i** as a copy of the given **Vector2i**.

classref-item-separator

classref-constructor

`Vector2i<class_Vector2i>` **Vector2i**(from: `Vector2<class_Vector2>`)

Constructs a new **Vector2i** from the given `Vector2<class_Vector2>` by truncating components' fractional parts (rounding towards zero). For a different behavior consider passing the result of `Vector2.ceil()<class_Vector2_method_ceil>`, `Vector2.floor()<class_Vector2_method_floor>` or `Vector2.round()<class_Vector2_method_round>` to this constructor instead.

classref-item-separator

classref-constructor

`Vector2i<class_Vector2i>` **Vector2i**(x: `int<class_int>`, y: `int<class_int>`)

Constructs a new **Vector2i** from the given `x` and `y`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Vector2i<class_Vector2i>` **abs**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_abs>`

Returns a new vector with all components in absolute values (i.e. positive).

classref-item-separator

classref-method

`float<class_float>` **aspect**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_aspect>`

Returns the aspect ratio of this vector, the ratio of `x<class_Vector2i_property_x>` to `y<class_Vector2i_property_y>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **clamp**(min: `Vector2i<class_Vector2i>`, max: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_clamp>`

Returns a new vector with all components clamped between the components of `min` and `max`, by running `@GlobalScope.clamp()<class_@GlobalScope_method_clamp>` on each component.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **clampi**(min: `int<class_int>`, max: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_clampi>`

Returns a new vector with all components clamped between `min` and `max`, by running `@GlobalScope.clamp()<class_@GlobalScope_method_clamp>` on each component.

classref-item-separator

classref-method

`int<class_int>` **distance_squared_to**(to: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_distance_squared_to>`

Returns the squared [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

This method runs faster than `distance_to()<class_Vector2i_method_distance_to>`, so prefer it if you need to compare vectors or need the squared distance for some formula.

classref-item-separator

classref-method

`float<class_float>` **distance_to**(to: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_distance_to>`

Returns the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between this vector and `to`.

classref-item-separator

classref-method

`float<class_float>` **length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_length>`

Returns the length (magnitude) of this vector.

classref-item-separator

classref-method

`int<class_int>` **length_squared**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_length_squared>`

Returns the squared length (squared magnitude) of this vector.

This method runs faster than `length()<class_Vector2i_method_length>`, so prefer it if you need to compare vectors or need the squared distance for some formula.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **max**(with: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_max>`

Returns the component-wise maximum of this and `with`, equivalent to `Vector2i(maxi(x, with.x), maxi(y, with.y))`.

classref-item-separator

classref-method

`int<class_int>` **max_axis_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_max_axis_index>`

Returns the axis of the vector's highest value. See `AXIS_*` constants. If all components are equal, this method returns `AXIS_X<class_Vector2i_constant_AXIS_X>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **maxi**(with: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_maxi>`

Returns the component-wise maximum of this and `with`, equivalent to `Vector2i(maxi(x, with), maxi(y, with))`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **min**(with: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_min>`

Returns the component-wise minimum of this and `with`, equivalent to `Vector2i(mini(x, with.x), mini(y, with.y))`.

classref-item-separator

classref-method

`int<class_int>` **min_axis_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_min_axis_index>`

Returns the axis of the vector's lowest value. See `AXIS_*` constants. If all components are equal, this method returns `AXIS_Y<class_Vector2i_constant_AXIS_Y>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **mini**(with: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_mini>`

Returns the component-wise minimum of this and `with`, equivalent to `Vector2i(mini(x, with), mini(y, with))`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **sign**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_sign>`

Returns a new vector with each component set to `1` if it's positive, `-1` if it's negative, and `0` if it's zero. The result is identical to calling `@GlobalScope.sign()<class_@GlobalScope_method_sign>` on each component.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **snapped**(step: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_snapped>`

Returns a new vector with each component snapped to the closest multiple of the corresponding component in `step`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **snappedi**(step: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Vector2i_method_snappedi>`

Returns a new vector with each component snapped to the closest multiple of `step`.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_neq_Vector2i>`

Returns `true` if the vectors are not equal.

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator %**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_mod_Vector2i>`

Gets the remainder of each component of the **Vector2i** with the components of the given **Vector2i**. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using `@GlobalScope.posmod()<class_@GlobalScope_method_posmod>` instead if you want to handle negative numbers.

    print(Vector2i(10, -20) % Vector2i(7, 8)) # Prints (3, -4)

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator %**(right: `int<class_int>`) `🔗<class_Vector2i_operator_mod_int>`

Gets the remainder of each component of the **Vector2i** with the given `int<class_int>`. This operation uses truncated division, which is often not desired as it does not work well with negative numbers. Consider using `@GlobalScope.posmod()<class_@GlobalScope_method_posmod>` instead if you want to handle negative numbers.

    print(Vector2i(10, -20) % 7) # Prints (3, -6)

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator**\*(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_mul_Vector2i>`

Multiplies each component of the **Vector2i** by the components of the given **Vector2i**.

    print(Vector2i(10, 20) * Vector2i(3, 4)) # Prints (30, 80)

classref-item-separator

classref-operator

`Vector2<class_Vector2>` **operator**\*(right: `float<class_float>`) `🔗<class_Vector2i_operator_mul_float>`

Multiplies each component of the **Vector2i** by the given `float<class_float>`. Returns a `Vector2<class_Vector2>`.

    print(Vector2i(10, 15) * 0.9) # Prints (9.0, 13.5)

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator**\*(right: `int<class_int>`) `🔗<class_Vector2i_operator_mul_int>`

Multiplies each component of the **Vector2i** by the given `int<class_int>`.

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator +**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_sum_Vector2i>`

Adds each component of the **Vector2i** by the components of the given **Vector2i**.

    print(Vector2i(10, 20) + Vector2i(3, 4)) # Prints (13, 24)

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator -**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_dif_Vector2i>`

Subtracts each component of the **Vector2i** by the components of the given **Vector2i**.

    print(Vector2i(10, 20) - Vector2i(3, 4)) # Prints (7, 16)

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator /**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_div_Vector2i>`

Divides each component of the **Vector2i** by the components of the given **Vector2i**.

    print(Vector2i(10, 20) / Vector2i(2, 5)) # Prints (5, 4)

classref-item-separator

classref-operator

`Vector2<class_Vector2>` **operator /**(right: `float<class_float>`) `🔗<class_Vector2i_operator_div_float>`

Divides each component of the **Vector2i** by the given `float<class_float>`. Returns a `Vector2<class_Vector2>`.

    print(Vector2i(1, 2) / 2.5) # Prints (0.4, 0.8)

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator /**(right: `int<class_int>`) `🔗<class_Vector2i_operator_div_int>`

Divides each component of the **Vector2i** by the given `int<class_int>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_lt_Vector2i>`

Compares two **Vector2i** vectors by first checking if the X value of the left vector is less than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<=**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_lte_Vector2i>`

Compares two **Vector2i** vectors by first checking if the X value of the left vector is less than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_eq_Vector2i>`

Returns `true` if the vectors are equal.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_gt_Vector2i>`

Compares two **Vector2i** vectors by first checking if the X value of the left vector is greater than the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>=**(right: `Vector2i<class_Vector2i>`) `🔗<class_Vector2i_operator_gte_Vector2i>`

Compares two **Vector2i** vectors by first checking if the X value of the left vector is greater than or equal to the X value of the `right` vector. If the X values are exactly equal, then it repeats this check with the Y values of the two vectors. This operator is useful for sorting vectors.

classref-item-separator

classref-operator

`int<class_int>` **operator \[\]**(index: `int<class_int>`) `🔗<class_Vector2i_operator_idx_int>`

Access vector components using their `index`. `v[0]` is equivalent to `v.x`, and `v[1]` is equivalent to `v.y`.

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator unary+**() `🔗<class_Vector2i_operator_unplus>`

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

classref-item-separator

classref-operator

`Vector2i<class_Vector2i>` **operator unary-**() `🔗<class_Vector2i_operator_unminus>`

Returns the negative value of the **Vector2i**. This is the same as writing `Vector2i(-v.x, -v.y)`. This operation flips the direction of the vector while keeping the same magnitude.