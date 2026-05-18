github_url
hide

# RDUniform

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Shader uniform (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **binding** = `0` `🔗<class_RDUniform_property_binding>`

classref-property-setget

- `void (No return value.)` **set_binding**(value: `int<class_int>`)
- `int<class_int>` **get_binding**()

The uniform's binding.

classref-item-separator

classref-property

`UniformType<enum_RenderingDevice_UniformType>` **uniform_type** = `3` `🔗<class_RDUniform_property_uniform_type>`

classref-property-setget

- `void (No return value.)` **set_uniform_type**(value: `UniformType<enum_RenderingDevice_UniformType>`)
- `UniformType<enum_RenderingDevice_UniformType>` **get_uniform_type**()

The uniform's data type.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_id**(id: `RID<class_RID>`) `🔗<class_RDUniform_method_add_id>`

Binds the given id to the uniform. The data associated with the id is then used when the uniform is passed to a shader.

classref-item-separator

classref-method

`void (No return value.)` **clear_ids**() `🔗<class_RDUniform_method_clear_ids>`

Unbinds all ids currently bound to the uniform.

classref-item-separator

classref-method

`Array<class_Array>`\[`RID<class_RID>`\] **get_ids**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RDUniform_method_get_ids>`

Returns an array of all ids currently bound to the uniform.