github_url
hide

# OpenXRStructureBase

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `OpenXRSpatialContextPersistenceConfig<class_OpenXRSpatialContextPersistenceConfig>`

Object for storing OpenXR structure data.

classref-introduction-group

## Description

Object for storing OpenXR structure data that is passed when calling into OpenXR APIs.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`OpenXRStructureBase<class_OpenXRStructureBase>` **next** `🔗<class_OpenXRStructureBase_property_next>`

classref-property-setget

- `void (No return value.)` **set_next**(value: `OpenXRStructureBase<class_OpenXRStructureBase>`)
- `OpenXRStructureBase<class_OpenXRStructureBase>` **get_next**()

Setting another structure object here chains these structures together to extend the API functionality. Consult the OpenXR documentation for which structures can be used with a given API call.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **\_get_header**(next: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_OpenXRStructureBase_private_method__get_header>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`int<class_int>` **get_structure_type**() `🔗<class_OpenXRStructureBase_method_get_structure_type>`

Returns the structure type (OpenXR `XrStructureType`) used for this structure.