github_url
hide

# VisualShaderNodeVarying

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `VisualShaderNodeVaryingGetter<class_VisualShaderNodeVaryingGetter>`, `VisualShaderNodeVaryingSetter<class_VisualShaderNodeVaryingSetter>`

A visual shader node that represents a "varying" shader value.

classref-introduction-group

## Description

Varying values are shader variables that can be passed between shader functions, e.g. from Vertex shader to Fragment shader.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **varying_name** = `"[None]"` `🔗<class_VisualShaderNodeVarying_property_varying_name>`

classref-property-setget

- `void (No return value.)` **set_varying_name**(value: `String<class_String>`)
- `String<class_String>` **get_varying_name**()

Name of the variable. Must be unique.

classref-item-separator

classref-property

`VaryingType<enum_VisualShader_VaryingType>` **varying_type** = `0` `🔗<class_VisualShaderNodeVarying_property_varying_type>`

classref-property-setget

- `void (No return value.)` **set_varying_type**(value: `VaryingType<enum_VisualShader_VaryingType>`)
- `VaryingType<enum_VisualShader_VaryingType>` **get_varying_type**()

Type of the variable. Determines where the variable can be accessed.