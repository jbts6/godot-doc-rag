github_url
hide

# PacketPeerStream

**Inherits:** `PacketPeer<class_PacketPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Wrapper to use a PacketPeer over a StreamPeer.

classref-introduction-group

## Description

PacketStreamPeer provides a wrapper for working using packets over a stream. This allows for using packet based code with StreamPeers. PacketPeerStream implements a custom protocol over the StreamPeer, so the user should not read or write to the wrapped StreamPeer directly.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **input_buffer_max_size** = `65532` `🔗<class_PacketPeerStream_property_input_buffer_max_size>`

classref-property-setget

- `void (No return value.)` **set_input_buffer_max_size**(value: `int<class_int>`)
- `int<class_int>` **get_input_buffer_max_size**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`int<class_int>` **output_buffer_max_size** = `65532` `🔗<class_PacketPeerStream_property_output_buffer_max_size>`

classref-property-setget

- `void (No return value.)` **set_output_buffer_max_size**(value: `int<class_int>`)
- `int<class_int>` **get_output_buffer_max_size**()

There is currently no description for this property. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-property

`StreamPeer<class_StreamPeer>` **stream_peer** `🔗<class_PacketPeerStream_property_stream_peer>`

classref-property-setget

- `void (No return value.)` **set_stream_peer**(value: `StreamPeer<class_StreamPeer>`)
- `StreamPeer<class_StreamPeer>` **get_stream_peer**()

The wrapped `StreamPeer<class_StreamPeer>` object.