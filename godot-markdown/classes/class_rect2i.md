github_url
hide

# Rect2i

A 2D axis-aligned bounding box using integer coordinates.

classref-introduction-group

## Description

The **Rect2i** built-in `Variant<class_Variant>` type represents an axis-aligned rectangle in a 2D space, using integer coordinates. It is defined by its `position<class_Rect2i_property_position>` and `size<class_Rect2i_property_size>`, which are `Vector2i<class_Vector2i>`. Because it does not rotate, it is frequently used for fast overlap tests (see `intersects()<class_Rect2i_method_intersects>`).

For floating-point coordinates, see `Rect2<class_Rect2>`.

**Note:** Negative values for `size<class_Rect2i_property_size>` are not supported. With negative size, most **Rect2i** methods do not work correctly. Use `abs()<class_Rect2i_method_abs>` to get an equivalent **Rect2i** with a non-negative size.

**Note:** In a boolean context, a **Rect2i** evaluates to `false` if both `position<class_Rect2i_property_position>` and `size<class_Rect2i_property_size>` are zero (equal to `Vector2i.ZERO<class_Vector2i_constant_ZERO>`). Otherwise, it always evaluates to `true`.

> [!NOTE]
> There are notable differences when using this API with C#. See `doc_c_sharp_differences` for more information.

classref-introduction-group

## Tutorials

- `Math documentation index <../tutorials/math/index>`
- `Vector math <../tutorials/math/vector_math>`

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

## Property Descriptions

classref-property

`Vector2i<class_Vector2i>` **end** = `Vector2i(0, 0)` `🔗<class_Rect2i_property_end>`

The ending point. This is usually the bottom-right corner of the rectangle, and is equivalent to `position + size`. Setting this point affects the `size<class_Rect2i_property_size>`.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **position** = `Vector2i(0, 0)` `🔗<class_Rect2i_property_position>`

The origin point. This is usually the top-left corner of the rectangle.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **size** = `Vector2i(0, 0)` `🔗<class_Rect2i_property_size>`

The rectangle's width and height, starting from `position<class_Rect2i_property_position>`. Setting this value also affects the `end<class_Rect2i_property_end>` point.

**Note:** It's recommended setting the width and height to non-negative values, as most methods in Godot assume that the `position<class_Rect2i_property_position>` is the top-left corner, and the `end<class_Rect2i_property_end>` is the bottom-right corner. To get an equivalent rectangle with non-negative size, use `abs()<class_Rect2i_method_abs>`.

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`Rect2i<class_Rect2i>` **Rect2i**() `🔗<class_Rect2i_constructor_Rect2i>`

Constructs a **Rect2i** with its `position<class_Rect2i_property_position>` and `size<class_Rect2i_property_size>` set to `Vector2i.ZERO<class_Vector2i_constant_ZERO>`.

classref-item-separator

classref-constructor

`Rect2i<class_Rect2i>` **Rect2i**(from: `Rect2i<class_Rect2i>`)

Constructs a **Rect2i** as a copy of the given **Rect2i**.

classref-item-separator

classref-constructor

`Rect2i<class_Rect2i>` **Rect2i**(from: `Rect2<class_Rect2>`)

Constructs a **Rect2i** from a `Rect2<class_Rect2>`. The floating-point coordinates are truncated.

classref-item-separator

classref-constructor

`Rect2i<class_Rect2i>` **Rect2i**(position: `Vector2i<class_Vector2i>`, size: `Vector2i<class_Vector2i>`)

Constructs a **Rect2i** by `position` and `size`.

classref-item-separator

classref-constructor

`Rect2i<class_Rect2i>` **Rect2i**(x: `int<class_int>`, y: `int<class_int>`, width: `int<class_int>`, height: `int<class_int>`)

Constructs a **Rect2i** by setting its `position<class_Rect2i_property_position>` to (`x`, `y`), and its `size<class_Rect2i_property_size>` to (`width`, `height`).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Rect2i<class_Rect2i>` **abs**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_abs>`

Returns a **Rect2i** equivalent to this rectangle, with its width and height modified to be non-negative values, and with its `position<class_Rect2i_property_position>` being the top-left corner of the rectangle.

gdscript

var rect = Rect2i(25, 25, -100, -50) var absolute = rect.abs() \# absolute is Rect2i(-75, -25, 100, 50)

csharp

var rect = new Rect2I(25, 25, -100, -50); var absolute = rect.Abs(); // absolute is Rect2I(-75, -25, 100, 50)

**Note:** It's recommended to use this method when `size<class_Rect2i_property_size>` is negative, as most other methods in Godot assume that the `position<class_Rect2i_property_position>` is the top-left corner, and the `end<class_Rect2i_property_end>` is the bottom-right corner.

classref-item-separator

classref-method

`bool<class_bool>` **encloses**(b: `Rect2i<class_Rect2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_encloses>`

Returns `true` if this **Rect2i** completely encloses another one.

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **expand**(to: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_expand>`

Returns a copy of this rectangle expanded to align the edges with the given `to` point, if necessary.

gdscript

var rect = Rect2i(0, 0, 5, 2)

rect = rect.expand(Vector2i(10, 0)) \# rect is Rect2i(0, 0, 10, 2) rect = rect.expand(Vector2i(-5, 5)) \# rect is Rect2i(-5, 0, 15, 5)

csharp

var rect = new Rect2I(0, 0, 5, 2);

rect = rect.Expand(new Vector2I(10, 0)); // rect is Rect2I(0, 0, 10, 2) rect = rect.Expand(new Vector2I(-5, 5)); // rect is Rect2I(-5, 0, 15, 5)

classref-item-separator

classref-method

`int<class_int>` **get_area**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_get_area>`

Returns the rectangle's area. This is equivalent to `size.x * size.y`. See also `has_area()<class_Rect2i_method_has_area>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_center**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_get_center>`

Returns the center point of the rectangle. This is the same as `position + (size / 2)`.

**Note:** If the `size<class_Rect2i_property_size>` is odd, the result will be rounded towards `position<class_Rect2i_property_position>`.

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **grow**(amount: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_grow>`

Returns a copy of this rectangle extended on all sides by the given `amount`. A negative `amount` shrinks the rectangle instead. See also `grow_individual()<class_Rect2i_method_grow_individual>` and `grow_side()<class_Rect2i_method_grow_side>`.

gdscript

var a = Rect2i(4, 4, 8, 8).grow(4) \# a is Rect2i(0, 0, 16, 16) var b = Rect2i(0, 0, 8, 4).grow(2) \# b is Rect2i(-2, -2, 12, 8)

csharp

var a = new Rect2I(4, 4, 8, 8).Grow(4); // a is Rect2I(0, 0, 16, 16) var b = new Rect2I(0, 0, 8, 4).Grow(2); // b is Rect2I(-2, -2, 12, 8)

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **grow_individual**(left: `int<class_int>`, top: `int<class_int>`, right: `int<class_int>`, bottom: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_grow_individual>`

Returns a copy of this rectangle with its `left`, `top`, `right`, and `bottom` sides extended by the given amounts. Negative values shrink the sides, instead. See also `grow()<class_Rect2i_method_grow>` and `grow_side()<class_Rect2i_method_grow_side>`.

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **grow_side**(side: `int<class_int>`, amount: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_grow_side>`

Returns a copy of this rectangle with its `side` extended by the given `amount` (see `Side<enum_@GlobalScope_Side>` constants). A negative `amount` shrinks the rectangle, instead. See also `grow()<class_Rect2i_method_grow>` and `grow_individual()<class_Rect2i_method_grow_individual>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_area**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_has_area>`

Returns `true` if this rectangle has positive width and height. See also `get_area()<class_Rect2i_method_get_area>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_point**(point: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_has_point>`

Returns `true` if the rectangle contains the given `point`. By convention, points on the right and bottom edges are **not** included.

**Note:** This method is not reliable for **Rect2i** with a *negative* `size<class_Rect2i_property_size>`. Use `abs()<class_Rect2i_method_abs>` first to get a valid rectangle.

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **intersection**(b: `Rect2i<class_Rect2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_intersection>`

Returns the intersection between this rectangle and `b`. If the rectangles do not intersect, returns an empty **Rect2i**.

gdscript

var a = Rect2i(0, 0, 5, 10) var b = Rect2i(2, 0, 8, 4)

var c = a.intersection(b) \# c is Rect2i(2, 0, 3, 4)

csharp

var a = new Rect2I(0, 0, 5, 10); var b = new Rect2I(2, 0, 8, 4);

var c = rect1.Intersection(rect2); // c is Rect2I(2, 0, 3, 4)

**Note:** If you only need to know whether two rectangles are overlapping, use `intersects()<class_Rect2i_method_intersects>`, instead.

classref-item-separator

classref-method

`bool<class_bool>` **intersects**(b: `Rect2i<class_Rect2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_intersects>`

Returns `true` if this rectangle overlaps with the `b` rectangle. The edges of both rectangles are excluded.

classref-item-separator

classref-method

`Rect2i<class_Rect2i>` **merge**(b: `Rect2i<class_Rect2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Rect2i_method_merge>`

Returns a **Rect2i** that encloses both this rectangle and `b` around the edges. See also `encloses()<class_Rect2i_method_encloses>`.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `Rect2i<class_Rect2i>`) `🔗<class_Rect2i_operator_neq_Rect2i>`

Returns `true` if the `position<class_Rect2i_property_position>` or `size<class_Rect2i_property_size>` of both rectangles are not equal.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `Rect2i<class_Rect2i>`) `🔗<class_Rect2i_operator_eq_Rect2i>`

Returns `true` if both `position<class_Rect2i_property_position>` and `size<class_Rect2i_property_size>` of the rectangles are equal, respectively.