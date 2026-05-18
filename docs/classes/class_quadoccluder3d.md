github_url
hide

# QuadOccluder3D

**Inherits:** `Occluder3D<class_Occluder3D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Flat plane shape for use with occlusion culling in `OccluderInstance3D<class_OccluderInstance3D>`.

classref-introduction-group

## Description

**QuadOccluder3D** stores a flat plane shape that can be used by the engine's occlusion culling system. See also `PolygonOccluder3D<class_PolygonOccluder3D>` if you need to customize the quad's shape.

See `OccluderInstance3D<class_OccluderInstance3D>`'s documentation for instructions on setting up occlusion culling.

classref-introduction-group

## Tutorials

- `Occlusion culling <../tutorials/3d/occlusion_culling>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector2<class_Vector2>` **size** = `Vector2(1, 1)` `🔗<class_QuadOccluder3D_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_size**()

The quad's size in 3D units.