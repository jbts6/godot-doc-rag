github_url
hide

# OpenXRAPIExtension

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Makes the OpenXR API available for GDExtension.

classref-introduction-group

## Description

**OpenXRAPIExtension** makes OpenXR available for GDExtension. It provides the OpenXR API to GDExtension through the `get_instance_proc_addr()<class_OpenXRAPIExtension_method_get_instance_proc_addr>` method, and the OpenXR instance through `get_instance()<class_OpenXRAPIExtension_method_get_instance>`.

It also provides methods for querying the status of OpenXR initialization, and helper methods for ease of use of the API with GDExtension.

classref-introduction-group

## Tutorials

- [XrResult documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html)
- [XrInstance documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html)
- [XrSpace documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html)
- [XrSession documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html)
- [XrSystemId documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html)
- [xrBeginSession documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html)
- [XrPosef documentation](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **OpenXRAlphaBlendModeSupport**: `🔗<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>`

classref-enumeration-constant

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>` **OPENXR_ALPHA_BLEND_MODE_SUPPORT_NONE** = `0`

Means that `XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>` isn't supported at all.

classref-enumeration-constant

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>` **OPENXR_ALPHA_BLEND_MODE_SUPPORT_REAL** = `1`

Means that `XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>` is really supported.

classref-enumeration-constant

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>` **OPENXR_ALPHA_BLEND_MODE_SUPPORT_EMULATING** = `2`

Means that `XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>` is emulated.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **action_get_handle**(action: `RID<class_RID>`) `🔗<class_OpenXRAPIExtension_method_action_get_handle>`

Returns the corresponding `XrAction` OpenXR handle for the given action RID.

classref-item-separator

classref-method

`void (No return value.)` **begin_debug_label_region**(label_name: `String<class_String>`) `🔗<class_OpenXRAPIExtension_method_begin_debug_label_region>`

Begins a new debug label region, this label will be reported in debug messages for any calls following this until `end_debug_label_region()<class_OpenXRAPIExtension_method_end_debug_label_region>` is called. Debug labels can be stacked.

classref-item-separator

classref-method

`bool<class_bool>` **can_render**() `🔗<class_OpenXRAPIExtension_method_can_render>`

Returns `true` if OpenXR is initialized for rendering with an XR viewport.

classref-item-separator

classref-method

`void (No return value.)` **end_debug_label_region**() `🔗<class_OpenXRAPIExtension_method_end_debug_label_region>`

Marks the end of a debug label region. Removes the latest debug label region added by calling `begin_debug_label_region()<class_OpenXRAPIExtension_method_begin_debug_label_region>`.

classref-item-separator

classref-method

`RID<class_RID>` **find_action**(name: `String<class_String>`, action_set: `RID<class_RID>`) `🔗<class_OpenXRAPIExtension_method_find_action>`

Returns the `RID<class_RID>` corresponding to an `Action` of a matching name, optionally limited to a specified action set.

classref-item-separator

classref-method

`String<class_String>` **get_error_string**(result: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_get_error_string>`

Returns an error string for the given [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html).

classref-item-separator

classref-method

`int<class_int>` **get_hand_tracker**(hand_index: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_get_hand_tracker>`

Returns the corresponding `XRHandTrackerEXT` handle for the given hand index value.

classref-item-separator

classref-method

`int<class_int>` **get_instance**() `🔗<class_OpenXRAPIExtension_method_get_instance>`

Returns the [XrInstance](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrInstance.html) created during the initialization of the OpenXR API.

classref-item-separator

classref-method

`int<class_int>` **get_instance_proc_addr**(name: `String<class_String>`) `🔗<class_OpenXRAPIExtension_method_get_instance_proc_addr>`

Returns the function pointer of the OpenXR function with the specified name, cast to an integer. If the function with the given name does not exist, the method returns `0`.

**Note:** `openxr/util.h` contains utility macros for acquiring OpenXR functions, e.g. `GDEXTENSION_INIT_XR_FUNC_V(xrCreateAction)`.

classref-item-separator

classref-method

`int<class_int>` **get_next_frame_time**() `🔗<class_OpenXRAPIExtension_method_get_next_frame_time>`

Returns the predicted display timing for the next frame.

classref-item-separator

classref-method

`int<class_int>` **get_openxr_version**() `🔗<class_OpenXRAPIExtension_method_get_openxr_version>`

Returns the version of OpenXR that was initialized. Only valid after the OpenXR instance has been created. See [XR_MAKE_VERSION](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_MAKE_VERSION) for how the version is calculated.

classref-item-separator

classref-method

`int<class_int>` **get_play_space**() `🔗<class_OpenXRAPIExtension_method_get_play_space>`

Returns the play space, which is an [XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html) cast to an integer.

classref-item-separator

classref-method

`int<class_int>` **get_predicted_display_time**() `🔗<class_OpenXRAPIExtension_method_get_predicted_display_time>`

Returns the predicted display timing for the current frame.

classref-item-separator

classref-method

`int<class_int>` **get_projection_layer**() `🔗<class_OpenXRAPIExtension_method_get_projection_layer>`

Returns a pointer to the render state's `XrCompositionLayerProjection` struct.

**Note:** This method should only be called from the rendering thread.

classref-item-separator

classref-method

`float<class_float>` **get_render_state_z_far**() `🔗<class_OpenXRAPIExtension_method_get_render_state_z_far>`

Returns the far boundary value of the camera frustum.

**Note:** This is only accessible in the render thread.

classref-item-separator

classref-method

`float<class_float>` **get_render_state_z_near**() `🔗<class_OpenXRAPIExtension_method_get_render_state_z_near>`

Returns the near boundary value of the camera frustum.

**Note:** This is only accessible in the render thread.

classref-item-separator

classref-method

`int<class_int>` **get_session**() `🔗<class_OpenXRAPIExtension_method_get_session>`

Returns the OpenXR session, which is an [XrSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSession.html) cast to an integer.

classref-item-separator

classref-method

`PackedInt64Array<class_PackedInt64Array>` **get_supported_swapchain_formats**() `🔗<class_OpenXRAPIExtension_method_get_supported_swapchain_formats>`

Returns an array of supported swapchain formats.

classref-item-separator

classref-method

`String<class_String>` **get_swapchain_format_name**(swapchain_format: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_get_swapchain_format_name>`

Returns the name of the specified swapchain format.

classref-item-separator

classref-method

`int<class_int>` **get_system_id**() `🔗<class_OpenXRAPIExtension_method_get_system_id>`

Returns the ID of the system, which is an [XrSystemId](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSystemId.html) cast to an integer.

classref-item-separator

classref-method

`int<class_int>` **get_view_configuration**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRAPIExtension_method_get_view_configuration>`

Returns the view configuration type, which is an [XrViewConfigurationType](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrViewConfigurationType.html) cast to an integer.

classref-item-separator

classref-method

`int<class_int>` **get_view_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRAPIExtension_method_get_view_count>`

Returns the number of views. It is usually two, one for each eye, but may differ with different view configurations.

classref-item-separator

classref-method

`void (No return value.)` **insert_debug_label**(label_name: `String<class_String>`) `🔗<class_OpenXRAPIExtension_method_insert_debug_label>`

Inserts a debug label, this label is reported in any debug message resulting from the OpenXR calls that follows, until any of `begin_debug_label_region()<class_OpenXRAPIExtension_method_begin_debug_label_region>`, `end_debug_label_region()<class_OpenXRAPIExtension_method_end_debug_label_region>`, or `insert_debug_label()<class_OpenXRAPIExtension_method_insert_debug_label>` is called.

classref-item-separator

classref-method

`OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>` **is_environment_blend_mode_alpha_supported**() `🔗<class_OpenXRAPIExtension_method_is_environment_blend_mode_alpha_supported>`

Returns `OpenXRAlphaBlendModeSupport<enum_OpenXRAPIExtension_OpenXRAlphaBlendModeSupport>` denoting if `XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>` is really supported, emulated or not supported at all.

classref-item-separator

classref-method

`bool<class_bool>` **is_initialized**() `🔗<class_OpenXRAPIExtension_method_is_initialized>`

Returns `true` if OpenXR is initialized.

classref-item-separator

classref-method

`bool<class_bool>` **is_running**() `🔗<class_OpenXRAPIExtension_method_is_running>`

Returns `true` if OpenXR is running ([xrBeginSession](https://registry.khronos.org/OpenXR/specs/1.0/man/html/xrBeginSession.html) was successfully called and the swapchains were created).

classref-item-separator

classref-method

`bool<class_bool>` **openxr_is_enabled**(check_run_in_editor: `bool<class_bool>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_OpenXRAPIExtension_method_openxr_is_enabled>`

Returns `true` if OpenXR is enabled.

classref-item-separator

classref-method

`void (No return value.)` **openxr_swapchain_acquire**(swapchain: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_openxr_swapchain_acquire>`

Acquires the image of the provided swapchain.

classref-item-separator

classref-method

`int<class_int>` **openxr_swapchain_create**(create_flags: `int<class_int>`, usage_flags: `int<class_int>`, swapchain_format: `int<class_int>`, width: `int<class_int>`, height: `int<class_int>`, sample_count: `int<class_int>`, array_size: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_openxr_swapchain_create>`

Returns a pointer to a new swapchain created using the provided parameters.

classref-item-separator

classref-method

`void (No return value.)` **openxr_swapchain_free**(swapchain: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_openxr_swapchain_free>`

Destroys the provided swapchain and frees it from memory.

classref-item-separator

classref-method

`RID<class_RID>` **openxr_swapchain_get_image**(swapchain: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_openxr_swapchain_get_image>`

Returns the RID of the provided swapchain's image.

classref-item-separator

classref-method

`int<class_int>` **openxr_swapchain_get_swapchain**(swapchain: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_openxr_swapchain_get_swapchain>`

Returns the `XrSwapchain` handle of the provided swapchain.

classref-item-separator

classref-method

`void (No return value.)` **openxr_swapchain_release**(swapchain: `int<class_int>`) `🔗<class_OpenXRAPIExtension_method_openxr_swapchain_release>`

Releases the image of the provided swapchain.

classref-item-separator

classref-method

`void (No return value.)` **register_composition_layer_provider**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_register_composition_layer_provider>`

Registers the given extension as a composition layer provider.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in `OpenXRExtensionWrapper._on_session_created()<class_OpenXRExtensionWrapper_private_method__on_session_created>`.

classref-item-separator

classref-method

`void (No return value.)` **register_frame_info_extension**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_register_frame_info_extension>`

Registers the given extension as modifying frame info via the `OpenXRExtensionWrapper._set_frame_wait_info_and_get_next_pointer()<class_OpenXRExtensionWrapper_private_method__set_frame_wait_info_and_get_next_pointer>`, `OpenXRExtensionWrapper._set_view_locate_info_and_get_next_pointer()<class_OpenXRExtensionWrapper_private_method__set_view_locate_info_and_get_next_pointer>`, or `OpenXRExtensionWrapper._set_frame_end_info_and_get_next_pointer()<class_OpenXRExtensionWrapper_private_method__set_frame_end_info_and_get_next_pointer>` virtual methods.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in `OpenXRExtensionWrapper._on_session_created()<class_OpenXRExtensionWrapper_private_method__on_session_created>`.

classref-item-separator

classref-method

`void (No return value.)` **register_projection_layer_extension**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_register_projection_layer_extension>`

Registers the given extension as modifying `XrCompositionLayerProjection` via the `OpenXRExtensionWrapper._set_projection_layer_and_get_next_pointer()<class_OpenXRExtensionWrapper_private_method__set_projection_layer_and_get_next_pointer>` virtual method.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in `OpenXRExtensionWrapper._on_session_created()<class_OpenXRExtensionWrapper_private_method__on_session_created>`.

classref-item-separator

classref-method

`void (No return value.)` **register_projection_views_extension**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_register_projection_views_extension>`

Registers the given extension as a provider of additional data structures to projections views.

**Note:** This cannot be called after the OpenXR session has started. However, it can be called in `OpenXRExtensionWrapper._on_session_created()<class_OpenXRExtensionWrapper_private_method__on_session_created>`.

classref-item-separator

classref-method

`void (No return value.)` **set_custom_play_space**(space: `const void*`) `🔗<class_OpenXRAPIExtension_method_set_custom_play_space>`

Sets the reference space used by OpenXR to the given [XrSpace](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrSpace.html) (cast to a `void *`).

classref-item-separator

classref-method

`void (No return value.)` **set_emulate_environment_blend_mode_alpha_blend**(enabled: `bool<class_bool>`) `🔗<class_OpenXRAPIExtension_method_set_emulate_environment_blend_mode_alpha_blend>`

If set to `true`, an OpenXR extension is loaded which is capable of emulating the `XRInterface.XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>` blend mode.

classref-item-separator

classref-method

`void (No return value.)` **set_object_name**(object_type: `int<class_int>`, object_handle: `int<class_int>`, object_name: `String<class_String>`) `🔗<class_OpenXRAPIExtension_method_set_object_name>`

Set the object name of an OpenXR object, used for debug output. `object_type` must be a valid OpenXR `XrObjectType` enum and `object_handle` must be a valid OpenXR object handle.

classref-item-separator

classref-method

`void (No return value.)` **set_render_region**(render_region: `Rect2i<class_Rect2i>`) `🔗<class_OpenXRAPIExtension_method_set_render_region>`

Sets the render region to `render_region`, overriding the normal render target's rect.

classref-item-separator

classref-method

`void (No return value.)` **set_velocity_depth_texture**(render_target: `RID<class_RID>`) `🔗<class_OpenXRAPIExtension_method_set_velocity_depth_texture>`

Sets the render target of the velocity depth texture.

classref-item-separator

classref-method

`void (No return value.)` **set_velocity_target_size**(target_size: `Vector2i<class_Vector2i>`) `🔗<class_OpenXRAPIExtension_method_set_velocity_target_size>`

Sets the target size of the velocity and velocity depth textures.

classref-item-separator

classref-method

`void (No return value.)` **set_velocity_texture**(render_target: `RID<class_RID>`) `🔗<class_OpenXRAPIExtension_method_set_velocity_texture>`

Sets the render target of the velocity texture.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **transform_from_pose**(pose: `const void*`) `🔗<class_OpenXRAPIExtension_method_transform_from_pose>`

Creates a `Transform3D<class_Transform3D>` from an [XrPosef](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrPosef.html).

classref-item-separator

classref-method

`void (No return value.)` **unregister_composition_layer_provider**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_unregister_composition_layer_provider>`

Unregisters the given extension as a composition layer provider.

**Note:** This cannot be called while the OpenXR session is still running.

classref-item-separator

classref-method

`void (No return value.)` **unregister_frame_info_extension**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_unregister_frame_info_extension>`

Unregisters the given extension as modifying frame info.

**Note:** This cannot be called while the OpenXR session is still running.

classref-item-separator

classref-method

`void (No return value.)` **unregister_projection_layer_extension**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_unregister_projection_layer_extension>`

Unregisters the given extension as modifying `XrCompositionLayerProjection`.

**Note:** This cannot be called while the OpenXR session is still running.

classref-item-separator

classref-method

`void (No return value.)` **unregister_projection_views_extension**(extension: `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`) `🔗<class_OpenXRAPIExtension_method_unregister_projection_views_extension>`

Unregisters the given extension as a provider of additional data structures to projections views.

**Note:** This cannot be called while the OpenXR session is still running.

classref-item-separator

classref-method

`void (No return value.)` **update_main_swapchain_size**() `🔗<class_OpenXRAPIExtension_method_update_main_swapchain_size>`

Request the recommended resolution from the OpenXR runtime and update the main swapchain size if it has changed.

classref-item-separator

classref-method

`bool<class_bool>` **xr_result**(result: `int<class_int>`, format: `String<class_String>`, args: `Array<class_Array>`) `🔗<class_OpenXRAPIExtension_method_xr_result>`

Returns `true` if the provided [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html) (cast to an integer) is successful. Otherwise returns `false` and prints the [XrResult](https://registry.khronos.org/OpenXR/specs/1.0/man/html/XrResult.html) converted to a string, with the specified additional information.