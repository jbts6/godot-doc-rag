github_url
hide

# Texture2D

**Inherits:** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AnimatedTexture<class_AnimatedTexture>`, `AtlasTexture<class_AtlasTexture>`, `CameraTexture<class_CameraTexture>`, `CanvasTexture<class_CanvasTexture>`, `CompressedTexture2D<class_CompressedTexture2D>`, `CurveTexture<class_CurveTexture>`, `CurveXYZTexture<class_CurveXYZTexture>`, `DPITexture<class_DPITexture>`, `DrawableTexture2D<class_DrawableTexture2D>`, `ExternalTexture<class_ExternalTexture>`, `GradientTexture1D<class_GradientTexture1D>`, `GradientTexture2D<class_GradientTexture2D>`, `ImageTexture<class_ImageTexture>`, `MeshTexture<class_MeshTexture>`, `NoiseTexture2D<class_NoiseTexture2D>`, `PlaceholderTexture2D<class_PlaceholderTexture2D>`, `PortableCompressedTexture2D<class_PortableCompressedTexture2D>`, `Texture2DRD<class_Texture2DRD>`, `ViewportTexture<class_ViewportTexture>`

Texture for 2D and 3D.

classref-introduction-group

## Description

A texture works by registering an image in the video hardware, which then can be used in 3D models or 2D `Sprite2D<class_Sprite2D>` or GUI `Control<class_Control>`.

Textures are often created by loading them from a file. See `@GDScript.load()<class_@GDScript_method_load>`.

**Texture2D** is a base for other resources. It cannot be used directly.

**Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations. Larger textures may fail to import.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_draw**(to_canvas_item: `RID<class_RID>`, pos: `Vector2<class_Vector2>`, modulate: `Color<class_Color>`, transpose: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__draw>`

Called when the entire **Texture2D** is requested to be drawn over a `CanvasItem<class_CanvasItem>`, with the top-left offset specified in `pos`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

classref-item-separator

classref-method

`void (No return value.)` **\_draw_rect**(to_canvas_item: `RID<class_RID>`, rect: `Rect2<class_Rect2>`, tile: `bool<class_bool>`, modulate: `Color<class_Color>`, transpose: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__draw_rect>`

Called when the **Texture2D** is requested to be drawn onto `CanvasItem<class_CanvasItem>`'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

classref-item-separator

classref-method

`void (No return value.)` **\_draw_rect_region**(to_canvas_item: `RID<class_RID>`, rect: `Rect2<class_Rect2>`, src_rect: `Rect2<class_Rect2>`, modulate: `Color<class_Color>`, transpose: `bool<class_bool>`, clip_uv: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__draw_rect_region>`

Called when a part of the **Texture2D** specified by `src_rect`'s coordinates is requested to be drawn onto `CanvasItem<class_CanvasItem>`'s specified `rect`. `modulate` specifies a multiplier for the colors being drawn, while `transpose` specifies whether drawing should be performed in column-major order instead of row-major order (resulting in 90-degree clockwise rotation).

**Note:** This is only used in 2D rendering, not 3D.

classref-item-separator

classref-method

`Format<enum_Image_Format>` **\_get_format**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__get_format>`

Called when `get_format()<class_Texture2D_method_get_format>` is called.

classref-item-separator

classref-method

`int<class_int>` **\_get_height**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__get_height>`

Called when the **Texture2D**'s height is queried.

classref-item-separator

classref-method

`Image<class_Image>` **\_get_image**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__get_image>`

Called when `get_image()<class_Texture2D_method_get_image>` is called.

classref-item-separator

classref-method

`int<class_int>` **\_get_mipmap_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__get_mipmap_count>`

Called when `get_mipmap_count()<class_Texture2D_method_get_mipmap_count>` is called.

classref-item-separator

classref-method

`int<class_int>` **\_get_width**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__get_width>`

Called when the **Texture2D**'s width is queried.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_alpha**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__has_alpha>`

Called when the presence of an alpha channel in the **Texture2D** is queried.

classref-item-separator

classref-method

`bool<class_bool>` **\_has_mipmaps**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__has_mipmaps>`

Called when `has_mipmaps()<class_Texture2D_method_has_mipmaps>` is called.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_pixel_opaque**(x: `int<class_int>`, y: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_private_method__is_pixel_opaque>`

Called when a pixel's opaque state in the **Texture2D** is queried at the specified `(x, y)` position.

classref-item-separator

classref-method

`Resource<class_Resource>` **create_placeholder**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_create_placeholder>`

Creates a placeholder version of this resource (`PlaceholderTexture2D<class_PlaceholderTexture2D>`).

classref-item-separator

classref-method

`void (No return value.)` **draw**(canvas_item: `RID<class_RID>`, position: `Vector2<class_Vector2>`, modulate: `Color<class_Color>` = Color(1, 1, 1, 1), transpose: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_draw>`

Draws the texture using a `CanvasItem<class_CanvasItem>` with the `RenderingServer<class_RenderingServer>` API at the specified `position`.

classref-item-separator

classref-method

`void (No return value.)` **draw_rect**(canvas_item: `RID<class_RID>`, rect: `Rect2<class_Rect2>`, tile: `bool<class_bool>`, modulate: `Color<class_Color>` = Color(1, 1, 1, 1), transpose: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_draw_rect>`

Draws the texture using a `CanvasItem<class_CanvasItem>` with the `RenderingServer<class_RenderingServer>` API.

classref-item-separator

classref-method

`void (No return value.)` **draw_rect_region**(canvas_item: `RID<class_RID>`, rect: `Rect2<class_Rect2>`, src_rect: `Rect2<class_Rect2>`, modulate: `Color<class_Color>` = Color(1, 1, 1, 1), transpose: `bool<class_bool>` = false, clip_uv: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_draw_rect_region>`

Draws a part of the texture using a `CanvasItem<class_CanvasItem>` with the `RenderingServer<class_RenderingServer>` API.

classref-item-separator

classref-method

`Format<enum_Image_Format>` **get_format**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_get_format>`

Returns the image format of the texture.

classref-item-separator

classref-method

`int<class_int>` **get_height**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_get_height>`

Returns the texture height in pixels.

classref-item-separator

classref-method

`Image<class_Image>` **get_image**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_get_image>`

Returns an `Image<class_Image>` that is a copy of data from this **Texture2D** (a new `Image<class_Image>` is created each time). `Image<class_Image>`s can be accessed and manipulated directly.

**Note:** This will return `null` if this **Texture2D** is invalid.

**Note:** This will fetch the texture data from the GPU, which might cause performance problems when overused. Avoid calling `get_image()<class_Texture2D_method_get_image>` every frame, especially on large textures.

classref-item-separator

classref-method

`int<class_int>` **get_mipmap_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_get_mipmap_count>`

Returns the number of mipmaps of the texture.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_get_size>`

Returns the texture size in pixels.

classref-item-separator

classref-method

`int<class_int>` **get_width**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_get_width>`

Returns the texture width in pixels.

classref-item-separator

classref-method

`bool<class_bool>` **has_alpha**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_has_alpha>`

Returns `true` if this **Texture2D** has an alpha channel.

classref-item-separator

classref-method

`bool<class_bool>` **has_mipmaps**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Texture2D_method_has_mipmaps>`

Returns `true` if the texture has mipmaps.