github_url
hide

# WebRTCDataChannel

**Inherits:** `PacketPeer<class_PacketPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `WebRTCDataChannelExtension<class_WebRTCDataChannelExtension>`

There is currently no description for this class. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **WriteMode**: `🔗<enum_WebRTCDataChannel_WriteMode>`

classref-enumeration-constant

`WriteMode<enum_WebRTCDataChannel_WriteMode>` **WRITE_MODE_TEXT** = `0`

Tells the channel to send data over this channel as text. An external peer (non-Godot) would receive this as a string.

classref-enumeration-constant

`WriteMode<enum_WebRTCDataChannel_WriteMode>` **WRITE_MODE_BINARY** = `1`

Tells the channel to send data over this channel as binary. An external peer (non-Godot) would receive this as array buffer or blob.

classref-item-separator

classref-enumeration

enum **ChannelState**: `🔗<enum_WebRTCDataChannel_ChannelState>`

classref-enumeration-constant

`ChannelState<enum_WebRTCDataChannel_ChannelState>` **STATE_CONNECTING** = `0`

The channel was created, but it's still trying to connect.

classref-enumeration-constant

`ChannelState<enum_WebRTCDataChannel_ChannelState>` **STATE_OPEN** = `1`

The channel is currently open, and data can flow over it.

classref-enumeration-constant

`ChannelState<enum_WebRTCDataChannel_ChannelState>` **STATE_CLOSING** = `2`

The channel is being closed, no new messages will be accepted, but those already in queue will be flushed.

classref-enumeration-constant

`ChannelState<enum_WebRTCDataChannel_ChannelState>` **STATE_CLOSED** = `3`

The channel was closed, or connection failed.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`WriteMode<enum_WebRTCDataChannel_WriteMode>` **write_mode** = `1` `🔗<class_WebRTCDataChannel_property_write_mode>`

classref-property-setget

- `void (No return value.)` **set_write_mode**(value: `WriteMode<enum_WebRTCDataChannel_WriteMode>`)
- `WriteMode<enum_WebRTCDataChannel_WriteMode>` **get_write_mode**()

The transfer mode to use when sending outgoing packet. Either text or binary.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **close**() `🔗<class_WebRTCDataChannel_method_close>`

Closes this data channel, notifying the other peer.

classref-item-separator

classref-method

`int<class_int>` **get_buffered_amount**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_buffered_amount>`

Returns the number of bytes currently queued to be sent over this channel.

classref-item-separator

classref-method

`int<class_int>` **get_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_id>`

Returns the ID assigned to this channel during creation (or auto-assigned during negotiation).

If the channel is not negotiated out-of-band the ID will only be available after the connection is established (will return `65535` until then).

classref-item-separator

classref-method

`String<class_String>` **get_label**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_label>`

Returns the label assigned to this channel during creation.

classref-item-separator

classref-method

`int<class_int>` **get_max_packet_life_time**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_max_packet_life_time>`

Returns the `maxPacketLifeTime` value assigned to this channel during creation.

Will be `65535` if not specified.

classref-item-separator

classref-method

`int<class_int>` **get_max_retransmits**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_max_retransmits>`

Returns the `maxRetransmits` value assigned to this channel during creation.

Will be `65535` if not specified.

classref-item-separator

classref-method

`String<class_String>` **get_protocol**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_protocol>`

Returns the sub-protocol assigned to this channel during creation. An empty string if not specified.

classref-item-separator

classref-method

`ChannelState<enum_WebRTCDataChannel_ChannelState>` **get_ready_state**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_get_ready_state>`

Returns the current state of this channel.

classref-item-separator

classref-method

`bool<class_bool>` **is_negotiated**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_is_negotiated>`

Returns `true` if this channel was created with out-of-band configuration.

classref-item-separator

classref-method

`bool<class_bool>` **is_ordered**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_is_ordered>`

Returns `true` if this channel was created with ordering enabled (default).

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **poll**() `🔗<class_WebRTCDataChannel_method_poll>`

Reserved, but not used for now.

classref-item-separator

classref-method

`bool<class_bool>` **was_string_packet**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_WebRTCDataChannel_method_was_string_packet>`

Returns `true` if the last received packet was transferred as text. See `write_mode<class_WebRTCDataChannel_property_write_mode>`.