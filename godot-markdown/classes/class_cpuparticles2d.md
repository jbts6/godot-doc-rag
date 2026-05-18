github_url
hide

# CPUParticles2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A CPU-based 2D particle emitter.

classref-introduction-group

## Description

CPU-based 2D particle node used to create a variety of particle systems and effects.

See also `GPUParticles2D<class_GPUParticles2D>`, which provides the same functionality with hardware acceleration, but may not run on older devices.

classref-introduction-group

## Tutorials

- `Particle systems (2D) <../tutorials/2d/particle_systems_2d>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**finished**() `🔗<class_CPUParticles2D_signal_finished>`

Emitted when all active particles have finished processing. When `one_shot<class_CPUParticles2D_property_one_shot>` is disabled, particles will process continuously, so this is never emitted.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DrawOrder**: `🔗<enum_CPUParticles2D_DrawOrder>`

classref-enumeration-constant

`DrawOrder<enum_CPUParticles2D_DrawOrder>` **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

classref-enumeration-constant

`DrawOrder<enum_CPUParticles2D_DrawOrder>` **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

classref-item-separator

classref-enumeration

enum **Parameter**: `🔗<enum_CPUParticles2D_Parameter>`

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set initial velocity properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_ANGULAR_VELOCITY** = `1`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set angular velocity properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_ORBIT_VELOCITY** = `2`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set orbital velocity properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_LINEAR_ACCEL** = `3`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set linear acceleration properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_RADIAL_ACCEL** = `4`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set radial acceleration properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_TANGENTIAL_ACCEL** = `5`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set tangential acceleration properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_DAMPING** = `6`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set damping properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_ANGLE** = `7`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set angle properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_SCALE** = `8`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set scale properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_HUE_VARIATION** = `9`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set hue variation properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_ANIM_SPEED** = `10`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set animation speed properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_ANIM_OFFSET** = `11`

Use with `set_param_min()<class_CPUParticles2D_method_set_param_min>`, `set_param_max()<class_CPUParticles2D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles2D_method_set_param_curve>` to set animation offset properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles2D_Parameter>` **PARAM_MAX** = `12`

Represents the size of the `Parameter<enum_CPUParticles2D_Parameter>` enum.

classref-item-separator

classref-enumeration

enum **ParticleFlags**: `🔗<enum_CPUParticles2D_ParticleFlags>`

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>` **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with `set_particle_flag()<class_CPUParticles2D_method_set_particle_flag>` to set `particle_flag_align_y<class_CPUParticles2D_property_particle_flag_align_y>`.

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>` **PARTICLE_FLAG_ROTATE_Y** = `1`

Present for consistency with 3D particle nodes, not used in 2D.

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>` **PARTICLE_FLAG_DISABLE_Z** = `2`

Present for consistency with 3D particle nodes, not used in 2D.

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>` **PARTICLE_FLAG_MAX** = `3`

Represents the size of the `ParticleFlags<enum_CPUParticles2D_ParticleFlags>` enum.

classref-item-separator

classref-enumeration

enum **EmissionShape**: `🔗<enum_CPUParticles2D_EmissionShape>`

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere flattened to two dimensions.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere flattened to two dimensions.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_RECTANGLE** = `3`

Particles will be emitted in the area of a rectangle.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among `emission_points<class_CPUParticles2D_property_emission_points>`. Particle color will be modulated by `emission_colors<class_CPUParticles2D_property_emission_colors>`.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among `emission_points<class_CPUParticles2D_property_emission_points>`. Particle velocity and rotation will be set based on `emission_normals<class_CPUParticles2D_property_emission_normals>`. Particle color will be modulated by `emission_colors<class_CPUParticles2D_property_emission_colors>`.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in the area of a ring parameterized by its outer and inner radius.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **EMISSION_SHAPE_MAX** = `7`

Represents the size of the `EmissionShape<enum_CPUParticles2D_EmissionShape>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **amount** = `8` `🔗<class_CPUParticles2D_property_amount>`

classref-property-setget

- `void (No return value.)` **set_amount**(value: `int<class_int>`)
- `int<class_int>` **get_amount**()

Number of particles emitted in one emission cycle.

classref-item-separator

classref-property

`Curve<class_Curve>` **angle_curve** `🔗<class_CPUParticles2D_property_angle_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's rotation will be animated along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **angle_max** = `0.0` `🔗<class_CPUParticles2D_property_angle_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial rotation applied to each particle, in degrees.

classref-item-separator

classref-property

`float<class_float>` **angle_min** = `0.0` `🔗<class_CPUParticles2D_property_angle_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `angle_max<class_CPUParticles2D_property_angle_max>`.

classref-item-separator

classref-property

`Curve<class_Curve>` **angular_velocity_curve** `🔗<class_CPUParticles2D_property_angular_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's angular velocity will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **angular_velocity_max** = `0.0` `🔗<class_CPUParticles2D_property_angular_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

classref-item-separator

classref-property

`float<class_float>` **angular_velocity_min** = `0.0` `🔗<class_CPUParticles2D_property_angular_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `angular_velocity_max<class_CPUParticles2D_property_angular_velocity_max>`.

classref-item-separator

classref-property

`Curve<class_Curve>` **anim_offset_curve** `🔗<class_CPUParticles2D_property_anim_offset_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's animation offset will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **anim_offset_max** = `0.0` `🔗<class_CPUParticles2D_property_anim_offset_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum animation offset that corresponds to frame index in the texture. `0` is the first frame, `1` is the last one. See `CanvasItemMaterial.particles_animation<class_CanvasItemMaterial_property_particles_animation>`.

classref-item-separator

classref-property

`float<class_float>` **anim_offset_min** = `0.0` `🔗<class_CPUParticles2D_property_anim_offset_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `anim_offset_max<class_CPUParticles2D_property_anim_offset_max>`.

classref-item-separator

classref-property

`Curve<class_Curve>` **anim_speed_curve** `🔗<class_CPUParticles2D_property_anim_speed_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's animation speed will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **anim_speed_max** = `0.0` `🔗<class_CPUParticles2D_property_anim_speed_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum particle animation speed. Animation speed of `1` means that the particles will make full `0` to `1` offset cycle during lifetime, `2` means `2` cycles etc.

With animation speed greater than `1`, remember to enable `CanvasItemMaterial.particles_anim_loop<class_CanvasItemMaterial_property_particles_anim_loop>` property if you want the animation to repeat.

classref-item-separator

classref-property

`float<class_float>` **anim_speed_min** = `0.0` `🔗<class_CPUParticles2D_property_anim_speed_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `anim_speed_max<class_CPUParticles2D_property_anim_speed_max>`.

classref-item-separator

classref-property

`Color<class_Color>` **color** = `Color(1, 1, 1, 1)` `🔗<class_CPUParticles2D_property_color>`

classref-property-setget

- `void (No return value.)` **set_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_color**()

Each particle's initial color. If `texture<class_CPUParticles2D_property_texture>` is defined, it will be multiplied by this color.

classref-item-separator

classref-property

`Gradient<class_Gradient>` **color_initial_ramp** `🔗<class_CPUParticles2D_property_color_initial_ramp>`

classref-property-setget

- `void (No return value.)` **set_color_initial_ramp**(value: `Gradient<class_Gradient>`)
- `Gradient<class_Gradient>` **get_color_initial_ramp**()

Each particle's initial color will vary along this `Gradient<class_Gradient>` (multiplied with `color<class_CPUParticles2D_property_color>`).

classref-item-separator

classref-property

`Gradient<class_Gradient>` **color_ramp** `🔗<class_CPUParticles2D_property_color_ramp>`

classref-property-setget

- `void (No return value.)` **set_color_ramp**(value: `Gradient<class_Gradient>`)
- `Gradient<class_Gradient>` **get_color_ramp**()

Each particle's color will vary along this `Gradient<class_Gradient>` over its lifetime (multiplied with `color<class_CPUParticles2D_property_color>`).

classref-item-separator

classref-property

`Curve<class_Curve>` **damping_curve** `🔗<class_CPUParticles2D_property_damping_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Damping will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **damping_max** = `0.0` `🔗<class_CPUParticles2D_property_damping_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

The maximum rate at which particles lose velocity. For example value of `100` means that the particle will go from `100` velocity to `0` in `1` second.

classref-item-separator

classref-property

`float<class_float>` **damping_min** = `0.0` `🔗<class_CPUParticles2D_property_damping_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `damping_max<class_CPUParticles2D_property_damping_max>`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **direction** = `Vector2(1, 0)` `🔗<class_CPUParticles2D_property_direction>`

classref-property-setget

- `void (No return value.)` **set_direction**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_direction**()

Unit vector specifying the particles' emission direction.

classref-item-separator

classref-property

`DrawOrder<enum_CPUParticles2D_DrawOrder>` **draw_order** = `0` `🔗<class_CPUParticles2D_property_draw_order>`

classref-property-setget

- `void (No return value.)` **set_draw_order**(value: `DrawOrder<enum_CPUParticles2D_DrawOrder>`)
- `DrawOrder<enum_CPUParticles2D_DrawOrder>` **get_draw_order**()

Particle draw order.

classref-item-separator

classref-property

`PackedColorArray<class_PackedColorArray>` **emission_colors** `🔗<class_CPUParticles2D_property_emission_colors>`

classref-property-setget

- `void (No return value.)` **set_emission_colors**(value: `PackedColorArray<class_PackedColorArray>`)
- `PackedColorArray<class_PackedColorArray>` **get_emission_colors**()

Sets the `Color<class_Color>`s to modulate particles by when using `EMISSION_SHAPE_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS>` or `EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedColorArray<class_PackedColorArray>` for more details.

classref-item-separator

classref-property

`PackedVector2Array<class_PackedVector2Array>` **emission_normals** `🔗<class_CPUParticles2D_property_emission_normals>`

classref-property-setget

- `void (No return value.)` **set_emission_normals**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_emission_normals**()

Sets the direction the particles will be emitted in when using `EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.

classref-item-separator

classref-property

`PackedVector2Array<class_PackedVector2Array>` **emission_points** `🔗<class_CPUParticles2D_property_emission_points>`

classref-property-setget

- `void (No return value.)` **set_emission_points**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_emission_points**()

Sets the initial positions to spawn particles when using `EMISSION_SHAPE_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS>` or `EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **emission_rect_extents** `🔗<class_CPUParticles2D_property_emission_rect_extents>`

classref-property-setget

- `void (No return value.)` **set_emission_rect_extents**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_emission_rect_extents**()

The rectangle's extents if `emission_shape<class_CPUParticles2D_property_emission_shape>` is set to `EMISSION_SHAPE_RECTANGLE<class_CPUParticles2D_constant_EMISSION_SHAPE_RECTANGLE>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_inner_radius** `🔗<class_CPUParticles2D_property_emission_ring_inner_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_inner_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_inner_radius**()

The ring's inner radius if `emission_shape<class_CPUParticles2D_property_emission_shape>` is set to `EMISSION_SHAPE_RING<class_CPUParticles2D_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_radius** `🔗<class_CPUParticles2D_property_emission_ring_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_radius**()

The ring's outer radius if `emission_shape<class_CPUParticles2D_property_emission_shape>` is set to `EMISSION_SHAPE_RING<class_CPUParticles2D_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`EmissionShape<enum_CPUParticles2D_EmissionShape>` **emission_shape** = `0` `🔗<class_CPUParticles2D_property_emission_shape>`

classref-property-setget

- `void (No return value.)` **set_emission_shape**(value: `EmissionShape<enum_CPUParticles2D_EmissionShape>`)
- `EmissionShape<enum_CPUParticles2D_EmissionShape>` **get_emission_shape**()

Particles will be emitted inside this region.

classref-item-separator

classref-property

`float<class_float>` **emission_sphere_radius** `🔗<class_CPUParticles2D_property_emission_sphere_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_sphere_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_sphere_radius**()

The sphere's radius if `emission_shape<class_CPUParticles2D_property_emission_shape>` is set to `EMISSION_SHAPE_SPHERE<class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE>`.

classref-item-separator

classref-property

`bool<class_bool>` **emitting** = `true` `🔗<class_CPUParticles2D_property_emitting>`

classref-property-setget

- `void (No return value.)` **set_emitting**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_emitting**()

If `true`, particles are being emitted. `emitting<class_CPUParticles2D_property_emitting>` can be used to start and stop particles from emitting. However, if `one_shot<class_CPUParticles2D_property_one_shot>` is `true` setting `emitting<class_CPUParticles2D_property_emitting>` to `true` will not restart the emission cycle until after all active particles finish processing. You can use the `finished<class_CPUParticles2D_signal_finished>` signal to be notified once all active particles finish processing.

classref-item-separator

classref-property

`float<class_float>` **explosiveness** = `0.0` `🔗<class_CPUParticles2D_property_explosiveness>`

classref-property-setget

- `void (No return value.)` **set_explosiveness_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

classref-item-separator

classref-property

`int<class_int>` **fixed_fps** = `0` `🔗<class_CPUParticles2D_property_fixed_fps>`

classref-property-setget

- `void (No return value.)` **set_fixed_fps**(value: `int<class_int>`)
- `int<class_int>` **get_fixed_fps**()

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the simulation of the particle system itself.

classref-item-separator

classref-property

`bool<class_bool>` **fract_delta** = `true` `🔗<class_CPUParticles2D_property_fract_delta>`

classref-property-setget

- `void (No return value.)` **set_fractional_delta**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother particles display effect.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **gravity** = `Vector2(0, 980)` `🔗<class_CPUParticles2D_property_gravity>`

classref-property-setget

- `void (No return value.)` **set_gravity**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_gravity**()

Gravity applied to every particle.

classref-item-separator

classref-property

`Curve<class_Curve>` **hue_variation_curve** `🔗<class_CPUParticles2D_property_hue_variation_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's hue will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **hue_variation_max** = `0.0` `🔗<class_CPUParticles2D_property_hue_variation_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial hue variation applied to each particle. It will shift the particle color's hue.

classref-item-separator

classref-property

`float<class_float>` **hue_variation_min** = `0.0` `🔗<class_CPUParticles2D_property_hue_variation_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `hue_variation_max<class_CPUParticles2D_property_hue_variation_max>`.

classref-item-separator

classref-property

`float<class_float>` **initial_velocity_max** = `0.0` `🔗<class_CPUParticles2D_property_initial_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial velocity magnitude for each particle. Direction comes from `direction<class_CPUParticles2D_property_direction>` and `spread<class_CPUParticles2D_property_spread>`.

classref-item-separator

classref-property

`float<class_float>` **initial_velocity_min** = `0.0` `🔗<class_CPUParticles2D_property_initial_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `initial_velocity_max<class_CPUParticles2D_property_initial_velocity_max>`.

classref-item-separator

classref-property

`float<class_float>` **lifetime** = `1.0` `🔗<class_CPUParticles2D_property_lifetime>`

classref-property-setget

- `void (No return value.)` **set_lifetime**(value: `float<class_float>`)
- `float<class_float>` **get_lifetime**()

Amount of time each particle will exist.

classref-item-separator

classref-property

`float<class_float>` **lifetime_randomness** = `0.0` `🔗<class_CPUParticles2D_property_lifetime_randomness>`

classref-property-setget

- `void (No return value.)` **set_lifetime_randomness**(value: `float<class_float>`)
- `float<class_float>` **get_lifetime_randomness**()

Particle lifetime randomness ratio.

classref-item-separator

classref-property

`Curve<class_Curve>` **linear_accel_curve** `🔗<class_CPUParticles2D_property_linear_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's linear acceleration will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **linear_accel_max** = `0.0` `🔗<class_CPUParticles2D_property_linear_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum linear acceleration applied to each particle in the direction of motion.

classref-item-separator

classref-property

`float<class_float>` **linear_accel_min** = `0.0` `🔗<class_CPUParticles2D_property_linear_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `linear_accel_max<class_CPUParticles2D_property_linear_accel_max>`.

classref-item-separator

classref-property

`bool<class_bool>` **local_coords** = `false` `🔗<class_CPUParticles2D_property_local_coords>`

classref-property-setget

- `void (No return value.)` **set_use_local_coordinates**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_local_coordinates**()

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles2D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles2D** node (and its parents) when it is moved or rotated.

classref-item-separator

classref-property

`bool<class_bool>` **one_shot** = `false` `🔗<class_CPUParticles2D_property_one_shot>`

classref-property-setget

- `void (No return value.)` **set_one_shot**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

classref-item-separator

classref-property

`Curve<class_Curve>` **orbit_velocity_curve** `🔗<class_CPUParticles2D_property_orbit_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's orbital velocity will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **orbit_velocity_max** = `0.0` `🔗<class_CPUParticles2D_property_orbit_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum orbital velocity applied to each particle. Makes the particles circle around origin. Specified in number of full rotations around origin per second.

classref-item-separator

classref-property

`float<class_float>` **orbit_velocity_min** = `0.0` `🔗<class_CPUParticles2D_property_orbit_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `orbit_velocity_max<class_CPUParticles2D_property_orbit_velocity_max>`.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_align_y** = `false` `🔗<class_CPUParticles2D_property_particle_flag_align_y>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles2D_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles2D_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Align Y axis of particle with the direction of its velocity.

classref-item-separator

classref-property

`float<class_float>` **preprocess** = `0.0` `🔗<class_CPUParticles2D_property_preprocess>`

classref-property-setget

- `void (No return value.)` **set_pre_process_time**(value: `float<class_float>`)
- `float<class_float>` **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

classref-item-separator

classref-property

`Curve<class_Curve>` **radial_accel_curve** `🔗<class_CPUParticles2D_property_radial_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's radial acceleration will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **radial_accel_max** = `0.0` `🔗<class_CPUParticles2D_property_radial_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum radial acceleration applied to each particle. Makes particle accelerate away from the origin or towards it if negative.

classref-item-separator

classref-property

`float<class_float>` **radial_accel_min** = `0.0` `🔗<class_CPUParticles2D_property_radial_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `radial_accel_max<class_CPUParticles2D_property_radial_accel_max>`.

classref-item-separator

classref-property

`float<class_float>` **randomness** = `0.0` `🔗<class_CPUParticles2D_property_randomness>`

classref-property-setget

- `void (No return value.)` **set_randomness_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_randomness_ratio**()

Emission lifetime randomness ratio.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_amount_curve** `🔗<class_CPUParticles2D_property_scale_amount_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's scale will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **scale_amount_max** = `1.0` `🔗<class_CPUParticles2D_property_scale_amount_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial scale applied to each particle.

classref-item-separator

classref-property

`float<class_float>` **scale_amount_min** = `1.0` `🔗<class_CPUParticles2D_property_scale_amount_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `scale_amount_max<class_CPUParticles2D_property_scale_amount_max>`.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_curve_x** `🔗<class_CPUParticles2D_property_scale_curve_x>`

classref-property-setget

- `void (No return value.)` **set_scale_curve_x**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_scale_curve_x**()

Each particle's horizontal scale will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

`split_scale<class_CPUParticles2D_property_split_scale>` must be enabled.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_curve_y** `🔗<class_CPUParticles2D_property_scale_curve_y>`

classref-property-setget

- `void (No return value.)` **set_scale_curve_y**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_scale_curve_y**()

Each particle's vertical scale will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

`split_scale<class_CPUParticles2D_property_split_scale>` must be enabled.

classref-item-separator

classref-property

`int<class_int>` **seed** = `0` `🔗<class_CPUParticles2D_property_seed>`

classref-property-setget

- `void (No return value.)` **set_seed**(value: `int<class_int>`)
- `int<class_int>` **get_seed**()

Sets the random seed used by the particle system. Only effective if `use_fixed_seed<class_CPUParticles2D_property_use_fixed_seed>` is `true`.

classref-item-separator

classref-property

`float<class_float>` **speed_scale** = `1.0` `🔗<class_CPUParticles2D_property_speed_scale>`

classref-property-setget

- `void (No return value.)` **set_speed_scale**(value: `float<class_float>`)
- `float<class_float>` **get_speed_scale**()

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

classref-item-separator

classref-property

`bool<class_bool>` **split_scale** = `false` `🔗<class_CPUParticles2D_property_split_scale>`

classref-property-setget

- `void (No return value.)` **set_split_scale**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_split_scale**()

If `true`, the scale curve will be split into x and y components. See `scale_curve_x<class_CPUParticles2D_property_scale_curve_x>` and `scale_curve_y<class_CPUParticles2D_property_scale_curve_y>`.

classref-item-separator

classref-property

`float<class_float>` **spread** = `45.0` `🔗<class_CPUParticles2D_property_spread>`

classref-property-setget

- `void (No return value.)` **set_spread**(value: `float<class_float>`)
- `float<class_float>` **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees.

classref-item-separator

classref-property

`Curve<class_Curve>` **tangential_accel_curve** `🔗<class_CPUParticles2D_property_tangential_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's tangential acceleration will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **tangential_accel_max** = `0.0` `🔗<class_CPUParticles2D_property_tangential_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum tangential acceleration applied to each particle. Tangential acceleration is perpendicular to the particle's velocity giving the particles a swirling motion.

classref-item-separator

classref-property

`float<class_float>` **tangential_accel_min** = `0.0` `🔗<class_CPUParticles2D_property_tangential_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum equivalent of `tangential_accel_max<class_CPUParticles2D_property_tangential_accel_max>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_CPUParticles2D_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

Particle texture. If `null`, particles will be squares.

classref-item-separator

classref-property

`bool<class_bool>` **use_fixed_seed** = `false` `🔗<class_CPUParticles2D_property_use_fixed_seed>`

classref-property-setget

- `void (No return value.)` **set_use_fixed_seed**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using the seed defined in `seed<class_CPUParticles2D_property_seed>`. This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **convert_from_particles**(particles: `Node<class_Node>`) `🔗<class_CPUParticles2D_method_convert_from_particles>`

Sets this node's properties to match a given `GPUParticles2D<class_GPUParticles2D>` node with an assigned `ParticleProcessMaterial<class_ParticleProcessMaterial>`.

classref-item-separator

classref-method

`Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles2D_method_get_param_curve>`

Returns the `Curve<class_Curve>` of the parameter specified by `Parameter<enum_CPUParticles2D_Parameter>`.

classref-item-separator

classref-method

`float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles2D_method_get_param_max>`

Returns the maximum value range for the given parameter.

classref-item-separator

classref-method

`float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles2D_method_get_param_min>`

Returns the minimum value range for the given parameter.

classref-item-separator

classref-method

`bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles2D_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles2D_method_get_particle_flag>`

Returns the enabled state of the given particle flag.

classref-item-separator

classref-method

`void (No return value.)` **request_particles_process**(process_time: `float<class_float>`, process_time_residual: `float<class_float>` = 0.0) `🔗<class_CPUParticles2D_method_request_particles_process>`

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with `speed_scale<class_CPUParticles2D_property_speed_scale>` set to `0.0`, this is useful to be able to seek a particle system timeline.

classref-item-separator

classref-method

`void (No return value.)` **restart**(keep_seed: `bool<class_bool>` = false) `🔗<class_CPUParticles2D_method_restart>`

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

classref-item-separator

classref-method

`void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles2D_Parameter>`, curve: `Curve<class_Curve>`) `🔗<class_CPUParticles2D_method_set_param_curve>`

Sets the `Curve<class_Curve>` of the parameter specified by `Parameter<enum_CPUParticles2D_Parameter>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-method

`void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`) `🔗<class_CPUParticles2D_method_set_param_max>`

Sets the maximum value for the given parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles2D_Parameter>`, value: `float<class_float>`) `🔗<class_CPUParticles2D_method_set_param_min>`

Sets the minimum value for the given parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles2D_ParticleFlags>`, enable: `bool<class_bool>`) `🔗<class_CPUParticles2D_method_set_particle_flag>`

Enables or disables the given particle flag.