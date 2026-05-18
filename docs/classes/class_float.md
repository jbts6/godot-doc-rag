github_url
hide

# float

A built-in type for floating-point numbers.

classref-introduction-group

## Description

The **float** built-in type is a 64-bit double-precision floating-point number, equivalent to `double` in C++. This type has 14 reliable decimal digits of precision. The maximum value of **float** is approximately `1.79769e308`, and the minimum is approximately `-1.79769e308`.

Many methods and properties in the engine use 32-bit single-precision floating-point numbers instead, equivalent to `float` in C++, which have 6 reliable decimal digits of precision. For data structures such as `Vector2<class_Vector2>` and `Vector3<class_Vector3>`, Godot uses 32-bit floating-point numbers by default, but it can be changed to use 64-bit doubles if Godot is compiled with the `precision=double` option.

Math done using the **float** type is not guaranteed to be exact and will often result in small errors. You should usually use the `@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` and `@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>` methods instead of `==` to compare **float** values for equality.

**Note:** In a boolean context, a **float** will evaluate to `false` if it's exactly equal to `0.0`, and to `true` otherwise.

classref-introduction-group

## Tutorials

- [Wikipedia: Double-precision floating-point format](https://en.wikipedia.org/wiki/Double-precision_floating-point_format)
- [Wikipedia: Single-precision floating-point format](https://en.wikipedia.org/wiki/Single-precision_floating-point_format)

classref-reftable-group

## Constructors

classref-reftable-group

## Operators

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`float<class_float>` **float**() `🔗<class_float_constructor_float>`

Constructs a default-initialized **float** set to `0.0`.

classref-item-separator

classref-constructor

`float<class_float>` **float**(from: `float<class_float>`)

Constructs a **float** as a copy of the given **float**.

classref-item-separator

classref-constructor

`float<class_float>` **float**(from: `String<class_String>`)

Converts a `String<class_String>` to a **float**, following the same rules as `String.to_float()<class_String_method_to_float>`.

classref-item-separator

classref-constructor

`float<class_float>` **float**(from: `bool<class_bool>`)

Cast a `bool<class_bool>` value to a floating-point value, `float(true)` will be equal to 1.0 and `float(false)` will be equal to 0.0.

classref-item-separator

classref-constructor

`float<class_float>` **float**(from: `int<class_int>`)

Cast an `int<class_int>` value to a floating-point value, `float(1)` will be equal to `1.0`.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `float<class_float>`) `🔗<class_float_operator_neq_float>`

Returns `true` if two floats are different from each other.

**Note:** `@GDScript.NAN<class_@GDScript_constant_NAN>` doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator !=**(right: `int<class_int>`) `🔗<class_float_operator_neq_int>`

Returns `true` if the integer has different value than the float.

classref-item-separator

classref-operator

`Color<class_Color>` **operator**\*(right: `Color<class_Color>`) `🔗<class_float_operator_mul_Color>`

Multiplies each component of the `Color<class_Color>`, including the alpha, by the given **float**.

    print(1.5 * Color(0.5, 0.5, 0.5)) # Prints (0.75, 0.75, 0.75, 1.5)

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator**\*(right: `Quaternion<class_Quaternion>`) `🔗<class_float_operator_mul_Quaternion>`

Multiplies each component of the `Quaternion<class_Quaternion>` by the given **float**. This operation is not meaningful on its own, but it can be used as a part of a larger expression.

classref-item-separator

classref-operator

`Vector2<class_Vector2>` **operator**\*(right: `Vector2<class_Vector2>`) `🔗<class_float_operator_mul_Vector2>`

Multiplies each component of the `Vector2<class_Vector2>` by the given **float**.

    print(2.5 * Vector2(1, 3)) # Prints (2.5, 7.5)

classref-item-separator

classref-operator

`Vector2<class_Vector2>` **operator**\*(right: `Vector2i<class_Vector2i>`) `🔗<class_float_operator_mul_Vector2i>`

Multiplies each component of the `Vector2i<class_Vector2i>` by the given **float**. Returns a `Vector2<class_Vector2>`.

    print(0.9 * Vector2i(10, 15)) # Prints (9.0, 13.5)

classref-item-separator

classref-operator

`Vector3<class_Vector3>` **operator**\*(right: `Vector3<class_Vector3>`) `🔗<class_float_operator_mul_Vector3>`

Multiplies each component of the `Vector3<class_Vector3>` by the given **float**.

classref-item-separator

classref-operator

`Vector3<class_Vector3>` **operator**\*(right: `Vector3i<class_Vector3i>`) `🔗<class_float_operator_mul_Vector3i>`

Multiplies each component of the `Vector3i<class_Vector3i>` by the given **float**. Returns a `Vector3<class_Vector3>`.

    print(0.9 * Vector3i(10, 15, 20)) # Prints (9.0, 13.5, 18.0)

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `Vector4<class_Vector4>`) `🔗<class_float_operator_mul_Vector4>`

Multiplies each component of the `Vector4<class_Vector4>` by the given **float**.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `Vector4i<class_Vector4i>`) `🔗<class_float_operator_mul_Vector4i>`

Multiplies each component of the `Vector4i<class_Vector4i>` by the given **float**. Returns a `Vector4<class_Vector4>`.

    print(0.9 * Vector4i(10, 15, 20, -10)) # Prints (9.0, 13.5, 18.0, -9.0)

classref-item-separator

classref-operator

`float<class_float>` **operator**\*(right: `float<class_float>`) `🔗<class_float_operator_mul_float>`

Multiplies two **float**s.

classref-item-separator

classref-operator

`float<class_float>` **operator**\*(right: `int<class_int>`) `🔗<class_float_operator_mul_int>`

Multiplies a **float** and an `int<class_int>`. The result is a **float**.

classref-item-separator

classref-operator

`float<class_float>` **operator**\*\*(right: `float<class_float>`) `🔗<class_float_operator_pow_float>`

Raises a **float** to a power of a **float**.

    print(39.0625**0.25) # 2.5

classref-item-separator

classref-operator

`float<class_float>` **operator**\*\*(right: `int<class_int>`) `🔗<class_float_operator_pow_int>`

Raises a **float** to a power of an `int<class_int>`. The result is a **float**.

    print(0.9**3) # 0.729

classref-item-separator

classref-operator

`float<class_float>` **operator +**(right: `float<class_float>`) `🔗<class_float_operator_sum_float>`

Adds two floats.

classref-item-separator

classref-operator

`float<class_float>` **operator +**(right: `int<class_int>`) `🔗<class_float_operator_sum_int>`

Adds a **float** and an `int<class_int>`. The result is a **float**.

classref-item-separator

classref-operator

`float<class_float>` **operator -**(right: `float<class_float>`) `🔗<class_float_operator_dif_float>`

Subtracts a float from a float.

classref-item-separator

classref-operator

`float<class_float>` **operator -**(right: `int<class_int>`) `🔗<class_float_operator_dif_int>`

Subtracts an `int<class_int>` from a **float**. The result is a **float**.

classref-item-separator

classref-operator

`float<class_float>` **operator /**(right: `float<class_float>`) `🔗<class_float_operator_div_float>`

Divides two floats.

classref-item-separator

classref-operator

`float<class_float>` **operator /**(right: `int<class_int>`) `🔗<class_float_operator_div_int>`

Divides a **float** by an `int<class_int>`. The result is a **float**.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<**(right: `float<class_float>`) `🔗<class_float_operator_lt_float>`

Returns `true` if the left float is less than the right one.

**Note:** `@GDScript.NAN<class_@GDScript_constant_NAN>` doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<**(right: `int<class_int>`) `🔗<class_float_operator_lt_int>`

Returns `true` if this **float** is less than the given `int<class_int>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<=**(right: `float<class_float>`) `🔗<class_float_operator_lte_float>`

Returns `true` if the left float is less than or equal to the right one.

**Note:** `@GDScript.NAN<class_@GDScript_constant_NAN>` doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \<=**(right: `int<class_int>`) `🔗<class_float_operator_lte_int>`

Returns `true` if this **float** is less than or equal to the given `int<class_int>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `float<class_float>`) `🔗<class_float_operator_eq_float>`

Returns `true` if both floats are exactly equal.

**Note:** Due to floating-point precision errors, consider using `@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` or `@GlobalScope.is_zero_approx()<class_@GlobalScope_method_is_zero_approx>` instead, which are more reliable.

**Note:** `@GDScript.NAN<class_@GDScript_constant_NAN>` doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `int<class_int>`) `🔗<class_float_operator_eq_int>`

Returns `true` if the **float** and the given `int<class_int>` are equal.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>**(right: `float<class_float>`) `🔗<class_float_operator_gt_float>`

Returns `true` if the left float is greater than the right one.

**Note:** `@GDScript.NAN<class_@GDScript_constant_NAN>` doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>**(right: `int<class_int>`) `🔗<class_float_operator_gt_int>`

Returns `true` if this **float** is greater than the given `int<class_int>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>=**(right: `float<class_float>`) `🔗<class_float_operator_gte_float>`

Returns `true` if the left float is greater than or equal to the right one.

**Note:** `@GDScript.NAN<class_@GDScript_constant_NAN>` doesn't behave the same as other numbers. Therefore, the results from this operator may not be accurate if NaNs are included.

classref-item-separator

classref-operator

`bool<class_bool>` **operator \>=**(right: `int<class_int>`) `🔗<class_float_operator_gte_int>`

Returns `true` if this **float** is greater than or equal to the given `int<class_int>`.

classref-item-separator

classref-operator

`float<class_float>` **operator unary+**() `🔗<class_float_operator_unplus>`

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

classref-item-separator

classref-operator

`float<class_float>` **operator unary-**() `🔗<class_float_operator_unminus>`

Returns the negative value of the **float**. If positive, turns the number negative. If negative, turns the number positive. With floats, the number zero can be either positive or negative.