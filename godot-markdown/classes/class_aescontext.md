github_url
hide

# AESContext

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Provides access to AES encryption/decryption of raw data.

classref-introduction-group

## Description

This class holds the context information required for encryption and decryption operations with AES (Advanced Encryption Standard). Both AES-ECB and AES-CBC modes are supported.

gdscript

extends Node

var aes = AESContext.new()

func ready():
var key = "My secret key!!!" \# Key must be either 16 or 32 bytes. var data = "My secret text!!" \# Data size must be multiple of 16 bytes, apply padding if needed. \# Encrypt ECB aes.start(AESContext.MODE_ECB_ENCRYPT, key.to_utf8_buffer()) var encrypted = aes.update(data.to_utf8_buffer()) aes.finish() \# Decrypt ECB aes.start(AESContext.MODE_ECB_DECRYPT, key.to_utf8_buffer()) var decrypted = aes.update(encrypted) aes.finish() \# Check ECB assert(decrypted == data.to_utf8_buffer())

var iv = "My secret iv!!!!" \# IV must be of exactly 16 bytes. \# Encrypt CBC aes.start(AESContext.MODE_CBC_ENCRYPT, key.to_utf8_buffer(), iv.to_utf8_buffer()) encrypted = aes.update(data.to_utf8_buffer()) aes.finish() \# Decrypt CBC aes.start(AESContext.MODE_CBC_DECRYPT, key.to_utf8_buffer(), iv.to_utf8_buffer()) decrypted = aes.update(encrypted) aes.finish() \# Check CBC assert(decrypted == data.to_utf8_buffer())

csharp

using Godot; using System.Diagnostics;

public partial class MyNode : Node { private AesContext aes = new AesContext();

> public override void Ready() { string key = "My secret key!!!"; // Key must be either 16 or 32 bytes. string data = "My secret text!!"; // Data size must be multiple of 16 bytes, apply padding if needed. // Encrypt ECB aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer()); byte\[\] encrypted = aes.Update(data.ToUtf8Buffer()); aes.Finish(); // Decrypt ECB aes.Start(AesContext.Mode.EcbDecrypt, key.ToUtf8Buffer()); byte\[\] decrypted = aes.Update(encrypted); aes.Finish(); // Check ECB Debug.Assert(decrypted == data.ToUtf8Buffer());
>
> > string iv = "My secret iv!!!!"; // IV must be of exactly 16 bytes. // Encrypt CBC aes.Start(AesContext.Mode.EcbEncrypt, key.ToUtf8Buffer(), iv.ToUtf8Buffer()); encrypted = aes.Update(data.ToUtf8Buffer()); aes.Finish(); // Decrypt CBC aes.Start(AesContext.Mode.EcbDecrypt, key.ToUtf8Buffer(), iv.ToUtf8Buffer()); decrypted = aes.Update(encrypted); aes.Finish(); // Check CBC Debug.Assert(decrypted == data.ToUtf8Buffer());
>
> }

}

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Mode**: `🔗<enum_AESContext_Mode>`

classref-enumeration-constant

`Mode<enum_AESContext_Mode>` **MODE_ECB_ENCRYPT** = `0`

AES electronic codebook encryption mode.

classref-enumeration-constant

`Mode<enum_AESContext_Mode>` **MODE_ECB_DECRYPT** = `1`

AES electronic codebook decryption mode.

classref-enumeration-constant

`Mode<enum_AESContext_Mode>` **MODE_CBC_ENCRYPT** = `2`

AES cipher block chaining encryption mode.

classref-enumeration-constant

`Mode<enum_AESContext_Mode>` **MODE_CBC_DECRYPT** = `3`

AES cipher block chaining decryption mode.

classref-enumeration-constant

`Mode<enum_AESContext_Mode>` **MODE_MAX** = `4`

Maximum value for the mode enum.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **finish**() `🔗<class_AESContext_method_finish>`

Close this AES context so it can be started again. See `start()<class_AESContext_method_start>`.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **get_iv_state**() `🔗<class_AESContext_method_get_iv_state>`

Get the current IV state for this context (IV gets updated when calling `update()<class_AESContext_method_update>`). You normally don't need this function.

**Note:** This function only makes sense when the context is started with `MODE_CBC_ENCRYPT<class_AESContext_constant_MODE_CBC_ENCRYPT>` or `MODE_CBC_DECRYPT<class_AESContext_constant_MODE_CBC_DECRYPT>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **start**(mode: `Mode<enum_AESContext_Mode>`, key: `PackedByteArray<class_PackedByteArray>`, iv: `PackedByteArray<class_PackedByteArray>` = PackedByteArray()) `🔗<class_AESContext_method_start>`

Start the AES context in the given `mode`. A `key` of either 16 or 32 bytes must always be provided, while an `iv` (initialization vector) of exactly 16 bytes, is only needed when `mode` is either `MODE_CBC_ENCRYPT<class_AESContext_constant_MODE_CBC_ENCRYPT>` or `MODE_CBC_DECRYPT<class_AESContext_constant_MODE_CBC_DECRYPT>`.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **update**(src: `PackedByteArray<class_PackedByteArray>`) `🔗<class_AESContext_method_update>`

Run the desired operation for this AES context. Will return a `PackedByteArray<class_PackedByteArray>` containing the result of encrypting (or decrypting) the given `src`. See `start()<class_AESContext_method_start>` for mode of operation.

**Note:** The size of `src` must be a multiple of 16. Apply some padding if needed.