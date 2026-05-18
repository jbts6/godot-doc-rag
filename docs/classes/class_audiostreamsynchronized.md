github_url
hide

# AudioStreamSynchronized

**Inherits:** `AudioStream<class_AudioStream>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Stream that can be fitted with sub-streams, which will be played in-sync.

classref-introduction-group

## Description

This is a stream that can be fitted with sub-streams, which will be played in-sync. The streams begin at exactly the same time when play is pressed, and will end when the last of them ends. If one of the sub-streams loops, then playback will continue.

classref-introduction-group

## Tutorials

- `Audio streams <../tutorials/audio/audio_streams>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**MAX_STREAMS** = `32` `🔗<class_AudioStreamSynchronized_constant_MAX_STREAMS>`

Maximum amount of streams that can be synchronized.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **stream_count** = `0` `🔗<class_AudioStreamSynchronized_property_stream_count>`

classref-property-setget

- `void (No return value.)` **set_stream_count**(value: `int<class_int>`)
- `int<class_int>` **get_stream_count**()

Set the total amount of streams that will be played back synchronized.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AudioStream<class_AudioStream>` **get_sync_stream**(stream_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamSynchronized_method_get_sync_stream>`

Get one of the synchronized streams, by index.

classref-item-separator

classref-method

`float<class_float>` **get_sync_stream_volume**(stream_index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioStreamSynchronized_method_get_sync_stream_volume>`

Get the volume of one of the synchronized streams, by index.

classref-item-separator

classref-method

`void (No return value.)` **set_sync_stream**(stream_index: `int<class_int>`, audio_stream: `AudioStream<class_AudioStream>`) `🔗<class_AudioStreamSynchronized_method_set_sync_stream>`

Set one of the synchronized streams, by index.

classref-item-separator

classref-method

`void (No return value.)` **set_sync_stream_volume**(stream_index: `int<class_int>`, volume_db: `float<class_float>`) `🔗<class_AudioStreamSynchronized_method_set_sync_stream_volume>`

Set the volume of one of the synchronized streams, by index.