github_url
hide

# PacketPeer

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `ENetPacketPeer<class_ENetPacketPeer>`, `MultiplayerPeer<class_MultiplayerPeer>`, `PacketPeerDTLS<class_PacketPeerDTLS>`, `PacketPeerExtension<class_PacketPeerExtension>`, `PacketPeerStream<class_PacketPeerStream>`, `PacketPeerUDP<class_PacketPeerUDP>`, `WebRTCDataChannel<class_WebRTCDataChannel>`, `WebSocketPeer<class_WebSocketPeer>`

Abstraction and base class for packet-based protocols.

classref-introduction-group

## Description

PacketPeer is an abstraction and base class for packet-based protocols (such as UDP). It provides an API for sending and receiving packets both as raw data or variables. This makes it easy to transfer data over a protocol, without having to encode data as low-level bytes or having to worry about network ordering.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **encode_buffer_max_size** = `8388608` `🔗<class_PacketPeer_property_encode_buffer_max_size>`

classref-property-setget

- `void (No return value.)` **set_encode_buffer_max_size**(value: `int<class_int>`)
- `int<class_int>` **get_encode_buffer_max_size**()

Maximum buffer size allowed when encoding `Variant<class_Variant>`s. Raise this value to support heavier memory allocations.

The `put_var()<class_PacketPeer_method_put_var>` method allocates memory on the stack, and the buffer used will grow automatically to the closest power of two to match the size of the `Variant<class_Variant>`. If the `Variant<class_Variant>` is bigger than `encode_buffer_max_size<class_PacketPeer_property_encode_buffer_max_size>`, the method will error out with `@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_available_packet_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PacketPeer_method_get_available_packet_count>`

Returns the number of packets currently available in the ring-buffer.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **get_packet**() `🔗<class_PacketPeer_method_get_packet>`

Gets a raw packet.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **get_packet_error**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PacketPeer_method_get_packet_error>`

Returns the error state of the last packet received (via `get_packet()<class_PacketPeer_method_get_packet>` and `get_var()<class_PacketPeer_method_get_var>`).

classref-item-separator

classref-method

`Variant<class_Variant>` **get_var**(allow_objects: `bool<class_bool>` = false) `🔗<class_PacketPeer_method_get_var>`

Gets a Variant. If `allow_objects` is `true`, decoding objects is allowed.

Internally, this uses the same decoding mechanism as the `@GlobalScope.bytes_to_var()<class_@GlobalScope_method_bytes_to_var>` method.

**Warning:** Deserialized objects can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats such as remote code execution.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **put_packet**(buffer: `PackedByteArray<class_PackedByteArray>`) `🔗<class_PacketPeer_method_put_packet>`

Sends a raw packet.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **put_var**(var: `Variant<class_Variant>`, full_objects: `bool<class_bool>` = false) `🔗<class_PacketPeer_method_put_var>`

Sends a `Variant<class_Variant>` as a packet. If `full_objects` is `true`, encoding objects is allowed (and can potentially include code).

Internally, this uses the same encoding mechanism as the `@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>` method.