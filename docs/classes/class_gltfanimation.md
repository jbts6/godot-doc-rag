github_url
hide

# GLTFAnimation

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-introduction-group

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **loop** = `false` `🔗<class_GLTFAnimation_property_loop>`

classref-property-setget

- `void (No return value.)` **set_loop**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_loop**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`String<class_String>` **original_name** = `""` `🔗<class_GLTFAnimation_property_original_name>`

classref-property-setget

- `void (No return value.)` **set_original_name**(value: `String<class_String>`)
- `String<class_String>` **get_original_name**()

The original name of the animation.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Variant<class_Variant>` **get_additional_data**(extension_name: `StringName<class_StringName>`) `🔗<class_GLTFAnimation_method_get_additional_data>`

Gets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in `GLTFDocumentExtension<class_GLTFDocumentExtension>` classes, which is important because they are stateless.

The argument should be the `GLTFDocumentExtension<class_GLTFDocumentExtension>` name (does not have to match the extension name in the glTF file), and the return value can be anything you set. If nothing was set, the return value is `null`.

classref-item-separator

classref-method

`void (No return value.)` **set_additional_data**(extension_name: `StringName<class_StringName>`, additional_data: `Variant<class_Variant>`) `🔗<class_GLTFAnimation_method_set_additional_data>`

Sets additional arbitrary data in this **GLTFAnimation** instance. This can be used to keep per-node state data in `GLTFDocumentExtension<class_GLTFDocumentExtension>` classes, which is important because they are stateless.

The first argument should be the `GLTFDocumentExtension<class_GLTFDocumentExtension>` name (does not have to match the extension name in the glTF file), and the second argument can be anything you want.