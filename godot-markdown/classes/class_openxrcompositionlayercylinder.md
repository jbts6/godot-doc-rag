github_url
hide

# OpenXRCompositionLayerCylinder

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRCompositionLayer<class_OpenXRCompositionLayer>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

An OpenXR composition layer that is rendered as an internal slice of a cylinder.

classref-introduction-group

## Description

An OpenXR composition layer that allows rendering a `SubViewport<class_SubViewport>` on an internal slice of a cylinder.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **aspect_ratio** = `1.0` `🔗<class_OpenXRCompositionLayerCylinder_property_aspect_ratio>`

classref-property-setget

- `void (No return value.)` **set_aspect_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_aspect_ratio**()

The aspect ratio of the slice. Used to set the height relative to the width.

classref-item-separator

classref-property

`float<class_float>` **central_angle** = `1.5707964` `🔗<class_OpenXRCompositionLayerCylinder_property_central_angle>`

classref-property-setget

- `void (No return value.)` **set_central_angle**(value: `float<class_float>`)
- `float<class_float>` **get_central_angle**()

The central angle of the cylinder. Used to set the width.

classref-item-separator

classref-property

`int<class_int>` **fallback_segments** = `10` `🔗<class_OpenXRCompositionLayerCylinder_property_fallback_segments>`

classref-property-setget

- `void (No return value.)` **set_fallback_segments**(value: `int<class_int>`)
- `int<class_int>` **get_fallback_segments**()

The number of segments to use in the fallback mesh.

classref-item-separator

classref-property

`float<class_float>` **radius** = `1.0` `🔗<class_OpenXRCompositionLayerCylinder_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

The radius of the cylinder.