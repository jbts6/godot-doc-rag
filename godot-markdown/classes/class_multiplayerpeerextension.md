github_url
hide

# MultiplayerPeerExtension

**Inherits:** `MultiplayerPeer<class_MultiplayerPeer>` **\<** `PacketPeer<class_PacketPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Class that can be inherited to implement custom multiplayer API networking layers via GDExtension.

classref-introduction-group

## Description

This class is designed to be inherited from a GDExtension plugin to implement custom networking layers for the multiplayer API (such as WebRTC). All the methods below **must** be implemented to have a working custom multiplayer implementation. See also `MultiplayerAPI<class_MultiplayerAPI>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_close**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_MultiplayerPeerExtension_private_method__close>`

Called when the multiplayer peer should be immediately closed (see `MultiplayerPeer.close()<class_MultiplayerPeer_method_close>`).

classref-item-separator

classref-method

`void (No return value.)` **\_disconnect_peer**(peer: `int<class_int>`, force: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_MultiplayerPeerExtension_private_method__disconnect_peer>`

Called when the connected `peer` should be forcibly disconnected (see `MultiplayerPeer.disconnect_peer()<class_MultiplayerPeer_method_disconnect_peer>`).

classref-item-separator

classref-method

`int<class_int>` **\_get_available_packet_count**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_available_packet_count>`

Called when the available packet count is internally requested by the `MultiplayerAPI<class_MultiplayerAPI>`.

classref-item-separator

classref-method

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>` **\_get_connection_status**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_connection_status>`

Called when the connection status is requested on the `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.get_connection_status()<class_MultiplayerPeer_method_get_connection_status>`).

classref-item-separator

classref-method

`int<class_int>` **\_get_max_packet_size**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_max_packet_size>`

Called when the maximum allowed packet size (in bytes) is requested by the `MultiplayerAPI<class_MultiplayerAPI>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_get_packet**(r_buffer: `const uint8_t **`, r_buffer_size: `int32_t*`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_MultiplayerPeerExtension_private_method__get_packet>`

Called when a packet needs to be received by the `MultiplayerAPI<class_MultiplayerAPI>`, with `r_buffer_size` being the size of the binary `r_buffer` in bytes.

classref-item-separator

classref-method

`int<class_int>` **\_get_packet_channel**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_packet_channel>`

Called to get the channel over which the next available packet was received. See `MultiplayerPeer.get_packet_channel()<class_MultiplayerPeer_method_get_packet_channel>`.

classref-item-separator

classref-method

`TransferMode<enum_MultiplayerPeer_TransferMode>` **\_get_packet_mode**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_packet_mode>`

Called to get the transfer mode the remote peer used to send the next available packet. See `MultiplayerPeer.get_packet_mode()<class_MultiplayerPeer_method_get_packet_mode>`.

classref-item-separator

classref-method

`int<class_int>` **\_get_packet_peer**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_packet_peer>`

Called when the ID of the `MultiplayerPeer<class_MultiplayerPeer>` who sent the most recent packet is requested (see `MultiplayerPeer.get_packet_peer()<class_MultiplayerPeer_method_get_packet_peer>`).

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **\_get_packet_script**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_MultiplayerPeerExtension_private_method__get_packet_script>`

Called when a packet needs to be received by the `MultiplayerAPI<class_MultiplayerAPI>`, if `_get_packet()<class_MultiplayerPeerExtension_private_method__get_packet>` isn't implemented. Use this when extending this class via GDScript.

classref-item-separator

classref-method

`int<class_int>` **\_get_transfer_channel**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_transfer_channel>`

Called when the transfer channel to use is read on this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.transfer_channel<class_MultiplayerPeer_property_transfer_channel>`).

classref-item-separator

classref-method

`TransferMode<enum_MultiplayerPeer_TransferMode>` **\_get_transfer_mode**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_transfer_mode>`

Called when the transfer mode to use is read on this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.transfer_mode<class_MultiplayerPeer_property_transfer_mode>`).

classref-item-separator

classref-method

`int<class_int>` **\_get_unique_id**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__get_unique_id>`

Called when the unique ID of this `MultiplayerPeer<class_MultiplayerPeer>` is requested (see `MultiplayerPeer.get_unique_id()<class_MultiplayerPeer_method_get_unique_id>`). The value must be between `1` and `2147483647`.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_refusing_new_connections**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__is_refusing_new_connections>`

Called when the "refuse new connections" status is requested on this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.refuse_new_connections<class_MultiplayerPeer_property_refuse_new_connections>`).

classref-item-separator

classref-method

`bool<class_bool>` **\_is_server**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__is_server>`

Called when the "is server" status is requested on the `MultiplayerAPI<class_MultiplayerAPI>`. See `MultiplayerAPI.is_server()<class_MultiplayerAPI_method_is_server>`.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_server_relay_supported**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeerExtension_private_method__is_server_relay_supported>`

Called to check if the server can act as a relay in the current configuration. See `MultiplayerPeer.is_server_relay_supported()<class_MultiplayerPeer_method_is_server_relay_supported>`.

classref-item-separator

classref-method

`void (No return value.)` **\_poll**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_MultiplayerPeerExtension_private_method__poll>`

Called when the `MultiplayerAPI<class_MultiplayerAPI>` is polled. See `MultiplayerAPI.poll()<class_MultiplayerAPI_method_poll>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_put_packet**(buffer: `const uint8_t*`, buffer_size: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_MultiplayerPeerExtension_private_method__put_packet>`

Called when a packet needs to be sent by the `MultiplayerAPI<class_MultiplayerAPI>`, with `buffer_size` being the size of the binary `buffer` in bytes.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **\_put_packet_script**(buffer: `PackedByteArray<class_PackedByteArray>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_MultiplayerPeerExtension_private_method__put_packet_script>`

Called when a packet needs to be sent by the `MultiplayerAPI<class_MultiplayerAPI>`, if `_put_packet()<class_MultiplayerPeerExtension_private_method__put_packet>` isn't implemented. Use this when extending this class via GDScript.

classref-item-separator

classref-method

`void (No return value.)` **\_set_refuse_new_connections**(enable: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_MultiplayerPeerExtension_private_method__set_refuse_new_connections>`

Called when the "refuse new connections" status is set on this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.refuse_new_connections<class_MultiplayerPeer_property_refuse_new_connections>`).

classref-item-separator

classref-method

`void (No return value.)` **\_set_target_peer**(peer: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_MultiplayerPeerExtension_private_method__set_target_peer>`

Called when the target peer to use is set for this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.set_target_peer()<class_MultiplayerPeer_method_set_target_peer>`).

classref-item-separator

classref-method

`void (No return value.)` **\_set_transfer_channel**(channel: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_MultiplayerPeerExtension_private_method__set_transfer_channel>`

Called when the channel to use is set for this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.transfer_channel<class_MultiplayerPeer_property_transfer_channel>`).

classref-item-separator

classref-method

`void (No return value.)` **\_set_transfer_mode**(mode: `TransferMode<enum_MultiplayerPeer_TransferMode>`) `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_MultiplayerPeerExtension_private_method__set_transfer_mode>`

Called when the transfer mode is set on this `MultiplayerPeer<class_MultiplayerPeer>` (see `MultiplayerPeer.transfer_mode<class_MultiplayerPeer_property_transfer_mode>`).