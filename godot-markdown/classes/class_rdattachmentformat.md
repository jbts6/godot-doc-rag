github_url
hide

# RDAttachmentFormat

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Attachment format (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`DataFormat<enum_RenderingDevice_DataFormat>` **format** = `36` `🔗<class_RDAttachmentFormat_property_format>`

classref-property-setget

- `void (No return value.)` **set_format**(value: `DataFormat<enum_RenderingDevice_DataFormat>`)
- `DataFormat<enum_RenderingDevice_DataFormat>` **get_format**()

The attachment's data format.

classref-item-separator

classref-property

`TextureSamples<enum_RenderingDevice_TextureSamples>` **samples** = `0` `🔗<class_RDAttachmentFormat_property_samples>`

classref-property-setget

- `void (No return value.)` **set_samples**(value: `TextureSamples<enum_RenderingDevice_TextureSamples>`)
- `TextureSamples<enum_RenderingDevice_TextureSamples>` **get_samples**()

The number of samples used when sampling the attachment.

classref-item-separator

classref-property

`int<class_int>` **usage_flags** = `0` `🔗<class_RDAttachmentFormat_property_usage_flags>`

classref-property-setget

- `void (No return value.)` **set_usage_flags**(value: `int<class_int>`)
- `int<class_int>` **get_usage_flags**()

The attachment's usage flags, which determine what can be done with it.