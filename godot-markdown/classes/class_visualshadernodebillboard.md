github_url
hide

# VisualShaderNodeBillboard

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A node that controls how the object faces the camera to be used within the visual shader graph.

classref-introduction-group

## Description

The output port of this node needs to be connected to `Model View Matrix` port of `VisualShaderNodeOutput<class_VisualShaderNodeOutput>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **BillboardType**: `🔗<enum_VisualShaderNodeBillboard_BillboardType>`

classref-enumeration-constant

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **BILLBOARD_TYPE_DISABLED** = `0`

Billboarding is disabled and the node does nothing.

classref-enumeration-constant

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **BILLBOARD_TYPE_ENABLED** = `1`

A standard billboarding algorithm is enabled.

classref-enumeration-constant

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **BILLBOARD_TYPE_FIXED_Y** = `2`

A billboarding algorithm to rotate around Y-axis is enabled.

classref-enumeration-constant

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **BILLBOARD_TYPE_PARTICLES** = `3`

A billboarding algorithm designed to use on particles is enabled.

classref-enumeration-constant

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **BILLBOARD_TYPE_MAX** = `4`

Represents the size of the `BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **billboard_type** = `1` `🔗<class_VisualShaderNodeBillboard_property_billboard_type>`

classref-property-setget

- `void (No return value.)` **set_billboard_type**(value: `BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`)
- `BillboardType<enum_VisualShaderNodeBillboard_BillboardType>` **get_billboard_type**()

Controls how the object faces the camera.

classref-item-separator

classref-property

`bool<class_bool>` **keep_scale** = `false` `🔗<class_VisualShaderNodeBillboard_property_keep_scale>`

classref-property-setget

- `void (No return value.)` **set_keep_scale_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_keep_scale_enabled**()

If `true`, the shader will keep the scale set for the mesh. Otherwise, the scale is lost when billboarding.