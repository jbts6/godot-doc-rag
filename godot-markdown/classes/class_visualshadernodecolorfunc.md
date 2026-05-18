github_url
hide

# VisualShaderNodeColorFunc

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `Color<class_Color>` function to be used within the visual shader graph.

classref-introduction-group

## Description

Accept a `Color<class_Color>` to the input port and transform it according to `function<class_VisualShaderNodeColorFunc_property_function>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Function**: `🔗<enum_VisualShaderNodeColorFunc_Function>`

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_GRAYSCALE** = `0`

Converts the color to grayscale using the following formula:

    vec3 c = input;
    float max1 = max(c.r, c.g);
    float max2 = max(max1, c.b);
    float max3 = max(max1, max2);
    return vec3(max3, max3, max3);

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_HSV2RGB** = `1`

Converts HSV vector to RGB equivalent.

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_RGB2HSV** = `2`

Converts RGB vector to HSV equivalent.

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_SEPIA** = `3`

Applies sepia tone effect using the following formula:

    vec3 c = input;
    float r = (c.r * 0.393) + (c.g * 0.769) + (c.b * 0.189);
    float g = (c.r * 0.349) + (c.g * 0.686) + (c.b * 0.168);
    float b = (c.r * 0.272) + (c.g * 0.534) + (c.b * 0.131);
    return vec3(r, g, b);

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_LINEAR_TO_SRGB** = `4`

Converts color from linear encoding to nonlinear sRGB encoding using the following formula:

    const vec3 a = vec3(0.055f);
    return mix((vec3(1.0f) + a) * pow(c.rgb, vec3(1.0f / 2.4f)) - a, 12.92f * c.rgb, lessThan(c.rgb, vec3(0.0031308f)));

The Compatibility renderer uses a simpler formula that may produce undefined behavior with negative input values:

    vec3 c = input;
    return max(vec3(1.055) * pow(c, vec3(0.416666667)) - vec3(0.055), vec3(0.0));

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_SRGB_TO_LINEAR** = `5`

Converts color from nonlinear sRGB encoding to linear encoding using the following formula:

    vec3 c = input;
    return mix(pow((c.rgb + vec3(0.055)) * (1.0 / (1.0 + 0.055)), vec3(2.4)), c.rgb * (1.0 / 12.92), lessThan(c.rgb, vec3(0.04045)));

The Compatibility renderer uses a simpler formula that behaves poorly with negative input values:

    vec3 c = input;
    return c * (c * (c * 0.305306011 + 0.682171111) + 0.012522878);

classref-enumeration-constant

`Function<enum_VisualShaderNodeColorFunc_Function>` **FUNC_MAX** = `6`

Represents the size of the `Function<enum_VisualShaderNodeColorFunc_Function>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Function<enum_VisualShaderNodeColorFunc_Function>` **function** = `0` `🔗<class_VisualShaderNodeColorFunc_property_function>`

classref-property-setget

- `void (No return value.)` **set_function**(value: `Function<enum_VisualShaderNodeColorFunc_Function>`)
- `Function<enum_VisualShaderNodeColorFunc_Function>` **get_function**()

A function to be applied to the input color.