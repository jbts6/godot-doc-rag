github_url
hide

# EditorNode3DGizmo

**Inherits:** `Node3DGizmo<class_Node3DGizmo>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Gizmo for editing `Node3D<class_Node3D>` objects.

classref-introduction-group

## Description

Gizmo that is used for providing custom visualization and editing (handles and subgizmos) for `Node3D<class_Node3D>` objects. Can be overridden to create custom gizmos, but for simple gizmos creating an `EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>` is usually recommended.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_begin_handle_action**(id: `int<class_int>`, secondary: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorNode3DGizmo_private_method__begin_handle_action>`

There is currently no description for this method. Please help us by [contributing one](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)!

classref-item-separator

classref-method

`void (No return value.)` **\_commit_handle**(id: `int<class_int>`, secondary: `bool<class_bool>`, restore: `Variant<class_Variant>`, cancel: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorNode3DGizmo_private_method__commit_handle>`

Override this method to commit a handle being edited (handles must have been previously added by `add_handles()<class_EditorNode3DGizmo_method_add_handles>`). This usually means creating an `UndoRedo<class_UndoRedo>` action for the change, using the current handle value as "do" and the `restore` argument as "undo".

If the `cancel` argument is `true`, the `restore` value should be directly set, without any `UndoRedo<class_UndoRedo>` action.

The `secondary` argument is `true` when the committed handle is secondary (see `add_handles()<class_EditorNode3DGizmo_method_add_handles>` for more information).

classref-item-separator

classref-method

`void (No return value.)` **\_commit_subgizmos**(ids: `PackedInt32Array<class_PackedInt32Array>`, restores: `Array<class_Array>`\[`Transform3D<class_Transform3D>`\], cancel: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorNode3DGizmo_private_method__commit_subgizmos>`

Override this method to commit a group of subgizmos being edited (see `_subgizmos_intersect_ray()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray>` and `_subgizmos_intersect_frustum()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum>`). This usually means creating an `UndoRedo<class_UndoRedo>` action for the change, using the current transforms as "do" and the `restores` transforms as "undo".

If the `cancel` argument is `true`, the `restores` transforms should be directly set, without any `UndoRedo<class_UndoRedo>` action.

classref-item-separator

classref-method

`String<class_String>` **\_get_handle_name**(id: `int<class_int>`, secondary: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_private_method__get_handle_name>`

Override this method to return the name of an edited handle (handles must have been previously added by `add_handles()<class_EditorNode3DGizmo_method_add_handles>`). Handles can be named for reference to the user when editing.

The `secondary` argument is `true` when the requested handle is secondary (see `add_handles()<class_EditorNode3DGizmo_method_add_handles>` for more information).

classref-item-separator

classref-method

`Variant<class_Variant>` **\_get_handle_value**(id: `int<class_int>`, secondary: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_private_method__get_handle_value>`

Override this method to return the current value of a handle. This value will be requested at the start of an edit and used as the `restore` argument in `_commit_handle()<class_EditorNode3DGizmo_private_method__commit_handle>`.

The `secondary` argument is `true` when the requested handle is secondary (see `add_handles()<class_EditorNode3DGizmo_method_add_handles>` for more information).

classref-item-separator

classref-method

`Transform3D<class_Transform3D>` **\_get_subgizmo_transform**(id: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_private_method__get_subgizmo_transform>`

Override this method to return the current transform of a subgizmo. This transform will be requested at the start of an edit and used as the `restore` argument in `_commit_subgizmos()<class_EditorNode3DGizmo_private_method__commit_subgizmos>`.

classref-item-separator

classref-method

`bool<class_bool>` **\_is_handle_highlighted**(id: `int<class_int>`, secondary: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_private_method__is_handle_highlighted>`

Override this method to return `true` whenever the given handle should be highlighted in the editor.

The `secondary` argument is `true` when the requested handle is secondary (see `add_handles()<class_EditorNode3DGizmo_method_add_handles>` for more information).

classref-item-separator

classref-method

`void (No return value.)` **\_redraw**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorNode3DGizmo_private_method__redraw>`

Override this method to add all the gizmo elements whenever a gizmo update is requested. It's common to call `clear()<class_EditorNode3DGizmo_method_clear>` at the beginning of this method and then add visual elements depending on the node's properties.

classref-item-separator

classref-method

`void (No return value.)` **\_set_handle**(id: `int<class_int>`, secondary: `bool<class_bool>`, camera: `Camera3D<class_Camera3D>`, point: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorNode3DGizmo_private_method__set_handle>`

Override this method to update the node properties when the user drags a gizmo handle (previously added with `add_handles()<class_EditorNode3DGizmo_method_add_handles>`). The provided `point` is the mouse position in screen coordinates and the `camera` can be used to convert it to raycasts.

The `secondary` argument is `true` when the edited handle is secondary (see `add_handles()<class_EditorNode3DGizmo_method_add_handles>` for more information).

classref-item-separator

classref-method

`void (No return value.)` **\_set_subgizmo_transform**(id: `int<class_int>`, transform: `Transform3D<class_Transform3D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorNode3DGizmo_private_method__set_subgizmo_transform>`

Override this method to update the node properties during subgizmo editing (see `_subgizmos_intersect_ray()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray>` and `_subgizmos_intersect_frustum()<class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum>`). The `transform` is given in the `Node3D<class_Node3D>`'s local coordinate system.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **\_subgizmos_intersect_frustum**(camera: `Camera3D<class_Camera3D>`, frustum: `Array<class_Array>`\[`Plane<class_Plane>`\]) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_private_method__subgizmos_intersect_frustum>`

Override this method to allow selecting subgizmos using mouse drag box selection. Given a `camera` and a `frustum`, this method should return which subgizmos are contained within the frustum. The `frustum` argument consists of an array with all the `Plane<class_Plane>`s that make up the selection frustum. The returned value should contain a list of unique subgizmo identifiers, which can have any non-negative value and will be used in other virtual methods like `_get_subgizmo_transform()<class_EditorNode3DGizmo_private_method__get_subgizmo_transform>` or `_commit_subgizmos()<class_EditorNode3DGizmo_private_method__commit_subgizmos>`.

classref-item-separator

classref-method

`int<class_int>` **\_subgizmos_intersect_ray**(camera: `Camera3D<class_Camera3D>`, point: `Vector2<class_Vector2>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_private_method__subgizmos_intersect_ray>`

Override this method to allow selecting subgizmos using mouse clicks. Given a `camera` and a `point` in screen coordinates, this method should return which subgizmo should be selected. The returned value should be a unique subgizmo identifier, which can have any non-negative value and will be used in other virtual methods like `_get_subgizmo_transform()<class_EditorNode3DGizmo_private_method__get_subgizmo_transform>` or `_commit_subgizmos()<class_EditorNode3DGizmo_private_method__commit_subgizmos>`.

classref-item-separator

classref-method

`void (No return value.)` **add_collision_segments**(segments: `PackedVector3Array<class_PackedVector3Array>`) `🔗<class_EditorNode3DGizmo_method_add_collision_segments>`

Adds the specified `segments` to the gizmo's collision shape for picking. Call this method during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **add_collision_triangles**(triangles: `TriangleMesh<class_TriangleMesh>`) `🔗<class_EditorNode3DGizmo_method_add_collision_triangles>`

Adds collision triangles to the gizmo for picking. A `TriangleMesh<class_TriangleMesh>` can be generated from a regular `Mesh<class_Mesh>` too. Call this method during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **add_handles**(handles: `PackedVector3Array<class_PackedVector3Array>`, material: `Material<class_Material>`, ids: `PackedInt32Array<class_PackedInt32Array>`, billboard: `bool<class_bool>` = false, secondary: `bool<class_bool>` = false) `🔗<class_EditorNode3DGizmo_method_add_handles>`

Adds a list of handles (points) which can be used to edit the properties of the gizmo's `Node3D<class_Node3D>`. The `ids` argument can be used to specify a custom identifier for each handle, if an empty array is passed, the ids will be assigned automatically from the `handles` argument order.

The `secondary` argument marks the added handles as secondary, meaning they will normally have lower selection priority than regular handles. When the user is holding the shift key secondary handles will switch to have higher priority than regular handles. This change in priority can be used to place multiple handles at the same point while still giving the user control on their selection.

There are virtual methods which will be called upon editing of these handles. Call this method during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **add_lines**(lines: `PackedVector3Array<class_PackedVector3Array>`, material: `Material<class_Material>`, billboard: `bool<class_bool>` = false, modulate: `Color<class_Color>` = Color(1, 1, 1, 1)) `🔗<class_EditorNode3DGizmo_method_add_lines>`

Adds lines to the gizmo (as sets of 2 points), with a given material. The lines are used for visualizing the gizmo. Call this method during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **add_mesh**(mesh: `Mesh<class_Mesh>`, material: `Material<class_Material>` = null, transform: `Transform3D<class_Transform3D>` = Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0), skeleton: `SkinReference<class_SkinReference>` = null) `🔗<class_EditorNode3DGizmo_method_add_mesh>`

Adds a mesh to the gizmo with the specified `material`, local `transform` and `skeleton`. Call this method during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **add_unscaled_billboard**(material: `Material<class_Material>`, default_scale: `float<class_float>` = 1, modulate: `Color<class_Color>` = Color(1, 1, 1, 1)) `🔗<class_EditorNode3DGizmo_method_add_unscaled_billboard>`

Adds an unscaled billboard for visualization and selection. Call this method during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_EditorNode3DGizmo_method_clear>`

Removes everything in the gizmo including meshes, collisions and handles.

classref-item-separator

classref-method

`Node3D<class_Node3D>` **get_node_3d**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_method_get_node_3d>`

Returns the `Node3D<class_Node3D>` node associated with this gizmo.

classref-item-separator

classref-method

`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>` **get_plugin**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_method_get_plugin>`

Returns the `EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>` that owns this gizmo. It's useful to retrieve materials using `EditorNode3DGizmoPlugin.get_material()<class_EditorNode3DGizmoPlugin_method_get_material>`.

classref-item-separator

classref-method

`PackedInt32Array<class_PackedInt32Array>` **get_subgizmo_selection**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_method_get_subgizmo_selection>`

Returns a list of the currently selected subgizmos. Can be used to highlight selected elements during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_subgizmo_selected**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorNode3DGizmo_method_is_subgizmo_selected>`

Returns `true` if the given subgizmo is currently selected. Can be used to highlight selected elements during `_redraw()<class_EditorNode3DGizmo_private_method__redraw>`.

classref-item-separator

classref-method

`void (No return value.)` **set_hidden**(hidden: `bool<class_bool>`) `🔗<class_EditorNode3DGizmo_method_set_hidden>`

Sets the gizmo's hidden state. If `true`, the gizmo will be hidden. If `false`, it will be shown.

classref-item-separator

classref-method

`void (No return value.)` **set_node_3d**(node: `Node<class_Node>`) `🔗<class_EditorNode3DGizmo_method_set_node_3d>`

Sets the reference `Node3D<class_Node3D>` node for the gizmo. `node` must inherit from `Node3D<class_Node3D>`.