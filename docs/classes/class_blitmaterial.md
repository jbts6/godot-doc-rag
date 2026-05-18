github_url
hide

# BlitMaterial

**Inherits:** `Material<class_Material>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A material that processes blit calls to a DrawableTexture.

classref-introduction-group

## Description

A material resource that can be used by DrawableTextures when processing blit calls to draw.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **BlendMode**: `🔗<enum_BlitMaterial_BlendMode>`

classref-enumeration-constant

`BlendMode<enum_BlitMaterial_BlendMode>` **BLEND_MODE_MIX** = `0`

Mix blending mode. Colors are assumed to be independent of the alpha (opacity) value.

classref-enumeration-constant

`BlendMode<enum_BlitMaterial_BlendMode>` **BLEND_MODE_ADD** = `1`

Additive blending mode.

classref-enumeration-constant

`BlendMode<enum_BlitMaterial_BlendMode>` **BLEND_MODE_SUB** = `2`

Subtractive blending mode.

classref-enumeration-constant

`BlendMode<enum_BlitMaterial_BlendMode>` **BLEND_MODE_MUL** = `3`

Multiplicative blending mode.

classref-enumeration-constant

`BlendMode<enum_BlitMaterial_BlendMode>` **BLEND_MODE_DISABLED** = `4`

No blending mode, direct color copy.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BlendMode<enum_BlitMaterial_BlendMode>` **blend_mode** = `0` `🔗<class_BlitMaterial_property_blend_mode>`

classref-property-setget

- `void (No return value.)` **set_blend_mode**(value: `BlendMode<enum_BlitMaterial_BlendMode>`)
- `BlendMode<enum_BlitMaterial_BlendMode>` **get_blend_mode**()

The manner in which the newly blitted texture is blended with the original DrawableTexture.