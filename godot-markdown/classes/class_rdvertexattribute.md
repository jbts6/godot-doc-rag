github_url
hide

# RDVertexAttribute

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Vertex attribute (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **binding** = `4294967295` `🔗<class_RDVertexAttribute_property_binding>`

classref-property-setget

- `void (No return value.)` **set_binding**(value: `int<class_int>`)
- `int<class_int>` **get_binding**()

The index of the buffer in the vertex buffer array to bind this vertex attribute. When set to `-1`, it defaults to the index of the attribute.

**Note:** You cannot mix binding explicitly assigned attributes with implicitly assigned ones (i.e. `-1`). Either all attributes must have their binding set to `-1`, or all must have explicit bindings.

classref-item-separator

classref-property

`DataFormat<enum_RenderingDevice_DataFormat>` **format** = `232` `🔗<class_RDVertexAttribute_property_format>`

classref-property-setget

- `void (No return value.)` **set_format**(value: `DataFormat<enum_RenderingDevice_DataFormat>`)
- `DataFormat<enum_RenderingDevice_DataFormat>` **get_format**()

The way that this attribute's data is interpreted when sent to a shader.

classref-item-separator

classref-property

`VertexFrequency<enum_RenderingDevice_VertexFrequency>` **frequency** = `0` `🔗<class_RDVertexAttribute_property_frequency>`

classref-property-setget

- `void (No return value.)` **set_frequency**(value: `VertexFrequency<enum_RenderingDevice_VertexFrequency>`)
- `VertexFrequency<enum_RenderingDevice_VertexFrequency>` **get_frequency**()

The rate at which this attribute is pulled from its vertex buffer.

classref-item-separator

classref-property

`int<class_int>` **location** = `0` `🔗<class_RDVertexAttribute_property_location>`

classref-property-setget

- `void (No return value.)` **set_location**(value: `int<class_int>`)
- `int<class_int>` **get_location**()

The location in the shader that this attribute is bound to.

classref-item-separator

classref-property

`int<class_int>` **offset** = `0` `🔗<class_RDVertexAttribute_property_offset>`

classref-property-setget

- `void (No return value.)` **set_offset**(value: `int<class_int>`)
- `int<class_int>` **get_offset**()

The number of bytes between the start of the vertex buffer and the first instance of this attribute.

classref-item-separator

classref-property

`int<class_int>` **stride** = `0` `🔗<class_RDVertexAttribute_property_stride>`

classref-property-setget

- `void (No return value.)` **set_stride**(value: `int<class_int>`)
- `int<class_int>` **get_stride**()

The number of bytes between the starts of consecutive instances of this attribute.