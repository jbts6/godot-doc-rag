github_url
hide

# PointLight2D

**Inherits:** `Light2D<class_Light2D>` **\<** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Positional 2D light source.

classref-introduction-group

## Description

Casts light in a 2D environment. This light's shape is defined by a (usually grayscale) texture.

classref-introduction-group

## Tutorials

- `2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **height** = `0.0` `🔗<class_PointLight2D_property_height>`

classref-property-setget

- `void (No return value.)` **set_height**(value: `float<class_float>`)
- `float<class_float>` **get_height**()

The height of the light. Used with 2D normal mapping. The units are in pixels, e.g. if the height is 100, then it will illuminate an object 100 pixels away at a 45° angle to the plane.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **offset** = `Vector2(0, 0)` `🔗<class_PointLight2D_property_offset>`

classref-property-setget

- `void (No return value.)` **set_texture_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_texture_offset**()

The offset of the light's `texture<class_PointLight2D_property_texture>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_PointLight2D_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

`Texture2D<class_Texture2D>` used for the light's appearance.

classref-item-separator

classref-property

`float<class_float>` **texture_scale** = `1.0` `🔗<class_PointLight2D_property_texture_scale>`

classref-property-setget

- `void (No return value.)` **set_texture_scale**(value: `float<class_float>`)
- `float<class_float>` **get_texture_scale**()

The `texture<class_PointLight2D_property_texture>`'s scale factor.