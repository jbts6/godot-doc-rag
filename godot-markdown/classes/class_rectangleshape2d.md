github_url
hide

# RectangleShape2D

**Inherits:** `Shape2D<class_Shape2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 2D rectangle shape used for physics collision.

classref-introduction-group

## Description

A 2D rectangle shape, intended for use in physics. Usually used to provide a shape for a `CollisionShape2D<class_CollisionShape2D>`.

**Performance:** **RectangleShape2D** is fast to check collisions against. It is faster than `CapsuleShape2D<class_CapsuleShape2D>`, but slower than `CircleShape2D<class_CircleShape2D>`.

classref-introduction-group

## Tutorials

- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector2<class_Vector2>` **size** = `Vector2(20, 20)` `🔗<class_RectangleShape2D_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_size**()

The rectangle's width and height.