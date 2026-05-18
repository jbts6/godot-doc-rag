github_url
hide

# Plane

A plane in Hessian normal form.

classref-introduction-group

## Description

Represents a normalized plane equation. `normal<class_Plane_property_normal>` is the normal of the plane (a, b, c normalized), and `d<class_Plane_property_d>` is the distance from the origin to the plane (in the direction of "normal"). "Over" or "Above" the plane is considered the side of the plane towards where the normal is pointing.

**Note:** In a boolean context, a plane will evaluate to `false` if all its components equal `0`. Otherwise, a plane will always evaluate to `true`.

classref-introduction-group

## Tutorials

- `Math documentation index <../tutorials/math/index>`

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

**PLANE_YZ** = `Plane(1, 0, 0, 0)` `🔗<class_Plane_constant_PLANE_YZ>`

A plane that extends in the Y and Z axes (normal vector points +X).

classref-constant

**PLANE_XZ** = `Plane(0, 1, 0, 0)` `🔗<class_Plane_constant_PLANE_XZ>`

A plane that extends in the X and Z axes (normal vector points +Y).

classref-constant

**PLANE_XY** = `Plane(0, 0, 1, 0)` `🔗<class_Plane_constant_PLANE_XY>`

A plane that extends in the X and Y axes (normal vector points +Z).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **d** = `0.0` `🔗<class_Plane_property_d>`

The distance from the origin to the plane, expressed in terms of `normal<class_Plane_property_normal>` (according to its direction and magnitude). Actual absolute distance from the origin to the plane can be calculated as `abs(d) / normal.length()` (if `normal<class_Plane_property_normal>` has zero length then this **Plane** does not represent a valid plane).

In the scalar equation of the plane `ax + by + cz = d`, this is `d`, while the `(a, b, c)` coordinates are represented by the `normal<class_Plane_property_normal>` property.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **normal** = `Vector3(0, 0, 0)` `🔗<class_Plane_property_normal>`

The normal of the plane, typically a unit vector. Shouldn't be a zero vector as **Plane** with such `normal<class_Plane_property_normal>` does not represent a valid plane.

In the scalar equation of the plane `ax + by + cz = d`, this is the vector `(a, b, c)`, where `d` is the `d<class_Plane_property_d>` property.

classref-item-separator

classref-property

`float<class_float>` **x** = `0.0` `🔗<class_Plane_property_x>`

The X component of the plane's `normal<class_Plane_property_normal>` vector.

classref-item-separator

classref-property

`float<class_float>` **y** = `0.0` `🔗<class_Plane_property_y>`

The Y component of the plane's `normal<class_Plane_property_normal>` vector.

classref-item-separator

classref-property

`float<class_float>` **z** = `0.0` `🔗<class_Plane_property_z>`

The Z component of the plane's `normal<class_Plane_property_normal>` vector.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Plane<class_Plane>` **Plane**() `🔗<class_Plane_constructor_Plane>`

Constructs a default-initialized **Plane** with all components set to `0`.

classref-item-separator

classref-constructor

`Plane<class_Plane>` **Plane**(from: `Plane<class_Plane>`)

Constructs a **Plane** as a copy of the given **Plane**.

classref-item-separator

classref-constructor

`Plane<class_Plane>` **Plane**(a: `float<class_float>`, b: `float<class_float>`, c: `float<class_float>`, d: `float<class_float>`)

Creates a plane from the four parameters. The three components of the resulting plane's `normal<class_Plane_property_normal>` are `a`, `b` and `c`, and the plane has a distance of `d` from the origin.

classref-item-separator

classref-constructor

`Plane<class_Plane>` **Plane**(normal: `Vector3<class_Vector3>`)

Creates a plane from the normal vector. The plane will intersect the origin.

The `normal` of the plane must be a unit vector.

classref-item-separator

classref-constructor

`Plane<class_Plane>` **Plane**(normal: `Vector3<class_Vector3>`, d: `float<class_float>`)

Creates a plane from the normal vector and the plane's distance from the origin.

The `normal` of the plane must be a unit vector.

classref-item-separator

classref-constructor

`Plane<class_Plane>` **Plane**(normal: `Vector3<class_Vector3>`, point: `Vector3<class_Vector3>`)

Creates a plane from the normal vector and a point on the plane.

The `normal` of the plane must be a unit vector.

classref-item-separator

classref-constructor

`Plane<class_Plane>` **Plane**(point1: `Vector3<class_Vector3>`, point2: `Vector3<class_Vector3>`, point3: `Vector3<class_Vector3>`)

Creates a plane from the three points, given in clockwise order.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **distance_to**(point: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_distance_to>`

Returns the shortest distance from the plane to the position `point`. If the point is above the plane, the distance will be positive. If below, the distance will be negative.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **get_center**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_get_center>`

Returns the center of the plane.

classref-item-separator

classref-method

`bool<class_bool>` **has_point**(point: `Vector3<class_Vector3>`, tolerance: `float<class_float>` = 1e-05) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_has_point>`

Returns `true` if `point` is inside the plane. Comparison uses a custom minimum `tolerance` threshold.

classref-item-separator

classref-method

`Variant<class_Variant>` **intersect_3**(b: `Plane<class_Plane>`, c: `Plane<class_Plane>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_intersect_3>`

Returns the intersection point of the three planes `b`, `c` and this plane. If no intersection is found, `null` is returned.

classref-item-separator

classref-method

`Variant<class_Variant>` **intersects_ray**(from: `Vector3<class_Vector3>`, dir: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_intersects_ray>`

Returns the intersection point of a ray consisting of the position `from` and the direction normal `dir` with this plane. If no intersection is found, `null` is returned.

classref-item-separator

classref-method

`Variant<class_Variant>` **intersects_segment**(from: `Vector3<class_Vector3>`, to: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_intersects_segment>`

Returns the intersection point of a segment from position `from` to position `to` with this plane. If no intersection is found, `null` is returned.

classref-item-separator

classref-method

`bool<class_bool>` **is_equal_approx**(to_plane: `Plane<class_Plane>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_is_equal_approx>`

Returns `true` if this plane and `to_plane` are approximately equal, by running `@GlobalScope.is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` on each component.

classref-item-separator

classref-method

`bool<class_bool>` **is_finite**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_is_finite>`

Returns `true` if this plane is finite, by calling `@GlobalScope.is_finite()<class_@GlobalScope_method_is_finite>` on each component.

classref-item-separator

classref-method

`bool<class_bool>` **is_point_over**(point: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_is_point_over>`

Returns `true` if `point` is located above the plane.

classref-item-separator

classref-method

`Plane<class_Plane>` **normalized**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_normalized>`

Returns a copy of the plane, with normalized `normal<class_Plane_property_normal>` (so it's a unit vector). Returns `Plane(0, 0, 0, 0)` if `normal<class_Plane_property_normal>` can't be normalized (it has zero length).

classref-item-separator

classref-method

`Vector3<class_Vector3>` **project**(point: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Plane_method_project>`

Returns the orthogonal projection of `point` into a point in the plane.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Plane<class_Plane>`) `🔗<class_Plane_operator_neq_Plane>`

Returns `true` if the planes are not equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Plane_method_is_equal_approx>` instead, which is more reliable.

classref-item-separator

classref-operator

`Plane<class_Plane>` **operator**\*(right: `Transform3D<class_Transform3D>`) `🔗<class_Plane_operator_mul_Transform3D>`

Inversely transforms (multiplies) the **Plane** by the given `Transform3D<class_Transform3D>` transformation matrix.

`plane * transform` is equivalent to `transform.affine_inverse() * plane`. See `Transform3D.affine_inverse()<class_Transform3D_method_affine_inverse>`.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Plane<class_Plane>`) `🔗<class_Plane_operator_eq_Plane>`

Returns `true` if the planes are exactly equal.

**Note:** Due to floating-point precision errors, consider using `is_equal_approx()<class_Plane_method_is_equal_approx>` instead, which is more reliable.

classref-item-separator

classref-operator

`Plane<class_Plane>` **operator unary+**() `🔗<class_Plane_operator_unplus>`

Returns the same value as if the `+` was not there. Unary `+` does nothing, but sometimes it can make your code more readable.

classref-item-separator

classref-operator

`Plane<class_Plane>` **operator unary-**() `🔗<class_Plane_operator_unminus>`

Returns the negative value of the **Plane**. This is the same as writing `Plane(-p.normal, -p.d)`. This operation flips the direction of the normal vector and also flips the distance value, resulting in a Plane that is in the same place, but facing the opposite direction.