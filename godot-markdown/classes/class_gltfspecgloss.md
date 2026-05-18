github_url
hide

# GLTFSpecGloss

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Archived glTF extension for specular/glossy materials.

classref-introduction-group

## Description

KHR_materials_pbrSpecularGlossiness is an archived glTF extension. This means that it is deprecated and not recommended for new files. However, it is still supported for loading old files.

classref-introduction-group

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`
- [KHR_materials_pbrSpecularGlossiness glTF extension spec](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Archived/KHR_materials_pbrSpecularGlossiness)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **diffuse_factor** = `Color(1, 1, 1, 1)` `🔗<class_GLTFSpecGloss_property_diffuse_factor>`

classref-property-setget

- `void (No return value.)` **set_diffuse_factor**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_diffuse_factor**()

The reflected diffuse factor of the material.

classref-item-separator

classref-property

`Image<class_Image>` **diffuse_img** `🔗<class_GLTFSpecGloss_property_diffuse_img>`

classref-property-setget

- `void (No return value.)` **set_diffuse_img**(value: `Image<class_Image>`)
- `Image<class_Image>` **get_diffuse_img**()

The diffuse texture.

classref-item-separator

classref-property

`float<class_float>` **gloss_factor** = `1.0` `🔗<class_GLTFSpecGloss_property_gloss_factor>`

classref-property-setget

- `void (No return value.)` **set_gloss_factor**(value: `float<class_float>`)
- `float<class_float>` **get_gloss_factor**()

The glossiness or smoothness of the material.

classref-item-separator

classref-property

`Image<class_Image>` **spec_gloss_img** `🔗<class_GLTFSpecGloss_property_spec_gloss_img>`

classref-property-setget

- `void (No return value.)` **set_spec_gloss_img**(value: `Image<class_Image>`)
- `Image<class_Image>` **get_spec_gloss_img**()

The specular-glossiness texture.

classref-item-separator

classref-property

`Color<class_Color>` **specular_factor** = `Color(1, 1, 1, 1)` `🔗<class_GLTFSpecGloss_property_specular_factor>`

classref-property-setget

- `void (No return value.)` **set_specular_factor**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_specular_factor**()

The specular RGB color of the material. The alpha channel is unused.