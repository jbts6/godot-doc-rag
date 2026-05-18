github_url
hide

# Camera3D

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `XRCamera3D<class_XRCamera3D>`

Camera node, displays from a point of view.

classref-introduction-group

## Description

**Camera3D** is a special node that displays what is visible from its current location. Cameras register themselves in the nearest `Viewport<class_Viewport>` node (when ascending the tree). Only one camera can be active per viewport. If no viewport is available ascending the tree, the camera will register in the global viewport. In other words, a camera just provides 3D display capabilities to a `Viewport<class_Viewport>`, and, without one, a scene registered in that `Viewport<class_Viewport>` (or higher viewports) can't be displayed.

classref-introduction-group

## Tutorials

- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ProjectionType**: `🔗<enum_Camera3D_ProjectionType>`

classref-enumeration-constant

`ProjectionType<enum_Camera3D_ProjectionType>` **PROJECTION_PERSPECTIVE** = `0`

Perspective projection. Objects on the screen becomes smaller when they are far away.

classref-enumeration-constant

`ProjectionType<enum_Camera3D_ProjectionType>` **PROJECTION_ORTHOGONAL** = `1`

Orthogonal projection, also known as orthographic projection. Objects remain the same size on the screen no matter how far away they are.

classref-enumeration-constant

`ProjectionType<enum_Camera3D_ProjectionType>` **PROJECTION_FRUSTUM** = `2`

Frustum projection. This mode allows adjusting `frustum_offset<class_Camera3D_property_frustum_offset>` to create "tilted frustum" effects.

classref-item-separator

classref-enumeration

enum **KeepAspect**: `🔗<enum_Camera3D_KeepAspect>`

classref-enumeration-constant

`KeepAspect<enum_Camera3D_KeepAspect>` **KEEP_WIDTH** = `0`

Preserves the horizontal aspect ratio; also known as Vert- scaling. This is usually the best option for projects running in portrait mode, as taller aspect ratios will benefit from a wider vertical FOV.

classref-enumeration-constant

`KeepAspect<enum_Camera3D_KeepAspect>` **KEEP_HEIGHT** = `1`

Preserves the vertical aspect ratio; also known as Hor+ scaling. This is usually the best option for projects running in landscape mode, as wider aspect ratios will automatically benefit from a wider horizontal FOV.

classref-item-separator

classref-enumeration

enum **DopplerTracking**: `🔗<enum_Camera3D_DopplerTracking>`

classref-enumeration-constant

`DopplerTracking<enum_Camera3D_DopplerTracking>` **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) simulation (default).

classref-enumeration-constant

`DopplerTracking<enum_Camera3D_DopplerTracking>` **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_process`. Changes in the relative velocity of this camera compared to those objects affect how audio is perceived (changing the audio's `AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>`).

classref-enumeration-constant

`DopplerTracking<enum_Camera3D_DopplerTracking>` **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) by tracking positions of objects that are changed in `_physics_process`. Changes in the relative velocity of this camera compared to those objects affect how audio is perceived (changing the audio's `AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>`).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`CameraAttributes<class_CameraAttributes>` **attributes** `🔗<class_Camera3D_property_attributes>`

classref-property-setget

- `void (No return value.)` **set_attributes**(value: `CameraAttributes<class_CameraAttributes>`)
- `CameraAttributes<class_CameraAttributes>` **get_attributes**()

The `CameraAttributes<class_CameraAttributes>` to use for this camera.

classref-item-separator

classref-property

`Compositor<class_Compositor>` **compositor** `🔗<class_Camera3D_property_compositor>`

classref-property-setget

- `void (No return value.)` **set_compositor**(value: `Compositor<class_Compositor>`)
- `Compositor<class_Compositor>` **get_compositor**()

The `Compositor<class_Compositor>` to use for this camera.

classref-item-separator

classref-property

`int<class_int>` **cull_mask** = `1048575` `🔗<class_Camera3D_property_cull_mask>`

classref-property-setget

- `void (No return value.)` **set_cull_mask**(value: `int<class_int>`)
- `int<class_int>` **get_cull_mask**()

The culling mask that describes which `VisualInstance3D.layers<class_VisualInstance3D_property_layers>` are rendered by this camera. By default, all 20 user-visible layers are rendered.

**Note:** Since the `cull_mask<class_Camera3D_property_cull_mask>` allows for 32 layers to be stored in total, there are an additional 12 layers that are only used internally by the engine and aren't exposed in the editor. Setting `cull_mask<class_Camera3D_property_cull_mask>` using a script allows you to toggle those reserved layers, which can be useful for editor plugins.

To adjust `cull_mask<class_Camera3D_property_cull_mask>` more easily using a script, use `get_cull_mask_value()<class_Camera3D_method_get_cull_mask_value>` and `set_cull_mask_value()<class_Camera3D_method_set_cull_mask_value>`.

**Note:** `VoxelGI<class_VoxelGI>`, SDFGI and `LightmapGI<class_LightmapGI>` will always take all layers into account to determine what contributes to global illumination. If this is an issue, set `GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>` to `GeometryInstance3D.GI_MODE_DISABLED<class_GeometryInstance3D_constant_GI_MODE_DISABLED>` for meshes and `Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>` to `Light3D.BAKE_DISABLED<class_Light3D_constant_BAKE_DISABLED>` for lights to exclude them from global illumination.

classref-item-separator

classref-property

`bool<class_bool>` **current** = `false` `🔗<class_Camera3D_property_current>`

classref-property-setget

- `void (No return value.)` **set_current**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_current**()

If `true`, the ancestor `Viewport<class_Viewport>` is currently using this camera.

If multiple cameras are in the scene, one will always be made current. For example, if two **Camera3D** nodes are present in the scene and only one is current, setting one camera's `current<class_Camera3D_property_current>` to `false` will cause the other camera to be made current.

classref-item-separator

classref-property

`DopplerTracking<enum_Camera3D_DopplerTracking>` **doppler_tracking** = `0` `🔗<class_Camera3D_property_doppler_tracking>`

classref-property-setget

- `void (No return value.)` **set_doppler_tracking**(value: `DopplerTracking<enum_Camera3D_DopplerTracking>`)
- `DopplerTracking<enum_Camera3D_DopplerTracking>` **get_doppler_tracking**()

If not `DOPPLER_TRACKING_DISABLED<class_Camera3D_constant_DOPPLER_TRACKING_DISABLED>`, this camera will simulate the [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) for objects changed in particular `_process` methods.

**Note:** The Doppler effect will only be heard on `AudioStreamPlayer3D<class_AudioStreamPlayer3D>`s if `AudioStreamPlayer3D.doppler_tracking<class_AudioStreamPlayer3D_property_doppler_tracking>` is not set to `AudioStreamPlayer3D.DOPPLER_TRACKING_DISABLED<class_AudioStreamPlayer3D_constant_DOPPLER_TRACKING_DISABLED>`.

classref-item-separator

classref-property

`Environment<class_Environment>` **environment** `🔗<class_Camera3D_property_environment>`

classref-property-setget

- `void (No return value.)` **set_environment**(value: `Environment<class_Environment>`)
- `Environment<class_Environment>` **get_environment**()

The `Environment<class_Environment>` to use for this camera.

classref-item-separator

classref-property

`float<class_float>` **far** = `4000.0` `🔗<class_Camera3D_property_far>`

classref-property-setget

- `void (No return value.)` **set_far**(value: `float<class_float>`)
- `float<class_float>` **get_far**()

The distance to the far culling boundary for this camera relative to its local Z axis. Higher values allow the camera to see further away, while decreasing `far<class_Camera3D_property_far>` can improve performance if it results in objects being partially or fully culled.

classref-item-separator

classref-property

`float<class_float>` **fov** = `75.0` `🔗<class_Camera3D_property_fov>`

classref-property-setget

- `void (No return value.)` **set_fov**(value: `float<class_float>`)
- `float<class_float>` **get_fov**()

The camera's field of view angle (in degrees). Only applicable in perspective mode. Since `keep_aspect<class_Camera3D_property_keep_aspect>` locks one axis, `fov<class_Camera3D_property_fov>` sets the other axis' field of view angle.

For reference, the default vertical field of view value (`75.0`) is equivalent to a horizontal FOV of:

- ~91.31 degrees in a 4:3 viewport
- ~101.67 degrees in a 16:10 viewport
- ~107.51 degrees in a 16:9 viewport
- ~121.63 degrees in a 21:9 viewport

classref-item-separator

classref-property

`Vector2<class_Vector2>` **frustum_offset** = `Vector2(0, 0)` `🔗<class_Camera3D_property_frustum_offset>`

classref-property-setget

- `void (No return value.)` **set_frustum_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_frustum_offset**()

The camera's frustum offset. This can be changed from the default to create "tilted frustum" effects such as [Y-shearing](https://zdoom.org/wiki/Y-shearing).

**Note:** Only effective if `projection<class_Camera3D_property_projection>` is `PROJECTION_FRUSTUM<class_Camera3D_constant_PROJECTION_FRUSTUM>`.

classref-item-separator

classref-property

`float<class_float>` **h_offset** = `0.0` `🔗<class_Camera3D_property_h_offset>`

classref-property-setget

- `void (No return value.)` **set_h_offset**(value: `float<class_float>`)
- `float<class_float>` **get_h_offset**()

The horizontal (X) offset of the camera viewport.

classref-item-separator

classref-property

`KeepAspect<enum_Camera3D_KeepAspect>` **keep_aspect** = `1` `🔗<class_Camera3D_property_keep_aspect>`

classref-property-setget

- `void (No return value.)` **set_keep_aspect_mode**(value: `KeepAspect<enum_Camera3D_KeepAspect>`)
- `KeepAspect<enum_Camera3D_KeepAspect>` **get_keep_aspect_mode**()

The axis to lock during `fov<class_Camera3D_property_fov>`/`size<class_Camera3D_property_size>` adjustments. Can be either `KEEP_WIDTH<class_Camera3D_constant_KEEP_WIDTH>` or `KEEP_HEIGHT<class_Camera3D_constant_KEEP_HEIGHT>`.

classref-item-separator

classref-property

`float<class_float>` **near** = `0.05` `🔗<class_Camera3D_property_near>`

classref-property-setget

- `void (No return value.)` **set_near**(value: `float<class_float>`)
- `float<class_float>` **get_near**()

The distance to the near culling boundary for this camera relative to its local Z axis. Lower values allow the camera to see objects more up close to its origin, at the cost of lower precision across the *entire* range. Values lower than the default can lead to increased Z-fighting.

classref-item-separator

classref-property

`ProjectionType<enum_Camera3D_ProjectionType>` **projection** = `0` `🔗<class_Camera3D_property_projection>`

classref-property-setget

- `void (No return value.)` **set_projection**(value: `ProjectionType<enum_Camera3D_ProjectionType>`)
- `ProjectionType<enum_Camera3D_ProjectionType>` **get_projection**()

The camera's projection mode. In `PROJECTION_PERSPECTIVE<class_Camera3D_constant_PROJECTION_PERSPECTIVE>` mode, objects' Z distance from the camera's local space scales their perceived size.

classref-item-separator

classref-property

`float<class_float>` **size** = `1.0` `🔗<class_Camera3D_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `float<class_float>`)
- `float<class_float>` **get_size**()

The camera's size in meters measured as the diameter of the width or height, depending on `keep_aspect<class_Camera3D_property_keep_aspect>`. Only applicable in orthogonal and frustum modes.

classref-item-separator

classref-property

`float<class_float>` **v_offset** = `0.0` `🔗<class_Camera3D_property_v_offset>`

classref-property-setget

- `void (No return value.)` **set_v_offset**(value: `float<class_float>`)
- `float<class_float>` **get_v_offset**()

The vertical (Y) offset of the camera viewport.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_current**(enable_next: `bool<class_bool>` = true) `🔗<class_Camera3D_method_clear_current>`

If this is the current camera, remove it from being current. If `enable_next` is `true`, request to make the next camera current, if any.

classref-item-separator

classref-method

`Projection<class_Projection>` **get_camera_projection**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_get_camera_projection>`

Returns the projection matrix that this camera uses to render to its associated viewport. The camera must be part of the scene tree to function.

classref-item-separator

classref-method

`RID<class_RID>` **get_camera_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_get_camera_rid>`

Returns the camera's RID from the `RenderingServer<class_RenderingServer>`.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_camera_transform**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_get_camera_transform>`

Returns the transform of the camera plus the vertical (`v_offset<class_Camera3D_property_v_offset>`) and horizontal (`h_offset<class_Camera3D_property_h_offset>`) offsets; and any other adjustments made to the position and orientation of the camera by subclassed cameras such as `XRCamera3D<class_XRCamera3D>`.

classref-item-separator

classref-method

`bool<class_bool>` **get_cull_mask_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_get_cull_mask_value>`

Returns whether or not the specified layer of the `cull_mask<class_Camera3D_property_cull_mask>` is enabled, given a `layer_number` between 1 and 20.

classref-item-separator

classref-method

`Array<class_Array>`\[`Plane<class_Plane>`\] **get_frustum**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_get_frustum>`

Returns the camera's frustum planes in world space units as an array of `Plane<class_Plane>`s in the following order: near, far, left, top, right, bottom. Not to be confused with `frustum_offset<class_Camera3D_property_frustum_offset>`.

classref-item-separator

classref-method

`RID<class_RID>` **get_pyramid_shape_rid**() `🔗<class_Camera3D_method_get_pyramid_shape_rid>`

Returns the RID of a pyramid shape encompassing the camera's view frustum, ignoring the camera's near plane. The tip of the pyramid represents the position of the camera.

classref-item-separator

classref-method

`bool<class_bool>` **is_position_behind**(world_point: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_is_position_behind>`

Returns `true` if the given position is behind the camera (the blue part of the linked diagram). [See this diagram](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/camera3d_position_frustum.png) for an overview of position query methods.

**Note:** A position which returns `false` may still be outside the camera's field of view.

classref-item-separator

classref-method

`bool<class_bool>` **is_position_in_frustum**(world_point: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_is_position_in_frustum>`

Returns `true` if the given position is inside the camera's frustum (the green part of the linked diagram). [See this diagram](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/camera3d_position_frustum.png) for an overview of position query methods.

classref-item-separator

classref-method

`void (No return value.)` **make_current**() `🔗<class_Camera3D_method_make_current>`

Makes this camera the current camera for the `Viewport<class_Viewport>` (see class description). If the camera node is outside the scene tree, it will attempt to become current once it's added.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **project_local_ray_normal**(screen_point: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_project_local_ray_normal>`

Returns a normal vector from the screen point location directed along the camera. Orthogonal cameras are normalized. Perspective cameras account for perspective, screen width/height, etc.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **project_position**(screen_point: `Vector2<class_Vector2>`, z_depth: `float<class_float>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_project_position>`

Returns the 3D point in world space that maps to the given 2D coordinate in the `Viewport<class_Viewport>` rectangle on a plane that is the given `z_depth` distance into the scene away from the camera.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **project_ray_normal**(screen_point: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_project_ray_normal>`

Returns a normal vector in world space, that is the result of projecting a point on the `Viewport<class_Viewport>` rectangle by the inverse camera projection. This is useful for casting rays in the form of (origin, normal) for object intersection or picking.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **project_ray_origin**(screen_point: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_project_ray_origin>`

Returns a 3D position in world space, that is the result of projecting a point on the `Viewport<class_Viewport>` rectangle by the inverse camera projection. This is useful for casting rays in the form of (origin, normal) for object intersection or picking.

classref-item-separator

classref-method

`void (No return value.)` **set_cull_mask_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_Camera3D_method_set_cull_mask_value>`

Based on `value`, enables or disables the specified layer in the `cull_mask<class_Camera3D_property_cull_mask>`, given a `layer_number` between 1 and 20.

classref-item-separator

classref-method

`void (No return value.)` **set_frustum**(size: `float<class_float>`, offset: `Vector2<class_Vector2>`, z_near: `float<class_float>`, z_far: `float<class_float>`) `🔗<class_Camera3D_method_set_frustum>`

Sets the camera projection to frustum mode (see `PROJECTION_FRUSTUM<class_Camera3D_constant_PROJECTION_FRUSTUM>`), by specifying a `size`, an `offset`, and the `z_near` and `z_far` clip planes in world space units. The `size` parameter represents the size of the near plane, either its width or height depending on the value of `keep_aspect<class_Camera3D_property_keep_aspect>`. See also `frustum_offset<class_Camera3D_property_frustum_offset>`.

classref-item-separator

classref-method

`void (No return value.)` **set_orthogonal**(size: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`) `🔗<class_Camera3D_method_set_orthogonal>`

Sets the camera projection to orthogonal mode (see `PROJECTION_ORTHOGONAL<class_Camera3D_constant_PROJECTION_ORTHOGONAL>`), by specifying a `size`, and the `z_near` and `z_far` clip planes in world space units.

As a hint, 3D games that look 2D often use this projection, with `size` specified in pixels.

classref-item-separator

classref-method

`void (No return value.)` **set_perspective**(fov: `float<class_float>`, z_near: `float<class_float>`, z_far: `float<class_float>`) `🔗<class_Camera3D_method_set_perspective>`

Sets the camera projection to perspective mode (see `PROJECTION_PERSPECTIVE<class_Camera3D_constant_PROJECTION_PERSPECTIVE>`), by specifying a `fov` (field of view) angle in degrees, and the `z_near` and `z_far` clip planes in world space units.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **unproject_position**(world_point: `Vector3<class_Vector3>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Camera3D_method_unproject_position>`

Returns the 2D coordinate in the `Viewport<class_Viewport>` rectangle that maps to the given 3D point in world space.

**Note:** When using this to position GUI elements over a 3D viewport, use `is_position_behind()<class_Camera3D_method_is_position_behind>` to prevent them from appearing if the 3D point is behind the camera:

    # This code block is part of a script that inherits from Node3D.
    # `control` is a reference to a node inheriting from Control.
    control.visible = not get_viewport().get_camera_3d().is_position_behind(global_transform.origin)
    control.position = get_viewport().get_camera_3d().unproject_position(global_transform.origin)