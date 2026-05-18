github_url
hide

# RDPipelineColorBlendStateAttachment

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Pipeline color blend state attachment (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

Controls how blending between source and destination fragments is performed when using `RenderingDevice<class_RenderingDevice>`.

For reference, this is how common user-facing blend modes are implemented in Godot's 2D renderer:

**Mix:**

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA

**Add:**

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE

**Subtract:**

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
    attachment.color_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE

**Multiply:**

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_DST_COLOR
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_DST_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO

**Pre-multiplied alpha:**

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BlendOperation<enum_RenderingDevice_BlendOperation>` **alpha_blend_op** = `0` `🔗<class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op>`

classref-property-setget

- `void (No return value.)` **set_alpha_blend_op**(value: `BlendOperation<enum_RenderingDevice_BlendOperation>`)
- `BlendOperation<enum_RenderingDevice_BlendOperation>` **get_alpha_blend_op**()

The blend mode to use for the alpha channel.

classref-item-separator

classref-property

`BlendOperation<enum_RenderingDevice_BlendOperation>` **color_blend_op** = `0` `🔗<class_RDPipelineColorBlendStateAttachment_property_color_blend_op>`

classref-property-setget

- `void (No return value.)` **set_color_blend_op**(value: `BlendOperation<enum_RenderingDevice_BlendOperation>`)
- `BlendOperation<enum_RenderingDevice_BlendOperation>` **get_color_blend_op**()

The blend mode to use for the red/green/blue color channels.

classref-item-separator

classref-property

`BlendFactor<enum_RenderingDevice_BlendFactor>` **dst_alpha_blend_factor** = `0` `🔗<class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor>`

classref-property-setget

- `void (No return value.)` **set_dst_alpha_blend_factor**(value: `BlendFactor<enum_RenderingDevice_BlendFactor>`)
- `BlendFactor<enum_RenderingDevice_BlendFactor>` **get_dst_alpha_blend_factor**()

Controls how the blend factor for the alpha channel is determined based on the destination's fragments.

classref-item-separator

classref-property

`BlendFactor<enum_RenderingDevice_BlendFactor>` **dst_color_blend_factor** = `0` `🔗<class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor>`

classref-property-setget

- `void (No return value.)` **set_dst_color_blend_factor**(value: `BlendFactor<enum_RenderingDevice_BlendFactor>`)
- `BlendFactor<enum_RenderingDevice_BlendFactor>` **get_dst_color_blend_factor**()

Controls how the blend factor for the color channels is determined based on the destination's fragments.

classref-item-separator

classref-property

`bool<class_bool>` **enable_blend** = `false` `🔗<class_RDPipelineColorBlendStateAttachment_property_enable_blend>`

classref-property-setget

- `void (No return value.)` **set_enable_blend**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_enable_blend**()

If `true`, performs blending between the source and destination according to the factors defined in `src_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor>`, `dst_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor>`, `src_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor>` and `dst_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor>`. The blend modes `color_blend_op<class_RDPipelineColorBlendStateAttachment_property_color_blend_op>` and `alpha_blend_op<class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op>` are also taken into account, with `write_r<class_RDPipelineColorBlendStateAttachment_property_write_r>`, `write_g<class_RDPipelineColorBlendStateAttachment_property_write_g>`, `write_b<class_RDPipelineColorBlendStateAttachment_property_write_b>` and `write_a<class_RDPipelineColorBlendStateAttachment_property_write_a>` controlling the output.

classref-item-separator

classref-property

`BlendFactor<enum_RenderingDevice_BlendFactor>` **src_alpha_blend_factor** = `0` `🔗<class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor>`

classref-property-setget

- `void (No return value.)` **set_src_alpha_blend_factor**(value: `BlendFactor<enum_RenderingDevice_BlendFactor>`)
- `BlendFactor<enum_RenderingDevice_BlendFactor>` **get_src_alpha_blend_factor**()

Controls how the blend factor for the alpha channel is determined based on the source's fragments.

classref-item-separator

classref-property

`BlendFactor<enum_RenderingDevice_BlendFactor>` **src_color_blend_factor** = `0` `🔗<class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor>`

classref-property-setget

- `void (No return value.)` **set_src_color_blend_factor**(value: `BlendFactor<enum_RenderingDevice_BlendFactor>`)
- `BlendFactor<enum_RenderingDevice_BlendFactor>` **get_src_color_blend_factor**()

Controls how the blend factor for the color channels is determined based on the source's fragments.

classref-item-separator

classref-property

`bool<class_bool>` **write_a** = `true` `🔗<class_RDPipelineColorBlendStateAttachment_property_write_a>`

classref-property-setget

- `void (No return value.)` **set_write_a**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_write_a**()

If `true`, writes the new alpha channel to the final result.

classref-item-separator

classref-property

`bool<class_bool>` **write_b** = `true` `🔗<class_RDPipelineColorBlendStateAttachment_property_write_b>`

classref-property-setget

- `void (No return value.)` **set_write_b**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_write_b**()

If `true`, writes the new blue color channel to the final result.

classref-item-separator

classref-property

`bool<class_bool>` **write_g** = `true` `🔗<class_RDPipelineColorBlendStateAttachment_property_write_g>`

classref-property-setget

- `void (No return value.)` **set_write_g**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_write_g**()

If `true`, writes the new green color channel to the final result.

classref-item-separator

classref-property

`bool<class_bool>` **write_r** = `true` `🔗<class_RDPipelineColorBlendStateAttachment_property_write_r>`

classref-property-setget

- `void (No return value.)` **set_write_r**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_write_r**()

If `true`, writes the new red color channel to the final result.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **set_as_mix**() `🔗<class_RDPipelineColorBlendStateAttachment_method_set_as_mix>`

Convenience method to perform standard mix blending with straight (non-premultiplied) alpha. This sets `enable_blend<class_RDPipelineColorBlendStateAttachment_property_enable_blend>` to `true`, `src_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor>` to `RenderingDevice.BLEND_FACTOR_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA>`, `dst_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor>` to `RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA>`, `src_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor>` to `RenderingDevice.BLEND_FACTOR_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA>` and `dst_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor>` to `RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA>`.