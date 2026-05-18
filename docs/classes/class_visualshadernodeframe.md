github_url
hide

# VisualShaderNodeFrame

**Inherits:** `VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>` **\<** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `VisualShaderNodeComment<class_VisualShaderNodeComment>`

A frame other visual shader nodes can be attached to for better organization.

classref-introduction-group

## Description

A rectangular frame that can be used to group visual shader nodes together to improve organization.

Nodes attached to the frame will move with it when it is dragged and it can automatically resize to enclose all attached nodes.

Its title, description and color can be customized.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedInt32Array<class_PackedInt32Array>` **attached_nodes** = `PackedInt32Array()` `🔗<class_VisualShaderNodeFrame_property_attached_nodes>`

classref-property-setget

- `void (No return value.)` **set_attached_nodes**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_attached_nodes**()

The list of nodes attached to the frame.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-item-separator

classref-property

`bool<class_bool>` **autoshrink** = `true` `🔗<class_VisualShaderNodeFrame_property_autoshrink>`

classref-property-setget

- `void (No return value.)` **set_autoshrink_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_autoshrink_enabled**()

If `true`, the frame will automatically resize to enclose all attached nodes.

classref-item-separator

classref-property

`Color<class_Color>` **tint_color** = `Color(0.3, 0.3, 0.3, 0.75)` `🔗<class_VisualShaderNodeFrame_property_tint_color>`

classref-property-setget

- `void (No return value.)` **set_tint_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_tint_color**()

The color of the frame when `tint_color_enabled<class_VisualShaderNodeFrame_property_tint_color_enabled>` is `true`.

classref-item-separator

classref-property

`bool<class_bool>` **tint_color_enabled** = `false` `🔗<class_VisualShaderNodeFrame_property_tint_color_enabled>`

classref-property-setget

- `void (No return value.)` **set_tint_color_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_tint_color_enabled**()

If `true`, the frame will be tinted with the color specified in `tint_color<class_VisualShaderNodeFrame_property_tint_color>`.

classref-item-separator

classref-property

`String<class_String>` **title** = `"Title"` `🔗<class_VisualShaderNodeFrame_property_title>`

classref-property-setget

- `void (No return value.)` **set_title**(value: `String<class_String>`)
- `String<class_String>` **get_title**()

The title of the node.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_attached_node**(node: `int<class_int>`) `🔗<class_VisualShaderNodeFrame_method_add_attached_node>`

Adds a node to the list of nodes attached to the frame. Should not be called directly, use the `VisualShader.attach_node_to_frame()<class_VisualShader_method_attach_node_to_frame>` method instead.

classref-item-separator

classref-method

`void (No return value.)` **remove_attached_node**(node: `int<class_int>`) `🔗<class_VisualShaderNodeFrame_method_remove_attached_node>`

Removes a node from the list of nodes attached to the frame. Should not be called directly, use the `VisualShader.detach_node_from_frame()<class_VisualShader_method_detach_node_from_frame>` method instead.