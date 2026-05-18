github_url
hide

# NavigationPathQueryResult2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents the result of a 2D pathfinding query.

classref-introduction-group

## Description

This class stores the result of a 2D navigation path query from the `NavigationServer2D<class_NavigationServer2D>`.

classref-introduction-group

## Tutorials

- `Using NavigationPathQueryObjects <../tutorials/navigation/navigation_using_navigationpathqueryobjects>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **PathSegmentType**: `🔗<enum_NavigationPathQueryResult2D_PathSegmentType>`

classref-enumeration-constant

`PathSegmentType<enum_NavigationPathQueryResult2D_PathSegmentType>` **PATH_SEGMENT_TYPE_REGION** = `0`

This segment of the path goes through a region.

classref-enumeration-constant

`PathSegmentType<enum_NavigationPathQueryResult2D_PathSegmentType>` **PATH_SEGMENT_TYPE_LINK** = `1`

This segment of the path goes through a link.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`PackedVector2Array<class_PackedVector2Array>` **path** = `PackedVector2Array()` `🔗<class_NavigationPathQueryResult2D_property_path>`

classref-property-setget

- `void (No return value.)` **set_path**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_path**()

The resulting path array from the navigation query. All path array positions are in global coordinates. Without customized query parameters this is the same path as returned by `NavigationServer2D.map_get_path()<class_NavigationServer2D_method_map_get_path>`.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.

classref-item-separator

classref-property

`float<class_float>` **path_length** = `0.0` `🔗<class_NavigationPathQueryResult2D_property_path_length>`

classref-property-setget

- `void (No return value.)` **set_path_length**(value: `float<class_float>`)
- `float<class_float>` **get_path_length**()

Returns the length of the path.

classref-item-separator

classref-property

`PackedInt64Array<class_PackedInt64Array>` **path_owner_ids** = `PackedInt64Array()` `🔗<class_NavigationPathQueryResult2D_property_path_owner_ids>`

classref-property-setget

- `void (No return value.)` **set_path_owner_ids**(value: `PackedInt64Array<class_PackedInt64Array>`)
- `PackedInt64Array<class_PackedInt64Array>` **get_path_owner_ids**()

The `ObjectID`s of the `Object<class_Object>`s which manage the regions and links each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt64Array<class_PackedInt64Array>` for more details.

classref-item-separator

classref-property

`Array<class_Array>`\[`RID<class_RID>`\] **path_rids** = `[]` `🔗<class_NavigationPathQueryResult2D_property_path_rids>`

classref-property-setget

- `void (No return value.)` **set_path_rids**(value: `Array<class_Array>`\[`RID<class_RID>`\])
- `Array<class_Array>`\[`RID<class_RID>`\] **get_path_rids**()

The `RID<class_RID>`s of the regions and links that each point of the path goes through.

classref-item-separator

classref-property

`PackedInt32Array<class_PackedInt32Array>` **path_types** = `PackedInt32Array()` `🔗<class_NavigationPathQueryResult2D_property_path_types>`

classref-property-setget

- `void (No return value.)` **set_path_types**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_path_types**()

The type of navigation primitive (region or link) that each point of the path goes through.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **reset**() `🔗<class_NavigationPathQueryResult2D_method_reset>`

Reset the result object to its initial state. This is useful to reuse the object across multiple queries.