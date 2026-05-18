github_url
hide

# PlaceholderTextureLayered

**Inherits:** `TextureLayered<class_TextureLayered>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `PlaceholderCubemap<class_PlaceholderCubemap>`, `PlaceholderCubemapArray<class_PlaceholderCubemapArray>`, `PlaceholderTexture2DArray<class_PlaceholderTexture2DArray>`

Placeholder class for a 2-dimensional texture array.

classref-introduction-group

## Description

This class is used when loading a project that uses a `TextureLayered<class_TextureLayered>` subclass in 2 conditions:

- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

**Note:** This is not intended to be used as an actual texture for rendering. It is not guaranteed to work like one in shaders or materials (for example when calculating UV).

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **layers** = `1` `🔗<class_PlaceholderTextureLayered_property_layers>`

classref-property-setget

- `void (No return value.)` **set_layers**(value: `int<class_int>`)
- `int<class_int>` **get_layers**()

The number of layers in the texture array.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **size** = `Vector2i(1, 1)` `🔗<class_PlaceholderTextureLayered_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_size**()

The size of each texture layer (in pixels).