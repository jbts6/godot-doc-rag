github_url
hide

# XRBodyModifier3D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `SkeletonModifier3D<class_SkeletonModifier3D>` **\<** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A node for driving body meshes from `XRBodyTracker<class_XRBodyTracker>` data.

classref-introduction-group

## Description

This node uses body tracking data from an `XRBodyTracker<class_XRBodyTracker>` to pose the skeleton of a body mesh.

Positioning of the body is performed by creating an `XRNode3D<class_XRNode3D>` ancestor of the body mesh driven by the same `XRBodyTracker<class_XRBodyTracker>`.

The body tracking position-data is scaled by `Skeleton3D.motion_scale<class_Skeleton3D_property_motion_scale>` when applied to the skeleton, which can be used to adjust the tracked body to match the scale of the body model.

classref-introduction-group

## Tutorials

- `XR documentation index <../tutorials/xr/index>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

flags **BodyUpdate**: `🔗<enum_XRBodyModifier3D_BodyUpdate>`

classref-enumeration-constant

`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>` **BODY_UPDATE_UPPER_BODY** = `1`

The skeleton's upper body joints are updated.

classref-enumeration-constant

`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>` **BODY_UPDATE_LOWER_BODY** = `2`

The skeleton's lower body joints are updated.

classref-enumeration-constant

`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>` **BODY_UPDATE_HANDS** = `4`

The skeleton's hand joints are updated.

classref-item-separator

classref-enumeration

enum **BoneUpdate**: `🔗<enum_XRBodyModifier3D_BoneUpdate>`

classref-enumeration-constant

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>` **BONE_UPDATE_FULL** = `0`

The skeleton's bones are fully updated (both position and rotation) to match the tracked bones.

classref-enumeration-constant

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>` **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton's bones are only rotated to align with the tracked bones, preserving bone length.

classref-enumeration-constant

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>` **BONE_UPDATE_MAX** = `2`

Represents the size of the `BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`StringName<class_StringName>` **body_tracker** = `&"/user/body_tracker"` `🔗<class_XRBodyModifier3D_property_body_tracker>`

classref-property-setget

- `void (No return value.)` **set_body_tracker**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_body_tracker**()

The name of the `XRBodyTracker<class_XRBodyTracker>` registered with `XRServer<class_XRServer>` to obtain the body tracking data from.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`\] **body_update** = `7` `🔗<class_XRBodyModifier3D_property_body_update>`

classref-property-setget

- `void (No return value.)` **set_body_update**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`\] **get_body_update**()

Specifies the body parts to update.

classref-item-separator

classref-property

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>` **bone_update** = `0` `🔗<class_XRBodyModifier3D_property_bone_update>`

classref-property-setget

- `void (No return value.)` **set_bone_update**(value: `BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`)
- `BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>` **get_bone_update**()

Specifies the type of updates to perform on the bones.