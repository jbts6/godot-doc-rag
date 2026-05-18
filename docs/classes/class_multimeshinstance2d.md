github_url
hide

# MultiMeshInstance2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Node that instances a `MultiMesh<class_MultiMesh>` in 2D.

classref-introduction-group

## Description

**MultiMeshInstance2D** is a specialized node to instance a `MultiMesh<class_MultiMesh>` resource in 2D. This can be faster to render compared to displaying many `Sprite2D<class_Sprite2D>` nodes with large transparent areas, especially if the nodes take up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprites' opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

Usage is the same as `MultiMeshInstance3D<class_MultiMeshInstance3D>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**texture_changed**() `🔗<class_MultiMeshInstance2D_signal_texture_changed>`

Emitted when the `texture<class_MultiMeshInstance2D_property_texture>` is changed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`MultiMesh<class_MultiMesh>` **multimesh** `🔗<class_MultiMeshInstance2D_property_multimesh>`

classref-property-setget

- `void (No return value.)` **set_multimesh**(value: `MultiMesh<class_MultiMesh>`)
- `MultiMesh<class_MultiMesh>` **get_multimesh**()

The `MultiMesh<class_MultiMesh>` that will be drawn by the **MultiMeshInstance2D**.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_MultiMeshInstance2D_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

The `Texture2D<class_Texture2D>` that will be used if using the default `CanvasItemMaterial<class_CanvasItemMaterial>`. Can be accessed as `TEXTURE` in CanvasItem shader.