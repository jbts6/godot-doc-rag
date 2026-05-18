github_url
hide

# ParticleProcessMaterial

**Inherits:** `Material<class_Material>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Holds a particle configuration for `GPUParticles2D<class_GPUParticles2D>` or `GPUParticles3D<class_GPUParticles3D>` nodes.

classref-introduction-group

## Description

**ParticleProcessMaterial** defines particle properties and behavior. It is used in the `process_material` of the `GPUParticles2D<class_GPUParticles2D>` and `GPUParticles3D<class_GPUParticles3D>` nodes. Some of this material's properties are applied to each particle when emitted, while others can have a `CurveTexture<class_CurveTexture>` or a `GradientTexture1D<class_GradientTexture1D>` applied to vary numerical or color values over the lifetime of the particle.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**emission_shape_changed**() `🔗<class_ParticleProcessMaterial_signal_emission_shape_changed>`

Emitted when this material's emission shape is changed in any way. This includes changes to `emission_shape<class_ParticleProcessMaterial_property_emission_shape>`, `emission_shape_scale<class_ParticleProcessMaterial_property_emission_shape_scale>`, or `emission_sphere_radius<class_ParticleProcessMaterial_property_emission_sphere_radius>`, and any other property that affects the emission shape's offset, size, scale, or orientation.

**Note:** This signal is only emitted inside the editor for performance reasons.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Parameter**: `🔗<enum_ParticleProcessMaterial_Parameter>`

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set initial velocity properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_ANGULAR_VELOCITY** = `1`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set angular velocity properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_ORBIT_VELOCITY** = `2`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set orbital velocity properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_LINEAR_ACCEL** = `3`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set linear acceleration properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_RADIAL_ACCEL** = `4`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set radial acceleration properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_TANGENTIAL_ACCEL** = `5`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set tangential acceleration properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_DAMPING** = `6`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set damping properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_ANGLE** = `7`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set angle properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_SCALE** = `8`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set scale properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_HUE_VARIATION** = `9`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set hue variation properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_ANIM_SPEED** = `10`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set animation speed properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_ANIM_OFFSET** = `11`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set animation offset properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_RADIAL_VELOCITY** = `15`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set radial velocity properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_DIRECTIONAL_VELOCITY** = `16`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set directional velocity properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_SCALE_OVER_VELOCITY** = `17`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`, `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`, and `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set scale over velocity properties.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_MAX** = `18`

Represents the size of the `Parameter<enum_ParticleProcessMaterial_Parameter>` enum.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_TURB_VEL_INFLUENCE** = `13`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>` and `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>` to set the turbulence minimum und maximum influence on each particles velocity.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_TURB_INIT_DISPLACEMENT** = `14`

Use with `set_param_min()<class_ParticleProcessMaterial_method_set_param_min>` and `set_param_max()<class_ParticleProcessMaterial_method_set_param_max>` to set the turbulence minimum and maximum displacement of the particles spawn position.

classref-enumeration-constant

`Parameter<enum_ParticleProcessMaterial_Parameter>` **PARAM_TURB_INFLUENCE_OVER_LIFE** = `12`

Use with `set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>` to set the turbulence influence over the particles life time.

classref-item-separator

classref-enumeration

enum **ParticleFlags**: `🔗<enum_ParticleProcessMaterial_ParticleFlags>`

classref-enumeration-constant

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with `set_particle_flag()<class_ParticleProcessMaterial_method_set_particle_flag>` to set `particle_flag_align_y<class_ParticleProcessMaterial_property_particle_flag_align_y>`.

classref-enumeration-constant

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with `set_particle_flag()<class_ParticleProcessMaterial_method_set_particle_flag>` to set `particle_flag_rotate_y<class_ParticleProcessMaterial_property_particle_flag_rotate_y>`.

classref-enumeration-constant

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with `set_particle_flag()<class_ParticleProcessMaterial_method_set_particle_flag>` to set `particle_flag_disable_z<class_ParticleProcessMaterial_property_particle_flag_disable_z>`.

classref-enumeration-constant

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` **PARTICLE_FLAG_DAMPING_AS_FRICTION** = `3`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` **PARTICLE_FLAG_INHERIT_EMITTER_SCALE** = `4`

There is currently no description for this enum. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-enumeration-constant

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` **PARTICLE_FLAG_MAX** = `5`

Represents the size of the `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>` enum.

classref-item-separator

classref-enumeration

enum **EmissionShape**: `🔗<enum_ParticleProcessMaterial_EmissionShape>`

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position determined by sampling a random point on the `emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`. Particle color will be modulated by `emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>`.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position determined by sampling a random point on the `emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`. Particle velocity and rotation will be set based on `emission_normal_texture<class_ParticleProcessMaterial_property_emission_normal_texture>`. Particle color will be modulated by `emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>`.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

classref-enumeration-constant

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **EMISSION_SHAPE_MAX** = `7`

Represents the size of the `EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` enum.

classref-item-separator

classref-enumeration

enum **SubEmitterMode**: `🔗<enum_ParticleProcessMaterial_SubEmitterMode>`

classref-enumeration-constant

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **SUB_EMITTER_DISABLED** = `0`

The subemitter is disabled.

classref-enumeration-constant

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **SUB_EMITTER_CONSTANT** = `1`

The submitter is emitted on the constant interval defined by `sub_emitter_frequency<class_ParticleProcessMaterial_property_sub_emitter_frequency>`.

classref-enumeration-constant

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **SUB_EMITTER_AT_END** = `2`

The subemitter is emitted at the end of the particle's lifetime.

classref-enumeration-constant

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **SUB_EMITTER_AT_COLLISION** = `3`

The subemitter is emitted when the particle collides.

classref-enumeration-constant

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **SUB_EMITTER_AT_START** = `4`

The subemitter is emitted when the particle spawns.

classref-enumeration-constant

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **SUB_EMITTER_MAX** = `5`

Represents the size of the `SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` enum.

classref-item-separator

classref-enumeration

enum **CollisionMode**: `🔗<enum_ParticleProcessMaterial_CollisionMode>`

classref-enumeration-constant

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` **COLLISION_DISABLED** = `0`

No collision for particles. Particles will go through `GPUParticlesCollision3D<class_GPUParticlesCollision3D>` nodes.

classref-enumeration-constant

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` **COLLISION_RIGID** = `1`

`RigidBody3D<class_RigidBody3D>`-style collision for particles using `GPUParticlesCollision3D<class_GPUParticlesCollision3D>` nodes.

classref-enumeration-constant

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` **COLLISION_HIDE_ON_CONTACT** = `2`

Hide particles instantly when colliding with a `GPUParticlesCollision3D<class_GPUParticlesCollision3D>` node. This can be combined with a subemitter that uses the `COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>` collision mode to "replace" the parent particle with the subemitter on impact.

classref-enumeration-constant

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` **COLLISION_MAX** = `3`

Represents the size of the `CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Texture2D<class_Texture2D>` **alpha_curve** `🔗<class_ParticleProcessMaterial_property_alpha_curve>`

classref-property-setget

- `void (No return value.)` **set_alpha_curve**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_alpha_curve**()

The alpha value of each particle's color will be multiplied by this `CurveTexture<class_CurveTexture>` over its lifetime.

**Note:** `alpha_curve<class_ParticleProcessMaterial_property_alpha_curve>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALPHA *= COLOR.a;` must be inserted in the shader's `fragment()` function. Otherwise, `alpha_curve<class_ParticleProcessMaterial_property_alpha_curve>` will have no visible effect.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **angle_curve** `🔗<class_ParticleProcessMaterial_property_angle_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's rotation will be animated along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **angle_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_angle_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial rotation applied to each particle, in degrees.

Only applied when `particle_flag_disable_z<class_ParticleProcessMaterial_property_particle_flag_disable_z>` or `particle_flag_rotate_y<class_ParticleProcessMaterial_property_particle_flag_rotate_y>` are `true` or the `BaseMaterial3D<class_BaseMaterial3D>` being used to draw the particle is using `BaseMaterial3D.BILLBOARD_PARTICLES<class_BaseMaterial3D_constant_BILLBOARD_PARTICLES>`.

classref-item-separator

classref-property

`float<class_float>` **angle_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_angle_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `angle_max<class_ParticleProcessMaterial_property_angle_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **angular_velocity_curve** `🔗<class_ParticleProcessMaterial_property_angular_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's angular velocity (rotation speed) will vary along this `CurveTexture<class_CurveTexture>` over its lifetime.

classref-item-separator

classref-property

`float<class_float>` **angular_velocity_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_angular_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

Only applied when `particle_flag_disable_z<class_ParticleProcessMaterial_property_particle_flag_disable_z>` or `particle_flag_rotate_y<class_ParticleProcessMaterial_property_particle_flag_rotate_y>` are `true` or the `BaseMaterial3D<class_BaseMaterial3D>` being used to draw the particle is using `BaseMaterial3D.BILLBOARD_PARTICLES<class_BaseMaterial3D_constant_BILLBOARD_PARTICLES>`.

classref-item-separator

classref-property

`float<class_float>` **angular_velocity_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_angular_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `angular_velocity_max<class_ParticleProcessMaterial_property_angular_velocity_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **anim_offset_curve** `🔗<class_ParticleProcessMaterial_property_anim_offset_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's animation offset will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **anim_offset_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_anim_offset_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum animation offset that corresponds to frame index in the texture. `0` is the first frame, `1` is the last one. See `CanvasItemMaterial.particles_animation<class_CanvasItemMaterial_property_particles_animation>`.

classref-item-separator

classref-property

`float<class_float>` **anim_offset_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_anim_offset_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `anim_offset_max<class_ParticleProcessMaterial_property_anim_offset_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **anim_speed_curve** `🔗<class_ParticleProcessMaterial_property_anim_speed_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's animation speed will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **anim_speed_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_anim_speed_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum particle animation speed. Animation speed of `1` means that the particles will make full `0` to `1` offset cycle during lifetime, `2` means `2` cycles etc.

With animation speed greater than `1`, remember to enable `CanvasItemMaterial.particles_anim_loop<class_CanvasItemMaterial_property_particles_anim_loop>` property if you want the animation to repeat.

classref-item-separator

classref-property

`float<class_float>` **anim_speed_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_anim_speed_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `anim_speed_max<class_ParticleProcessMaterial_property_anim_speed_max>`.

classref-item-separator

classref-property

`bool<class_bool>` **attractor_interaction_enabled** = `true` `🔗<class_ParticleProcessMaterial_property_attractor_interaction_enabled>`

classref-property-setget

- `void (No return value.)` **set_attractor_interaction_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_attractor_interaction_enabled**()

If `true`, interaction with particle attractors is enabled. In 3D, attraction only occurs within the area defined by the `GPUParticles3D<class_GPUParticles3D>` node's `GPUParticles3D.visibility_aabb<class_GPUParticles3D_property_visibility_aabb>`.

classref-item-separator

classref-property

`float<class_float>` **collision_bounce** `🔗<class_ParticleProcessMaterial_property_collision_bounce>`

classref-property-setget

- `void (No return value.)` **set_collision_bounce**(value: `float<class_float>`)
- `float<class_float>` **get_collision_bounce**()

The particles' bounciness. Values range from `0` (no bounce) to `1` (full bounciness). Only effective if `collision_mode<class_ParticleProcessMaterial_property_collision_mode>` is `COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`.

classref-item-separator

classref-property

`float<class_float>` **collision_friction** `🔗<class_ParticleProcessMaterial_property_collision_friction>`

classref-property-setget

- `void (No return value.)` **set_collision_friction**(value: `float<class_float>`)
- `float<class_float>` **get_collision_friction**()

The particles' friction. Values range from `0` (frictionless) to `1` (maximum friction). Only effective if `collision_mode<class_ParticleProcessMaterial_property_collision_mode>` is `COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`.

classref-item-separator

classref-property

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` **collision_mode** = `0` `🔗<class_ParticleProcessMaterial_property_collision_mode>`

classref-property-setget

- `void (No return value.)` **set_collision_mode**(value: `CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`)
- `CollisionMode<enum_ParticleProcessMaterial_CollisionMode>` **get_collision_mode**()

The particles' collision mode.

**Note:** 3D Particles can only collide with `GPUParticlesCollision3D<class_GPUParticlesCollision3D>` nodes, not `PhysicsBody3D<class_PhysicsBody3D>` nodes. To make particles collide with various objects, you can add `GPUParticlesCollision3D<class_GPUParticlesCollision3D>` nodes as children of `PhysicsBody3D<class_PhysicsBody3D>` nodes. In 3D, collisions only occur within the area defined by the `GPUParticles3D<class_GPUParticles3D>` node's `GPUParticles3D.visibility_aabb<class_GPUParticles3D_property_visibility_aabb>`.

**Note:** 2D Particles can only collide with `LightOccluder2D<class_LightOccluder2D>` nodes, not `PhysicsBody2D<class_PhysicsBody2D>` nodes.

classref-item-separator

classref-property

`bool<class_bool>` **collision_use_scale** = `false` `🔗<class_ParticleProcessMaterial_property_collision_use_scale>`

classref-property-setget

- `void (No return value.)` **set_collision_use_scale**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collision_using_scale**()

If `true`, `GPUParticles3D.collision_base_size<class_GPUParticles3D_property_collision_base_size>` is multiplied by the particle's effective scale (see `scale_min<class_ParticleProcessMaterial_property_scale_min>`, `scale_max<class_ParticleProcessMaterial_property_scale_max>`, `scale_curve<class_ParticleProcessMaterial_property_scale_curve>`, and `scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`).

classref-item-separator

classref-property

`Color<class_Color>` **color** = `Color(1, 1, 1, 1)` `🔗<class_ParticleProcessMaterial_property_color>`

classref-property-setget

- `void (No return value.)` **set_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_color**()

Each particle's initial color. If the `GPUParticles2D<class_GPUParticles2D>`'s `texture` is defined, it will be multiplied by this color.

**Note:** `color<class_ParticleProcessMaterial_property_color>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `color<class_ParticleProcessMaterial_property_color>` will have no visible effect.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **color_initial_ramp** `🔗<class_ParticleProcessMaterial_property_color_initial_ramp>`

classref-property-setget

- `void (No return value.)` **set_color_initial_ramp**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_color_initial_ramp**()

Each particle's initial color will vary along this `GradientTexture1D<class_GradientTexture1D>` (multiplied with `color<class_ParticleProcessMaterial_property_color>`).

**Note:** `color_initial_ramp<class_ParticleProcessMaterial_property_color_initial_ramp>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `color_initial_ramp<class_ParticleProcessMaterial_property_color_initial_ramp>` will have no visible effect.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **color_ramp** `🔗<class_ParticleProcessMaterial_property_color_ramp>`

classref-property-setget

- `void (No return value.)` **set_color_ramp**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_color_ramp**()

Each particle's color will vary along this `GradientTexture1D<class_GradientTexture1D>` over its lifetime (multiplied with `color<class_ParticleProcessMaterial_property_color>`).

**Note:** `color_ramp<class_ParticleProcessMaterial_property_color_ramp>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `color_ramp<class_ParticleProcessMaterial_property_color_ramp>` will have no visible effect.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **damping_curve** `🔗<class_ParticleProcessMaterial_property_damping_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Damping will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **damping_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_damping_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum rate at which particles lose velocity. For example value of `100` means that the particle will go from `100` velocity to `0` in `1` second.

classref-item-separator

classref-property

`float<class_float>` **damping_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_damping_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `damping_max<class_ParticleProcessMaterial_property_damping_max>`.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **direction** = `Vector3(1, 0, 0)` `🔗<class_ParticleProcessMaterial_property_direction>`

classref-property-setget

- `void (No return value.)` **set_direction**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_direction**()

Unit vector specifying the particles' emission direction.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **directional_velocity_curve** `🔗<class_ParticleProcessMaterial_property_directional_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

A curve that specifies the velocity along each of the axes of the particle system along its lifetime.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`float<class_float>` **directional_velocity_max** `🔗<class_ParticleProcessMaterial_property_directional_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum directional velocity value, which is multiplied by `directional_velocity_curve<class_ParticleProcessMaterial_property_directional_velocity_curve>`.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`float<class_float>` **directional_velocity_min** `🔗<class_ParticleProcessMaterial_property_directional_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum directional velocity value, which is multiplied by `directional_velocity_curve<class_ParticleProcessMaterial_property_directional_velocity_curve>`.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **emission_box_extents** `🔗<class_ParticleProcessMaterial_property_emission_box_extents>`

classref-property-setget

- `void (No return value.)` **set_emission_box_extents**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_emission_box_extents**()

The box's extents if `emission_shape<class_ParticleProcessMaterial_property_emission_shape>` is set to `EMISSION_SHAPE_BOX<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_BOX>`.

**Note:** `emission_box_extents<class_ParticleProcessMaterial_property_emission_box_extents>` starts from the center point and applies the X, Y, and Z values in both directions. The size is twice the area of the extents.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **emission_color_texture** `🔗<class_ParticleProcessMaterial_property_emission_color_texture>`

classref-property-setget

- `void (No return value.)` **set_emission_color_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_emission_color_texture**()

Particle color will be modulated by color determined by sampling this texture at the same point as the `emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`.

**Note:** `emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>` will have no visible effect.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **emission_curve** `🔗<class_ParticleProcessMaterial_property_emission_curve>`

classref-property-setget

- `void (No return value.)` **set_emission_curve**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_emission_curve**()

Each particle's color will be multiplied by this `CurveTexture<class_CurveTexture>` over its lifetime.

**Note:** `emission_curve<class_ParticleProcessMaterial_property_emission_curve>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `emission_curve<class_ParticleProcessMaterial_property_emission_curve>` will have no visible effect.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **emission_normal_texture** `🔗<class_ParticleProcessMaterial_property_emission_normal_texture>`

classref-property-setget

- `void (No return value.)` **set_emission_normal_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_emission_normal_texture**()

Particle velocity and rotation will be set by sampling this texture at the same point as the `emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`. Used only in `EMISSION_SHAPE_DIRECTED_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS>`. Can be created automatically from mesh or node by selecting "Create Emission Points from Mesh/Node" under the "Particles" tool in the toolbar.

classref-item-separator

classref-property

`int<class_int>` **emission_point_count** `🔗<class_ParticleProcessMaterial_property_emission_point_count>`

classref-property-setget

- `void (No return value.)` **set_emission_point_count**(value: `int<class_int>`)
- `int<class_int>` **get_emission_point_count**()

The number of emission points if `emission_shape<class_ParticleProcessMaterial_property_emission_shape>` is set to `EMISSION_SHAPE_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS>` or `EMISSION_SHAPE_DIRECTED_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **emission_point_texture** `🔗<class_ParticleProcessMaterial_property_emission_point_texture>`

classref-property-setget

- `void (No return value.)` **set_emission_point_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_emission_point_texture**()

Particles will be emitted at positions determined by sampling this texture at a random position. Used with `EMISSION_SHAPE_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS>` and `EMISSION_SHAPE_DIRECTED_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS>`. Can be created automatically from mesh or node by selecting "Create Emission Points from Mesh/Node" under the "Particles" tool in the toolbar.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **emission_ring_axis** `🔗<class_ParticleProcessMaterial_property_emission_ring_axis>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_axis**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_emission_ring_axis**()

The axis of the ring when using the emitter `EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_cone_angle** `🔗<class_ParticleProcessMaterial_property_emission_ring_cone_angle>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_cone_angle**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_cone_angle**()

The angle of the cone when using the emitter `EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`. The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

**Note:** Depending on `emission_ring_height<class_ParticleProcessMaterial_property_emission_ring_height>`, the angle may be clamped if the ring's end is reached to form a perfect cone.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_height** `🔗<class_ParticleProcessMaterial_property_emission_ring_height>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_height**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_height**()

The height of the ring when using the emitter `EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_inner_radius** `🔗<class_ParticleProcessMaterial_property_emission_ring_inner_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_inner_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_inner_radius**()

The inner radius of the ring when using the emitter `EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_radius** `🔗<class_ParticleProcessMaterial_property_emission_ring_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_radius**()

The radius of the ring when using the emitter `EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **emission_shape** = `0` `🔗<class_ParticleProcessMaterial_property_emission_shape>`

classref-property-setget

- `void (No return value.)` **set_emission_shape**(value: `EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`)
- `EmissionShape<enum_ParticleProcessMaterial_EmissionShape>` **get_emission_shape**()

Particles will be emitted inside this region.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **emission_shape_offset** = `Vector3(0, 0, 0)` `🔗<class_ParticleProcessMaterial_property_emission_shape_offset>`

classref-property-setget

- `void (No return value.)` **set_emission_shape_offset**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_emission_shape_offset**()

The offset for the `emission_shape<class_ParticleProcessMaterial_property_emission_shape>`, in local space.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **emission_shape_scale** = `Vector3(1, 1, 1)` `🔗<class_ParticleProcessMaterial_property_emission_shape_scale>`

classref-property-setget

- `void (No return value.)` **set_emission_shape_scale**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_emission_shape_scale**()

The scale of the `emission_shape<class_ParticleProcessMaterial_property_emission_shape>`, in local space.

classref-item-separator

classref-property

`float<class_float>` **emission_sphere_radius** `🔗<class_ParticleProcessMaterial_property_emission_sphere_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_sphere_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_sphere_radius**()

The sphere's radius if `emission_shape<class_ParticleProcessMaterial_property_emission_shape>` is set to `EMISSION_SHAPE_SPHERE<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE>`.

classref-item-separator

classref-property

`float<class_float>` **flatness** = `0.0` `🔗<class_ParticleProcessMaterial_property_flatness>`

classref-property-setget

- `void (No return value.)` **set_flatness**(value: `float<class_float>`)
- `float<class_float>` **get_flatness**()

Amount of `spread<class_ParticleProcessMaterial_property_spread>` along the Y axis.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **gravity** = `Vector3(0, -9.8, 0)` `🔗<class_ParticleProcessMaterial_property_gravity>`

classref-property-setget

- `void (No return value.)` **set_gravity**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_gravity**()

Gravity applied to every particle.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **hue_variation_curve** `🔗<class_ParticleProcessMaterial_property_hue_variation_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's hue will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **hue_variation_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_hue_variation_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial hue variation applied to each particle. It will shift the particle color's hue.

classref-item-separator

classref-property

`float<class_float>` **hue_variation_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_hue_variation_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `hue_variation_max<class_ParticleProcessMaterial_property_hue_variation_max>`.

classref-item-separator

classref-property

`float<class_float>` **inherit_velocity_ratio** = `0.0` `🔗<class_ParticleProcessMaterial_property_inherit_velocity_ratio>`

classref-property-setget

- `void (No return value.)` **set_inherit_velocity_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_inherit_velocity_ratio**()

Percentage of the velocity of the respective `GPUParticles2D<class_GPUParticles2D>` or `GPUParticles3D<class_GPUParticles3D>` inherited by each particle when spawning.

classref-item-separator

classref-property

`float<class_float>` **initial_velocity_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_initial_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial velocity magnitude for each particle. Direction comes from `direction<class_ParticleProcessMaterial_property_direction>` and `spread<class_ParticleProcessMaterial_property_spread>`.

classref-item-separator

classref-property

`float<class_float>` **initial_velocity_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_initial_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `initial_velocity_max<class_ParticleProcessMaterial_property_initial_velocity_max>`.

classref-item-separator

classref-property

`float<class_float>` **lifetime_randomness** = `0.0` `🔗<class_ParticleProcessMaterial_property_lifetime_randomness>`

classref-property-setget

- `void (No return value.)` **set_lifetime_randomness**(value: `float<class_float>`)
- `float<class_float>` **get_lifetime_randomness**()

Particle lifetime randomness ratio. The equation for the lifetime of a particle is `lifetime * (1.0 - randf() * lifetime_randomness)`. For example, a `lifetime_randomness<class_ParticleProcessMaterial_property_lifetime_randomness>` of `0.4` scales the lifetime between `0.6` to `1.0` of its original value.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **linear_accel_curve** `🔗<class_ParticleProcessMaterial_property_linear_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's linear acceleration will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **linear_accel_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_linear_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum linear acceleration applied to each particle in the direction of motion.

classref-item-separator

classref-property

`float<class_float>` **linear_accel_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_linear_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `linear_accel_max<class_ParticleProcessMaterial_property_linear_accel_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **orbit_velocity_curve** `🔗<class_ParticleProcessMaterial_property_orbit_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's orbital velocity will vary along this `CurveTexture<class_CurveTexture>`.

**Note:** For 3D orbital velocity, use a `CurveXYZTexture<class_CurveXYZTexture>`.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`float<class_float>` **orbit_velocity_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_orbit_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum orbital velocity applied to each particle. Makes the particles circle around origin. Specified in number of full rotations around origin per second.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`float<class_float>` **orbit_velocity_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_orbit_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `orbit_velocity_max<class_ParticleProcessMaterial_property_orbit_velocity_max>`.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_align_y** = `false` `🔗<class_ParticleProcessMaterial_property_particle_flag_align_y>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Align Y axis of particle with the direction of its velocity.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_damping_as_friction** = `false` `🔗<class_ParticleProcessMaterial_property_particle_flag_damping_as_friction>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Changes the behavior of the damping properties from a linear deceleration to a deceleration based on speed percentage.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_disable_z** = `false` `🔗<class_ParticleProcessMaterial_property_particle_flag_disable_z>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, particles will not move on the z axis.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_inherit_emitter_scale** = `false` `🔗<class_ParticleProcessMaterial_property_particle_flag_inherit_emitter_scale>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, particles will inherit the scale of the emitter.

**Note:** This has no effect when `GPUParticles3D.local_coords<class_GPUParticles3D_property_local_coords>` is `true`, since particles in local space are already affected by the emitter's scale.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_rotate_y** = `false` `🔗<class_ParticleProcessMaterial_property_particle_flag_rotate_y>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, particles rotate around Y axis by `angle_min<class_ParticleProcessMaterial_property_angle_min>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **radial_accel_curve** `🔗<class_ParticleProcessMaterial_property_radial_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's radial acceleration will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **radial_accel_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_radial_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum radial acceleration applied to each particle. Makes particle accelerate away from the origin or towards it if negative.

classref-item-separator

classref-property

`float<class_float>` **radial_accel_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_radial_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `radial_accel_max<class_ParticleProcessMaterial_property_radial_accel_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **radial_velocity_curve** `🔗<class_ParticleProcessMaterial_property_radial_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

A `CurveTexture<class_CurveTexture>` that defines the velocity over the particle's lifetime away (or toward) the `velocity_pivot<class_ParticleProcessMaterial_property_velocity_pivot>`.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`float<class_float>` **radial_velocity_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_radial_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum radial velocity applied to each particle. Makes particles move away from the `velocity_pivot<class_ParticleProcessMaterial_property_velocity_pivot>`, or toward it if negative.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`float<class_float>` **radial_velocity_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_radial_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum radial velocity applied to each particle. Makes particles move away from the `velocity_pivot<class_ParticleProcessMaterial_property_velocity_pivot>`, or toward it if negative.

**Note:** Animated velocities will not be affected by damping, use `velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>` instead.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **rotation_3d_max** `🔗<class_ParticleProcessMaterial_property_rotation_3d_max>`

classref-property-setget

- `void (No return value.)` **set_rotation_3d_max**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_rotation_3d_max**()

The maximum 3D orientation, in degrees. Works only in 3D and if `use_rotation_3d<class_ParticleProcessMaterial_property_use_rotation_3d>` is enabled.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **rotation_3d_min** `🔗<class_ParticleProcessMaterial_property_rotation_3d_min>`

classref-property-setget

- `void (No return value.)` **set_rotation_3d_min**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_rotation_3d_min**()

The minimum 3D orientation, in degrees. Works only in 3D and if `use_rotation_3d<class_ParticleProcessMaterial_property_use_rotation_3d>` is enabled.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **rotation_velocity_3d_curve** `🔗<class_ParticleProcessMaterial_property_rotation_velocity_3d_curve>`

classref-property-setget

- `void (No return value.)` **set_rotation_velocity_3d_curve**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_rotation_velocity_3d_curve**()

Rotation velocity curve over lifetime, per-axis. Enable `use_rotation_velocity_3d<class_ParticleProcessMaterial_property_use_rotation_velocity_3d>` to use this.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **rotation_velocity_3d_max** `🔗<class_ParticleProcessMaterial_property_rotation_velocity_3d_max>`

classref-property-setget

- `void (No return value.)` **set_rotation_velocity_3d_max**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_rotation_velocity_3d_max**()

Maximum 3D rotation velocity on the particle's local axis. Enable `use_rotation_velocity_3d<class_ParticleProcessMaterial_property_use_rotation_velocity_3d>` to use this.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **rotation_velocity_3d_min** `🔗<class_ParticleProcessMaterial_property_rotation_velocity_3d_min>`

classref-property-setget

- `void (No return value.)` **set_rotation_velocity_3d_min**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_rotation_velocity_3d_min**()

Minimum 3D rotation velocity on the particle's local axis. Enable `use_rotation_velocity_3d<class_ParticleProcessMaterial_property_use_rotation_velocity_3d>` to use this.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **scale_3d_max** `🔗<class_ParticleProcessMaterial_property_scale_3d_max>`

classref-property-setget

- `void (No return value.)` **set_scale_3d_max**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_scale_3d_max**()

The maximum value of the random scale vector for each particle.

Works only if `use_scale_3d<class_ParticleProcessMaterial_property_use_scale_3d>` is enabled.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **scale_3d_min** `🔗<class_ParticleProcessMaterial_property_scale_3d_min>`

classref-property-setget

- `void (No return value.)` **set_scale_3d_min**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_scale_3d_min**()

The minimum value of the random scale vector for each particle.

Works only if `use_scale_3d<class_ParticleProcessMaterial_property_use_scale_3d>` is enabled.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **scale_curve** `🔗<class_ParticleProcessMaterial_property_scale_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's scale will vary along this `CurveTexture<class_CurveTexture>` over its lifetime. If a `CurveXYZTexture<class_CurveXYZTexture>` is supplied instead, the scale will be separated per-axis.

classref-item-separator

classref-property

`float<class_float>` **scale_max** = `1.0` `🔗<class_ParticleProcessMaterial_property_scale_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial scale applied to each particle.

classref-item-separator

classref-property

`float<class_float>` **scale_min** = `1.0` `🔗<class_ParticleProcessMaterial_property_scale_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `scale_max<class_ParticleProcessMaterial_property_scale_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **scale_over_velocity_curve** `🔗<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Either a `CurveTexture<class_CurveTexture>` or a `CurveXYZTexture<class_CurveXYZTexture>` that scales each particle based on its velocity.

classref-item-separator

classref-property

`float<class_float>` **scale_over_velocity_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_scale_over_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum velocity value reference for `scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`.

`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>` will be interpolated between `scale_over_velocity_min<class_ParticleProcessMaterial_property_scale_over_velocity_min>` and `scale_over_velocity_max<class_ParticleProcessMaterial_property_scale_over_velocity_max>`.

classref-item-separator

classref-property

`float<class_float>` **scale_over_velocity_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_scale_over_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum velocity value reference for `scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`.

`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>` will be interpolated between `scale_over_velocity_min<class_ParticleProcessMaterial_property_scale_over_velocity_min>` and `scale_over_velocity_max<class_ParticleProcessMaterial_property_scale_over_velocity_max>`.

classref-item-separator

classref-property

`float<class_float>` **spread** = `45.0` `🔗<class_ParticleProcessMaterial_property_spread>`

classref-property-setget

- `void (No return value.)` **set_spread**(value: `float<class_float>`)
- `float<class_float>` **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees.

classref-item-separator

classref-property

`int<class_int>` **sub_emitter_amount_at_collision** `🔗<class_ParticleProcessMaterial_property_sub_emitter_amount_at_collision>`

classref-property-setget

- `void (No return value.)` **set_sub_emitter_amount_at_collision**(value: `int<class_int>`)
- `int<class_int>` **get_sub_emitter_amount_at_collision**()

The amount of particles to spawn from the subemitter node when a collision occurs. When combined with `COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>` on the main particles material, this can be used to achieve effects such as raindrops hitting the ground.

**Note:** This value shouldn't exceed `GPUParticles2D.amount<class_GPUParticles2D_property_amount>` or `GPUParticles3D.amount<class_GPUParticles3D_property_amount>` defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

classref-item-separator

classref-property

`int<class_int>` **sub_emitter_amount_at_end** `🔗<class_ParticleProcessMaterial_property_sub_emitter_amount_at_end>`

classref-property-setget

- `void (No return value.)` **set_sub_emitter_amount_at_end**(value: `int<class_int>`)
- `int<class_int>` **get_sub_emitter_amount_at_end**()

The amount of particles to spawn from the subemitter node when the particle expires.

**Note:** This value shouldn't exceed `GPUParticles2D.amount<class_GPUParticles2D_property_amount>` or `GPUParticles3D.amount<class_GPUParticles3D_property_amount>` defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

classref-item-separator

classref-property

`int<class_int>` **sub_emitter_amount_at_start** `🔗<class_ParticleProcessMaterial_property_sub_emitter_amount_at_start>`

classref-property-setget

- `void (No return value.)` **set_sub_emitter_amount_at_start**(value: `int<class_int>`)
- `int<class_int>` **get_sub_emitter_amount_at_start**()

The amount of particles to spawn from the subemitter node when the particle spawns.

**Note:** This value shouldn't exceed `GPUParticles2D.amount<class_GPUParticles2D_property_amount>` or `GPUParticles3D.amount<class_GPUParticles3D_property_amount>` defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

classref-item-separator

classref-property

`float<class_float>` **sub_emitter_frequency** `🔗<class_ParticleProcessMaterial_property_sub_emitter_frequency>`

classref-property-setget

- `void (No return value.)` **set_sub_emitter_frequency**(value: `float<class_float>`)
- `float<class_float>` **get_sub_emitter_frequency**()

The frequency at which particles should be emitted from the subemitter node. One particle will be spawned every `sub_emitter_frequency<class_ParticleProcessMaterial_property_sub_emitter_frequency>` seconds.

**Note:** This value shouldn't exceed `GPUParticles2D.amount<class_GPUParticles2D_property_amount>` or `GPUParticles3D.amount<class_GPUParticles3D_property_amount>` defined on the *subemitter node* (not the main node), relative to the subemitter's particle lifetime. If the number of particles is exceeded, no new particles will spawn from the subemitter until enough particles have expired.

classref-item-separator

classref-property

`bool<class_bool>` **sub_emitter_keep_velocity** = `false` `🔗<class_ParticleProcessMaterial_property_sub_emitter_keep_velocity>`

classref-property-setget

- `void (No return value.)` **set_sub_emitter_keep_velocity**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_sub_emitter_keep_velocity**()

If `true`, the subemitter inherits the parent particle's velocity when it spawns.

classref-item-separator

classref-property

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **sub_emitter_mode** = `0` `🔗<class_ParticleProcessMaterial_property_sub_emitter_mode>`

classref-property-setget

- `void (No return value.)` **set_sub_emitter_mode**(value: `SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`)
- `SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>` **get_sub_emitter_mode**()

The particle subemitter mode (see `GPUParticles2D.sub_emitter<class_GPUParticles2D_property_sub_emitter>` and `GPUParticles3D.sub_emitter<class_GPUParticles3D_property_sub_emitter>`).

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **tangential_accel_curve** `🔗<class_ParticleProcessMaterial_property_tangential_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's tangential acceleration will vary along this `CurveTexture<class_CurveTexture>`.

classref-item-separator

classref-property

`float<class_float>` **tangential_accel_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_tangential_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum tangential acceleration applied to each particle. Tangential acceleration is perpendicular to the particle's velocity giving the particles a swirling motion.

classref-item-separator

classref-property

`float<class_float>` **tangential_accel_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_tangential_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `tangential_accel_max<class_ParticleProcessMaterial_property_tangential_accel_max>`.

classref-item-separator

classref-property

`bool<class_bool>` **turbulence_enabled** = `false` `🔗<class_ParticleProcessMaterial_property_turbulence_enabled>`

classref-property-setget

- `void (No return value.)` **set_turbulence_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_turbulence_enabled**()

If `true`, enables turbulence for the particle system. Turbulence can be used to vary particle movement according to its position (based on a 3D noise pattern). In 3D, `GPUParticlesAttractorVectorField3D<class_GPUParticlesAttractorVectorField3D>` with `NoiseTexture3D<class_NoiseTexture3D>` can be used as an alternative to turbulence that works in world space and with multiple particle systems reacting in the same way.

**Note:** Enabling turbulence has a high performance cost on the GPU. Only enable turbulence on a few particle systems at once at most, and consider disabling it when targeting mobile/web platforms.

classref-item-separator

classref-property

`float<class_float>` **turbulence_influence_max** = `0.1` `🔗<class_ParticleProcessMaterial_property_turbulence_influence_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated as a random value between `turbulence_influence_min<class_ParticleProcessMaterial_property_turbulence_influence_min>` and `turbulence_influence_max<class_ParticleProcessMaterial_property_turbulence_influence_max>` and multiplied by the amount of turbulence influence from `turbulence_influence_over_life<class_ParticleProcessMaterial_property_turbulence_influence_over_life>`.

classref-item-separator

classref-property

`float<class_float>` **turbulence_influence_min** = `0.1` `🔗<class_ParticleProcessMaterial_property_turbulence_influence_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated as a random value between `turbulence_influence_min<class_ParticleProcessMaterial_property_turbulence_influence_min>` and `turbulence_influence_max<class_ParticleProcessMaterial_property_turbulence_influence_max>` and multiplied by the amount of turbulence influence from `turbulence_influence_over_life<class_ParticleProcessMaterial_property_turbulence_influence_over_life>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **turbulence_influence_over_life** `🔗<class_ParticleProcessMaterial_property_turbulence_influence_over_life>`

classref-property-setget

- `void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's amount of turbulence will be influenced along this `CurveTexture<class_CurveTexture>` over its life time.

classref-item-separator

classref-property

`float<class_float>` **turbulence_initial_displacement_max** = `0.0` `🔗<class_ParticleProcessMaterial_property_turbulence_initial_displacement_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum displacement of each particle's spawn position by the turbulence.

The actual amount of displacement will be a factor of the underlying turbulence multiplied by a random value between `turbulence_initial_displacement_min<class_ParticleProcessMaterial_property_turbulence_initial_displacement_min>` and `turbulence_initial_displacement_max<class_ParticleProcessMaterial_property_turbulence_initial_displacement_max>`.

classref-item-separator

classref-property

`float<class_float>` **turbulence_initial_displacement_min** = `0.0` `🔗<class_ParticleProcessMaterial_property_turbulence_initial_displacement_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum displacement of each particle's spawn position by the turbulence.

The actual amount of displacement will be a factor of the underlying turbulence multiplied by a random value between `turbulence_initial_displacement_min<class_ParticleProcessMaterial_property_turbulence_initial_displacement_min>` and `turbulence_initial_displacement_max<class_ParticleProcessMaterial_property_turbulence_initial_displacement_max>`.

classref-item-separator

classref-property

`float<class_float>` **turbulence_noise_scale** = `9.0` `🔗<class_ParticleProcessMaterial_property_turbulence_noise_scale>`

classref-property-setget

- `void (No return value.)` **set_turbulence_noise_scale**(value: `float<class_float>`)
- `float<class_float>` **get_turbulence_noise_scale**()

This value controls the overall scale/frequency of the turbulence noise pattern.

A small scale will result in smaller features with more detail while a high scale will result in smoother noise with larger features.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **turbulence_noise_speed** = `Vector3(0, 0, 0)` `🔗<class_ParticleProcessMaterial_property_turbulence_noise_speed>`

classref-property-setget

- `void (No return value.)` **set_turbulence_noise_speed**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_turbulence_noise_speed**()

A scrolling velocity for the turbulence field. This sets a directional trend for the pattern to move in over time.

The default value of `Vector3(0, 0, 0)` turns off the scrolling.

classref-item-separator

classref-property

`float<class_float>` **turbulence_noise_speed_random** = `0.2` `🔗<class_ParticleProcessMaterial_property_turbulence_noise_speed_random>`

classref-property-setget

- `void (No return value.)` **set_turbulence_noise_speed_random**(value: `float<class_float>`)
- `float<class_float>` **get_turbulence_noise_speed_random**()

The in-place rate of change of the turbulence field. This defines how quickly the noise pattern varies over time.

A value of 0.0 will result in a fixed pattern.

classref-item-separator

classref-property

`float<class_float>` **turbulence_noise_strength** = `1.0` `🔗<class_ParticleProcessMaterial_property_turbulence_noise_strength>`

classref-property-setget

- `void (No return value.)` **set_turbulence_noise_strength**(value: `float<class_float>`)
- `float<class_float>` **get_turbulence_noise_strength**()

The turbulence noise strength. Increasing this will result in a stronger, more contrasting, flow pattern.

classref-item-separator

classref-property

`bool<class_bool>` **use_rotation_3d** = `false` `🔗<class_ParticleProcessMaterial_property_use_rotation_3d>`

classref-property-setget

- `void (No return value.)` **set_use_rotation_3d**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_rotation_3d**()

Enable the usage of `rotation_3d_min<class_ParticleProcessMaterial_property_rotation_3d_min>` and `rotation_3d_max<class_ParticleProcessMaterial_property_rotation_3d_max>`.

classref-item-separator

classref-property

`bool<class_bool>` **use_rotation_velocity_3d** = `false` `🔗<class_ParticleProcessMaterial_property_use_rotation_velocity_3d>`

classref-property-setget

- `void (No return value.)` **set_using_rotation_velocity_3d**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_rotation_velocity_3d**()

Enable 3D rotation velocity.

classref-item-separator

classref-property

`bool<class_bool>` **use_scale_3d** = `false` `🔗<class_ParticleProcessMaterial_property_use_scale_3d>`

classref-property-setget

- `void (No return value.)` **set_use_scale_3d**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_scale_3d**()

Enable the usage of `scale_3d_min<class_ParticleProcessMaterial_property_scale_3d_min>` and `scale_3d_max<class_ParticleProcessMaterial_property_scale_3d_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **velocity_limit_curve** `🔗<class_ParticleProcessMaterial_property_velocity_limit_curve>`

classref-property-setget

- `void (No return value.)` **set_velocity_limit_curve**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_velocity_limit_curve**()

A `CurveTexture<class_CurveTexture>` that defines the maximum velocity of a particle during its lifetime.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **velocity_pivot** = `Vector3(0, 0, 0)` `🔗<class_ParticleProcessMaterial_property_velocity_pivot>`

classref-property-setget

- `void (No return value.)` **set_velocity_pivot**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_velocity_pivot**()

A pivot point used to calculate radial and orbital velocity of particles.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Vector2<class_Vector2>` **get_param**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ParticleProcessMaterial_method_get_param>`

Returns the minimum and maximum values of the given `param` as a vector.

The `x` component of the returned vector corresponds to minimum and the `y` component corresponds to maximum.

classref-item-separator

classref-method

`float<class_float>` **get_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ParticleProcessMaterial_method_get_param_max>`

Returns the maximum value range for the given parameter.

classref-item-separator

classref-method

`float<class_float>` **get_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ParticleProcessMaterial_method_get_param_min>`

Returns the minimum value range for the given parameter.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ParticleProcessMaterial_method_get_param_texture>`

Returns the `Texture2D<class_Texture2D>` used by the specified parameter.

classref-item-separator

classref-method

`bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ParticleProcessMaterial_method_get_particle_flag>`

Returns `true` if the specified particle flag is enabled.

classref-item-separator

classref-method

`void (No return value.)` **set_param**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `Vector2<class_Vector2>`) `🔗<class_ParticleProcessMaterial_method_set_param>`

Sets the minimum and maximum values of the given `param`.

The `x` component of the argument vector corresponds to minimum and the `y` component corresponds to maximum.

classref-item-separator

classref-method

`void (No return value.)` **set_param_max**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`) `🔗<class_ParticleProcessMaterial_method_set_param_max>`

Sets the maximum value range for the given parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_param_min**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, value: `float<class_float>`) `🔗<class_ParticleProcessMaterial_method_set_param_min>`

Sets the minimum value range for the given parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_param_texture**(param: `Parameter<enum_ParticleProcessMaterial_Parameter>`, texture: `Texture2D<class_Texture2D>`) `🔗<class_ParticleProcessMaterial_method_set_param_texture>`

Sets the `Texture2D<class_Texture2D>` for the specified `Parameter<enum_ParticleProcessMaterial_Parameter>`.

classref-item-separator

classref-method

`void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`, enable: `bool<class_bool>`) `🔗<class_ParticleProcessMaterial_method_set_particle_flag>`

Sets the `particle_flag` to `enable`.