github_url
hide

# CollisionShape2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A node that provides a `Shape2D<class_Shape2D>` to a `CollisionObject2D<class_CollisionObject2D>` parent.

classref-introduction-group

## Description

A node that provides a `Shape2D<class_Shape2D>` to a `CollisionObject2D<class_CollisionObject2D>` parent and allows it to be edited. This can give a detection shape to an `Area2D<class_Area2D>` or turn a `PhysicsBody2D<class_PhysicsBody2D>` into a solid object.

classref-introduction-group

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`
- [2D Dodge The Creeps Demo](https://godotengine.org/asset-library/asset/2712)
- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
- [2D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2719)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **debug_color** = `Color(0, 0, 0, 0)` `🔗<class_CollisionShape2D_property_debug_color>`

classref-property-setget

- `void (No return value.)` **set_debug_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_debug_color**()

The collision shape color that is displayed in the editor, or in the running project if **Debug \> Visible Collision Shapes** is checked at the top of the editor.

**Note:** The default value is `ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>`. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

classref-item-separator

classref-property

`bool<class_bool>` **disabled** = `false` `🔗<class_CollisionShape2D_property_disabled>`

classref-property-setget

- `void (No return value.)` **set_disabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_disabled**()

A disabled collision shape has no effect in the world. This property should be changed with `Object.set_deferred()<class_Object_method_set_deferred>`.

classref-item-separator

classref-property

`bool<class_bool>` **one_way_collision** = `false` `🔗<class_CollisionShape2D_property_one_way_collision>`

classref-property-setget

- `void (No return value.)` **set_one_way_collision**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_one_way_collision_enabled**()

Sets whether this collision shape should only detect collision on one side (top or bottom).

**Note:** This property has no effect if this **CollisionShape2D** is a child of an `Area2D<class_Area2D>` node.

**Note:** The one way collision direction can be configured by setting `one_way_collision_direction<class_CollisionShape2D_property_one_way_collision_direction>`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **one_way_collision_direction** = `Vector2(0, 1)` `🔗<class_CollisionShape2D_property_one_way_collision_direction>`

classref-property-setget

- `void (No return value.)` **set_one_way_collision_direction**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_one_way_collision_direction**()

The direction used for one-way collision.

classref-item-separator

classref-property

`float<class_float>` **one_way_collision_margin** = `1.0` `🔗<class_CollisionShape2D_property_one_way_collision_margin>`

classref-property-setget

- `void (No return value.)` **set_one_way_collision_margin**(value: `float<class_float>`)
- `float<class_float>` **get_one_way_collision_margin**()

The margin used for one-way collision (in pixels). Higher values will make the shape thicker, and work better for colliders that enter the shape at a high velocity.

classref-item-separator

classref-property

`Shape2D<class_Shape2D>` **shape** `🔗<class_CollisionShape2D_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Shape2D<class_Shape2D>`)
- `Shape2D<class_Shape2D>` **get_shape**()

The actual shape owned by this collision shape.