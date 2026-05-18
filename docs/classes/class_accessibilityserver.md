github_url
hide

# AccessibilityServer

**Inherits:** `Object<class_Object>`

A server interface for screen reader support.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **AccessibilityRole**: `🔗<enum_AccessibilityServer_AccessibilityRole>`

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_UNKNOWN** = `0`

Unknown or custom role.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_DEFAULT_BUTTON** = `1`

Default dialog button element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_AUDIO** = `2`

Audio player element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_VIDEO** = `3`

Video player element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_STATIC_TEXT** = `4`

Non-editable text label.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_CONTAINER** = `5`

Container element. Elements with this role are used for internal structure and ignored by screen readers.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_PANEL** = `6`

Panel container element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_BUTTON** = `7`

Button element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_LINK** = `8`

Link element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_CHECK_BOX** = `9`

Check box element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_RADIO_BUTTON** = `10`

Radio button element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_CHECK_BUTTON** = `11`

Check button element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_SCROLL_BAR** = `12`

Scroll bar element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_SCROLL_VIEW** = `13`

Scroll container element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_SPLITTER** = `14`

Container splitter handle element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_SLIDER** = `15`

Slider element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_SPIN_BUTTON** = `16`

Spin box element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_PROGRESS_INDICATOR** = `17`

Progress indicator element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TEXT_FIELD** = `18`

Editable text field element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_MULTILINE_TEXT_FIELD** = `19`

Multiline editable text field element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_COLOR_PICKER** = `20`

Color picker element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TABLE** = `21`

Table element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_CELL** = `22`

Table/tree cell element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_ROW** = `23`

Table/tree row element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_ROW_GROUP** = `24`

Table/tree row group element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_ROW_HEADER** = `25`

Table/tree row header element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_COLUMN_HEADER** = `26`

Table/tree column header element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TREE** = `27`

Tree view element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TREE_ITEM** = `28`

Tree view item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_LIST** = `29`

List element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_LIST_ITEM** = `30`

List item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_LIST_BOX** = `31`

List view element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_LIST_BOX_OPTION** = `32`

List view item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TAB_BAR** = `33`

Tab bar element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TAB** = `34`

Tab bar item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TAB_PANEL** = `35`

Tab panel element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_MENU_BAR** = `36`

Menu bar element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_MENU** = `37`

Popup menu element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_MENU_ITEM** = `38`

Popup menu item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_MENU_ITEM_CHECK_BOX** = `39`

Popup menu check button item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_MENU_ITEM_RADIO** = `40`

Popup menu radio button item element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_IMAGE** = `41`

Image element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_WINDOW** = `42`

Window element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TITLE_BAR** = `43`

Embedded window title bar element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_DIALOG** = `44`

Dialog window element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TOOLTIP** = `45`

Tooltip element.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_REGION** = `46`

Region/landmark element. Screen readers can navigate between regions using landmark navigation.

classref-enumeration-constant

`AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>` **ROLE_TEXT_RUN** = `47`

Unifor text run.

Note: This role is used for internal text elements, and should not be assigned to nodes.

classref-item-separator

classref-enumeration

enum **AccessibilityPopupType**: `🔗<enum_AccessibilityServer_AccessibilityPopupType>`

classref-enumeration-constant

`AccessibilityPopupType<enum_AccessibilityServer_AccessibilityPopupType>` **POPUP_MENU** = `0`

Popup menu.

classref-enumeration-constant

`AccessibilityPopupType<enum_AccessibilityServer_AccessibilityPopupType>` **POPUP_LIST** = `1`

Popup list.

classref-enumeration-constant

`AccessibilityPopupType<enum_AccessibilityServer_AccessibilityPopupType>` **POPUP_TREE** = `2`

Popup tree view.

classref-enumeration-constant

`AccessibilityPopupType<enum_AccessibilityServer_AccessibilityPopupType>` **POPUP_DIALOG** = `3`

Popup dialog.

classref-item-separator

classref-enumeration

enum **AccessibilityFlags**: `🔗<enum_AccessibilityServer_AccessibilityFlags>`

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_HIDDEN** = `0`

Element is hidden for accessibility tools.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_MULTISELECTABLE** = `1`

Element supports multiple item selection.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_REQUIRED** = `2`

Element require user input.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_VISITED** = `3`

Element is a visited link.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_BUSY** = `4`

Element content is not ready (e.g. loading).

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_MODAL** = `5`

Element is modal window.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_TOUCH_PASSTHROUGH** = `6`

Element allows touches to be passed through when a screen reader is in touch exploration mode.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_READONLY** = `7`

Element is text field with selectable but read-only text.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_DISABLED** = `8`

Element is disabled.

classref-enumeration-constant

`AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>` **FLAG_CLIPS_CHILDREN** = `9`

Element clips children.

classref-item-separator

classref-enumeration

enum **AccessibilityAction**: `🔗<enum_AccessibilityServer_AccessibilityAction>`

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_CLICK** = `0`

Single click action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_FOCUS** = `1`

Focus action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_BLUR** = `2`

Blur action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_COLLAPSE** = `3`

Collapse action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_EXPAND** = `4`

Expand action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_DECREMENT** = `5`

Decrement action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_INCREMENT** = `6`

Increment action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_HIDE_TOOLTIP** = `7`

Hide tooltip action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SHOW_TOOLTIP** = `8`

Show tooltip action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SET_TEXT_SELECTION** = `9`

Set text selection action, callback argument is set to `Dictionary<class_Dictionary>` with the following keys:

- `"start_element"` accessibility element of the selection start.
- `"start_char"` character offset relative to the accessibility element of the selection start.
- `"end_element"` accessibility element of the selection end.
- `"end_char"` character offset relative to the accessibility element of the selection end.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_REPLACE_SELECTED_TEXT** = `10`

Replace text action, callback argument is set to `String<class_String>` with the replacement text.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_BACKWARD** = `11`

Scroll backward action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_DOWN** = `12`

Scroll down action, callback argument is set to `AccessibilityScrollUnit<enum_AccessibilityServer_AccessibilityScrollUnit>`.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_FORWARD** = `13`

Scroll forward action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_LEFT** = `14`

Scroll left action, callback argument is set to `AccessibilityScrollUnit<enum_AccessibilityServer_AccessibilityScrollUnit>`.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_RIGHT** = `15`

Scroll right action, callback argument is set to `AccessibilityScrollUnit<enum_AccessibilityServer_AccessibilityScrollUnit>`.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_UP** = `16`

Scroll up action, callback argument is set to `AccessibilityScrollUnit<enum_AccessibilityServer_AccessibilityScrollUnit>`.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_INTO_VIEW** = `17`

Scroll into view action, callback argument is set to `AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>`.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SCROLL_TO_POINT** = `18`

Scroll to point action, callback argument is set to `Vector2<class_Vector2>` with the relative point coordinates.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SET_SCROLL_OFFSET** = `19`

Set scroll offset action, callback argument is set to `Vector2<class_Vector2>` with the scroll offset.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SET_VALUE** = `20`

Set value action, callback argument is set to `String<class_String>` or number with the new value.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_SHOW_CONTEXT_MENU** = `21`

Show context menu action, callback argument is not set.

classref-enumeration-constant

`AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>` **ACTION_CUSTOM** = `22`

Custom action, callback argument is set to the integer action ID.

classref-item-separator

classref-enumeration

enum **AccessibilityLiveMode**: `🔗<enum_AccessibilityServer_AccessibilityLiveMode>`

classref-enumeration-constant

`AccessibilityLiveMode<enum_AccessibilityServer_AccessibilityLiveMode>` **LIVE_OFF** = `0`

Indicates that updates to the live region should not be presented.

classref-enumeration-constant

`AccessibilityLiveMode<enum_AccessibilityServer_AccessibilityLiveMode>` **LIVE_POLITE** = `1`

Indicates that updates to the live region should be presented at the next opportunity (for example at the end of speaking the current sentence).

classref-enumeration-constant

`AccessibilityLiveMode<enum_AccessibilityServer_AccessibilityLiveMode>` **LIVE_ASSERTIVE** = `2`

Indicates that updates to the live region have the highest priority and should be presented immediately.

classref-item-separator

classref-enumeration

enum **AccessibilityScrollUnit**: `🔗<enum_AccessibilityServer_AccessibilityScrollUnit>`

classref-enumeration-constant

`AccessibilityScrollUnit<enum_AccessibilityServer_AccessibilityScrollUnit>` **SCROLL_UNIT_ITEM** = `0`

The amount by which to scroll. A single item of a list, line of text.

classref-enumeration-constant

`AccessibilityScrollUnit<enum_AccessibilityServer_AccessibilityScrollUnit>` **SCROLL_UNIT_PAGE** = `1`

The amount by which to scroll. A single page.

classref-item-separator

classref-enumeration

enum **AccessibilityScrollHint**: `🔗<enum_AccessibilityServer_AccessibilityScrollHint>`

classref-enumeration-constant

`AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>` **SCROLL_HINT_TOP_LEFT** = `0`

A preferred position for the node scrolled into view. Top-left edge of the scroll container.

classref-enumeration-constant

`AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>` **SCROLL_HINT_BOTTOM_RIGHT** = `1`

A preferred position for the node scrolled into view. Bottom-right edge of the scroll container.

classref-enumeration-constant

`AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>` **SCROLL_HINT_TOP_EDGE** = `2`

A preferred position for the node scrolled into view. Top edge of the scroll container.

classref-enumeration-constant

`AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>` **SCROLL_HINT_BOTTOM_EDGE** = `3`

A preferred position for the node scrolled into view. Bottom edge of the scroll container.

classref-enumeration-constant

`AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>` **SCROLL_HINT_LEFT_EDGE** = `4`

A preferred position for the node scrolled into view. Left edge of the scroll container.

classref-enumeration-constant

`AccessibilityScrollHint<enum_AccessibilityServer_AccessibilityScrollHint>` **SCROLL_HINT_RIGHT_EDGE** = `5`

A preferred position for the node scrolled into view. Right edge of the scroll container.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **create_element**(window_id: `int<class_int>`, role: `AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>`) `🔗<class_AccessibilityServer_method_create_element>`

Creates a new, empty accessibility element resource.

**Note:** An accessibility element is created and freed automatically for each `Node<class_Node>`. In general, this function should not be called manually.

classref-item-separator

classref-method

`RID<class_RID>` **create_sub_element**(parent_rid: `RID<class_RID>`, role: `AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>`, insert_pos: `int<class_int>` = -1) `🔗<class_AccessibilityServer_method_create_sub_element>`

Creates a new, empty accessibility sub-element resource. Sub-elements can be used to provide accessibility information for objects which are not `Node<class_Node>`s, such as list items, table cells, or menu items. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the `free_element()<class_AccessibilityServer_method_free_element>` method.

classref-item-separator

classref-method

`RID<class_RID>` **create_sub_text_edit_elements**(parent_rid: `RID<class_RID>`, shaped_text: `RID<class_RID>`, min_height: `float<class_float>`, insert_pos: `int<class_int>` = -1, is_last_line: `bool<class_bool>` = false) `🔗<class_AccessibilityServer_method_create_sub_text_edit_elements>`

Creates a new, empty accessibility sub-element from the shaped text buffer. Sub-elements are freed automatically when the parent element is freed, or can be freed early using the `free_element()<class_AccessibilityServer_method_free_element>` method.

If `is_last_line` is `true`, no trailing newline is appended to the text content. Set to `true` for the last line in multi-line text fields and for single-line text fields.

classref-item-separator

classref-method

`Variant<class_Variant>` **element_get_meta**(id: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AccessibilityServer_method_element_get_meta>`

Returns the metadata of the accessibility element `id`.

classref-item-separator

classref-method

`void (No return value.)` **element_set_meta**(id: `RID<class_RID>`, meta: `Variant<class_Variant>`) `🔗<class_AccessibilityServer_method_element_set_meta>`

Sets the metadata of the accessibility element `id` to `meta`.

classref-item-separator

classref-method

`void (No return value.)` **free_element**(id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_free_element>`

Frees the accessibility element `id` created by `create_element()<class_AccessibilityServer_method_create_element>`, `create_sub_element()<class_AccessibilityServer_method_create_sub_element>`, or `create_sub_text_edit_elements()<class_AccessibilityServer_method_create_sub_text_edit_elements>`.

classref-item-separator

classref-method

`RID<class_RID>` **get_window_root**(window_id: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AccessibilityServer_method_get_window_root>`

Returns the main accessibility element of the OS native window.

classref-item-separator

classref-method

`bool<class_bool>` **has_element**(id: `RID<class_RID>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AccessibilityServer_method_has_element>`

Returns `true` if `id` is a valid accessibility element.

classref-item-separator

classref-method

`bool<class_bool>` **is_supported**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AccessibilityServer_method_is_supported>`

Returns `true` if screen reader is support by this implementation.

classref-item-separator

classref-method

`void (No return value.)` **set_window_focused**(window_id: `int<class_int>`, focused: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_set_window_focused>`

Sets the window focused state for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! `Window<class_Window>` objects call this method automatically.

classref-item-separator

classref-method

`void (No return value.)` **set_window_rect**(window_id: `int<class_int>`, rect_out: `Rect2<class_Rect2>`, rect_in: `Rect2<class_Rect2>`) `🔗<class_AccessibilityServer_method_set_window_rect>`

Sets window outer (with decorations) and inner (without decorations) bounds for assistive apps.

**Note:** This method is implemented on Linux, macOS, and Windows.

**Note:** Advanced users only! `Window<class_Window>` objects call this method automatically.

classref-item-separator

classref-method

`void (No return value.)` **update_add_action**(id: `RID<class_RID>`, action: `AccessibilityAction<enum_AccessibilityServer_AccessibilityAction>`, callable: `Callable<class_Callable>`) `🔗<class_AccessibilityServer_method_update_add_action>`

Adds a callback for the accessibility action (action which can be performed by using a special screen reader command or buttons on the Braille display), and marks this action as supported. The action callback receives one `Variant<class_Variant>` argument, which value depends on action type.

classref-item-separator

classref-method

`void (No return value.)` **update_add_child**(id: `RID<class_RID>`, child_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_child>`

Adds a child accessibility element.

**Note:** `Node<class_Node>` children and sub-elements are added to the child list automatically.

classref-item-separator

classref-method

`void (No return value.)` **update_add_custom_action**(id: `RID<class_RID>`, action_id: `int<class_int>`, action_description: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_add_custom_action>`

Adds support for a custom accessibility action. `action_id` is passed as an argument to the callback of `ACTION_CUSTOM<class_AccessibilityServer_constant_ACTION_CUSTOM>` action.

classref-item-separator

classref-method

`void (No return value.)` **update_add_related_controls**(id: `RID<class_RID>`, related_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_related_controls>`

Adds an element that is controlled by this element.

classref-item-separator

classref-method

`void (No return value.)` **update_add_related_described_by**(id: `RID<class_RID>`, related_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_related_described_by>`

Adds an element that describes this element.

classref-item-separator

classref-method

`void (No return value.)` **update_add_related_details**(id: `RID<class_RID>`, related_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_related_details>`

Adds an element that details this element.

classref-item-separator

classref-method

`void (No return value.)` **update_add_related_flow_to**(id: `RID<class_RID>`, related_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_related_flow_to>`

Adds an element that this element flow into.

classref-item-separator

classref-method

`void (No return value.)` **update_add_related_labeled_by**(id: `RID<class_RID>`, related_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_related_labeled_by>`

Adds an element that labels this element.

classref-item-separator

classref-method

`void (No return value.)` **update_add_related_radio_group**(id: `RID<class_RID>`, related_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_add_related_radio_group>`

Adds an element that is part of the same radio group.

**Note:** This method should be called on each element of the group, using all other elements as `related_id`.

classref-item-separator

classref-method

`void (No return value.)` **update_set_active_descendant**(id: `RID<class_RID>`, other_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_active_descendant>`

Adds an element that is an active descendant of this element.

classref-item-separator

classref-method

`void (No return value.)` **update_set_background_color**(id: `RID<class_RID>`, color: `Color<class_Color>`) `🔗<class_AccessibilityServer_method_update_set_background_color>`

Sets element background color.

classref-item-separator

classref-method

`void (No return value.)` **update_set_bounds**(id: `RID<class_RID>`, rect: `Rect2<class_Rect2>`) `🔗<class_AccessibilityServer_method_update_set_bounds>`

Sets element bounding box, relative to the node position.

classref-item-separator

classref-method

`void (No return value.)` **update_set_braille_label**(id: `RID<class_RID>`, name: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_braille_label>`

Sets element accessibility label for Braille display.

classref-item-separator

classref-method

`void (No return value.)` **update_set_braille_role_description**(id: `RID<class_RID>`, description: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_braille_role_description>`

Sets element accessibility role description for Braille display.

classref-item-separator

classref-method

`void (No return value.)` **update_set_checked**(id: `RID<class_RID>`, checekd: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_update_set_checked>`

Sets element checked state.

classref-item-separator

classref-method

`void (No return value.)` **update_set_classname**(id: `RID<class_RID>`, classname: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_classname>`

Sets element class name.

classref-item-separator

classref-method

`void (No return value.)` **update_set_color_value**(id: `RID<class_RID>`, color: `Color<class_Color>`) `🔗<class_AccessibilityServer_method_update_set_color_value>`

Sets element color value.

classref-item-separator

classref-method

`void (No return value.)` **update_set_description**(id: `RID<class_RID>`, description: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_description>`

Sets element accessibility description.

classref-item-separator

classref-method

`void (No return value.)` **update_set_error_message**(id: `RID<class_RID>`, other_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_error_message>`

Sets an element which contains an error message for this element.

classref-item-separator

classref-method

`void (No return value.)` **update_set_extra_info**(id: `RID<class_RID>`, name: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_extra_info>`

Sets element accessibility extra information added to the element name.

classref-item-separator

classref-method

`void (No return value.)` **update_set_flag**(id: `RID<class_RID>`, flag: `AccessibilityFlags<enum_AccessibilityServer_AccessibilityFlags>`, value: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_update_set_flag>`

Sets element flag.

classref-item-separator

classref-method

`void (No return value.)` **update_set_focus**(id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_focus>`

Sets currently focused element.

classref-item-separator

classref-method

`void (No return value.)` **update_set_foreground_color**(id: `RID<class_RID>`, color: `Color<class_Color>`) `🔗<class_AccessibilityServer_method_update_set_foreground_color>`

Sets element foreground color.

classref-item-separator

classref-method

`void (No return value.)` **update_set_in_page_link_target**(id: `RID<class_RID>`, other_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_in_page_link_target>`

Sets target element for the link.

classref-item-separator

classref-method

`void (No return value.)` **update_set_language**(id: `RID<class_RID>`, language: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_language>`

Sets element text language.

classref-item-separator

classref-method

`void (No return value.)` **update_set_list_item_count**(id: `RID<class_RID>`, size: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_list_item_count>`

Sets number of items in the list.

classref-item-separator

classref-method

`void (No return value.)` **update_set_list_item_expanded**(id: `RID<class_RID>`, expanded: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_update_set_list_item_expanded>`

Sets list/tree item expanded status.

classref-item-separator

classref-method

`void (No return value.)` **update_set_list_item_index**(id: `RID<class_RID>`, index: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_list_item_index>`

Sets the position of the element in the list.

classref-item-separator

classref-method

`void (No return value.)` **update_set_list_item_level**(id: `RID<class_RID>`, level: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_list_item_level>`

Sets the hierarchical level of the element in the list.

classref-item-separator

classref-method

`void (No return value.)` **update_set_list_item_selected**(id: `RID<class_RID>`, selected: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_update_set_list_item_selected>`

Sets list/tree item selected status.

classref-item-separator

classref-method

`void (No return value.)` **update_set_list_orientation**(id: `RID<class_RID>`, vertical: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_update_set_list_orientation>`

Sets the orientation of the list elements.

classref-item-separator

classref-method

`void (No return value.)` **update_set_live**(id: `RID<class_RID>`, live: `AccessibilityLiveMode<enum_AccessibilityServer_AccessibilityLiveMode>`) `🔗<class_AccessibilityServer_method_update_set_live>`

Sets the priority of the live region updates.

classref-item-separator

classref-method

`void (No return value.)` **update_set_member_of**(id: `RID<class_RID>`, group_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_member_of>`

Sets the element to be a member of the group.

classref-item-separator

classref-method

`void (No return value.)` **update_set_name**(id: `RID<class_RID>`, name: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_name>`

Sets element accessibility name.

classref-item-separator

classref-method

`void (No return value.)` **update_set_next_on_line**(id: `RID<class_RID>`, other_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_next_on_line>`

Sets next element on the line.

classref-item-separator

classref-method

`void (No return value.)` **update_set_num_jump**(id: `RID<class_RID>`, jump: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_num_jump>`

Sets numeric value jump.

classref-item-separator

classref-method

`void (No return value.)` **update_set_num_range**(id: `RID<class_RID>`, min: `float<class_float>`, max: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_num_range>`

Sets numeric value range.

classref-item-separator

classref-method

`void (No return value.)` **update_set_num_step**(id: `RID<class_RID>`, step: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_num_step>`

Sets numeric value step.

classref-item-separator

classref-method

`void (No return value.)` **update_set_num_value**(id: `RID<class_RID>`, position: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_num_value>`

Sets numeric value.

classref-item-separator

classref-method

`void (No return value.)` **update_set_placeholder**(id: `RID<class_RID>`, placeholder: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_placeholder>`

Sets placeholder text.

classref-item-separator

classref-method

`void (No return value.)` **update_set_popup_type**(id: `RID<class_RID>`, popup: `AccessibilityPopupType<enum_AccessibilityServer_AccessibilityPopupType>`) `🔗<class_AccessibilityServer_method_update_set_popup_type>`

Sets popup type for popup buttons.

classref-item-separator

classref-method

`void (No return value.)` **update_set_previous_on_line**(id: `RID<class_RID>`, other_id: `RID<class_RID>`) `🔗<class_AccessibilityServer_method_update_set_previous_on_line>`

Sets previous element on the line.

classref-item-separator

classref-method

`void (No return value.)` **update_set_role**(id: `RID<class_RID>`, role: `AccessibilityRole<enum_AccessibilityServer_AccessibilityRole>`) `🔗<class_AccessibilityServer_method_update_set_role>`

Sets element accessibility role.

classref-item-separator

classref-method

`void (No return value.)` **update_set_role_description**(id: `RID<class_RID>`, description: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_role_description>`

Sets element accessibility role description text.

classref-item-separator

classref-method

`void (No return value.)` **update_set_scroll_x**(id: `RID<class_RID>`, position: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_scroll_x>`

Sets scroll bar x position.

classref-item-separator

classref-method

`void (No return value.)` **update_set_scroll_x_range**(id: `RID<class_RID>`, min: `float<class_float>`, max: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_scroll_x_range>`

Sets scroll bar x range.

classref-item-separator

classref-method

`void (No return value.)` **update_set_scroll_y**(id: `RID<class_RID>`, position: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_scroll_y>`

Sets scroll bar y position.

classref-item-separator

classref-method

`void (No return value.)` **update_set_scroll_y_range**(id: `RID<class_RID>`, min: `float<class_float>`, max: `float<class_float>`) `🔗<class_AccessibilityServer_method_update_set_scroll_y_range>`

Sets scroll bar y range.

classref-item-separator

classref-method

`void (No return value.)` **update_set_shortcut**(id: `RID<class_RID>`, shortcut: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_shortcut>`

Sets the list of keyboard shortcuts used by element.

classref-item-separator

classref-method

`void (No return value.)` **update_set_state_description**(id: `RID<class_RID>`, description: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_state_description>`

Sets human-readable description of the current checked state.

classref-item-separator

classref-method

`void (No return value.)` **update_set_table_cell_position**(id: `RID<class_RID>`, row_index: `int<class_int>`, column_index: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_table_cell_position>`

Sets cell position in the table.

classref-item-separator

classref-method

`void (No return value.)` **update_set_table_cell_span**(id: `RID<class_RID>`, row_span: `int<class_int>`, column_span: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_table_cell_span>`

Sets cell row/column span.

classref-item-separator

classref-method

`void (No return value.)` **update_set_table_column_count**(id: `RID<class_RID>`, count: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_table_column_count>`

Sets number of columns in the table.

classref-item-separator

classref-method

`void (No return value.)` **update_set_table_column_index**(id: `RID<class_RID>`, index: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_table_column_index>`

Sets position of the column.

classref-item-separator

classref-method

`void (No return value.)` **update_set_table_row_count**(id: `RID<class_RID>`, count: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_table_row_count>`

Sets number of rows in the table.

classref-item-separator

classref-method

`void (No return value.)` **update_set_table_row_index**(id: `RID<class_RID>`, index: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_table_row_index>`

Sets position of the row in the table.

classref-item-separator

classref-method

`void (No return value.)` **update_set_text_align**(id: `RID<class_RID>`, align: `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`) `🔗<class_AccessibilityServer_method_update_set_text_align>`

Sets element text alignment.

classref-item-separator

classref-method

`void (No return value.)` **update_set_text_decorations**(id: `RID<class_RID>`, underline: `bool<class_bool>`, strikethrough: `bool<class_bool>`, overline: `bool<class_bool>`, color: `Color<class_Color>` = Color(0, 0, 0, 1)) `🔗<class_AccessibilityServer_method_update_set_text_decorations>`

Sets text underline/overline/strikethrough.

classref-item-separator

classref-method

`void (No return value.)` **update_set_text_orientation**(id: `RID<class_RID>`, vertical: `bool<class_bool>`) `🔗<class_AccessibilityServer_method_update_set_text_orientation>`

Sets text orientation.

classref-item-separator

classref-method

`void (No return value.)` **update_set_text_selection**(id: `RID<class_RID>`, text_start_id: `RID<class_RID>`, start_char: `int<class_int>`, text_end_id: `RID<class_RID>`, end_char: `int<class_int>`) `🔗<class_AccessibilityServer_method_update_set_text_selection>`

Sets text selection to the text field. `text_start_id` and `text_end_id` should be elements created by `create_sub_text_edit_elements()<class_AccessibilityServer_method_create_sub_text_edit_elements>`. Character offsets are relative to the corresponding element.

classref-item-separator

classref-method

`void (No return value.)` **update_set_tooltip**(id: `RID<class_RID>`, tooltip: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_tooltip>`

Sets tooltip text.

classref-item-separator

classref-method

`void (No return value.)` **update_set_transform**(id: `RID<class_RID>`, transform: `Transform2D<class_Transform2D>`) `🔗<class_AccessibilityServer_method_update_set_transform>`

Sets element 2D transform.

classref-item-separator

classref-method

`void (No return value.)` **update_set_url**(id: `RID<class_RID>`, url: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_url>`

Sets link URL.

classref-item-separator

classref-method

`void (No return value.)` **update_set_value**(id: `RID<class_RID>`, value: `String<class_String>`) `🔗<class_AccessibilityServer_method_update_set_value>`

Sets element text value.