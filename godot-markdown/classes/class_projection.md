github_url
hide

# Projection

A 4×4 matrix for 3D projective transformations.

classref-introduction-group

## Description

A 4×4 matrix used for 3D projective transformations. It can represent transformations such as translation, rotation, scaling, shearing, and perspective division. It consists of four `Vector4<class_Vector4>` columns.

For purely linear transformations (translation, rotation, and scale), it is recommended to use `Transform3D<class_Transform3D>`, as it is more performant and requires less memory.

Used internally as `Camera3D<class_Camera3D>`'s projection matrix.

**Note:** In a boolean context, a projection will evaluate to `false` if it's equal to `IDENTITY<class_Projection_constant_IDENTITY>`. Otherwise, a projection will always evaluate to `true`.

> [!NOTE]
> There are notable differences when using this API with C#. See `doc_c_sharp_differences` for more information.

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

enum **Planes**: `🔗<enum_Projection_Planes>`

classref-enumeration-constant

`Planes<enum_Projection_Planes>` **PLANE_NEAR** = `0`

The index value of the projection's near clipping plane.

classref-enumeration-constant

`Planes<enum_Projection_Planes>` **PLANE_FAR** = `1`

The index value of the projection's far clipping plane.

classref-enumeration-constant

`Planes<enum_Projection_Planes>` **PLANE_LEFT** = `2`

The index value of the projection's left clipping plane.

classref-enumeration-constant

`Planes<enum_Projection_Planes>` **PLANE_TOP** = `3`

The index value of the projection's top clipping plane.

classref-enumeration-constant

`Planes<enum_Projection_Planes>` **PLANE_RIGHT** = `4`

The index value of the projection's right clipping plane.

classref-enumeration-constant

`Planes<enum_Projection_Planes>` **PLANE_BOTTOM** = `5`

The index value of the projection bottom clipping plane.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**IDENTITY** = `Projection(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)` `🔗<class_Projection_constant_IDENTITY>`

A **Projection** with no transformation defined. When applied to other data structures, no transformation is performed.

classref-constant

**ZERO** = `Projection(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)` `🔗<class_Projection_constant_ZERO>`

A **Projection** with all values initialized to 0. When applied to other data structures, they will be zeroed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector4<class_Vector4>` **w** = `Vector4(0, 0, 0, 1)` `🔗<class_Projection_property_w>`

The projection matrix's W vector (column 3). Equivalent to array index `3`.

classref-item-separator

classref-property

`Vector4<class_Vector4>` **x** = `Vector4(1, 0, 0, 0)` `🔗<class_Projection_property_x>`

The projection matrix's X vector (column 0). Equivalent to array index `0`.

classref-item-separator

classref-property

`Vector4<class_Vector4>` **y** = `Vector4(0, 1, 0, 0)` `🔗<class_Projection_property_y>`

The projection matrix's Y vector (column 1). Equivalent to array index `1`.

classref-item-separator

classref-property

`Vector4<class_Vector4>` **z** = `Vector4(0, 0, 1, 0)` `🔗<class_Projection_property_z>`

The projection matrix's Z vector (column 2). Equivalent to array index `2`.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Projection<class_Projection>` **Projection**() `🔗<class_Projection_constructor_Projection>`

Constructs a default-initialized **Projection** identical to `IDENTITY<class_Projection_constant_IDENTITY>`.

**Note:** In C#, this constructs a **Projection** identical to `ZERO<class_Projection_constant_ZERO>`.

classref-item-separator

classref-constructor

`Projection<class_Projection>` **Projection**(from: `Projection<class_Projection>`)

Constructs a **Projection** as a copy of the given **Projection**.

classref-item-separator

classref-constructor

`Projection<class_Projection>` **Projection**(from: `Transform3D<class_Transform3D>`)

Constructs a Projection as a copy of the given `Transform3D<class_Transform3D>`.

classref-item-separator

classref-constructor

`Projection<class_Projection>` **Projection**(x_axis: `Vector4<class_Vector4>`, y_axis: `Vector4<class_Vector4>`, z_axis: `Vector4<class_Vector4>`, w_axis: `Vector4<class_Vector4>`)

Constructs a Projection from four `Vector4<class_Vector4>` values (matrix columns).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Projection<class_Projection>` **create_depth_correction**(flip_y: `bool<class_bool>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_depth_correction>`

Creates a new **Projection** that projects positions from a depth range of `-1` to `1` to one that ranges from `0` to `1`, and flips the projected positions vertically, according to `flip_y`.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_fit_aabb**(aabb: `AABB<class_AABB>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_fit_aabb>`

Creates a new **Projection** that scales a given projection to fit around a given `AABB<class_AABB>` in projection space.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_for_hmd**(eye: `int<class_int>`, aspect: `float<class_float>`, intraocular_dist: `float<class_float>`, display_width: `float<class_float>`, display_to_lens: `float<class_float>`, oversample: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_for_hmd>`

Creates a new **Projection** for projecting positions onto a head-mounted display with the given X:Y aspect ratio, distance between eyes, display width, distance to lens, oversampling factor, and depth clipping planes.

`eye` creates the projection for the left eye when set to 1, or the right eye when set to 2.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_frustum**(left: `float<class_float>`, right: `float<class_float>`, bottom: `float<class_float>`, top: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_frustum>`

Creates a new **Projection** that projects positions in a frustum with the given clipping planes.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_frustum_aspect**(size: `float<class_float>`, aspect: `float<class_float>`, offset: `Vector2<class_Vector2>`, z_near: `float<class_float>`, z_far: `float<class_float>`, flip_fov: `bool<class_bool>` = false) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_frustum_aspect>`

Creates a new **Projection** that projects positions in a frustum with the given size, X:Y aspect ratio, offset, and clipping planes.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_light_atlas_rect**(rect: `Rect2<class_Rect2>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_light_atlas_rect>`

Creates a new **Projection** that projects positions into the given `Rect2<class_Rect2>`.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_orthogonal**(left: `float<class_float>`, right: `float<class_float>`, bottom: `float<class_float>`, top: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_orthogonal>`

Creates a new **Projection** that projects positions using an orthogonal projection with the given clipping planes.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_orthogonal_aspect**(size: `float<class_float>`, aspect: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`, flip_fov: `bool<class_bool>` = false) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_orthogonal_aspect>`

Creates a new **Projection** that projects positions using an orthogonal projection with the given size, X:Y aspect ratio, and clipping planes.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_perspective**(fovy: `float<class_float>`, aspect: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`, flip_fov: `bool<class_bool>` = false) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_perspective>`

Creates a new **Projection** that projects positions using a perspective projection with the given Y-axis field of view (in degrees), X:Y aspect ratio, and clipping planes.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

classref-item-separator

classref-method

`Projection<class_Projection>` **create_perspective_hmd**(fovy: `float<class_float>`, aspect: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`, flip_fov: `bool<class_bool>`, eye: `int<class_int>`, intraocular_dist: `float<class_float>`, convergence_dist: `float<class_float>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_create_perspective_hmd>`

Creates a new **Projection** that projects positions using a perspective projection with the given Y-axis field of view (in degrees), X:Y aspect ratio, and clipping distances. The projection is adjusted for a head-mounted display with the given distance between eyes and distance to a point that can be focused on.

`eye` creates the projection for the left eye when set to 1, or the right eye when set to 2.

`flip_fov` determines whether the projection's field of view is flipped over its diagonal.

classref-item-separator

classref-method

`float<class_float>` **determinant**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_determinant>`

Returns a scalar value that is the signed factor by which areas are scaled by this matrix. If the sign is negative, the matrix flips the orientation of the area.

The determinant can be used to calculate the invertibility of a matrix or solve linear systems of equations involving the matrix, among other applications.

classref-item-separator

classref-method

`Projection<class_Projection>` **flipped_y**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_flipped_y>`

Returns a copy of this **Projection** with the signs of the values of the Y column flipped.

classref-item-separator

classref-method

`float<class_float>` **get_aspect**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_aspect>`

Returns the X:Y aspect ratio of this **Projection**'s viewport.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_far_plane_half_extents**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_far_plane_half_extents>`

Returns the dimensions of the far clipping plane of the projection, divided by two.

classref-item-separator

classref-method

`float<class_float>` **get_fov**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_fov>`

Returns the horizontal field of view of the projection (in degrees).

classref-item-separator

classref-method

`float<class_float>` **get_fovy**(fovx: `float<class_float>`, aspect: `float<class_float>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Projection_method_get_fovy>`

Returns the vertical field of view of the projection (in degrees) associated with the given horizontal field of view (in degrees) and aspect ratio.

**Note:** Unlike most methods of **Projection**, `aspect` is expected to be 1 divided by the X:Y aspect ratio.

classref-item-separator

classref-method

`float<class_float>` **get_lod_multiplier**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_lod_multiplier>`

Returns the factor by which the visible level of detail is scaled by this **Projection**.

classref-item-separator

classref-method

`int<class_int>` **get_pixels_per_meter**(for_pixel_width: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_pixels_per_meter>`

Returns `for_pixel_width` divided by the viewport's width measured in meters on the near plane, after this **Projection** is applied.

classref-item-separator

classref-method

`Plane<class_Plane>` **get_projection_plane**(plane: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_projection_plane>`

Returns the clipping plane of this **Projection** whose index is given by `plane`.

`plane` should be equal to one of `PLANE_NEAR<class_Projection_constant_PLANE_NEAR>`, `PLANE_FAR<class_Projection_constant_PLANE_FAR>`, `PLANE_LEFT<class_Projection_constant_PLANE_LEFT>`, `PLANE_TOP<class_Projection_constant_PLANE_TOP>`, `PLANE_RIGHT<class_Projection_constant_PLANE_RIGHT>`, or `PLANE_BOTTOM<class_Projection_constant_PLANE_BOTTOM>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_viewport_half_extents**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_viewport_half_extents>`

Returns the dimensions of the viewport plane that this **Projection** projects positions onto, divided by two.

classref-item-separator

classref-method

`float<class_float>` **get_z_far**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_z_far>`

Returns the distance for this **Projection** beyond which positions are clipped.

classref-item-separator

classref-method

`float<class_float>` **get_z_near**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_get_z_near>`

Returns the distance for this **Projection** before which positions are clipped.

classref-item-separator

classref-method

`Projection<class_Projection>` **inverse**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_inverse>`

Returns a **Projection** that performs the inverse of this **Projection**'s projective transformation.

classref-item-separator

classref-method

`bool<class_bool>` **is_orthogonal**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_is_orthogonal>`

Returns `true` if this **Projection** performs an orthogonal projection.

classref-item-separator

classref-method

`Projection<class_Projection>` **jitter_offseted**(offset: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_jitter_offseted>`

Returns a **Projection** with the X and Y values from the given `Vector2<class_Vector2>` added to the first and second values of the final column respectively.

classref-item-separator

classref-method

`Projection<class_Projection>` **perspective_znear_adjusted**(new_znear: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Projection_method_perspective_znear_adjusted>`

Returns a **Projection** with the near clipping distance adjusted to be `new_znear`.

**Note:** The original **Projection** must be a perspective projection.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Projection<class_Projection>`) `🔗<class_Projection_operator_neq_Projection>`

Returns `true` if the projections are not equal.

**Note:** Due to floating-point precision errors, this may return `true`, even if the projections are virtually equal. An `is_equal_approx` method may be added in a future version of Godot.

classref-item-separator

classref-operator

`Projection<class_Projection>` **operator**\*(right: `Projection<class_Projection>`) `🔗<class_Projection_operator_mul_Projection>`

Returns a **Projection** that applies the combined transformations of this **Projection** and `right`.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator**\*(right: `Vector4<class_Vector4>`) `🔗<class_Projection_operator_mul_Vector4>`

Projects (multiplies) the given `Vector4<class_Vector4>` by this **Projection** matrix.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Projection<class_Projection>`) `🔗<class_Projection_operator_eq_Projection>`

Returns `true` if the projections are equal.

**Note:** Due to floating-point precision errors, this may return `false`, even if the projections are virtually equal. An `is_equal_approx` method may be added in a future version of Godot.

classref-item-separator

classref-operator

`Vector4<class_Vector4>` **operator \[\]**(index: `int<class_int>`) `🔗<class_Projection_operator_idx_int>`

Returns the column of the **Projection** with the given index.

Indices are in the following order: x, y, z, w.