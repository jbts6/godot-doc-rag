github_url
hide

# NavigationAgent2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `Node<class_Node>` **\<** `Object<class_Object>`

A 2D agent used to pathfind to a position while avoiding obstacles.

classref-introduction-group

## Description

A 2D agent used to pathfind to a position while avoiding static and dynamic obstacles. The calculation can be used by the parent node to dynamically move it along the path. Requires navigation data to work correctly.

Dynamic obstacles are avoided using RVO collision avoidance. Avoidance is computed before physics, so the pathfinding information can be used safely in the physics step.

**Note:** After setting the `target_position<class_NavigationAgent2D_property_target_position>` property, the `get_next_path_position()<class_NavigationAgent2D_method_get_next_path_position>` method must be used once every physics frame to update the internal path logic of the navigation agent. The vector position it returns should be used as the next movement position for the agent's parent node.

**Note:** Several methods of this class, such as `get_next_path_position()<class_NavigationAgent2D_method_get_next_path_position>`, can trigger a new path calculation. Calling these in your callback to an agent's signal, such as `waypoint_reached<class_NavigationAgent2D_signal_waypoint_reached>`, can cause infinite recursion. It is recommended to call these methods in the physics step or, alternatively, delay their call until the end of the frame (see `Object.call_deferred()<class_Object_method_call_deferred>` or `Object.CONNECT_DEFERRED<class_Object_constant_CONNECT_DEFERRED>`).

classref-introduction-group

## Tutorials

- `Using NavigationAgents <../tutorials/navigation/navigation_using_navigationagents>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**link_reached**(details: `Dictionary<class_Dictionary>`) `🔗<class_NavigationAgent2D_signal_link_reached>`

Signals that the agent reached a navigation link. Emitted when the agent moves within `path_desired_distance<class_NavigationAgent2D_property_path_desired_distance>` of the next position of the path when that position is a navigation link.

The details dictionary may contain the following keys depending on the value of `path_metadata_flags<class_NavigationAgent2D_property_path_metadata_flags>`:

- `position`: The start position of the link that was reached.
- `type`: Always `NavigationPathQueryResult2D.PATH_SEGMENT_TYPE_LINK<class_NavigationPathQueryResult2D_constant_PATH_SEGMENT_TYPE_LINK>`.
- `rid`: The `RID<class_RID>` of the link.
- `owner`: The object which manages the link (usually `NavigationLink2D<class_NavigationLink2D>`).
- `link_entry_position`: If `owner` is available and the owner is a `NavigationLink2D<class_NavigationLink2D>`, it will contain the global position of the link's point the agent is entering.
- `link_exit_position`: If `owner` is available and the owner is a `NavigationLink2D<class_NavigationLink2D>`, it will contain the global position of the link's point which the agent is exiting.

classref-item-separator

classref-signal

**navigation_finished**() `🔗<class_NavigationAgent2D_signal_navigation_finished>`

Signals that the agent's navigation has finished. If the target is reachable, navigation ends when the target is reached. If the target is unreachable, navigation ends when the last waypoint of the path is reached. This signal is emitted only once per loaded path.

This signal will be emitted just after `target_reached<class_NavigationAgent2D_signal_target_reached>` when the target is reachable.

classref-item-separator

classref-signal

**path_changed**() `🔗<class_NavigationAgent2D_signal_path_changed>`

Emitted when the agent had to update the loaded path:

- because path was previously empty.
- because navigation map has changed.
- because agent pushed further away from the current path segment than the `path_max_distance<class_NavigationAgent2D_property_path_max_distance>`.

classref-item-separator

classref-signal

**target_reached**() `🔗<class_NavigationAgent2D_signal_target_reached>`

Signals that the agent reached the target, i.e. the agent moved within `target_desired_distance<class_NavigationAgent2D_property_target_desired_distance>` of the `target_position<class_NavigationAgent2D_property_target_position>`. This signal is emitted only once per loaded path.

This signal will be emitted just before `navigation_finished<class_NavigationAgent2D_signal_navigation_finished>` when the target is reachable.

It may not always be possible to reach the target but it should always be possible to reach the final position. See `get_final_position()<class_NavigationAgent2D_method_get_final_position>`.

classref-item-separator

classref-signal

**velocity_computed**(safe_velocity: `Vector2<class_Vector2>`) `🔗<class_NavigationAgent2D_signal_velocity_computed>`

Notifies when the collision avoidance velocity is calculated. Emitted every update as long as `avoidance_enabled<class_NavigationAgent2D_property_avoidance_enabled>` is `true` and the agent has a navigation map.

classref-item-separator

classref-signal

**waypoint_reached**(details: `Dictionary<class_Dictionary>`) `🔗<class_NavigationAgent2D_signal_waypoint_reached>`

Signals that the agent reached a waypoint. Emitted when the agent moves within `path_desired_distance<class_NavigationAgent2D_property_path_desired_distance>` of the next position of the path.

The details dictionary may contain the following keys depending on the value of `path_metadata_flags<class_NavigationAgent2D_property_path_metadata_flags>`:

- `position`: The position of the waypoint that was reached.
- `type`: The type of navigation primitive (region or link) that contains this waypoint.
- `rid`: The `RID<class_RID>` of the containing navigation primitive (region or link).
- `owner`: The object which manages the containing navigation primitive (region or link).

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **avoidance_enabled** = `false` `🔗<class_NavigationAgent2D_property_avoidance_enabled>`

classref-property-setget

- `void (No return value.)` **set_avoidance_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_avoidance_enabled**()

If `true` the agent is registered for an RVO avoidance callback on the `NavigationServer2D<class_NavigationServer2D>`. When `velocity<class_NavigationAgent2D_property_velocity>` is used and the processing is completed a `safe_velocity` Vector2 is received with a signal connection to `velocity_computed<class_NavigationAgent2D_signal_velocity_computed>`. Avoidance processing with many registered agents has a significant performance cost and should only be enabled on agents that currently require it.

classref-item-separator

classref-property

`int<class_int>` **avoidance_layers** = `1` `🔗<class_NavigationAgent2D_property_avoidance_layers>`

classref-property-setget

- `void (No return value.)` **set_avoidance_layers**(value: `int<class_int>`)
- `int<class_int>` **get_avoidance_layers**()

A bitfield determining the avoidance layers for this NavigationAgent. Other agents with a matching bit on the `avoidance_mask<class_NavigationAgent2D_property_avoidance_mask>` will avoid this agent.

classref-item-separator

classref-property

`int<class_int>` **avoidance_mask** = `1` `🔗<class_NavigationAgent2D_property_avoidance_mask>`

classref-property-setget

- `void (No return value.)` **set_avoidance_mask**(value: `int<class_int>`)
- `int<class_int>` **get_avoidance_mask**()

A bitfield determining what other avoidance agents and obstacles this NavigationAgent will avoid when a bit matches at least one of their `avoidance_layers<class_NavigationAgent2D_property_avoidance_layers>`.

classref-item-separator

classref-property

`float<class_float>` **avoidance_priority** = `1.0` `🔗<class_NavigationAgent2D_property_avoidance_priority>`

classref-property-setget

- `void (No return value.)` **set_avoidance_priority**(value: `float<class_float>`)
- `float<class_float>` **get_avoidance_priority**()

The agent does not adjust the velocity for other agents that would match the `avoidance_mask<class_NavigationAgent2D_property_avoidance_mask>` but have a lower `avoidance_priority<class_NavigationAgent2D_property_avoidance_priority>`. This in turn makes the other agents with lower priority adjust their velocities even more to avoid collision with this agent.

classref-item-separator

classref-property

`bool<class_bool>` **debug_enabled** = `false` `🔗<class_NavigationAgent2D_property_debug_enabled>`

classref-property-setget

- `void (No return value.)` **set_debug_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_debug_enabled**()

If `true` shows debug visuals for this agent.

classref-item-separator

classref-property

`Color<class_Color>` **debug_path_custom_color** = `Color(1, 1, 1, 1)` `🔗<class_NavigationAgent2D_property_debug_path_custom_color>`

classref-property-setget

- `void (No return value.)` **set_debug_path_custom_color**(value: `Color<class_Color>`)
- `Color<class_Color>` **get_debug_path_custom_color**()

If `debug_use_custom<class_NavigationAgent2D_property_debug_use_custom>` is `true` uses this color for this agent instead of global color.

classref-item-separator

classref-property

`float<class_float>` **debug_path_custom_line_width** = `-1.0` `🔗<class_NavigationAgent2D_property_debug_path_custom_line_width>`

classref-property-setget

- `void (No return value.)` **set_debug_path_custom_line_width**(value: `float<class_float>`)
- `float<class_float>` **get_debug_path_custom_line_width**()

If `debug_use_custom<class_NavigationAgent2D_property_debug_use_custom>` is `true` uses this line width for rendering paths for this agent instead of global line width.

classref-item-separator

classref-property

`float<class_float>` **debug_path_custom_point_size** = `4.0` `🔗<class_NavigationAgent2D_property_debug_path_custom_point_size>`

classref-property-setget

- `void (No return value.)` **set_debug_path_custom_point_size**(value: `float<class_float>`)
- `float<class_float>` **get_debug_path_custom_point_size**()

If `debug_use_custom<class_NavigationAgent2D_property_debug_use_custom>` is `true` uses this rasterized point size for rendering path points for this agent instead of global point size.

classref-item-separator

classref-property

`bool<class_bool>` **debug_use_custom** = `false` `🔗<class_NavigationAgent2D_property_debug_use_custom>`

classref-property-setget

- `void (No return value.)` **set_debug_use_custom**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_debug_use_custom**()

If `true` uses the defined `debug_path_custom_color<class_NavigationAgent2D_property_debug_path_custom_color>` for this agent instead of global color.

classref-item-separator

classref-property

`int<class_int>` **max_neighbors** = `10` `🔗<class_NavigationAgent2D_property_max_neighbors>`

classref-property-setget

- `void (No return value.)` **set_max_neighbors**(value: `int<class_int>`)
- `int<class_int>` **get_max_neighbors**()

The maximum number of neighbors for the agent to consider.

classref-item-separator

classref-property

`float<class_float>` **max_speed** = `100.0` `🔗<class_NavigationAgent2D_property_max_speed>`

classref-property-setget

- `void (No return value.)` **set_max_speed**(value: `float<class_float>`)
- `float<class_float>` **get_max_speed**()

The maximum speed that an agent can move.

classref-item-separator

classref-property

`int<class_int>` **navigation_layers** = `1` `🔗<class_NavigationAgent2D_property_navigation_layers>`

classref-property-setget

- `void (No return value.)` **set_navigation_layers**(value: `int<class_int>`)
- `int<class_int>` **get_navigation_layers**()

A bitfield determining which navigation layers of navigation regions this agent will use to calculate a path. Changing it during runtime will clear the current navigation path and generate a new one, according to the new navigation layers.

classref-item-separator

classref-property

`float<class_float>` **neighbor_distance** = `500.0` `🔗<class_NavigationAgent2D_property_neighbor_distance>`

classref-property-setget

- `void (No return value.)` **set_neighbor_distance**(value: `float<class_float>`)
- `float<class_float>` **get_neighbor_distance**()

The distance to search for other agents.

classref-item-separator

classref-property

`float<class_float>` **path_desired_distance** = `20.0` `🔗<class_NavigationAgent2D_property_path_desired_distance>`

classref-property-setget

- `void (No return value.)` **set_path_desired_distance**(value: `float<class_float>`)
- `float<class_float>` **get_path_desired_distance**()

The distance threshold before a path point is considered to be reached. This allows agents to not have to hit a path point on the path exactly, but only to reach its general area. If this value is set too high, the NavigationAgent will skip points on the path, which can lead to it leaving the navigation mesh. If this value is set too low, the NavigationAgent will be stuck in a repath loop because it will constantly overshoot the distance to the next point on each physics frame update.

classref-item-separator

classref-property

`float<class_float>` **path_max_distance** = `100.0` `🔗<class_NavigationAgent2D_property_path_max_distance>`

classref-property-setget

- `void (No return value.)` **set_path_max_distance**(value: `float<class_float>`)
- `float<class_float>` **get_path_max_distance**()

The maximum distance the agent is allowed away from the ideal path to the final position. This can happen due to trying to avoid collisions. When the maximum distance is exceeded, it recalculates the ideal path.

classref-item-separator

classref-property

`BitField (This value is an integer composed as a bitmask of the following flags.)`\[`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`\] **path_metadata_flags** = `7` `🔗<class_NavigationAgent2D_property_path_metadata_flags>`

classref-property-setget

- `void (No return value.)` **set_path_metadata_flags**(value: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`PathMetadataFlags<enum_NavigationPathQueryParameters2D_PathMetadataFlags>`\] **get_path_metadata_flags**()

Additional information to return with the navigation path.

classref-item-separator

classref-property

`PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>` **path_postprocessing** = `0` `🔗<class_NavigationAgent2D_property_path_postprocessing>`

classref-property-setget

- `void (No return value.)` **set_path_postprocessing**(value: `PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>`)
- `PathPostProcessing<enum_NavigationPathQueryParameters2D_PathPostProcessing>` **get_path_postprocessing**()

The path postprocessing applied to the raw path corridor found by the `pathfinding_algorithm<class_NavigationAgent2D_property_pathfinding_algorithm>`.

classref-item-separator

classref-property

`float<class_float>` **path_return_max_length** = `0.0` `🔗<class_NavigationAgent2D_property_path_return_max_length>`

classref-property-setget

- `void (No return value.)` **set_path_return_max_length**(value: `float<class_float>`)
- `float<class_float>` **get_path_return_max_length**()

The maximum allowed length of the returned path in world units. A path will be clipped when going over this length.

classref-item-separator

classref-property

`float<class_float>` **path_return_max_radius** = `0.0` `🔗<class_NavigationAgent2D_property_path_return_max_radius>`

classref-property-setget

- `void (No return value.)` **set_path_return_max_radius**(value: `float<class_float>`)
- `float<class_float>` **get_path_return_max_radius**()

The maximum allowed radius in world units that the returned path can be from the path start. The path will be clipped when going over this radius. Compared to `path_return_max_length<class_NavigationAgent2D_property_path_return_max_length>`, this allows the agent to go that much further, if they need to walk around a corner.

**Note:** This will perform a sphere clip considering only the actual navigation mesh path points with the first path position being the sphere's center.

classref-item-separator

classref-property

`float<class_float>` **path_search_max_distance** = `0.0` `🔗<class_NavigationAgent2D_property_path_search_max_distance>`

classref-property-setget

- `void (No return value.)` **set_path_search_max_distance**(value: `float<class_float>`)
- `float<class_float>` **get_path_search_max_distance**()

The maximum distance a searched polygon can be away from the start polygon before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of `0` or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.

classref-item-separator

classref-property

`int<class_int>` **path_search_max_polygons** = `4096` `🔗<class_NavigationAgent2D_property_path_search_max_polygons>`

classref-property-setget

- `void (No return value.)` **set_path_search_max_polygons**(value: `int<class_int>`)
- `int<class_int>` **get_path_search_max_polygons**()

The maximum number of polygons that are searched before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of `0` or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.

classref-item-separator

classref-property

`PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>` **pathfinding_algorithm** = `0` `🔗<class_NavigationAgent2D_property_pathfinding_algorithm>`

classref-property-setget

- `void (No return value.)` **set_pathfinding_algorithm**(value: `PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>`)
- `PathfindingAlgorithm<enum_NavigationPathQueryParameters2D_PathfindingAlgorithm>` **get_pathfinding_algorithm**()

The pathfinding algorithm used in the path query.

classref-item-separator

classref-property

`float<class_float>` **radius** = `10.0` `🔗<class_NavigationAgent2D_property_radius>`

classref-property-setget

- `void (No return value.)` **set_radius**(value: `float<class_float>`)
- `float<class_float>` **get_radius**()

The radius of the avoidance agent. This is the "body" of the avoidance agent and not the avoidance maneuver starting radius (which is controlled by `neighbor_distance<class_NavigationAgent2D_property_neighbor_distance>`).

Does not affect normal pathfinding. To change an actor's pathfinding radius bake `NavigationPolygon<class_NavigationPolygon>` resources with a different `NavigationPolygon.agent_radius<class_NavigationPolygon_property_agent_radius>` property and use different navigation maps for each actor size.

classref-item-separator

classref-property

`float<class_float>` **simplify_epsilon** = `0.0` `🔗<class_NavigationAgent2D_property_simplify_epsilon>`

classref-property-setget

- `void (No return value.)` **set_simplify_epsilon**(value: `float<class_float>`)
- `float<class_float>` **get_simplify_epsilon**()

The path simplification amount in worlds units.

classref-item-separator

classref-property

`bool<class_bool>` **simplify_path** = `false` `🔗<class_NavigationAgent2D_property_simplify_path>`

classref-property-setget

- `void (No return value.)` **set_simplify_path**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_simplify_path**()

If `true` a simplified version of the path will be returned with less critical path points removed. The simplification amount is controlled by `simplify_epsilon<class_NavigationAgent2D_property_simplify_epsilon>`. The simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve point decimation.

Path simplification can be helpful to mitigate various path following issues that can arise with certain agent types and script behaviors. E.g. "steering" agents or avoidance in "open fields".

classref-item-separator

classref-property

`float<class_float>` **target_desired_distance** = `10.0` `🔗<class_NavigationAgent2D_property_target_desired_distance>`

classref-property-setget

- `void (No return value.)` **set_target_desired_distance**(value: `float<class_float>`)
- `float<class_float>` **get_target_desired_distance**()

The distance threshold before the target is considered to be reached. On reaching the target, `target_reached<class_NavigationAgent2D_signal_target_reached>` is emitted and navigation ends (see `is_navigation_finished()<class_NavigationAgent2D_method_is_navigation_finished>` and `navigation_finished<class_NavigationAgent2D_signal_navigation_finished>`).

You can make navigation end early by setting this property to a value greater than `path_desired_distance<class_NavigationAgent2D_property_path_desired_distance>` (navigation will end before reaching the last waypoint).

You can also make navigation end closer to the target than each individual path position by setting this property to a value lower than `path_desired_distance<class_NavigationAgent2D_property_path_desired_distance>` (navigation won't immediately end when reaching the last waypoint). However, if the value set is too low, the agent will be stuck in a repath loop because it will constantly overshoot the distance to the target on each physics frame update.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **target_position** = `Vector2(0, 0)` `🔗<class_NavigationAgent2D_property_target_position>`

classref-property-setget

- `void (No return value.)` **set_target_position**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_target_position**()

If set, a new navigation path from the current agent position to the `target_position<class_NavigationAgent2D_property_target_position>` is requested from the NavigationServer.

classref-item-separator

classref-property

`float<class_float>` **time_horizon_agents** = `1.0` `🔗<class_NavigationAgent2D_property_time_horizon_agents>`

classref-property-setget

- `void (No return value.)` **set_time_horizon_agents**(value: `float<class_float>`)
- `float<class_float>` **get_time_horizon_agents**()

The minimal amount of time for which this agent's velocities, that are computed with the collision avoidance algorithm, are safe with respect to other agents. The larger the number, the sooner the agent will respond to other agents, but less freedom in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.

classref-item-separator

classref-property

`float<class_float>` **time_horizon_obstacles** = `0.0` `🔗<class_NavigationAgent2D_property_time_horizon_obstacles>`

classref-property-setget

- `void (No return value.)` **set_time_horizon_obstacles**(value: `float<class_float>`)
- `float<class_float>` **get_time_horizon_obstacles**()

The minimal amount of time for which this agent's velocities, that are computed with the collision avoidance algorithm, are safe with respect to static avoidance obstacles. The larger the number, the sooner the agent will respond to static avoidance obstacles, but less freedom in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **velocity** = `Vector2(0, 0)` `🔗<class_NavigationAgent2D_property_velocity>`

classref-property-setget

- `void (No return value.)` **set_velocity**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_velocity**()

Sets the new wanted velocity for the agent. The avoidance simulation will try to fulfill this velocity if possible but will modify it to avoid collision with other agents and obstacles. When an agent is teleported to a new position, use `set_velocity_forced()<class_NavigationAgent2D_method_set_velocity_forced>` as well to reset the internal simulation velocity.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`float<class_float>` **distance_to_target**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_distance_to_target>`

Returns the distance to the target position, using the agent's global position. The user must set `target_position<class_NavigationAgent2D_property_target_position>` in order for this to be accurate.

classref-item-separator

classref-method

`bool<class_bool>` **get_avoidance_layer_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_avoidance_layer_value>`

Returns whether or not the specified layer of the `avoidance_layers<class_NavigationAgent2D_property_avoidance_layers>` bitmask is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`bool<class_bool>` **get_avoidance_mask_value**(mask_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_avoidance_mask_value>`

Returns whether or not the specified mask of the `avoidance_mask<class_NavigationAgent2D_property_avoidance_mask>` bitmask is enabled, given a `mask_number` between 1 and 32.

classref-item-separator

classref-method

`PackedVector2Array<class_PackedVector2Array>` **get_current_navigation_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_current_navigation_path>`

Returns this agent's current path from start to finish in global coordinates. The path only updates when the target position is changed or the agent requires a repath. The path array is not intended to be used in direct path movement as the agent has its own internal path logic that would get corrupted by changing the path array manually. Use the intended `get_next_path_position()<class_NavigationAgent2D_method_get_next_path_position>` once every physics frame to receive the next path point for the agents movement as this function also updates the internal path logic.

classref-item-separator

classref-method

`int<class_int>` **get_current_navigation_path_index**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_current_navigation_path_index>`

Returns which index the agent is currently on in the navigation path's `PackedVector2Array<class_PackedVector2Array>`.

classref-item-separator

classref-method

`NavigationPathQueryResult2D<class_NavigationPathQueryResult2D>` **get_current_navigation_result**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_current_navigation_result>`

Returns the path query result for the path the agent is currently following.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_final_position**() `🔗<class_NavigationAgent2D_method_get_final_position>`

Returns the reachable final position of the current navigation path in global coordinates. This position can change if the agent needs to update the navigation path which makes the agent emit the `path_changed<class_NavigationAgent2D_signal_path_changed>` signal.

classref-item-separator

classref-method

`bool<class_bool>` **get_navigation_layer_value**(layer_number: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_navigation_layer_value>`

Returns whether or not the specified layer of the `navigation_layers<class_NavigationAgent2D_property_navigation_layers>` bitmask is enabled, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`RID<class_RID>` **get_navigation_map**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_navigation_map>`

Returns the `RID<class_RID>` of the navigation map for this NavigationAgent node. This function returns always the map set on the NavigationAgent node and not the map of the abstract agent on the NavigationServer. If the agent map is changed directly with the NavigationServer API the NavigationAgent node will not be aware of the map change. Use `set_navigation_map()<class_NavigationAgent2D_method_set_navigation_map>` to change the navigation map for the NavigationAgent and also update the agent on the NavigationServer.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_next_path_position**() `🔗<class_NavigationAgent2D_method_get_next_path_position>`

Returns the next position in global coordinates that can be moved to, making sure that there are no static objects in the way. If the agent does not have a navigation path, it will return the position of the agent's parent. The use of this function once every physics frame is required to update the internal path logic of the NavigationAgent.

classref-item-separator

classref-method

`float<class_float>` **get_path_length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_path_length>`

Returns the length of the currently calculated path. The returned value is `0.0`, if the path is still calculating or no calculation has been requested yet.

classref-item-separator

classref-method

`RID<class_RID>` **get_rid**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_get_rid>`

Returns the `RID<class_RID>` of this agent on the `NavigationServer2D<class_NavigationServer2D>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_navigation_finished**() `🔗<class_NavigationAgent2D_method_is_navigation_finished>`

Returns `true` if the agent's navigation has finished. If the target is reachable, navigation ends when the target is reached. If the target is unreachable, navigation ends when the last waypoint of the path is reached.

**Note:** While `true` prefer to stop calling update functions like `get_next_path_position()<class_NavigationAgent2D_method_get_next_path_position>`. This avoids jittering the standing agent due to calling repeated path updates.

classref-item-separator

classref-method

`bool<class_bool>` **is_target_reachable**() `🔗<class_NavigationAgent2D_method_is_target_reachable>`

Returns `true` if `get_final_position()<class_NavigationAgent2D_method_get_final_position>` is within `target_desired_distance<class_NavigationAgent2D_property_target_desired_distance>` of the `target_position<class_NavigationAgent2D_property_target_position>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_target_reached**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NavigationAgent2D_method_is_target_reached>`

Returns `true` if the agent reached the target, i.e. the agent moved within `target_desired_distance<class_NavigationAgent2D_property_target_desired_distance>` of the `target_position<class_NavigationAgent2D_property_target_position>`. It may not always be possible to reach the target but it should always be possible to reach the final position. See `get_final_position()<class_NavigationAgent2D_method_get_final_position>`.

classref-item-separator

classref-method

`void (No return value.)` **set_avoidance_layer_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_NavigationAgent2D_method_set_avoidance_layer_value>`

Based on `value`, enables or disables the specified layer in the `avoidance_layers<class_NavigationAgent2D_property_avoidance_layers>` bitmask, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_avoidance_mask_value**(mask_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_NavigationAgent2D_method_set_avoidance_mask_value>`

Based on `value`, enables or disables the specified mask in the `avoidance_mask<class_NavigationAgent2D_property_avoidance_mask>` bitmask, given a `mask_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_navigation_layer_value**(layer_number: `int<class_int>`, value: `bool<class_bool>`) `🔗<class_NavigationAgent2D_method_set_navigation_layer_value>`

Based on `value`, enables or disables the specified layer in the `navigation_layers<class_NavigationAgent2D_property_navigation_layers>` bitmask, given a `layer_number` between 1 and 32.

classref-item-separator

classref-method

`void (No return value.)` **set_navigation_map**(navigation_map: `RID<class_RID>`) `🔗<class_NavigationAgent2D_method_set_navigation_map>`

Sets the `RID<class_RID>` of the navigation map this NavigationAgent node should use and also updates the `agent` on the NavigationServer.

classref-item-separator

classref-method

`void (No return value.)` **set_velocity_forced**(velocity: `Vector2<class_Vector2>`) `🔗<class_NavigationAgent2D_method_set_velocity_forced>`

Replaces the internal velocity in the collision avoidance simulation with `velocity`. When an agent is teleported to a new position this function should be used in the same frame. If called frequently this function can get agents stuck.