github_url
hide

# RenderSceneBuffersConfiguration

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Configuration object used to setup a `RenderSceneBuffers<class_RenderSceneBuffers>` object.

classref-introduction-group

## Description

This configuration object is created and populated by the render engine on a viewport change and used to (re)configure a `RenderSceneBuffers<class_RenderSceneBuffers>` object.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>` **anisotropic_filtering_level** = `2` `🔗<class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level>`

classref-property-setget

- `void (No return value.)` **set_anisotropic_filtering_level**(value: `ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`)
- `ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>` **get_anisotropic_filtering_level**()

Level of the anisotropic filter.

classref-item-separator

classref-property

`float<class_float>` **fsr_sharpness** = `0.0` `🔗<class_RenderSceneBuffersConfiguration_property_fsr_sharpness>`

classref-property-setget

- `void (No return value.)` **set_fsr_sharpness**(value: `float<class_float>`)
- `float<class_float>` **get_fsr_sharpness**()

FSR Sharpness applicable if FSR upscaling is used.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **internal_size** = `Vector2i(0, 0)` `🔗<class_RenderSceneBuffersConfiguration_property_internal_size>`

classref-property-setget

- `void (No return value.)` **set_internal_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_internal_size**()

The size of the 3D render buffer used for rendering.

classref-item-separator

classref-property

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>` **msaa_3d** = `0` `🔗<class_RenderSceneBuffersConfiguration_property_msaa_3d>`

classref-property-setget

- `void (No return value.)` **set_msaa_3d**(value: `ViewportMSAA<enum_RenderingServer_ViewportMSAA>`)
- `ViewportMSAA<enum_RenderingServer_ViewportMSAA>` **get_msaa_3d**()

The MSAA mode we're using for 3D rendering.

classref-item-separator

classref-property

`RID<class_RID>` **render_target** = `RID()` `🔗<class_RenderSceneBuffersConfiguration_property_render_target>`

classref-property-setget

- `void (No return value.)` **set_render_target**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_render_target**()

The render target associated with these buffer.

classref-item-separator

classref-property

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>` **scaling_3d_mode** = `255` `🔗<class_RenderSceneBuffersConfiguration_property_scaling_3d_mode>`

classref-property-setget

- `void (No return value.)` **set_scaling_3d_mode**(value: `ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`)
- `ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>` **get_scaling_3d_mode**()

The requested scaling mode with which we upscale/downscale if `internal_size<class_RenderSceneBuffersConfiguration_property_internal_size>` and `target_size<class_RenderSceneBuffersConfiguration_property_target_size>` are not equal.

classref-item-separator

classref-property

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>` **screen_space_aa** = `0` `🔗<class_RenderSceneBuffersConfiguration_property_screen_space_aa>`

classref-property-setget

- `void (No return value.)` **set_screen_space_aa**(value: `ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`)
- `ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>` **get_screen_space_aa**()

The requested screen space AA applied in post processing.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **target_size** = `Vector2i(0, 0)` `🔗<class_RenderSceneBuffersConfiguration_property_target_size>`

classref-property-setget

- `void (No return value.)` **set_target_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_target_size**()

The target (upscale) size if scaling is used.

classref-item-separator

classref-property

`float<class_float>` **texture_mipmap_bias** = `0.0` `🔗<class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias>`

classref-property-setget

- `void (No return value.)` **set_texture_mipmap_bias**(value: `float<class_float>`)
- `float<class_float>` **get_texture_mipmap_bias**()

Bias applied to mipmaps.

classref-item-separator

classref-property

`int<class_int>` **view_count** = `1` `🔗<class_RenderSceneBuffersConfiguration_property_view_count>`

classref-property-setget

- `void (No return value.)` **set_view_count**(value: `int<class_int>`)
- `int<class_int>` **get_view_count**()

The number of views we're rendering.