github_url
hide

# Script

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `CSharpScript<class_CSharpScript>`, `GDScript<class_GDScript>`, `ScriptExtension<class_ScriptExtension>`

A class stored as a resource.

classref-introduction-group

## Description

A class stored as a resource. A script extends the functionality of all objects that instantiate it.

This is the base class for all scripts and should not be used directly. Trying to create a new script with this class will result in an error.

The `new` method of a script subclass creates a new instance. `Object.set_script()<class_Object_method_set_script>` extends an existing object, if that object's class matches one of the script's base classes.

classref-introduction-group

## Tutorials

- `Scripting documentation index <../tutorials/scripting/index>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **source_code** `🔗<class_Script_property_source_code>`

classref-property-setget

- `void (No return value.)` **set_source_code**(value: `String<class_String>`)
- `String<class_String>` **get_source_code**()

The script source code or an empty string if source code is not available. When set, does not reload the class implementation automatically.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **can_instantiate**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_can_instantiate>`

Returns `true` if the script can be instantiated.

classref-item-separator

classref-method

`Script<class_Script>` **get_base_script**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_get_base_script>`

Returns the script directly inherited by this script.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_global_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_get_global_name>`

Returns the class name associated with the script, if there is one. Returns an empty string otherwise.

To give the script a global name, you can use the `class_name` keyword in GDScript and the `[GlobalClass]` attribute in C#.

gdscript

class_name MyNode extends Node

csharp

using Godot;

\[GlobalClass\] public partial class MyNode : Node { }

classref-item-separator

classref-method

`StringName<class_StringName>` **get_instance_base_type**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_get_instance_base_type>`

Returns the script's base type.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_property_default_value**(property: `StringName<class_StringName>`) `🔗<class_Script_method_get_property_default_value>`

Returns the default value of the specified property.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_rpc_config**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_get_rpc_config>`

Returns a `Dictionary<class_Dictionary>` mapping method names to their RPC configuration defined by this script.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **get_script_constant_map**() `🔗<class_Script_method_get_script_constant_map>`

Returns a dictionary containing constant names and their values.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_script_method_list**() `🔗<class_Script_method_get_script_method_list>`

Returns the list of methods in this **Script**.

**Note:** The dictionaries returned by this method are formatted identically to those returned by `Object.get_method_list()<class_Object_method_get_method_list>`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_script_property_list**() `🔗<class_Script_method_get_script_property_list>`

Returns the list of properties in this **Script**.

**Note:** The dictionaries returned by this method are formatted identically to those returned by `Object.get_property_list()<class_Object_method_get_property_list>`.

classref-item-separator

classref-method

`Array<class_Array>`\[`Dictionary<class_Dictionary>`\] **get_script_signal_list**() `🔗<class_Script_method_get_script_signal_list>`

Returns the list of signals defined in this **Script**.

**Note:** The dictionaries returned by this method are formatted identically to those returned by `Object.get_signal_list()<class_Object_method_get_signal_list>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_script_method**(method_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_has_script_method>`

Returns `true` if the script, or a base class, defines a method with the given name.

classref-item-separator

classref-method

`bool<class_bool>` **has_script_signal**(signal_name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_has_script_signal>`

Returns `true` if the script, or a base class, defines a signal with the given name.

classref-item-separator

classref-method

`bool<class_bool>` **has_source_code**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_has_source_code>`

Returns `true` if the script contains non-empty source code.

**Note:** If a script does not have source code, this does not mean that it is invalid or unusable. For example, a `GDScript<class_GDScript>` that was exported with binary tokenization has no source code, but still behaves as expected and could be instantiated. This can be checked with `can_instantiate()<class_Script_method_can_instantiate>`.

classref-item-separator

classref-method

`bool<class_bool>` **instance_has**(base_object: `Object<class_Object>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_instance_has>`

**Deprecated:** Compare this script with `Object.get_script()<class_Object_method_get_script>` instead.

Returns `true` if `base_object` is an instance of this script.

classref-item-separator

classref-method

`bool<class_bool>` **is_abstract**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_is_abstract>`

Returns `true` if the script is an abstract script. An abstract script does not have a constructor and cannot be instantiated.

classref-item-separator

classref-method

`bool<class_bool>` **is_tool**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Script_method_is_tool>`

Returns `true` if the script is a tool script. A tool script can run in the editor.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **reload**(keep_state: `bool<class_bool>` = false) `🔗<class_Script_method_reload>`

Reloads the script's class implementation. Returns an error code.