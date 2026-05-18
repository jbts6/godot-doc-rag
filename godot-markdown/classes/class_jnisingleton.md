github_url
hide

# JNISingleton

**Inherits:** `Object<class_Object>`

Singleton that connects the engine with Android plugins to interface with native Android code.

classref-introduction-group

## Description

The JNISingleton is implemented only in the Android export. It's used to call methods and connect signals from an Android plugin written in Java or Kotlin. Methods and signals can be called and connected to the JNISingleton as if it is a Node. See [Java Native Interface - Wikipedia](https://en.wikipedia.org/wiki/Java_Native_Interface) for more information.

classref-introduction-group

## Tutorials

- [Creating Android plugins](../tutorials/platform/android/android_plugin.html#doc-android-plugin)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **has_java_method**(method: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_JNISingleton_method_has_java_method>`

Returns `true` if the given `method` name exists in the JNISingleton's Java methods.