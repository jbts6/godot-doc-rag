github_url
hide

# PhysicsShapeQueryParameters3D

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Provides parameters for `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`'s methods.

classref-introduction-group

## Description

By changing various properties of this object, such as the shape, you can configure the parameters for `PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`'s methods.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **collide_with_areas** = `false` `🔗<class_PhysicsShapeQueryParameters3D_property_collide_with_areas>`

classref-property-setget

- `void (No return value.)` **set_collide_with_areas**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collide_with_areas_enabled**()

If `true`, the query will take `Area3D<class_Area3D>`s into account.

classref-item-separator

classref-property

`bool<class_bool>` **collide_with_bodies** = `true` `🔗<class_PhysicsShapeQueryParameters3D_property_collide_with_bodies>`

classref-property-setget

- `void (No return value.)` **set_collide_with_bodies**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collide_with_bodies_enabled**()

If `true`, the query will take `PhysicsBody3D<class_PhysicsBody3D>`s into account.

classref-item-separator

classref-property

`int<class_int>` **collision_mask** = `4294967295` `🔗<class_PhysicsShapeQueryParameters3D_property_collision_mask>`

classref-property-setget

- `void (No return value.)` **set_collision_mask**(value: `int<class_int>`)
- `int<class_int>` **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. See [Collision layers and masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks) in the documentation for more information.

classref-item-separator

classref-property

`Array<class_Array>`\[`RID<class_RID>`\] **exclude** = `[]` `🔗<class_PhysicsShapeQueryParameters3D_property_exclude>`

classref-property-setget

- `void (No return value.)` **set_exclude**(value: `Array<class_Array>`\[`RID<class_RID>`\])
- `Array<class_Array>`\[`RID<class_RID>`\] **get_exclude**()

The list of object `RID<class_RID>`s that will be excluded from collisions. Use `CollisionObject3D.get_rid()<class_CollisionObject3D_method_get_rid>` to get the `RID<class_RID>` associated with a `CollisionObject3D<class_CollisionObject3D>`-derived node.

**Note:** The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.

classref-item-separator

classref-property

`float<class_float>` **margin** = `0.0` `🔗<class_PhysicsShapeQueryParameters3D_property_margin>`

classref-property-setget

- `void (No return value.)` **set_margin**(value: `float<class_float>`)
- `float<class_float>` **get_margin**()

The collision margin for the shape.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **motion** = `Vector3(0, 0, 0)` `🔗<class_PhysicsShapeQueryParameters3D_property_motion>`

classref-property-setget

- `void (No return value.)` **set_motion**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_motion**()

The motion of the shape being queried for.

classref-item-separator

classref-property

`Resource<class_Resource>` **shape** `🔗<class_PhysicsShapeQueryParameters3D_property_shape>`

classref-property-setget

- `void (No return value.)` **set_shape**(value: `Resource<class_Resource>`)
- `Resource<class_Resource>` **get_shape**()

The `Shape3D<class_Shape3D>` that will be used for collision/intersection queries. This stores the actual reference which avoids the shape to be released while being used for queries, so always prefer using this over `shape_rid<class_PhysicsShapeQueryParameters3D_property_shape_rid>`.

classref-item-separator

classref-property

`RID<class_RID>` **shape_rid** = `RID()` `🔗<class_PhysicsShapeQueryParameters3D_property_shape_rid>`

classref-property-setget

- `void (No return value.)` **set_shape_rid**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_shape_rid**()

The queried shape's `RID<class_RID>` that will be used for collision/intersection queries. Use this over `shape<class_PhysicsShapeQueryParameters3D_property_shape>` if you want to optimize for performance using the Servers API:

gdscript

var shape_rid = PhysicsServer3D.sphere_shape_create() var radius = 2.0 PhysicsServer3D.shape_set_data(shape_rid, radius)

var params = PhysicsShapeQueryParameters3D.new() params.shape_rid = shape_rid

\# Execute physics queries here...

\# Release the shape when done with physics queries. PhysicsServer3D.free_rid(shape_rid)

csharp

RID shapeRid = PhysicsServer3D.SphereShapeCreate(); float radius = 2.0f; PhysicsServer3D.ShapeSetData(shapeRid, radius);

var params = new PhysicsShapeQueryParameters3D(); params.ShapeRid = shapeRid;

// Execute physics queries here...

// Release the shape when done with physics queries. PhysicsServer3D.FreeRid(shapeRid);

classref-item-separator

classref-property

`Transform3D<class_Transform3D>` **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` `🔗<class_PhysicsShapeQueryParameters3D_property_transform>`

classref-property-setget

- `void (No return value.)` **set_transform**(value: `Transform3D<class_Transform3D>`)
- `Transform3D<class_Transform3D>` **get_transform**()

The queried shape's transform matrix.