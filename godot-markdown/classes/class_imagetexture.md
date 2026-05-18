github_url
hide

# ImageTexture

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A `Texture2D<class_Texture2D>` based on an `Image<class_Image>`.

classref-introduction-group

## Description

A `Texture2D<class_Texture2D>` based on an `Image<class_Image>`. For an image to be displayed, an **ImageTexture** has to be created from it using the `create_from_image()<class_ImageTexture_method_create_from_image>` method:

    var image = Image.load_from_file("res://icon.svg")
    var texture = ImageTexture.create_from_image(image)
    $Sprite2D.texture = texture

This way, textures can be created at run-time by loading images both from within the editor and externally.

**Warning:** Prefer to load imported textures with `@GDScript.load()<class_@GDScript_method_load>` over loading them from within the filesystem dynamically with `Image.load()<class_Image_method_load>`, as it may not work in exported projects:

    var texture = load("res://icon.svg")
    $Sprite2D.texture = texture

This is because images have to be imported as a `CompressedTexture2D<class_CompressedTexture2D>` first to be loaded with `@GDScript.load()<class_@GDScript_method_load>`. If you'd still like to load an image file just like any other `Resource<class_Resource>`, import it as an `Image<class_Image>` resource instead, and then load it normally using the `@GDScript.load()<class_@GDScript_method_load>` method.

**Note:** The image can be retrieved from an imported texture using the `Texture2D.get_image()<class_Texture2D_method_get_image>` method, which returns a copy of the image:

    var texture = load("res://icon.svg")
    var image = texture.get_image()

An **ImageTexture** is not meant to be operated from within the editor interface directly, and is mostly useful for rendering images on screen dynamically via code. If you need to generate images procedurally from within the editor, consider saving and importing images as custom texture resources implementing a new `EditorImportPlugin<class_EditorImportPlugin>`.

**Note:** The maximum texture size is 16384×16384 pixels due to graphics hardware limitations.

classref-introduction-group

## Tutorials

- `Importing images <../tutorials/assets_pipeline/importing_images>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`ImageTexture<class_ImageTexture>` **create_from_image**(image: `Image<class_Image>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_ImageTexture_method_create_from_image>`

Creates a new **ImageTexture** and initializes it by allocating and setting the data from an `Image<class_Image>`.

classref-item-separator

classref-method

`void (No return value.)` **set_image**(image: `Image<class_Image>`) `🔗<class_ImageTexture_method_set_image>`

Replaces the texture's data with a new `Image<class_Image>`. This will re-allocate new memory for the texture.

If you want to update the image, but don't need to change its parameters (format, size), use `update()<class_ImageTexture_method_update>` instead for better performance.

classref-item-separator

classref-method

`void (No return value.)` **set_size_override**(size: `Vector2i<class_Vector2i>`) `🔗<class_ImageTexture_method_set_size_override>`

Resizes the texture to the specified dimensions.

classref-item-separator

classref-method

`void (No return value.)` **update**(image: `Image<class_Image>`) `🔗<class_ImageTexture_method_update>`

Replaces the texture's data with a new `Image<class_Image>`.

**Note:** The texture has to be created using `create_from_image()<class_ImageTexture_method_create_from_image>` or initialized first with the `set_image()<class_ImageTexture_method_set_image>` method before it can be updated. The new image dimensions, format, and mipmaps configuration should match the existing texture's image configuration.

Use this method over `set_image()<class_ImageTexture_method_set_image>` if you need to update the texture frequently, which is faster than allocating additional memory for a new texture each time.