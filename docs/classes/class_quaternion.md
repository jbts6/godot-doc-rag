github_url
hide

# Quaternion

A unit quaternion used for representing 3D rotations.

classref-introduction-group

## Description

The **Quaternion** built-in `Variant<class_Variant>` type is a 4D data structure that represents rotation in the form of a [Hamilton convention quaternion](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation). Compared to the `Basis<class_Basis>` type which can store both rotation and scale, quaternions can *only* store rotation.

A **Quaternion** is composed by 4 floating-point components: `w<class_Quaternion_property_w>`, `x<class_Quaternion_property_x>`, `y<class_Quaternion_property_y>`, and `z<class_Quaternion_property_z>`. These components are very compact in memory, and because of this some operations are more efficient and less likely to cause floating-point errors. Methods such as `get_angle()<class_Quaternion_method_get_angle>`, `get_axis()<class_Quaternion_method_get_axis>`, and `slerp()<class_Quaternion_method_slerp>` are faster than their `Basis<class_Basis>` counterparts.

For a great introduction to quaternions, see [this video by 3Blue1Brown](https://www.youtube.com/watch?v=d4EgbgTm0Bg). You do not need to know the math behind quaternions, as Godot provides several helper methods that handle it for you. These include `slerp()<class_Quaternion_method_slerp>` and `spherical_cubic_interpolate()<class_Quaternion_method_spherical_cubic_interpolate>`, as well as the `*` operator.

**Note:** Quaternions must be normalized before being used for rotation (see `normalized()<class_Quaternion_method_normalized>`).

**Note:** Similarly to `Vector2<class_Vector2>` and `Vector3<class_Vector3>`, the components of a quaternion use 32-bit precision by default, unlike `float<class_float>` which is always 64-bit. If double precision is needed, compile the engine with the option `precision=double`.

**Note:** In a boolean context, a quaternion will evaluate to `false` if it's equal to `IDENTITY<class_Quaternion_constant_IDENTITY>`. Otherwise, a quaternion will always evaluate to `true`.

> [!NOTE]
> There are notable differences when using this API with C#. See `doc_c_sharp_differences` for more information.

classref-introduction-group

## Tutorials

- [3Blue1Brown's video on Quaternions](https://www.youtube.com/watch?v=d4EgbgTm0Bg)
- [Online Quaternion Visualization](https://quaternions.online/)
- [Using 3D transforms](../tutorials/3d/using_transforms.html#interpolating-with-quaternions)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)
- [Advanced Quaternion Visualization](https://iwatake2222.github.io/rotation_master/rotation_master.html)

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

## Constants

classref-constant

**IDENTITY** = `Quaternion(0, 0, 0, 1)` `🔗<class_Quaternion_constant_IDENTITY>`

The identity quaternion, representing no rotation. This has the same rotation as `Basis.IDENTITY<class_Basis_constant_IDENTITY>`.

If a `Vector3<class_Vector3>` is rotated (multiplied) by this quaternion, it does not change.

**Note:** In GDScript, this constant is equivalent to creating a `Quaternion<class_Quaternion_constructor_Quaternion>` without any arguments. It can be used to make your code clearer, and for consistency with C#.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **w** = `1.0` `🔗<class_Quaternion_property_w>`

W component of the quaternion. This is the "real" part.

**Note:** Quaternion components should usually not be manipulated directly.

classref-item-separator

classref-property

`float<class_float>` **x** = `0.0` `🔗<class_Quaternion_property_x>`

X component of the quaternion. This is the value along the "imaginary" `i` axis.

**Note:** Quaternion components should usually not be manipulated directly.

classref-item-separator

classref-property

`float<class_float>` **y** = `0.0` `🔗<class_Quaternion_property_y>`

Y component of the quaternion. This is the value along the "imaginary" `j` axis.

**Note:** Quaternion components should usually not be manipulated directly.

classref-item-separator

classref-property

`float<class_float>` **z** = `0.0` `🔗<class_Quaternion_property_z>`

Z component of the quaternion. This is the value along the "imaginary" `k` axis.

**Note:** Quaternion components should usually not be manipulated directly.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Quaternion<class_Quaternion>` **Quaternion**() `🔗<class_Quaternion_constructor_Quaternion>`

Constructs a **Quaternion** identical to `IDENTITY<class_Quaternion_constant_IDENTITY>`.

**Note:** In C#, this constructs a **Quaternion** with all of its components set to `0.0`.

classref-item-separator

classref-constructor

`Quaternion<class_Quaternion>` **Quaternion**(from: `Quaternion<class_Quaternion>`)

Constructs a **Quaternion** as a copy of the given **Quaternion**.

classref-item-separator

classref-constructor

`Quaternion<class_Quaternion>` **Quaternion**(arc_from: `Vector3<class_Vector3>`, arc_to: `Vector3<class_Vector3>`)

Constructs a **Quaternion** representing the shortest arc between `arc_from` and `arc_to`. These can be imagined as two points intersecting a sphere's surface, with a radius of `1.0`.

classref-item-separator

classref-constructor

`Quaternion<class_Quaternion>` **Quaternion**(axis: `Vector3<class_Vector3>`, angle: `float<class_float>`)

Constructs a **Quaternion** representing rotation around the `axis` by the given `angle`, in radians. The axis must be a normalized vector.

classref-item-separator

classref-constructor

`Quaternion<class_Quaternion>` **Quaternion**(from: `Basis<class_Basis>`)

Constructs a **Quaternion** from the given rotation `Basis<class_Basis>`.

This constructor is faster than `Basis.get_rotation_quaternion()<class_Basis_method_get_rotation_quaternion>`, but the given basis must be *orthonormalized* (see `Basis.orthonormalized()<class_Basis_method_orthonormalized>`). Otherwise, the constructor fails and returns `IDENTITY<class_Quaternion_constant_IDENTITY>`.

classref-item-separator

classref-constructor

`Quaternion<class_Quaternion>` **Quaternion**(x: `float<class_float>`, y: `float<class_float>`, z: `float<class_float>`, w: `float<class_float>`)

Constructs a **Quaternion** defined by the given values.

**Note:** Only normalized quaternions represent rotation; if these values are not normalized, the new **Quaternion** will not be a valid rotation.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **angle_to**(to: `Quaternion<class_Quaternion>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_angle_to>`

Returns the angle between this quaternion and `to`. This is the magnitude of the angle you would need to rotate by to get from one to the other.

**Note:** The magnitude of the floating-point error for this method is abnormally high, so methods such as `is_zero_approx` will not work reliably.

classref-item-separator

classref-method

`float<class_float>` **dot**(with: `Quaternion<class_Quaternion>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_dot>`

Returns the dot product between this quaternion and `with`.

This is equivalent to `(quat.x * with.x) + (quat.y * with.y) + (quat.z * with.z) + (quat.w * with.w)`.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **exp**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_exp>`

Returns the exponential of this quaternion. The rotation axis of the result is the normalized rotation axis of this quaternion, the angle of the result is the length of the vector part of this quaternion.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **from_euler**(euler: `Vector3<class_Vector3>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Quaternion_method_from_euler>`

Constructs a new **Quaternion** from the given `Vector3<class_Vector3>` of [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians. In Godot, Euler angles always use intrinsic order. This method always uses the intrinsic YXZ convention (`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`).

classref-item-separator

classref-method

`float<class_float>` **get_angle**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_get_angle>`

Returns the angle of the rotation represented by this quaternion.

**Note:** The quaternion must be normalized.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_axis**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_get_axis>`

Returns the rotation axis of the rotation represented by this quaternion.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_euler**(order: `int<class_int>` = 2) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_get_euler>`

Returns this quaternion's rotation as a `Vector3<class_Vector3>` of [Euler angles](https://en.wikipedia.org/wiki/Euler_angles), in radians.

The order of each consecutive rotation can be changed with `order` (see `EulerOrder<enum_@GlobalScope_EulerOrder>` constants). In Godot, Euler angles always use intrinsic order. By default, the intrinsic YXZ convention is used (`@GlobalScope.EULER_ORDER_YXZ<class_@GlobalScope_constant_EULER_ORDER_YXZ>`): since we are decomposing, local Z (roll) is calculated first, then local X (pitch), and lastly local Y (yaw). When using the opposite method `from_euler()<class_Quaternion_method_from_euler>` to compose a rotation, this order is reversed.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **inverse**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_inverse>`

Returns the inverse version of this quaternion, inverting the sign of every component except `w<class_Quaternion_property_w>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_equal_approx**(to: `Quaternion<class_Quaternion>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_is_equal_approx>`

Returns `true` if this quaternion and `to` are approximately equal, by calling `@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` on each component.

classref-item-separator

classref-method

`bool<class_bool>` **is_finite**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_is_finite>`

Returns `true` if this quaternion is finite, by calling `@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>` on each component.

classref-item-separator

classref-method

`bool<class_bool>` **is_normalized**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_is_normalized>`

Returns `true` if this quaternion is normalized. See also `normalized()<class_Quaternion_method_normalized>`.

classref-item-separator

classref-method

`float<class_float>` **length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_length>`

Returns this quaternion's length, also called magnitude.

classref-item-separator

classref-method

`float<class_float>` **length_squared**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_length_squared>`

Returns this quaternion's length, squared.

**Note:** This method is faster than `length()<class_Quaternion_method_length>`, so prefer it if you only need to compare quaternion lengths.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **log**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_log>`

Returns the logarithm of this quaternion. Multiplies this quaternion's rotation axis by its rotation angle, and stores the result in the returned quaternion's vector part (`x<class_Quaternion_property_x>`, `y<class_Quaternion_property_y>`, and `z<class_Quaternion_property_z>`). The returned quaternion's real part (`w<class_Quaternion_property_w>`) is always `0.0`.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **normalized**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_normalized>`

Returns a copy of this quaternion, normalized so that its length is `1.0`. See also `is_normalized()<class_Quaternion_method_is_normalized>`.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **slerp**(to: `Quaternion<class_Quaternion>`, weight: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_slerp>`

Performs a spherical-linear interpolation with the `to` quaternion, given a `weight` and returns the result. Both this quaternion and `to` must be normalized.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **slerpni**(to: `Quaternion<class_Quaternion>`, weight: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_slerpni>`

Performs a spherical-linear interpolation with the `to` quaternion, given a `weight` and returns the result. Unlike `slerp()<class_Quaternion_method_slerp>`, this method does not check if the rotation path is smaller than 90 degrees. Both this quaternion and `to` must be normalized.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **spherical_cubic_interpolate**(b: `Quaternion<class_Quaternion>`, pre_a: `Quaternion<class_Quaternion>`, post_b: `Quaternion<class_Quaternion>`, weight: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_spherical_cubic_interpolate>`

Performs a spherical cubic interpolation between quaternions `pre_a`, this vector, `b`, and `post_b`, by the given amount `weight`.

classref-item-separator

classref-method

`Quaternion<class_Quaternion>` **spherical_cubic_interpolate_in_time**(b: `Quaternion<class_Quaternion>`, pre_a: `Quaternion<class_Quaternion>`, post_b: `Quaternion<class_Quaternion>`, weight: `float<class_float>`, b_t: `float<class_float>`, pre_a_t: `float<class_float>`, post_b_t: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Quaternion_method_spherical_cubic_interpolate_in_time>`

Performs a spherical cubic interpolation between quaternions `pre_a`, this vector, `b`, and `post_b`, by the given amount `weight`.

It can perform smoother interpolation than `spherical_cubic_interpolate()<class_Quaternion_method_spherical_cubic_interpolate>` by the time values.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Quaternion<class_Quaternion>`) `🔗<class_Quaternion_operator_neq_Quaternion>`

Returns `true` if the components of both quaternions are not exactly equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Quaternion_method_is_equal_approx>` instead, which is more reliable.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator**\*(right: `Quaternion<class_Quaternion>`) `🔗<class_Quaternion_operator_mul_Quaternion>`

Composes (multiplies) two quaternions. This rotates the `right` quaternion (the child) by this quaternion (the parent).

classref-item-separator

classref-operator

`Vector3<class_Vector3>` **operator**\*(right: `Vector3<class_Vector3>`) `🔗<class_Quaternion_operator_mul_Vector3>`

Rotates (multiplies) the `right` vector by this quaternion, returning a `Vector3<class_Vector3>`.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator**\*(right: `float<class_float>`) `🔗<class_Quaternion_operator_mul_float>`

Multiplies each component of the **Quaternion** by the right `float<class_float>` value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator**\*(right: `int<class_int>`) `🔗<class_Quaternion_operator_mul_int>`

Multiplies each component of the **Quaternion** by the right `int<class_int>` value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator +**(right: `Quaternion<class_Quaternion>`) `🔗<class_Quaternion_operator_sum_Quaternion>`

Adds each component of the left **Quaternion** to the right **Quaternion**.

This operation is not meaningful on its own, but it can be used as a part of a larger expression, such as approximating an intermediate rotation between two nearby rotations.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator -**(right: `Quaternion<class_Quaternion>`) `🔗<class_Quaternion_operator_dif_Quaternion>`

Subtracts each component of the left **Quaternion** by the right **Quaternion**.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator /**(right: `float<class_float>`) `🔗<class_Quaternion_operator_div_float>`

Divides each component of the **Quaternion** by the right `float<class_float>` value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator /**(right: `int<class_int>`) `🔗<class_Quaternion_operator_div_int>`

Divides each component of the **Quaternion** by the right `int<class_int>` value.

This operation is not meaningful on its own, but it can be used as a part of a larger expression.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Quaternion<class_Quaternion>`) `🔗<class_Quaternion_operator_eq_Quaternion>`

Returns `true` if the components of both quaternions are exactly equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Quaternion_method_is_equal_approx>` instead, which is more reliable.

classref-item-separator

classref-operator

`float<class_float>` **operator \[\]**(index: `int<class_int>`) `🔗<class_Quaternion_operator_idx_int>`

Accesses each component of this quaternion by their index.

Index `0` is the same as `x<class_Quaternion_property_x>`, index `1` is the same as `y<class_Quaternion_property_y>`, index `2` is the same as `z<class_Quaternion_property_z>`, and index `3` is the same as `w<class_Quaternion_property_w>`.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator unary+**() `🔗<class_Quaternion_operator_unplus>`

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

classref-item-separator

classref-operator

`Quaternion<class_Quaternion>` **operator unary-**() `🔗<class_Quaternion_operator_unminus>`

Returns the negative value of the **Quaternion**. This is the same as multiplying all components by `-1`. This operation results in a quaternion that represents the same rotation.