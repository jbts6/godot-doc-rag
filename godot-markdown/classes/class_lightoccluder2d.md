github_url
hide

# LightOccluder2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Occludes light cast by a Light2D, casting shadows.

classref-introduction-group

## Description

Occludes light cast by a Light2D, casting shadows. The LightOccluder2D must be provided with an `OccluderPolygon2D<class_OccluderPolygon2D>` in order for the shadow to be computed.

classref-introduction-group

## Tutorials

- `2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OccluderPolygon2D<class_OccluderPolygon2D>` **occluder** `🔗<class_LightOccluder2D_property_occluder>`

classref-property-setget

- `void (No return value.)` **set_occluder_polygon**(value: `OccluderPolygon2D<class_OccluderPolygon2D>`)
- `OccluderPolygon2D<class_OccluderPolygon2D>` **get_occluder_polygon**()

The `OccluderPolygon2D<class_OccluderPolygon2D>` used to compute the shadow.

classref-item-separator

classref-property

`int<class_int>` **occluder_light_mask** = `1` `🔗<class_LightOccluder2D_property_occluder_light_mask>`

classref-property-setget

- `void (No return value.)` **set_occluder_light_mask**(value: `int<class_int>`)
- `int<class_int>` **get_occluder_light_mask**()

The LightOccluder2D's occluder light mask. The LightOccluder2D will cast shadows only from Light2D(s) that have the same light mask(s).

classref-item-separator

classref-property

`bool<class_bool>` **sdf_collision** = `true` `🔗<class_LightOccluder2D_property_sdf_collision>`

classref-property-setget

- `void (No return value.)` **set_as_sdf_collision**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_set_as_sdf_collision**()

If enabled, the occluder will be part of a real-time generated signed distance field that can be used in custom shaders.