github_url
hide

# RenderDataExtension

**Inherits:** `RenderData<class_RenderData>` **\<** `Object<class_Object>`

This class allows for a RenderData implementation to be made in GDExtension.

classref-introduction-group

## Description

This class allows for a RenderData implementation to be made in GDExtension.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **\_get_camera_attributes**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderDataExtension_private_method__get_camera_attributes>`

Implement this in GDExtension to return the `RID<class_RID>` for the implementation's camera attributes object.

classref-item-separator

classref-method

`RID<class_RID>` **\_get_environment**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderDataExtension_private_method__get_environment>`

Implement this in GDExtension to return the `RID<class_RID>` of the implementation's environment object.

classref-item-separator

classref-method

`RenderSceneBuffers<class_RenderSceneBuffers>` **\_get_render_scene_buffers**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderDataExtension_private_method__get_render_scene_buffers>`

Implement this in GDExtension to return the implementation's `RenderSceneBuffers<class_RenderSceneBuffers>` object.

classref-item-separator

classref-method

`RenderSceneData<class_RenderSceneData>` **\_get_render_scene_data**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderDataExtension_private_method__get_render_scene_data>`

Implement this in GDExtension to return the implementation's `RenderSceneDataExtension<class_RenderSceneDataExtension>` object.