github_url
hide

# RDAccelerationStructureInstance

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Acceleration structure instance (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

**RDAccelerationStructureInstance** describes an instance of a Bottom-Level Acceleration Structure (BLAS) used in the `RenderingDevice.tlas_build()<class_RenderingDevice_method_tlas_build>` method.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **blas** = `RID()` `🔗<class_RDAccelerationStructureInstance_property_blas>`

classref-property-setget

- `void (No return value.)` **set_blas**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_blas**()

The BLAS referenced by this instance. If `null`, the instance is treated as a placeholder but still contributes to `gl_InstanceIndex` in GLSL.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AccelerationStructureInstanceFlagBits<enum_RenderingDevice_AccelerationStructureInstanceFlagBits>`\] **flags** = `0` `🔗<class_RDAccelerationStructureInstance_property_flags>`

classref-property-setget

- `void (No return value.)` **set_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AccelerationStructureInstanceFlagBits<enum_RenderingDevice_AccelerationStructureInstanceFlagBits>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AccelerationStructureInstanceFlagBits<enum_RenderingDevice_AccelerationStructureInstanceFlagBits>`\] **get_flags**()

Flags for the instance.

classref-item-separator

classref-property

`int<class_int>` **hit_sbt_range** = `0` `🔗<class_RDAccelerationStructureInstance_property_hit_sbt_range>`

classref-property-setget

- `void (No return value.)` **set_hit_sbt_range**(value: `int<class_int>`)
- `int<class_int>` **get_hit_sbt_range**()

Hit shader binding table range used for this instance, allocated using the `RenderingDevice.hit_sbt_range_alloc()<class_RenderingDevice_method_hit_sbt_range_alloc>` method.

classref-item-separator

classref-property

`int<class_int>` **id** = `0` `🔗<class_RDAccelerationStructureInstance_property_id>`

classref-property-setget

- `void (No return value.)` **set_id**(value: `int<class_int>`)
- `int<class_int>` **get_id**()

Custom instance ID that can be accessed in GLSL using `gl_InstanceCustomIndexEXT`.

classref-item-separator

classref-property

`int<class_int>` **mask** = `255` `🔗<class_RDAccelerationStructureInstance_property_mask>`

classref-property-setget

- `void (No return value.)` **set_mask**(value: `int<class_int>`)
- `int<class_int>` **get_mask**()

Visibility mask used to control which rays can intersect this instance.

classref-item-separator

classref-property

`Transform3D<class_Transform3D>` **transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` `🔗<class_RDAccelerationStructureInstance_property_transform>`

classref-property-setget

- `void (No return value.)` **set_transform**(value: `Transform3D<class_Transform3D>`)
- `Transform3D<class_Transform3D>` **get_transform**()

Transform applied to the referenced BLAS for this instance.