github_url
hide

# DirectionalLight3D

**Inherits:** `Light3D<class_Light3D>` **\<** `VisualInstance3D<class_VisualInstance3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Directional light from a distance, as from the Sun.

classref-introduction-group

## Description

A directional light is a type of `Light3D<class_Light3D>` node that models an infinite number of parallel rays covering the entire scene. It is used for lights with strong intensity that are located far away from the scene to model sunlight or moonlight.

Light is emitted in the -Z direction of the node's global basis. For an unrotated light, this means that the light is emitted forwards, illuminating the front side of a 3D model (see `Vector3.FORWARD<class_Vector3_constant_FORWARD>` and `Vector3.MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>`). The position of the node is ignored; only the basis is used to determine light direction.

classref-introduction-group

## Tutorials

- `3D lights and shadows <../tutorials/3d/lights_and_shadows>`
- `Faking global illumination <../tutorials/3d/global_illumination/faking_global_illumination>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ShadowMode**: `🔗<enum_DirectionalLight3D_ShadowMode>`

classref-enumeration-constant

`ShadowMode<enum_DirectionalLight3D_ShadowMode>` **SHADOW_ORTHOGONAL** = `0`

Renders the entire scene's shadow map from an orthogonal point of view. This is the fastest directional shadow mode. May result in blurrier shadows on close objects.

classref-enumeration-constant

`ShadowMode<enum_DirectionalLight3D_ShadowMode>` **SHADOW_PARALLEL_2_SPLITS** = `1`

Splits the view frustum in 2 areas, each with its own shadow map. This shadow mode is a compromise between `SHADOW_ORTHOGONAL<class_DirectionalLight3D_constant_SHADOW_ORTHOGONAL>` and `SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>` in terms of performance.

classref-enumeration-constant

`ShadowMode<enum_DirectionalLight3D_ShadowMode>` **SHADOW_PARALLEL_4_SPLITS** = `2`

Splits the view frustum in 4 areas, each with its own shadow map. This is the slowest directional shadow mode.

classref-item-separator

classref-enumeration

enum **SkyMode**: `🔗<enum_DirectionalLight3D_SkyMode>`

classref-enumeration-constant

`SkyMode<enum_DirectionalLight3D_SkyMode>` **SKY_MODE_LIGHT_AND_SKY** = `0`

Makes the light visible in both scene lighting and sky rendering.

classref-enumeration-constant

`SkyMode<enum_DirectionalLight3D_SkyMode>` **SKY_MODE_LIGHT_ONLY** = `1`

Makes the light visible in scene lighting only (including direct lighting and global illumination). When using this mode, the light will not be visible from sky shaders.

classref-enumeration-constant

`SkyMode<enum_DirectionalLight3D_SkyMode>` **SKY_MODE_SKY_ONLY** = `2`

Makes the light visible to sky shaders only. When using this mode the light will not cast light into the scene (either through direct lighting or through global illumination), but can be accessed through sky shaders. This can be useful, for example, when you want to control sky effects without illuminating the scene (during a night cycle, for example).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **directional_shadow_blend_splits** = `false` `🔗<class_DirectionalLight3D_property_directional_shadow_blend_splits>`

classref-property-setget

- `void (No return value.)` **set_blend_splits**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_blend_splits_enabled**()

If `true`, shadow detail is sacrificed in exchange for smoother transitions between splits. Enabling shadow blend splitting also has a moderate performance cost. This is ignored when `directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>` is `SHADOW_ORTHOGONAL<class_DirectionalLight3D_constant_SHADOW_ORTHOGONAL>`.

classref-item-separator

classref-property

`float<class_float>` **directional_shadow_fade_start** = `0.8` `🔗<class_DirectionalLight3D_property_directional_shadow_fade_start>`

classref-property-setget

- `void (No return value.)` **set_param**(value: `float<class_float>`)
- `float<class_float>` **get_param**()

Proportion of `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>` at which point the shadow starts to fade. At `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`, the shadow will disappear. The default value is a balance between smooth fading and distant shadow visibility. If the camera moves fast and the `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>` is low, consider lowering `directional_shadow_fade_start<class_DirectionalLight3D_property_directional_shadow_fade_start>` below `0.8` to make shadow transitions less noticeable. On the other hand, if you tuned `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>` to cover the entire scene, you can set `directional_shadow_fade_start<class_DirectionalLight3D_property_directional_shadow_fade_start>` to `1.0` to prevent the shadow from fading in the distance (it will suddenly cut off instead).

classref-item-separator

classref-property

`float<class_float>` **directional_shadow_max_distance** = `100.0` `🔗<class_DirectionalLight3D_property_directional_shadow_max_distance>`

classref-property-setget

- `void (No return value.)` **set_param**(value: `float<class_float>`)
- `float<class_float>` **get_param**()

The maximum distance for shadow splits. Increasing this value will make directional shadows visible from further away, at the cost of lower overall shadow detail and performance (since more objects need to be included in the directional shadow rendering).

classref-item-separator

classref-property

`ShadowMode<enum_DirectionalLight3D_ShadowMode>` **directional_shadow_mode** = `2` `🔗<class_DirectionalLight3D_property_directional_shadow_mode>`

classref-property-setget

- `void (No return value.)` **set_shadow_mode**(value: `ShadowMode<enum_DirectionalLight3D_ShadowMode>`)
- `ShadowMode<enum_DirectionalLight3D_ShadowMode>` **get_shadow_mode**()

The light's shadow rendering algorithm.

classref-item-separator

classref-property

`float<class_float>` **directional_shadow_pancake_size** = `20.0` `🔗<class_DirectionalLight3D_property_directional_shadow_pancake_size>`

classref-property-setget

- `void (No return value.)` **set_param**(value: `float<class_float>`)
- `float<class_float>` **get_param**()

Sets the size of the directional shadow pancake. The pancake offsets the start of the shadow's camera frustum to provide a higher effective depth resolution for the shadow. However, a high pancake size can cause artifacts in the shadows of large objects that are close to the edge of the frustum. Reducing the pancake size can help. Setting the size to `0` turns off the pancaking effect.

classref-item-separator

classref-property

`float<class_float>` **directional_shadow_split_1** = `0.1` `🔗<class_DirectionalLight3D_property_directional_shadow_split_1>`

classref-property-setget

- `void (No return value.)` **set_param**(value: `float<class_float>`)
- `float<class_float>` **get_param**()

The distance from camera to shadow split 1. Relative to `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`. Only used when `directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>` is `SHADOW_PARALLEL_2_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_2_SPLITS>` or `SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`.

classref-item-separator

classref-property

`float<class_float>` **directional_shadow_split_2** = `0.2` `🔗<class_DirectionalLight3D_property_directional_shadow_split_2>`

classref-property-setget

- `void (No return value.)` **set_param**(value: `float<class_float>`)
- `float<class_float>` **get_param**()

The distance from shadow split 1 to split 2. Relative to `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`. Only used when `directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>` is `SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`.

classref-item-separator

classref-property

`float<class_float>` **directional_shadow_split_3** = `0.5` `🔗<class_DirectionalLight3D_property_directional_shadow_split_3>`

classref-property-setget

- `void (No return value.)` **set_param**(value: `float<class_float>`)
- `float<class_float>` **get_param**()

The distance from shadow split 2 to split 3. Relative to `directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`. Only used when `directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>` is `SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`.

classref-item-separator

classref-property

`SkyMode<enum_DirectionalLight3D_SkyMode>` **sky_mode** = `0` `🔗<class_DirectionalLight3D_property_sky_mode>`

classref-property-setget

- `void (No return value.)` **set_sky_mode**(value: `SkyMode<enum_DirectionalLight3D_SkyMode>`)
- `SkyMode<enum_DirectionalLight3D_SkyMode>` **get_sky_mode**()

Whether this **DirectionalLight3D** is visible in the sky, in the scene, or both in the sky and in the scene.