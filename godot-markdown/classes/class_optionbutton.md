github_url
hide

# OptionButton

**Inherits:** `Button<class_Button>` **\<** `BaseButton<class_BaseButton>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A button that brings up a dropdown with selectable options when pressed.

classref-introduction-group

## Description

**OptionButton** is a type of button that brings up a dropdown with selectable items when pressed. The item selected becomes the "current" item and is displayed as the button text.

See also `BaseButton<class_BaseButton>` which contains common properties and methods associated with this node.

**Note:** The IDs used for items are limited to signed 32-bit integers, not the full 64 bits of `int<class_int>`. These have a range of `-2^31` to `2^31 - 1`, that is, `-2147483648` to `2147483647`.

**Note:** The `Button.text<class_Button_property_text>` and `Button.icon<class_Button_property_icon>` properties are set automatically based on the selected item. They shouldn't be changed manually.

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

**item_focused**(index: `int<class_int>`) `🔗<class_OptionButton_signal_item_focused>`

Emitted when the user navigates to an item using the `ProjectSettings.input/ui_up<class_ProjectSettings_property_input/ui_up>` or `ProjectSettings.input/ui_down<class_ProjectSettings_property_input/ui_down>` input actions. The index of the item focused is passed as argument.

classref-item-separator

classref-signal

**item_selected**(index: `int<class_int>`) `🔗<class_OptionButton_signal_item_selected>`

Emitted when the current item has been changed by the user. The index of the item selected is passed as argument.

`allow_reselect<class_OptionButton_property_allow_reselect>` must be enabled to reselect an item.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **allow_reselect** = `false` `🔗<class_OptionButton_property_allow_reselect>`

classref-property-setget

- `void (No return value.)` **set_allow_reselect**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_allow_reselect**()

If `true`, the currently selected item can be selected again.

classref-item-separator

classref-property

`bool<class_bool>` **fit_to_longest_item** = `true` `🔗<class_OptionButton_property_fit_to_longest_item>`

classref-property-setget

- `void (No return value.)` **set_fit_to_longest_item**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_fit_to_longest_item**()

If `true`, minimum size will be determined by the longest item's text, instead of the currently selected one's.

**Note:** For performance reasons, the minimum size doesn't update immediately when adding, removing or modifying items.

classref-item-separator

classref-property

`int<class_int>` **item_count** = `0` `🔗<class_OptionButton_property_item_count>`

classref-property-setget

- `void (No return value.)` **set_item_count**(value: `int<class_int>`)
- `int<class_int>` **get_item_count**()

The number of items to select from.

classref-item-separator

classref-property

`bool<class_bool>` **popup/item\_{index}/disabled** = `false` `🔗<class_OptionButton_property_popup/item_{index}/disabled>`

If `true`, the item at `index` is disabled.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **popup/item\_{index}/icon** `🔗<class_OptionButton_property_popup/item_{index}/icon>`

The icon of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

classref-item-separator

classref-property

`int<class_int>` **popup/item\_{index}/id** = `0` `🔗<class_OptionButton_property_popup/item_{index}/id>`

The ID of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

classref-item-separator

classref-property

`bool<class_bool>` **popup/item\_{index}/separator** = `false` `🔗<class_OptionButton_property_popup/item_{index}/separator>`

If `true`, the item at `index` is a separator.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

classref-item-separator

classref-property

`String<class_String>` **popup/item\_{index}/text** = `""` `🔗<class_OptionButton_property_popup/item_{index}/text>`

The text of the item at `index`.

**Note:** `index` is a value in the `0 .. item_count - 1` range.

classref-item-separator

classref-property

`bool<class_bool>` **search_bar_enabled** = `false` `🔗<class_OptionButton_property_search_bar_enabled>`

classref-property-setget

- `void (No return value.)` **set_search_bar_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_search_bar_enabled**()

If `true`, shows a search bar at the top of the `PopupMenu<class_PopupMenu>` for filtering items. See `search_bar_min_item_count<class_OptionButton_property_search_bar_min_item_count>` for dynamically controlling its visibility based on the number of items.

classref-item-separator

classref-property

`bool<class_bool>` **search_bar_fuzzy_search_enabled** = `true` `🔗<class_OptionButton_property_search_bar_fuzzy_search_enabled>`

classref-property-setget

- `void (No return value.)` **set_search_bar_fuzzy_search_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_search_bar_fuzzy_search_enabled**()

If `true`, enables fuzzy searching in the `PopupMenu<class_PopupMenu>` search bar. This allows the search results to include items that almost match the search query, as well items that match the individual characters of the search query, but not in sequence.

Use `search_bar_fuzzy_search_max_misses<class_OptionButton_property_search_bar_fuzzy_search_max_misses>` to set the maximum number of mismatches allowed in the search results.

classref-item-separator

classref-property

`int<class_int>` **search_bar_fuzzy_search_max_misses** = `2` `🔗<class_OptionButton_property_search_bar_fuzzy_search_max_misses>`

classref-property-setget

- `void (No return value.)` **set_search_bar_fuzzy_search_max_misses**(value: `int<class_int>`)
- `int<class_int>` **get_search_bar_fuzzy_search_max_misses**()

Sets the maximum number of mismatches allowed in each search result when fuzzy searching is enabled for the `PopupMenu<class_PopupMenu>` search bar. Any item with more mismatches will be hidden from the search results.

classref-item-separator

classref-property

`int<class_int>` **search_bar_min_item_count** = `0` `🔗<class_OptionButton_property_search_bar_min_item_count>`

classref-property-setget

- `void (No return value.)` **set_search_bar_min_item_count**(value: `int<class_int>`)
- `int<class_int>` **get_search_bar_min_item_count**()

Sets the minimum number of items required for the `PopupMenu<class_PopupMenu>` search bar to be visible. `search_bar_enabled<class_OptionButton_property_search_bar_enabled>` must be `true` for this to have any effect.

classref-item-separator

classref-property

`int<class_int>` **selected** = `-1` `🔗<class_OptionButton_property_selected>`

classref-property-setget

- `int<class_int>` **get_selected**()

The index of the currently selected item, or `-1` if no item is selected.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_icon_item**(texture: `Texture2D<class_Texture2D>`, label: `String<class_String>`, id: `int<class_int>` = -1) `🔗<class_OptionButton_method_add_icon_item>`

Adds an item, with a `texture` icon, text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

**Note:** The item will be selected if there are no other items.

classref-item-separator

classref-method

`void (No return value.)` **add_item**(label: `String<class_String>`, id: `int<class_int>` = -1) `🔗<class_OptionButton_method_add_item>`

Adds an item, with text `label` and (optionally) `id`. If no `id` is passed, the item index will be used as the item's ID. New items are appended at the end.

**Note:** The item will be selected if there are no other items.

classref-item-separator

classref-method

`void (No return value.)` **add_separator**(text: `String<class_String>` = "") `🔗<class_OptionButton_method_add_separator>`

Adds a separator to the list of items. Separators help to group items, and can optionally be given a `text` header. A separator also gets an index assigned, and is appended at the end of the item list.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_OptionButton_method_clear>`

Clears all the items in the **OptionButton**.

classref-item-separator

classref-method

`AutoTranslateMode<enum_Node_AutoTranslateMode>` **get_item_auto_translate_mode**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_auto_translate_mode>`

Returns the auto translate mode of the item at index `idx`.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_item_icon**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_icon>`

Returns the icon of the item at index `idx`.

classref-item-separator

classref-method

`int<class_int>` **get_item_id**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_id>`

Returns the ID of the item at index `idx`.

classref-item-separator

classref-method

`int<class_int>` **get_item_index**(id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_index>`

Returns the index of the item with the given `id`.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_item_metadata**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_metadata>`

Retrieves the metadata of an item. Metadata may be any type and can be used to store extra information about an item, such as an external string ID.

classref-item-separator

classref-method

`String<class_String>` **get_item_text**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_text>`

Returns the text of the item at index `idx`.

classref-item-separator

classref-method

`String<class_String>` **get_item_tooltip**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_item_tooltip>`

Returns the tooltip of the item at index `idx`.

classref-item-separator

classref-method

`PopupMenu<class_PopupMenu>` **get_popup**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_popup>`

Returns the `PopupMenu<class_PopupMenu>` contained in this button.

**Warning:** This is a required internal node, removing and freeing it may cause a crash. If you wish to hide it or any of its children, use their `Window.visible<class_Window_property_visible>` property.

classref-item-separator

classref-method

`int<class_int>` **get_selectable_item**(from_last: `bool<class_bool>` = false) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_selectable_item>`

Returns the index of the first item which is not disabled, or marked as a separator. If `from_last` is `true`, the items will be searched in reverse order.

Returns `-1` if no item is found.

classref-item-separator

classref-method

`int<class_int>` **get_selected_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_selected_id>`

Returns the ID of the selected item, or `-1` if no item is selected.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_selected_metadata**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_get_selected_metadata>`

Gets the metadata of the selected item. Metadata for items can be set using `set_item_metadata()<class_OptionButton_method_set_item_metadata>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_selectable_items**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_has_selectable_items>`

Returns `true` if this button contains at least one item which is not disabled, or marked as a separator.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_disabled**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_is_item_disabled>`

Returns `true` if the item at index `idx` is disabled.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_separator**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OptionButton_method_is_item_separator>`

Returns `true` if the item at index `idx` is marked as a separator.

classref-item-separator

classref-method

`void (No return value.)` **remove_item**(idx: `int<class_int>`) `🔗<class_OptionButton_method_remove_item>`

Removes the item at index `idx`.

classref-item-separator

classref-method

`void (No return value.)` **select**(idx: `int<class_int>`) `🔗<class_OptionButton_method_select>`

Selects an item by index and makes it the current item. This will work even if the item is disabled.

Passing `-1` as the index deselects any currently selected item.

classref-item-separator

classref-method

`void (No return value.)` **set_disable_shortcuts**(disabled: `bool<class_bool>`) `🔗<class_OptionButton_method_set_disable_shortcuts>`

If `true`, shortcuts are disabled and cannot be used to trigger the button.

classref-item-separator

classref-method

`void (No return value.)` **set_item_auto_translate_mode**(idx: `int<class_int>`, mode: `AutoTranslateMode<enum_Node_AutoTranslateMode>`) `🔗<class_OptionButton_method_set_item_auto_translate_mode>`

Sets the auto translate mode of the item at index `idx`.

Items use `Node.AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>` by default, which uses the same auto translate mode as the **OptionButton** itself.

classref-item-separator

classref-method

`void (No return value.)` **set_item_disabled**(idx: `int<class_int>`, disabled: `bool<class_bool>`) `🔗<class_OptionButton_method_set_item_disabled>`

Sets whether the item at index `idx` is disabled.

Disabled items are drawn differently in the dropdown and are not selectable by the user. If the current selected item is set as disabled, it will remain selected.

classref-item-separator

classref-method

`void (No return value.)` **set_item_icon**(idx: `int<class_int>`, texture: `Texture2D<class_Texture2D>`) `🔗<class_OptionButton_method_set_item_icon>`

Sets the icon of the item at index `idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_item_id**(idx: `int<class_int>`, id: `int<class_int>`) `🔗<class_OptionButton_method_set_item_id>`

Sets the ID of the item at index `idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_item_metadata**(idx: `int<class_int>`, metadata: `Variant<class_Variant>`) `🔗<class_OptionButton_method_set_item_metadata>`

Sets the metadata of an item. Metadata may be of any type and can be used to store extra information about an item, such as an external string ID.

classref-item-separator

classref-method

`void (No return value.)` **set_item_text**(idx: `int<class_int>`, text: `String<class_String>`) `🔗<class_OptionButton_method_set_item_text>`

Sets the text of the item at index `idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_item_tooltip**(idx: `int<class_int>`, tooltip: `String<class_String>`) `🔗<class_OptionButton_method_set_item_tooltip>`

Sets the tooltip of the item at index `idx`.

classref-item-separator

classref-method

`void (No return value.)` **show_popup**() `🔗<class_OptionButton_method_show_popup>`

Adjusts popup position and sizing for the **OptionButton**, then shows the `PopupMenu<class_PopupMenu>`. Prefer this over using `get_popup().popup()`.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`int<class_int>` **arrow_margin** = `4` `🔗<class_OptionButton_theme_constant_arrow_margin>`

The horizontal space between the arrow icon and the right edge of the button.

classref-item-separator

classref-themeproperty

`int<class_int>` **modulate_arrow** = `0` `🔗<class_OptionButton_theme_constant_modulate_arrow>`

If different than `0`, the arrow icon will be modulated to the font color.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **arrow** `🔗<class_OptionButton_theme_icon_arrow>`

The arrow icon to be drawn on the right end of the button.