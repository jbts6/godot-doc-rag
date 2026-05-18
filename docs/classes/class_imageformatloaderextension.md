github_url
hide

# ImageFormatLoaderExtension

**Inherits:** `ImageFormatLoader<class_ImageFormatLoader>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Base class for creating `ImageFormatLoader<class_ImageFormatLoader>` extensions (adding support for extra image formats).

classref-introduction-group

## Description

The engine supports multiple image formats out of the box (PNG, SVG, JPEG, WebP to name a few), but you can choose to implement support for additional image formats by extending this class.

Be sure to respect the documented return types and values. You should create an instance of it, and call `add_format_loader()<class_ImageFormatLoaderExtension_method_add_format_loader>` to register that loader during the initialization phase.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PackedStringArray<class_PackedStringArray>` **\_get_recognized_extensions**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>`

Returns the list of file extensions for this image format. Files with the given extensions will be treated as image file and loaded using this class.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_load_image**(image: `Image<class_Image>`, fileaccess: `FileAccess<class_FileAccess>`, flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`LoaderFlags<enum_ImageFormatLoader_LoaderFlags>`\], scale: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_ImageFormatLoaderExtension_private_method__load_image>`

Loads the content of `fileaccess` into the provided `image`.

classref-item-separator

classref-method

`void (No return value.)` **add_format_loader**() `🔗<class_ImageFormatLoaderExtension_method_add_format_loader>`

Add this format loader to the engine, allowing it to recognize the file extensions returned by `_get_recognized_extensions()<class_ImageFormatLoaderExtension_private_method__get_recognized_extensions>`.

classref-item-separator

classref-method

`void (No return value.)` **remove_format_loader**() `🔗<class_ImageFormatLoaderExtension_method_remove_format_loader>`

Remove this format loader from the engine.