github_url
hide

# VisualShaderNodeColorOp

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `Color<class_Color>` operator to be used within the visual shader graph.

classref-introduction-group

## Description

Applies `operator<class_VisualShaderNodeColorOp_property_operator>` to two color inputs.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Operator**: `🔗<enum_VisualShaderNodeColorOp_Operator>`

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_SCREEN** = `0`

Produce a screen effect with the following formula:

    result = vec3(1.0) - (vec3(1.0) - a) * (vec3(1.0) - b);

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_DIFFERENCE** = `1`

Produce a difference effect with the following formula:

    result = abs(a - b);

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_DARKEN** = `2`

Produce a darken effect with the following formula:

    result = min(a, b);

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_LIGHTEN** = `3`

Produce a lighten effect with the following formula:

    result = max(a, b);

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_OVERLAY** = `4`

Produce an overlay effect with the following formula:

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = 2.0 * base * blend;
        } else {
            result[i] = 1.0 - 2.0 * (1.0 - blend) * (1.0 - base);
        }
    }

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_DODGE** = `5`

Produce a dodge effect with the following formula:

    result = a / (vec3(1.0) - b);

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_BURN** = `6`

Produce a burn effect with the following formula:

    result = vec3(1.0) - (vec3(1.0) - a) / b;

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_SOFT_LIGHT** = `7`

Produce a soft light effect with the following formula:

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = base * (blend + 0.5);
        } else {
            result[i] = 1.0 - (1.0 - base) * (1.0 - (blend - 0.5));
        }
    }

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_HARD_LIGHT** = `8`

Produce a hard light effect with the following formula:

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = base * (2.0 * blend);
        } else {
            result[i] = 1.0 - (1.0 - base) * (1.0 - 2.0 * (blend - 0.5));
        }
    }

classref-enumeration-constant

`Operator<enum_VisualShaderNodeColorOp_Operator>` **OP_MAX** = `9`

Represents the size of the `Operator<enum_VisualShaderNodeColorOp_Operator>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Operator<enum_VisualShaderNodeColorOp_Operator>` **operator** = `0` `🔗<class_VisualShaderNodeColorOp_property_operator>`

classref-property-setget

- `void (No return value.)` **set_operator**(value: `Operator<enum_VisualShaderNodeColorOp_Operator>`)
- `Operator<enum_VisualShaderNodeColorOp_Operator>` **get_operator**()

An operator to be applied to the inputs.