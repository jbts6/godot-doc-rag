github_url
hide

# HMACContext

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Used to create an HMAC for a message using a key.

classref-introduction-group

## Description

The HMACContext class is useful for advanced HMAC use cases, such as streaming the message as it supports creating the message over time rather than providing it all at once.

gdscript

extends Node var ctx = HMACContext.new()

func ready():
var key = "supersecret".to_utf8_buffer() var err = ctx.start(HashingContext.HASH_SHA256, key) assert(err == OK) var msg1 = "this is ".to_utf8_buffer() var msg2 = "super duper secret".to_utf8_buffer() err = ctx.update(msg1) assert(err == OK) err = ctx.update(msg2) assert(err == OK) var hmac = ctx.finish() print(hmac.hex_encode())

csharp

using Godot; using System.Diagnostics;

public partial class MyNode : Node { private HmacContext ctx = new HmacContext();

> public override void Ready() { byte\[\] key = "supersecret".ToUtf8Buffer(); Error err = ctx.Start(HashingContext.HashType.Sha256, key); Debug.Assert(err == Error.Ok); byte\[\] msg1 = "this is ".ToUtf8Buffer(); byte\[\] msg2 = "super duper secret".ToUtf8Buffer(); err = ctx.Update(msg1); Debug.Assert(err == Error.Ok); err = ctx.Update(msg2); Debug.Assert(err == Error.Ok); byte\[\] hmac = ctx.Finish(); GD.Print(hmac.HexEncode()); }

}

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`PackedByteArray<class_PackedByteArray>` **finish**() `🔗<class_HMACContext_method_finish>`

Returns the resulting HMAC. If the HMAC failed, an empty `PackedByteArray<class_PackedByteArray>` is returned.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **start**(hash_type: `HashType<enum_HashingContext_HashType>`, key: `PackedByteArray<class_PackedByteArray>`) `🔗<class_HMACContext_method_start>`

Initializes the HMACContext. This method cannot be called again on the same HMACContext until `finish()<class_HMACContext_method_finish>` has been called.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **update**(data: `PackedByteArray<class_PackedByteArray>`) `🔗<class_HMACContext_method_update>`

Updates the message to be HMACed. This can be called multiple times before `finish()<class_HMACContext_method_finish>` is called to append `data` to the message, but cannot be called until `start()<class_HMACContext_method_start>` has been called.