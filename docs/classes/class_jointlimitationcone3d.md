github_url
hide

# JointLimitationCone3D

**Inherits:** `JointLimitation3D<class_JointLimitation3D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A cone shape limitation that interacts with `ChainIK3D<class_ChainIK3D>`.

classref-introduction-group

## Description

A cone shape limitation that interacts with `ChainIK3D<class_ChainIK3D>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **angle** = `1.5707964` `🔗<class_JointLimitationCone3D_property_angle>`

classref-property-setget

- `void (No return value.)` **set_angle**(value: `float<class_float>`)
- `float<class_float>` **get_angle**()

The radius range of the hole made by the cone.

`0` degrees makes a sphere without hole, `180` degrees makes a hemisphere, and `360` degrees become empty (no limitation).