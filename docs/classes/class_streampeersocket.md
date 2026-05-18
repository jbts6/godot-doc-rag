github_url
hide

# StreamPeerSocket

**Inherits:** `StreamPeer<class_StreamPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `StreamPeerTCP<class_StreamPeerTCP>`, `StreamPeerUDS<class_StreamPeerUDS>`

Abstract base class for interacting with socket streams.

classref-introduction-group

## Description

StreamPeerSocket is an abstract base class that defines common behavior for socket-based streams.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Status**: `🔗<enum_StreamPeerSocket_Status>`

classref-enumeration-constant

`Status<enum_StreamPeerSocket_Status>` **STATUS_NONE** = `0`

The initial status of the **StreamPeerSocket**. This is also the status after disconnecting.

classref-enumeration-constant

`Status<enum_StreamPeerSocket_Status>` **STATUS_CONNECTING** = `1`

A status representing a **StreamPeerSocket** that is connecting to a host.

classref-enumeration-constant

`Status<enum_StreamPeerSocket_Status>` **STATUS_CONNECTED** = `2`

A status representing a **StreamPeerSocket** that is connected to a host.

classref-enumeration-constant

`Status<enum_StreamPeerSocket_Status>` **STATUS_ERROR** = `3`

A status representing a **StreamPeerSocket** in error state.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **disconnect_from_host**() `🔗<class_StreamPeerSocket_method_disconnect_from_host>`

Disconnects from host.

classref-item-separator

classref-method

`Status<enum_StreamPeerSocket_Status>` **get_status**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StreamPeerSocket_method_get_status>`

Returns the status of the connection.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **poll**() `🔗<class_StreamPeerSocket_method_poll>`

Polls the socket, updating its state. See `get_status()<class_StreamPeerSocket_method_get_status>`.