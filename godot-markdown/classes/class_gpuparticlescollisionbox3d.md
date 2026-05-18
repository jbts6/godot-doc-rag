github_url
hide

# GPUParticlesCollisionBox3D

**Inherits:** `GPUParticlesCollision3D<class_GPUParticlesCollision3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A box-shaped 3D particle collision shape affecting `GPUParticles3D<class_GPUParticles3D>` nodes.

classref-introduction-group

## Description

A box-shaped 3D particle collision shape affecting `GPUParticles3D<class_GPUParticles3D>` nodes.

Particle collision shapes work in real-time and can be moved, rotated and scaled during gameplay. Unlike attractors, non-uniform scaling of collision shapes is *not* supported.

**Note:** `ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>` must be `ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>` or `ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>` on the `GPUParticles3D<class_GPUParticles3D>`'s process material for collision to work.

**Note:** Particle collision only affects `GPUParticles3D<class_GPUParticles3D>`, not `CPUParticles3D<class_CPUParticles3D>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector3<class_Vector3>` **size** = `Vector3(2, 2, 2)` `🔗<class_GPUParticlesCollisionBox3D_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_size**()

The collision box's size in 3D units.