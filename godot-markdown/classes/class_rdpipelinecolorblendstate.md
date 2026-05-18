github_url
hide

# RDPipelineColorBlendState

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Pipeline color blend state (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

This object is used by `RenderingDevice<class_RenderingDevice>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Array<class_Array>`\[`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`\] **attachments** = `[]` `🔗<class_RDPipelineColorBlendState_property_attachments>`

classref-property-setget

- `void (No return value.)` **set_attachments**(value: `Array<class_Array>`\[`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`\])
- `Array<class_Array>`\[`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`\] **get_attachments**()

The attachments that are blended together.

classref-item-separator

classref-property

`Color<class_Color>` **blend_constant** = `Color(0, 0, 0, 1)` `🔗<class_RDPipelineColorBlendState_property_blend_constant>`

classref-property-setget

- `void (No return value.)` **set_blend_constant**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_blend_constant**()

The constant color to blend with. See also `RenderingDevice.draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>`.

classref-item-separator

classref-property

`bool<class_bool>` **enable_logic_op** = `false` `🔗<class_RDPipelineColorBlendState_property_enable_logic_op>`

classref-property-setget

- `void (No return value.)` **set_enable_logic_op**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_enable_logic_op**()

If `true`, performs the logic operation defined in `logic_op<class_RDPipelineColorBlendState_property_logic_op>`.

classref-item-separator

classref-property

`LogicOperation<enum_RenderingDevice_LogicOperation>` **logic_op** = `0` `🔗<class_RDPipelineColorBlendState_property_logic_op>`

classref-property-setget

- `void (No return value.)` **set_logic_op**(value: `LogicOperation<enum_RenderingDevice_LogicOperation>`)
- `LogicOperation<enum_RenderingDevice_LogicOperation>` **get_logic_op**()

The logic operation to perform for blending. Only effective if `enable_logic_op<class_RDPipelineColorBlendState_property_enable_logic_op>` is `true`.