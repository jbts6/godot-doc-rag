github_url
hide

# X509Certificate

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

An X509 certificate (e.g. for TLS).

classref-introduction-group

## Description

The X509Certificate class represents an X509 certificate. Certificates can be loaded and saved like any other `Resource<class_Resource>`.

They can be used as the server certificate in `StreamPeerTLS.accept_stream()<class_StreamPeerTLS_method_accept_stream>` (along with the proper `CryptoKey<class_CryptoKey>`), and to specify the only certificate that should be accepted when connecting to a TLS server via `StreamPeerTLS.connect_to_stream()<class_StreamPeerTLS_method_connect_to_stream>`.

classref-introduction-group

## Tutorials

- `SSL certificates <../tutorials/networking/ssl_certificates>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Error<enum_@GlobalScope_Error>` **load**(path: `String<class_String>`) `🔗<class_X509Certificate_method_load>`

Loads a certificate from `path` ("\*.crt" file).

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **load_from_string**(string: `String<class_String>`) `🔗<class_X509Certificate_method_load_from_string>`

Loads a certificate from the given `string`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **save**(path: `String<class_String>`) `🔗<class_X509Certificate_method_save>`

Saves a certificate to the given `path` (should be a "\*.crt" file).

classref-item-separator

classref-method

`String<class_String>` **save_to_string**() `🔗<class_X509Certificate_method_save_to_string>`

Returns a string representation of the certificate, or an empty string if the certificate is invalid.