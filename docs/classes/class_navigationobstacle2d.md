github_url
hide

# NavigationObstacle2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

2D obstacle used to affect navigation mesh baking or constrain velocities of avoidance controlled agents.

classref-introduction-group

## Description

An obstacle needs a navigation map and outline `vertices<class_NavigationObstacle2D_property_vertices>` defined to work correctly. The outlines can not cross or overlap.

Obstacles can be included in the navigation mesh baking process when `affect_navigation_mesh<class_NavigationObstacle2D_property_affect_navigation_mesh>` is enabled. They do not add walkable geometry, instead their role is to discard other source geometry inside the shape. This can be used to prevent navigation mesh from appearing in unwanted places. If `carve_navigation_mesh<class_NavigationObstacle2D_property_carve_navigation_mesh>` is enabled the baked shape will not be affected by offsets of the navigation mesh baking, e.g. the agent radius.

With `avoidance_enabled<class_NavigationObstacle2D_property_avoidance_enabled>` the obstacle can constrain the avoidance velocities of avoidance using agents. If the obstacle's vertices are wound in clockwise order, avoidance agents will be pushed in by the obstacle, otherwise, avoidance agents will be pushed out. Obstacles using vertices and avoidance can warp to a new position but should not be moved every single frame as each change requires a rebuild of the avoidance map.

classref-introduction-group

## Tutorials

- `Using NavigationObstacles <../tutorials/navigation/navigation_using_navigationobstacles>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **affect_navigation_mesh** = `false` `🔗<class_NavigationObstacle2D_property_affect_navigation_mesh>`

classref-property-setget

- `void (No return value.)` **set_affect_navigation_mesh**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_affect_navigation_mesh**()

If enabled and parsed in a navigation mesh baking process the obstacle will discard source geometry inside its `vertices<class_NavigationObstacle2D_property_vertices>` defined shape.

classref-item-separator

classref-property

`bool<class_bool>` **avoidance_enabled** = `true` `🔗<class_NavigationObstacle2D_property_avoidance_enabled>`

classref-property-setget

- `void (No return value.)` **set_avoidance_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_avoidance_enabled**()

If `true` the obstacle affects avoidance using agents.

classref-item-separator

classref-property

`int<class_int>` **avoidance_layers** = `1` `🔗<class_NavigationObstacle2D_property_avoidance_layers>`

classref-property-setget

- `void (No return value.)` **set_avoidance_layers**(value: `int<class_int>`)
- `int<class_int>` **get_avoidance_layers**()

A bitfield determining the avoidance layers for this obstacle. Agents with a matching bit on the their avoidance mask will avoid this obstacle.

classref-item-separator

classref-property

`bool<class_bool>` **carve_navigation_mesh** = `false` `🔗<class_NavigationObstacle2D_property_carve_navigation_mesh>`

classref-property-setget

- `void (No return value.)` **set_carve_navigation_mesh**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_carve_navigation_mesh**()

If enabled the obstacle vertices will carve into the baked navigation mesh with the shape unaffected by additional offsets (e.g. agent radius).

It will still be affected by further postprocessing of the baking process, like edge and polygon simplification.

Requires `affect_navigation_mesh<class_NavigationObstacle2D_property_affect_navigation_mesh>` to be enabled.

classref-item-separator

classref-property

`float<class_float>` **radius** = `0.0` `🔗<class_NavigationObstacle2D_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

Sets the avoidance radius for the obstacle.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **velocity** = `Vector2(0, 0)` `🔗<class_NavigationObstacle2D_property_velocity>`

classref-property-setget

- `void (No return value.)` **set_velocity**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_velocity**()

Sets the wanted velocity for the obstacle so other agent's can better predict the obstacle if it is moved with a velocity regularly (every frame) instead of warped to a new position. Does only affect avoidance for the obstacles `radius<class_NavigationObstacle2D_property_radius>`. Does nothing for the obstacles static vertices.

classref-item-separator

classref-property

`PackedVector2Array<class_PackedVector2Array>` **vertices** = `PackedVector2Array()` `🔗<class_NavigationObstacle2D_property_vertices>`

classref-property-setget

- `void (No return value.)` **set_vertices**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_vertices**()

The outline vertices of the obstacle. If the vertices are winded in clockwise order agents will be pushed in by the obstacle, else they will be pushed out. Outlines can not be crossed or overlap. Should the vertices using obstacle be warped to a new position agent's can not predict this movement and may get trapped inside the obstacle.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **get_avoidance_layer_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationObstacle2D_method_get_avoidance_layer_value>`

Returns whether or not the specified layer of the `avoidance_layers<class_NavigationObstacle2D_property_avoidance_layers>` bitmask is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`RID<class_RID>` **get_navigation_map**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationObstacle2D_method_get_navigation_map>`

Returns the `RID<class_RID>` of the navigation map for this NavigationObstacle node. This function returns always the map set on the NavigationObstacle node and not the map of the abstract obstacle on the NavigationServer. If the obstacle map is changed directly with the NavigationServer API the NavigationObstacle node will not be aware of the map change. Use `set_navigation_map()<class_NavigationObstacle2D_method_set_navigation_map>` to change the navigation map for the NavigationObstacle and also update the obstacle on the NavigationServer.

classref-item-separator

classref-method

`RID<class_RID>` **get_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationObstacle2D_method_get_rid>`

Returns the `RID<class_RID>` of this obstacle on the `NavigationServer2D<class_NavigationServer2D>`.

classref-item-separator

classref-method

`void (No return value.)` **set_avoidance_layer_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_NavigationObstacle2D_method_set_avoidance_layer_value>`

Based on `value`, enables or disables the specified layer in the `avoidance_layers<class_NavigationObstacle2D_property_avoidance_layers>` bitmask, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_navigation_map**(navigation_map: `RID<class_RID>`) `🔗<class_NavigationObstacle2D_method_set_navigation_map>`

Sets the `RID<class_RID>` of the navigation map this NavigationObstacle node should use and also updates the `obstacle` on the NavigationServer.