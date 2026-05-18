github_url
hide

# OpenXRCompositionLayerEquirect

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRCompositionLayer<class_OpenXRCompositionLayer>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

An OpenXR composition layer that is rendered as an internal slice of a sphere.

classref-introduction-group

## Description

An OpenXR composition layer that allows rendering a `SubViewport<class_SubViewport>` on an internal slice of a sphere.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **central_horizontal_angle** = `1.5707964` `🔗<class_OpenXRCompositionLayerEquirect_property_central_horizontal_angle>`

classref-property-setget

- `void (No return value.)` **set_central_horizontal_angle**(value: `float<class_float>`)
- `float<class_float>` **get_central_horizontal_angle**()

The central horizontal angle of the sphere. Used to set the width.

classref-item-separator

classref-property

`int<class_int>` **fallback_segments** = `10` `🔗<class_OpenXRCompositionLayerEquirect_property_fallback_segments>`

classref-property-setget

- `void (No return value.)` **set_fallback_segments**(value: `int<class_int>`)
- `int<class_int>` **get_fallback_segments**()

The number of segments to use in the fallback mesh.

classref-item-separator

classref-property

`float<class_float>` **lower_vertical_angle** = `0.7853982` `🔗<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>`

classref-property-setget

- `void (No return value.)` **set_lower_vertical_angle**(value: `float<class_float>`)
- `float<class_float>` **get_lower_vertical_angle**()

The lower vertical angle of the sphere. Used (together with `upper_vertical_angle<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>`) to set the height.

classref-item-separator

classref-property

`float<class_float>` **radius** = `1.0` `🔗<class_OpenXRCompositionLayerEquirect_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

The radius of the sphere.

classref-item-separator

classref-property

`float<class_float>` **upper_vertical_angle** = `0.7853982` `🔗<class_OpenXRCompositionLayerEquirect_property_upper_vertical_angle>`

classref-property-setget

- `void (No return value.)` **set_upper_vertical_angle**(value: `float<class_float>`)
- `float<class_float>` **get_upper_vertical_angle**()

The upper vertical angle of the sphere. Used (together with `lower_vertical_angle<class_OpenXRCompositionLayerEquirect_property_lower_vertical_angle>`) to set the height.