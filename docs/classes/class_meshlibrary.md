github_url
hide

# MeshLibrary

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Library of meshes.

classref-introduction-group

## Description

A library of meshes. Contains a list of `Mesh<class_Mesh>` resources, each with a name and ID. Each item can also include collision and navigation shapes. This resource is used in `GridMap<class_GridMap>`.

classref-introduction-group

## Tutorials

- [3D Kinematic Character Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear**() `🔗<class_MeshLibrary_method_clear>`

Clears the library.

classref-item-separator

classref-method

`void (No return value.)` **create_item**(id: `int<class_int>`) `🔗<class_MeshLibrary_method_create_item>`

Creates a new item in the library with the given ID.

You can get an unused ID from `get_last_unused_item_id()<class_MeshLibrary_method_get_last_unused_item_id>`.

classref-item-separator

classref-method

`int<class_int>` **find_item_by_name**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_find_item_by_name>`

Returns the first item with the given name, or `-1` if no item is found.

classref-item-separator

classref-method

`int<class_int>` **get_item_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_count>`

Returns the number of items present in the library.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_item_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_list>`

Returns the list of item IDs in use.

classref-item-separator

classref-method

`Mesh<class_Mesh>` **get_item_mesh**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_mesh>`

Returns the item's mesh.

classref-item-separator

classref-method

`ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>` **get_item_mesh_cast_shadow**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_mesh_cast_shadow>`

Returns the item's shadow casting mode.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_item_mesh_transform**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_mesh_transform>`

Returns the transform applied to the item's mesh.

classref-item-separator

classref-method

`String<class_String>` **get_item_name**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_name>`

Returns the item's name.

classref-item-separator

classref-method

`int<class_int>` **get_item_navigation_layers**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_navigation_layers>`

Returns the item's navigation layers bitmask.

classref-item-separator

classref-method

`NavigationMesh<class_NavigationMesh>` **get_item_navigation_mesh**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_navigation_mesh>`

Returns the item's navigation mesh.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_item_navigation_mesh_transform**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_navigation_mesh_transform>`

Returns the transform applied to the item's navigation mesh.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_item_preview**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_preview>`

When running in the editor, returns a generated item preview (a 3D rendering in isometric perspective). When used in a running project, returns the manually-defined item preview which can be set using `set_item_preview()<class_MeshLibrary_method_set_item_preview>`. Returns an empty `Texture2D<class_Texture2D>` if no preview was manually set in a running project.

classref-item-separator

classref-method

`Array<class_Array>` **get_item_shapes**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_item_shapes>`

Returns an item's collision shapes.

The array consists of each `Shape3D<class_Shape3D>` followed by its `Transform3D<class_Transform3D>`.

classref-item-separator

classref-method

`int<class_int>` **get_last_unused_item_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MeshLibrary_method_get_last_unused_item_id>`

Gets an unused ID for a new item.

classref-item-separator

classref-method

`void (No return value.)` **remove_item**(id: `int<class_int>`) `🔗<class_MeshLibrary_method_remove_item>`

Removes the item.

classref-item-separator

classref-method

`void (No return value.)` **set_item_mesh**(id: `int<class_int>`, mesh: `Mesh<class_Mesh>`) `🔗<class_MeshLibrary_method_set_item_mesh>`

Sets the item's mesh.

classref-item-separator

classref-method

`void (No return value.)` **set_item_mesh_cast_shadow**(id: `int<class_int>`, shadow_casting_setting: `ShadowCastingSetting<enum_RenderingServer_ShadowCastingSetting>`) `🔗<class_MeshLibrary_method_set_item_mesh_cast_shadow>`

Sets the item's shadow casting mode to `shadow_casting_setting`.

classref-item-separator

classref-method

`void (No return value.)` **set_item_mesh_transform**(id: `int<class_int>`, mesh_transform: `Transform3D<class_Transform3D>`) `🔗<class_MeshLibrary_method_set_item_mesh_transform>`

Sets the transform to apply to the item's mesh.

classref-item-separator

classref-method

`void (No return value.)` **set_item_name**(id: `int<class_int>`, name: `String<class_String>`) `🔗<class_MeshLibrary_method_set_item_name>`

Sets the item's name.

This name is shown in the editor. It can also be used to look up the item later using `find_item_by_name()<class_MeshLibrary_method_find_item_by_name>`.

classref-item-separator

classref-method

`void (No return value.)` **set_item_navigation_layers**(id: `int<class_int>`, navigation_layers: `int<class_int>`) `🔗<class_MeshLibrary_method_set_item_navigation_layers>`

Sets the item's navigation layers bitmask.

classref-item-separator

classref-method

`void (No return value.)` **set_item_navigation_mesh**(id: `int<class_int>`, navigation_mesh: `NavigationMesh<class_NavigationMesh>`) `🔗<class_MeshLibrary_method_set_item_navigation_mesh>`

Sets the item's navigation mesh.

classref-item-separator

classref-method

`void (No return value.)` **set_item_navigation_mesh_transform**(id: `int<class_int>`, navigation_mesh: `Transform3D<class_Transform3D>`) `🔗<class_MeshLibrary_method_set_item_navigation_mesh_transform>`

Sets the transform to apply to the item's navigation mesh.

classref-item-separator

classref-method

`void (No return value.)` **set_item_preview**(id: `int<class_int>`, texture: `Texture2D<class_Texture2D>`) `🔗<class_MeshLibrary_method_set_item_preview>`

Sets a texture to use as the item's preview icon in the editor.

classref-item-separator

classref-method

`void (No return value.)` **set_item_shapes**(id: `int<class_int>`, shapes: `Array<class_Array>`) `🔗<class_MeshLibrary_method_set_item_shapes>`

Sets an item's collision shapes.

The array should consist of `Shape3D<class_Shape3D>` objects, each followed by a `Transform3D<class_Transform3D>` that will be applied to it. For shapes that should not have a transform, use `Transform3D.IDENTITY<class_Transform3D_constant_IDENTITY>`.