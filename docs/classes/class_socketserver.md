github_url
hide

# SocketServer

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `TCPServer<class_TCPServer>`, `UDSServer<class_UDSServer>`

An abstract class for servers based on sockets.

classref-introduction-group

## Description

A socket server.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_connection_available**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SocketServer_method_is_connection_available>`

Returns `true` if a connection is available for taking.

classref-item-separator

classref-method

`bool<class_bool>` **is_listening**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SocketServer_method_is_listening>`

Returns `true` if the server is currently listening for connections.

classref-item-separator

classref-method

`void (No return value.)` **stop**() `🔗<class_SocketServer_method_stop>`

Stops listening.

classref-item-separator

classref-method

`StreamPeerSocket<class_StreamPeerSocket>` **take_socket_connection**() `🔗<class_SocketServer_method_take_socket_connection>`

If a connection is available, returns a StreamPeerSocket with the connection.