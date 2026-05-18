github_url
hide

# OpenXRHand

**Deprecated:** Use `XRHandModifier3D<class_XRHandModifier3D>` instead.

**Inherits:** `Node3D<class_Node3D>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Node supporting hand and finger tracking in OpenXR.

classref-introduction-group

## Description

This node enables OpenXR's hand tracking functionality. The node should be a child node of an `XROrigin3D<class_XROrigin3D>` node, tracking will update its position to the player's tracked hand Palm joint location (the center of the middle finger's metacarpal bone). This node also updates the skeleton of a properly skinned hand or avatar model.

If the skeleton is a hand (one of the hand bones is the root node of the skeleton), then the skeleton will be placed relative to the hand palm location and the hand mesh and skeleton should be children of the OpenXRHand node.

If the hand bones are part of a full skeleton, then the root of the hand will keep its location with the assumption that IK is used to position the hand and arm.

By default the skeleton hand bones are repositioned to match the size of the tracked hand. To preserve the modeled bone sizes change `bone_update<class_OpenXRHand_property_bone_update>` to apply rotation only.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Hands**: `🔗<enum_OpenXRHand_Hands>`

classref-enumeration-constant

`Hands<enum_OpenXRHand_Hands>` **HAND_LEFT** = `0`

Tracking the player's left hand.

classref-enumeration-constant

`Hands<enum_OpenXRHand_Hands>` **HAND_RIGHT** = `1`

Tracking the player's right hand.

classref-enumeration-constant

`Hands<enum_OpenXRHand_Hands>` **HAND_MAX** = `2`

Maximum supported hands.

classref-item-separator

classref-enumeration

enum **MotionRange**: `🔗<enum_OpenXRHand_MotionRange>`

classref-enumeration-constant

`MotionRange<enum_OpenXRHand_MotionRange>` **MOTION_RANGE_UNOBSTRUCTED** = `0`

When player grips, hand skeleton will form a full fist.

classref-enumeration-constant

`MotionRange<enum_OpenXRHand_MotionRange>` **MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

When player grips, hand skeleton conforms to the controller the player is holding.

classref-enumeration-constant

`MotionRange<enum_OpenXRHand_MotionRange>` **MOTION_RANGE_MAX** = `2`

Maximum supported motion ranges.

classref-item-separator

classref-enumeration

enum **SkeletonRig**: `🔗<enum_OpenXRHand_SkeletonRig>`

classref-enumeration-constant

`SkeletonRig<enum_OpenXRHand_SkeletonRig>` **SKELETON_RIG_OPENXR** = `0`

An OpenXR compliant skeleton.

classref-enumeration-constant

`SkeletonRig<enum_OpenXRHand_SkeletonRig>` **SKELETON_RIG_HUMANOID** = `1`

A `SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>` compliant skeleton.

classref-enumeration-constant

`SkeletonRig<enum_OpenXRHand_SkeletonRig>` **SKELETON_RIG_MAX** = `2`

Maximum supported hands.

classref-item-separator

classref-enumeration

enum **BoneUpdate**: `🔗<enum_OpenXRHand_BoneUpdate>`

classref-enumeration-constant

`BoneUpdate<enum_OpenXRHand_BoneUpdate>` **BONE_UPDATE_FULL** = `0`

The skeletons bones are fully updated (both position and rotation) to match the tracked bones.

classref-enumeration-constant

`BoneUpdate<enum_OpenXRHand_BoneUpdate>` **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeletons bones are only rotated to align with the tracked bones, preserving bone length.

classref-enumeration-constant

`BoneUpdate<enum_OpenXRHand_BoneUpdate>` **BONE_UPDATE_MAX** = `2`

Maximum supported bone update mode.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BoneUpdate<enum_OpenXRHand_BoneUpdate>` **bone_update** = `0` `🔗<class_OpenXRHand_property_bone_update>`

classref-property-setget

- `void (No return value.)` **set_bone_update**(value: `BoneUpdate<enum_OpenXRHand_BoneUpdate>`)
- `BoneUpdate<enum_OpenXRHand_BoneUpdate>` **get_bone_update**()

Specify the type of updates to perform on the bone.

classref-item-separator

classref-property

`Hands<enum_OpenXRHand_Hands>` **hand** = `0` `🔗<class_OpenXRHand_property_hand>`

classref-property-setget

- `void (No return value.)` **set_hand**(value: `Hands<enum_OpenXRHand_Hands>`)
- `Hands<enum_OpenXRHand_Hands>` **get_hand**()

Specifies whether this node tracks the left or right hand of the player.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **hand_skeleton** = `NodePath("")` `🔗<class_OpenXRHand_property_hand_skeleton>`

classref-property-setget

- `void (No return value.)` **set_hand_skeleton**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_hand_skeleton**()

Set a `Skeleton3D<class_Skeleton3D>` node for which the pose positions will be updated.

classref-item-separator

classref-property

`MotionRange<enum_OpenXRHand_MotionRange>` **motion_range** = `0` `🔗<class_OpenXRHand_property_motion_range>`

classref-property-setget

- `void (No return value.)` **set_motion_range**(value: `MotionRange<enum_OpenXRHand_MotionRange>`)
- `MotionRange<enum_OpenXRHand_MotionRange>` **get_motion_range**()

Set the motion range (if supported) limiting the hand motion.

classref-item-separator

classref-property

`SkeletonRig<enum_OpenXRHand_SkeletonRig>` **skeleton_rig** = `0` `🔗<class_OpenXRHand_property_skeleton_rig>`

classref-property-setget

- `void (No return value.)` **set_skeleton_rig**(value: `SkeletonRig<enum_OpenXRHand_SkeletonRig>`)
- `SkeletonRig<enum_OpenXRHand_SkeletonRig>` **get_skeleton_rig**()

Set the type of skeleton rig the `hand_skeleton<class_OpenXRHand_property_hand_skeleton>` is compliant with.