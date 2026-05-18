github_url
hide

# FoldableContainer

**Inherits:** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A container that can be expanded/collapsed.

classref-introduction-group

## Description

A container that can be expanded/collapsed, with a title that can be filled with controls, such as buttons. This is also called an accordion.

The title can be positioned at the top or bottom of the container. The container can be expanded or collapsed by clicking the title or by pressing `ui_accept` when focused. Child control nodes are hidden when the container is collapsed. Ignores non-control children.

A FoldableContainer can be grouped with other FoldableContainers so that only one of them can be opened at a time; see `foldable_group<class_FoldableContainer_property_foldable_group>` and `FoldableGroup<class_FoldableGroup>`.

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

**folding_changed**(is_folded: `bool<class_bool>`) `🔗<class_FoldableContainer_signal_folding_changed>`

Emitted when the container is folded/expanded.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **TitlePosition**: `🔗<enum_FoldableContainer_TitlePosition>`

classref-enumeration-constant

`TitlePosition<enum_FoldableContainer_TitlePosition>` **POSITION_TOP** = `0`

Makes the title appear at the top of the container.

classref-enumeration-constant

`TitlePosition<enum_FoldableContainer_TitlePosition>` **POSITION_BOTTOM** = `1`

Makes the title appear at the bottom of the container. Also makes all StyleBoxes flipped vertically.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`FoldableGroup<class_FoldableGroup>` **foldable_group** `🔗<class_FoldableContainer_property_foldable_group>`

classref-property-setget

- `void (No return value.)` **set_foldable_group**(value: `FoldableGroup<class_FoldableGroup>`)
- `FoldableGroup<class_FoldableGroup>` **get_foldable_group**()

The `FoldableGroup<class_FoldableGroup>` associated with the container. When multiple **FoldableContainer** nodes share the same group, only one of them is allowed to be unfolded.

classref-item-separator

classref-property

`bool<class_bool>` **folded** = `false` `🔗<class_FoldableContainer_property_folded>`

classref-property-setget

- `void (No return value.)` **set_folded**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_folded**()

If `true`, the container will become folded and will hide all its children.

classref-item-separator

classref-property

`String<class_String>` **language** = `""` `🔗<class_FoldableContainer_property_language>`

classref-property-setget

- `void (No return value.)` **set_language**(value: `String<class_String>`)
- `String<class_String>` **get_language**()

Language code used for text shaping algorithms. If left empty, the current locale is used instead.

classref-item-separator

classref-property

`String<class_String>` **title** = `""` `🔗<class_FoldableContainer_property_title>`

classref-property-setget

- `void (No return value.)` **set_title**(value: `String<class_String>`)
- `String<class_String>` **get_title**()

The container's title text.

classref-item-separator

classref-property

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **title_alignment** = `0` `🔗<class_FoldableContainer_property_title_alignment>`

classref-property-setget

- `void (No return value.)` **set_title_alignment**(value: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`)
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **get_title_alignment**()

Title's horizontal text alignment.

classref-item-separator

classref-property

`TitlePosition<enum_FoldableContainer_TitlePosition>` **title_position** = `0` `🔗<class_FoldableContainer_property_title_position>`

classref-property-setget

- `void (No return value.)` **set_title_position**(value: `TitlePosition<enum_FoldableContainer_TitlePosition>`)
- `TitlePosition<enum_FoldableContainer_TitlePosition>` **get_title_position**()

Title's position.

classref-item-separator

classref-property

`TextDirection<enum_Control_TextDirection>` **title_text_direction** = `0` `🔗<class_FoldableContainer_property_title_text_direction>`

classref-property-setget

- `void (No return value.)` **set_title_text_direction**(value: `TextDirection<enum_Control_TextDirection>`)
- `TextDirection<enum_Control_TextDirection>` **get_title_text_direction**()

Title text writing direction.

classref-item-separator

classref-property

`OverrunBehavior<enum_TextServer_OverrunBehavior>` **title_text_overrun_behavior** = `0` `🔗<class_FoldableContainer_property_title_text_overrun_behavior>`

classref-property-setget

- `void (No return value.)` **set_title_text_overrun_behavior**(value: `OverrunBehavior<enum_TextServer_OverrunBehavior>`)
- `OverrunBehavior<enum_TextServer_OverrunBehavior>` **get_title_text_overrun_behavior**()

Defines the behavior of the title when the text is longer than the available space.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_title_bar_control**(control: `Control<class_Control>`) `🔗<class_FoldableContainer_method_add_title_bar_control>`

Adds a `Control<class_Control>` that will be placed next to the container's title, obscuring the clickable area. Prime usage is adding `Button<class_Button>` nodes, but it can be any `Control<class_Control>`.

The control will be added as a child of this container and removed from previous parent if necessary. The controls will be placed aligned to the right, with the first added control being the leftmost one.

classref-item-separator

classref-method

`void (No return value.)` **expand**() `🔗<class_FoldableContainer_method_expand>`

Expands the container and emits `folding_changed<class_FoldableContainer_signal_folding_changed>`.

classref-item-separator

classref-method

`void (No return value.)` **fold**() `🔗<class_FoldableContainer_method_fold>`

Folds the container and emits `folding_changed<class_FoldableContainer_signal_folding_changed>`.

classref-item-separator

classref-method

`void (No return value.)` **remove_title_bar_control**(control: `Control<class_Control>`) `🔗<class_FoldableContainer_method_remove_title_bar_control>`

Removes a `Control<class_Control>` added with `add_title_bar_control()<class_FoldableContainer_method_add_title_bar_control>`. The node is not freed automatically, you need to use `Node.queue_free()<class_Node_method_queue_free>`.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **collapsed_font_color** = `Color(1, 1, 1, 1)` `🔗<class_FoldableContainer_theme_color_collapsed_font_color>`

The title's font color when collapsed.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_FoldableContainer_theme_color_font_color>`

The title's font color when expanded.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **font_outline_color** = `Color(1, 1, 1, 1)` `🔗<class_FoldableContainer_theme_color_font_outline_color>`

The title's font outline color.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **hover_font_color** = `Color(0.95, 0.95, 0.95, 1)` `🔗<class_FoldableContainer_theme_color_hover_font_color>`

The title's font hover color.

classref-item-separator

classref-themeproperty

`int<class_int>` **h_separation** = `2` `🔗<class_FoldableContainer_theme_constant_h_separation>`

The horizontal separation between the title's icon and text, and between title bar controls.

classref-item-separator

classref-themeproperty

`int<class_int>` **outline_size** = `0` `🔗<class_FoldableContainer_theme_constant_outline_size>`

The title's font outline size.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **font** `🔗<class_FoldableContainer_theme_font_font>`

The title's font.

classref-item-separator

classref-themeproperty

`int<class_int>` **font_size** `🔗<class_FoldableContainer_theme_font_size_font_size>`

The title's font size.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **expanded_arrow** `🔗<class_FoldableContainer_theme_icon_expanded_arrow>`

The title's icon used when expanded.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **expanded_arrow_mirrored** `🔗<class_FoldableContainer_theme_icon_expanded_arrow_mirrored>`

The title's icon used when expanded (for bottom title).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **folded_arrow** `🔗<class_FoldableContainer_theme_icon_folded_arrow>`

The title's icon used when folded (for left-to-right layouts).

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **folded_arrow_mirrored** `🔗<class_FoldableContainer_theme_icon_folded_arrow_mirrored>`

The title's icon used when collapsed (for right-to-left layouts).

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **focus** `🔗<class_FoldableContainer_theme_style_focus>`

Background used when **FoldableContainer** has GUI focus. The `focus<class_FoldableContainer_theme_style_focus>` `StyleBox<class_StyleBox>` is displayed *over* the base `StyleBox<class_StyleBox>`, so a partially transparent `StyleBox<class_StyleBox>` should be used to ensure the base `StyleBox<class_StyleBox>` remains visible. A `StyleBox<class_StyleBox>` that represents an outline or an underline works well for this purpose. To disable the focus visual effect, assign a `StyleBoxEmpty<class_StyleBoxEmpty>` resource. Note that disabling the focus visual effect will harm keyboard/controller navigation usability, so this is not recommended for accessibility reasons.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **panel** `🔗<class_FoldableContainer_theme_style_panel>`

Default background for the **FoldableContainer**.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **title_collapsed_hover_panel** `🔗<class_FoldableContainer_theme_style_title_collapsed_hover_panel>`

Background used when the mouse cursor enters the title's area when collapsed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **title_collapsed_panel** `🔗<class_FoldableContainer_theme_style_title_collapsed_panel>`

Default background for the **FoldableContainer**'s title when collapsed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **title_hover_panel** `🔗<class_FoldableContainer_theme_style_title_hover_panel>`

Background used when the mouse cursor enters the title's area when expanded.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **title_panel** `🔗<class_FoldableContainer_theme_style_title_panel>`

Default background for the **FoldableContainer**'s title when expanded.