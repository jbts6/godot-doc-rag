github_url
hide

# PanoramaSkyMaterial

**Inherits:** `Material<class_Material>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A material that provides a special texture to a `Sky<class_Sky>`, usually an HDR panorama.

classref-introduction-group

## Description

A resource referenced in a `Sky<class_Sky>` that is used to draw a background. **PanoramaSkyMaterial** functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a `Cubemap<class_Cubemap>`.

Using an HDR panorama is strongly recommended for accurate, high-quality reflections. Godot supports the Radiance HDR (`.hdr`) and OpenEXR (`.exr`) image formats for this purpose.

You can use [this tool](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html) to convert a cubemap to an equirectangular sky map.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **energy_multiplier** = `1.0` `🔗<class_PanoramaSkyMaterial_property_energy_multiplier>`

classref-property-setget

- `void (No return value.)` **set_energy_multiplier**(value: `float<class_float>`)
- `float<class_float>` **get_energy_multiplier**()

The sky's overall brightness multiplier. Higher values result in a brighter sky.

classref-item-separator

classref-property

`bool<class_bool>` **filter** = `true` `🔗<class_PanoramaSkyMaterial_property_filter>`

classref-property-setget

- `void (No return value.)` **set_filtering_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_filtering_enabled**()

A boolean value to determine if the background texture should be filtered or not.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **panorama** `🔗<class_PanoramaSkyMaterial_property_panorama>`

classref-property-setget

- `void (No return value.)` **set_panorama**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_panorama**()

`Texture2D<class_Texture2D>` to be applied to the **PanoramaSkyMaterial**.