github_url
hide

# TextMesh

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>` **\<** `Mesh<class_Mesh>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Generate a `PrimitiveMesh<class_PrimitiveMesh>` from the text.

classref-introduction-group

## Description

Generate a `PrimitiveMesh<class_PrimitiveMesh>` from the text.

TextMesh can be generated only when using dynamic fonts with vector glyph contours. Bitmap fonts (including bitmap data in the TrueType/OpenType containers, like color emoji fonts) are not supported.

The UV layout is arranged in 4 horizontal strips, top to bottom: 40% of the height for the front face, 40% for the back face, 10% for the outer edges and 10% for the inner edges.

classref-introduction-group

## Tutorials

- `3D text <../tutorials/3d/3d_text>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`AutowrapMode<enum_TextServer_AutowrapMode>` **autowrap_mode** = `0` `🔗<class_TextMesh_property_autowrap_mode>`

classref-property-setget

- `void (No return value.)` **set_autowrap_mode**(value: `AutowrapMode<enum_TextServer_AutowrapMode>`)
- `AutowrapMode<enum_TextServer_AutowrapMode>` **get_autowrap_mode**()

If set to something other than `TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`, the text gets wrapped inside the node's bounding rectangle. If you resize the node, it will change its height automatically to show all the text.

classref-item-separator

classref-property

`float<class_float>` **curve_step** = `0.5` `🔗<class_TextMesh_property_curve_step>`

classref-property-setget

- `void (No return value.)` **set_curve_step**(value: `float<class_float>`)
- `float<class_float>` **get_curve_step**()

Step (in pixels) used to approximate Bézier curves. Lower values result in smoother curves, but is slower to generate and render. Consider adjusting this according to the font size and the typical viewing distance.

**Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts.

classref-item-separator

classref-property

`float<class_float>` **depth** = `0.05` `🔗<class_TextMesh_property_depth>`

classref-property-setget

- `void (No return value.)` **set_depth**(value: `float<class_float>`)
- `float<class_float>` **get_depth**()

Depths of the mesh, if set to `0.0` only front surface, is generated, and UV layout is changed to use full texture for the front face only.

classref-item-separator

classref-property

`Font<class_Font>` **font** `🔗<class_TextMesh_property_font>`

classref-property-setget

- `void (No return value.)` **set_font**(value: `Font<class_Font>`)
- `Font<class_Font>` **get_font**()

Font configuration used to display text.

classref-item-separator

classref-property

`int<class_int>` **font_size** = `16` `🔗<class_TextMesh_property_font_size>`

classref-property-setget

- `void (No return value.)` **set_font_size**(value: `int<class_int>`)
- `int<class_int>` **get_font_size**()

Font size of the **TextMesh**'s text. This property works in tandem with `pixel_size<class_TextMesh_property_pixel_size>`. Higher values will result in a more detailed font, regardless of `curve_step<class_TextMesh_property_curve_step>` and `pixel_size<class_TextMesh_property_pixel_size>`. Consider keeping this value below 63 (inclusive) for good performance, and adjust `pixel_size<class_TextMesh_property_pixel_size>` as needed to enlarge text.

**Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's `Node3D.scale<class_Node3D_property_scale>` instead.

classref-item-separator

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **horizontal_alignment** = `1` `🔗<class_TextMesh_property_horizontal_alignment>`

classref-property-setget

- `void (No return value.)` **set_horizontal_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_horizontal_alignment**()

Controls the text's horizontal alignment. Supports left, center, right, and fill (also known as justify).

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **justification_flags** = `163` `🔗<class_TextMesh_property_justification_flags>`

classref-property-setget

- `void (No return value.)` **set_justification_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`JustificationFlag<enum_TextServer_JustificationFlag>`\] **get_justification_flags**()

Line fill alignment rules.

classref-item-separator

classref-property

`String<class_String>` **language** = `""` `🔗<class_TextMesh_property_language>`

classref-property-setget

- `void (No return value.)` **set_language**(value: `String<class_String>`)
- `String<class_String>` **get_language**()

Language code used for line-breaking and text shaping algorithms. If left empty, the current locale is used instead.

classref-item-separator

classref-property

`float<class_float>` **line_spacing** = `0.0` `🔗<class_TextMesh_property_line_spacing>`

classref-property-setget

- `void (No return value.)` **set_line_spacing**(value: `float<class_float>`)
- `float<class_float>` **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added to line descent. This value can be negative.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **offset** = `Vector2(0, 0)` `🔗<class_TextMesh_property_offset>`

classref-property-setget

- `void (No return value.)` **set_offset**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_offset**()

The text drawing offset (in pixels).

**Note:** Changing this property will regenerate the mesh, which is a slow operation. To change the text's position in real-time efficiently, change the node's `Node3D.position<class_Node3D_property_position>` instead.

classref-item-separator

classref-property

`float<class_float>` **pixel_size** = `0.01` `🔗<class_TextMesh_property_pixel_size>`

classref-property-setget

- `void (No return value.)` **set_pixel_size**(value: `float<class_float>`)
- `float<class_float>` **get_pixel_size**()

The size of one pixel's width on the text to scale it in 3D. This property works in tandem with `font_size<class_TextMesh_property_font_size>`.

**Note:** Changing this property will regenerate the mesh, which is a slow operation, especially with large font sizes and long texts. To change the text's size in real-time efficiently, change the node's `Node3D.scale<class_Node3D_property_scale>` instead.

classref-item-separator

classref-property

`StructuredTextParser<enum_TextServer_StructuredTextParser>` **structured_text_bidi_override** = `0` `🔗<class_TextMesh_property_structured_text_bidi_override>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override**(value: `StructuredTextParser<enum_TextServer_StructuredTextParser>`)
- `StructuredTextParser<enum_TextServer_StructuredTextParser>` **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

classref-item-separator

classref-property

`Array<class_Array>` **structured_text_bidi_override_options** = `[]` `🔗<class_TextMesh_property_structured_text_bidi_override_options>`

classref-property-setget

- `void (No return value.)` **set_structured_text_bidi_override_options**(value: `Array<class_Array>`)
- `Array<class_Array>` **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

classref-item-separator

classref-property

`String<class_String>` **text** = `""` `🔗<class_TextMesh_property_text>`

classref-property-setget

- `void (No return value.)` **set_text**(value: `String<class_String>`)
- `String<class_String>` **get_text**()

The text to generate mesh from.

**Note:** Due to being a `Resource<class_Resource>`, it doesn't follow the rules of `Node.auto_translate_mode<class_Node_property_auto_translate_mode>`. If disabling translation is desired, it should be done manually with `Object.set_message_translation()<class_Object_method_set_message_translation>`.

classref-item-separator

classref-property

`Direction<enum_TextServer_Direction>` **text_direction** = `0` `🔗<class_TextMesh_property_text_direction>`

classref-property-setget

- `void (No return value.)` **set_text_direction**(value: `Direction<enum_TextServer_Direction>`)
- `Direction<enum_TextServer_Direction>` **get_text_direction**()

Base text writing direction.

classref-item-separator

classref-property

`bool<class_bool>` **uppercase** = `false` `🔗<class_TextMesh_property_uppercase>`

classref-property-setget

- `void (No return value.)` **set_uppercase**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

classref-item-separator

classref-property

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **vertical_alignment** = `1` `🔗<class_TextMesh_property_vertical_alignment>`

classref-property-setget

- `void (No return value.)` **set_vertical_alignment**(value: `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`)
- `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **get_vertical_alignment**()

Controls the text's vertical alignment. Supports top, center, and bottom.

classref-item-separator

classref-property

`float<class_float>` **width** = `500.0` `🔗<class_TextMesh_property_width>`

classref-property-setget

- `void (No return value.)` **set_width**(value: `float<class_float>`)
- `float<class_float>` **get_width**()

Text width (in pixels), used for fill alignment.