github_url
hide

# TextureLayeredRD

**Inherits:** `TextureLayered<class_TextureLayered>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `Texture2DArrayRD<class_Texture2DArrayRD>`, `TextureCubemapArrayRD<class_TextureCubemapArrayRD>`, `TextureCubemapRD<class_TextureCubemapRD>`

Abstract base class for layered texture RD types.

classref-introduction-group

## Description

Base class for `Texture2DArrayRD<class_Texture2DArrayRD>`, `TextureCubemapRD<class_TextureCubemapRD>` and `TextureCubemapArrayRD<class_TextureCubemapArrayRD>`. Cannot be used directly, but contains all the functions necessary for accessing the derived resource types.

**Note:** **TextureLayeredRD** is intended for low-level usage with `RenderingDevice<class_RenderingDevice>`. For most use cases, use `TextureLayered<class_TextureLayered>` instead.

classref-introduction-group

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **texture_rd_rid** `🔗<class_TextureLayeredRD_property_texture_rd_rid>`

classref-property-setget

- `void (No return value.)` **set_texture_rd_rid**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_texture_rd_rid**()

The RID of the texture object created on the `RenderingDevice<class_RenderingDevice>`.