github_url
hide

# RDAccelerationStructureGeometry

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Acceleration structure geometry (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

**RDAccelerationStructureGeometry** describes a set of triangles used as raytracing geometry in the `RenderingDevice.blas_create()<class_RenderingDevice_method_blas_create>` method.

The geometry is always in triangle list form, either indexed or non-indexed. Triangle strips are not supported.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AccelerationStructureGeometryFlagBits<enum_RenderingDevice_AccelerationStructureGeometryFlagBits>`\] **flags** = `0` `🔗<class_RDAccelerationStructureGeometry_property_flags>`

classref-property-setget

- `void (No return value.)` **set_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AccelerationStructureGeometryFlagBits<enum_RenderingDevice_AccelerationStructureGeometryFlagBits>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`AccelerationStructureGeometryFlagBits<enum_RenderingDevice_AccelerationStructureGeometryFlagBits>`\] **get_flags**()

Flags for the geometry.

classref-item-separator

classref-property

`RID<class_RID>` **index_buffer** = `RID()` `🔗<class_RDAccelerationStructureGeometry_property_index_buffer>`

classref-property-setget

- `void (No return value.)` **set_index_buffer**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_index_buffer**()

Buffer containing vertex indices. If `null`, triangles are non-indexed.

classref-item-separator

classref-property

`int<class_int>` **index_count** = `0` `🔗<class_RDAccelerationStructureGeometry_property_index_count>`

classref-property-setget

- `void (No return value.)` **set_index_count**(value: `int<class_int>`)
- `int<class_int>` **get_index_count**()

Number of indices used by this geometry in `index_buffer<class_RDAccelerationStructureGeometry_property_index_buffer>`.

classref-item-separator

classref-property

`int<class_int>` **index_offset** = `0` `🔗<class_RDAccelerationStructureGeometry_property_index_offset>`

classref-property-setget

- `void (No return value.)` **set_index_offset**(value: `int<class_int>`)
- `int<class_int>` **get_index_offset**()

Byte offset of the first index in `index_buffer<class_RDAccelerationStructureGeometry_property_index_buffer>`.

classref-item-separator

classref-property

`RID<class_RID>` **vertex_buffer** = `RID()` `🔗<class_RDAccelerationStructureGeometry_property_vertex_buffer>`

classref-property-setget

- `void (No return value.)` **set_vertex_buffer**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_vertex_buffer**()

Buffer containing vertices.

classref-item-separator

classref-property

`int<class_int>` **vertex_count** = `0` `🔗<class_RDAccelerationStructureGeometry_property_vertex_count>`

classref-property-setget

- `void (No return value.)` **set_vertex_count**(value: `int<class_int>`)
- `int<class_int>` **get_vertex_count**()

Number of vertices used by this geometry in `vertex_buffer<class_RDAccelerationStructureGeometry_property_vertex_buffer>`.

classref-item-separator

classref-property

`DataFormat<enum_RenderingDevice_DataFormat>` **vertex_format** = `232` `🔗<class_RDAccelerationStructureGeometry_property_vertex_format>`

classref-property-setget

- `void (No return value.)` **set_vertex_format**(value: `DataFormat<enum_RenderingDevice_DataFormat>`)
- `DataFormat<enum_RenderingDevice_DataFormat>` **get_vertex_format**()

Format of the vertices in `vertex_buffer<class_RDAccelerationStructureGeometry_property_vertex_buffer>`.

classref-item-separator

classref-property

`int<class_int>` **vertex_offset** = `0` `🔗<class_RDAccelerationStructureGeometry_property_vertex_offset>`

classref-property-setget

- `void (No return value.)` **set_vertex_offset**(value: `int<class_int>`)
- `int<class_int>` **get_vertex_offset**()

Byte offset of the first vertex in `vertex_buffer<class_RDAccelerationStructureGeometry_property_vertex_buffer>`.

classref-item-separator

classref-property

`int<class_int>` **vertex_stride** = `0` `🔗<class_RDAccelerationStructureGeometry_property_vertex_stride>`

classref-property-setget

- `void (No return value.)` **set_vertex_stride**(value: `int<class_int>`)
- `int<class_int>` **get_vertex_stride**()

Number of bytes between each vertex in `vertex_buffer<class_RDAccelerationStructureGeometry_property_vertex_buffer>`.