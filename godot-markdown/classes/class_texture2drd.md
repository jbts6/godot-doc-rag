github_url
hide

# Texture2DRD

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Texture for 2D that is bound to a texture created on the `RenderingDevice<class_RenderingDevice>`.

classref-introduction-group

## Description

This texture class allows you to use a 2D texture created directly on the `RenderingDevice<class_RenderingDevice>` as a texture for materials, meshes, etc.

**Note:** **Texture2DRD** is intended for low-level usage with `RenderingDevice<class_RenderingDevice>`. For most use cases, use `Texture2D<class_Texture2D>` instead.

classref-introduction-group

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **texture_rd_rid** `🔗<class_Texture2DRD_property_texture_rd_rid>`

classref-property-setget

- `void (No return value.)` **set_texture_rd_rid**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_texture_rd_rid**()

The RID of the texture object created on the `RenderingDevice<class_RenderingDevice>`.