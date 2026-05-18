github_url
hide

# CollisionPolygon3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A node that provides a thickened polygon shape (a prism) to a `CollisionObject3D<class_CollisionObject3D>` parent.

classref-introduction-group

## Description

A node that provides a thickened polygon shape (a prism) to a `CollisionObject3D<class_CollisionObject3D>` parent and allows it to be edited. The polygon can be concave or convex. This can give a detection shape to an `Area3D<class_Area3D>` or turn a `PhysicsBody3D<class_PhysicsBody3D>` into a solid object.

**Warning:** A non-uniformly scaled `CollisionShape3D<class_CollisionShape3D>` will likely not behave as expected. Make sure to keep its scale the same on all axes and adjust its shape resource instead.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **debug_color** = `Color(0, 0, 0, 0)` `🔗<class_CollisionPolygon3D_property_debug_color>`

classref-property-setget

- `void (No return value.)` **set_debug_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_debug_color**()

The collision shape color that is displayed in the editor, or in the running project if **Debug \> Visible Collision Shapes** is checked at the top of the editor.

**Note:** The default value is `ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>`. The `Color(0, 0, 0, 0)` value documented here is a placeholder, and not the actual default debug color.

classref-item-separator

classref-property

`bool<class_bool>` **debug_fill** = `true` `🔗<class_CollisionPolygon3D_property_debug_fill>`

classref-property-setget

- `void (No return value.)` **set_enable_debug_fill**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_enable_debug_fill**()

If `true`, when the shape is displayed, it will show a solid fill color in addition to its wireframe.

classref-item-separator

classref-property

`float<class_float>` **depth** = `1.0` `🔗<class_CollisionPolygon3D_property_depth>`

classref-property-setget

- `void (No return value.)` **set_depth**(value: `float<class_float>`)
- `float<class_float>` **get_depth**()

Length that the resulting collision extends in either direction perpendicular to its 2D polygon.

classref-item-separator

classref-property

`bool<class_bool>` **disabled** = `false` `🔗<class_CollisionPolygon3D_property_disabled>`

classref-property-setget

- `void (No return value.)` **set_disabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_disabled**()

If `true`, no collision will be produced. This property should be changed with `Object.set_deferred()<class_Object_method_set_deferred>`.

classref-item-separator

classref-property

`float<class_float>` **margin** = `0.04` `🔗<class_CollisionPolygon3D_property_margin>`

classref-property-setget

- `void (No return value.)` **set_margin**(value: `float<class_float>`)
- `float<class_float>` **get_margin**()

The collision margin for the generated `Shape3D<class_Shape3D>`. See `Shape3D.margin<class_Shape3D_property_margin>` for more details.

classref-item-separator

classref-property

`PackedVector2Array<class_PackedVector2Array>` **polygon** = `PackedVector2Array()` `🔗<class_CollisionPolygon3D_property_polygon>`

classref-property-setget

- `void (No return value.)` **set_polygon**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_polygon**()

Array of vertices which define the 2D polygon in the local XY plane.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.