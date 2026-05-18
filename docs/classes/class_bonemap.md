github_url
hide

# BoneMap

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Describes a mapping of bone names for retargeting `Skeleton3D<class_Skeleton3D>` into common names defined by a `SkeletonProfile<class_SkeletonProfile>`.

classref-introduction-group

## Description

This class contains a dictionary that uses a list of bone names in `SkeletonProfile<class_SkeletonProfile>` as key names.

By assigning the actual `Skeleton3D<class_Skeleton3D>` bone name as the key value, it maps the `Skeleton3D<class_Skeleton3D>` to the `SkeletonProfile<class_SkeletonProfile>`.

classref-introduction-group

## Tutorials

- `Retargeting 3D Skeletons <../tutorials/assets_pipeline/retargeting_3d_skeletons>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**bone_map_updated**() `🔗<class_BoneMap_signal_bone_map_updated>`

This signal is emitted when change the key value in the **BoneMap**. This is used to validate mapping and to update **BoneMap** editor.

classref-item-separator

classref-signal

**profile_updated**() `🔗<class_BoneMap_signal_profile_updated>`

This signal is emitted when change the value in profile or change the reference of profile. This is used to update key names in the **BoneMap** and to redraw the **BoneMap** editor.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`SkeletonProfile<class_SkeletonProfile>` **profile** `🔗<class_BoneMap_property_profile>`

classref-property-setget

- `void (No return value.)` **set_profile**(value: `SkeletonProfile<class_SkeletonProfile>`)
- `SkeletonProfile<class_SkeletonProfile>` **get_profile**()

A `SkeletonProfile<class_SkeletonProfile>` of the mapping target. Key names in the **BoneMap** are synchronized with it.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`StringName<class_StringName>` **find_profile_bone_name**(skeleton_bone_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneMap_method_find_profile_bone_name>`

Returns a profile bone name having `skeleton_bone_name`. If not found, an empty `StringName<class_StringName>` will be returned.

In the retargeting process, the returned bone name is the bone name of the target skeleton.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_skeleton_bone_name**(profile_bone_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BoneMap_method_get_skeleton_bone_name>`

Returns a skeleton bone name is mapped to `profile_bone_name`.

In the retargeting process, the returned bone name is the bone name of the source skeleton.

classref-item-separator

classref-method

`void (No return value.)` **set_skeleton_bone_name**(profile_bone_name: `StringName<class_StringName>`, skeleton_bone_name: `StringName<class_StringName>`) `🔗<class_BoneMap_method_set_skeleton_bone_name>`

Maps a skeleton bone name to `profile_bone_name`.

In the retargeting process, the setting bone name is the bone name of the source skeleton.