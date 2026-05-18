github_url
hide

# CollisionShape3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A node that provides a `Shape3D<class_Shape3D>` to a `CollisionObject3D<class_CollisionObject3D>` parent.

classref-introduction-group

## Description

A node that provides a `Shape3D<class_Shape3D>` to a `CollisionObject3D<class_CollisionObject3D>` parent and allows it to be edited. This can give a detection shape to an `Area3D<class_Area3D>` or turn a `PhysicsBody3D<class_PhysicsBody3D>` into a solid object.

**Warning:** A non-uniformly scaled **CollisionShape3D** will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its `shape<class_CollisionShape3D_property_shape>` resource instead.

classref-introduction-group

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`
- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **debug_color** = `Color(0, 0, 0, 0)` `🔗<class_CollisionShape3D_property_debug_color>`

classref-property-setget

- `void (No return value.)` **set_debug_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_debug_color**()

The collision shape color that is displayed in the editor, or in the running project if **Debug \> Visible Collision Shapes** is checked at the top of the editor.

**Note:** The default value is `ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>`. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

classref-item-separator

classref-property

`bool<class_bool>` **debug_fill** = `true` `🔗<class_CollisionShape3D_property_debug_fill>`

classref-property-setget

- `void (No return value.)` **set_enable_debug_fill**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_enable_debug_fill**()

If `true`, when the shape is displayed, it will show a solid fill color in addition to its wireframe.

classref-item-separator

classref-property

`bool<class_bool>` **disabled** = `false` `🔗<class_CollisionShape3D_property_disabled>`

classref-property-setget

- `void (No return value.)` **set_disabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_disabled**()

A disabled collision shape has no effect in the world. This property should be changed with `Object.set_deferred()<class_Object_method_set_deferred>`.

classref-item-separator

classref-property

`Shape3D<class_Shape3D>` **shape** `🔗<class_CollisionShape3D_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Shape3D<class_Shape3D>`)
- `Shape3D<class_Shape3D>` **get_shape**()

The actual shape owned by this collision shape.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **make_convex_from_siblings**() `🔗<class_CollisionShape3D_method_make_convex_from_siblings>`

Sets the collision shape's shape to the addition of all its convexed `MeshInstance3D<class_MeshInstance3D>` siblings geometry.

classref-item-separator

classref-method

`void (No return value.)` **resource_changed**(resource: `Resource<class_Resource>`) `🔗<class_CollisionShape3D_method_resource_changed>`

**Deprecated:** Use `Resource.changed<class_Resource_signal_changed>` instead.

This method does nothing.