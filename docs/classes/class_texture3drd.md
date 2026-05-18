github_url
hide

# Texture3DRD

**Inherits:** `Texture3D<class_Texture3D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Texture for 3D that is bound to a texture created on the `RenderingDevice<class_RenderingDevice>`.

classref-introduction-group

## Description

This texture class allows you to use a 3D texture created directly on the `RenderingDevice<class_RenderingDevice>` as a texture for materials, meshes, etc.

**Note:** **Texture3DRD** is intended for low-level usage with `RenderingDevice<class_RenderingDevice>`. For most use cases, use `Texture3D<class_Texture3D>` instead.

classref-introduction-group

## Tutorials

- [Compute Texture demo](https://godotengine.org/asset-library/asset/2764)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **texture_rd_rid** `🔗<class_Texture3DRD_property_texture_rd_rid>`

classref-property-setget

- `void (No return value.)` **set_texture_rd_rid**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_texture_rd_rid**()

The RID of the texture object created on the `RenderingDevice<class_RenderingDevice>`.