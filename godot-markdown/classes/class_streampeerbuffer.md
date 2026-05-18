github_url
hide

# StreamPeerBuffer

**Inherits:** `StreamPeer<class_StreamPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A stream peer used to handle binary data streams.

classref-introduction-group

## Description

A data buffer stream peer that uses a byte array as the stream. This object can be used to handle binary data from network sessions. To handle binary data stored in files, `FileAccess<class_FileAccess>` can be used directly.

A **StreamPeerBuffer** object keeps an internal cursor which is the offset in bytes to the start of the buffer. Get and put operations are performed at the cursor position and will move the cursor accordingly.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedByteArray<class_PackedByteArray>` **data_array** = `PackedByteArray()` `🔗<class_StreamPeerBuffer_property_data_array>`

classref-property-setget

- `void (No return value.)` **set_data_array**(value: `PackedByteArray<class_PackedByteArray>`)
- `PackedByteArray<class_PackedByteArray>` **get_data_array**()

The underlying data buffer. Setting this value resets the cursor.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedByteArray<class_PackedByteArray>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear**() `🔗<class_StreamPeerBuffer_method_clear>`

Clears the `data_array<class_StreamPeerBuffer_property_data_array>` and resets the cursor.

classref-item-separator

classref-method

`StreamPeerBuffer<class_StreamPeerBuffer>` **duplicate**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StreamPeerBuffer_method_duplicate>`

Returns a new **StreamPeerBuffer** with the same `data_array<class_StreamPeerBuffer_property_data_array>` content.

classref-item-separator

classref-method

`int<class_int>` **get_position**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StreamPeerBuffer_method_get_position>`

Returns the current cursor position.

classref-item-separator

classref-method

`int<class_int>` **get_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StreamPeerBuffer_method_get_size>`

Returns the size of `data_array<class_StreamPeerBuffer_property_data_array>`.

classref-item-separator

classref-method

`void (No return value.)` **resize**(size: `int<class_int>`) `🔗<class_StreamPeerBuffer_method_resize>`

Resizes the `data_array<class_StreamPeerBuffer_property_data_array>`. This *doesn't* update the cursor.

classref-item-separator

classref-method

`void (No return value.)` **seek**(position: `int<class_int>`) `🔗<class_StreamPeerBuffer_method_seek>`

Moves the cursor to the specified position. `position` must be a valid index of `data_array<class_StreamPeerBuffer_property_data_array>`.