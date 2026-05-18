github_url
hide

# OpenXRRenderModelExtension

**Inherits:** `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>` **\<** `Object<class_Object>`

This class implements the OpenXR Render Model Extension.

classref-introduction-group

## Description

This class implements the OpenXR Render Model Extension, if enabled it will maintain a list of active render models and provides an interface to the render model data.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**render_model_added**(render_model: `RID<class_RID>`) `🔗<class_OpenXRRenderModelExtension_signal_render_model_added>`

Emitted when a new render model is added.

classref-item-separator

classref-signal

**render_model_removed**(render_model: `RID<class_RID>`) `🔗<class_OpenXRRenderModelExtension_signal_render_model_removed>`

Emitted when a render model is removed.

classref-item-separator

classref-signal

**render_model_top_level_path_changed**(render_model: `RID<class_RID>`) `🔗<class_OpenXRRenderModelExtension_signal_render_model_top_level_path_changed>`

Emitted when the top level path associated with a render model changed.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_active**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_is_active>`

Returns `true` if OpenXR's render model extension is supported and enabled.

**Note:** This only returns a valid value after OpenXR has been initialized.

classref-item-separator

classref-method

`RID<class_RID>` **render_model_create**(render_model_id: `int<class_int>`) `🔗<class_OpenXRRenderModelExtension_method_render_model_create>`

Creates a render model object within OpenXR using a render model id.

**Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.

classref-item-separator

classref-method

`void (No return value.)` **render_model_destroy**(render_model: `RID<class_RID>`) `🔗<class_OpenXRRenderModelExtension_method_render_model_destroy>`

Destroys a render model object within OpenXR that was previously created with `render_model_create()<class_OpenXRRenderModelExtension_method_render_model_create>`.

**Note:** This function is exposed for dependent OpenXR extensions that provide render model ids to be used with the render model extension.

classref-item-separator

classref-method

`Array<class_Array>`\[`RID<class_RID>`\] **render_model_get_all**() `🔗<class_OpenXRRenderModelExtension_method_render_model_get_all>`

Returns an array of all currently active render models registered with this extension.

classref-item-separator

classref-method

`int<class_int>` **render_model_get_animatable_node_count**(render_model: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_count>`

Returns the number of animatable nodes this render model has.

classref-item-separator

classref-method

`String<class_String>` **render_model_get_animatable_node_name**(render_model: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_name>`

Returns the name of the given animatable node.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **render_model_get_animatable_node_transform**(render_model: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_get_animatable_node_transform>`

Returns the current local transform for an animatable node. This is updated every frame.

classref-item-separator

classref-method

`TrackingConfidence<enum_XRPose_TrackingConfidence>` **render_model_get_confidence**(render_model: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_get_confidence>`

Returns the tracking confidence of the tracking data for the render model.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **render_model_get_root_transform**(render_model: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_get_root_transform>`

Returns the root transform of a render model. This is the tracked position relative to our `XROrigin3D<class_XROrigin3D>` node.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **render_model_get_subaction_paths**(render_model: `RID<class_RID>`) `🔗<class_OpenXRRenderModelExtension_method_render_model_get_subaction_paths>`

Returns a list of active subaction paths for this `render_model`.

**Note:** If different devices are bound to your actions than available in suggested interaction bindings, this information shows paths related to the interaction bindings being mimicked by that device.

classref-item-separator

classref-method

`String<class_String>` **render_model_get_top_level_path**(render_model: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_get_top_level_path>`

Returns the top level path associated with this `render_model`. If provided this identifies whether the render model is associated with the player's hands or other body part.

classref-item-separator

classref-method

`bool<class_bool>` **render_model_is_animatable_node_visible**(render_model: `RID<class_RID>`, index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_is_animatable_node_visible>`

Returns `true` if this animatable node should be visible.

classref-item-separator

classref-method

`Node3D<class_Node3D>` **render_model_new_scene_instance**(render_model: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRRenderModelExtension_method_render_model_new_scene_instance>`

Returns an instance of a subscene that contains all `MeshInstance3D<class_MeshInstance3D>` nodes that allow you to visualize the render model.