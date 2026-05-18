github_url
hide

# Material

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `BaseMaterial3D<class_BaseMaterial3D>`, `BlitMaterial<class_BlitMaterial>`, `CanvasItemMaterial<class_CanvasItemMaterial>`, `FogMaterial<class_FogMaterial>`, `PanoramaSkyMaterial<class_PanoramaSkyMaterial>`, `ParticleProcessMaterial<class_ParticleProcessMaterial>`, `PhysicalSkyMaterial<class_PhysicalSkyMaterial>`, `PlaceholderMaterial<class_PlaceholderMaterial>`, `ProceduralSkyMaterial<class_ProceduralSkyMaterial>`, `ShaderMaterial<class_ShaderMaterial>`

Virtual base class for applying visual properties to an object, such as color and roughness.

classref-introduction-group

## Description

**Material** is a base resource used for coloring and shading geometry. All materials inherit from it and almost all `VisualInstance3D<class_VisualInstance3D>` derived nodes carry a **Material**. A few flags and parameters are shared between all material types and are configured here.

Importantly, you can inherit from **Material** to create your own custom material type in script or in GDExtension.

classref-introduction-group

## Tutorials

- [3D Material Testers Demo](https://godotengine.org/asset-library/asset/2742)
- [Third Person Shooter (TPS) Demo](https://godotengine.org/asset-library/asset/2710)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**RENDER_PRIORITY_MAX** = `127` `🔗<class_Material_constant_RENDER_PRIORITY_MAX>`

Maximum value for the `render_priority<class_Material_property_render_priority>` parameter.

classref-constant

**RENDER_PRIORITY_MIN** = `-128` `🔗<class_Material_constant_RENDER_PRIORITY_MIN>`

Minimum value for the `render_priority<class_Material_property_render_priority>` parameter.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Material<class_Material>` **next_pass** `🔗<class_Material_property_next_pass>`

classref-property-setget

- `void (No return value.)` **set_next_pass**(value: `Material<class_Material>`)
- `Material<class_Material>` **get_next_pass**()

Sets the **Material** to be used for the next pass. This renders the object again using a different material.

**Note:** `next_pass<class_Material_property_next_pass>` materials are not necessarily drawn immediately after the source **Material**. Draw order is determined by material properties, `render_priority<class_Material_property_render_priority>`, and distance to camera.

**Note:** This only applies to `StandardMaterial3D<class_StandardMaterial3D>`s and `ShaderMaterial<class_ShaderMaterial>`s with type "Spatial".

classref-item-separator

classref-property

`int<class_int>` **render_priority** `🔗<class_Material_property_render_priority>`

classref-property-setget

- `void (No return value.)` **set_render_priority**(value: `int<class_int>`)
- `int<class_int>` **get_render_priority**()

Sets the render priority for objects in 3D scenes. Higher priority objects will be sorted in front of lower priority objects. In other words, all objects with `render_priority<class_Material_property_render_priority>` `1` will render on top of all objects with `render_priority<class_Material_property_render_priority>` `0`.

**Note:** This only applies to `StandardMaterial3D<class_StandardMaterial3D>`s and `ShaderMaterial<class_ShaderMaterial>`s with type "Spatial".

**Note:** This will not impact how transparent objects are sorted relative to opaque objects or how dynamic meshes will be sorted relative to other opaque meshes. This is because all transparent objects are drawn after all opaque objects and all dynamic opaque meshes are drawn before other opaque meshes.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **\_can_do_next_pass**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Material_private_method__can_do_next_pass>`

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if `next_pass<class_Material_property_next_pass>` should be shown in the editor or not.

classref-item-separator

classref-method

`bool<class_bool>` **\_can_use_render_priority**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Material_private_method__can_use_render_priority>`

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally to determine if `render_priority<class_Material_property_render_priority>` should be shown in the editor or not.

classref-item-separator

classref-method

`Mode<enum_Shader_Mode>` **\_get_shader_mode**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Material_private_method__get_shader_mode>`

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools.

classref-item-separator

classref-method

`RID<class_RID>` **\_get_shader_rid**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Material_private_method__get_shader_rid>`

Only exposed for the purpose of overriding. You cannot call this function directly. Used internally by various editor tools. Used to access the RID of the **Material**'s `Shader<class_Shader>`.

classref-item-separator

classref-method

`Resource<class_Resource>` **create_placeholder**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Material_method_create_placeholder>`

Creates a placeholder version of this resource (`PlaceholderMaterial<class_PlaceholderMaterial>`).

classref-item-separator

classref-method

`void (No return value.)` **inspect_native_shader_code**() `🔗<class_Material_method_inspect_native_shader_code>`

Only available when running in the editor. Opens a popup that visualizes the generated shader code, including all variants and internal shader code. See also `Shader.inspect_native_shader_code()<class_Shader_method_inspect_native_shader_code>`.