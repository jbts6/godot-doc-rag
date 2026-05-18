github_url
hide

# SplitContainer

**Inherits:** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `HSplitContainer<class_HSplitContainer>`, `VSplitContainer<class_VSplitContainer>`

A container that arranges child controls horizontally or vertically and provides grabbers for adjusting the split ratios between them.

classref-introduction-group

## Description

A container that arranges child controls horizontally or vertically and creates grabbers between them. The grabbers can be dragged around to change the size relations between the child controls.

classref-introduction-group

## Tutorials

- `Using Containers <../tutorials/ui/gui_containers>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-reftable-group

## Theme Properties

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**drag_ended**() `🔗<class_SplitContainer_signal_drag_ended>`

Emitted when the user ends dragging.

classref-item-separator

classref-signal

**drag_started**() `🔗<class_SplitContainer_signal_drag_started>`

Emitted when the user starts dragging.

classref-item-separator

classref-signal

**dragged**(offset: `int<class_int>`) `🔗<class_SplitContainer_signal_dragged>`

Emitted when any dragger is dragged by user.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **DraggerVisibility**: `🔗<enum_SplitContainer_DraggerVisibility>`

classref-enumeration-constant

`DraggerVisibility<enum_SplitContainer_DraggerVisibility>` **DRAGGER_VISIBLE** = `0`

The split dragger icon is always visible when `autohide<class_SplitContainer_theme_constant_autohide>` is `false`, otherwise visible only when the cursor hovers it.

The size of the grabber icon determines the minimum `separation<class_SplitContainer_theme_constant_separation>`.

The dragger icon is automatically hidden if the length of the grabber icon is longer than the split bar.

classref-enumeration-constant

`DraggerVisibility<enum_SplitContainer_DraggerVisibility>` **DRAGGER_HIDDEN** = `1`

The split dragger icon is never visible regardless of the value of `autohide<class_SplitContainer_theme_constant_autohide>`.

The size of the grabber icon determines the minimum `separation<class_SplitContainer_theme_constant_separation>`.

classref-enumeration-constant

`DraggerVisibility<enum_SplitContainer_DraggerVisibility>` **DRAGGER_HIDDEN_COLLAPSED** = `2`

The split dragger icon is not visible, and the split bar is collapsed to zero thickness.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **collapsed** = `false` `🔗<class_SplitContainer_property_collapsed>`

classref-property-setget

- `void (No return value.)` **set_collapsed**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_collapsed**()

If `true`, the draggers will be disabled and the children will be sized as if all `split_offsets<class_SplitContainer_property_split_offsets>` were `0`.

classref-item-separator

classref-property

`bool<class_bool>` **drag_area_highlight_in_editor** = `false` `🔗<class_SplitContainer_property_drag_area_highlight_in_editor>`

classref-property-setget

- `void (No return value.)` **set_drag_area_highlight_in_editor**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_drag_area_highlight_in_editor_enabled**()

Highlights the drag area `Rect2<class_Rect2>` so you can see where it is during development. The drag area is gold if `dragging_enabled<class_SplitContainer_property_dragging_enabled>` is `true`, and red if `false`.

classref-item-separator

classref-property

`int<class_int>` **drag_area_margin_begin** = `0` `🔗<class_SplitContainer_property_drag_area_margin_begin>`

classref-property-setget

- `void (No return value.)` **set_drag_area_margin_begin**(value: `int<class_int>`)
- `int<class_int>` **get_drag_area_margin_begin**()

Reduces the size of the drag area and split bar `split_bar_background<class_SplitContainer_theme_style_split_bar_background>` at the beginning of the container.

classref-item-separator

classref-property

`int<class_int>` **drag_area_margin_end** = `0` `🔗<class_SplitContainer_property_drag_area_margin_end>`

classref-property-setget

- `void (No return value.)` **set_drag_area_margin_end**(value: `int<class_int>`)
- `int<class_int>` **get_drag_area_margin_end**()

Reduces the size of the drag area and split bar `split_bar_background<class_SplitContainer_theme_style_split_bar_background>` at the end of the container.

classref-item-separator

classref-property

`int<class_int>` **drag_area_offset** = `0` `🔗<class_SplitContainer_property_drag_area_offset>`

classref-property-setget

- `void (No return value.)` **set_drag_area_offset**(value: `int<class_int>`)
- `int<class_int>` **get_drag_area_offset**()

Shifts the drag area in the axis of the container to prevent the drag area from overlapping the `ScrollBar<class_ScrollBar>` or other selectable `Control<class_Control>` of a child node.

classref-item-separator

classref-property

`bool<class_bool>` **drag_nested_intersections** = `false` `🔗<class_SplitContainer_property_drag_nested_intersections>`

classref-property-setget

- `void (No return value.)` **set_drag_nested_intersections**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_dragging_nested_intersections**()

Adds extra draggers at the intersection of the draggers of two SplitContainers to allow dragging both at once. This must be set to `true` for both SplitContainers, and one needs to be a descendant of the other. They also must be orthogonal (their `vertical<class_SplitContainer_property_vertical>` are different) and the descendant must be next to at least one of the ancestor's draggers (within `minimum_grab_thickness<class_SplitContainer_theme_constant_minimum_grab_thickness>`).

classref-item-separator

classref-property

`DraggerVisibility<enum_SplitContainer_DraggerVisibility>` **dragger_visibility** = `0` `🔗<class_SplitContainer_property_dragger_visibility>`

classref-property-setget

- `void (No return value.)` **set_dragger_visibility**(value: `DraggerVisibility<enum_SplitContainer_DraggerVisibility>`)
- `DraggerVisibility<enum_SplitContainer_DraggerVisibility>` **get_dragger_visibility**()

Determines the dragger's visibility. This property does not determine whether dragging is enabled or not. Use `dragging_enabled<class_SplitContainer_property_dragging_enabled>` for that.

classref-item-separator

classref-property

`bool<class_bool>` **dragging_enabled** = `true` `🔗<class_SplitContainer_property_dragging_enabled>`

classref-property-setget

- `void (No return value.)` **set_dragging_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_dragging_enabled**()

Enables or disables split dragging.

classref-item-separator

classref-property

`int<class_int>` **split_offset** = `0` `🔗<class_SplitContainer_property_split_offset>`

classref-property-setget

- `void (No return value.)` **set_split_offset**(value: `int<class_int>`)
- `int<class_int>` **get_split_offset**()

**Deprecated:** Use `split_offsets<class_SplitContainer_property_split_offsets>` instead. The first element of the array is the split offset between the first two children.

The first element of `split_offsets<class_SplitContainer_property_split_offsets>`.

classref-item-separator

classref-property

`PackedInt32Array<class_PackedInt32Array>` **split_offsets** = `PackedInt32Array(0)` `🔗<class_SplitContainer_property_split_offsets>`

classref-property-setget

- `void (No return value.)` **set_split_offsets**(value: `PackedInt32Array<class_PackedInt32Array>`)
- `PackedInt32Array<class_PackedInt32Array>` **get_split_offsets**()

Offsets for each dragger in pixels. Each one is the offset of the split between the `Control<class_Control>` nodes before and after the dragger, with `0` being the default position. The default position is based on the `Control<class_Control>` nodes expand flags and minimum sizes. See `Control.size_flags_horizontal<class_Control_property_size_flags_horizontal>`, `Control.size_flags_vertical<class_Control_property_size_flags_vertical>`, and `Control.size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>`.

If none of the `Control<class_Control>` nodes before the dragger are expanded, the default position will be at the start of the **SplitContainer**. If none of the `Control<class_Control>` nodes after the dragger are expanded, the default position will be at the end of the **SplitContainer**. If the dragger is in between expanded `Control<class_Control>` nodes, the default position will be in the middle, based on the `Control.size_flags_stretch_ratio<class_Control_property_size_flags_stretch_ratio>`s and minimum sizes.

**Note:** If the split offsets cause `Control<class_Control>` nodes to overlap, the first split will take priority when resolving the positions.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedInt32Array<class_PackedInt32Array>` for more details.

classref-item-separator

classref-property

`bool<class_bool>` **touch_dragger_enabled** = `false` `🔗<class_SplitContainer_property_touch_dragger_enabled>`

classref-property-setget

- `void (No return value.)` **set_touch_dragger_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_touch_dragger_enabled**()

If `true`, a touch-friendly drag handle will be enabled for better usability on smaller screens. Unlike the standard grabber, this drag handle overlaps the **SplitContainer**'s children and does not affect their minimum separation. The standard grabber will no longer be drawn when this option is enabled.

classref-item-separator

classref-property

`bool<class_bool>` **vertical** = `false` `🔗<class_SplitContainer_property_vertical>`

classref-property-setget

- `void (No return value.)` **set_vertical**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_vertical**()

If `true`, the **SplitContainer** will arrange its children vertically, rather than horizontally.

Can't be changed when using `HSplitContainer<class_HSplitContainer>` and `VSplitContainer<class_VSplitContainer>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clamp_split_offset**(priority_index: `int<class_int>` = 0) `🔗<class_SplitContainer_method_clamp_split_offset>`

Clamps the `split_offsets<class_SplitContainer_property_split_offsets>` values to ensure they are within valid ranges and do not overlap with each other. When overlaps occur, this method prioritizes one split offset (at index `priority_index`) by clamping any overlapping split offsets to it.

classref-item-separator

classref-method

`Control<class_Control>` **get_drag_area_control**() `🔗<class_SplitContainer_method_get_drag_area_control>`

**Deprecated:** Use the first element of `get_drag_area_controls()<class_SplitContainer_method_get_drag_area_controls>` instead.

Returns the drag area `Control<class_Control>`. For example, you can move a pre-configured button into the drag area `Control<class_Control>` so that it rides along with the split bar. Try setting the `Button<class_Button>` anchors to `center` prior to the `reparent()` call.

    $BarnacleButton.reparent($SplitContainer.get_drag_area_control())

**Note:** The drag area `Control<class_Control>` is drawn over the **SplitContainer**'s children, so `CanvasItem<class_CanvasItem>` draw objects called from the `Control<class_Control>` and children added to the `Control<class_Control>` will also appear over the **SplitContainer**'s children. Try setting `Control.mouse_filter<class_Control_property_mouse_filter>` of custom children to `Control.MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>` to prevent blocking the mouse from dragging if desired.

**Warning:** This is a required internal node, removing and freeing it may cause a crash.

classref-item-separator

classref-method

`Array<class_Array>`\[`Control<class_Control>`\] **get_drag_area_controls**() `🔗<class_SplitContainer_method_get_drag_area_controls>`

Returns an `Array<class_Array>` of the drag area `Control<class_Control>`s. These are the interactable `Control<class_Control>` nodes between each child. For example, this can be used to add a pre-configured button to a drag area `Control<class_Control>` so that it rides along with the split bar. Try setting the `Button<class_Button>` anchors to `center` prior to the `Node.reparent()<class_Node_method_reparent>` call.

    $BarnacleButton.reparent($SplitContainer.get_drag_area_controls()[0])

**Note:** The drag area `Control<class_Control>`s are drawn over the **SplitContainer**'s children, so `CanvasItem<class_CanvasItem>` draw objects called from a drag area and children added to it will also appear over the **SplitContainer**'s children. Try setting `Control.mouse_filter<class_Control_property_mouse_filter>` of custom children to `Control.MOUSE_FILTER_IGNORE<class_Control_constant_MOUSE_FILTER_IGNORE>` to prevent blocking the mouse from dragging if desired.

**Warning:** These are required internal nodes, removing or freeing them may cause a crash.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **touch_dragger_color** = `Color(1, 1, 1, 0.3)` `🔗<class_SplitContainer_theme_color_touch_dragger_color>`

The color of the touch dragger.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **touch_dragger_hover_color** = `Color(1, 1, 1, 0.6)` `🔗<class_SplitContainer_theme_color_touch_dragger_hover_color>`

The color of the touch dragger when hovered.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **touch_dragger_pressed_color** = `Color(1, 1, 1, 1)` `🔗<class_SplitContainer_theme_color_touch_dragger_pressed_color>`

The color of the touch dragger when pressed.

classref-item-separator

classref-themeproperty

`int<class_int>` **autohide** = `1` `🔗<class_SplitContainer_theme_constant_autohide>`

Boolean value. If `1` (`true`), the grabbers will hide automatically when they aren't under the cursor. If `0` (`false`), the grabbers are always visible. The `dragger_visibility<class_SplitContainer_property_dragger_visibility>` must be `DRAGGER_VISIBLE<class_SplitContainer_constant_DRAGGER_VISIBLE>`.

classref-item-separator

classref-themeproperty

`int<class_int>` **minimum_grab_thickness** = `6` `🔗<class_SplitContainer_theme_constant_minimum_grab_thickness>`

The minimum thickness of the area users can click on to grab a split bar. This ensures that the split bar can still be dragged if `separation<class_SplitContainer_theme_constant_separation>` or `h_grabber<class_SplitContainer_theme_icon_h_grabber>` / `v_grabber<class_SplitContainer_theme_icon_v_grabber>`'s size is too narrow to easily select.

classref-item-separator

classref-themeproperty

`int<class_int>` **separation** = `12` `🔗<class_SplitContainer_theme_constant_separation>`

The split bar thickness, i.e., the gap between each child of the container. This is overridden by the size of the grabber icon if `dragger_visibility<class_SplitContainer_property_dragger_visibility>` is set to `DRAGGER_VISIBLE<class_SplitContainer_constant_DRAGGER_VISIBLE>`, or `DRAGGER_HIDDEN<class_SplitContainer_constant_DRAGGER_HIDDEN>`, and `separation<class_SplitContainer_theme_constant_separation>` is smaller than the size of the grabber icon in the same axis.

**Note:** To obtain `separation<class_SplitContainer_theme_constant_separation>` values less than the size of the grabber icon, for example a `1 px` hairline, set `h_grabber<class_SplitContainer_theme_icon_h_grabber>` or `v_grabber<class_SplitContainer_theme_icon_v_grabber>` to a new `ImageTexture<class_ImageTexture>`, which effectively sets the grabber icon size to `0 px`.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **grabber** `🔗<class_SplitContainer_theme_icon_grabber>`

The icon used for the grabbers drawn in the separations. This is only used in `HSplitContainer<class_HSplitContainer>` and `VSplitContainer<class_VSplitContainer>`. For **SplitContainer**, see `h_grabber<class_SplitContainer_theme_icon_h_grabber>` and `v_grabber<class_SplitContainer_theme_icon_v_grabber>` instead.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **h_grabber** `🔗<class_SplitContainer_theme_icon_h_grabber>`

The icon used for the grabbers drawn in the separations when `vertical<class_SplitContainer_property_vertical>` is `false`.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **h_touch_dragger** `🔗<class_SplitContainer_theme_icon_h_touch_dragger>`

The icon used for the drag handle when `touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>` is `true` and `vertical<class_SplitContainer_property_vertical>` is `false`.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **touch_dragger** `🔗<class_SplitContainer_theme_icon_touch_dragger>`

The icon used for the drag handle when `touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>` is `true`. This is only used in `HSplitContainer<class_HSplitContainer>` and `VSplitContainer<class_VSplitContainer>`. For **SplitContainer**, see `h_touch_dragger<class_SplitContainer_theme_icon_h_touch_dragger>` and `v_touch_dragger<class_SplitContainer_theme_icon_v_touch_dragger>` instead.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **v_grabber** `🔗<class_SplitContainer_theme_icon_v_grabber>`

The icon used for the grabbers drawn in the separations when `vertical<class_SplitContainer_property_vertical>` is `true`.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **v_touch_dragger** `🔗<class_SplitContainer_theme_icon_v_touch_dragger>`

The icon used for the drag handle when `touch_dragger_enabled<class_SplitContainer_property_touch_dragger_enabled>` is `true` and `vertical<class_SplitContainer_property_vertical>` is `true`.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **split_bar_background** `🔗<class_SplitContainer_theme_style_split_bar_background>`

Determines the background of the split bar if its thickness is greater than zero.