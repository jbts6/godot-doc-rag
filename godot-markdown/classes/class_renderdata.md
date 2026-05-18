github_url
hide

# RenderData

**Inherits:** `Object<class_Object>`

**Inherited By:** `RenderDataExtension<class_RenderDataExtension>`, `RenderDataRD<class_RenderDataRD>`

Abstract render data object, holds frame data related to rendering a single frame of a viewport.

classref-introduction-group

## Description

Abstract render data object, exists for the duration of rendering a single viewport. See also `RenderDataRD<class_RenderDataRD>`, `RenderSceneData<class_RenderSceneData>`, and `RenderSceneDataRD<class_RenderSceneDataRD>`.

**Note:** This is an internal rendering server object. Do not instantiate this class from a script.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **get_camera_attributes**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderData_method_get_camera_attributes>`

Returns the `RID<class_RID>` of the camera attributes object in the `RenderingServer<class_RenderingServer>` being used to render this viewport.

classref-item-separator

classref-method

`RID<class_RID>` **get_environment**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderData_method_get_environment>`

Returns the `RID<class_RID>` of the environment object in the `RenderingServer<class_RenderingServer>` being used to render this viewport.

classref-item-separator

classref-method

`RenderSceneBuffers<class_RenderSceneBuffers>` **get_render_scene_buffers**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderData_method_get_render_scene_buffers>`

Returns the `RenderSceneBuffers<class_RenderSceneBuffers>` object managing the scene buffers for rendering this viewport.

classref-item-separator

classref-method

`RenderSceneData<class_RenderSceneData>` **get_render_scene_data**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderData_method_get_render_scene_data>`

Returns the `RenderSceneData<class_RenderSceneData>` object managing this frames scene data.