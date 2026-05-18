github_url
hide

# TabContainer

**Inherits:** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A container that creates a tab for each child control, displaying only the active tab's control.

classref-introduction-group

## Description

Arranges child controls into a tabbed view, creating a tab for each one. The active tab's corresponding control is made visible, while all other child controls are hidden. Ignores non-control children.

**Note:** The drawing of the clickable tabs is handled by this node; `TabBar<class_TabBar>` is not needed.

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

**active_tab_rearranged**(idx_to: `int<class_int>`) `🔗<class_TabContainer_signal_active_tab_rearranged>`

Emitted when the active tab is rearranged via mouse drag. See `drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`.

classref-item-separator

classref-signal

**pre_popup_pressed**() `🔗<class_TabContainer_signal_pre_popup_pressed>`

Emitted when the **TabContainer**'s `Popup<class_Popup>` button is clicked. See `set_popup()<class_TabContainer_method_set_popup>` for details.

classref-item-separator

classref-signal

**tab_button_pressed**(tab: `int<class_int>`) `🔗<class_TabContainer_signal_tab_button_pressed>`

Emitted when the user clicks on the button icon on this tab.

classref-item-separator

classref-signal

**tab_changed**(tab: `int<class_int>`) `🔗<class_TabContainer_signal_tab_changed>`

Emitted when switching to another tab.

classref-item-separator

classref-signal

**tab_clicked**(tab: `int<class_int>`) `🔗<class_TabContainer_signal_tab_clicked>`

Emitted when a tab is clicked, even if it is the current tab.

classref-item-separator

classref-signal

**tab_hovered**(tab: `int<class_int>`) `🔗<class_TabContainer_signal_tab_hovered>`

Emitted when a tab is hovered by the mouse.

classref-item-separator

classref-signal

**tab_selected**(tab: `int<class_int>`) `🔗<class_TabContainer_signal_tab_selected>`

Emitted when a tab is selected via click, directional input, or script, even if it is the current tab.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **TabPosition**: `🔗<enum_TabContainer_TabPosition>`

classref-enumeration-constant

`TabPosition<enum_TabContainer_TabPosition>` **POSITION_TOP** = `0`

Places the tab bar at the top.

classref-enumeration-constant

`TabPosition<enum_TabContainer_TabPosition>` **POSITION_BOTTOM** = `1`

Places the tab bar at the bottom. The tab bar's `StyleBox<class_StyleBox>` will be flipped vertically.

classref-enumeration-constant

`TabPosition<enum_TabContainer_TabPosition>` **POSITION_MAX** = `2`

Represents the size of the `TabPosition<enum_TabContainer_TabPosition>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **all_tabs_in_front** = `false` `🔗<class_TabContainer_property_all_tabs_in_front>`

classref-property-setget

- `void (No return value.)` **set_all_tabs_in_front**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_all_tabs_in_front**()

**Deprecated:** Due to internal changes this doesn't do anything anymore, as they're always in front.

This doesn't do anything.

classref-item-separator

classref-property

`bool<class_bool>` **clip_tabs** = `true` `🔗<class_TabContainer_property_clip_tabs>`

classref-property-setget

- `void (No return value.)` **set_clip_tabs**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_clip_tabs**()

If `true`, tabs overflowing this node's width will be hidden, displaying two navigation buttons instead. Otherwise, this node's minimum size is updated so that all tabs are visible.

classref-item-separator

classref-property

`int<class_int>` **current_tab** = `-1` `🔗<class_TabContainer_property_current_tab>`

classref-property-setget

- `void (No return value.)` **set_current_tab**(value: `int<class_int>`)
- `int<class_int>` **get_current_tab**()

The current tab index. When set, this index's `Control<class_Control>` node's `visible` property is set to `true` and all others are set to `false`.

A value of `-1` means that no tab is selected.

classref-item-separator

classref-property

`bool<class_bool>` **deselect_enabled** = `false` `🔗<class_TabContainer_property_deselect_enabled>`

classref-property-setget

- `void (No return value.)` **set_deselect_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_deselect_enabled**()

If `true`, all tabs can be deselected so that no tab is selected. Click on the `current_tab<class_TabContainer_property_current_tab>` to deselect it.

Only the tab header will be shown if no tabs are selected.

classref-item-separator

classref-property

`bool<class_bool>` **drag_to_rearrange_enabled** = `false` `🔗<class_TabContainer_property_drag_to_rearrange_enabled>`

classref-property-setget

- `void (No return value.)` **set_drag_to_rearrange_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_drag_to_rearrange_enabled**()

If `true`, tabs can be rearranged with mouse drag.

classref-item-separator

classref-property

`bool<class_bool>` **switch_on_drag_hover** = `true` `🔗<class_TabContainer_property_switch_on_drag_hover>`

classref-property-setget

- `void (No return value.)` **set_switch_on_drag_hover**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_switch_on_drag_hover**()

If `true`, hovering over a tab while dragging something will switch to that tab. Does not have effect when hovering another tab to rearrange.

classref-item-separator

classref-property

`AlignmentMode<enum_TabBar_AlignmentMode>` **tab_alignment** = `0` `🔗<class_TabContainer_property_tab_alignment>`

classref-property-setget

- `void (No return value.)` **set_tab_alignment**(value: `AlignmentMode<enum_TabBar_AlignmentMode>`)
- `AlignmentMode<enum_TabBar_AlignmentMode>` **get_tab_alignment**()

The position at which tabs will be placed.

classref-item-separator

classref-property

`FocusMode<enum_Control_FocusMode>` **tab_focus_mode** = `2` `🔗<class_TabContainer_property_tab_focus_mode>`

classref-property-setget

- `void (No return value.)` **set_tab_focus_mode**(value: `FocusMode<enum_Control_FocusMode>`)
- `FocusMode<enum_Control_FocusMode>` **get_tab_focus_mode**()

The focus access mode for the internal `TabBar<class_TabBar>` node.

classref-item-separator

classref-property

`bool<class_bool>` **tab\_{index}/disabled** = `false` `🔗<class_TabContainer_property_tab_{index}/disabled>`

If `true`, the tab at `index` is disabled.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

classref-item-separator

classref-property

`bool<class_bool>` **tab\_{index}/hidden** = `false` `🔗<class_TabContainer_property_tab_{index}/hidden>`

If `true`, the tab at `index` is hidden.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **tab\_{index}/icon** `🔗<class_TabContainer_property_tab_{index}/icon>`

The title text of the tab at `index`.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

classref-item-separator

classref-property

`String<class_String>` **tab\_{index}/title** = `""` `🔗<class_TabContainer_property_tab_{index}/title>`

The tooltip text of the tab at `index`.

**Note:** `index` is a value in the `0 .. get_tab_count() - 1` range.

classref-item-separator

classref-property

`TabPosition<enum_TabContainer_TabPosition>` **tabs_position** = `0` `🔗<class_TabContainer_property_tabs_position>`

classref-property-setget

- `void (No return value.)` **set_tabs_position**(value: `TabPosition<enum_TabContainer_TabPosition>`)
- `TabPosition<enum_TabContainer_TabPosition>` **get_tabs_position**()

The horizontal alignment of the tabs.

classref-item-separator

classref-property

`int<class_int>` **tabs_rearrange_group** = `-1` `🔗<class_TabContainer_property_tabs_rearrange_group>`

classref-property-setget

- `void (No return value.)` **set_tabs_rearrange_group**(value: `int<class_int>`)
- `int<class_int>` **get_tabs_rearrange_group**()

**TabContainer**s with the same rearrange group ID will allow dragging the tabs between them. Enable drag with `drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`.

Setting this to `-1` will disable rearranging between **TabContainer**s.

classref-item-separator

classref-property

`bool<class_bool>` **tabs_visible** = `true` `🔗<class_TabContainer_property_tabs_visible>`

classref-property-setget

- `void (No return value.)` **set_tabs_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **are_tabs_visible**()

If `true`, tabs are visible. If `false`, tabs' content and titles are hidden.

classref-item-separator

classref-property

`bool<class_bool>` **use_hidden_tabs_for_min_size** = `false` `🔗<class_TabContainer_property_use_hidden_tabs_for_min_size>`

classref-property-setget

- `void (No return value.)` **set_use_hidden_tabs_for_min_size**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_hidden_tabs_for_min_size**()

If `true`, child `Control<class_Control>` nodes that are hidden have their minimum size take into account in the total, instead of only the currently visible one.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Control<class_Control>` **get_current_tab_control**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_current_tab_control>`

Returns the child `Control<class_Control>` node located at the active tab index.

classref-item-separator

classref-method

`Popup<class_Popup>` **get_popup**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_popup>`

Returns the `Popup<class_Popup>` node instance if one has been set already with `set_popup()<class_TabContainer_method_set_popup>`.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `Window.visible<class_Window_property_visible>` property.

classref-item-separator

classref-method

`int<class_int>` **get_previous_tab**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_previous_tab>`

Returns the previously active tab index.

classref-item-separator

classref-method

`TabBar<class_TabBar>` **get_tab_bar**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_bar>`

Returns the `TabBar<class_TabBar>` contained in this container.

**Warning:** This is a required internal node, removing and freeing it or editing its tabs may cause a crash. If you wish to edit the tabs, use the methods provided in **TabContainer**.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_tab_button_icon**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_button_icon>`

Returns the button icon from the tab at index `tab_idx`.

classref-item-separator

classref-method

`Control<class_Control>` **get_tab_control**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_control>`

Returns the `Control<class_Control>` node from the tab at index `tab_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_tab_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_count>`

Returns the number of tabs.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_tab_icon**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_icon>`

Returns the `Texture2D<class_Texture2D>` for the tab at index `tab_idx` or `null` if the tab has no `Texture2D<class_Texture2D>`.

classref-item-separator

classref-method

`int<class_int>` **get_tab_icon_max_width**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_icon_max_width>`

Returns the maximum allowed width of the icon for the tab at index `tab_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_tab_idx_at_point**(point: `Vector2<class_Vector2>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_idx_at_point>`

Returns the index of the tab at local coordinates `point`. Returns `-1` if the point is outside the control boundaries or if there's no tab at the queried position.

classref-item-separator

classref-method

`int<class_int>` **get_tab_idx_from_control**(control: `Control<class_Control>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_idx_from_control>`

Returns the index of the tab tied to the given `control`. The control must be a child of the **TabContainer**.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_tab_metadata**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_metadata>`

Returns the metadata value set to the tab at index `tab_idx` using `set_tab_metadata()<class_TabContainer_method_set_tab_metadata>`. If no metadata was previously set, returns `null` by default.

classref-item-separator

classref-method

`String<class_String>` **get_tab_title**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_title>`

Returns the title of the tab at index `tab_idx`. Tab titles default to the name of the indexed child node, but this can be overridden with `set_tab_title()<class_TabContainer_method_set_tab_title>`.

classref-item-separator

classref-method

`String<class_String>` **get_tab_tooltip**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_get_tab_tooltip>`

Returns the tooltip text of the tab at index `tab_idx`.

classref-item-separator

classref-method

`bool<class_bool>` **is_tab_disabled**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_is_tab_disabled>`

Returns `true` if the tab at index `tab_idx` is disabled.

classref-item-separator

classref-method

`bool<class_bool>` **is_tab_hidden**(tab_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TabContainer_method_is_tab_hidden>`

Returns `true` if the tab at index `tab_idx` is hidden.

classref-item-separator

classref-method

`bool<class_bool>` **select_next_available**() `🔗<class_TabContainer_method_select_next_available>`

Selects the first available tab with greater index than the currently selected. Returns `true` if tab selection changed.

classref-item-separator

classref-method

`bool<class_bool>` **select_previous_available**() `🔗<class_TabContainer_method_select_previous_available>`

Selects the first available tab with lower index than the currently selected. Returns `true` if tab selection changed.

classref-item-separator

classref-method

`void (No return value.)` **set_popup**(popup: `Node<class_Node>`) `🔗<class_TabContainer_method_set_popup>`

If set on a `Popup<class_Popup>` node instance, a popup menu icon appears in the top-right corner of the **TabContainer** (setting it to `null` will make it go away). Clicking it will expand the `Popup<class_Popup>` node.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_button_icon**(tab_idx: `int<class_int>`, icon: `Texture2D<class_Texture2D>`) `🔗<class_TabContainer_method_set_tab_button_icon>`

Sets the button icon from the tab at index `tab_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_disabled**(tab_idx: `int<class_int>`, disabled: `bool<class_bool>`) `🔗<class_TabContainer_method_set_tab_disabled>`

If `disabled` is `true`, disables the tab at index `tab_idx`, making it non-interactable.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_hidden**(tab_idx: `int<class_int>`, hidden: `bool<class_bool>`) `🔗<class_TabContainer_method_set_tab_hidden>`

If `hidden` is `true`, hides the tab at index `tab_idx`, making it disappear from the tab area.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_icon**(tab_idx: `int<class_int>`, icon: `Texture2D<class_Texture2D>`) `🔗<class_TabContainer_method_set_tab_icon>`

Sets an icon for the tab at index `tab_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_icon_max_width**(tab_idx: `int<class_int>`, width: `int<class_int>`) `🔗<class_TabContainer_method_set_tab_icon_max_width>`

Sets the maximum allowed width of the icon for the tab at index `tab_idx`. This limit is applied on top of the default size of the icon and on top of `icon_max_width<class_TabContainer_theme_constant_icon_max_width>`. The height is adjusted according to the icon's ratio.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_metadata**(tab_idx: `int<class_int>`, metadata: `Variant<class_Variant>`) `🔗<class_TabContainer_method_set_tab_metadata>`

Sets the metadata value for the tab at index `tab_idx`, which can be retrieved later using `get_tab_metadata()<class_TabContainer_method_get_tab_metadata>`.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_title**(tab_idx: `int<class_int>`, title: `String<class_String>`) `🔗<class_TabContainer_method_set_tab_title>`

Sets a custom title for the tab at index `tab_idx` (tab titles default to the name of the indexed child node). Set it back to the child's name to make the tab default to it again.

classref-item-separator

classref-method

`void (No return value.)` **set_tab_tooltip**(tab_idx: `int<class_int>`, tooltip: `String<class_String>`) `🔗<class_TabContainer_method_set_tab_tooltip>`

Sets a custom tooltip text for tab at index `tab_idx`.

**Note:** By default, if the `tooltip` is empty and the tab text is truncated (not all characters fit into the tab), the title will be displayed as a tooltip. To hide the tooltip, assign `" "` as the `tooltip` text.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **drop_mark_color** = `Color(1, 1, 1, 1)` `🔗<class_TabContainer_theme_color_drop_mark_color>`

Modulation color for the `drop_mark<class_TabContainer_theme_icon_drop_mark>` icon.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)` `🔗<class_TabContainer_theme_color_font_disabled_color>`

Font color of disabled tabs.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_hovered_color** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_TabContainer_theme_color_font_hovered_color>`

Font color of the currently hovered tab. Does not apply to the selected tab.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_outline_color** = `Color(0, 0, 0, 1)` `🔗<class_TabContainer_theme_color_font_outline_color>`

The tint of text outline of the tab name.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_selected_color** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_TabContainer_theme_color_font_selected_color>`

Font color of the currently selected tab.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_unselected_color** = `Color(0.7, 0.7, 0.7, 1)` `🔗<class_TabContainer_theme_color_font_unselected_color>`

Font color of the other, unselected tabs.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **icon_disabled_color** = `Color(1, 1, 1, 1)` `🔗<class_TabContainer_theme_color_icon_disabled_color>`

Icon color of disabled tabs.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **icon_hovered_color** = `Color(1, 1, 1, 1)` `🔗<class_TabContainer_theme_color_icon_hovered_color>`

Icon color of the currently hovered tab. Does not apply to the selected tab.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **icon_selected_color** = `Color(1, 1, 1, 1)` `🔗<class_TabContainer_theme_color_icon_selected_color>`

Icon color of the currently selected tab.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **icon_unselected_color** = `Color(1, 1, 1, 1)` `🔗<class_TabContainer_theme_color_icon_unselected_color>`

Icon color of the other, unselected tabs.

classref-item-separator

classref-themeproperty

`int<class_int>` **icon_max_width** = `0` `🔗<class_TabContainer_theme_constant_icon_max_width>`

The maximum allowed width of the tab's icon. This limit is applied on top of the default size of the icon, but before the value set with `TabBar.set_tab_icon_max_width()<class_TabBar_method_set_tab_icon_max_width>`. The height is adjusted according to the icon's ratio.

classref-item-separator

classref-themeproperty

`int<class_int>` **icon_separation** = `4` `🔗<class_TabContainer_theme_constant_icon_separation>`

Space between tab's name and its icon.

classref-item-separator

classref-themeproperty

`int<class_int>` **outline_size** = `0` `🔗<class_TabContainer_theme_constant_outline_size>`

The size of the tab text outline.

**Note:** If using a font with `FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>` enabled, its `FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>` must be set to at least *twice* the value of `outline_size<class_TabContainer_theme_constant_outline_size>` for outline rendering to look correct. Otherwise, the outline may appear to be cut off earlier than intended.

classref-item-separator

classref-themeproperty

`int<class_int>` **side_margin** = `8` `🔗<class_TabContainer_theme_constant_side_margin>`

The space at the left or right edges of the tab bar, accordingly with the current `tab_alignment<class_TabContainer_property_tab_alignment>`.

The margin is ignored with `TabBar.ALIGNMENT_RIGHT<class_TabBar_constant_ALIGNMENT_RIGHT>` if the tabs are clipped (see `clip_tabs<class_TabContainer_property_clip_tabs>`) or a popup has been set (see `set_popup()<class_TabContainer_method_set_popup>`). The margin is always ignored with `TabBar.ALIGNMENT_CENTER<class_TabBar_constant_ALIGNMENT_CENTER>`.

classref-item-separator

classref-themeproperty

`int<class_int>` **tab_separation** = `0` `🔗<class_TabContainer_theme_constant_tab_separation>`

The space between tabs in the tab bar.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **font** `🔗<class_TabContainer_theme_font_font>`

The font used to draw tab names.

classref-item-separator

classref-themeproperty

`int<class_int>` **font_size** `🔗<class_TabContainer_theme_font_size_font_size>`

Font size of the tab names.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **decrement** `🔗<class_TabContainer_theme_icon_decrement>`

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the first tab is visible), it appears semi-transparent.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **decrement_highlight** `🔗<class_TabContainer_theme_icon_decrement_highlight>`

Icon for the left arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **drop_mark** `🔗<class_TabContainer_theme_icon_drop_mark>`

Icon shown to indicate where a dragged tab will be dropped (see `drag_to_rearrange_enabled<class_TabContainer_property_drag_to_rearrange_enabled>`).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **increment** `🔗<class_TabContainer_theme_icon_increment>`

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. When the button is disabled (i.e. the last tab is visible) it appears semi-transparent.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **increment_highlight** `🔗<class_TabContainer_theme_icon_increment_highlight>`

Icon for the right arrow button that appears when there are too many tabs to fit in the container width. Used when the button is being hovered with the cursor.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **menu** `🔗<class_TabContainer_theme_icon_menu>`

The icon for the menu button (see `set_popup()<class_TabContainer_method_set_popup>`).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **menu_highlight** `🔗<class_TabContainer_theme_icon_menu_highlight>`

The icon for the menu button (see `set_popup()<class_TabContainer_method_set_popup>`) when it's being hovered with the cursor.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel** `🔗<class_TabContainer_theme_style_panel>`

The style for the background fill.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **tab_disabled** `🔗<class_TabContainer_theme_style_tab_disabled>`

The style of disabled tabs.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **tab_focus** `🔗<class_TabContainer_theme_style_tab_focus>`

`StyleBox<class_StyleBox>` used when the `TabBar<class_TabBar>` is focused. The `tab_focus<class_TabContainer_theme_style_tab_focus>` `StyleBox<class_StyleBox>` is displayed *over* the base `StyleBox<class_StyleBox>` of the selected tab, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the base `StyleBox<class_StyleBox>` remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **tab_hovered** `🔗<class_TabContainer_theme_style_tab_hovered>`

The style of the currently hovered tab.

**Note:** This style will be drawn with the same width as `tab_unselected<class_TabContainer_theme_style_tab_unselected>` at minimum.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **tab_selected** `🔗<class_TabContainer_theme_style_tab_selected>`

The style of the currently selected tab.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **tab_unselected** `🔗<class_TabContainer_theme_style_tab_unselected>`

The style of the other, unselected tabs.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **tabbar_background** `🔗<class_TabContainer_theme_style_tabbar_background>`

The style for the background fill of the `TabBar<class_TabBar>` area.