github_url
hide

# ResourcePreloader

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

A node used to preload sub-resources inside a scene.

classref-introduction-group

## Description

This node is used to preload sub-resources inside a scene, so when the scene is loaded, all the resources are ready to use and can be retrieved from the preloader. You can add the resources using the ResourcePreloader tab when the node is selected.

GDScript has a simplified `@GDScript.preload()<class_@GDScript_method_preload>` built-in method which can be used in most situations, leaving the use of **ResourcePreloader** for more advanced scenarios.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_resource**(name: `StringName<class_StringName>`, resource: `Resource<class_Resource>`) `🔗<class_ResourcePreloader_method_add_resource>`

Adds a resource to the preloader with the given `name`. If a resource with the given `name` already exists, the new resource will be renamed to "`name` N" where N is an incrementing number starting from 2.

classref-item-separator

classref-method

`Resource<class_Resource>` **get_resource**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ResourcePreloader_method_get_resource>`

Returns the resource associated to `name`.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_resource_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ResourcePreloader_method_get_resource_list>`

Returns the list of resources inside the preloader.

classref-item-separator

classref-method

`bool<class_bool>` **has_resource**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_ResourcePreloader_method_has_resource>`

Returns `true` if the preloader contains a resource associated to `name`.

classref-item-separator

classref-method

`void (No return value.)` **remove_resource**(name: `StringName<class_StringName>`) `🔗<class_ResourcePreloader_method_remove_resource>`

Removes the resource associated to `name` from the preloader.

classref-item-separator

classref-method

`void (No return value.)` **rename_resource**(name: `StringName<class_StringName>`, newname: `StringName<class_StringName>`) `🔗<class_ResourcePreloader_method_rename_resource>`

Renames a resource inside the preloader from `name` to `newname`.