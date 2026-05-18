github_url
hide

# Sprite2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

General-purpose sprite node.

classref-introduction-group

## Description

A node that displays a 2D texture. The texture displayed can be a region from a larger atlas texture, or a frame from a sprite sheet animation.

classref-introduction-group

## Tutorials

- [Instancing Demo](https://godotengine.org/asset-library/asset/2716)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**frame_changed**() `🔗<class_Sprite2D_signal_frame_changed>`

Emitted when the `frame<class_Sprite2D_property_frame>` changes.

classref-item-separator

classref-signal

**texture_changed**() `🔗<class_Sprite2D_signal_texture_changed>`

Emitted when the `texture<class_Sprite2D_property_texture>` changes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **centered** = `true` `🔗<class_Sprite2D_property_centered>`

classref-property-setget

- `void (No return value.)` **set_centered**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_centered**()

If `true`, texture is centered.

**Note:** For games with a pixel art aesthetic, textures may appear deformed when centered. This is caused by their position being between pixels. To prevent this, set this property to `false`, or consider enabling `ProjectSettings.rendering/2d/snap/snap_2d_vertices_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_vertices_to_pixel>` and `ProjectSettings.rendering/2d/snap/snap_2d_transforms_to_pixel<class_ProjectSettings_property_rendering/2d/snap/snap_2d_transforms_to_pixel>`.

classref-item-separator

classref-property

`bool<class_bool>` **flip_h** = `false` `🔗<class_Sprite2D_property_flip_h>`

classref-property-setget

- `void (No return value.)` **set_flip_h**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_flipped_h**()

If `true`, texture is flipped horizontally.

classref-item-separator

classref-property

`bool<class_bool>` **flip_v** = `false` `🔗<class_Sprite2D_property_flip_v>`

classref-property-setget

- `void (No return value.)` **set_flip_v**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_flipped_v**()

If `true`, texture is flipped vertically.

classref-item-separator

classref-property

`int<class_int>` **frame** = `0` `🔗<class_Sprite2D_property_frame>`

classref-property-setget

- `void (No return value.)` **set_frame**(value: `int<class_int>`)
- `int<class_int>` **get_frame**()

Current frame to display from sprite sheet. `hframes<class_Sprite2D_property_hframes>` or `vframes<class_Sprite2D_property_vframes>` must be greater than 1. This property is automatically adjusted when `hframes<class_Sprite2D_property_hframes>` or `vframes<class_Sprite2D_property_vframes>` are changed to keep pointing to the same visual frame (same column and row). If that's impossible, this value is reset to `0`.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **frame_coords** = `Vector2i(0, 0)` `🔗<class_Sprite2D_property_frame_coords>`

classref-property-setget

- `void (No return value.)` **set_frame_coords**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_frame_coords**()

Coordinates of the frame to display from sprite sheet. This is as an alias for the `frame<class_Sprite2D_property_frame>` property. `hframes<class_Sprite2D_property_hframes>` or `vframes<class_Sprite2D_property_vframes>` must be greater than 1.

classref-item-separator

classref-property

`int<class_int>` **hframes** = `1` `🔗<class_Sprite2D_property_hframes>`

classref-property-setget

- `void (No return value.)` **set_hframes**(value: `int<class_int>`)
- `int<class_int>` **get_hframes**()

The number of columns in the sprite sheet. When this property is changed, `frame<class_Sprite2D_property_frame>` is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, `frame<class_Sprite2D_property_frame>` is reset to `0`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **offset** = `Vector2(0, 0)` `🔗<class_Sprite2D_property_offset>`

classref-property-setget

- `void (No return value.)` **set_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_offset**()

The texture's drawing offset.

**Note:** When you increase `offset<class_Sprite2D_property_offset>`.y in Sprite2D, the sprite moves downward on screen (i.e., +Y is down).

classref-item-separator

classref-property

`bool<class_bool>` **region_enabled** = `false` `🔗<class_Sprite2D_property_region_enabled>`

classref-property-setget

- `void (No return value.)` **set_region_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_region_enabled**()

If `true`, texture is cut from a larger atlas texture. See `region_rect<class_Sprite2D_property_region_rect>`.

**Note:** When using a custom `Shader<class_Shader>` on a **Sprite2D**, the `UV` shader built-in will refer to the entire texture space. Use the `REGION_RECT` built-in to get the currently visible region defined in `region_rect<class_Sprite2D_property_region_rect>` instead. See `CanvasItem shaders <../tutorials/shaders/shader_reference/canvas_item_shader>` for details.

classref-item-separator

classref-property

`bool<class_bool>` **region_filter_clip_enabled** = `false` `🔗<class_Sprite2D_property_region_filter_clip_enabled>`

classref-property-setget

- `void (No return value.)` **set_region_filter_clip_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_region_filter_clip_enabled**()

If `true`, the area outside of the `region_rect<class_Sprite2D_property_region_rect>` is clipped to avoid bleeding of the surrounding texture pixels. `region_enabled<class_Sprite2D_property_region_enabled>` must be `true`.

classref-item-separator

classref-property

`Rect2<class_Rect2>` **region_rect** = `Rect2(0, 0, 0, 0)` `🔗<class_Sprite2D_property_region_rect>`

classref-property-setget

- `void (No return value.)` **set_region_rect**(value: `Rect2<class_Rect2>`)
- `Rect2<class_Rect2>` **get_region_rect**()

The region of the atlas texture to display. `region_enabled<class_Sprite2D_property_region_enabled>` must be `true`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_Sprite2D_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

`Texture2D<class_Texture2D>` object to draw.

classref-item-separator

classref-property

`int<class_int>` **vframes** = `1` `🔗<class_Sprite2D_property_vframes>`

classref-property-setget

- `void (No return value.)` **set_vframes**(value: `int<class_int>`)
- `int<class_int>` **get_vframes**()

The number of rows in the sprite sheet. When this property is changed, `frame<class_Sprite2D_property_frame>` is adjusted so that the same visual frame is maintained (same row and column). If that's impossible, `frame<class_Sprite2D_property_frame>` is reset to `0`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Rect2<class_Rect2>` **get_rect**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Sprite2D_method_get_rect>`

Returns a `Rect2<class_Rect2>` representing the Sprite2D's boundary in local coordinates.

**Example:** Detect if the Sprite2D was clicked:

gdscript

func input(event):
if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
if get_rect().has_point(to_local(event.position)):
print("A click!")

csharp

public override void Input(InputEvent @event) { if (@event is InputEventMouseButton inputEventMouse) { if (inputEventMouse.Pressed && inputEventMouse.ButtonIndex == MouseButton.Left) { if (GetRect().HasPoint(ToLocal(inputEventMouse.Position))) { GD.Print("A click!"); } } } }

classref-item-separator

classref-method

`bool<class_bool>` **is_pixel_opaque**(pos: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Sprite2D_method_is_pixel_opaque>`

Returns `true` if the pixel at the given position is opaque, `false` otherwise. Also returns `false` if the given position is out of bounds or this sprite's `texture<class_Sprite2D_property_texture>` is `null`. `pos` is in local coordinates.