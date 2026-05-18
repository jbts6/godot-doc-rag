github_url
hide

# NativeMenu

**Inherits:** `Object<class_Object>`

A server interface for OS native menus.

classref-introduction-group

## Description

**NativeMenu** handles low-level access to the OS native global menu bar and popup menus.

**Note:** This is low-level API, consider using `MenuBar<class_MenuBar>` with `MenuBar.prefer_global_menu<class_MenuBar_property_prefer_global_menu>` set to `true`, and `PopupMenu<class_PopupMenu>` with `PopupMenu.prefer_native_menu<class_PopupMenu_property_prefer_native_menu>` set to `true`.

To create a menu, use `create_menu()<class_NativeMenu_method_create_menu>`, add menu items using `add_*_item` methods. To remove a menu, use `free_menu()<class_NativeMenu_method_free_menu>`.

    var menu

    func _menu_callback(item_id):
        if item_id == "ITEM_CUT":
            cut()
        elif item_id == "ITEM_COPY":
            copy()
        elif item_id == "ITEM_PASTE":
            paste()

    func _enter_tree():
        # Create new menu and add items:
        menu = NativeMenu.create_menu()
        NativeMenu.add_item(menu, "Cut", _menu_callback, Callable(), "ITEM_CUT")
        NativeMenu.add_item(menu, "Copy", _menu_callback, Callable(), "ITEM_COPY")
        NativeMenu.add_separator(menu)
        NativeMenu.add_item(menu, "Paste", _menu_callback, Callable(), "ITEM_PASTE")

    func _on_button_pressed():
        # Show popup menu at mouse position:
        NativeMenu.popup(menu, DisplayServer.mouse_get_position())

    func _exit_tree():
        # Remove menu when it's no longer needed:
        NativeMenu.free_menu(menu)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Feature**: `🔗<enum_NativeMenu_Feature>`

classref-enumeration-constant

`Feature<enum_NativeMenu_Feature>` **FEATURE_GLOBAL_MENU** = `0`

**NativeMenu** supports native global main menu.

classref-enumeration-constant

`Feature<enum_NativeMenu_Feature>` **FEATURE_POPUP_MENU** = `1`

**NativeMenu** supports native popup menus.

classref-enumeration-constant

`Feature<enum_NativeMenu_Feature>` **FEATURE_OPEN_CLOSE_CALLBACK** = `2`

**NativeMenu** supports menu open and close callbacks.

classref-enumeration-constant

`Feature<enum_NativeMenu_Feature>` **FEATURE_HOVER_CALLBACK** = `3`

**NativeMenu** supports menu item hover callback.

classref-enumeration-constant

`Feature<enum_NativeMenu_Feature>` **FEATURE_KEY_CALLBACK** = `4`

**NativeMenu** supports menu item accelerator/key callback.

classref-item-separator

classref-enumeration

enum **SystemMenus**: `🔗<enum_NativeMenu_SystemMenus>`

classref-enumeration-constant

`SystemMenus<enum_NativeMenu_SystemMenus>` **INVALID_MENU_ID** = `0`

Invalid special system menu ID.

classref-enumeration-constant

`SystemMenus<enum_NativeMenu_SystemMenus>` **MAIN_MENU_ID** = `1`

Global main menu ID.

classref-enumeration-constant

`SystemMenus<enum_NativeMenu_SystemMenus>` **APPLICATION_MENU_ID** = `2`

Application (first menu after "Apple" menu on macOS) menu ID.

classref-enumeration-constant

`SystemMenus<enum_NativeMenu_SystemMenus>` **WINDOW_MENU_ID** = `3`

"Window" menu ID (on macOS this menu includes standard window control items and a list of open windows).

classref-enumeration-constant

`SystemMenus<enum_NativeMenu_SystemMenus>` **HELP_MENU_ID** = `4`

"Help" menu ID (on macOS this menu includes help search bar).

classref-enumeration-constant

`SystemMenus<enum_NativeMenu_SystemMenus>` **DOCK_MENU_ID** = `5`

Dock icon right-click menu ID (on macOS this menu include standard application control items and a list of open windows).

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **add_check_item**(rid: `RID<class_RID>`, label: `String<class_String>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_check_item>`

Adds a new checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_icon_check_item**(rid: `RID<class_RID>`, icon: `Texture2D<class_Texture2D>`, label: `String<class_String>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_icon_check_item>`

Adds a new checkable item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_icon_item**(rid: `RID<class_RID>`, icon: `Texture2D<class_Texture2D>`, label: `String<class_String>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_icon_item>`

Adds a new item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_icon_radio_check_item**(rid: `RID<class_RID>`, icon: `Texture2D<class_Texture2D>`, label: `String<class_String>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_icon_radio_check_item>`

Adds a new radio-checkable item with text `label` and icon `icon` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See `set_item_checked()<class_NativeMenu_method_set_item_checked>` for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_item**(rid: `RID<class_RID>`, label: `String<class_String>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_item>`

Adds a new item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_multistate_item**(rid: `RID<class_RID>`, label: `String<class_String>`, max_states: `int<class_int>`, default_state: `int<class_int>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_multistate_item>`

Adds a new item with text `label` to the global menu `rid`.

Contrarily to normal binary items, multistate items can have more than two states, as defined by `max_states`. Each press or activate of the item will increase the state by one. The default value is defined by `default_state`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** By default, there's no indication of the current item state, it should be changed manually.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_radio_check_item**(rid: `RID<class_RID>`, label: `String<class_String>`, callback: `Callable<class_Callable>` = Callable(), key_callback: `Callable<class_Callable>` = Callable(), tag: `Variant<class_Variant>` = null, accelerator: `Key<enum_@GlobalScope_Key>` = 0, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_radio_check_item>`

Adds a new radio-checkable item with text `label` to the global menu `rid`.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

An `accelerator` can optionally be defined, which is a keyboard shortcut that can be pressed to trigger the menu button even if it's not currently open. The `accelerator` is generally a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** Radio-checkable items just display a checkmark, but don't have any built-in checking behavior and must be checked/unchecked manually. See `set_item_checked()<class_NativeMenu_method_set_item_checked>` for more info on how to control it.

**Note:** The `callback` and `key_callback` Callables need to accept exactly one Variant parameter, the parameter passed to the Callables will be the value passed to `tag`.

**Note:** This method is implemented on macOS and Windows.

**Note:** On Windows, `accelerator` and `key_callback` are ignored.

classref-item-separator

classref-method

`int<class_int>` **add_separator**(rid: `RID<class_RID>`, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_separator>`

Adds a separator between items to the global menu `rid`. Separators also occupy an index.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **add_submenu_item**(rid: `RID<class_RID>`, label: `String<class_String>`, submenu_rid: `RID<class_RID>`, tag: `Variant<class_Variant>` = null, index: `int<class_int>` = -1) `🔗<class_NativeMenu_method_add_submenu_item>`

Adds an item that will act as a submenu of the global menu `rid`. The `submenu_rid` argument is the RID of the global menu that will be shown when the item is clicked.

Returns index of the inserted item, it's not guaranteed to be the same as `index` value.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **clear**(rid: `RID<class_RID>`) `🔗<class_NativeMenu_method_clear>`

Removes all items from the global menu `rid`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`RID<class_RID>` **create_menu**() `🔗<class_NativeMenu_method_create_menu>`

Creates a new global menu object.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **find_item_index_with_submenu**(rid: `RID<class_RID>`, submenu_rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_find_item_index_with_submenu>`

Returns the index of the item with the submenu specified by `submenu_rid`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **find_item_index_with_tag**(rid: `RID<class_RID>`, tag: `Variant<class_Variant>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_find_item_index_with_tag>`

Returns the index of the item with the specified `tag`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **find_item_index_with_text**(rid: `RID<class_RID>`, text: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_find_item_index_with_text>`

Returns the index of the item with the specified `text`. Indices are automatically assigned to each item by the engine.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **free_menu**(rid: `RID<class_RID>`) `🔗<class_NativeMenu_method_free_menu>`

Frees a global menu object created by this **NativeMenu**.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`Key<enum_@GlobalScope_Key>` **get_item_accelerator**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_accelerator>`

Returns the accelerator of the item at index `idx`. Accelerators are special combinations of keys that activate the item, no matter which control is focused.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`Callable<class_Callable>` **get_item_callback**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_callback>`

Returns the callback of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **get_item_count**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_count>`

Returns number of items in the global menu `rid`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_item_icon**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_icon>`

Returns the icon of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **get_item_indentation_level**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_indentation_level>`

Returns the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`Callable<class_Callable>` **get_item_key_callback**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_key_callback>`

Returns the callback of the item accelerator at index `idx`.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`int<class_int>` **get_item_max_states**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_max_states>`

Returns number of states of a multistate item. See `add_multistate_item()<class_NativeMenu_method_add_multistate_item>` for details.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`int<class_int>` **get_item_state**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_state>`

Returns the state of a multistate item. See `add_multistate_item()<class_NativeMenu_method_add_multistate_item>` for details.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`RID<class_RID>` **get_item_submenu**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_submenu>`

Returns the submenu ID of the item at index `idx`. See `add_submenu_item()<class_NativeMenu_method_add_submenu_item>` for more info on how to add a submenu.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_item_tag**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_tag>`

Returns the metadata of the specified item, which might be of any type. You can set it with `set_item_tag()<class_NativeMenu_method_set_item_tag>`, which provides a simple way of assigning context data to items.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`String<class_String>` **get_item_text**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_text>`

Returns the text of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`String<class_String>` **get_item_tooltip**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_item_tooltip>`

Returns the tooltip associated with the specified index `idx`.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`float<class_float>` **get_minimum_width**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_minimum_width>`

Returns global menu minimum width.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`Callable<class_Callable>` **get_popup_close_callback**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_popup_close_callback>`

Returns global menu close callback.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`Callable<class_Callable>` **get_popup_open_callback**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_popup_open_callback>`

Returns global menu open callback.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_size**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_size>`

Returns global menu size.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`RID<class_RID>` **get_system_menu**(menu_id: `SystemMenus<enum_NativeMenu_SystemMenus>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_system_menu>`

Returns RID of a special system menu.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`String<class_String>` **get_system_menu_name**(menu_id: `SystemMenus<enum_NativeMenu_SystemMenus>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_system_menu_name>`

Returns readable name of a special system menu.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`String<class_String>` **get_system_menu_text**(menu_id: `SystemMenus<enum_NativeMenu_SystemMenus>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_get_system_menu_text>`

Returns the text of the system menu item.

**Note:** This method is implemented on macOS.

classref-item-separator

classref-method

`bool<class_bool>` **has_feature**(feature: `Feature<enum_NativeMenu_Feature>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_has_feature>`

Returns `true` if the specified `feature` is supported by the current **NativeMenu**, `false` otherwise.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`bool<class_bool>` **has_menu**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_has_menu>`

Returns `true` if `rid` is valid global menu.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`bool<class_bool>` **has_system_menu**(menu_id: `SystemMenus<enum_NativeMenu_SystemMenus>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_has_system_menu>`

Returns `true` if a special system menu is supported.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_checkable**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_item_checkable>`

Returns `true` if the item at index `idx` is checkable in some way, i.e. if it has a checkbox or radio button.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_checked**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_item_checked>`

Returns `true` if the item at index `idx` is checked.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_disabled**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_item_disabled>`

Returns `true` if the item at index `idx` is disabled. When it is disabled it can't be selected, or its action invoked.

See `set_item_disabled()<class_NativeMenu_method_set_item_disabled>` for more info on how to disable an item.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_hidden**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_item_hidden>`

Returns `true` if the item at index `idx` is hidden.

See `set_item_hidden()<class_NativeMenu_method_set_item_hidden>` for more info on how to hide an item.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`bool<class_bool>` **is_item_radio_checkable**(rid: `RID<class_RID>`, idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_item_radio_checkable>`

Returns `true` if the item at index `idx` has radio button-style checkability.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`bool<class_bool>` **is_opened**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_opened>`

Returns `true` if the menu is currently opened.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`bool<class_bool>` **is_system_menu**(rid: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_NativeMenu_method_is_system_menu>`

Return `true` is global menu is a special system menu.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **popup**(rid: `RID<class_RID>`, position: `Vector2i<class_Vector2i>`) `🔗<class_NativeMenu_method_popup>`

Shows the global menu at `position` in the screen coordinates.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **remove_item**(rid: `RID<class_RID>`, idx: `int<class_int>`) `🔗<class_NativeMenu_method_remove_item>`

Removes the item at index `idx` from the global menu `rid`.

**Note:** The indices of items after the removed item will be shifted by one.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_interface_direction**(rid: `RID<class_RID>`, is_rtl: `bool<class_bool>`) `🔗<class_NativeMenu_method_set_interface_direction>`

Sets the menu text layout direction from right-to-left if `is_rtl` is `true`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_accelerator**(rid: `RID<class_RID>`, idx: `int<class_int>`, keycode: `Key<enum_@GlobalScope_Key>`) `🔗<class_NativeMenu_method_set_item_accelerator>`

Sets the accelerator of the item at index `idx`. `keycode` can be a single `Key<enum_@GlobalScope_Key>`, or a combination of `KeyModifierMask<enum_@GlobalScope_KeyModifierMask>`s and `Key<enum_@GlobalScope_Key>`s using bitwise OR such as `KEY_MASK_CTRL | KEY_A` (`Ctrl + A`).

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_item_callback**(rid: `RID<class_RID>`, idx: `int<class_int>`, callback: `Callable<class_Callable>`) `🔗<class_NativeMenu_method_set_item_callback>`

Sets the callback of the item at index `idx`. Callback is emitted when an item is pressed.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_checkable**(rid: `RID<class_RID>`, idx: `int<class_int>`, checkable: `bool<class_bool>`) `🔗<class_NativeMenu_method_set_item_checkable>`

Sets whether the item at index `idx` has a checkbox. If `false`, sets the type of the item to plain text.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_checked**(rid: `RID<class_RID>`, idx: `int<class_int>`, checked: `bool<class_bool>`) `🔗<class_NativeMenu_method_set_item_checked>`

Sets the checkstate status of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_disabled**(rid: `RID<class_RID>`, idx: `int<class_int>`, disabled: `bool<class_bool>`) `🔗<class_NativeMenu_method_set_item_disabled>`

Enables/disables the item at index `idx`. When it is disabled, it can't be selected and its action can't be invoked.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_hidden**(rid: `RID<class_RID>`, idx: `int<class_int>`, hidden: `bool<class_bool>`) `🔗<class_NativeMenu_method_set_item_hidden>`

Hides/shows the item at index `idx`. When it is hidden, an item does not appear in a menu and its action cannot be invoked.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_item_hover_callbacks**(rid: `RID<class_RID>`, idx: `int<class_int>`, callback: `Callable<class_Callable>`) `🔗<class_NativeMenu_method_set_item_hover_callbacks>`

Sets the callback of the item at index `idx`. The callback is emitted when an item is hovered.

**Note:** The `callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_item_icon**(rid: `RID<class_RID>`, idx: `int<class_int>`, icon: `Texture2D<class_Texture2D>`) `🔗<class_NativeMenu_method_set_item_icon>`

Replaces the `Texture2D<class_Texture2D>` icon of the specified `idx`.

**Note:** This method is implemented on macOS and Windows.

**Note:** This method is not supported by macOS Dock menu items.

classref-item-separator

classref-method

`void (No return value.)` **set_item_indentation_level**(rid: `RID<class_RID>`, idx: `int<class_int>`, level: `int<class_int>`) `🔗<class_NativeMenu_method_set_item_indentation_level>`

Sets the horizontal offset of the item at the given `idx`.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`int<class_int>` **set_item_index**(rid: `RID<class_RID>`, idx: `int<class_int>`, target_idx: `int<class_int>`) `🔗<class_NativeMenu_method_set_item_index>`

Changes the index of the item at index `idx` to be at index `target_idx`. This can be used to move an item above other items.

Returns the new index of the moved item, it's not guaranteed to be the same as `target_idx`.

**Note:** The indices of any items between index `idx` and index `target_idx` will be shifted by one.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_key_callback**(rid: `RID<class_RID>`, idx: `int<class_int>`, key_callback: `Callable<class_Callable>`) `🔗<class_NativeMenu_method_set_item_key_callback>`

Sets the callback of the item at index `idx`. Callback is emitted when its accelerator is activated.

**Note:** The `key_callback` Callable needs to accept exactly one Variant parameter, the parameter passed to the Callable will be the value passed to the `tag` parameter when the menu item was created.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_item_max_states**(rid: `RID<class_RID>`, idx: `int<class_int>`, max_states: `int<class_int>`) `🔗<class_NativeMenu_method_set_item_max_states>`

Sets number of state of a multistate item. See `add_multistate_item()<class_NativeMenu_method_add_multistate_item>` for details.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_radio_checkable**(rid: `RID<class_RID>`, idx: `int<class_int>`, checkable: `bool<class_bool>`) `🔗<class_NativeMenu_method_set_item_radio_checkable>`

Sets the type of the item at the specified index `idx` to radio button. If `false`, sets the type of the item to plain text.

**Note:** This is purely cosmetic; you must add the logic for checking/unchecking items in radio groups.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_state**(rid: `RID<class_RID>`, idx: `int<class_int>`, state: `int<class_int>`) `🔗<class_NativeMenu_method_set_item_state>`

Sets the state of a multistate item. See `add_multistate_item()<class_NativeMenu_method_add_multistate_item>` for details.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_submenu**(rid: `RID<class_RID>`, idx: `int<class_int>`, submenu_rid: `RID<class_RID>`) `🔗<class_NativeMenu_method_set_item_submenu>`

Sets the submenu RID of the item at index `idx`. The submenu is a global menu that would be shown when the item is clicked.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_tag**(rid: `RID<class_RID>`, idx: `int<class_int>`, tag: `Variant<class_Variant>`) `🔗<class_NativeMenu_method_set_item_tag>`

Sets the metadata of an item, which may be of any type. You can later get it with `get_item_tag()<class_NativeMenu_method_get_item_tag>`, which provides a simple way of assigning context data to items.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_text**(rid: `RID<class_RID>`, idx: `int<class_int>`, text: `String<class_String>`) `🔗<class_NativeMenu_method_set_item_text>`

Sets the text of the item at index `idx`.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_item_tooltip**(rid: `RID<class_RID>`, idx: `int<class_int>`, tooltip: `String<class_String>`) `🔗<class_NativeMenu_method_set_item_tooltip>`

Sets the `String<class_String>` tooltip of the item at the specified index `idx`.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_minimum_width**(rid: `RID<class_RID>`, width: `float<class_float>`) `🔗<class_NativeMenu_method_set_minimum_width>`

Sets the minimum width of the global menu.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_popup_close_callback**(rid: `RID<class_RID>`, callback: `Callable<class_Callable>`) `🔗<class_NativeMenu_method_set_popup_close_callback>`

Registers callable to emit when the menu is about to show.

**Note:** The OS can simulate menu opening to track menu item changes and global shortcuts, in which case the corresponding close callback is not triggered. Use `is_opened()<class_NativeMenu_method_is_opened>` to check if the menu is currently opened.

**Note:** This method is implemented on macOS and Windows.

classref-item-separator

classref-method

`void (No return value.)` **set_popup_open_callback**(rid: `RID<class_RID>`, callback: `Callable<class_Callable>`) `🔗<class_NativeMenu_method_set_popup_open_callback>`

Registers callable to emit after the menu is closed.

**Note:** This method is implemented only on macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_system_menu_text**(menu_id: `SystemMenus<enum_NativeMenu_SystemMenus>`, name: `String<class_String>`) `🔗<class_NativeMenu_method_set_system_menu_text>`

Sets the text of the system menu item.

**Note:** This method is implemented on macOS.