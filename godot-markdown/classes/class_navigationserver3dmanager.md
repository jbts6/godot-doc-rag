github_url
hide

# NavigationServer3DManager

**Inherits:** `Object<class_Object>`

A singleton for managing `NavigationServer3D<class_NavigationServer3D>` implementations.

classref-introduction-group

## Description

**NavigationServer3DManager** is the API for registering `NavigationServer3D<class_NavigationServer3D>` implementations and setting the default implementation.

**Note:** It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **register_server**(name: `String<class_String>`, create_callback: `Callable<class_Callable>`) `🔗<class_NavigationServer3DManager_method_register_server>`

Registers a `NavigationServer3D<class_NavigationServer3D>` implementation by passing a `name` and a `Callable<class_Callable>` that returns a `NavigationServer3D<class_NavigationServer3D>` object.

classref-item-separator

classref-method

`void (No return value.)` **set_default_server**(name: `String<class_String>`, priority: `int<class_int>`) `🔗<class_NavigationServer3DManager_method_set_default_server>`

Sets the default `NavigationServer3D<class_NavigationServer3D>` implementation to the one identified by `name`, if `priority` is greater than the priority of the current default implementation.