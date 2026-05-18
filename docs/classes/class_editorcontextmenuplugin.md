github_url
hide

# EditorContextMenuPlugin

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Plugin for adding custom context menus in the editor.

classref-introduction-group

## Description

**EditorContextMenuPlugin** allows for the addition of custom options in the editor's context menu.

Currently, context menus are supported for three commonly used areas: the file system, scene tree, and editor script list panel.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ContextMenuSlot**: `🔗<enum_EditorContextMenuPlugin_ContextMenuSlot>`

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_SCENE_TREE** = `0`

Context menu of Scene dock. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` will be called with a list of paths to currently selected nodes, while option callback will receive the list of currently selected nodes.

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_FILESYSTEM** = `1`

Context menu of FileSystem dock. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` and option callback will be called with list of paths of the currently selected files.

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_SCRIPT_EDITOR** = `2`

Context menu of Script editor's script tabs. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` will be called with the path to the currently edited script, while option callback will receive reference to that script.

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_FILESYSTEM_CREATE** = `3`

The "Create..." submenu of FileSystem dock's context menu, or the "New" section of the main context menu when empty space is clicked. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` and option callback will be called with the path of the currently selected folder. When clicking the empty space, the list of paths for popup method will be empty.

    func _popup_menu(paths):
        if paths.is_empty():
            add_context_menu_item("New Image File...", create_image)
        else:
            add_context_menu_item("Image File...", create_image)

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_SCRIPT_EDITOR_CODE** = `4`

Context menu of Script editor's code editor. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` will be called with the path to the `CodeEdit<class_CodeEdit>` node. You can fetch it using this code:

    func _popup_menu(paths):
        var code_edit = Engine.get_main_loop().root.get_node(paths[0]);

The option callback will receive reference to that node. You can use `CodeEdit<class_CodeEdit>` methods to perform symbol lookups etc.

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_SCENE_TABS** = `5`

Context menu of scene tabs. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` will be called with the path of the clicked scene, or empty `PackedStringArray<class_PackedStringArray>` if the menu was opened on empty space. The option callback will receive the path of the clicked scene, or empty `String<class_String>` if none was clicked.

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_2D_EDITOR** = `6`

Context menu of 2D editor's basic right-click menu. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` will be called with paths to all `CanvasItem<class_CanvasItem>` nodes under the cursor. You can fetch them using this code:

    func _popup_menu(paths):
        var canvas_item = Engine.get_main_loop().root.get_node(paths[0]); # Replace 0 with the desired index.

The paths array is empty if there weren't any nodes under cursor. The option callback will receive a typed array of `CanvasItem<class_CanvasItem>` nodes.

classref-enumeration-constant

`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>` **CONTEXT_SLOT_INSPECTOR_PROPERTY** = `7`

Context menu of the inspectors right-click menu. `_popup_menu()<class_EditorContextMenuPlugin_private_method__popup_menu>` will be called with an array of two items: The first will be the object's ID, the second will be the property name. An object can be retrieved from it's ID via `@GlobalScope.instance_from_id()<class_@GlobalScope_method_instance_from_id>` after converting it to an int. The option callback will receive the EditorProperty directly.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_popup_menu**(paths: `PackedStringArray<class_PackedStringArray>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorContextMenuPlugin_private_method__popup_menu>`

Called when creating a context menu, custom options can be added by using the `add_context_menu_item()<class_EditorContextMenuPlugin_method_add_context_menu_item>` or `add_context_menu_item_from_shortcut()<class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut>` functions. `paths` contains currently selected paths (depending on menu), which can be used to conditionally add options.

classref-item-separator

classref-method

`void (No return value.)` **add_context_menu_item**(name: `String<class_String>`, callback: `Callable<class_Callable>`, icon: `Texture2D<class_Texture2D>` = null) `🔗<class_EditorContextMenuPlugin_method_add_context_menu_item>`

Add custom option to the context menu of the plugin's specified slot. When the option is activated, `callback` will be called. Callback should take single `Array<class_Array>` argument; array contents depend on context menu slot.

    func _popup_menu(paths):
        add_context_menu_item("File Custom options", handle, ICON)

If you want to assign shortcut to the menu item, use `add_context_menu_item_from_shortcut()<class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut>` instead.

classref-item-separator

classref-method

`void (No return value.)` **add_context_menu_item_from_shortcut**(name: `String<class_String>`, shortcut: `Shortcut<class_Shortcut>`, icon: `Texture2D<class_Texture2D>` = null) `🔗<class_EditorContextMenuPlugin_method_add_context_menu_item_from_shortcut>`

Add custom option to the context menu of the plugin's specified slot. The option will have the `shortcut` assigned and reuse its callback. The shortcut has to be registered beforehand with `add_menu_shortcut()<class_EditorContextMenuPlugin_method_add_menu_shortcut>`.

    func _init():
        add_menu_shortcut(SHORTCUT, handle)

    func _popup_menu(paths):
        add_context_menu_item_from_shortcut("File Custom options", SHORTCUT, ICON)

classref-item-separator

classref-method

`void (No return value.)` **add_context_submenu_item**(name: `String<class_String>`, menu: `PopupMenu<class_PopupMenu>`, icon: `Texture2D<class_Texture2D>` = null) `🔗<class_EditorContextMenuPlugin_method_add_context_submenu_item>`

Add a submenu to the context menu of the plugin's specified slot. The submenu is not automatically handled, you need to connect to its signals yourself. Also the submenu is freed on every popup, so provide a new `PopupMenu<class_PopupMenu>` every time.

    func _popup_menu(paths):
        var popup_menu = PopupMenu.new()
        popup_menu.add_item("Blue")
        popup_menu.add_item("White")
        popup_menu.id_pressed.connect(_on_color_submenu_option)

        add_context_submenu_item("Set Node Color", popup_menu)

classref-item-separator

classref-method

`void (No return value.)` **add_menu_shortcut**(shortcut: `Shortcut<class_Shortcut>`, callback: `Callable<class_Callable>`) `🔗<class_EditorContextMenuPlugin_method_add_menu_shortcut>`

Registers a shortcut associated with the plugin's context menu. This method should be called once (e.g. in plugin's `Object._init()<class_Object_private_method__init>`). `callback` will be called when user presses the specified `shortcut` while the menu's context is in effect (e.g. FileSystem dock is focused). Callback should take single `Array<class_Array>` argument; array contents depend on context menu slot.

    func _init():
        add_menu_shortcut(SHORTCUT, handle)