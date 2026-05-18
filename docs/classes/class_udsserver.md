github_url
hide

# UDSServer

**Inherits:** `SocketServer<class_SocketServer>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A Unix Domain Socket (UDS) server.

classref-introduction-group

## Description

A Unix Domain Socket (UDS) server. Listens to connections on a socket path and returns a `StreamPeerUDS<class_StreamPeerUDS>` when it gets an incoming connection. Unix Domain Sockets provide inter-process communication on the same machine using the filesystem namespace.

**Note:** Unix Domain Sockets are only available on Unix-like systems (Linux, macOS, etc.) and are not supported on Windows.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Error<enum_@GlobalScope_Error>` **listen**(path: `String<class_String>`) `🔗<class_UDSServer_method_listen>`

Listens on the socket at `path`. The socket file will be created at the specified path.

**Note:** The socket file must not already exist at the specified path. You may need to remove any existing socket file before calling this method.

classref-item-separator

classref-method

`StreamPeerUDS<class_StreamPeerUDS>` **take_connection**() `🔗<class_UDSServer_method_take_connection>`

If a connection is available, returns a StreamPeerUDS with the connection.