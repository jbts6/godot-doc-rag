github_url
hide

# CopyTransformModifier3D

**Inherits:** `BoneConstraint3D<class_BoneConstraint3D>` **\<** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A `SkeletonModifier3D<class_SkeletonModifier3D>` that apply transform to the bone which copied from reference.

classref-introduction-group

## Description

Apply the copied transform of the bone set by `BoneConstraint3D.set_reference_bone()<class_BoneConstraint3D_method_set_reference_bone>` to the bone set by `BoneConstraint3D.set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>` with processing it with some masks and options.

There are 4 ways to apply the transform, depending on the combination of `set_relative()<class_CopyTransformModifier3D_method_set_relative>` and `set_additive()<class_CopyTransformModifier3D_method_set_additive>`.

**Relative + Additive:**

- Extract reference pose relative to the rest and add it to the apply bone's pose.

**Relative + Not Additive:**

- Extract reference pose relative to the rest and add it to the apply bone's rest.

**Not Relative + Additive:**

- Extract reference pose absolutely and add it to the apply bone's pose.

**Not Relative + Not Additive:**

- Extract reference pose absolutely and the apply bone's pose is replaced with it.

**Note:** Relative option is available only in the case `BoneConstraint3D.get_reference_type()<class_BoneConstraint3D_method_get_reference_type>` is `BoneConstraint3D.REFERENCE_TYPE_BONE<class_BoneConstraint3D_constant_REFERENCE_TYPE_BONE>`. See also `ReferenceType<enum_BoneConstraint3D_ReferenceType>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

flags **TransformFlag**: `🔗<enum_CopyTransformModifier3D_TransformFlag>`

classref-enumeration-constant

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>` **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to copy the position.

classref-enumeration-constant

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>` **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to copy the rotation.

classref-enumeration-constant

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>` **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to copy the scale.

classref-enumeration-constant

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>` **TRANSFORM_FLAG_ALL** = `7`

If set, allows to copy the position/rotation/scale.

classref-item-separator

classref-enumeration

flags **AxisFlag**: `🔗<enum_CopyTransformModifier3D_AxisFlag>`

classref-enumeration-constant

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>` **AXIS_FLAG_X** = `1`

If set, allows to process the X-axis.

classref-enumeration-constant

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>` **AXIS_FLAG_Y** = `2`

If set, allows to process the Y-axis.

classref-enumeration-constant

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>` **AXIS_FLAG_Z** = `4`

If set, allows to process the Z-axis.

classref-enumeration-constant

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>` **AXIS_FLAG_ALL** = `7`

If set, allows to process the all axes.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **setting_count** = `0` `🔗<class_CopyTransformModifier3D_property_setting_count>`

classref-property-setget

- `void (No return value.)` **set_setting_count**(value: `int<class_int>`)
- `int<class_int>` **get_setting_count**()

The number of settings in the modifier.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`\] **get_axis_flags**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_get_axis_flags>`

Returns the axis flags of the setting at `index`.

classref-item-separator

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`\] **get_copy_flags**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_get_copy_flags>`

Returns the copy flags of the setting at `index`.

classref-item-separator

classref-method

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`\] **get_invert_flags**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_get_invert_flags>`

Returns the invert flags of the setting at `index`.

classref-item-separator

classref-method

`bool<class_bool>` **is_additive**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_additive>`

Returns `true` if the additive option is enabled in the setting at `index`.

classref-item-separator

classref-method

`bool<class_bool>` **is_axis_x_enabled**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_axis_x_enabled>`

Returns `true` if the enable flags has the flag for the X-axis in the setting at `index`. See also `set_axis_flags()<class_CopyTransformModifier3D_method_set_axis_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_axis_x_inverted**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_axis_x_inverted>`

Returns `true` if the invert flags has the flag for the X-axis in the setting at `index`. See also `set_invert_flags()<class_CopyTransformModifier3D_method_set_invert_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_axis_y_enabled**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_axis_y_enabled>`

Returns `true` if the enable flags has the flag for the Y-axis in the setting at `index`. See also `set_axis_flags()<class_CopyTransformModifier3D_method_set_axis_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_axis_y_inverted**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_axis_y_inverted>`

Returns `true` if the invert flags has the flag for the Y-axis in the setting at `index`. See also `set_invert_flags()<class_CopyTransformModifier3D_method_set_invert_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_axis_z_enabled**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_axis_z_enabled>`

Returns `true` if the enable flags has the flag for the Z-axis in the setting at `index`. See also `set_axis_flags()<class_CopyTransformModifier3D_method_set_axis_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_axis_z_inverted**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_axis_z_inverted>`

Returns `true` if the invert flags has the flag for the Z-axis in the setting at `index`. See also `set_invert_flags()<class_CopyTransformModifier3D_method_set_invert_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_position_copying**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_position_copying>`

Returns `true` if the copy flags has the flag for the position in the setting at `index`. See also `set_copy_flags()<class_CopyTransformModifier3D_method_set_copy_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_relative**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_relative>`

Returns `true` if the relative option is enabled in the setting at `index`.

classref-item-separator

classref-method

`bool<class_bool>` **is_rotation_copying**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_rotation_copying>`

Returns `true` if the copy flags has the flag for the rotation in the setting at `index`. See also `set_copy_flags()<class_CopyTransformModifier3D_method_set_copy_flags>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_scale_copying**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CopyTransformModifier3D_method_is_scale_copying>`

Returns `true` if the copy flags has the flag for the scale in the setting at `index`. See also `set_copy_flags()<class_CopyTransformModifier3D_method_set_copy_flags>`.

classref-item-separator

classref-method

`void (No return value.)` **set_additive**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_additive>`

Sets additive option in the setting at `index` to `enabled`. This mainly affects the process of applying transform to the `BoneConstraint3D.set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>`.

If sets `enabled` to `true`, the processed transform is added to the pose of the current apply bone.

If sets `enabled` to `false`, the pose of the current apply bone is replaced with the processed transform. However, if set `set_relative()<class_CopyTransformModifier3D_method_set_relative>` to `true`, the transform is relative to rest.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_flags**(index: `int<class_int>`, axis_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`\]) `🔗<class_CopyTransformModifier3D_method_set_axis_flags>`

Sets the flags to copy axes. If the flag is valid, the axis is copied.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_x_enabled**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_axis_x_enabled>`

If sets `enabled` to `true`, the X-axis will be copied.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_x_inverted**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_axis_x_inverted>`

If sets `enabled` to `true`, the X-axis will be inverted.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_y_enabled**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_axis_y_enabled>`

If sets `enabled` to `true`, the Y-axis will be copied.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_y_inverted**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_axis_y_inverted>`

If sets `enabled` to `true`, the Y-axis will be inverted.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_z_enabled**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_axis_z_enabled>`

If sets `enabled` to `true`, the Z-axis will be copied.

classref-item-separator

classref-method

`void (No return value.)` **set_axis_z_inverted**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_axis_z_inverted>`

If sets `enabled` to `true`, the Z-axis will be inverted.

classref-item-separator

classref-method

`void (No return value.)` **set_copy_flags**(index: `int<class_int>`, copy_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`\]) `🔗<class_CopyTransformModifier3D_method_set_copy_flags>`

Sets the flags to process the transform operations. If the flag is valid, the transform operation is processed.

**Note:** If the rotation is valid for only one axis, it respects the roll of the valid axis. If the rotation is valid for two axes, it discards the roll of the invalid axis.

classref-item-separator

classref-method

`void (No return value.)` **set_copy_position**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_copy_position>`

If sets `enabled` to `true`, the position will be copied.

classref-item-separator

classref-method

`void (No return value.)` **set_copy_rotation**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_copy_rotation>`

If sets `enabled` to `true`, the rotation will be copied.

classref-item-separator

classref-method

`void (No return value.)` **set_copy_scale**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_copy_scale>`

If sets `enabled` to `true`, the scale will be copied.

classref-item-separator

classref-method

`void (No return value.)` **set_invert_flags**(index: `int<class_int>`, axis_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`\]) `🔗<class_CopyTransformModifier3D_method_set_invert_flags>`

Sets the flags to inverte axes. If the flag is valid, the axis is copied.

**Note:** An inverted scale means an inverse number, not a negative scale. For example, inverting `2.0` means `0.5`.

**Note:** An inverted rotation flips the elements of the quaternion. For example, a two-axis inversion will flip the roll of each axis, and a three-axis inversion will flip the final orientation. However, be aware that flipping only one axis may cause unintended rotation by the unflipped axes, due to the characteristics of the quaternion.

classref-item-separator

classref-method

`void (No return value.)` **set_relative**(index: `int<class_int>`, enabled: `bool<class_bool>`) `🔗<class_CopyTransformModifier3D_method_set_relative>`

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the extracted and applying transform is relative to the rest.

If sets `enabled` to `false`, the extracted transform is absolute.