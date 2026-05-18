github_url
hide

# OggPacketSequence

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A sequence of Ogg packets.

classref-introduction-group

## Description

A sequence of Ogg packets.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedInt64Array<class_PackedInt64Array>` **granule_positions** = `PackedInt64Array()` `🔗<class_OggPacketSequence_property_granule_positions>`

classref-property-setget

- `void (No return value.)` **set_packet_granule_positions**(value: `PackedInt64Array<class_PackedInt64Array>`)
- `PackedInt64Array<class_PackedInt64Array>` **get_packet_granule_positions**()

Contains the granule positions for each page in this packet sequence.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt64Array<class_PackedInt64Array>` for more details.

classref-item-separator

classref-property

`Array<class_Array>`\[`Array<class_Array>`\] **packet_data** = `[]` `🔗<class_OggPacketSequence_property_packet_data>`

classref-property-setget

- `void (No return value.)` **set_packet_data**(value: `Array<class_Array>`\[`Array<class_Array>`\])
- `Array<class_Array>`\[`Array<class_Array>`\] **get_packet_data**()

Contains the raw packets that make up this OggPacketSequence.

classref-item-separator

classref-property

`float<class_float>` **sampling_rate** = `0.0` `🔗<class_OggPacketSequence_property_sampling_rate>`

classref-property-setget

- `void (No return value.)` **set_sampling_rate**(value: `float<class_float>`)
- `float<class_float>` **get_sampling_rate**()

Holds sample rate information about this sequence. Must be set by another class that actually understands the codec.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **get_length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OggPacketSequence_method_get_length>`

The length of this stream, in seconds.