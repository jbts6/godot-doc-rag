github_url
hide

# RetargetModifier3D

**Inherits:** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A modifier to transfer parent skeleton poses (or global poses) to child skeletons in model space with different rests.

classref-introduction-group

## Description

Retrieves the pose (or global pose) relative to the parent Skeleton's rest in model space and transfers it to the child Skeleton.

This modifier rewrites the pose of the child skeleton directly in the parent skeleton's update process. This means that it overwrites the mapped bone pose set in the normal process on the target skeleton. If you want to set the target skeleton bone pose after retargeting, you will need to add a `SkeletonModifier3D<class_SkeletonModifier3D>` child to the target skeleton and thereby modify the pose.

**Note:** When the `use_global_pose<class_RetargetModifier3D_property_use_global_pose>` is enabled, even if it is an unmapped bone, it can cause visual problems because the global pose is applied ignoring the parent bone's pose **if it has mapped bone children**. See also `use_global_pose<class_RetargetModifier3D_property_use_global_pose>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

flags **TransformFlag**: `🔗<enum_RetargetModifier3D_TransformFlag>`

classref-enumeration-constant

`TransformFlag<enum_RetargetModifier3D_TransformFlag>` **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to retarget the position.

classref-enumeration-constant

`TransformFlag<enum_RetargetModifier3D_TransformFlag>` **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to retarget the rotation.

classref-enumeration-constant

`TransformFlag<enum_RetargetModifier3D_TransformFlag>` **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to retarget the scale.

classref-enumeration-constant

`TransformFlag<enum_RetargetModifier3D_TransformFlag>` **TRANSFORM_FLAG_ALL** = `7`

If set, allows to retarget the position/rotation/scale.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TransformFlag<enum_RetargetModifier3D_TransformFlag>`\] **enable** = `7` `🔗<class_RetargetModifier3D_property_enable>`

classref-property-setget

- `void (No return value.)` **set_enable_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TransformFlag<enum_RetargetModifier3D_TransformFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TransformFlag<enum_RetargetModifier3D_TransformFlag>`\] **get_enable_flags**()

Flags to control the process of the transform elements individually when `use_global_pose<class_RetargetModifier3D_property_use_global_pose>` is disabled.

classref-item-separator

classref-property

`SkeletonProfile<class_SkeletonProfile>` **profile** `🔗<class_RetargetModifier3D_property_profile>`

classref-property-setget

- `void (No return value.)` **set_profile**(value: `SkeletonProfile<class_SkeletonProfile>`)
- `SkeletonProfile<class_SkeletonProfile>` **get_profile**()

`SkeletonProfile<class_SkeletonProfile>` for retargeting bones with names matching the bone list.

classref-item-separator

classref-property

`bool<class_bool>` **use_global_pose** = `false` `🔗<class_RetargetModifier3D_property_use_global_pose>`

classref-property-setget

- `void (No return value.)` **set_use_global_pose**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_global_pose**()

If `false`, in case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform will be ignored.

Instead, it is possible to retarget between models with different body shapes, and position, rotation, and scale can be retargeted separately.

If `true`, retargeting is performed taking into account global pose.

In case the target skeleton has fewer bones than the source skeleton, the source bone parent's transform is taken into account. However, bone length between skeletons must match exactly, if not, the bones will be forced to expand or shrink.

This is useful for using dummy bone with length `0` to match postures when retargeting between models with different number of bones.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_position_enabled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RetargetModifier3D_method_is_position_enabled>`

Returns `true` if `enable<class_RetargetModifier3D_property_enable>` has `TRANSFORM_FLAG_POSITION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_rotation_enabled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RetargetModifier3D_method_is_rotation_enabled>`

Returns `true` if `enable<class_RetargetModifier3D_property_enable>` has `TRANSFORM_FLAG_ROTATION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_scale_enabled**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RetargetModifier3D_method_is_scale_enabled>`

Returns `true` if `enable<class_RetargetModifier3D_property_enable>` has `TRANSFORM_FLAG_SCALE<class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE>`.

classref-item-separator

classref-method

`void (No return value.)` **set_position_enabled**(enabled: `bool<class_bool>`) `🔗<class_RetargetModifier3D_method_set_position_enabled>`

Sets `TRANSFORM_FLAG_POSITION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION>` into `enable<class_RetargetModifier3D_property_enable>`.

classref-item-separator

classref-method

`void (No return value.)` **set_rotation_enabled**(enabled: `bool<class_bool>`) `🔗<class_RetargetModifier3D_method_set_rotation_enabled>`

Sets `TRANSFORM_FLAG_ROTATION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION>` into `enable<class_RetargetModifier3D_property_enable>`.

classref-item-separator

classref-method

`void (No return value.)` **set_scale_enabled**(enabled: `bool<class_bool>`) `🔗<class_RetargetModifier3D_method_set_scale_enabled>`

Sets `TRANSFORM_FLAG_SCALE<class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE>` into `enable<class_RetargetModifier3D_property_enable>`.