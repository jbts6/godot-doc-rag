github_url
hide

# SkeletonProfileHumanoid

**Inherits:** `SkeletonProfile<class_SkeletonProfile>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A humanoid `SkeletonProfile<class_SkeletonProfile>` preset.

classref-introduction-group

## Description

A `SkeletonProfile<class_SkeletonProfile>` as a preset that is optimized for the human form. This exists for standardization, so all parameters are read-only.

A humanoid skeleton profile contains 56 bones divided into 4 groups: `"Body"`, `"Face"`, `"LeftHand"`, and `"RightHand"`. It is structured as follows:

``` text
Root
└─ Hips
    ├─ LeftUpperLeg
    │  └─ LeftLowerLeg
    │     └─ LeftFoot
    │        └─ LeftToes
    ├─ RightUpperLeg
    │  └─ RightLowerLeg
    │     └─ RightFoot
    │        └─ RightToes
    └─ Spine
        └─ Chest
            └─ UpperChest
                ├─ Neck
                │   └─ Head
                │       ├─ Jaw
                │       ├─ LeftEye
                │       └─ RightEye
                ├─ LeftShoulder
                │  └─ LeftUpperArm
                │     └─ LeftLowerArm
                │        └─ LeftHand
                │           ├─ LeftThumbMetacarpal
                │           │  └─ LeftThumbProximal
                │           │    └─ LeftThumbDistal
                │           ├─ LeftIndexProximal
                │           │  └─ LeftIndexIntermediate
                │           │    └─ LeftIndexDistal
                │           ├─ LeftMiddleProximal
                │           │  └─ LeftMiddleIntermediate
                │           │    └─ LeftMiddleDistal
                │           ├─ LeftRingProximal
                │           │  └─ LeftRingIntermediate
                │           │    └─ LeftRingDistal
                │           └─ LeftLittleProximal
                │              └─ LeftLittleIntermediate
                │                └─ LeftLittleDistal
                └─ RightShoulder
                   └─ RightUpperArm
                      └─ RightLowerArm
                         └─ RightHand
                            ├─ RightThumbMetacarpal
                            │  └─ RightThumbProximal
                            │     └─ RightThumbDistal
                            ├─ RightIndexProximal
                            │  └─ RightIndexIntermediate
                            │     └─ RightIndexDistal
                            ├─ RightMiddleProximal
                            │  └─ RightMiddleIntermediate
                            │     └─ RightMiddleDistal
                            ├─ RightRingProximal
                            │  └─ RightRingIntermediate
                            │     └─ RightRingDistal
                            └─ RightLittleProximal
                               └─ RightLittleIntermediate
                                 └─ RightLittleDistal
```

classref-introduction-group

## Tutorials

- `Retargeting 3D Skeletons <../tutorials/assets_pipeline/retargeting_3d_skeletons>`

classref-reftable-group

## Properties