github_url
hide

# XRCamera3D

**Inherits:** `Camera3D<class_Camera3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A camera node which automatically positions itself based on XR tracking data.

classref-introduction-group

## Description

A camera node which automatically positions itself based on XR tracking data.

In contrast to `XRController3D<class_XRController3D>`, the render thread has access to more up-to-date tracking data, and the location of the **XRCamera3D** node can lag a few milliseconds behind what is used for rendering.

**Note:** If `Viewport.use_xr<class_Viewport_property_use_xr>` is `true`, most of the camera properties are overridden by the active `XRInterface<class_XRInterface>`. The only properties that can be trusted are the near and far planes.

classref-introduction-group

## Tutorials

- `XR documentation index <../tutorials/xr/index>`

classref-reftable-group

## Properties