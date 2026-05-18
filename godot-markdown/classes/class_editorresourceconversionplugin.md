github_url
hide

# EditorResourceConversionPlugin

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Plugin for adding custom converters from one resource format to another in the editor resource picker context menu; for example, converting a `StandardMaterial3D<class_StandardMaterial3D>` to a `ShaderMaterial<class_ShaderMaterial>`.

classref-introduction-group

## Description

**EditorResourceConversionPlugin** is invoked when the context menu is brought up for a resource in the editor inspector. Relevant conversion plugins will appear as menu options to convert the given resource to a target type.

Below shows an example of a basic plugin that will convert an `ImageTexture<class_ImageTexture>` to a `PortableCompressedTexture2D<class_PortableCompressedTexture2D>`.

gdscript

extends EditorResourceConversionPlugin

func handles(resource: Resource):
return resource is ImageTexture

func converts_to():
return "PortableCompressedTexture2D"

func convert(itex: Resource):
var ptex = PortableCompressedTexture2D.new() ptex.create_from_image(itex.get_image(), PortableCompressedTexture2D.COMPRESSION_MODE_LOSSLESS) return ptex

To use an **EditorResourceConversionPlugin**, register it using the `EditorPlugin.add_resource_conversion_plugin()<class_EditorPlugin_method_add_resource_conversion_plugin>` method first.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Resource<class_Resource>` **\_convert**(resource: `Resource<class_Resource>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorResourceConversionPlugin_private_method__convert>`

Takes an input `Resource<class_Resource>` and converts it to the type given in `_converts_to()<class_EditorResourceConversionPlugin_private_method__converts_to>`. The returned `Resource<class_Resource>` is the result of the conversion, and the input `Resource<class_Resource>` remains unchanged.

classref-item-separator

classref-method

`String<class_String>` **\_converts_to**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorResourceConversionPlugin_private_method__converts_to>`

Returns the class name of the target type of `Resource<class_Resource>` that this plugin converts source resources to.

classref-item-separator

classref-method

`bool<class_bool>` **\_handles**(resource: `Resource<class_Resource>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorResourceConversionPlugin_private_method__handles>`

Called to determine whether a particular `Resource<class_Resource>` can be converted to the target resource type by this plugin.