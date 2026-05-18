github_url
hide

# RenderSceneDataExtension

**Inherits:** `RenderSceneData<class_RenderSceneData>` **\<** `Object<class_Object>`

This class allows for a RenderSceneData implementation to be made in GDExtension.

classref-introduction-group

## Description

This class allows for a RenderSceneData implementation to be made in GDExtension.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Projection<class_Projection>` **\_get_cam_projection**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneDataExtension_private_method__get_cam_projection>`

Implement this in GDExtension to return the camera `Projection<class_Projection>`.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **\_get_cam_transform**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneDataExtension_private_method__get_cam_transform>`

Implement this in GDExtension to return the camera `Transform3D<class_Transform3D>`.

classref-item-separator

classref-method

`RID<class_RID>` **\_get_uniform_buffer**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneDataExtension_private_method__get_uniform_buffer>`

Implement this in GDExtension to return the `RID<class_RID>` of the uniform buffer containing the scene data as a UBO.

classref-item-separator

classref-method

`int<class_int>` **\_get_view_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneDataExtension_private_method__get_view_count>`

Implement this in GDExtension to return the view count.

classref-item-separator

classref-method

`Vector3<class_Vector3>` **\_get_view_eye_offset**(view: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneDataExtension_private_method__get_view_eye_offset>`

Implement this in GDExtension to return the eye offset for the given `view`.

classref-item-separator

classref-method

`Projection<class_Projection>` **\_get_view_projection**(view: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RenderSceneDataExtension_private_method__get_view_projection>`

Implement this in GDExtension to return the view `Projection<class_Projection>` for the given `view`.