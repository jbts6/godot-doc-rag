github_url
hide

# CPUParticles3D

**Inherits:** `GeometryInstance3D<class_GeometryInstance3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A CPU-based 3D particle emitter.

classref-introduction-group

## Description

CPU-based 3D particle node used to create a variety of particle systems and effects.

See also `GPUParticles3D<class_GPUParticles3D>`, which provides the same functionality with hardware acceleration, but may not run on older devices.

classref-introduction-group

## Tutorials

- `Particle systems (3D) <../tutorials/3d/particles/index>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**finished**() `🔗<class_CPUParticles3D_signal_finished>`

Emitted when all active particles have finished processing. When `one_shot<class_CPUParticles3D_property_one_shot>` is disabled, particles will process continuously, so this is never emitted.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DrawOrder**: `🔗<enum_CPUParticles3D_DrawOrder>`

classref-enumeration-constant

`DrawOrder<enum_CPUParticles3D_DrawOrder>` **DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

classref-enumeration-constant

`DrawOrder<enum_CPUParticles3D_DrawOrder>` **DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the particle with the highest lifetime is drawn at the front.

classref-enumeration-constant

`DrawOrder<enum_CPUParticles3D_DrawOrder>` **DRAW_ORDER_VIEW_DEPTH** = `2`

Particles are drawn in order of depth.

classref-item-separator

classref-enumeration

enum **Parameter**: `🔗<enum_CPUParticles3D_Parameter>`

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set initial velocity properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_ANGULAR_VELOCITY** = `1`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set angular velocity properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_ORBIT_VELOCITY** = `2`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set orbital velocity properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_LINEAR_ACCEL** = `3`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set linear acceleration properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_RADIAL_ACCEL** = `4`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set radial acceleration properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_TANGENTIAL_ACCEL** = `5`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set tangential acceleration properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_DAMPING** = `6`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set damping properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_ANGLE** = `7`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set angle properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_SCALE** = `8`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set scale properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_HUE_VARIATION** = `9`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set hue variation properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_ANIM_SPEED** = `10`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set animation speed properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_ANIM_OFFSET** = `11`

Use with `set_param_min()<class_CPUParticles3D_method_set_param_min>`, `set_param_max()<class_CPUParticles3D_method_set_param_max>`, and `set_param_curve()<class_CPUParticles3D_method_set_param_curve>` to set animation offset properties.

classref-enumeration-constant

`Parameter<enum_CPUParticles3D_Parameter>` **PARAM_MAX** = `12`

Represents the size of the `Parameter<enum_CPUParticles3D_Parameter>` enum.

classref-item-separator

classref-enumeration

enum **ParticleFlags**: `🔗<enum_CPUParticles3D_ParticleFlags>`

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles3D_ParticleFlags>` **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with `set_particle_flag()<class_CPUParticles3D_method_set_particle_flag>` to set `particle_flag_align_y<class_CPUParticles3D_property_particle_flag_align_y>`.

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles3D_ParticleFlags>` **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with `set_particle_flag()<class_CPUParticles3D_method_set_particle_flag>` to set `particle_flag_rotate_y<class_CPUParticles3D_property_particle_flag_rotate_y>`.

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles3D_ParticleFlags>` **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with `set_particle_flag()<class_CPUParticles3D_method_set_particle_flag>` to set `particle_flag_disable_z<class_CPUParticles3D_property_particle_flag_disable_z>`.

classref-enumeration-constant

`ParticleFlags<enum_CPUParticles3D_ParticleFlags>` **PARTICLE_FLAG_MAX** = `3`

Represents the size of the `ParticleFlags<enum_CPUParticles3D_ParticleFlags>` enum.

classref-item-separator

classref-enumeration

enum **EmissionShape**: `🔗<enum_CPUParticles3D_EmissionShape>`

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among `emission_points<class_CPUParticles3D_property_emission_points>`. Particle color will be modulated by `emission_colors<class_CPUParticles3D_property_emission_colors>`.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among `emission_points<class_CPUParticles3D_property_emission_points>`. Particle velocity and rotation will be set based on `emission_normals<class_CPUParticles3D_property_emission_normals>`. Particle color will be modulated by `emission_colors<class_CPUParticles3D_property_emission_colors>`.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

classref-enumeration-constant

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **EMISSION_SHAPE_MAX** = `7`

Represents the size of the `EmissionShape<enum_CPUParticles3D_EmissionShape>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **amount** = `8` `🔗<class_CPUParticles3D_property_amount>`

classref-property-setget

- `void (No return value.)` **set_amount**(value: `int<class_int>`)
- `int<class_int>` **get_amount**()

Number of particles emitted in one emission cycle.

classref-item-separator

classref-property

`Curve<class_Curve>` **angle_curve** `🔗<class_CPUParticles3D_property_angle_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's rotation will be animated along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **angle_max** = `0.0` `🔗<class_CPUParticles3D_property_angle_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum angle.

classref-item-separator

classref-property

`float<class_float>` **angle_min** = `0.0` `🔗<class_CPUParticles3D_property_angle_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum angle.

classref-item-separator

classref-property

`Curve<class_Curve>` **angular_velocity_curve** `🔗<class_CPUParticles3D_property_angular_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's angular velocity (rotation speed) will vary along this `Curve<class_Curve>` over its lifetime. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **angular_velocity_max** = `0.0` `🔗<class_CPUParticles3D_property_angular_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

classref-item-separator

classref-property

`float<class_float>` **angular_velocity_min** = `0.0` `🔗<class_CPUParticles3D_property_angular_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum initial angular velocity (rotation speed) applied to each particle in *degrees* per second.

classref-item-separator

classref-property

`Curve<class_Curve>` **anim_offset_curve** `🔗<class_CPUParticles3D_property_anim_offset_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's animation offset will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **anim_offset_max** = `0.0` `🔗<class_CPUParticles3D_property_anim_offset_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum animation offset.

classref-item-separator

classref-property

`float<class_float>` **anim_offset_min** = `0.0` `🔗<class_CPUParticles3D_property_anim_offset_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum animation offset.

classref-item-separator

classref-property

`Curve<class_Curve>` **anim_speed_curve** `🔗<class_CPUParticles3D_property_anim_speed_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's animation speed will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **anim_speed_max** = `0.0` `🔗<class_CPUParticles3D_property_anim_speed_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum particle animation speed.

classref-item-separator

classref-property

`float<class_float>` **anim_speed_min** = `0.0` `🔗<class_CPUParticles3D_property_anim_speed_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum particle animation speed.

classref-item-separator

classref-property

`Color<class_Color>` **color** = `Color(1, 1, 1, 1)` `🔗<class_CPUParticles3D_property_color>`

classref-property-setget

- `void (No return value.)` **set_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_color**()

Each particle's initial color.

**Note:** `color<class_CPUParticles3D_property_color>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `color<class_CPUParticles3D_property_color>` will have no visible effect.

classref-item-separator

classref-property

`Gradient<class_Gradient>` **color_initial_ramp** `🔗<class_CPUParticles3D_property_color_initial_ramp>`

classref-property-setget

- `void (No return value.)` **set_color_initial_ramp**(value: `Gradient<class_Gradient>`)
- `Gradient<class_Gradient>` **get_color_initial_ramp**()

Each particle's initial color will vary along this `Gradient<class_Gradient>` (multiplied with `color<class_CPUParticles3D_property_color>`).

**Note:** `color_initial_ramp<class_CPUParticles3D_property_color_initial_ramp>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `color_initial_ramp<class_CPUParticles3D_property_color_initial_ramp>` will have no visible effect.

classref-item-separator

classref-property

`Gradient<class_Gradient>` **color_ramp** `🔗<class_CPUParticles3D_property_color_ramp>`

classref-property-setget

- `void (No return value.)` **set_color_ramp**(value: `Gradient<class_Gradient>`)
- `Gradient<class_Gradient>` **get_color_ramp**()

Each particle's color will vary along this `Gradient<class_Gradient>` over its lifetime (multiplied with `color<class_CPUParticles3D_property_color>`).

**Note:** `color_ramp<class_CPUParticles3D_property_color_ramp>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `color_ramp<class_CPUParticles3D_property_color_ramp>` will have no visible effect.

classref-item-separator

classref-property

`Curve<class_Curve>` **damping_curve** `🔗<class_CPUParticles3D_property_damping_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Damping will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **damping_max** = `0.0` `🔗<class_CPUParticles3D_property_damping_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum damping.

classref-item-separator

classref-property

`float<class_float>` **damping_min** = `0.0` `🔗<class_CPUParticles3D_property_damping_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum damping.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **direction** = `Vector3(1, 0, 0)` `🔗<class_CPUParticles3D_property_direction>`

classref-property-setget

- `void (No return value.)` **set_direction**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_direction**()

Unit vector specifying the particles' emission direction.

classref-item-separator

classref-property

`DrawOrder<enum_CPUParticles3D_DrawOrder>` **draw_order** = `0` `🔗<class_CPUParticles3D_property_draw_order>`

classref-property-setget

- `void (No return value.)` **set_draw_order**(value: `DrawOrder<enum_CPUParticles3D_DrawOrder>`)
- `DrawOrder<enum_CPUParticles3D_DrawOrder>` **get_draw_order**()

Particle draw order.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **emission_box_extents** `🔗<class_CPUParticles3D_property_emission_box_extents>`

classref-property-setget

- `void (No return value.)` **set_emission_box_extents**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_emission_box_extents**()

The rectangle's extents if `emission_shape<class_CPUParticles3D_property_emission_shape>` is set to `EMISSION_SHAPE_BOX<class_CPUParticles3D_constant_EMISSION_SHAPE_BOX>`.

classref-item-separator

classref-property

`PackedColorArray<class_PackedColorArray>` **emission_colors** = `PackedColorArray()` `🔗<class_CPUParticles3D_property_emission_colors>`

classref-property-setget

- `void (No return value.)` **set_emission_colors**(value: `PackedColorArray<class_PackedColorArray>`)
- `PackedColorArray<class_PackedColorArray>` **get_emission_colors**()

Sets the `Color<class_Color>`s to modulate particles by when using `EMISSION_SHAPE_POINTS<class_CPUParticles3D_constant_EMISSION_SHAPE_POINTS>` or `EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

**Note:** `emission_colors<class_CPUParticles3D_property_emission_colors>` multiplies the particle mesh's vertex colors. To have a visible effect on a `BaseMaterial3D<class_BaseMaterial3D>`, `BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>` *must* be `true`. For a `ShaderMaterial<class_ShaderMaterial>`, `ALBEDO *= COLOR.rgb;` must be inserted in the shader's `fragment()` function. Otherwise, `emission_colors<class_CPUParticles3D_property_emission_colors>` will have no visible effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedColorArray<class_PackedColorArray>` for more details.

classref-item-separator

classref-property

`PackedVector3Array<class_PackedVector3Array>` **emission_normals** `🔗<class_CPUParticles3D_property_emission_normals>`

classref-property-setget

- `void (No return value.)` **set_emission_normals**(value: `PackedVector3Array<class_PackedVector3Array>`)
- `PackedVector3Array<class_PackedVector3Array>` **get_emission_normals**()

Sets the direction the particles will be emitted in when using `EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector3Array<class_PackedVector3Array>` for more details.

classref-item-separator

classref-property

`PackedVector3Array<class_PackedVector3Array>` **emission_points** `🔗<class_CPUParticles3D_property_emission_points>`

classref-property-setget

- `void (No return value.)` **set_emission_points**(value: `PackedVector3Array<class_PackedVector3Array>`)
- `PackedVector3Array<class_PackedVector3Array>` **get_emission_points**()

Sets the initial positions to spawn particles when using `EMISSION_SHAPE_POINTS<class_CPUParticles3D_constant_EMISSION_SHAPE_POINTS>` or `EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles3D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector3Array<class_PackedVector3Array>` for more details.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **emission_ring_axis** `🔗<class_CPUParticles3D_property_emission_ring_axis>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_axis**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_emission_ring_axis**()

The axis of the ring when using the emitter `EMISSION_SHAPE_RING<class_CPUParticles3D_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_cone_angle** `🔗<class_CPUParticles3D_property_emission_ring_cone_angle>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_cone_angle**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_cone_angle**()

The angle of the cone when using the emitter `EMISSION_SHAPE_RING<class_CPUParticles3D_constant_EMISSION_SHAPE_RING>`. The default angle of 90 degrees results in a ring, while an angle of 0 degrees results in a cone. Intermediate values will result in a ring where one end is larger than the other.

**Note:** Depending on `emission_ring_height<class_CPUParticles3D_property_emission_ring_height>`, the angle may be clamped if the ring's end is reached to form a perfect cone.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_height** `🔗<class_CPUParticles3D_property_emission_ring_height>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_height**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_height**()

The height of the ring when using the emitter `EMISSION_SHAPE_RING<class_CPUParticles3D_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_inner_radius** `🔗<class_CPUParticles3D_property_emission_ring_inner_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_inner_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_inner_radius**()

The inner radius of the ring when using the emitter `EMISSION_SHAPE_RING<class_CPUParticles3D_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`float<class_float>` **emission_ring_radius** `🔗<class_CPUParticles3D_property_emission_ring_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_ring_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_ring_radius**()

The radius of the ring when using the emitter `EMISSION_SHAPE_RING<class_CPUParticles3D_constant_EMISSION_SHAPE_RING>`.

classref-item-separator

classref-property

`EmissionShape<enum_CPUParticles3D_EmissionShape>` **emission_shape** = `0` `🔗<class_CPUParticles3D_property_emission_shape>`

classref-property-setget

- `void (No return value.)` **set_emission_shape**(value: `EmissionShape<enum_CPUParticles3D_EmissionShape>`)
- `EmissionShape<enum_CPUParticles3D_EmissionShape>` **get_emission_shape**()

Particles will be emitted inside this region.

classref-item-separator

classref-property

`float<class_float>` **emission_sphere_radius** `🔗<class_CPUParticles3D_property_emission_sphere_radius>`

classref-property-setget

- `void (No return value.)` **set_emission_sphere_radius**(value: `float<class_float>`)
- `float<class_float>` **get_emission_sphere_radius**()

The sphere's radius if `EmissionShape<enum_CPUParticles3D_EmissionShape>` is set to `EMISSION_SHAPE_SPHERE<class_CPUParticles3D_constant_EMISSION_SHAPE_SPHERE>`.

classref-item-separator

classref-property

`bool<class_bool>` **emitting** = `true` `🔗<class_CPUParticles3D_property_emitting>`

classref-property-setget

- `void (No return value.)` **set_emitting**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_emitting**()

If `true`, particles are being emitted. `emitting<class_CPUParticles3D_property_emitting>` can be used to start and stop particles from emitting. However, if `one_shot<class_CPUParticles3D_property_one_shot>` is `true` setting `emitting<class_CPUParticles3D_property_emitting>` to `true` will not restart the emission cycle until after all active particles finish processing. You can use the `finished<class_CPUParticles3D_signal_finished>` signal to be notified once all active particles finish processing.

classref-item-separator

classref-property

`float<class_float>` **explosiveness** = `0.0` `🔗<class_CPUParticles3D_property_explosiveness>`

classref-property-setget

- `void (No return value.)` **set_explosiveness_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than `0`, there will be a gap in emissions before the next cycle begins.

classref-item-separator

classref-property

`int<class_int>` **fixed_fps** = `0` `🔗<class_CPUParticles3D_property_fixed_fps>`

classref-property-setget

- `void (No return value.)` **set_fixed_fps**(value: `int<class_int>`)
- `int<class_int>` **get_fixed_fps**()

The particle system's frame rate is fixed to a value. For example, changing the value to 2 will make the particles render at 2 frames per second. Note this does not slow down the particle system itself.

classref-item-separator

classref-property

`float<class_float>` **flatness** = `0.0` `🔗<class_CPUParticles3D_property_flatness>`

classref-property-setget

- `void (No return value.)` **set_flatness**(value: `float<class_float>`)
- `float<class_float>` **get_flatness**()

Amount of `spread<class_CPUParticles3D_property_spread>` in Y/Z plane. A value of `1` restricts particles to X/Z plane.

classref-item-separator

classref-property

`bool<class_bool>` **fract_delta** = `true` `🔗<class_CPUParticles3D_property_fract_delta>`

classref-property-setget

- `void (No return value.)` **set_fractional_delta**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother particles display effect.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **gravity** = `Vector3(0, -9.8, 0)` `🔗<class_CPUParticles3D_property_gravity>`

classref-property-setget

- `void (No return value.)` **set_gravity**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_gravity**()

Gravity applied to every particle.

classref-item-separator

classref-property

`Curve<class_Curve>` **hue_variation_curve** `🔗<class_CPUParticles3D_property_hue_variation_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's hue will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **hue_variation_max** = `0.0` `🔗<class_CPUParticles3D_property_hue_variation_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum hue variation.

classref-item-separator

classref-property

`float<class_float>` **hue_variation_min** = `0.0` `🔗<class_CPUParticles3D_property_hue_variation_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum hue variation.

classref-item-separator

classref-property

`float<class_float>` **initial_velocity_max** = `0.0` `🔗<class_CPUParticles3D_property_initial_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum value of the initial velocity.

classref-item-separator

classref-property

`float<class_float>` **initial_velocity_min** = `0.0` `🔗<class_CPUParticles3D_property_initial_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum value of the initial velocity.

classref-item-separator

classref-property

`float<class_float>` **lifetime** = `1.0` `🔗<class_CPUParticles3D_property_lifetime>`

classref-property-setget

- `void (No return value.)` **set_lifetime**(value: `float<class_float>`)
- `float<class_float>` **get_lifetime**()

Amount of time each particle will exist.

classref-item-separator

classref-property

`float<class_float>` **lifetime_randomness** = `0.0` `🔗<class_CPUParticles3D_property_lifetime_randomness>`

classref-property-setget

- `void (No return value.)` **set_lifetime_randomness**(value: `float<class_float>`)
- `float<class_float>` **get_lifetime_randomness**()

Particle lifetime randomness ratio.

classref-item-separator

classref-property

`Curve<class_Curve>` **linear_accel_curve** `🔗<class_CPUParticles3D_property_linear_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's linear acceleration will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **linear_accel_max** = `0.0` `🔗<class_CPUParticles3D_property_linear_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum linear acceleration.

classref-item-separator

classref-property

`float<class_float>` **linear_accel_min** = `0.0` `🔗<class_CPUParticles3D_property_linear_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum linear acceleration.

classref-item-separator

classref-property

`bool<class_bool>` **local_coords** = `false` `🔗<class_CPUParticles3D_property_local_coords>`

classref-property-setget

- `void (No return value.)` **set_use_local_coordinates**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_local_coordinates**()

If `true`, particles use the parent node's coordinate space (known as local coordinates). This will cause particles to move and rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated. If `false`, particles use global coordinates; they will not move or rotate along the **CPUParticles3D** node (and its parents) when it is moved or rotated.

classref-item-separator

classref-property

`Mesh<class_Mesh>` **mesh** `🔗<class_CPUParticles3D_property_mesh>`

classref-property-setget

- `void (No return value.)` **set_mesh**(value: `Mesh<class_Mesh>`)
- `Mesh<class_Mesh>` **get_mesh**()

The `Mesh<class_Mesh>` used for each particle. If `null`, particles will be spheres.

classref-item-separator

classref-property

`bool<class_bool>` **one_shot** = `false` `🔗<class_CPUParticles3D_property_one_shot>`

classref-property-setget

- `void (No return value.)` **set_one_shot**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle, emission will stop at the cycle's end.

classref-item-separator

classref-property

`Curve<class_Curve>` **orbit_velocity_curve** `🔗<class_CPUParticles3D_property_orbit_velocity_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's orbital velocity will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **orbit_velocity_max** `🔗<class_CPUParticles3D_property_orbit_velocity_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum orbit velocity.

classref-item-separator

classref-property

`float<class_float>` **orbit_velocity_min** `🔗<class_CPUParticles3D_property_orbit_velocity_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum orbit velocity.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_align_y** = `false` `🔗<class_CPUParticles3D_property_particle_flag_align_y>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Align Y axis of particle with the direction of its velocity.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_disable_z** = `false` `🔗<class_CPUParticles3D_property_particle_flag_disable_z>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, particles will not move on the Z axis.

classref-item-separator

classref-property

`bool<class_bool>` **particle_flag_rotate_y** = `false` `🔗<class_CPUParticles3D_property_particle_flag_rotate_y>`

classref-property-setget

- `void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`, enable: `bool<class_bool>`)
- `bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, particles rotate around Y axis by `angle_min<class_CPUParticles3D_property_angle_min>`.

classref-item-separator

classref-property

`float<class_float>` **preprocess** = `0.0` `🔗<class_CPUParticles3D_property_preprocess>`

classref-property-setget

- `void (No return value.)` **set_pre_process_time**(value: `float<class_float>`)
- `float<class_float>` **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

classref-item-separator

classref-property

`Curve<class_Curve>` **radial_accel_curve** `🔗<class_CPUParticles3D_property_radial_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's radial acceleration will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **radial_accel_max** = `0.0` `🔗<class_CPUParticles3D_property_radial_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum radial acceleration.

classref-item-separator

classref-property

`float<class_float>` **radial_accel_min** = `0.0` `🔗<class_CPUParticles3D_property_radial_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum radial acceleration.

classref-item-separator

classref-property

`float<class_float>` **randomness** = `0.0` `🔗<class_CPUParticles3D_property_randomness>`

classref-property-setget

- `void (No return value.)` **set_randomness_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_randomness_ratio**()

Emission lifetime randomness ratio.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_amount_curve** `🔗<class_CPUParticles3D_property_scale_amount_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's scale will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **scale_amount_max** = `1.0` `🔗<class_CPUParticles3D_property_scale_amount_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum scale.

classref-item-separator

classref-property

`float<class_float>` **scale_amount_min** = `1.0` `🔗<class_CPUParticles3D_property_scale_amount_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum scale.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_curve_x** `🔗<class_CPUParticles3D_property_scale_curve_x>`

classref-property-setget

- `void (No return value.)` **set_scale_curve_x**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_scale_curve_x**()

Curve for the scale over life, along the x axis.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_curve_y** `🔗<class_CPUParticles3D_property_scale_curve_y>`

classref-property-setget

- `void (No return value.)` **set_scale_curve_y**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_scale_curve_y**()

Curve for the scale over life, along the y axis.

classref-item-separator

classref-property

`Curve<class_Curve>` **scale_curve_z** `🔗<class_CPUParticles3D_property_scale_curve_z>`

classref-property-setget

- `void (No return value.)` **set_scale_curve_z**(value: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_scale_curve_z**()

Curve for the scale over life, along the z axis.

classref-item-separator

classref-property

`int<class_int>` **seed** = `0` `🔗<class_CPUParticles3D_property_seed>`

classref-property-setget

- `void (No return value.)` **set_seed**(value: `int<class_int>`)
- `int<class_int>` **get_seed**()

Sets the random seed used by the particle system. Only effective if `use_fixed_seed<class_CPUParticles3D_property_use_fixed_seed>` is `true`.

classref-item-separator

classref-property

`float<class_float>` **speed_scale** = `1.0` `🔗<class_CPUParticles3D_property_speed_scale>`

classref-property-setget

- `void (No return value.)` **set_speed_scale**(value: `float<class_float>`)
- `float<class_float>` **get_speed_scale**()

Particle system's running speed scaling ratio. A value of `0` can be used to pause the particles.

classref-item-separator

classref-property

`bool<class_bool>` **split_scale** = `false` `🔗<class_CPUParticles3D_property_split_scale>`

classref-property-setget

- `void (No return value.)` **set_split_scale**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_split_scale**()

If set to `true`, three different scale curves can be specified, one per scale axis.

classref-item-separator

classref-property

`float<class_float>` **spread** = `45.0` `🔗<class_CPUParticles3D_property_spread>`

classref-property-setget

- `void (No return value.)` **set_spread**(value: `float<class_float>`)
- `float<class_float>` **get_spread**()

Each particle's initial direction range from `+spread` to `-spread` degrees. Applied to X/Z plane and Y/Z planes.

classref-item-separator

classref-property

`Curve<class_Curve>` **tangential_accel_curve** `🔗<class_CPUParticles3D_property_tangential_accel_curve>`

classref-property-setget

- `void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`)
- `Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Each particle's tangential acceleration will vary along this `Curve<class_Curve>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-property

`float<class_float>` **tangential_accel_max** = `0.0` `🔗<class_CPUParticles3D_property_tangential_accel_max>`

classref-property-setget

- `void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Maximum tangent acceleration.

classref-item-separator

classref-property

`float<class_float>` **tangential_accel_min** = `0.0` `🔗<class_CPUParticles3D_property_tangential_accel_min>`

classref-property-setget

- `void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`)
- `float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Minimum tangent acceleration.

classref-item-separator

classref-property

`bool<class_bool>` **use_fixed_seed** = `false` `🔗<class_CPUParticles3D_property_use_fixed_seed>`

classref-property-setget

- `void (No return value.)` **set_use_fixed_seed**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using the seed defined in `seed<class_CPUParticles3D_property_seed>`. This is useful for situations where the visual outcome should be consistent across replays, for example when using Movie Maker mode.

classref-item-separator

classref-property

`AABB<class_AABB>` **visibility_aabb** = `AABB(0, 0, 0, 0, 0, 0)` `🔗<class_CPUParticles3D_property_visibility_aabb>`

classref-property-setget

- `void (No return value.)` **set_visibility_aabb**(value: `AABB<class_AABB>`)
- `AABB<class_AABB>` **get_visibility_aabb**()

The `AABB<class_AABB>` that determines the node's region which needs to be visible on screen for the particle system to be active.

Grow the box if particles suddenly appear/disappear when the node enters/exits the screen. The `AABB<class_AABB>` can be grown via code or with the **Particles → Generate AABB** editor tool.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AABB<class_AABB>` **capture_aabb**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles3D_method_capture_aabb>`

Returns the axis-aligned bounding box that contains all the particles that are active in the current frame.

classref-item-separator

classref-method

`void (No return value.)` **convert_from_particles**(particles: `Node<class_Node>`) `🔗<class_CPUParticles3D_method_convert_from_particles>`

Sets this node's properties to match a given `GPUParticles3D<class_GPUParticles3D>` node with an assigned `ParticleProcessMaterial<class_ParticleProcessMaterial>`.

classref-item-separator

classref-method

`Curve<class_Curve>` **get_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles3D_method_get_param_curve>`

Returns the `Curve<class_Curve>` of the parameter specified by `Parameter<enum_CPUParticles3D_Parameter>`.

classref-item-separator

classref-method

`float<class_float>` **get_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles3D_method_get_param_max>`

Returns the maximum value range for the given parameter.

classref-item-separator

classref-method

`float<class_float>` **get_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles3D_method_get_param_min>`

Returns the minimum value range for the given parameter.

classref-item-separator

classref-method

`bool<class_bool>` **get_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CPUParticles3D_method_get_particle_flag>`

Returns the enabled state of the given particle flag.

classref-item-separator

classref-method

`void (No return value.)` **request_particles_process**(process_time: `float<class_float>`, process_time_residual: `float<class_float>` = 0.0) `🔗<class_CPUParticles3D_method_request_particles_process>`

Requests the particles to process for extra process time during a single frame.

`process_time` defines the time that the particles will process while emitting is on. `process_time_residual` defines the time that particles will process with emitting turned off for the simulation. When combined with `speed_scale<class_CPUParticles3D_property_speed_scale>` set to `0.0`, this is useful to be able to seek a particle system timeline.

classref-item-separator

classref-method

`void (No return value.)` **restart**(keep_seed: `bool<class_bool>` = false) `🔗<class_CPUParticles3D_method_restart>`

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved. Useful for seeking and playback.

classref-item-separator

classref-method

`void (No return value.)` **set_param_curve**(param: `Parameter<enum_CPUParticles3D_Parameter>`, curve: `Curve<class_Curve>`) `🔗<class_CPUParticles3D_method_set_param_curve>`

Sets the `Curve<class_Curve>` of the parameter specified by `Parameter<enum_CPUParticles3D_Parameter>`. Should be a unit `Curve<class_Curve>`.

classref-item-separator

classref-method

`void (No return value.)` **set_param_max**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`) `🔗<class_CPUParticles3D_method_set_param_max>`

Sets the maximum value for the given parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_param_min**(param: `Parameter<enum_CPUParticles3D_Parameter>`, value: `float<class_float>`) `🔗<class_CPUParticles3D_method_set_param_min>`

Sets the minimum value for the given parameter.

classref-item-separator

classref-method

`void (No return value.)` **set_particle_flag**(particle_flag: `ParticleFlags<enum_CPUParticles3D_ParticleFlags>`, enable: `bool<class_bool>`) `🔗<class_CPUParticles3D_method_set_particle_flag>`

Enables or disables the given particle flag.