github_url
hide

# AtlasTexture

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A texture that crops out part of another Texture2D.

classref-introduction-group

## Description

`Texture2D<class_Texture2D>` resource that draws only part of its `atlas<class_AtlasTexture_property_atlas>` texture, as defined by the `region<class_AtlasTexture_property_region>`. An additional `margin<class_AtlasTexture_property_margin>` can also be set, which is useful for small adjustments.

Multiple **AtlasTexture** resources can be cropped from the same `atlas<class_AtlasTexture_property_atlas>`. Packing many smaller textures into a singular large texture helps to optimize video memory costs and render calls.

**Note:** **AtlasTexture** cannot be used in an `AnimatedTexture<class_AnimatedTexture>`, and will not tile properly in nodes such as `TextureRect<class_TextureRect>` or `Sprite2D<class_Sprite2D>`. To tile an **AtlasTexture**, modify its `region<class_AtlasTexture_property_region>` instead.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Texture2D<class_Texture2D>` **atlas** `🔗<class_AtlasTexture_property_atlas>`

classref-property-setget

- `void (No return value.)` **set_atlas**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_atlas**()

The texture that contains the atlas. Can be any type inheriting from `Texture2D<class_Texture2D>`, including another **AtlasTexture**.

classref-item-separator

classref-property

`bool<class_bool>` **filter_clip** = `false` `🔗<class_AtlasTexture_property_filter_clip>`

classref-property-setget

- `void (No return value.)` **set_filter_clip**(value: `bool<class_bool>`)
- `bool<class_bool>` **has_filter_clip**()

If `true`, the area outside of the `region<class_AtlasTexture_property_region>` is clipped to avoid bleeding of the surrounding texture pixels.

classref-item-separator

classref-property

`Rect2<class_Rect2>` **margin** = `Rect2(0, 0, 0, 0)` `🔗<class_AtlasTexture_property_margin>`

classref-property-setget

- `void (No return value.)` **set_margin**(value: `Rect2<class_Rect2>`)
- `Rect2<class_Rect2>` **get_margin**()

The margin around the `region<class_AtlasTexture_property_region>`. Useful for small adjustments. If the `Rect2.size<class_Rect2_property_size>` of this property ("w" and "h" in the editor) is set, the drawn texture is resized to fit within the margin.

classref-item-separator

classref-property

`Rect2<class_Rect2>` **region** = `Rect2(0, 0, 0, 0)` `🔗<class_AtlasTexture_property_region>`

classref-property-setget

- `void (No return value.)` **set_region**(value: `Rect2<class_Rect2>`)
- `Rect2<class_Rect2>` **get_region**()

The region used to draw the `atlas<class_AtlasTexture_property_atlas>`. If either dimension of the region's size is `0`, the value from `atlas<class_AtlasTexture_property_atlas>` size will be used for that axis instead.

**Note:** The image size is always an integer, so the actual region size is rounded down.