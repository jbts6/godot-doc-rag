github_url
hide

# GLTFObjectModelProperty

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Describes how to access a property as defined in the glTF object model.

classref-introduction-group

## Description

GLTFObjectModelProperty defines a mapping between a property in the glTF object model and a NodePath in the Godot scene tree. This can be used to animate properties in a glTF file using the `KHR_animation_pointer` extension, or to access them through an engine-agnostic script such as a behavior graph as defined by the `KHR_interactivity` extension.

The glTF property is identified by JSON pointer(s) stored in `json_pointers<class_GLTFObjectModelProperty_property_json_pointers>`, while the Godot property it maps to is defined by `node_paths<class_GLTFObjectModelProperty_property_node_paths>`. In most cases `json_pointers<class_GLTFObjectModelProperty_property_json_pointers>` and `node_paths<class_GLTFObjectModelProperty_property_node_paths>` will each only have one item, but in some cases a single glTF JSON pointer will map to multiple Godot properties, or a single Godot property will be mapped to multiple glTF JSON pointers, or it might be a many-to-many relationship.

`Expression<class_Expression>` objects can be used to define conversions between the data, such as when glTF defines an angle in radians and Godot uses degrees. The `object_model_type<class_GLTFObjectModelProperty_property_object_model_type>` property defines the type of data stored in the glTF file as defined by the object model, see `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` for possible values.

classref-introduction-group

## Tutorials

- [GLTF Object Model](https://github.com/KhronosGroup/glTF/blob/main/specification/2.0/ObjectModel.adoc)
- [KHR_animation_pointer GLTF extension](https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_animation_pointer)

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **GLTFObjectModelType**: `🔗<enum_GLTFObjectModelProperty_GLTFObjectModelType>`

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_UNKNOWN** = `0`

Unknown or not set object model type. If the object model type is set to this value, the real type still needs to be determined.

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_BOOL** = `1`

Object model type "bool". Represented in the glTF JSON as a boolean, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "SCALAR". When encoded in an accessor, a value of `0` is `false`, and any other value is `true`.

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT** = `2`

Object model type "float". Represented in the glTF JSON as a number, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "SCALAR".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT_ARRAY** = `3`

Object model type "float\[\]". Represented in the glTF JSON as an array of numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "SCALAR".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT2** = `4`

Object model type "float2". Represented in the glTF JSON as an array of two numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "VEC2".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT3** = `5`

Object model type "float3". Represented in the glTF JSON as an array of three numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "VEC3".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT4** = `6`

Object model type "float4". Represented in the glTF JSON as an array of four numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "VEC4".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT2X2** = `7`

Object model type "float2x2". Represented in the glTF JSON as an array of four numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "MAT2".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT3X3** = `8`

Object model type "float3x3". Represented in the glTF JSON as an array of nine numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "MAT3".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_FLOAT4X4** = `9`

Object model type "float4x4". Represented in the glTF JSON as an array of sixteen numbers, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "MAT4".

classref-enumeration-constant

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **GLTF_OBJECT_MODEL_TYPE_INT** = `10`

Object model type "int". Represented in the glTF JSON as a number, and encoded in a `GLTFAccessor<class_GLTFAccessor>` as "SCALAR". The range of values is limited to signed integers. For `KHR_interactivity`, only 32-bit integers are supported.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Expression<class_Expression>` **gltf_to_godot_expression** `🔗<class_GLTFObjectModelProperty_property_gltf_to_godot_expression>`

classref-property-setget

- `void (No return value.)` **set_gltf_to_godot_expression**(value: `Expression<class_Expression>`)
- `Expression<class_Expression>` **get_gltf_to_godot_expression**()

If set, this `Expression<class_Expression>` will be used to convert the property value from the glTF object model to the value expected by the Godot property. This is useful when the glTF object model uses a different unit system, or when the data needs to be transformed in some way. If `null`, the value will be copied as-is.

classref-item-separator

classref-property

`Expression<class_Expression>` **godot_to_gltf_expression** `🔗<class_GLTFObjectModelProperty_property_godot_to_gltf_expression>`

classref-property-setget

- `void (No return value.)` **set_godot_to_gltf_expression**(value: `Expression<class_Expression>`)
- `Expression<class_Expression>` **get_godot_to_gltf_expression**()

If set, this `Expression<class_Expression>` will be used to convert the property value from the Godot property to the value expected by the glTF object model. This is useful when the glTF object model uses a different unit system, or when the data needs to be transformed in some way. If `null`, the value will be copied as-is.

classref-item-separator

classref-property

`Array<class_Array>`\[`PackedStringArray<class_PackedStringArray>`\] **json_pointers** = `[]` `🔗<class_GLTFObjectModelProperty_property_json_pointers>`

classref-property-setget

- `void (No return value.)` **set_json_pointers**(value: `Array<class_Array>`\[`PackedStringArray<class_PackedStringArray>`\])
- `Array<class_Array>`\[`PackedStringArray<class_PackedStringArray>`\] **get_json_pointers**()

The glTF object model JSON pointers used to identify the property in the glTF object model. In most cases, there will be only one item in this array, but specific cases may require multiple pointers. The items are themselves arrays which represent the JSON pointer split into its components.

classref-item-separator

classref-property

`Array<class_Array>`\[`NodePath<class_NodePath>`\] **node_paths** = `[]` `🔗<class_GLTFObjectModelProperty_property_node_paths>`

classref-property-setget

- `void (No return value.)` **set_node_paths**(value: `Array<class_Array>`\[`NodePath<class_NodePath>`\])
- `Array<class_Array>`\[`NodePath<class_NodePath>`\] **get_node_paths**()

An array of `NodePath<class_NodePath>`s that point to a property, or multiple properties, in the Godot scene tree. On import, this will either be set by `GLTFDocument<class_GLTFDocument>`, or by a `GLTFDocumentExtension<class_GLTFDocumentExtension>` class. For simple cases, use `append_path_to_property()<class_GLTFObjectModelProperty_method_append_path_to_property>` to add properties to this array.

In most cases `node_paths<class_GLTFObjectModelProperty_property_node_paths>` will only have one item, but in some cases a single glTF JSON pointer will map to multiple Godot properties. For example, a `GLTFCamera<class_GLTFCamera>` or `GLTFLight<class_GLTFLight>` used on multiple glTF nodes will be represented by multiple Godot nodes.

classref-item-separator

classref-property

`GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **object_model_type** = `0` `🔗<class_GLTFObjectModelProperty_property_object_model_type>`

classref-property-setget

- `void (No return value.)` **set_object_model_type**(value: `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`)
- `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` **get_object_model_type**()

The type of data stored in the glTF file as defined by the object model. This is a superset of the available accessor types, and determines the accessor type.

classref-item-separator

classref-property

`Variant.Type<enum_@GlobalScope_Variant.Type>` **variant_type** = `0` `🔗<class_GLTFObjectModelProperty_property_variant_type>`

classref-property-setget

- `void (No return value.)` **set_variant_type**(value: `Variant.Type<enum_@GlobalScope_Variant.Type>`)
- `Variant.Type<enum_@GlobalScope_Variant.Type>` **get_variant_type**()

The type of data stored in the Godot property. This is the type of the property that the `node_paths<class_GLTFObjectModelProperty_property_node_paths>` point to.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **append_node_path**(node_path: `NodePath<class_NodePath>`) `🔗<class_GLTFObjectModelProperty_method_append_node_path>`

Appends a `NodePath<class_NodePath>` to `node_paths<class_GLTFObjectModelProperty_property_node_paths>`. This can be used by `GLTFDocumentExtension<class_GLTFDocumentExtension>` classes to define how a glTF object model property maps to a Godot property, or multiple Godot properties. Prefer using `append_path_to_property()<class_GLTFObjectModelProperty_method_append_path_to_property>` for simple cases. Be sure to also call `set_types()<class_GLTFObjectModelProperty_method_set_types>` once (the order does not matter).

classref-item-separator

classref-method

`void (No return value.)` **append_path_to_property**(node_path: `NodePath<class_NodePath>`, prop_name: `StringName<class_StringName>`) `🔗<class_GLTFObjectModelProperty_method_append_path_to_property>`

High-level wrapper over `append_node_path()<class_GLTFObjectModelProperty_method_append_node_path>` that handles the most common cases. It constructs a new `NodePath<class_NodePath>` using `node_path` as a base and appends `prop_name` to the subpath. Be sure to also call `set_types()<class_GLTFObjectModelProperty_method_set_types>` once (the order does not matter).

classref-item-separator

classref-method

`GLTFAccessorType<enum_GLTFAccessor_GLTFAccessorType>` **get_accessor_type**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFObjectModelProperty_method_get_accessor_type>`

The GLTF accessor type associated with this property's `object_model_type<class_GLTFObjectModelProperty_property_object_model_type>`. See `GLTFAccessor.accessor_type<class_GLTFAccessor_property_accessor_type>` for possible values, and see `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>` for how the object model type maps to accessor types.

classref-item-separator

classref-method

`bool<class_bool>` **has_json_pointers**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFObjectModelProperty_method_has_json_pointers>`

Returns `true` if `json_pointers<class_GLTFObjectModelProperty_property_json_pointers>` is not empty. This is used during export to determine if a **GLTFObjectModelProperty** can handle converting a Godot property to a glTF object model property.

classref-item-separator

classref-method

`bool<class_bool>` **has_node_paths**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFObjectModelProperty_method_has_node_paths>`

Returns `true` if `node_paths<class_GLTFObjectModelProperty_property_node_paths>` is not empty. This is used during import to determine if a **GLTFObjectModelProperty** can handle converting a glTF object model property to a Godot property.

classref-item-separator

classref-method

`void (No return value.)` **set_types**(variant_type: `Variant.Type<enum_@GlobalScope_Variant.Type>`, obj_model_type: `GLTFObjectModelType<enum_GLTFObjectModelProperty_GLTFObjectModelType>`) `🔗<class_GLTFObjectModelProperty_method_set_types>`

Sets the `variant_type<class_GLTFObjectModelProperty_property_variant_type>` and `object_model_type<class_GLTFObjectModelProperty_property_object_model_type>` properties. This is a convenience method to set both properties at once, since they are almost always known at the same time. This method should be called once. Calling it again with the same values will have no effect.