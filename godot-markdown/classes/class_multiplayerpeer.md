github_url
hide

# MultiplayerPeer

**Inherits:** `PacketPeer<class_PacketPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `ENetMultiplayerPeer<class_ENetMultiplayerPeer>`, `MultiplayerPeerExtension<class_MultiplayerPeerExtension>`, `OfflineMultiplayerPeer<class_OfflineMultiplayerPeer>`, `WebRTCMultiplayerPeer<class_WebRTCMultiplayerPeer>`, `WebSocketMultiplayerPeer<class_WebSocketMultiplayerPeer>`

Abstract class for specialized `PacketPeer<class_PacketPeer>`s used by the `MultiplayerAPI<class_MultiplayerAPI>`.

classref-introduction-group

## Description

Manages the connection with one or more remote peers acting as server or client and assigning unique IDs to each of them. See also `MultiplayerAPI<class_MultiplayerAPI>`.

**Note:** The `MultiplayerAPI<class_MultiplayerAPI>` protocol is an implementation detail and isn't meant to be used by non-Godot servers. It may change without notice.

**Note:** When exporting to Android, make sure to enable the `INTERNET` permission in the Android export preset before exporting the project or using one-click deploy. Otherwise, network communication of any kind will be blocked by Android.

classref-introduction-group

## Tutorials

- `High-level multiplayer <../tutorials/networking/high_level_multiplayer>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**peer_connected**(id: `int<class_int>`) `🔗<class_MultiplayerPeer_signal_peer_connected>`

Emitted when a remote peer connects.

classref-item-separator

classref-signal

**peer_disconnected**(id: `int<class_int>`) `🔗<class_MultiplayerPeer_signal_peer_disconnected>`

Emitted when a remote peer has disconnected.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ConnectionStatus**: `🔗<enum_MultiplayerPeer_ConnectionStatus>`

classref-enumeration-constant

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>` **CONNECTION_DISCONNECTED** = `0`

The MultiplayerPeer is disconnected.

classref-enumeration-constant

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>` **CONNECTION_CONNECTING** = `1`

The MultiplayerPeer is currently connecting to a server.

classref-enumeration-constant

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>` **CONNECTION_CONNECTED** = `2`

This MultiplayerPeer is connected.

classref-item-separator

classref-enumeration

enum **TransferMode**: `🔗<enum_MultiplayerPeer_TransferMode>`

classref-enumeration-constant

`TransferMode<enum_MultiplayerPeer_TransferMode>` **TRANSFER_MODE_UNRELIABLE** = `0`

Packets are not acknowledged, no resend attempts are made for lost packets. Packets may arrive in any order. Potentially faster than `TRANSFER_MODE_UNRELIABLE_ORDERED<class_MultiplayerPeer_constant_TRANSFER_MODE_UNRELIABLE_ORDERED>`. Use for non-critical data, and always consider whether the order matters.

classref-enumeration-constant

`TransferMode<enum_MultiplayerPeer_TransferMode>` **TRANSFER_MODE_UNRELIABLE_ORDERED** = `1`

Packets are not acknowledged, no resend attempts are made for lost packets. Packets are received in the order they were sent in. Potentially faster than `TRANSFER_MODE_RELIABLE<class_MultiplayerPeer_constant_TRANSFER_MODE_RELIABLE>`. Use for non-critical data or data that would be outdated if received late due to resend attempt(s) anyway, for example movement and positional data.

classref-enumeration-constant

`TransferMode<enum_MultiplayerPeer_TransferMode>` **TRANSFER_MODE_RELIABLE** = `2`

Packets must be received and resend attempts should be made until the packets are acknowledged. Packets must be received in the order they were sent in. Most reliable transfer mode, but potentially the slowest due to the overhead. Use for critical data that must be transmitted and arrive in order, for example an ability being triggered or a chat message. Consider carefully if the information really is critical, and use sparingly.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**TARGET_PEER_BROADCAST** = `0` `🔗<class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST>`

Packets are sent to all connected peers.

classref-constant

**TARGET_PEER_SERVER** = `1` `🔗<class_MultiplayerPeer_constant_TARGET_PEER_SERVER>`

Packets are sent to the remote peer acting as server.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **refuse_new_connections** = `false` `🔗<class_MultiplayerPeer_property_refuse_new_connections>`

classref-property-setget

- `void (No return value.)` **set_refuse_new_connections**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_refusing_new_connections**()

If `true`, this **MultiplayerPeer** refuses new connections.

classref-item-separator

classref-property

`int<class_int>` **transfer_channel** = `0` `🔗<class_MultiplayerPeer_property_transfer_channel>`

classref-property-setget

- `void (No return value.)` **set_transfer_channel**(value: `int<class_int>`)
- `int<class_int>` **get_transfer_channel**()

The channel to use to send packets. Many network APIs such as ENet and WebRTC allow the creation of multiple independent channels which behaves, in a way, like separate connections. This means that reliable data will only block delivery of other packets on that channel, and ordering will only be in respect to the channel the packet is being sent on. Using different channels to send **different and independent** state updates is a common way to optimize network usage and decrease latency in fast-paced games.

**Note:** The default channel (`0`) actually works as 3 separate channels (one for each `TransferMode<enum_MultiplayerPeer_TransferMode>`) so that `TRANSFER_MODE_RELIABLE<class_MultiplayerPeer_constant_TRANSFER_MODE_RELIABLE>` and `TRANSFER_MODE_UNRELIABLE_ORDERED<class_MultiplayerPeer_constant_TRANSFER_MODE_UNRELIABLE_ORDERED>` does not interact with each other by default. Refer to the specific network API documentation (e.g. ENet or WebRTC) to learn how to set up channels correctly.

classref-item-separator

classref-property

`TransferMode<enum_MultiplayerPeer_TransferMode>` **transfer_mode** = `2` `🔗<class_MultiplayerPeer_property_transfer_mode>`

classref-property-setget

- `void (No return value.)` **set_transfer_mode**(value: `TransferMode<enum_MultiplayerPeer_TransferMode>`)
- `TransferMode<enum_MultiplayerPeer_TransferMode>` **get_transfer_mode**()

The manner in which to send packets to the target peer. See the `set_target_peer()<class_MultiplayerPeer_method_set_target_peer>` method.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **close**() `🔗<class_MultiplayerPeer_method_close>`

Immediately close the multiplayer peer returning to the state `CONNECTION_DISCONNECTED<class_MultiplayerPeer_constant_CONNECTION_DISCONNECTED>`. Connected peers will be dropped without emitting `peer_disconnected<class_MultiplayerPeer_signal_peer_disconnected>`.

classref-item-separator

classref-method

`void (No return value.)` **disconnect_peer**(peer: `int<class_int>`, force: `bool<class_bool>` = false) `🔗<class_MultiplayerPeer_method_disconnect_peer>`

Disconnects the given `peer` from this host. If `force` is `true` the `peer_disconnected<class_MultiplayerPeer_signal_peer_disconnected>` signal will not be emitted for this peer.

classref-item-separator

classref-method

`int<class_int>` **generate_unique_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_generate_unique_id>`

Returns a randomly generated integer that can be used as a network unique ID.

classref-item-separator

classref-method

`ConnectionStatus<enum_MultiplayerPeer_ConnectionStatus>` **get_connection_status**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_get_connection_status>`

Returns the current state of the connection.

classref-item-separator

classref-method

`int<class_int>` **get_packet_channel**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_get_packet_channel>`

Returns the channel over which the next available packet was received. See `PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`.

classref-item-separator

classref-method

`TransferMode<enum_MultiplayerPeer_TransferMode>` **get_packet_mode**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_get_packet_mode>`

Returns the transfer mode the remote peer used to send the next available packet. See `PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`.

classref-item-separator

classref-method

`int<class_int>` **get_packet_peer**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_get_packet_peer>`

Returns the ID of the **MultiplayerPeer** who sent the next available packet. See `PacketPeer.get_available_packet_count()<class_PacketPeer_method_get_available_packet_count>`.

classref-item-separator

classref-method

`int<class_int>` **get_unique_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_get_unique_id>`

Returns the ID of this **MultiplayerPeer**.

classref-item-separator

classref-method

`bool<class_bool>` **is_server_relay_supported**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_MultiplayerPeer_method_is_server_relay_supported>`

Returns `true` if the server can act as a relay in the current configuration. That is, if the higher level `MultiplayerAPI<class_MultiplayerAPI>` should notify connected clients of other peers, and implement a relay protocol to allow communication between them.

classref-item-separator

classref-method

`void (No return value.)` **poll**() `🔗<class_MultiplayerPeer_method_poll>`

Waits up to 1 second to receive a new network event.

classref-item-separator

classref-method

`void (No return value.)` **set_target_peer**(id: `int<class_int>`) `🔗<class_MultiplayerPeer_method_set_target_peer>`

Sets the peer to which packets will be sent.

The `id` can be one of: `TARGET_PEER_BROADCAST<class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST>` to send to all connected peers, `TARGET_PEER_SERVER<class_MultiplayerPeer_constant_TARGET_PEER_SERVER>` to send to the peer acting as server, a valid peer ID to send to that specific peer, a negative peer ID to send to all peers except that one. By default, the target peer is `TARGET_PEER_BROADCAST<class_MultiplayerPeer_constant_TARGET_PEER_BROADCAST>`.