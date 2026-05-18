github_url
hide

# VisualShaderNodeColorParameter

**Inherits:** `VisualShaderNodeParameter<class_VisualShaderNodeParameter>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `Color<class_Color>` parameter to be used within the visual shader graph.

classref-introduction-group

## Description

Translated to `uniform vec4` in the shader language.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Color<class_Color>` **default_value** = `Color(1, 1, 1, 1)` `🔗<class_VisualShaderNodeColorParameter_property_default_value>`

classref-property-setget

- `void (No return value.)` **set_default_value**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_default_value**()

A default value to be assigned within the shader.

classref-item-separator

classref-property

`bool<class_bool>` **default_value_enabled** = `false` `🔗<class_VisualShaderNodeColorParameter_property_default_value_enabled>`

classref-property-setget

- `void (No return value.)` **set_default_value_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_default_value_enabled**()

Enables usage of the `default_value<class_VisualShaderNodeColorParameter_property_default_value>`.