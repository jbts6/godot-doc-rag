github_url
hide

# Window

**Inherits:** `Viewport<class_Viewport>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

**Inherited By:** `AcceptDialog<class_AcceptDialog>`, `Popup<class_Popup>`

Base class for all windows, dialogs, and popups.

classref-introduction-group

## Description

A node that creates a window. The window can either be a native system window or embedded inside another **Window** (see `Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`).

At runtime, **Window**s will not close automatically when requested. You need to handle it manually using the `close_requested<class_Window_signal_close_requested>` signal (this applies both to pressing the close button and clicking outside of a popup).

classref-introduction-group

## Tutorials

- `HDR output <../tutorials/rendering/hdr_output>`

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

**about_to_popup**() `🔗<class_Window_signal_about_to_popup>`

Emitted right after `popup()<class_Window_method_popup>` call, before the **Window** appears or does anything.

classref-item-separator

classref-signal

**close_requested**() `🔗<class_Window_signal_close_requested>`

Emitted when the **Window**'s close button is pressed or when `popup_window<class_Window_property_popup_window>` is enabled and user clicks outside the window.

This signal can be used to handle window closing, e.g. by connecting it to `hide()<class_Window_method_hide>`.

classref-item-separator

classref-signal

**dpi_changed**() `🔗<class_Window_signal_dpi_changed>`

Emitted when the **Window**'s DPI changes as a result of OS-level changes (e.g. moving the window from a Retina display to a lower resolution one).

**Note:** Only implemented on macOS and Linux (Wayland).

classref-item-separator

classref-signal

**files_dropped**(files: `PackedStringArray<class_PackedStringArray>`) `🔗<class_Window_signal_files_dropped>`

Emitted when files are dragged from the OS file manager and dropped in the game window. The argument is a list of file paths.

    func _ready():
        get_window().files_dropped.connect(on_files_dropped)

    func on_files_dropped(files):
        print(files)

**Note:** This signal only works with native windows, i.e. the main window and **Window**-derived nodes when `Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>` is disabled in the main viewport.

classref-item-separator

classref-signal

**focus_entered**() `🔗<class_Window_signal_focus_entered>`

Emitted when the **Window** gains focus.

classref-item-separator

classref-signal

**focus_exited**() `🔗<class_Window_signal_focus_exited>`

Emitted when the **Window** loses its focus.

classref-item-separator

classref-signal

**go_back_requested**() `🔗<class_Window_signal_go_back_requested>`

Emitted when a go back request is sent (e.g. pressing the "Back" button on Android), right after `Node.NOTIFICATION_WM_GO_BACK_REQUEST<class_Node_constant_NOTIFICATION_WM_GO_BACK_REQUEST>`.

classref-item-separator

classref-signal

**mouse_entered**() `🔗<class_Window_signal_mouse_entered>`

Emitted when the mouse cursor enters the **Window**'s visible area, that is not occluded behind other `Control<class_Control>`s or windows, provided its `Viewport.gui_disable_input<class_Viewport_property_gui_disable_input>` is `false` and regardless if it's currently focused or not.

classref-item-separator

classref-signal

**mouse_exited**() `🔗<class_Window_signal_mouse_exited>`

Emitted when the mouse cursor leaves the **Window**'s visible area, that is not occluded behind other `Control<class_Control>`s or windows, provided its `Viewport.gui_disable_input<class_Viewport_property_gui_disable_input>` is `false` and regardless if it's currently focused or not.

classref-item-separator

classref-signal

**nonclient_window_input**(event: `InputEvent<class_InputEvent>`) `🔗<class_Window_signal_nonclient_window_input>`

Emitted when the mouse event is received by the custom decoration area defined by `nonclient_area<class_Window_property_nonclient_area>`, and normal input to the window is blocked (such as when it has an exclusive child opened). `event`'s position is in the embedder's coordinate system.

classref-item-separator

classref-signal

**output_max_linear_value_changed**(output_max_linear_value: `float<class_float>`) `🔗<class_Window_signal_output_max_linear_value_changed>`

Emitted when the output max linear value returned by `get_output_max_linear_value()<class_Window_method_get_output_max_linear_value>` has changed. This occurs when HDR output is enabled or disabled and when any HDR output luminance values of the window have changed, such as when the player adjusts their screen brightness setting or moves the window to a different screen. `output_max_linear_value` is the new value.

classref-item-separator

classref-signal

**theme_changed**() `🔗<class_Window_signal_theme_changed>`

Emitted when the `NOTIFICATION_THEME_CHANGED<class_Window_constant_NOTIFICATION_THEME_CHANGED>` notification is sent.

classref-item-separator

classref-signal

**title_changed**() `🔗<class_Window_signal_title_changed>`

Emitted when window title bar text is changed.

classref-item-separator

classref-signal

**titlebar_changed**() `🔗<class_Window_signal_titlebar_changed>`

Emitted when window title bar decorations are changed, e.g. macOS window enter/exit full screen mode, or extend-to-title flag is changed.

classref-item-separator

classref-signal

**visibility_changed**() `🔗<class_Window_signal_visibility_changed>`

Emitted when **Window** is made visible or disappears.

classref-item-separator

classref-signal

**window_input**(event: `InputEvent<class_InputEvent>`) `🔗<class_Window_signal_window_input>`

Emitted when the **Window** is currently focused and receives any input, passing the received event as an argument. The event's position, if present, is in the embedder's coordinate system.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Mode**: `🔗<enum_Window_Mode>`

classref-enumeration-constant

`Mode<enum_Window_Mode>` **MODE_WINDOWED** = `0`

Windowed mode, i.e. **Window** doesn't occupy the whole screen (unless set to the size of the screen).

classref-enumeration-constant

`Mode<enum_Window_Mode>` **MODE_MINIMIZED** = `1`

Minimized window mode, i.e. **Window** is not visible and available on window manager's window list. Normally happens when the minimize button is pressed.

classref-enumeration-constant

`Mode<enum_Window_Mode>` **MODE_MAXIMIZED** = `2`

Maximized window mode, i.e. **Window** will occupy whole screen area except task bar and still display its borders. Normally happens when the maximize button is pressed.

classref-enumeration-constant

`Mode<enum_Window_Mode>` **MODE_FULLSCREEN** = `3`

Full screen mode with full multi-window support.

Full screen window covers the entire display area of a screen and has no decorations. The display's video mode is not changed.

**On Android:** This enables immersive mode.

**On macOS:** A new desktop is used to display the running project.

**Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports `multiple resolutions <../tutorials/rendering/multiple_resolutions>` when enabling full screen mode.

classref-enumeration-constant

`Mode<enum_Window_Mode>` **MODE_EXCLUSIVE_FULLSCREEN** = `4`

A single window full screen mode. This mode has less overhead, but only one window can be open on a given screen at a time (opening a child window or application switching will trigger a full screen transition).

Full screen window covers the entire display area of a screen and has no border or decorations. The display's video mode is not changed.

**Note:** This mode might not work with screen recording software.

**On Android:** This enables immersive mode.

**On Windows:** Depending on video driver, full screen transition might cause screens to go black for a moment.

**On macOS:** A new desktop is used to display the running project. Exclusive full screen mode prevents Dock and Menu from showing up when the mouse pointer is hovering the edge of the screen.

**On Linux (X11):** Exclusive full screen mode bypasses compositor.

**On Linux (Wayland):** Equivalent to `MODE_FULLSCREEN<class_Window_constant_MODE_FULLSCREEN>`.

**Note:** Regardless of the platform, enabling full screen will change the window size to match the monitor's size. Therefore, make sure your project supports `multiple resolutions <../tutorials/rendering/multiple_resolutions>` when enabling full screen mode.

classref-item-separator

classref-enumeration

enum **Flags**: `🔗<enum_Window_Flags>`

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_RESIZE_DISABLED** = `0`

The window can't be resized by dragging its resize grip. It's still possible to resize the window using `size<class_Window_property_size>`. This flag is ignored for full screen windows. Set with `unresizable<class_Window_property_unresizable>`.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_BORDERLESS** = `1`

The window do not have native title bar and other decorations. This flag is ignored for full-screen windows. Set with `borderless<class_Window_property_borderless>`.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_ALWAYS_ON_TOP** = `2`

The window is floating on top of all other windows. This flag is ignored for full-screen windows. Set with `always_on_top<class_Window_property_always_on_top>`.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_TRANSPARENT** = `3`

The window background can be transparent. Set with `transparent<class_Window_property_transparent>`.

**Note:** This flag has no effect if either `ProjectSettings.display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>`, or the window's `Viewport.transparent_bg<class_Viewport_property_transparent_bg>` is set to `false`.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_NO_FOCUS** = `4`

The window can't be focused. No-focus window will ignore all input, except mouse clicks. Set with `unfocusable<class_Window_property_unfocusable>`.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_POPUP** = `5`

Window is part of menu or `OptionButton<class_OptionButton>` dropdown. This flag can't be changed when the window is visible. An active popup window will exclusively receive all input, without stealing focus from its parent. Popup windows are automatically closed when uses click outside it, or when an application is switched. Popup window must have transient parent set (see `transient<class_Window_property_transient>`).

**Note:** This flag has no effect in embedded windows (unless said window is a `Popup<class_Popup>`).

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_EXTEND_TO_TITLE** = `6`

Window content is expanded to the full size of the window. Unlike borderless window, the frame is left intact and can be used to resize the window, title bar is transparent, but have minimize/maximize/close buttons. Set with `extend_to_title<class_Window_property_extend_to_title>`.

**Note:** This flag is implemented only on macOS.

**Note:** This flag has no effect in embedded windows.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_MOUSE_PASSTHROUGH** = `7`

All mouse events are passed to the underlying window of the same application.

**Note:** This flag has no effect in embedded windows.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_SHARP_CORNERS** = `8`

Window style is overridden, forcing sharp corners.

**Note:** This flag has no effect in embedded windows.

**Note:** This flag is implemented only on Windows (11).

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_EXCLUDE_FROM_CAPTURE** = `9`

Windows is excluded from screenshots taken by `DisplayServer.screen_get_image()<class_DisplayServer_method_screen_get_image>`, `DisplayServer.screen_get_image_rect()<class_DisplayServer_method_screen_get_image_rect>`, and `DisplayServer.screen_get_pixel()<class_DisplayServer_method_screen_get_pixel>`.

**Note:** This flag has no effect in embedded windows.

**Note:** This flag is implemented on macOS and Windows (10, 20H1).

**Note:** Setting this flag will prevent standard screenshot methods from capturing a window image, but does **NOT** guarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_POPUP_WM_HINT** = `10`

Signals the window manager that this window is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_MINIMIZE_DISABLED** = `11`

Window minimize button is disabled.

**Note:** This flag is implemented on macOS and Windows.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_MAXIMIZE_DISABLED** = `12`

Window maximize button is disabled.

**Note:** This flag is implemented on macOS and Windows.

classref-enumeration-constant

`Flags<enum_Window_Flags>` **FLAG_MAX** = `13`

Max value of the `Flags<enum_Window_Flags>`.

classref-item-separator

classref-enumeration

enum **ContentScaleMode**: `🔗<enum_Window_ContentScaleMode>`

classref-enumeration-constant

`ContentScaleMode<enum_Window_ContentScaleMode>` **CONTENT_SCALE_MODE_DISABLED** = `0`

The content will not be scaled to match the **Window**'s size (`content_scale_size<class_Window_property_content_scale_size>` is ignored).

classref-enumeration-constant

`ContentScaleMode<enum_Window_ContentScaleMode>` **CONTENT_SCALE_MODE_CANVAS_ITEMS** = `1`

The content will be rendered at the target size. This is more performance-expensive than `CONTENT_SCALE_MODE_VIEWPORT<class_Window_constant_CONTENT_SCALE_MODE_VIEWPORT>`, but provides better results.

classref-enumeration-constant

`ContentScaleMode<enum_Window_ContentScaleMode>` **CONTENT_SCALE_MODE_VIEWPORT** = `2`

The content will be rendered at the base size and then scaled to the target size. More performant than `CONTENT_SCALE_MODE_CANVAS_ITEMS<class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS>`, but results in pixelated image.

classref-item-separator

classref-enumeration

enum **ContentScaleAspect**: `🔗<enum_Window_ContentScaleAspect>`

classref-enumeration-constant

`ContentScaleAspect<enum_Window_ContentScaleAspect>` **CONTENT_SCALE_ASPECT_IGNORE** = `0`

The aspect will be ignored. Scaling will simply stretch the content to fit the target size.

classref-enumeration-constant

`ContentScaleAspect<enum_Window_ContentScaleAspect>` **CONTENT_SCALE_ASPECT_KEEP** = `1`

The content's aspect will be preserved. If the target size has different aspect from the base one, the image will be centered and black bars will appear on left and right sides.

classref-enumeration-constant

`ContentScaleAspect<enum_Window_ContentScaleAspect>` **CONTENT_SCALE_ASPECT_KEEP_WIDTH** = `2`

The content can be expanded vertically. Scaling horizontally will result in keeping the width ratio and then black bars on left and right sides.

classref-enumeration-constant

`ContentScaleAspect<enum_Window_ContentScaleAspect>` **CONTENT_SCALE_ASPECT_KEEP_HEIGHT** = `3`

The content can be expanded horizontally. Scaling vertically will result in keeping the height ratio and then black bars on top and bottom sides.

classref-enumeration-constant

`ContentScaleAspect<enum_Window_ContentScaleAspect>` **CONTENT_SCALE_ASPECT_EXPAND** = `4`

The content's aspect will be preserved. If the target size has different aspect from the base one, the content will stay in the top-left corner and add an extra visible area in the stretched space.

classref-item-separator

classref-enumeration

enum **ContentScaleStretch**: `🔗<enum_Window_ContentScaleStretch>`

classref-enumeration-constant

`ContentScaleStretch<enum_Window_ContentScaleStretch>` **CONTENT_SCALE_STRETCH_FRACTIONAL** = `0`

The content will be stretched according to a fractional factor. This fills all the space available in the window, but allows "pixel wobble" to occur due to uneven pixel scaling.

classref-enumeration-constant

`ContentScaleStretch<enum_Window_ContentScaleStretch>` **CONTENT_SCALE_STRETCH_INTEGER** = `1`

The content will be stretched only according to an integer factor, preserving sharp pixels. This may leave a black background visible on the window's edges depending on the window size.

classref-item-separator

classref-enumeration

enum **LayoutDirection**: `🔗<enum_Window_LayoutDirection>`

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_INHERITED** = `0`

Automatic layout direction, determined from the parent window layout direction.

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_APPLICATION_LOCALE** = `1`

Automatic layout direction, determined from the current locale.

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_LTR** = `2`

Left-to-right layout direction.

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_RTL** = `3`

Right-to-left layout direction.

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_SYSTEM_LOCALE** = `4`

Automatic layout direction, determined from the system locale.

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_MAX** = `5`

Represents the size of the `LayoutDirection<enum_Window_LayoutDirection>` enum.

classref-enumeration-constant

`LayoutDirection<enum_Window_LayoutDirection>` **LAYOUT_DIRECTION_LOCALE** = `1`

**Deprecated:** Use `LAYOUT_DIRECTION_APPLICATION_LOCALE<class_Window_constant_LAYOUT_DIRECTION_APPLICATION_LOCALE>` instead.

classref-item-separator

classref-enumeration

enum **WindowInitialPosition**: `🔗<enum_Window_WindowInitialPosition>`

classref-enumeration-constant

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **WINDOW_INITIAL_POSITION_ABSOLUTE** = `0`

Initial window position is determined by `position<class_Window_property_position>`.

classref-enumeration-constant

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **WINDOW_INITIAL_POSITION_CENTER_PRIMARY_SCREEN** = `1`

Initial window position is the center of the primary screen.

classref-enumeration-constant

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **WINDOW_INITIAL_POSITION_CENTER_MAIN_WINDOW_SCREEN** = `2`

Initial window position is the center of the main window screen.

classref-enumeration-constant

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **WINDOW_INITIAL_POSITION_CENTER_OTHER_SCREEN** = `3`

Initial window position is the center of `current_screen<class_Window_property_current_screen>` screen.

classref-enumeration-constant

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_MOUSE_FOCUS** = `4`

Initial window position is the center of the screen containing the mouse pointer.

classref-enumeration-constant

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **WINDOW_INITIAL_POSITION_CENTER_SCREEN_WITH_KEYBOARD_FOCUS** = `5`

Initial window position is the center of the screen containing the window with the keyboard focus.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**NOTIFICATION_VISIBILITY_CHANGED** = `30` `🔗<class_Window_constant_NOTIFICATION_VISIBILITY_CHANGED>`

Emitted when **Window**'s visibility changes, right before `visibility_changed<class_Window_signal_visibility_changed>`.

classref-constant

**NOTIFICATION_THEME_CHANGED** = `32` `🔗<class_Window_constant_NOTIFICATION_THEME_CHANGED>`

Sent when the node needs to refresh its theme items. This happens in one of the following cases:

- The `theme<class_Window_property_theme>` property is changed on this node or any of its ancestors.
- The `theme_type_variation<class_Window_property_theme_type_variation>` property is changed on this node.
- The node enters the scene tree.

**Note:** As an optimization, this notification won't be sent from changes that occur while this node is outside of the scene tree. Instead, all of the theme item updates can be applied at once when the node enters the scene tree.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **accessibility_description** = `""` `🔗<class_Window_property_accessibility_description>`

classref-property-setget

- `void (No return value.)` **set_accessibility_description**(value: `String<class_String>`)
- `String<class_String>` **get_accessibility_description**()

The human-readable node description that is reported to assistive apps.

classref-item-separator

classref-property

`String<class_String>` **accessibility_name** = `""` `🔗<class_Window_property_accessibility_name>`

classref-property-setget

- `void (No return value.)` **set_accessibility_name**(value: `String<class_String>`)
- `String<class_String>` **get_accessibility_name**()

The human-readable node name that is reported to assistive apps.

classref-item-separator

classref-property

`bool<class_bool>` **always_on_top** = `false` `🔗<class_Window_property_always_on_top>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the window will be on top of all other windows. Does not work if `transient<class_Window_property_transient>` is enabled.

classref-item-separator

classref-property

`bool<class_bool>` **auto_translate** `🔗<class_Window_property_auto_translate>`

classref-property-setget

- `void (No return value.)` **set_auto_translate**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_auto_translating**()

**Deprecated:** Use `Node.auto_translate_mode<class_Node_property_auto_translate_mode>` and `Node.can_auto_translate()<class_Node_method_can_auto_translate>` instead.

Toggles if any text should automatically change to its translated version depending on the current locale.

classref-item-separator

classref-property

`bool<class_bool>` **borderless** = `false` `🔗<class_Window_property_borderless>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the window will have no borders.

classref-item-separator

classref-property

`ContentScaleAspect<enum_Window_ContentScaleAspect>` **content_scale_aspect** = `0` `🔗<class_Window_property_content_scale_aspect>`

classref-property-setget

- `void (No return value.)` **set_content_scale_aspect**(value: `ContentScaleAspect<enum_Window_ContentScaleAspect>`)
- `ContentScaleAspect<enum_Window_ContentScaleAspect>` **get_content_scale_aspect**()

Specifies how the content's aspect behaves when the **Window** is resized. The base aspect is determined by `content_scale_size<class_Window_property_content_scale_size>`.

classref-item-separator

classref-property

`float<class_float>` **content_scale_factor** = `1.0` `🔗<class_Window_property_content_scale_factor>`

classref-property-setget

- `void (No return value.)` **set_content_scale_factor**(value: `float<class_float>`)
- `float<class_float>` **get_content_scale_factor**()

Specifies the base scale of **Window**'s content when its `size<class_Window_property_size>` is equal to `content_scale_size<class_Window_property_content_scale_size>`. See also `Viewport.get_stretch_transform()<class_Viewport_method_get_stretch_transform>`.

classref-item-separator

classref-property

`ContentScaleMode<enum_Window_ContentScaleMode>` **content_scale_mode** = `0` `🔗<class_Window_property_content_scale_mode>`

classref-property-setget

- `void (No return value.)` **set_content_scale_mode**(value: `ContentScaleMode<enum_Window_ContentScaleMode>`)
- `ContentScaleMode<enum_Window_ContentScaleMode>` **get_content_scale_mode**()

Specifies how the content is scaled when the **Window** is resized.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **content_scale_size** = `Vector2i(0, 0)` `🔗<class_Window_property_content_scale_size>`

classref-property-setget

- `void (No return value.)` **set_content_scale_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_content_scale_size**()

The content's base size in "virtual" pixels. Not to be confused with `size<class_Window_property_size>`, which sets the actual window's physical size in pixels. If set to a value greater than `0` and `content_scale_mode<class_Window_property_content_scale_mode>` is set to a value other than `CONTENT_SCALE_MODE_DISABLED<class_Window_constant_CONTENT_SCALE_MODE_DISABLED>`, the **Window**'s content will be scaled when the window is resized to a different size. Higher values will make the content appear *smaller*, as it will be able to fit more of the project in view. On the root **Window**, this is set to match `ProjectSettings.display/window/size/viewport_width<class_ProjectSettings_property_display/window/size/viewport_width>` and `ProjectSettings.display/window/size/viewport_height<class_ProjectSettings_property_display/window/size/viewport_height>` by default.

For example, when using `CONTENT_SCALE_MODE_CANVAS_ITEMS<class_Window_constant_CONTENT_SCALE_MODE_CANVAS_ITEMS>` and `content_scale_size<class_Window_property_content_scale_size>` set to `Vector2i(1280, 720)`, using a window size of `2560×1440` will make 2D elements appear at double their original size, as the content is scaled by a factor of `2.0` (`2560.0 / 1280.0 = 2.0`, `1440.0 / 720.0 = 2.0`).

See [the Base size section of the Multiple resolutions documentation](../tutorials/rendering/multiple_resolutions.html#base-size) for details.

classref-item-separator

classref-property

`ContentScaleStretch<enum_Window_ContentScaleStretch>` **content_scale_stretch** = `0` `🔗<class_Window_property_content_scale_stretch>`

classref-property-setget

- `void (No return value.)` **set_content_scale_stretch**(value: `ContentScaleStretch<enum_Window_ContentScaleStretch>`)
- `ContentScaleStretch<enum_Window_ContentScaleStretch>` **get_content_scale_stretch**()

The policy to use to determine the final scale factor for 2D elements. This affects how `content_scale_factor<class_Window_property_content_scale_factor>` is applied, in addition to the automatic scale factor determined by `content_scale_size<class_Window_property_content_scale_size>`.

classref-item-separator

classref-property

`int<class_int>` **current_screen** `🔗<class_Window_property_current_screen>`

classref-property-setget

- `void (No return value.)` **set_current_screen**(value: `int<class_int>`)
- `int<class_int>` **get_current_screen**()

The screen the window is currently on.

classref-item-separator

classref-property

`bool<class_bool>` **exclude_from_capture** = `false` `🔗<class_Window_property_exclude_from_capture>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window** is excluded from screenshots taken by `DisplayServer.screen_get_image()<class_DisplayServer_method_screen_get_image>`, `DisplayServer.screen_get_image_rect()<class_DisplayServer_method_screen_get_image_rect>`, and `DisplayServer.screen_get_pixel()<class_DisplayServer_method_screen_get_pixel>`.

**Note:** This property is implemented on macOS and Windows.

**Note:** Enabling this setting will prevent standard screenshot methods from capturing a window image, but does **NOT** guarantee that other apps won't be able to capture an image. It should not be used as a DRM or security measure.

classref-item-separator

classref-property

`bool<class_bool>` **exclusive** = `false` `🔗<class_Window_property_exclusive>`

classref-property-setget

- `void (No return value.)` **set_exclusive**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_exclusive**()

If `true`, the **Window** will be in exclusive mode. Exclusive windows are always on top of their parent and will block all input going to the parent **Window**.

Needs `transient<class_Window_property_transient>` enabled to work.

classref-item-separator

classref-property

`bool<class_bool>` **extend_to_title** = `false` `🔗<class_Window_property_extend_to_title>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window** contents is expanded to the full size of the window, window title bar is transparent.

**Note:** This property is implemented only on macOS.

**Note:** This property only works with native windows.

classref-item-separator

classref-property

`bool<class_bool>` **force_native** = `false` `🔗<class_Window_property_force_native>`

classref-property-setget

- `void (No return value.)` **set_force_native**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_force_native**()

If `true`, native window will be used regardless of parent viewport and project settings.

classref-item-separator

classref-property

`bool<class_bool>` **hdr_output_requested** = `false` `🔗<class_Window_property_hdr_output_requested>`

classref-property-setget

- `void (No return value.)` **set_hdr_output_requested**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_hdr_output_requested**()

If `true`, requests HDR output for the **Window**, falling back to SDR if not supported, and automatically switching between HDR and SDR as the window moves between screens, screen capabilities change, or system settings are modified. This will internally force `Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>` to be enabled on the main `Viewport<class_Viewport>`. All other `SubViewport<class_SubViewport>` of this **Window** must have their `Viewport.use_hdr_2d<class_Viewport_property_use_hdr_2d>` property enabled to produce HDR output.

classref-item-separator

classref-property

`WindowInitialPosition<enum_Window_WindowInitialPosition>` **initial_position** = `0` `🔗<class_Window_property_initial_position>`

classref-property-setget

- `void (No return value.)` **set_initial_position**(value: `WindowInitialPosition<enum_Window_WindowInitialPosition>`)
- `WindowInitialPosition<enum_Window_WindowInitialPosition>` **get_initial_position**()

Specifies the initial type of position for the **Window**.

classref-item-separator

classref-property

`bool<class_bool>` **keep_title_visible** = `false` `🔗<class_Window_property_keep_title_visible>`

classref-property-setget

- `void (No return value.)` **set_keep_title_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_keep_title_visible**()

If `true`, the **Window** width is expanded to keep the title bar text fully visible.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **max_size** = `Vector2i(0, 0)` `🔗<class_Window_property_max_size>`

classref-property-setget

- `void (No return value.)` **set_max_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_max_size**()

If non-zero, the **Window** can't be resized to be bigger than this size.

**Note:** This property will be ignored if the value is lower than `min_size<class_Window_property_min_size>`.

classref-item-separator

classref-property

`bool<class_bool>` **maximize_disabled** = `false` `🔗<class_Window_property_maximize_disabled>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window**'s maximize button is disabled.

**Note:** If both minimize and maximize buttons are disabled, buttons are fully hidden, and only close button is visible.

**Note:** This property is implemented only on macOS and Windows.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **min_size** = `Vector2i(0, 0)` `🔗<class_Window_property_min_size>`

classref-property-setget

- `void (No return value.)` **set_min_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_min_size**()

If non-zero, the **Window** can't be resized to be smaller than this size.

**Note:** This property will be ignored in favor of `get_contents_minimum_size()<class_Window_method_get_contents_minimum_size>` if `wrap_controls<class_Window_property_wrap_controls>` is enabled and if its size is bigger.

classref-item-separator

classref-property

`bool<class_bool>` **minimize_disabled** = `false` `🔗<class_Window_property_minimize_disabled>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window**'s minimize button is disabled.

**Note:** If both minimize and maximize buttons are disabled, buttons are fully hidden, and only close button is visible.

**Note:** This property is implemented only on macOS and Windows.

classref-item-separator

classref-property

`Mode<enum_Window_Mode>` **mode** = `0` `🔗<class_Window_property_mode>`

classref-property-setget

- `void (No return value.)` **set_mode**(value: `Mode<enum_Window_Mode>`)
- `Mode<enum_Window_Mode>` **get_mode**()

Set's the window's current mode.

**Note:** Fullscreen mode is not exclusive full screen on Windows and Linux.

**Note:** This method only works with native windows, i.e. the main window and **Window**-derived nodes when `Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>` is disabled in the main viewport.

classref-item-separator

classref-property

`bool<class_bool>` **mouse_passthrough** = `false` `🔗<class_Window_property_mouse_passthrough>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, all mouse events will be passed to the underlying window of the same application. See also `mouse_passthrough_polygon<class_Window_property_mouse_passthrough_polygon>`.

**Note:** This property is implemented on Linux (X11), macOS and Windows.

**Note:** This property only works with native windows.

classref-item-separator

classref-property

`PackedVector2Array<class_PackedVector2Array>` **mouse_passthrough_polygon** = `PackedVector2Array()` `🔗<class_Window_property_mouse_passthrough_polygon>`

classref-property-setget

- `void (No return value.)` **set_mouse_passthrough_polygon**(value: `PackedVector2Array<class_PackedVector2Array>`)
- `PackedVector2Array<class_PackedVector2Array>` **get_mouse_passthrough_polygon**()

Sets a polygonal region of the window which accepts mouse events. Mouse events outside the region will be passed through.

Passing an empty array will disable passthrough support (all mouse events will be intercepted by the window, which is the default behavior).

gdscript

\# Set region, using Path2D node. \$Window.mouse_passthrough_polygon = \$Path2D.curve.get_baked_points()

\# Set region, using Polygon2D node. \$Window.mouse_passthrough_polygon = \$Polygon2D.polygon

\# Reset region to default. \$Window.mouse_passthrough_polygon = \[\]

csharp

// Set region, using Path2D node. GetNode\<Window\>("Window").MousePassthroughPolygon = GetNode\<Path2D\>("Path2D").Curve.GetBakedPoints();

// Set region, using Polygon2D node. GetNode\<Window\>("Window").MousePassthroughPolygon = GetNode\<Polygon2D\>("Polygon2D").Polygon;

// Reset region to default. GetNode\<Window\>("Window").MousePassthroughPolygon = \[\];

**Note:** This property is ignored if `mouse_passthrough<class_Window_property_mouse_passthrough>` is set to `true`.

**Note:** On Windows, the portion of a window that lies outside the region is not drawn, while on Linux (X11) and macOS it is.

**Note:** This property is implemented on Linux (X11), macOS and Windows.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedVector2Array<class_PackedVector2Array>` for more details.

classref-item-separator

classref-property

`Rect2i<class_Rect2i>` **nonclient_area** = `Rect2i(0, 0, 0, 0)` `🔗<class_Window_property_nonclient_area>`

classref-property-setget

- `void (No return value.)` **set_nonclient_area**(value: `Rect2i<class_Rect2i>`)
- `Rect2i<class_Rect2i>` **get_nonclient_area**()

If set, defines the window's custom decoration area which will receive mouse input, even if normal input to the window is blocked (such as when it has an exclusive child opened). See also `nonclient_window_input<class_Window_signal_nonclient_window_input>`.

classref-item-separator

classref-property

`bool<class_bool>` **popup_window** = `false` `🔗<class_Window_property_popup_window>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window** will be considered a popup. Popups are sub-windows that don't show as separate windows in system's window manager's window list and will send close request when anything is clicked outside of them (unless `exclusive<class_Window_property_exclusive>` is enabled).

classref-item-separator

classref-property

`bool<class_bool>` **popup_wm_hint** = `false` `🔗<class_Window_property_popup_wm_hint>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window** will signal to the window manager that it is supposed to be an implementation-defined "popup" (usually a floating, borderless, untileable and immovable child window).

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **position** = `Vector2i(0, 0)` `🔗<class_Window_property_position>`

classref-property-setget

- `void (No return value.)` **set_position**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_position**()

The window's position in pixels.

If `ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>` is `false`, the position is in absolute screen coordinates. This typically applies to editor plugins. If the setting is `true`, the window's position is in the coordinates of its parent `Viewport<class_Viewport>`.

**Note:** This property only works if `initial_position<class_Window_property_initial_position>` is set to `WINDOW_INITIAL_POSITION_ABSOLUTE<class_Window_constant_WINDOW_INITIAL_POSITION_ABSOLUTE>`.

classref-item-separator

classref-property

`bool<class_bool>` **sharp_corners** = `false` `🔗<class_Window_property_sharp_corners>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window** will override the OS window style to display sharp corners.

**Note:** This property is implemented only on Windows (11).

**Note:** This property only works with native windows.

classref-item-separator

classref-property

`Vector2i<class_Vector2i>` **size** = `Vector2i(100, 100)` `🔗<class_Window_property_size>`

classref-property-setget

- `void (No return value.)` **set_size**(value: `Vector2i<class_Vector2i>`)
- `Vector2i<class_Vector2i>` **get_size**()

The window's size in pixels. See also `content_scale_size<class_Window_property_content_scale_size>`, which doesn't set the window's physical size but affects how scaling works relative to the current `content_scale_mode<class_Window_property_content_scale_mode>`.

classref-item-separator

classref-property

`Theme<class_Theme>` **theme** `🔗<class_Window_property_theme>`

classref-property-setget

- `void (No return value.)` **set_theme**(value: `Theme<class_Theme>`)
- `Theme<class_Theme>` **get_theme**()

The `Theme<class_Theme>` resource this node and all its `Control<class_Control>` and **Window** children use. If a child node has its own `Theme<class_Theme>` resource set, theme items are merged with child's definitions having higher priority.

**Note:** **Window** styles will have no effect unless the window is embedded.

classref-item-separator

classref-property

`StringName<class_StringName>` **theme_type_variation** = `&""` `🔗<class_Window_property_theme_type_variation>`

classref-property-setget

- `void (No return value.)` **set_theme_type_variation**(value: `StringName<class_StringName>`)
- `StringName<class_StringName>` **get_theme_type_variation**()

The name of a theme type variation used by this **Window** to look up its own theme items. See `Control.theme_type_variation<class_Control_property_theme_type_variation>` for more details.

classref-item-separator

classref-property

`String<class_String>` **title** = `""` `🔗<class_Window_property_title>`

classref-property-setget

- `void (No return value.)` **set_title**(value: `String<class_String>`)
- `String<class_String>` **get_title**()

The window's title. If the **Window** is native, title styles set in `Theme<class_Theme>` will have no effect.

classref-item-separator

classref-property

`bool<class_bool>` **transient** = `false` `🔗<class_Window_property_transient>`

classref-property-setget

- `void (No return value.)` **set_transient**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_transient**()

If `true`, the **Window** is transient, i.e. it's considered a child of another **Window**. The transient window will be destroyed with its transient parent and will return focus to their parent when closed. The transient window is displayed on top of a non-exclusive full-screen parent window. Transient windows can't enter full-screen mode.

Note that behavior might be different depending on the platform.

classref-item-separator

classref-property

`bool<class_bool>` **transient_to_focused** = `false` `🔗<class_Window_property_transient_to_focused>`

classref-property-setget

- `void (No return value.)` **set_transient_to_focused**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_transient_to_focused**()

If `true`, and the **Window** is `transient<class_Window_property_transient>`, this window will (at the time of becoming visible) become transient to the currently focused window instead of the immediate parent window in the hierarchy. Note that the transient parent is assigned at the time this window becomes visible, so changing it afterwards has no effect until re-shown.

classref-item-separator

classref-property

`bool<class_bool>` **transparent** = `false` `🔗<class_Window_property_transparent>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window**'s background can be transparent. This is best used with embedded windows.

**Note:** Transparency support is implemented on Linux, macOS and Windows, but availability might vary depending on GPU driver, display manager, and compositor capabilities.

**Note:** This property has no effect if `ProjectSettings.display/window/per_pixel_transparency/allowed<class_ProjectSettings_property_display/window/per_pixel_transparency/allowed>` is set to `false`.

classref-item-separator

classref-property

`bool<class_bool>` **unfocusable** = `false` `🔗<class_Window_property_unfocusable>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the **Window** can't be focused nor interacted with. It can still be visible.

classref-item-separator

classref-property

`bool<class_bool>` **unresizable** = `false` `🔗<class_Window_property_unresizable>`

classref-property-setget

- `void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`)
- `bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

If `true`, the window can't be resized.

classref-item-separator

classref-property

`bool<class_bool>` **visible** = `true` `🔗<class_Window_property_visible>`

classref-property-setget

- `void (No return value.)` **set_visible**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_visible**()

If `true`, the window is visible.

classref-item-separator

classref-property

`bool<class_bool>` **wrap_controls** = `false` `🔗<class_Window_property_wrap_controls>`

classref-property-setget

- `void (No return value.)` **set_wrap_controls**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_wrapping_controls**()

If `true`, the window's size will automatically update when a child node is added or removed, ignoring `min_size<class_Window_property_min_size>` if the new size is bigger.

If `false`, you need to call `child_controls_changed()<class_Window_method_child_controls_changed>` manually.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Vector2<class_Vector2>` **\_get_contents_minimum_size**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_private_method__get_contents_minimum_size>`

Virtual method to be implemented by the user. Overrides the value returned by `get_contents_minimum_size()<class_Window_method_get_contents_minimum_size>`.

classref-item-separator

classref-method

`void (No return value.)` **add_theme_color_override**(name: `StringName<class_StringName>`, color: `Color<class_Color>`) `🔗<class_Window_method_add_theme_color_override>`

Creates a local override for a theme `Color<class_Color>` with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with `remove_theme_color_override()<class_Window_method_remove_theme_color_override>`.

See also `get_theme_color()<class_Window_method_get_theme_color>` and `Control.add_theme_color_override()<class_Control_method_add_theme_color_override>` for more details.

classref-item-separator

classref-method

`void (No return value.)` **add_theme_constant_override**(name: `StringName<class_StringName>`, constant: `int<class_int>`) `🔗<class_Window_method_add_theme_constant_override>`

Creates a local override for a theme constant with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with `remove_theme_constant_override()<class_Window_method_remove_theme_constant_override>`.

See also `get_theme_constant()<class_Window_method_get_theme_constant>`.

classref-item-separator

classref-method

`void (No return value.)` **add_theme_font_override**(name: `StringName<class_StringName>`, font: `Font<class_Font>`) `🔗<class_Window_method_add_theme_font_override>`

Creates a local override for a theme `Font<class_Font>` with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with `remove_theme_font_override()<class_Window_method_remove_theme_font_override>`.

See also `get_theme_font()<class_Window_method_get_theme_font>`.

classref-item-separator

classref-method

`void (No return value.)` **add_theme_font_size_override**(name: `StringName<class_StringName>`, font_size: `int<class_int>`) `🔗<class_Window_method_add_theme_font_size_override>`

Creates a local override for a theme font size with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with `remove_theme_font_size_override()<class_Window_method_remove_theme_font_size_override>`.

See also `get_theme_font_size()<class_Window_method_get_theme_font_size>`.

classref-item-separator

classref-method

`void (No return value.)` **add_theme_icon_override**(name: `StringName<class_StringName>`, texture: `Texture2D<class_Texture2D>`) `🔗<class_Window_method_add_theme_icon_override>`

Creates a local override for a theme icon with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with `remove_theme_icon_override()<class_Window_method_remove_theme_icon_override>`.

See also `get_theme_icon()<class_Window_method_get_theme_icon>`.

classref-item-separator

classref-method

`void (No return value.)` **add_theme_stylebox_override**(name: `StringName<class_StringName>`, stylebox: `StyleBox<class_StyleBox>`) `🔗<class_Window_method_add_theme_stylebox_override>`

Creates a local override for a theme `StyleBox<class_StyleBox>` with the specified `name`. Local overrides always take precedence when fetching theme items for the control. An override can be removed with `remove_theme_stylebox_override()<class_Window_method_remove_theme_stylebox_override>`.

See also `get_theme_stylebox()<class_Window_method_get_theme_stylebox>` and `Control.add_theme_stylebox_override()<class_Control_method_add_theme_stylebox_override>` for more details.

classref-item-separator

classref-method

`void (No return value.)` **begin_bulk_theme_override**() `🔗<class_Window_method_begin_bulk_theme_override>`

Prevents `*_theme_*_override` methods from emitting `NOTIFICATION_THEME_CHANGED<class_Window_constant_NOTIFICATION_THEME_CHANGED>` until `end_bulk_theme_override()<class_Window_method_end_bulk_theme_override>` is called.

classref-item-separator

classref-method

`bool<class_bool>` **can_draw**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_can_draw>`

Returns whether the window is being drawn to the screen.

classref-item-separator

classref-method

`void (No return value.)` **child_controls_changed**() `🔗<class_Window_method_child_controls_changed>`

Requests an update of the **Window** size to fit underlying `Control<class_Control>` nodes.

classref-item-separator

classref-method

`void (No return value.)` **end_bulk_theme_override**() `🔗<class_Window_method_end_bulk_theme_override>`

Ends a bulk theme override update. See `begin_bulk_theme_override()<class_Window_method_begin_bulk_theme_override>`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_contents_minimum_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_contents_minimum_size>`

Returns the combined minimum size from the child `Control<class_Control>` nodes of the window. Use `child_controls_changed()<class_Window_method_child_controls_changed>` to update it when child nodes have changed.

The value returned by this method can be overridden with `_get_contents_minimum_size()<class_Window_private_method__get_contents_minimum_size>`.

classref-item-separator

classref-method

`bool<class_bool>` **get_flag**(flag: `Flags<enum_Window_Flags>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_flag>`

Returns `true` if the `flag` is set.

classref-item-separator

classref-method

`Window<class_Window>` **get_focused_window**() `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Window_method_get_focused_window>`

Returns the focused window.

classref-item-separator

classref-method

`LayoutDirection<enum_Window_LayoutDirection>` **get_layout_direction**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_layout_direction>`

Returns layout direction and text writing direction.

classref-item-separator

classref-method

`float<class_float>` **get_output_max_linear_value**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_output_max_linear_value>`

Returns the maximum value for linear color components that can be displayed in this window, regardless of SDR or HDR output. Returns `1.0` if HDR is not enabled or not supported. The `output_max_linear_value_changed<class_Window_signal_output_max_linear_value_changed>` signal will be emitted whenever this value changes.

This value is used by tonemapping and other `Environment<class_Environment>` effects to ensure that bright colors are presented in the range that can be displayed by this window. When using this maximum linear value in your project, it should only be used to present colors directly to the screen without tonemapping and without influencing lighting, post-processing effects, or surrounding color. The following is an example that produces the brightest purple color that the screen can produce:

gdscript

func process(delta):
\# output_max_linear_value may change often, so do this every frame. var max_linear_value = get_window().get_output_max_linear_value() \# Replace this with your color: var original_color = Color.PURPLE \# Normalize to max_linear_value to produce the brightest color possible, \# regardless of SDR or HDR output: var bright_color = normalize_color(original_color, max_linear_value)

func normalize_color(srgb_color, max_linear_value = 1.0):
\# Color must be linear-encoded to use math operations. var linear_color = srgb_color.srgb_to_linear() var max_rgb_value = maxf(linear_color.r, maxf(linear_color.g, linear_color.b)) var brightness_scale = max_linear_value / max_rgb_value linear_color \*= brightness_scale \# Undo changes to the alpha channel, which should not be modified. linear_color.a = srgb_color.a \# Convert back to nonlinear sRGB encoding, which is required for Color in \# Godot unless stated otherwise. return linear_color.linear_to_srgb()

**Note:** You will need to convert sRGB colors to linear before multiplying by this value to get correct results.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_position_with_decorations**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_position_with_decorations>`

Returns the window's position including its border.

**Note:** If `visible<class_Window_property_visible>` is `false`, this method returns the same value as `position<class_Window_property_position>`.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_size_with_decorations**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_size_with_decorations>`

Returns the window's size including its border.

**Note:** If `visible<class_Window_property_visible>` is `false`, this method returns the same value as `size<class_Window_property_size>`.

classref-item-separator

classref-method

`Color<class_Color>` **get_theme_color**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_color>`

Returns a `Color<class_Color>` from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a color item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for more details.

classref-item-separator

classref-method

`int<class_int>` **get_theme_constant**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_constant>`

Returns a constant from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a constant item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for more details.

classref-item-separator

classref-method

`float<class_float>` **get_theme_default_base_scale**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_default_base_scale>`

Returns the default base scale value from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a valid `Theme.default_base_scale<class_Theme_property_default_base_scale>` value.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`Font<class_Font>` **get_theme_default_font**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_default_font>`

Returns the default font from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a valid `Theme.default_font<class_Theme_property_default_font>` value.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`int<class_int>` **get_theme_default_font_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_default_font_size>`

Returns the default font size value from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a valid `Theme.default_font_size<class_Theme_property_default_font_size>` value.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`Font<class_Font>` **get_theme_font**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_font>`

Returns a `Font<class_Font>` from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a font item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`int<class_int>` **get_theme_font_size**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_font_size>`

Returns a font size from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a font size item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`Texture2D<class_Texture2D>` **get_theme_icon**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_icon>`

Returns an icon from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has an icon item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`StyleBox<class_StyleBox>` **get_theme_stylebox**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_theme_stylebox>`

Returns a `StyleBox<class_StyleBox>` from the first matching `Theme<class_Theme>` in the tree if that `Theme<class_Theme>` has a stylebox item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`int<class_int>` **get_window_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_get_window_id>`

Returns the ID of the window.

classref-item-separator

classref-method

`void (No return value.)` **grab_focus**() `🔗<class_Window_method_grab_focus>`

Causes the window to grab focus, allowing it to receive user input.

classref-item-separator

classref-method

`bool<class_bool>` **has_focus**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_focus>`

Returns `true` if the window is focused.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_color**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_color>`

Returns `true` if there is a matching `Theme<class_Theme>` in the tree that has a color item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_color_override**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_color_override>`

Returns `true` if there is a local override for a theme `Color<class_Color>` with the specified `name` in this `Control<class_Control>` node.

See `add_theme_color_override()<class_Window_method_add_theme_color_override>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_constant**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_constant>`

Returns `true` if there is a matching `Theme<class_Theme>` in the tree that has a constant item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_constant_override**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_constant_override>`

Returns `true` if there is a local override for a theme constant with the specified `name` in this `Control<class_Control>` node.

See `add_theme_constant_override()<class_Window_method_add_theme_constant_override>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_font**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_font>`

Returns `true` if there is a matching `Theme<class_Theme>` in the tree that has a font item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_font_override**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_font_override>`

Returns `true` if there is a local override for a theme `Font<class_Font>` with the specified `name` in this `Control<class_Control>` node.

See `add_theme_font_override()<class_Window_method_add_theme_font_override>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_font_size**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_font_size>`

Returns `true` if there is a matching `Theme<class_Theme>` in the tree that has a font size item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_font_size_override**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_font_size_override>`

Returns `true` if there is a local override for a theme font size with the specified `name` in this `Control<class_Control>` node.

See `add_theme_font_size_override()<class_Window_method_add_theme_font_size_override>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_icon**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_icon>`

Returns `true` if there is a matching `Theme<class_Theme>` in the tree that has an icon item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_icon_override**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_icon_override>`

Returns `true` if there is a local override for a theme icon with the specified `name` in this `Control<class_Control>` node.

See `add_theme_icon_override()<class_Window_method_add_theme_icon_override>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_stylebox**(name: `StringName<class_StringName>`, theme_type: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_stylebox>`

Returns `true` if there is a matching `Theme<class_Theme>` in the tree that has a stylebox item with the specified `name` and `theme_type`.

See `Control.get_theme_color()<class_Control_method_get_theme_color>` for details.

classref-item-separator

classref-method

`bool<class_bool>` **has_theme_stylebox_override**(name: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_has_theme_stylebox_override>`

Returns `true` if there is a local override for a theme `StyleBox<class_StyleBox>` with the specified `name` in this `Control<class_Control>` node.

See `add_theme_stylebox_override()<class_Window_method_add_theme_stylebox_override>`.

classref-item-separator

classref-method

`void (No return value.)` **hide**() `🔗<class_Window_method_hide>`

Hides the window. This is not the same as minimized state. Hidden window can't be interacted with and needs to be made visible with `show()<class_Window_method_show>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_embedded**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_is_embedded>`

Returns `true` if the window is currently embedded in another window.

classref-item-separator

classref-method

`bool<class_bool>` **is_layout_rtl**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_is_layout_rtl>`

Returns `true` if the layout is right-to-left.

classref-item-separator

classref-method

`bool<class_bool>` **is_maximize_allowed**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_is_maximize_allowed>`

Returns `true` if the window can be maximized (the maximize button is enabled).

classref-item-separator

classref-method

`bool<class_bool>` **is_using_font_oversampling**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Window_method_is_using_font_oversampling>`

Returns `true` if font oversampling is enabled. See `set_use_font_oversampling()<class_Window_method_set_use_font_oversampling>`.

classref-item-separator

classref-method

`void (No return value.)` **move_to_center**() `🔗<class_Window_method_move_to_center>`

Centers the window in the current screen. If the window is embedded, it is centered in the embedder `Viewport<class_Viewport>` instead.

classref-item-separator

classref-method

`void (No return value.)` **move_to_foreground**() `🔗<class_Window_method_move_to_foreground>`

**Deprecated:** Use `grab_focus()<class_Window_method_grab_focus>` instead.

Causes the window to grab focus, allowing it to receive user input.

classref-item-separator

classref-method

`void (No return value.)` **popup**(rect: `Rect2i<class_Rect2i>` = Rect2i(0, 0, 0, 0)) `🔗<class_Window_method_popup>`

Shows the **Window** and makes it transient (see `transient<class_Window_property_transient>`). If `rect` is provided, it will be set as the **Window**'s size. Fails if called on the main window.

If `ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>` is `true` (single-window mode), `rect`'s coordinates are global and relative to the main window's top-left corner (excluding window decorations). If `rect`'s position coordinates are negative, the window will be located outside the main window and may not be visible as a result.

If `ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>` is `false` (multi-window mode), `rect`'s coordinates are global and relative to the top-left corner of the leftmost screen. If `rect`'s position coordinates are negative, the window will be placed at the top-left corner of the screen.

**Note:** `rect` must be in global coordinates if specified.

classref-item-separator

classref-method

`void (No return value.)` **popup_centered**(minsize: `Vector2i<class_Vector2i>` = Vector2i(0, 0)) `🔗<class_Window_method_popup_centered>`

Popups the **Window** at the center of the current screen, with optionally given minimum size. If the **Window** is embedded, it will be centered in the parent `Viewport<class_Viewport>` instead.

**Note:** Calling it with the default value of `minsize` is equivalent to calling it with `size<class_Window_property_size>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_centered_clamped**(minsize: `Vector2i<class_Vector2i>` = Vector2i(0, 0), fallback_ratio: `float<class_float>` = 0.75) `🔗<class_Window_method_popup_centered_clamped>`

Popups the **Window** centered inside its parent **Window**. `fallback_ratio` determines the maximum size of the **Window**, in relation to its parent.

**Note:** Calling it with the default value of `minsize` is equivalent to calling it with `size<class_Window_property_size>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_centered_ratio**(ratio: `float<class_float>` = 0.8) `🔗<class_Window_method_popup_centered_ratio>`

If **Window** is embedded, popups the **Window** centered inside its embedder and sets its size as a `ratio` of embedder's size.

If **Window** is a native window, popups the **Window** centered inside the screen of its parent **Window** and sets its size as a `ratio` of the screen size.

classref-item-separator

classref-method

`void (No return value.)` **popup_exclusive**(from_node: `Node<class_Node>`, rect: `Rect2i<class_Rect2i>` = Rect2i(0, 0, 0, 0)) `🔗<class_Window_method_popup_exclusive>`

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls `popup()<class_Window_method_popup>` on it. The dialog must have no current parent, otherwise the method fails.

See also `set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>` and `Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_exclusive_centered**(from_node: `Node<class_Node>`, minsize: `Vector2i<class_Vector2i>` = Vector2i(0, 0)) `🔗<class_Window_method_popup_exclusive_centered>`

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls `popup_centered()<class_Window_method_popup_centered>` on it. The dialog must have no current parent, otherwise the method fails.

See also `set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>` and `Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_exclusive_centered_clamped**(from_node: `Node<class_Node>`, minsize: `Vector2i<class_Vector2i>` = Vector2i(0, 0), fallback_ratio: `float<class_float>` = 0.75) `🔗<class_Window_method_popup_exclusive_centered_clamped>`

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls `popup_centered_clamped()<class_Window_method_popup_centered_clamped>` on it. The dialog must have no current parent, otherwise the method fails.

See also `set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>` and `Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_exclusive_centered_ratio**(from_node: `Node<class_Node>`, ratio: `float<class_float>` = 0.8) `🔗<class_Window_method_popup_exclusive_centered_ratio>`

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls `popup_centered_ratio()<class_Window_method_popup_centered_ratio>` on it. The dialog must have no current parent, otherwise the method fails.

See also `set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>` and `Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_exclusive_on_parent**(from_node: `Node<class_Node>`, parent_rect: `Rect2i<class_Rect2i>`) `🔗<class_Window_method_popup_exclusive_on_parent>`

Attempts to parent this dialog to the last exclusive window relative to `from_node`, and then calls `popup_on_parent()<class_Window_method_popup_on_parent>` on it. The dialog must have no current parent, otherwise the method fails.

See also `set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>` and `Node.get_last_exclusive_window()<class_Node_method_get_last_exclusive_window>`.

classref-item-separator

classref-method

`void (No return value.)` **popup_on_parent**(parent_rect: `Rect2i<class_Rect2i>`) `🔗<class_Window_method_popup_on_parent>`

Popups the **Window** with a position shifted by parent **Window**'s position. If the **Window** is embedded, has the same effect as `popup()<class_Window_method_popup>`.

classref-item-separator

classref-method

`void (No return value.)` **remove_theme_color_override**(name: `StringName<class_StringName>`) `🔗<class_Window_method_remove_theme_color_override>`

Removes a local override for a theme `Color<class_Color>` with the specified `name` previously added by `add_theme_color_override()<class_Window_method_add_theme_color_override>` or via the Inspector dock.

classref-item-separator

classref-method

`void (No return value.)` **remove_theme_constant_override**(name: `StringName<class_StringName>`) `🔗<class_Window_method_remove_theme_constant_override>`

Removes a local override for a theme constant with the specified `name` previously added by `add_theme_constant_override()<class_Window_method_add_theme_constant_override>` or via the Inspector dock.

classref-item-separator

classref-method

`void (No return value.)` **remove_theme_font_override**(name: `StringName<class_StringName>`) `🔗<class_Window_method_remove_theme_font_override>`

Removes a local override for a theme `Font<class_Font>` with the specified `name` previously added by `add_theme_font_override()<class_Window_method_add_theme_font_override>` or via the Inspector dock.

classref-item-separator

classref-method

`void (No return value.)` **remove_theme_font_size_override**(name: `StringName<class_StringName>`) `🔗<class_Window_method_remove_theme_font_size_override>`

Removes a local override for a theme font size with the specified `name` previously added by `add_theme_font_size_override()<class_Window_method_add_theme_font_size_override>` or via the Inspector dock.

classref-item-separator

classref-method

`void (No return value.)` **remove_theme_icon_override**(name: `StringName<class_StringName>`) `🔗<class_Window_method_remove_theme_icon_override>`

Removes a local override for a theme icon with the specified `name` previously added by `add_theme_icon_override()<class_Window_method_add_theme_icon_override>` or via the Inspector dock.

classref-item-separator

classref-method

`void (No return value.)` **remove_theme_stylebox_override**(name: `StringName<class_StringName>`) `🔗<class_Window_method_remove_theme_stylebox_override>`

Removes a local override for a theme `StyleBox<class_StyleBox>` with the specified `name` previously added by `add_theme_stylebox_override()<class_Window_method_add_theme_stylebox_override>` or via the Inspector dock.

classref-item-separator

classref-method

`void (No return value.)` **request_attention**() `🔗<class_Window_method_request_attention>`

Tells the OS that the **Window** needs an attention. This makes the window stand out in some way depending on the system, e.g. it might blink on the task bar.

classref-item-separator

classref-method

`void (No return value.)` **reset_size**() `🔗<class_Window_method_reset_size>`

Resets the size to the minimum size, which is the max of `min_size<class_Window_property_min_size>` and (if `wrap_controls<class_Window_property_wrap_controls>` is enabled) `get_contents_minimum_size()<class_Window_method_get_contents_minimum_size>`. This is equivalent to calling `set_size(Vector2i())` (or any size below the minimum).

classref-item-separator

classref-method

`void (No return value.)` **set_flag**(flag: `Flags<enum_Window_Flags>`, enabled: `bool<class_bool>`) `🔗<class_Window_method_set_flag>`

Sets a specified window flag.

classref-item-separator

classref-method

`void (No return value.)` **set_ime_active**(active: `bool<class_bool>`) `🔗<class_Window_method_set_ime_active>`

If `active` is `true`, enables system's native IME (Input Method Editor).

classref-item-separator

classref-method

`void (No return value.)` **set_ime_position**(position: `Vector2i<class_Vector2i>`) `🔗<class_Window_method_set_ime_position>`

Moves IME to the given position.

classref-item-separator

classref-method

`void (No return value.)` **set_layout_direction**(direction: `LayoutDirection<enum_Window_LayoutDirection>`) `🔗<class_Window_method_set_layout_direction>`

Sets layout direction and text writing direction. Right-to-left layouts are necessary for certain languages (e.g. Arabic and Hebrew).

classref-item-separator

classref-method

`void (No return value.)` **set_taskbar_progress_state**(state: `ProgressState<enum_DisplayServer_ProgressState>`) `🔗<class_Window_method_set_taskbar_progress_state>`

Sets the type and state of the progress bar on the taskbar/dock icon of the **Window**. See `ProgressState<enum_DisplayServer_ProgressState>` for possible values and how each mode behaves.

**Note:** This method is implemented only on Windows and macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_taskbar_progress_value**(value: `float<class_float>`) `🔗<class_Window_method_set_taskbar_progress_value>`

Creates a progress bar on the taskbar/dock icon of the **Window** if it does not exist, sets the progress of the icon.

`value` acts as a relative percentage value, ranges from `0.0` (lowest) to `1.0` (highest).

**Note:** This method is implemented only on Windows and macOS.

classref-item-separator

classref-method

`void (No return value.)` **set_unparent_when_invisible**(unparent: `bool<class_bool>`) `🔗<class_Window_method_set_unparent_when_invisible>`

If `unparent` is `true`, the window is automatically unparented when going invisible.

**Note:** Make sure to keep a reference to the node, otherwise it will be orphaned. You also need to manually call `Node.queue_free()<class_Node_method_queue_free>` to free the window if it's not parented.

classref-item-separator

classref-method

`void (No return value.)` **set_use_font_oversampling**(enable: `bool<class_bool>`) `🔗<class_Window_method_set_use_font_oversampling>`

Enables font oversampling. This makes fonts look better when they are scaled up.

classref-item-separator

classref-method

`void (No return value.)` **show**() `🔗<class_Window_method_show>`

Makes the **Window** appear. This enables interactions with the **Window** and doesn't change any of its property other than visibility (unlike e.g. `popup()<class_Window_method_popup>`).

classref-item-separator

classref-method

`void (No return value.)` **start_drag**() `🔗<class_Window_method_start_drag>`

Starts an interactive drag operation on the window, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's title bar. Using this method allows the window to participate in space switching, tiling, and other system features.

classref-item-separator

classref-method

`void (No return value.)` **start_resize**(edge: `WindowResizeEdge<enum_DisplayServer_WindowResizeEdge>`) `🔗<class_Window_method_start_resize>`

Starts an interactive resize operation on the window, using the current mouse position. Call this method when handling a mouse button being pressed to simulate a pressed event on the window's edge.

classref-section-separator

classref-descriptions-group

## Theme Property Descriptions

classref-themeproperty

`Color<class_Color>` **title_color** = `Color(0.875, 0.875, 0.875, 1)` `🔗<class_Window_theme_color_title_color>`

The color of the title's text.

classref-item-separator

classref-themeproperty

`Color<class_Color>` **title_outline_modulate** = `Color(0, 0, 0, 1)` `🔗<class_Window_theme_color_title_outline_modulate>`

The color of the title's text outline.

classref-item-separator

classref-themeproperty

`int<class_int>` **close_h_offset** = `18` `🔗<class_Window_theme_constant_close_h_offset>`

Horizontal position offset of the close button, relative to the end of the title bar, towards the beginning of the title bar.

classref-item-separator

classref-themeproperty

`int<class_int>` **close_v_offset** = `24` `🔗<class_Window_theme_constant_close_v_offset>`

Vertical position offset of the close button, relative to the bottom of the title bar, towards the top of the title bar.

classref-item-separator

classref-themeproperty

`int<class_int>` **resize_margin** = `4` `🔗<class_Window_theme_constant_resize_margin>`

Defines the outside margin at which the window border can be grabbed with mouse and resized.

classref-item-separator

classref-themeproperty

`int<class_int>` **title_height** = `36` `🔗<class_Window_theme_constant_title_height>`

Height of the title bar.

classref-item-separator

classref-themeproperty

`int<class_int>` **title_outline_size** = `0` `🔗<class_Window_theme_constant_title_outline_size>`

The size of the title outline.

classref-item-separator

classref-themeproperty

`Font<class_Font>` **title_font** `🔗<class_Window_theme_font_title_font>`

The font used to draw the title.

classref-item-separator

classref-themeproperty

`int<class_int>` **title_font_size** `🔗<class_Window_theme_font_size_title_font_size>`

The size of the title font.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **close** `🔗<class_Window_theme_icon_close>`

The icon for the close button.

classref-item-separator

classref-themeproperty

`Texture2D<class_Texture2D>` **close_pressed** `🔗<class_Window_theme_icon_close_pressed>`

The icon for the close button when it's being pressed.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **embedded_border** `🔗<class_Window_theme_style_embedded_border>`

The background style used when the **Window** is embedded. Note that this is drawn only under the window's content, excluding the title. For proper borders and title bar style, you can use `expand_margin_*` properties of `StyleBoxFlat<class_StyleBoxFlat>`.

**Note:** The content background will not be visible unless `transparent<class_Window_property_transparent>` is enabled.

classref-item-separator

classref-themeproperty

`StyleBox<class_StyleBox>` **embedded_unfocused_border** `🔗<class_Window_theme_style_embedded_unfocused_border>`

The background style used when the **Window** is embedded and unfocused.