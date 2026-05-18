github_url
hide

# WorldEnvironment

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

Default environment properties for the entire scene (post-processing effects, lighting and background settings).

classref-introduction-group

## Description

The **WorldEnvironment** node is used to configure the default `Environment<class_Environment>` for the scene.

The parameters defined in the **WorldEnvironment** can be overridden by an `Environment<class_Environment>` node set on the current `Camera3D<class_Camera3D>`. Additionally, only one **WorldEnvironment** may be instantiated in a given scene at a time.

The **WorldEnvironment** allows the user to specify default lighting parameters (e.g. ambient lighting), various post-processing effects (e.g. SSAO, DOF, Tonemapping), and how to draw the background (e.g. solid color, skybox). Usually, these are added in order to improve the realism/color balance of the scene.

classref-introduction-group

## Tutorials

- `Environment and post-processing <../tutorials/3d/environment_and_post_processing>`
- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`CameraAttributes<class_CameraAttributes>` **camera_attributes** `🔗<class_WorldEnvironment_property_camera_attributes>`

classref-property-setget

- `void (No return value.)` **set_camera_attributes**(value: `CameraAttributes<class_CameraAttributes>`)
- `CameraAttributes<class_CameraAttributes>` **get_camera_attributes**()

The default `CameraAttributes<class_CameraAttributes>` resource to use if none set on the `Camera3D<class_Camera3D>`.

classref-item-separator

classref-property

`Compositor<class_Compositor>` **compositor** `🔗<class_WorldEnvironment_property_compositor>`

classref-property-setget

- `void (No return value.)` **set_compositor**(value: `Compositor<class_Compositor>`)
- `Compositor<class_Compositor>` **get_compositor**()

The default `Compositor<class_Compositor>` resource to use if none set on the `Camera3D<class_Camera3D>`.

classref-item-separator

classref-property

`Environment<class_Environment>` **environment** `🔗<class_WorldEnvironment_property_environment>`

classref-property-setget

- `void (No return value.)` **set_environment**(value: `Environment<class_Environment>`)
- `Environment<class_Environment>` **get_environment**()

The `Environment<class_Environment>` resource used by this **WorldEnvironment**, defining the default properties.