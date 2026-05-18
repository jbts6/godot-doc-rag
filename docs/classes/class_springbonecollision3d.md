github_url
hide

# SpringBoneCollision3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `SpringBoneCollisionCapsule3D<class_SpringBoneCollisionCapsule3D>`, `SpringBoneCollisionPlane3D<class_SpringBoneCollisionPlane3D>`, `SpringBoneCollisionSphere3D<class_SpringBoneCollisionSphere3D>`

A base class of the collision that interacts with `SpringBoneSimulator3D<class_SpringBoneSimulator3D>`.

classref-introduction-group

## Description

A collision can be a child of `SpringBoneSimulator3D<class_SpringBoneSimulator3D>`. If it is not a child of `SpringBoneSimulator3D<class_SpringBoneSimulator3D>`, it has no effect.

The colliding and sliding are done in the `SpringBoneSimulator3D<class_SpringBoneSimulator3D>`'s modification process in order of its collision list which is set by `SpringBoneSimulator3D.set_collision_path()<class_SpringBoneSimulator3D_method_set_collision_path>`. If `SpringBoneSimulator3D.are_all_child_collisions_enabled()<class_SpringBoneSimulator3D_method_are_all_child_collisions_enabled>` is `true`, the order matches `SceneTree<class_SceneTree>`.

If `bone<class_SpringBoneCollision3D_property_bone>` is set, it synchronizes with the bone pose of the ancestor `Skeleton3D<class_Skeleton3D>`, which is done in before the `SpringBoneSimulator3D<class_SpringBoneSimulator3D>`'s modification process as the pre-process.

**Warning:** A scaled **SpringBoneCollision3D** will likely not behave as expected. Make sure that the parent `Skeleton3D<class_Skeleton3D>` and its bones are not scaled.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **bone** = `-1` `🔗<class_SpringBoneCollision3D_property_bone>`

classref-property-setget

- `void (No return value.)` **set_bone**(value: `int<class_int>`)
- `int<class_int>` **get_bone**()

The index of the attached bone.

classref-item-separator

classref-property

`String<class_String>` **bone_name** = `""` `🔗<class_SpringBoneCollision3D_property_bone_name>`

classref-property-setget

- `void (No return value.)` **set_bone_name**(value: `String<class_String>`)
- `String<class_String>` **get_bone_name**()

The name of the attached bone.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **position_offset** `🔗<class_SpringBoneCollision3D_property_position_offset>`

classref-property-setget

- `void (No return value.)` **set_position_offset**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_position_offset**()

The offset of the position from `Skeleton3D<class_Skeleton3D>`'s `bone<class_SpringBoneCollision3D_property_bone>` pose position.

classref-item-separator

classref-property

`Quaternion<class_Quaternion>` **rotation_offset** `🔗<class_SpringBoneCollision3D_property_rotation_offset>`

classref-property-setget

- `void (No return value.)` **set_rotation_offset**(value: `Quaternion<class_Quaternion>`)
- `Quaternion<class_Quaternion>` **get_rotation_offset**()

The offset of the rotation from `Skeleton3D<class_Skeleton3D>`'s `bone<class_SpringBoneCollision3D_property_bone>` pose rotation.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Skeleton3D<class_Skeleton3D>` **get_skeleton**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SpringBoneCollision3D_method_get_skeleton>`

Get parent `Skeleton3D<class_Skeleton3D>` node of the parent `SpringBoneSimulator3D<class_SpringBoneSimulator3D>` if found.