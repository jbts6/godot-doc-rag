github_url
hide

# RenderSceneBuffersRD

**Inherits:** `RenderSceneBuffers<class_RenderSceneBuffers>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Render scene buffer implementation for the RenderingDevice based renderers.

classref-introduction-group

## Description

This object manages all 3D rendering buffers for the rendering device based renderers. An instance of this object is created for every viewport that has 3D rendering enabled. See also `RenderSceneBuffers<class_RenderSceneBuffers>`.

All buffers are organized in **contexts**. The default context is called **render_buffers** and can contain amongst others the color buffer, depth buffer, velocity buffers, VRS density map and MSAA variants of these buffers.

Buffers are only guaranteed to exist during rendering of the viewport.

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_context**(context: `StringName<class_StringName>`) `🔗<class_RenderSceneBuffersRD_method_clear_context>`

Frees all buffers related to this context.

classref-item-separator

classref-method

`RID<class_RID>` **create_texture**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`, data_format: `DataFormat<enum_RenderingDevice_DataFormat>`, usage_bits: `int<class_int>`, texture_samples: `TextureSamples<enum_RenderingDevice_TextureSamples>`, size: `Vector2i<class_Vector2i>`, layers: `int<class_int>`, mipmaps: `int<class_int>`, unique: `bool<class_bool>`, discardable: `bool<class_bool>`) `🔗<class_RenderSceneBuffersRD_method_create_texture>`

Create a new texture with the given definition and cache this under the given name. Will return the existing texture if it already exists.

classref-item-separator

classref-method

`RID<class_RID>` **create_texture_from_format**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`, format: `RDTextureFormat<class_RDTextureFormat>`, view: `RDTextureView<class_RDTextureView>`, unique: `bool<class_bool>`) `🔗<class_RenderSceneBuffersRD_method_create_texture_from_format>`

Create a new texture using the given format and view and cache this under the given name. Will return the existing texture if it already exists.

classref-item-separator

classref-method

`RID<class_RID>` **create_texture_view**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`, view_name: `StringName<class_StringName>`, view: `RDTextureView<class_RDTextureView>`) `🔗<class_RenderSceneBuffersRD_method_create_texture_view>`

Create a new texture view for an existing texture and cache this under the given `view_name`. Will return the existing texture view if it already exists. Will error if the source texture doesn't exist.

classref-item-separator

classref-method

`RID<class_RID>` **get_color_layer**(layer: `int<class_int>`, msaa: `bool<class_bool>` = false) `🔗<class_RenderSceneBuffersRD_method_get_color_layer>`

Returns the specified layer from the color texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

classref-item-separator

classref-method

`RID<class_RID>` **get_color_texture**(msaa: `bool<class_bool>` = false) `🔗<class_RenderSceneBuffersRD_method_get_color_texture>`

Returns the color texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

classref-item-separator

classref-method

`RID<class_RID>` **get_depth_layer**(layer: `int<class_int>`, msaa: `bool<class_bool>` = false) `🔗<class_RenderSceneBuffersRD_method_get_depth_layer>`

Returns the specified layer from the depth texture we are rendering 3D content to.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

classref-item-separator

classref-method

`RID<class_RID>` **get_depth_texture**(msaa: `bool<class_bool>` = false) `🔗<class_RenderSceneBuffersRD_method_get_depth_texture>`

Returns the depth texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is `true` and MSAA is enabled, this returns the MSAA variant of the buffer.

classref-item-separator

classref-method

`float<class_float>` **get_fsr_sharpness**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_fsr_sharpness>`

Returns the FSR sharpness value used while rendering the 3D content (if `get_scaling_3d_mode()<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>` is an FSR mode).

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_internal_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_internal_size>`

Returns the internal size of the render buffer (size before upscaling) with which textures are created by default.

classref-item-separator

classref-method

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>` **get_msaa_3d**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_msaa_3d>`

Returns the applied 3D MSAA mode for this viewport.

classref-item-separator

classref-method

`RID<class_RID>` **get_render_target**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_render_target>`

Returns the render target associated with this buffers object.

classref-item-separator

classref-method

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>` **get_scaling_3d_mode**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_scaling_3d_mode>`

Returns the scaling mode used for upscaling.

classref-item-separator

classref-method

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>` **get_screen_space_aa**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_screen_space_aa>`

Returns the screen-space antialiasing method applied.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_target_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_target_size>`

Returns the target size of the render buffer (size after upscaling).

classref-item-separator

classref-method

`RID<class_RID>` **get_texture**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_texture>`

Returns a cached texture with this name.

classref-item-separator

classref-method

`RDTextureFormat<class_RDTextureFormat>` **get_texture_format**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_texture_format>`

Returns the texture format information with which a cached texture was created.

classref-item-separator

classref-method

`TextureSamples<enum_RenderingDevice_TextureSamples>` **get_texture_samples**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_texture_samples>`

Returns the number of MSAA samples used.

classref-item-separator

classref-method

`RID<class_RID>` **get_texture_slice**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`, layer: `int<class_int>`, mipmap: `int<class_int>`, layers: `int<class_int>`, mipmaps: `int<class_int>`) `🔗<class_RenderSceneBuffersRD_method_get_texture_slice>`

Returns a specific slice (layer or mipmap) for a cached texture.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_texture_slice_size**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`, mipmap: `int<class_int>`) `🔗<class_RenderSceneBuffersRD_method_get_texture_slice_size>`

Returns the texture size of a given slice of a cached texture.

classref-item-separator

classref-method

`RID<class_RID>` **get_texture_slice_view**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`, layer: `int<class_int>`, mipmap: `int<class_int>`, layers: `int<class_int>`, mipmaps: `int<class_int>`, view: `RDTextureView<class_RDTextureView>`) `🔗<class_RenderSceneBuffersRD_method_get_texture_slice_view>`

Returns a specific view of a slice (layer or mipmap) for a cached texture.

classref-item-separator

classref-method

`bool<class_bool>` **get_use_debanding**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_use_debanding>`

Returns `true` if debanding is enabled.

classref-item-separator

classref-method

`bool<class_bool>` **get_use_taa**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_use_taa>`

Returns `true` if TAA is enabled.

classref-item-separator

classref-method

`RID<class_RID>` **get_velocity_layer**(layer: `int<class_int>`, msaa: `bool<class_bool>` = false) `🔗<class_RenderSceneBuffersRD_method_get_velocity_layer>`

Returns the specified layer from the velocity texture we are rendering 3D content to.

classref-item-separator

classref-method

`RID<class_RID>` **get_velocity_texture**(msaa: `bool<class_bool>` = false) `🔗<class_RenderSceneBuffersRD_method_get_velocity_texture>`

Returns the velocity texture we are rendering 3D content to. If multiview is used this will be a texture array with all views.

If `msaa` is **true** and MSAA is enabled, this returns the MSAA variant of the buffer.

classref-item-separator

classref-method

`int<class_int>` **get_view_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_get_view_count>`

Returns the view count for the associated viewport.

classref-item-separator

classref-method

`bool<class_bool>` **has_texture**(context: `StringName<class_StringName>`, name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneBuffersRD_method_has_texture>`

Returns `true` if a cached texture exists for this name.