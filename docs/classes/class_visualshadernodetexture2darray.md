github_url
hide

# VisualShaderNodeTexture2DArray

**Inherits:** `VisualShaderNodeSample3D<class_VisualShaderNodeSample3D>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A 2D texture uniform array to be used within the visual shader graph.

classref-introduction-group

## Description

Translated to `uniform sampler2DArray` in the shader language.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`TextureLayered<class_TextureLayered>` **texture_array** `🔗<class_VisualShaderNodeTexture2DArray_property_texture_array>`

classref-property-setget

- `void (No return value.)` **set_texture_array**(value: `TextureLayered<class_TextureLayered>`)
- `TextureLayered<class_TextureLayered>` **get_texture_array**()

A source texture array. Used if `VisualShaderNodeSample3D.source<class_VisualShaderNodeSample3D_property_source>` is set to `VisualShaderNodeSample3D.SOURCE_TEXTURE<class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE>`.