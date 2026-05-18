github_url
hide

# OpenXRPlaneTracker

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `OpenXRSpatialEntityTracker<class_OpenXRSpatialEntityTracker>` **\<** `XRPositionalTracker<class_XRPositionalTracker>` **\<** `XRTracker<class_XRTracker>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Spatial entity tracker for our spatial entity plane tracking extension.

classref-introduction-group

## Description

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**mesh_changed**() `🔗<class_OpenXRPlaneTracker_signal_mesh_changed>`

Emitted when our mesh data has changed the mesh instance and collision needs to be updated.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Vector2<class_Vector2>` **bounds_size** = `Vector2(0, 0)` `🔗<class_OpenXRPlaneTracker_property_bounds_size>`

classref-property-setget

- `void (No return value.)` **set_bounds_size**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_bounds_size**()

The bounding size of the plane. This is a 2D size.

classref-item-separator

classref-property

`PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **plane_alignment** = `0` `🔗<class_OpenXRPlaneTracker_property_plane_alignment>`

classref-property-setget

- `void (No return value.)` **set_plane_alignment**(value: `PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>`)
- `PlaneAlignment<enum_OpenXRSpatialComponentPlaneAlignmentList_PlaneAlignment>` **get_plane_alignment**()

The main alignment in space of this plane.

classref-item-separator

classref-property

`String<class_String>` **plane_label** = `""` `🔗<class_OpenXRPlaneTracker_property_plane_label>`

classref-property-setget

- `void (No return value.)` **set_plane_label**(value: `String<class_String>`)
- `String<class_String>` **get_plane_label**()

The semantic label for this plane.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_mesh_data**() `🔗<class_OpenXRPlaneTracker_method_clear_mesh_data>`

Clears the mesh data for this tracker. You should only call this if you are handling your own discovery logic.

classref-item-separator

classref-method

`Mesh<class_Mesh>` **get_mesh**() `🔗<class_OpenXRPlaneTracker_method_get_mesh>`

Gets a mesh created from either the mesh data or from our bounding size for this plane.

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **get_mesh_offset**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRPlaneTracker_method_get_mesh_offset>`

Gets the transform by which to offset the mesh and collision shape from our pose to display these correctly.

classref-item-separator

classref-method

`Shape3D<class_Shape3D>` **get_shape**(thickness: `float<class_float>` = 0.01) `🔗<class_OpenXRPlaneTracker_method_get_shape>`

Gets a collision shape built either from the mesh data or from our bounding size for this plane.

classref-item-separator

classref-method

`void (No return value.)` **set_mesh_data**(origin: `Transform3D<class_Transform3D>`, vertices: `PackedVector2Array<class_PackedVector2Array>`, indices: `PackedInt32Array<class_PackedInt32Array>` = PackedInt32Array()) `🔗<class_OpenXRPlaneTracker_method_set_mesh_data>`

Sets the mesh data for this plane. You should only call this if you are handling your own discovery logic.