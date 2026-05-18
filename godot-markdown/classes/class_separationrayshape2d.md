github_url
hide

# SeparationRayShape2D

**Inherits:** `Shape2D<class_Shape2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 2D ray shape used for physics collision that tries to separate itself from any collider.

classref-introduction-group

## Description

A 2D ray shape, intended for use in physics. Usually used to provide a shape for a `CollisionShape2D<class_CollisionShape2D>`. When a **SeparationRayShape2D** collides with an object, it tries to separate itself from it by moving its endpoint to the collision point. For example, a **SeparationRayShape2D** next to a character can allow it to instantly move up when touching stairs.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **length** = `20.0` `🔗<class_SeparationRayShape2D_property_length>`

classref-property-setget

- `void (No return value.)` **set_length**(value: `float<class_float>`)
- `float<class_float>` **get_length**()

The ray's length.

classref-item-separator

classref-property

`bool<class_bool>` **slide_on_slope** = `false` `🔗<class_SeparationRayShape2D_property_slide_on_slope>`

classref-property-setget

- `void (No return value.)` **set_slide_on_slope**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_slide_on_slope**()

If `false` (default), the shape always separates and returns a normal along its own direction.

If `true`, the shape can return the correct normal and separate in any direction, allowing sliding motion on slopes.