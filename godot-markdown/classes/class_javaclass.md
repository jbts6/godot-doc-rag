github_url
hide

# JavaClass

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a class from the Java Native Interface.

classref-introduction-group

## Description

Represents a class from the Java Native Interface. It is returned from `JavaClassWrapper.wrap()<class_JavaClassWrapper_method_wrap>`.

**Note:** This class only works on Android. On any other platform, this class does nothing.

**Note:** This class is not to be confused with `JavaScriptObject<class_JavaScriptObject>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_java_class_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_JavaClass_method_get_java_class_name>`

Returns the Java class name.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_java_method_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_JavaClass_method_get_java_method_list>`

Returns the object's Java methods and their signatures as an `Array<class_Array>` of dictionaries, in the same format as `Object.get_method_list()<class_Object_method_get_method_list>`.

classref-item-separator

classref-method

`JavaClass<class_JavaClass>` **get_java_parent_class**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_JavaClass_method_get_java_parent_class>`

Returns a **JavaClass** representing the Java parent class of this class.

classref-item-separator

classref-method

`bool<class_bool>` **has_java_method**(method: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_JavaClass_method_has_java_method>`

Returns `true` if the given `method` name exists in the object's Java methods.