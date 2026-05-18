github_url
hide

# CylinderShape3D

**Inherits:** `Shape3D<class_Shape3D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 3D cylinder shape used for physics collision.

classref-introduction-group

## Description

A 3D cylinder shape, intended for use in physics. Usually used to provide a shape for a `CollisionShape3D<class_CollisionShape3D>`.

**Note:** There are several known bugs with cylinder collision shapes. Using `CapsuleShape3D<class_CapsuleShape3D>` or `BoxShape3D<class_BoxShape3D>` instead is recommended.

**Performance:** **CylinderShape3D** is fast to check collisions against, but it is slower than `CapsuleShape3D<class_CapsuleShape3D>`, `BoxShape3D<class_BoxShape3D>`, and `SphereShape3D<class_SphereShape3D>`.

classref-introduction-group

## Tutorials

- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)
- [3D Physics Tests Demo](https://godotengine.org/asset-library/asset/2747)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **height** = `2.0` `🔗<class_CylinderShape3D_property_height>`

classref-property-setget

- `void (No return value.)` **set_height**(value: `float<class_float>`)
- `float<class_float>` **get_height**()

The cylinder's height.

classref-item-separator

classref-property

`float<class_float>` **radius** = `0.5` `🔗<class_CylinderShape3D_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

The cylinder's radius.