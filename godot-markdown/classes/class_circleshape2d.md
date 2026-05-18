github_url
hide

# CircleShape2D

**Inherits:** `Shape2D<class_Shape2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 2D circle shape used for physics collision.

classref-introduction-group

## Description

A 2D circle shape, intended for use in physics. Usually used to provide a shape for a `CollisionShape2D<class_CollisionShape2D>`.

**Performance:** **CircleShape2D** is fast to check collisions against. It is faster than `RectangleShape2D<class_RectangleShape2D>` and `CapsuleShape2D<class_CapsuleShape2D>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **radius** = `10.0` `🔗<class_CircleShape2D_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

The circle's radius.