github_url
hide

# RDFramebufferPass

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Framebuffer pass attachment description (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This class contains the list of attachment descriptions for a framebuffer pass. Each points with an index to a previously supplied list of texture attachments.

Multipass framebuffers can optimize some configurations in mobile. On desktop, they provide little to no advantage.

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**ATTACHMENT_UNUSED** = `-1` `🔗<class_RDFramebufferPass_constant_ATTACHMENT_UNUSED>`

Attachment is unused.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedInt32Array<class_PackedInt32Array>` **color_attachments** = `PackedInt32Array()` `🔗<class_RDFramebufferPass_property_color_attachments>`

classref-property-setget

- `void (No return value.)` **set_color_attachments**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_color_attachments**()

Color attachments in order starting from 0. If this attachment is not used by the shader, pass ATTACHMENT_UNUSED to skip.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-item-separator

classref-property

`int<class_int>` **depth_attachment** = `-1` `🔗<class_RDFramebufferPass_property_depth_attachment>`

classref-property-setget

- `void (No return value.)` **set_depth_attachment**(value: `int<class_int>`)
- `int<class_int>` **get_depth_attachment**()

Depth attachment. ATTACHMENT_UNUSED should be used if no depth buffer is required for this pass.

classref-item-separator

classref-property

`PackedInt32Array<class_PackedInt32Array>` **input_attachments** = `PackedInt32Array()` `🔗<class_RDFramebufferPass_property_input_attachments>`

classref-property-setget

- `void (No return value.)` **set_input_attachments**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_input_attachments**()

Used for multipass framebuffers (more than one render pass). Converts an attachment to an input. Make sure to also supply it properly in the `RDUniform<class_RDUniform>` for the uniform set.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-item-separator

classref-property

`PackedInt32Array<class_PackedInt32Array>` **preserve_attachments** = `PackedInt32Array()` `🔗<class_RDFramebufferPass_property_preserve_attachments>`

classref-property-setget

- `void (No return value.)` **set_preserve_attachments**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_preserve_attachments**()

Attachments to preserve in this pass (otherwise they are erased).

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-item-separator

classref-property

`PackedInt32Array<class_PackedInt32Array>` **resolve_attachments** = `PackedInt32Array()` `🔗<class_RDFramebufferPass_property_resolve_attachments>`

classref-property-setget

- `void (No return value.)` **set_resolve_attachments**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_resolve_attachments**()

If the color attachments are multisampled, non-multisampled resolve attachments can be provided.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.