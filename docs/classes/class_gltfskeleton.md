github_url
hide

# GLTFSkeleton

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-introduction-group

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedInt32Array<class_PackedInt32Array>` **joints** = `PackedInt32Array()` `🔗<class_GLTFSkeleton_property_joints>`

classref-property-setget

- `void (No return value.)` **set_joints**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_joints**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-item-separator

classref-property

`PackedInt32Array<class_PackedInt32Array>` **roots** = `PackedInt32Array()` `🔗<class_GLTFSkeleton_property_roots>`

classref-property-setget

- `void (No return value.)` **set_roots**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_roots**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`BoneAttachment3D<class_BoneAttachment3D>` **get_bone_attachment**(idx: `int<class_int>`) `🔗<class_GLTFSkeleton_method_get_bone_attachment>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **get_bone_attachment_count**() `🔗<class_GLTFSkeleton_method_get_bone_attachment_count>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_godot_bone_node**() `🔗<class_GLTFSkeleton_method_get_godot_bone_node>`

Returns a `Dictionary<class_Dictionary>` that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

classref-item-separator

classref-method

`Skeleton3D<class_Skeleton3D>` **get_godot_skeleton**() `🔗<class_GLTFSkeleton_method_get_godot_skeleton>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`Array<class_Array>`\[`String<class_String>`\] **get_unique_names**() `🔗<class_GLTFSkeleton_method_get_unique_names>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **set_godot_bone_node**(godot_bone_node: `Dictionary<class_Dictionary>`) `🔗<class_GLTFSkeleton_method_set_godot_bone_node>`

Sets a `Dictionary<class_Dictionary>` that maps skeleton bone indices to the indices of glTF nodes. This property is unused during import, and only set during export. In a glTF file, a bone is a node, so Godot converts skeleton bones to glTF nodes.

classref-item-separator

classref-method

`void (No return value.)` **set_unique_names**(unique_names: `Array<class_Array>`\[`String<class_String>`\]) `🔗<class_GLTFSkeleton_method_set_unique_names>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!