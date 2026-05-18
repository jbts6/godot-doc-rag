github_url
hide

# ResourceImporterBMFont

**Inherits:** `ResourceImporter<class_ResourceImporter>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Imports a bitmap font in the BMFont (`.fnt`) format.

classref-introduction-group

## Description

The BMFont format is a format created by the [BMFont](https://www.angelcode.com/products/bmfont/) program. Many BMFont-compatible programs also exist, like [BMGlyph](https://www.bmglyph.com/).

Compared to `ResourceImporterImageFont<class_ResourceImporterImageFont>`, **ResourceImporterBMFont** supports bitmap fonts with varying glyph widths/heights.

See also `ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>`.

classref-introduction-group

## Tutorials

- [Bitmap fonts - Using fonts](../tutorials/ui/gui_using_fonts.html#bitmap-fonts)

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **compress** = `true` `🔗<class_ResourceImporterBMFont_property_compress>`

If `true`, uses lossless compression for the resulting font.

classref-item-separator

classref-property

`Array<class_Array>` **fallbacks** = `[]` `🔗<class_ResourceImporterBMFont_property_fallbacks>`

List of font fallbacks to use if a glyph isn't found in this bitmap font. Fonts at the beginning of the array are attempted first.

classref-item-separator

classref-property

`int<class_int>` **scaling_mode** = `2` `🔗<class_ResourceImporterBMFont_property_scaling_mode>`

Font scaling mode.