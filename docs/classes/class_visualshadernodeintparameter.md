github_url
hide

# VisualShaderNodeIntParameter

**Inherits:** `VisualShaderNodeParameter<class_VisualShaderNodeParameter>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A visual shader node for shader parameter (uniform) of type `int<class_int>`.

classref-introduction-group

## Description

A `VisualShaderNodeParameter<class_VisualShaderNodeParameter>` of type `int<class_int>`. Offers additional customization for range of accepted values.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Hint**: `🔗<enum_VisualShaderNodeIntParameter_Hint>`

classref-enumeration-constant

`Hint<enum_VisualShaderNodeIntParameter_Hint>` **HINT_NONE** = `0`

The parameter will not constrain its value.

classref-enumeration-constant

`Hint<enum_VisualShaderNodeIntParameter_Hint>` **HINT_RANGE** = `1`

The parameter's value must be within the specified `min<class_VisualShaderNodeIntParameter_property_min>`/`max<class_VisualShaderNodeIntParameter_property_max>` range.

classref-enumeration-constant

`Hint<enum_VisualShaderNodeIntParameter_Hint>` **HINT_RANGE_STEP** = `2`

The parameter's value must be within the specified range, with the given `step<class_VisualShaderNodeIntParameter_property_step>` between values.

classref-enumeration-constant

`Hint<enum_VisualShaderNodeIntParameter_Hint>` **HINT_ENUM** = `3`

The parameter uses an enum to associate preset values to names in the editor.

classref-enumeration-constant

`Hint<enum_VisualShaderNodeIntParameter_Hint>` **HINT_MAX** = `4`

Represents the size of the `Hint<enum_VisualShaderNodeIntParameter_Hint>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **default_value** = `0` `🔗<class_VisualShaderNodeIntParameter_property_default_value>`

classref-property-setget

- `void (No return value.)` **set_default_value**(value: `int<class_int>`)
- `int<class_int>` **get_default_value**()

Default value of this parameter, which will be used if not set externally. `default_value_enabled<class_VisualShaderNodeIntParameter_property_default_value_enabled>` must be enabled; defaults to `0` otherwise.

classref-item-separator

classref-property

`bool<class_bool>` **default_value_enabled** = `false` `🔗<class_VisualShaderNodeIntParameter_property_default_value_enabled>`

classref-property-setget

- `void (No return value.)` **set_default_value_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_default_value_enabled**()

If `true`, the node will have a custom default value.

classref-item-separator

classref-property

`PackedStringArray<class_PackedStringArray>` **enum_names** = `PackedStringArray()` `🔗<class_VisualShaderNodeIntParameter_property_enum_names>`

classref-property-setget

- `void (No return value.)` **set_enum_names**(value: `PackedStringArray<class_PackedStringArray>`)
- `PackedStringArray<class_PackedStringArray>` **get_enum_names**()

The names used for the enum select in the editor. `hint<class_VisualShaderNodeIntParameter_property_hint>` must be `HINT_ENUM<class_VisualShaderNodeIntParameter_constant_HINT_ENUM>` for this to take effect.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedStringArray<class_PackedStringArray>` for more details.

classref-item-separator

classref-property

`Hint<enum_VisualShaderNodeIntParameter_Hint>` **hint** = `0` `🔗<class_VisualShaderNodeIntParameter_property_hint>`

classref-property-setget

- `void (No return value.)` **set_hint**(value: `Hint<enum_VisualShaderNodeIntParameter_Hint>`)
- `Hint<enum_VisualShaderNodeIntParameter_Hint>` **get_hint**()

Range hint of this node. Use it to customize valid parameter range.

classref-item-separator

classref-property

`int<class_int>` **max** = `100` `🔗<class_VisualShaderNodeIntParameter_property_max>`

classref-property-setget

- `void (No return value.)` **set_max**(value: `int<class_int>`)
- `int<class_int>` **get_max**()

The maximum value this parameter can take. `hint<class_VisualShaderNodeIntParameter_property_hint>` must be either `HINT_RANGE<class_VisualShaderNodeIntParameter_constant_HINT_RANGE>` or `HINT_RANGE_STEP<class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP>` for this to take effect.

classref-item-separator

classref-property

`int<class_int>` **min** = `0` `🔗<class_VisualShaderNodeIntParameter_property_min>`

classref-property-setget

- `void (No return value.)` **set_min**(value: `int<class_int>`)
- `int<class_int>` **get_min**()

The minimum value this parameter can take. `hint<class_VisualShaderNodeIntParameter_property_hint>` must be either `HINT_RANGE<class_VisualShaderNodeIntParameter_constant_HINT_RANGE>` or `HINT_RANGE_STEP<class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP>` for this to take effect.

classref-item-separator

classref-property

`int<class_int>` **step** = `1` `🔗<class_VisualShaderNodeIntParameter_property_step>`

classref-property-setget

- `void (No return value.)` **set_step**(value: `int<class_int>`)
- `int<class_int>` **get_step**()

The step between parameter's values. Forces the parameter to be a multiple of the given value. `hint<class_VisualShaderNodeIntParameter_property_hint>` must be `HINT_RANGE_STEP<class_VisualShaderNodeIntParameter_constant_HINT_RANGE_STEP>` for this to take effect.