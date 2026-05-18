github_url
hide

# MeshInstance2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Node used for displaying a `Mesh<class_Mesh>` in 2D.

classref-introduction-group

## Description

Node used for displaying a `Mesh<class_Mesh>` in 2D. This can be faster to render compared to displaying a `Sprite2D<class_Sprite2D>` node with large transparent areas, especially if the node takes up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprite's opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).

When a `Mesh<class_Mesh>` has to be instantiated more than thousands of times close to each other, consider using a `MultiMesh<class_MultiMesh>` in a `MultiMeshInstance2D<class_MultiMeshInstance2D>` instead.

A **MeshInstance2D** can be created from an existing `Sprite2D<class_Sprite2D>` via a tool in the editor toolbar. Select the `Sprite2D<class_Sprite2D>` node, then choose **Sprite2D \> Convert to MeshInstance2D** at the top of the 2D editor viewport.

classref-introduction-group

## Tutorials

- `2D meshes <../tutorials/2d/2d_meshes>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**texture_changed**() `🔗<class_MeshInstance2D_signal_texture_changed>`

Emitted when the `texture<class_MeshInstance2D_property_texture>` is changed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Mesh<class_Mesh>` **mesh** `🔗<class_MeshInstance2D_property_mesh>`

classref-property-setget

- `void (No return value.)` **set_mesh**(value: `Mesh<class_Mesh>`)
- `Mesh<class_Mesh>` **get_mesh**()

The `Mesh<class_Mesh>` that will be drawn by the **MeshInstance2D**.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **texture** `🔗<class_MeshInstance2D_property_texture>`

classref-property-setget

- `void (No return value.)` **set_texture**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_texture**()

The `Texture2D<class_Texture2D>` that will be used if using the default `CanvasItemMaterial<class_CanvasItemMaterial>`. Can be accessed as `TEXTURE` in CanvasItem shader.