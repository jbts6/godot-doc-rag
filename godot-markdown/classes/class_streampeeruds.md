github_url
hide

# StreamPeerUDS

**Inherits:** `StreamPeerSocket<class_StreamPeerSocket>` **\<** `StreamPeer<class_StreamPeer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A stream peer that handles UNIX Domain Socket (UDS) connections.

classref-introduction-group

## Description

A stream peer that handles UNIX Domain Socket (UDS) connections. This object can be used to connect to UDS servers, or also is returned by a UDS server. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Note:** UNIX Domain Sockets are only available on UNIX-like systems (Linux, macOS, etc.) and are not supported on Windows.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Error<enum_@GlobalScope_Error>` **bind**(path: `String<class_String>`) `🔗<class_StreamPeerUDS_method_bind>`

Opens the UDS socket, and binds it to the specified socket path.

This method is generally not needed, and only used to force the subsequent call to `connect_to_host()<class_StreamPeerUDS_method_connect_to_host>` to use the specified `path` as the source address.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **connect_to_host**(path: `String<class_String>`) `🔗<class_StreamPeerUDS_method_connect_to_host>`

Connects to the specified UNIX Domain Socket path. Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success.

classref-item-separator

classref-method

`String<class_String>` **get_connected_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_StreamPeerUDS_method_get_connected_path>`

Returns the socket path of this peer.