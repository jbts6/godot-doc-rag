github_url
hide

# GLTFBufferView

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a glTF buffer view.

classref-introduction-group

## Description

GLTFBufferView is a data structure representing a glTF `bufferView` that would be found in the `"bufferViews"` array. A buffer is a blob of binary data. A buffer view is a slice of a buffer that can be used to identify and extract data from the buffer.

Most custom uses of buffers only need to use the `buffer<class_GLTFBufferView_property_buffer>`, `byte_length<class_GLTFBufferView_property_byte_length>`, and `byte_offset<class_GLTFBufferView_property_byte_offset>`. The `byte_stride<class_GLTFBufferView_property_byte_stride>` and `indices<class_GLTFBufferView_property_indices>` properties are for more advanced use cases such as interleaved mesh data encoded for the GPU.

classref-introduction-group

## Tutorials

- [Buffers, BufferViews, and Accessors in Khronos glTF specification](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md)
- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **buffer** = `-1` `🔗<class_GLTFBufferView_property_buffer>`

classref-property-setget

- `void (No return value.)` **set_buffer**(value: `int<class_int>`)
- `int<class_int>` **get_buffer**()

The index of the buffer this buffer view is referencing. If `-1`, this buffer view is not referencing any buffer.

classref-item-separator

classref-property

`int<class_int>` **byte_length** = `0` `🔗<class_GLTFBufferView_property_byte_length>`

classref-property-setget

- `void (No return value.)` **set_byte_length**(value: `int<class_int>`)
- `int<class_int>` **get_byte_length**()

The length, in bytes, of this buffer view. If `0`, this buffer view is empty.

classref-item-separator

classref-property

`int<class_int>` **byte_offset** = `0` `🔗<class_GLTFBufferView_property_byte_offset>`

classref-property-setget

- `void (No return value.)` **set_byte_offset**(value: `int<class_int>`)
- `int<class_int>` **get_byte_offset**()

The offset, in bytes, from the start of the buffer to the start of this buffer view.

classref-item-separator

classref-property

`int<class_int>` **byte_stride** = `-1` `🔗<class_GLTFBufferView_property_byte_stride>`

classref-property-setget

- `void (No return value.)` **set_byte_stride**(value: `int<class_int>`)
- `int<class_int>` **get_byte_stride**()

The stride, in bytes, between interleaved data. If `-1`, this buffer view is not interleaved.

classref-item-separator

classref-property

`bool<class_bool>` **indices** = `false` `🔗<class_GLTFBufferView_property_indices>`

classref-property-setget

- `void (No return value.)` **set_indices**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_indices**()

`true` if the GLTFBufferView's OpenGL GPU buffer type is an `ELEMENT_ARRAY_BUFFER` used for vertex indices (integer constant `34963`). `false` if the buffer type is any other value. See [Buffers, BufferViews, and Accessors](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md) for possible values. This property is set on import and used on export.

classref-item-separator

classref-property

`bool<class_bool>` **vertex_attributes** = `false` `🔗<class_GLTFBufferView_property_vertex_attributes>`

classref-property-setget

- `void (No return value.)` **set_vertex_attributes**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_vertex_attributes**()

`true` if the GLTFBufferView's OpenGL GPU buffer type is an `ARRAY_BUFFER` used for vertex attributes (integer constant `34962`). `false` if the buffer type is any other value. See [Buffers, BufferViews, and Accessors](https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/gltfTutorial_005_BuffersBufferViewsAccessors.md) for possible values. This property is set on import and used on export.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`GLTFBufferView<class_GLTFBufferView>` **from_dictionary**(dictionary: `Dictionary<class_Dictionary>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_GLTFBufferView_method_from_dictionary>`

Creates a new GLTFBufferView instance by parsing the given `Dictionary<class_Dictionary>`.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **load_buffer_view_data**(state: `GLTFState<class_GLTFState>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFBufferView_method_load_buffer_view_data>`

Loads the buffer view data from the buffer referenced by this buffer view in the given `GLTFState<class_GLTFState>`. Interleaved data with a byte stride is not yet supported by this method. The data is returned as a `PackedByteArray<class_PackedByteArray>`.

classref-item-separator

classref-method

`Dictionary<class_Dictionary>` **to_dictionary**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_GLTFBufferView_method_to_dictionary>`

Serializes this GLTFBufferView instance into a `Dictionary<class_Dictionary>`.