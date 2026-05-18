github_url
hide

# VisualShaderNodeTransformParameter

**Inherits:** `VisualShaderNodeParameter<class_VisualShaderNodeParameter>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `Transform3D<class_Transform3D>` parameter for use within the visual shader graph.

classref-introduction-group

## Description

Translated to `uniform mat4` in the shader language.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Transform3D<class_Transform3D>` **default_value** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)` `🔗<class_VisualShaderNodeTransformParameter_property_default_value>`

classref-property-setget

- `void (No return value.)` **set_default_value**(value: `Transform3D<class_Transform3D>`)
- `Transform3D<class_Transform3D>` **get_default_value**()

A default value to be assigned within the shader.

classref-item-separator

classref-property

`bool<class_bool>` **default_value_enabled** = `false` `🔗<class_VisualShaderNodeTransformParameter_property_default_value_enabled>`

classref-property-setget

- `void (No return value.)` **set_default_value_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_default_value_enabled**()

Enables usage of the `default_value<class_VisualShaderNodeTransformParameter_property_default_value>`.