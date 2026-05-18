github_url
hide

# ParallaxBackground

**Deprecated:** Use the `Parallax2D<class_Parallax2D>` node instead.

**Inherits:** `CanvasLayer<class_CanvasLayer>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A node used to create a parallax scrolling background.

classref-introduction-group

## Description

A ParallaxBackground uses one or more `ParallaxLayer<class_ParallaxLayer>` child nodes to create a parallax effect. Each `ParallaxLayer<class_ParallaxLayer>` can move at a different speed using `ParallaxLayer.motion_offset<class_ParallaxLayer_property_motion_offset>`. This creates an illusion of depth in a 2D game. If not used with a `Camera2D<class_Camera2D>`, you must manually calculate the `scroll_offset<class_ParallaxBackground_property_scroll_offset>`.

**Note:** Each **ParallaxBackground** is drawn on one specific `Viewport<class_Viewport>` and cannot be shared between multiple `Viewport<class_Viewport>`s, see `CanvasLayer.custom_viewport<class_CanvasLayer_property_custom_viewport>`. When using multiple `Viewport<class_Viewport>`s, for example in a split-screen game, you need create an individual **ParallaxBackground** for each `Viewport<class_Viewport>` you want it to be drawn on.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector2<class_Vector2>` **scroll_base_offset** = `Vector2(0, 0)` `🔗<class_ParallaxBackground_property_scroll_base_offset>`

classref-property-setget

- `void (No return value.)` **set_scroll_base_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_scroll_base_offset**()

The base position offset for all `ParallaxLayer<class_ParallaxLayer>` children.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **scroll_base_scale** = `Vector2(1, 1)` `🔗<class_ParallaxBackground_property_scroll_base_scale>`

classref-property-setget

- `void (No return value.)` **set_scroll_base_scale**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_scroll_base_scale**()

The base motion scale for all `ParallaxLayer<class_ParallaxLayer>` children.

classref-item-separator

classref-property

`bool<class_bool>` **scroll_ignore_camera_zoom** = `false` `🔗<class_ParallaxBackground_property_scroll_ignore_camera_zoom>`

classref-property-setget

- `void (No return value.)` **set_ignore_camera_zoom**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_ignore_camera_zoom**()

If `true`, elements in `ParallaxLayer<class_ParallaxLayer>` child aren't affected by the zoom level of the camera.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **scroll_limit_begin** = `Vector2(0, 0)` `🔗<class_ParallaxBackground_property_scroll_limit_begin>`

classref-property-setget

- `void (No return value.)` **set_limit_begin**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_limit_begin**()

Top-left limits for scrolling to begin. If the camera is outside of this limit, the background will stop scrolling. Must be lower than `scroll_limit_end<class_ParallaxBackground_property_scroll_limit_end>` to work.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **scroll_limit_end** = `Vector2(0, 0)` `🔗<class_ParallaxBackground_property_scroll_limit_end>`

classref-property-setget

- `void (No return value.)` **set_limit_end**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_limit_end**()

Bottom-right limits for scrolling to end. If the camera is outside of this limit, the background will stop scrolling. Must be higher than `scroll_limit_begin<class_ParallaxBackground_property_scroll_limit_begin>` to work.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **scroll_offset** = `Vector2(0, 0)` `🔗<class_ParallaxBackground_property_scroll_offset>`

classref-property-setget

- `void (No return value.)` **set_scroll_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_scroll_offset**()

The ParallaxBackground's scroll value. Calculated automatically when using a `Camera2D<class_Camera2D>`, but can be used to manually manage scrolling when no camera is present.