github_url
hide

# OpenXRRenderModel

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

This node will display an OpenXR render model.

classref-introduction-group

## Description

This node will display an OpenXR render model by accessing the associated GLTF and processes all animation data (if supported by the XR runtime).

Render models were introduced to allow showing the correct model for the controller (or other device) the user has in hand, since the OpenXR action map does not provide information about the hardware used by the user. Note that while the controller (or device) can be somewhat inferred by the bound action map profile, this is a dangerous approach as the user may be using hardware not known at time of development and OpenXR will simply simulate an available interaction profile.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**render_model_top_level_path_changed**() `🔗<class_OpenXRRenderModel_signal_render_model_top_level_path_changed>`

Emitted when the top level path of this render model has changed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **render_model** = `RID()` `🔗<class_OpenXRRenderModel_property_render_model>`

classref-property-setget

- `void (No return value.)` **set_render_model**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_render_model**()

The render model RID for the render model to load, as returned by `OpenXRRenderModelExtension.render_model_create()<class_OpenXRRenderModelExtension_method_render_model_create>` or `OpenXRRenderModelExtension.render_model_get_all()<class_OpenXRRenderModelExtension_method_render_model_get_all>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_top_level_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModel_method_get_top_level_path>`

Returns the top level path related to this render model.