github_url
hide

# @GlobalScope

Global scope constants and functions.

classref-introduction-group

## Description

A list of global scope enumerated constants and built-in functions. This is all that resides in the globals, constants regarding error codes, keycodes, property hints, etc.

Singletons are also documented here, since they can be accessed from anywhere.

For the entries that can only be accessed from scripts written in GDScript, see `@GDScript<class_@GDScript>`.

> [!NOTE]
> There are notable differences when using this API with C#. See `doc_c_sharp_differences` for more information.

classref-introduction-group

## Tutorials

- `Random number generation <../tutorials/math/random_number_generation>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Side**: `🔗<enum_@GlobalScope_Side>`

classref-enumeration-constant

`Side<enum_@GlobalScope_Side>` **SIDE_LEFT** = `0`

Left side, usually used for `Control<class_Control>` or `StyleBox<class_StyleBox>`-derived classes.

classref-enumeration-constant

`Side<enum_@GlobalScope_Side>` **SIDE_TOP** = `1`

Top side, usually used for `Control<class_Control>` or `StyleBox<class_StyleBox>`-derived classes.

classref-enumeration-constant

`Side<enum_@GlobalScope_Side>` **SIDE_RIGHT** = `2`

Right side, usually used for `Control<class_Control>` or `StyleBox<class_StyleBox>`-derived classes.

classref-enumeration-constant

`Side<enum_@GlobalScope_Side>` **SIDE_BOTTOM** = `3`

Bottom side, usually used for `Control<class_Control>` or `StyleBox<class_StyleBox>`-derived classes.

classref-item-separator

classref-enumeration

enum **Corner**: `🔗<enum_@GlobalScope_Corner>`

classref-enumeration-constant

`Corner<enum_@GlobalScope_Corner>` **CORNER_TOP_LEFT** = `0`

Top-left corner.

classref-enumeration-constant

`Corner<enum_@GlobalScope_Corner>` **CORNER_TOP_RIGHT** = `1`

Top-right corner.

classref-enumeration-constant

`Corner<enum_@GlobalScope_Corner>` **CORNER_BOTTOM_RIGHT** = `2`

Bottom-right corner.

classref-enumeration-constant

`Corner<enum_@GlobalScope_Corner>` **CORNER_BOTTOM_LEFT** = `3`

Bottom-left corner.

classref-item-separator

classref-enumeration

enum **Orientation**: `🔗<enum_@GlobalScope_Orientation>`

classref-enumeration-constant

`Orientation<enum_@GlobalScope_Orientation>` **VERTICAL** = `1`

General vertical alignment, usually used for `Separator<class_Separator>`, `ScrollBar<class_ScrollBar>`, `Slider<class_Slider>`, etc.

classref-enumeration-constant

`Orientation<enum_@GlobalScope_Orientation>` **HORIZONTAL** = `0`

General horizontal alignment, usually used for `Separator<class_Separator>`, `ScrollBar<class_ScrollBar>`, `Slider<class_Slider>`, etc.

classref-item-separator

classref-enumeration

enum **ClockDirection**: `🔗<enum_@GlobalScope_ClockDirection>`

classref-enumeration-constant

`ClockDirection<enum_@GlobalScope_ClockDirection>` **CLOCKWISE** = `0`

Clockwise rotation. Used by some methods (e.g. `Image.rotate_90()<class_Image_method_rotate_90>`).

classref-enumeration-constant

`ClockDirection<enum_@GlobalScope_ClockDirection>` **COUNTERCLOCKWISE** = `1`

Counter-clockwise rotation. Used by some methods (e.g. `Image.rotate_90()<class_Image_method_rotate_90>`).

classref-item-separator

classref-enumeration

enum **HorizontalAlignment**: `🔗<enum_@GlobalScope_HorizontalAlignment>`

classref-enumeration-constant

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **HORIZONTAL_ALIGNMENT_LEFT** = `0`

Horizontal left alignment, usually for text-derived classes.

classref-enumeration-constant

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **HORIZONTAL_ALIGNMENT_CENTER** = `1`

Horizontal center alignment, usually for text-derived classes.

classref-enumeration-constant

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **HORIZONTAL_ALIGNMENT_RIGHT** = `2`

Horizontal right alignment, usually for text-derived classes.

classref-enumeration-constant

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>` **HORIZONTAL_ALIGNMENT_FILL** = `3`

Expand row to fit width, usually for text-derived classes.

classref-item-separator

classref-enumeration

enum **VerticalAlignment**: `🔗<enum_@GlobalScope_VerticalAlignment>`

classref-enumeration-constant

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **VERTICAL_ALIGNMENT_TOP** = `0`

Vertical top alignment, usually for text-derived classes.

classref-enumeration-constant

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **VERTICAL_ALIGNMENT_CENTER** = `1`

Vertical center alignment, usually for text-derived classes.

classref-enumeration-constant

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **VERTICAL_ALIGNMENT_BOTTOM** = `2`

Vertical bottom alignment, usually for text-derived classes.

classref-enumeration-constant

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>` **VERTICAL_ALIGNMENT_FILL** = `3`

Expand rows to fit height, usually for text-derived classes.

classref-item-separator

classref-enumeration

enum **InlineAlignment**: `🔗<enum_@GlobalScope_InlineAlignment>`

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TOP_TO** = `0`

Aligns the top of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_CENTER_TO** = `1`

Aligns the center of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_BASELINE_TO** = `3`

Aligns the baseline (user defined) of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_BOTTOM_TO** = `2`

Aligns the bottom of the inline object (e.g. image, table) to the position of the text specified by `INLINE_ALIGNMENT_TO_*` constant.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TO_TOP** = `0`

Aligns the position of the inline object (e.g. image, table) specified by `INLINE_ALIGNMENT_*_TO` constant to the top of the text.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TO_CENTER** = `4`

Aligns the position of the inline object (e.g. image, table) specified by `INLINE_ALIGNMENT_*_TO` constant to the center of the text.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TO_BASELINE** = `8`

Aligns the position of the inline object (e.g. image, table) specified by `INLINE_ALIGNMENT_*_TO` constant to the baseline of the text.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TO_BOTTOM** = `12`

Aligns inline object (e.g. image, table) to the bottom of the text.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TOP** = `0`

Aligns top of the inline object (e.g. image, table) to the top of the text. Equivalent to `INLINE_ALIGNMENT_TOP_TO | INLINE_ALIGNMENT_TO_TOP`.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_CENTER** = `5`

Aligns center of the inline object (e.g. image, table) to the center of the text. Equivalent to `INLINE_ALIGNMENT_CENTER_TO | INLINE_ALIGNMENT_TO_CENTER`.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_BOTTOM** = `14`

Aligns bottom of the inline object (e.g. image, table) to the bottom of the text. Equivalent to `INLINE_ALIGNMENT_BOTTOM_TO | INLINE_ALIGNMENT_TO_BOTTOM`.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_IMAGE_MASK** = `3`

A bit mask for `INLINE_ALIGNMENT_*_TO` alignment constants.

classref-enumeration-constant

`InlineAlignment<enum_@GlobalScope_InlineAlignment>` **INLINE_ALIGNMENT_TEXT_MASK** = `12`

A bit mask for `INLINE_ALIGNMENT_TO_*` alignment constants.

classref-item-separator

classref-enumeration

enum **EulerOrder**: `🔗<enum_@GlobalScope_EulerOrder>`

classref-enumeration-constant

`EulerOrder<enum_@GlobalScope_EulerOrder>` **EULER_ORDER_XYZ** = `0`

Specifies that Euler angles should be in intrinsic XYZ order. When composing, the rotations happen around the local X, Y, and Z axes, in that order. When decomposing, the order is reversed, first Z, then Y, and X last.

classref-enumeration-constant

`EulerOrder<enum_@GlobalScope_EulerOrder>` **EULER_ORDER_XZY** = `1`

Specifies that Euler angles should be in intrinsic XZY order. When composing, the rotations happen around the local X, Z, and Y axes, in that order. When decomposing, the order is reversed, first Y, then Z, and X last.

classref-enumeration-constant

`EulerOrder<enum_@GlobalScope_EulerOrder>` **EULER_ORDER_YXZ** = `2`

Specifies that Euler angles should be in intrinsic YXZ order. When composing, the rotations happen around the local Y, X, and Z axes, in that order. When decomposing, the order is reversed, first Z, then X, and Y last.

classref-enumeration-constant

`EulerOrder<enum_@GlobalScope_EulerOrder>` **EULER_ORDER_YZX** = `3`

Specifies that Euler angles should be in intrinsic YZX order. When composing, the rotations happen around the local Y, Z, and X axes, in that order. When decomposing, the order is reversed, first X, then Z, and Y last.

classref-enumeration-constant

`EulerOrder<enum_@GlobalScope_EulerOrder>` **EULER_ORDER_ZXY** = `4`

Specifies that Euler angles should be in intrinsic ZXY order. When composing, the rotations happen around the local Z, X, and Y axes, in that order. When decomposing, the order is reversed, first Y, then X, and Z last.

classref-enumeration-constant

`EulerOrder<enum_@GlobalScope_EulerOrder>` **EULER_ORDER_ZYX** = `5`

Specifies that Euler angles should be in intrinsic ZYX order. When composing, the rotations happen around the local Z, Y, and X axes, in that order. When decomposing, the order is reversed, first X, then Y, and Z last.

classref-item-separator

classref-enumeration

enum **Key**: `🔗<enum_@GlobalScope_Key>`

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_NONE** = `0`

Enum value which doesn't correspond to any key. This is used to initialize `Key<enum_@GlobalScope_Key>` properties with a generic state.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SPECIAL** = `4194304`

Keycodes with this bit applied are non-printable.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_ESCAPE** = `4194305`

Escape key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_TAB** = `4194306`

Tab key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BACKTAB** = `4194307`

Shift + Tab key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BACKSPACE** = `4194308`

Backspace key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_ENTER** = `4194309`

Return key (on the main keyboard).

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_ENTER** = `4194310`

Enter key on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_INSERT** = `4194311`

Insert key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_DELETE** = `4194312`

Delete key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PAUSE** = `4194313`

Pause key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PRINT** = `4194314`

Print Screen key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SYSREQ** = `4194315`

System Request key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_CLEAR** = `4194316`

Clear key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_HOME** = `4194317`

Home key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_END** = `4194318`

End key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LEFT** = `4194319`

Left arrow key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_UP** = `4194320`

Up arrow key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_RIGHT** = `4194321`

Right arrow key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_DOWN** = `4194322`

Down arrow key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PAGEUP** = `4194323`

Page Up key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PAGEDOWN** = `4194324`

Page Down key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SHIFT** = `4194325`

Shift key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_CTRL** = `4194326`

Control key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_META** = `4194327`

Meta key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_ALT** = `4194328`

Alt key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_CAPSLOCK** = `4194329`

Caps Lock key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_NUMLOCK** = `4194330`

Num Lock key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SCROLLLOCK** = `4194331`

Scroll Lock key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F1** = `4194332`

F1 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F2** = `4194333`

F2 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F3** = `4194334`

F3 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F4** = `4194335`

F4 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F5** = `4194336`

F5 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F6** = `4194337`

F6 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F7** = `4194338`

F7 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F8** = `4194339`

F8 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F9** = `4194340`

F9 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F10** = `4194341`

F10 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F11** = `4194342`

F11 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F12** = `4194343`

F12 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F13** = `4194344`

F13 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F14** = `4194345`

F14 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F15** = `4194346`

F15 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F16** = `4194347`

F16 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F17** = `4194348`

F17 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F18** = `4194349`

F18 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F19** = `4194350`

F19 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F20** = `4194351`

F20 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F21** = `4194352`

F21 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F22** = `4194353`

F22 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F23** = `4194354`

F23 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F24** = `4194355`

F24 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F25** = `4194356`

F25 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F26** = `4194357`

F26 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F27** = `4194358`

F27 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F28** = `4194359`

F28 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F29** = `4194360`

F29 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F30** = `4194361`

F30 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F31** = `4194362`

F31 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F32** = `4194363`

F32 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F33** = `4194364`

F33 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F34** = `4194365`

F34 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F35** = `4194366`

F35 key. Only supported on macOS and Linux due to a Windows limitation.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_MULTIPLY** = `4194433`

Multiply (\*) key on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_DIVIDE** = `4194434`

Divide (/) key on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_SUBTRACT** = `4194435`

Subtract (-) key on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_PERIOD** = `4194436`

Period (.) key on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_ADD** = `4194437`

Add (+) key on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_0** = `4194438`

Number 0 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_1** = `4194439`

Number 1 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_2** = `4194440`

Number 2 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_3** = `4194441`

Number 3 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_4** = `4194442`

Number 4 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_5** = `4194443`

Number 5 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_6** = `4194444`

Number 6 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_7** = `4194445`

Number 7 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_8** = `4194446`

Number 8 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KP_9** = `4194447`

Number 9 on the numeric keypad.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MENU** = `4194370`

Context menu key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_HYPER** = `4194371`

Hyper key. (On Linux/X11 only).

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_HELP** = `4194373`

Help key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BACK** = `4194376`

Back key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_FORWARD** = `4194377`

Forward key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_STOP** = `4194378`

Media stop key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_REFRESH** = `4194379`

Refresh key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_VOLUMEDOWN** = `4194380`

Volume down key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_VOLUMEMUTE** = `4194381`

Mute volume key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_VOLUMEUP** = `4194382`

Volume up key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MEDIAPLAY** = `4194388`

Media play key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MEDIASTOP** = `4194389`

Media stop key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MEDIAPREVIOUS** = `4194390`

Previous song key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MEDIANEXT** = `4194391`

Next song key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MEDIARECORD** = `4194392`

Media record key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_HOMEPAGE** = `4194393`

Home page key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_FAVORITES** = `4194394`

Favorites key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SEARCH** = `4194395`

Search key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_STANDBY** = `4194396`

Standby key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_OPENURL** = `4194397`

Open URL / Launch Browser key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHMAIL** = `4194398`

Launch Mail key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHMEDIA** = `4194399`

Launch Media key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH0** = `4194400`

Launch Shortcut 0 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH1** = `4194401`

Launch Shortcut 1 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH2** = `4194402`

Launch Shortcut 2 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH3** = `4194403`

Launch Shortcut 3 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH4** = `4194404`

Launch Shortcut 4 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH5** = `4194405`

Launch Shortcut 5 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH6** = `4194406`

Launch Shortcut 6 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH7** = `4194407`

Launch Shortcut 7 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH8** = `4194408`

Launch Shortcut 8 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCH9** = `4194409`

Launch Shortcut 9 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHA** = `4194410`

Launch Shortcut A key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHB** = `4194411`

Launch Shortcut B key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHC** = `4194412`

Launch Shortcut C key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHD** = `4194413`

Launch Shortcut D key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHE** = `4194414`

Launch Shortcut E key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LAUNCHF** = `4194415`

Launch Shortcut F key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_GLOBE** = `4194416`

"Globe" key on Mac / iPad keyboard.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_KEYBOARD** = `4194417`

"On-screen keyboard" key on iPad keyboard.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_JIS_EISU** = `4194418`

英数 key on Mac keyboard.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_JIS_KANA** = `4194419`

かな key on Mac keyboard.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_UNKNOWN** = `8388607`

Unknown key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SPACE** = `32`

Space key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_EXCLAM** = `33`

Exclamation mark (`!`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_QUOTEDBL** = `34`

Double quotation mark (`"`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_NUMBERSIGN** = `35`

Number sign or *hash* (`#`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_DOLLAR** = `36`

Dollar sign (`$`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PERCENT** = `37`

Percent sign (`%`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_AMPERSAND** = `38`

Ampersand (`&`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_APOSTROPHE** = `39`

Apostrophe (`'`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PARENLEFT** = `40`

Left parenthesis (`(`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PARENRIGHT** = `41`

Right parenthesis (`)`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_ASTERISK** = `42`

Asterisk (`*`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PLUS** = `43`

Plus (`+`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_COMMA** = `44`

Comma (`,`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_MINUS** = `45`

Minus (`-`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_PERIOD** = `46`

Period (`.`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SLASH** = `47`

Slash (`/`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_0** = `48`

Number 0 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_1** = `49`

Number 1 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_2** = `50`

Number 2 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_3** = `51`

Number 3 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_4** = `52`

Number 4 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_5** = `53`

Number 5 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_6** = `54`

Number 6 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_7** = `55`

Number 7 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_8** = `56`

Number 8 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_9** = `57`

Number 9 key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_COLON** = `58`

Colon (`:`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SEMICOLON** = `59`

Semicolon (`;`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_LESS** = `60`

Less-than sign (`<`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_EQUAL** = `61`

Equal sign (`=`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_GREATER** = `62`

Greater-than sign (`>`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_QUESTION** = `63`

Question mark (`?`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_AT** = `64`

At sign (`@`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_A** = `65`

A key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_B** = `66`

B key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_C** = `67`

C key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_D** = `68`

D key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_E** = `69`

E key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_F** = `70`

F key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_G** = `71`

G key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_H** = `72`

H key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_I** = `73`

I key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_J** = `74`

J key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_K** = `75`

K key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_L** = `76`

L key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_M** = `77`

M key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_N** = `78`

N key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_O** = `79`

O key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_P** = `80`

P key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_Q** = `81`

Q key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_R** = `82`

R key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_S** = `83`

S key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_T** = `84`

T key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_U** = `85`

U key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_V** = `86`

V key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_W** = `87`

W key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_X** = `88`

X key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_Y** = `89`

Y key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_Z** = `90`

Z key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BRACKETLEFT** = `91`

Left bracket (`[lb]`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BACKSLASH** = `92`

Backslash (`\`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BRACKETRIGHT** = `93`

Right bracket (`[rb]`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_ASCIICIRCUM** = `94`

Caret (`^`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_UNDERSCORE** = `95`

Underscore (`_`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_QUOTELEFT** = `96`

Backtick (``\`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BRACELEFT** = `123`

Left brace (`{`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BAR** = `124`

Vertical bar or *pipe* (`|`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_BRACERIGHT** = `125`

Right brace (`}`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_ASCIITILDE** = `126`

Tilde (`~`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_YEN** = `165`

Yen symbol (`¥`) key.

classref-enumeration-constant

`Key<enum_@GlobalScope_Key>` **KEY_SECTION** = `167`

Section sign (`§`) key.

classref-item-separator

classref-enumeration

flags **KeyModifierMask**: `🔗<enum_@GlobalScope_KeyModifierMask>`

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_CODE_MASK** = `8388607`

Bit mask with all bits enabled except for modifier keys. Apply it to remove modifiers.

    var keycode = KEY_A | KEY_MASK_SHIFT
    keycode = keycode & KEY_CODE_MASK
    print(keycode) # KEY_A

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MODIFIER_MASK** = `2130706432`

Bit mask with all modifier bits enabled. Apply it to isolate modifiers.

    var keycode = KEY_A | KEY_MASK_SHIFT
    keycode = keycode & KEY_MODIFIER_MASK
    print(keycode) # KEY_MASK_SHIFT

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_CMD_OR_CTRL** = `16777216`

Automatically remapped to `KEY_META<class_@GlobalScope_constant_KEY_META>` on macOS and `KEY_CTRL<class_@GlobalScope_constant_KEY_CTRL>` on other platforms, this mask is never set in the actual events, and should be used for key mapping only.

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_SHIFT** = `33554432`

Shift key mask.

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_ALT** = `67108864`

Alt or Option (on macOS) key mask.

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_META** = `134217728`

Command (on macOS) or Meta/Windows key mask.

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_CTRL** = `268435456`

Control key mask.

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_KPAD** = `536870912`

Keypad key mask.

classref-enumeration-constant

`KeyModifierMask<enum_@GlobalScope_KeyModifierMask>` **KEY_MASK_GROUP_SWITCH** = `1073741824`

Group Switch key mask.

classref-item-separator

classref-enumeration

enum **KeyLocation**: `🔗<enum_@GlobalScope_KeyLocation>`

classref-enumeration-constant

`KeyLocation<enum_@GlobalScope_KeyLocation>` **KEY_LOCATION_UNSPECIFIED** = `0`

Used for keys which only appear once, or when a comparison doesn't need to differentiate the `LEFT` and `RIGHT` versions.

For example, when using `InputEvent.is_match()<class_InputEvent_method_is_match>`, an event which has `KEY_LOCATION_UNSPECIFIED<class_@GlobalScope_constant_KEY_LOCATION_UNSPECIFIED>` will match any `KeyLocation<enum_@GlobalScope_KeyLocation>` on the passed event.

classref-enumeration-constant

`KeyLocation<enum_@GlobalScope_KeyLocation>` **KEY_LOCATION_LEFT** = `1`

A key which is to the left of its twin.

classref-enumeration-constant

`KeyLocation<enum_@GlobalScope_KeyLocation>` **KEY_LOCATION_RIGHT** = `2`

A key which is to the right of its twin.

classref-item-separator

classref-enumeration

enum **MouseButton**: `🔗<enum_@GlobalScope_MouseButton>`

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_NONE** = `0`

Enum value which doesn't correspond to any mouse button. This is used to initialize `MouseButton<enum_@GlobalScope_MouseButton>` properties with a generic state.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_LEFT** = `1`

Primary mouse button, usually assigned to the left button.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_RIGHT** = `2`

Secondary mouse button, usually assigned to the right button.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_MIDDLE** = `3`

Middle mouse button.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_WHEEL_UP** = `4`

Mouse wheel scrolling up.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_WHEEL_DOWN** = `5`

Mouse wheel scrolling down.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_WHEEL_LEFT** = `6`

Mouse wheel left button (only present on some mice).

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_WHEEL_RIGHT** = `7`

Mouse wheel right button (only present on some mice).

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_XBUTTON1** = `8`

Extra mouse button 1. This is sometimes present, usually to the sides of the mouse.

classref-enumeration-constant

`MouseButton<enum_@GlobalScope_MouseButton>` **MOUSE_BUTTON_XBUTTON2** = `9`

Extra mouse button 2. This is sometimes present, usually to the sides of the mouse.

classref-item-separator

classref-enumeration

flags **MouseButtonMask**: `🔗<enum_@GlobalScope_MouseButtonMask>`

classref-enumeration-constant

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>` **MOUSE_BUTTON_MASK_LEFT** = `1`

Primary mouse button mask, usually for the left button.

classref-enumeration-constant

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>` **MOUSE_BUTTON_MASK_RIGHT** = `2`

Secondary mouse button mask, usually for the right button.

classref-enumeration-constant

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>` **MOUSE_BUTTON_MASK_MIDDLE** = `4`

Middle mouse button mask.

classref-enumeration-constant

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>` **MOUSE_BUTTON_MASK_MB_XBUTTON1** = `128`

Extra mouse button 1 mask.

classref-enumeration-constant

`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>` **MOUSE_BUTTON_MASK_MB_XBUTTON2** = `256`

Extra mouse button 2 mask.

classref-item-separator

classref-enumeration

enum **JoyButton**: `🔗<enum_@GlobalScope_JoyButton>`

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_INVALID** = `-1`

An invalid game controller button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_A** = `0`

Game controller SDL button A. Corresponds to the bottom action button: Sony Cross, Xbox A, Nintendo B.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_B** = `1`

Game controller SDL button B. Corresponds to the right action button: Sony Circle, Xbox B, Nintendo A.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_X** = `2`

Game controller SDL button X. Corresponds to the left action button: Sony Square, Xbox X, Nintendo Y.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_Y** = `3`

Game controller SDL button Y. Corresponds to the top action button: Sony Triangle, Xbox Y, Nintendo X.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_BACK** = `4`

Game controller SDL back button. Corresponds to the Sony Select, Xbox Back, Nintendo - button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_GUIDE** = `5`

Game controller SDL guide button. Corresponds to the Sony PS, Xbox Home button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_START** = `6`

Game controller SDL start button. Corresponds to the Sony Options, Xbox Menu, Nintendo + button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_LEFT_STICK** = `7`

Game controller SDL left stick button. Corresponds to the Sony L3, Xbox L/LS button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_RIGHT_STICK** = `8`

Game controller SDL right stick button. Corresponds to the Sony R3, Xbox R/RS button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_LEFT_SHOULDER** = `9`

Game controller SDL left shoulder button. Corresponds to the Sony L1, Xbox LB button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_RIGHT_SHOULDER** = `10`

Game controller SDL right shoulder button. Corresponds to the Sony R1, Xbox RB button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_DPAD_UP** = `11`

Game controller D-pad up button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_DPAD_DOWN** = `12`

Game controller D-pad down button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_DPAD_LEFT** = `13`

Game controller D-pad left button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_DPAD_RIGHT** = `14`

Game controller D-pad right button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MISC1** = `15`

Game controller SDL miscellaneous button. Corresponds to Xbox share button, PS5 microphone button, Nintendo Switch capture button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_PADDLE1** = `16`

Game controller SDL paddle 1 button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_PADDLE2** = `17`

Game controller SDL paddle 2 button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_PADDLE3** = `18`

Game controller SDL paddle 3 button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_PADDLE4** = `19`

Game controller SDL paddle 4 button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_TOUCHPAD** = `20`

Game controller SDL touchpad button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MISC2** = `21`

Game controller SDL miscellaneous button. Used by Nintendo Switch 2 Pro Controller and Horipad Steam controllers.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MISC3** = `22`

Game controller SDL miscellaneous button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MISC4** = `23`

Game controller SDL miscellaneous button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MISC5** = `24`

Game controller SDL miscellaneous button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MISC6** = `25`

Game controller SDL miscellaneous button.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_SDL_MAX** = `26`

The number of SDL game controller buttons.

classref-enumeration-constant

`JoyButton<enum_@GlobalScope_JoyButton>` **JOY_BUTTON_MAX** = `128`

The maximum number of game controller buttons supported by the engine. The actual limit may be lower on specific platforms:

- **Android:** Up to 36 buttons.
- **Linux:** Up to 80 buttons.
- **Windows** and **macOS:** Up to 128 buttons.

classref-item-separator

classref-enumeration

enum **JoyAxis**: `🔗<enum_@GlobalScope_JoyAxis>`

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_INVALID** = `-1`

An invalid game controller axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_LEFT_X** = `0`

Game controller left joystick x-axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_LEFT_Y** = `1`

Game controller left joystick y-axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_RIGHT_X** = `2`

Game controller right joystick x-axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_RIGHT_Y** = `3`

Game controller right joystick y-axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_TRIGGER_LEFT** = `4`

Game controller left trigger axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_TRIGGER_RIGHT** = `5`

Game controller right trigger axis.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_SDL_MAX** = `6`

The number of SDL game controller axes.

classref-enumeration-constant

`JoyAxis<enum_@GlobalScope_JoyAxis>` **JOY_AXIS_MAX** = `10`

The maximum number of game controller axes: OpenVR supports up to 5 Joysticks making a total of 10 axes.

classref-item-separator

classref-enumeration

enum **MIDIMessage**: `🔗<enum_@GlobalScope_MIDIMessage>`

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_NONE** = `0`

Does not correspond to any MIDI message. This is the default value of `InputEventMIDI.message<class_InputEventMIDI_property_message>`.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_NOTE_OFF** = `8`

MIDI message sent when a note is released.

**Note:** Not all MIDI devices send this message; some may send `MIDI_MESSAGE_NOTE_ON<class_@GlobalScope_constant_MIDI_MESSAGE_NOTE_ON>` with `InputEventMIDI.velocity<class_InputEventMIDI_property_velocity>` set to `0`.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_NOTE_ON** = `9`

MIDI message sent when a note is pressed.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_AFTERTOUCH** = `10`

MIDI message sent to indicate a change in pressure while a note is being pressed down, also called aftertouch.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_CONTROL_CHANGE** = `11`

MIDI message sent when a controller value changes. In a MIDI device, a controller is any input that doesn't play notes. These may include sliders for volume, balance, and panning, as well as switches and pedals. See the [General MIDI specification](https://en.wikipedia.org/wiki/General_MIDI#Controller_events) for a small list.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_PROGRAM_CHANGE** = `12`

MIDI message sent when the MIDI device changes its current instrument (also called *program* or *preset*).

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_CHANNEL_PRESSURE** = `13`

MIDI message sent to indicate a change in pressure for the whole channel. Some MIDI devices may send this instead of `MIDI_MESSAGE_AFTERTOUCH<class_@GlobalScope_constant_MIDI_MESSAGE_AFTERTOUCH>`.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_PITCH_BEND** = `14`

MIDI message sent when the value of the pitch bender changes, usually a wheel on the MIDI device.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_SYSTEM_EXCLUSIVE** = `240`

MIDI system exclusive (SysEx) message. This type of message is not standardized and it's highly dependent on the MIDI device sending it.

**Note:** Getting this message's data from `InputEventMIDI<class_InputEventMIDI>` is not implemented.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_QUARTER_FRAME** = `241`

MIDI message sent every quarter frame to keep connected MIDI devices synchronized. Related to `MIDI_MESSAGE_TIMING_CLOCK<class_@GlobalScope_constant_MIDI_MESSAGE_TIMING_CLOCK>`.

**Note:** Getting this message's data from `InputEventMIDI<class_InputEventMIDI>` is not implemented.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_SONG_POSITION_POINTER** = `242`

MIDI message sent to jump onto a new position in the current sequence or song.

**Note:** Getting this message's data from `InputEventMIDI<class_InputEventMIDI>` is not implemented.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_SONG_SELECT** = `243`

MIDI message sent to select a sequence or song to play.

**Note:** Getting this message's data from `InputEventMIDI<class_InputEventMIDI>` is not implemented.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_TUNE_REQUEST** = `246`

MIDI message sent to request a tuning calibration. Used on analog synthesizers. Most modern MIDI devices do not need this message.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_TIMING_CLOCK** = `248`

MIDI message sent 24 times after `MIDI_MESSAGE_QUARTER_FRAME<class_@GlobalScope_constant_MIDI_MESSAGE_QUARTER_FRAME>`, to keep connected MIDI devices synchronized.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_START** = `250`

MIDI message sent to start the current sequence or song from the beginning.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_CONTINUE** = `251`

MIDI message sent to resume from the point the current sequence or song was paused.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_STOP** = `252`

MIDI message sent to pause the current sequence or song.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_ACTIVE_SENSING** = `254`

MIDI message sent repeatedly while the MIDI device is idle, to tell the receiver that the connection is alive. Most MIDI devices do not send this message.

classref-enumeration-constant

`MIDIMessage<enum_@GlobalScope_MIDIMessage>` **MIDI_MESSAGE_SYSTEM_RESET** = `255`

MIDI message sent to reset a MIDI device to its default state, as if it was just turned on. It should not be sent when the MIDI device is being turned on.

classref-item-separator

classref-enumeration

enum **Error**: `🔗<enum_@GlobalScope_Error>`

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **OK** = `0`

Methods that return `Error<enum_@GlobalScope_Error>` return `OK<class_@GlobalScope_constant_OK>` when no error occurred.

Since `OK<class_@GlobalScope_constant_OK>` has value `0`, and all other error constants are positive integers, it can also be used in boolean checks.

    var error = method_that_returns_error()
    if error != OK:
        printerr("Failure!")

    # Or, alternatively:
    if error:
        printerr("Still failing!")

**Note:** Many functions do not return an error code, but will print error messages to standard output.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **FAILED** = `1`

Generic error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_UNAVAILABLE** = `2`

Unavailable error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_UNCONFIGURED** = `3`

Unconfigured error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_UNAUTHORIZED** = `4`

Unauthorized error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_PARAMETER_RANGE_ERROR** = `5`

Parameter range error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_OUT_OF_MEMORY** = `6`

Out of memory (OOM) error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_NOT_FOUND** = `7`

File: Not found error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_BAD_DRIVE** = `8`

File: Bad drive error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_BAD_PATH** = `9`

File: Bad path error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_NO_PERMISSION** = `10`

File: No permission error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_ALREADY_IN_USE** = `11`

File: Already in use error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_CANT_OPEN** = `12`

File: Can't open error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_CANT_WRITE** = `13`

File: Can't write error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_CANT_READ** = `14`

File: Can't read error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_UNRECOGNIZED** = `15`

File: Unrecognized error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_CORRUPT** = `16`

File: Corrupt error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_MISSING_DEPENDENCIES** = `17`

File: Missing dependencies error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_FILE_EOF** = `18`

File: End of file (EOF) error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CANT_OPEN** = `19`

Can't open error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CANT_CREATE** = `20`

Can't create error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_QUERY_FAILED** = `21`

Query failed error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_ALREADY_IN_USE** = `22`

Already in use error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_LOCKED** = `23`

Locked error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_TIMEOUT** = `24`

Timeout error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CANT_CONNECT** = `25`

Can't connect error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CANT_RESOLVE** = `26`

Can't resolve error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CONNECTION_ERROR** = `27`

Connection error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CANT_ACQUIRE_RESOURCE** = `28`

Can't acquire resource error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CANT_FORK** = `29`

Can't fork process error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_INVALID_DATA** = `30`

Invalid data error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_INVALID_PARAMETER** = `31`

Invalid parameter error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_ALREADY_EXISTS** = `32`

Already exists error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_DOES_NOT_EXIST** = `33`

Does not exist error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_DATABASE_CANT_READ** = `34`

Database: Read error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_DATABASE_CANT_WRITE** = `35`

Database: Write error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_COMPILATION_FAILED** = `36`

Compilation failed error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_METHOD_NOT_FOUND** = `37`

Method not found error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_LINK_FAILED** = `38`

Linking failed error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_SCRIPT_FAILED** = `39`

Script failed error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_CYCLIC_LINK** = `40`

Cycling link (import cycle) error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_INVALID_DECLARATION** = `41`

Invalid declaration error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_DUPLICATE_SYMBOL** = `42`

Duplicate symbol error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_PARSE_ERROR** = `43`

Parse error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_BUSY** = `44`

Busy error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_SKIP** = `45`

Skip error.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_HELP** = `46`

Help error. Used internally when passing `--version` or `--help` as executable options.

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_BUG** = `47`

Bug error, caused by an implementation issue in the method.

**Note:** If a built-in method returns this code, please open an issue on [the GitHub Issue Tracker](https://github.com/godotengine/godot/issues).

classref-enumeration-constant

`Error<enum_@GlobalScope_Error>` **ERR_PRINTER_ON_FIRE** = `48`

Printer on fire error (this is an easter egg, no built-in methods return this error code).

classref-item-separator

classref-enumeration

enum **PropertyHint**: `🔗<enum_@GlobalScope_PropertyHint>`

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_NONE** = `0`

The property has no hint for the editor. However, the hint string is still read, which can be used to specify a suffix for a property that has no range limit (see `PROPERTY_HINT_RANGE<class_@GlobalScope_constant_PROPERTY_HINT_RANGE>`'s description).

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_RANGE** = `1`

Hints that an `int<class_int>`, `float<class_float>`, or packed/typed `Array<class_Array>` property containing `int<class_int>` or `float<class_float>` types should be within a range specified via the hint string `"min,max"` or `"min,max,step"`. The hint string can optionally include `"or_greater"` and/or `"or_less"` to allow manual input going respectively above the max or below the min values.

**Example:** `"-360,360,1,or_greater,or_less"`.

Additionally, other keywords can be included: `"exp"` for exponential range editing, `"radians_as_degrees"` for editing radian angles in degrees (the range values are also in degrees), `"degrees"` to hint at an angle, `"prefer_slider"` to show the slider for integers, `"hide_control"` to hide the slider or up-down arrows, and `"suffix:px/s"` to display a suffix indicating the value's unit (e.g. `px/s` for pixels per second).

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_ENUM** = `2`

Hints that an `int<class_int>`, `String<class_String>`, or `StringName<class_StringName>` property is an enumerated value to pick in a list specified via a hint string.

The hint string is a comma separated list of names such as `"Hello,Something,Else"`. Whitespace is **not** removed from either end of a name. For integer properties, the first name in the list has value 0, the next 1, and so on. Explicit values can also be specified by appending `:integer` to the name, e.g. `"Zero,One,Three:3,Four,Six:6"`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_ENUM_SUGGESTION** = `3`

Hints that a `String<class_String>` or `StringName<class_StringName>` property can be an enumerated value to pick in a list specified via a hint string such as `"Hello,Something,Else"`. See `PROPERTY_HINT_ENUM<class_@GlobalScope_constant_PROPERTY_HINT_ENUM>` for details.

Unlike `PROPERTY_HINT_ENUM<class_@GlobalScope_constant_PROPERTY_HINT_ENUM>`, a property with this hint still accepts arbitrary values and can be empty. The list of values serves to suggest possible values.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_EXP_EASING** = `4`

Hints that a `float<class_float>` property should be edited using a curve editor showing an exponential easing function. The hint string can include `"attenuation"` to flip the curve horizontally and/or `"positive_only"` to exclude in/out easing and limit values to be greater than or equal to zero. This displays differently to a property that uses `PROPERTY_HINT_RANGE<class_@GlobalScope_constant_PROPERTY_HINT_RANGE>` with the `"exp"` keyword, as it's edited with a slider instead of a curve editor.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LINK** = `5`

Hints that a vector property should allow its components to be linked. For example, this allows `Vector2.x<class_Vector2_property_x>` and `Vector2.y<class_Vector2_property_y>` to be edited together. This hint is supported on `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, and `Vector4i<class_Vector4i>`. The hint string can be used to specify a suffix indicating each value's unit with the `"suffix:px/s"` syntax.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_FLAGS** = `6`

Hints that an `int<class_int>` property is a bitmask with named bit flags.

The hint string is a comma separated list of names such as `"Bit0,Bit1,Bit2,Bit3"`. Whitespace is **not** removed from either end of a name. The first name in the list has value 1, the next 2, then 4, 8, 16 and so on. Explicit values can also be specified by appending `:integer` to the name, e.g. `"A:4,B:8,C:16"`. You can also combine several flags (`"A:4,B:8,AB:12,C:16"`).

**Note:** A flag value must be at least `1` and at most `2 ** 32 - 1`.

**Note:** Unlike `PROPERTY_HINT_ENUM<class_@GlobalScope_constant_PROPERTY_HINT_ENUM>`, the previous explicit value is not taken into account. For the hint `"A:16,B,C"`, A is 16, B is 2, C is 4.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_2D_RENDER** = `7`

Hints that an `int<class_int>` property is a bitmask using the optionally named 2D render layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_2D_PHYSICS** = `8`

Hints that an `int<class_int>` property is a bitmask using the optionally named 2D physics layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_2D_NAVIGATION** = `9`

Hints that an `int<class_int>` property is a bitmask using the optionally named 2D navigation layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_3D_RENDER** = `10`

Hints that an `int<class_int>` property is a bitmask using the optionally named 3D render layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_3D_PHYSICS** = `11`

Hints that an `int<class_int>` property is a bitmask using the optionally named 3D physics layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_3D_NAVIGATION** = `12`

Hints that an `int<class_int>` property is a bitmask using the optionally named 3D navigation layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LAYERS_AVOIDANCE** = `37`

Hints that an integer property is a bitmask using the optionally named avoidance layers.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_FILE** = `13`

Hints that a `String<class_String>` property is a path to a file. Editing it will show a file dialog for picking the path. The hint string can be a set of filters with wildcards like `"*.png,*.jpg"`. By default the file will be stored as UID whenever available. You can use `ResourceUID<class_ResourceUID>` methods to convert it back to path. For storing a raw path, use `PROPERTY_HINT_FILE_PATH<class_@GlobalScope_constant_PROPERTY_HINT_FILE_PATH>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_DIR** = `14`

Hints that a `String<class_String>` property is a path to a directory. Editing it will show a file dialog for picking the path.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_GLOBAL_FILE** = `15`

Hints that a `String<class_String>` property is an absolute path to a file outside the project folder. Editing it will show a file dialog for picking the path. The hint string can be a set of filters with wildcards, like `"*.png,*.jpg"`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_GLOBAL_DIR** = `16`

Hints that a `String<class_String>` property is an absolute path to a directory outside the project folder. Editing it will show a file dialog for picking the path.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_RESOURCE_TYPE** = `17`

Hints that a property is an instance of a `Resource<class_Resource>`-derived type, optionally specified via the hint string (e.g. `"Texture2D"`). Editing it will show a popup menu of valid resource types to instantiate.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_MULTILINE_TEXT** = `18`

Hints that a `String<class_String>` property is text with line breaks. Editing it will show a text input field where line breaks can be typed.

The hint string can be set to `"monospace"` to force the input field to use a monospaced font.

If the hint string `"no_wrap"` is set, the input field will not wrap lines at boundaries, instead resorting to making the area scrollable.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_EXPRESSION** = `19`

Hints that a `String<class_String>` property is an `Expression<class_Expression>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_PLACEHOLDER_TEXT** = `20`

Hints that a `String<class_String>` property should show a placeholder text on its input field, if empty. The hint string is the placeholder text to use.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_COLOR_NO_ALPHA** = `21`

Hints that a `Color<class_Color>` property should be edited without affecting its transparency (`Color.a<class_Color_property_a>` is not editable).

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_OBJECT_ID** = `22`

Hints that the property's value is an object encoded as object ID, with its type specified in the hint string. Used by the debugger.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_TYPE_STRING** = `23`

If a property is `String<class_String>`, hints that the property represents a particular type (class). This allows to select a type from the create dialog. The property will store the selected type as a string.

If a property is `Array<class_Array>`, hints the editor how to show elements. The `hint_string` must encode nested types using `":"` and `"/"`.

If a property is `Dictionary<class_Dictionary>`, hints the editor how to show elements. The `hint_string` is the same as `Array<class_Array>`, with a `";"` separating the key and value.

gdscript

\# Array of elem_type. hint_string = "%d:" % \[elem_type\] hint_string = "%d/%d:%s" % \[elem_type, elem_hint, elem_hint_string\] \# Two-dimensional array of elem_type (array of arrays of elem_type). hint_string = "%d:%d:" % \[TYPE_ARRAY, elem_type\] hint_string = "%d:%d/%d:%s" % \[TYPE_ARRAY, elem_type, elem_hint, elem_hint_string\] \# Three-dimensional array of elem_type (array of arrays of arrays of elem_type). hint_string = "%d:%d:%d:" % \[TYPE_ARRAY, TYPE_ARRAY, elem_type\] hint_string = "%d:%d:%d/%d:%s" % \[TYPE_ARRAY, TYPE_ARRAY, elem_type, elem_hint, elem_hint_string\]

csharp

// Array of elemType. hintString = \$"{elemType:D}:"; hintString = \$"{elemType:D}/{elemHint:D}:{elemHintString}"; // Two-dimensional array of elemType (array of arrays of elemType). hintString = \$"{Variant.Type.Array:D}:{elemType:D}:"; hintString = \$"{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}"; // Three-dimensional array of elemType (array of arrays of arrays of elemType). hintString = \$"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}:"; hintString = \$"{Variant.Type.Array:D}:{Variant.Type.Array:D}:{elemType:D}/{elemHint:D}:{elemHintString}";

**Examples:**

gdscript

hint_string = "%d:" % \[TYPE_INT\] \# Array of integers. hint_string = "%d/%d:1,10,1" % \[TYPE_INT, PROPERTY_HINT_RANGE\] \# Array of integers (in range from 1 to 10). hint_string = "%d/%d:Zero,One,Two" % \[TYPE_INT, PROPERTY_HINT_ENUM\] \# Array of integers (an enum). hint_string = "%d/%d:Zero,One,Three:3,Six:6" % \[TYPE_INT, PROPERTY_HINT_ENUM\] \# Array of integers (an enum). hint_string = "%d/%d:\*.png" % \[TYPE_STRING, PROPERTY_HINT_FILE\] \# Array of strings (file paths). hint_string = "%d/%d:Texture2D" % \[TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE\] \# Array of textures.

hint_string = "%d:%d:" % \[TYPE_ARRAY, TYPE_FLOAT\] \# Two-dimensional array of floats. hint_string = "%d:%d/%d:" % \[TYPE_ARRAY, TYPE_STRING, PROPERTY_HINT_MULTILINE_TEXT\] \# Two-dimensional array of multiline strings. hint_string = "%d:%d/%d:-1,1,0.1" % \[TYPE_ARRAY, TYPE_FLOAT, PROPERTY_HINT_RANGE\] \# Two-dimensional array of floats (in range from -1 to 1). hint_string = "%d:%d/%d:Texture2D" % \[TYPE_ARRAY, TYPE_OBJECT, PROPERTY_HINT_RESOURCE_TYPE\] \# Two-dimensional array of textures.

csharp

hintString = \$"{Variant.Type.Int:D}/{PropertyHint.Range:D}:1,10,1"; // Array of integers (in range from 1 to 10). hintString = \$"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Two"; // Array of integers (an enum). hintString = \$"{Variant.Type.Int:D}/{PropertyHint.Enum:D}:Zero,One,Three:3,Six:6"; // Array of integers (an enum). hintString = \$"{Variant.Type.String:D}/{PropertyHint.File:D}:\*.png"; // Array of strings (file paths). hintString = \$"{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Array of textures.

hintString = \$"{Variant.Type.Array:D}:{Variant.Type.Float:D}:"; // Two-dimensional array of floats. hintString = \$"{Variant.Type.Array:D}:{Variant.Type.String:D}/{PropertyHint.MultilineText:D}:"; // Two-dimensional array of multiline strings. hintString = \$"{Variant.Type.Array:D}:{Variant.Type.Float:D}/{PropertyHint.Range:D}:-1,1,0.1"; // Two-dimensional array of floats (in range from -1 to 1). hintString = \$"{Variant.Type.Array:D}:{Variant.Type.Object:D}/{PropertyHint.ResourceType:D}:Texture2D"; // Two-dimensional array of textures.

**Note:** The trailing colon is required for properly detecting built-in types.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_NODE_PATH_TO_EDITED_NODE** = `24`

**Deprecated:** This hint is not used by the engine.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_OBJECT_TOO_BIG** = `25`

Hints that an object is too big to be sent via the debugger.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_NODE_PATH_VALID_TYPES** = `26`

Hints that the hint string specifies valid node types for property of type `NodePath<class_NodePath>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_SAVE_FILE** = `27`

Hints that a `String<class_String>` property is a path to a file. Editing it will show a file dialog for picking the path for the file to be saved at. The dialog has access to the project's directory. The hint string can be a set of filters with wildcards like `"*.png,*.jpg"`. See also `FileDialog.filters<class_FileDialog_property_filters>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_GLOBAL_SAVE_FILE** = `28`

Hints that a `String<class_String>` property is a path to a file. Editing it will show a file dialog for picking the path for the file to be saved at. The dialog has access to the entire filesystem. The hint string can be a set of filters with wildcards like `"*.png,*.jpg"`. See also `FileDialog.filters<class_FileDialog_property_filters>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_INT_IS_OBJECTID** = `29`

**Deprecated:** This hint is not used by the engine.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_INT_IS_POINTER** = `30`

Hints that an `int<class_int>` property is a pointer. Used by GDExtension.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_ARRAY_TYPE** = `31`

Hints that a property is an `Array<class_Array>` with the stored type specified in the hint string. The hint string contains the type of the array (e.g. `"String"`).

Use the hint string format from `PROPERTY_HINT_TYPE_STRING<class_@GlobalScope_constant_PROPERTY_HINT_TYPE_STRING>` for more control over the stored type.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_DICTIONARY_TYPE** = `38`

Hints that a property is a `Dictionary<class_Dictionary>` with the stored types specified in the hint string. The hint string contains the key and value types separated by a semicolon (e.g. `"int;String"`).

Use the hint string format from `PROPERTY_HINT_TYPE_STRING<class_@GlobalScope_constant_PROPERTY_HINT_TYPE_STRING>` for more control over the stored types.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LOCALE_ID** = `32`

Hints that a string property is a locale code. Editing it will show a locale dialog for picking language and country.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_LOCALIZABLE_STRING** = `33`

Hints that a dictionary property is string translation map. Dictionary keys are locale codes and, values are translated strings.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_NODE_TYPE** = `34`

Hints that a property is an instance of a `Node<class_Node>`-derived type, optionally specified via the hint string (e.g. `"Node2D"`). Editing it will show a dialog for picking a node from the scene.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_HIDE_QUATERNION_EDIT** = `35`

Hints that a quaternion property should disable the temporary euler editor.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_PASSWORD** = `36`

Hints that a string property is a password, and every character is replaced with the secret character.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_TOOL_BUTTON** = `39`

Hints that a `Callable<class_Callable>` property should be displayed as a clickable button. When the button is pressed, the callable is called. The hint string specifies the button text and optionally an icon from the `"EditorIcons"` theme type.

``` text
"Click me!" - A button with the text "Click me!" and the default "Callable" icon.
"Click me!,ColorRect" - A button with the text "Click me!" and the "ColorRect" icon.
```

**Note:** A `Callable<class_Callable>` cannot be properly serialized and stored in a file, so it is recommended to use `PROPERTY_USAGE_EDITOR<class_@GlobalScope_constant_PROPERTY_USAGE_EDITOR>` instead of `PROPERTY_USAGE_DEFAULT<class_@GlobalScope_constant_PROPERTY_USAGE_DEFAULT>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_ONESHOT** = `40`

Hints that a property will be changed on its own after setting, such as `AudioStreamPlayer.playing<class_AudioStreamPlayer_property_playing>` or `GPUParticles3D.emitting<class_GPUParticles3D_property_emitting>`.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_GROUP_ENABLE** = `42`

Hints that a boolean property will enable the feature associated with the group that it occurs in. The property will be displayed as a checkbox on the group header. Only works within a group or subgroup.

By default, disabling the property hides all properties in the group. Use the optional hint string `"checkbox_only"` to disable this behavior.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_INPUT_NAME** = `43`

Hints that a `String<class_String>` or `StringName<class_StringName>` property is the name of an input action. This allows the selection of any action name from the Input Map in the Project Settings. The hint string may contain two options separated by commas:

- If it contains `"show_builtin"`, built-in input actions are included in the selection.
- If it contains `"loose_mode"`, loose mode is enabled. This allows inserting any action name even if it's not present in the input map.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_FILE_PATH** = `44`

Like `PROPERTY_HINT_FILE<class_@GlobalScope_constant_PROPERTY_HINT_FILE>`, but the property is stored as a raw path, not UID. That means the reference will be broken if you move the file. Consider using `PROPERTY_HINT_FILE<class_@GlobalScope_constant_PROPERTY_HINT_FILE>` when possible.

classref-enumeration-constant

`PropertyHint<enum_@GlobalScope_PropertyHint>` **PROPERTY_HINT_MAX** = `45`

Represents the size of the `PropertyHint<enum_@GlobalScope_PropertyHint>` enum.

classref-item-separator

classref-enumeration

flags **PropertyUsageFlags**: `🔗<enum_@GlobalScope_PropertyUsageFlags>`

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_NONE** = `0`

The property is not stored, and does not display in the editor. This is the default for non-exported properties.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_STORAGE** = `2`

The property is serialized and saved in the scene file (default for exported properties).

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_EDITOR** = `4`

The property is shown in the `EditorInspector<class_EditorInspector>` (default for exported properties).

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_INTERNAL** = `8`

The property is excluded from the class reference.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_CHECKABLE** = `16`

The property can be checked in the `EditorInspector<class_EditorInspector>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_CHECKED** = `32`

The property is checked in the `EditorInspector<class_EditorInspector>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_GROUP** = `64`

Used to group properties together in the editor. See `EditorInspector<class_EditorInspector>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_CATEGORY** = `128`

Used to categorize properties together in the editor.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_SUBGROUP** = `256`

Used to group properties together in the editor in a subgroup (under a group). See `EditorInspector<class_EditorInspector>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_CLASS_IS_BITFIELD** = `512`

The property is a bitfield, i.e. it contains multiple flags represented as bits.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_NO_INSTANCE_STATE** = `1024`

The property does not save its state in `PackedScene<class_PackedScene>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_RESTART_IF_CHANGED** = `2048`

Editing the property prompts the user for restarting the editor.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_SCRIPT_VARIABLE** = `4096`

The property is a script variable. `PROPERTY_USAGE_SCRIPT_VARIABLE<class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_VARIABLE>` can be used to distinguish between exported script variables from built-in variables (which don't have this usage flag). By default, `PROPERTY_USAGE_SCRIPT_VARIABLE<class_@GlobalScope_constant_PROPERTY_USAGE_SCRIPT_VARIABLE>` is **not** applied to variables that are created by overriding `Object._get_property_list()<class_Object_private_method__get_property_list>` in a script.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_STORE_IF_NULL** = `8192`

The property value of type `Object<class_Object>` will be stored even if its value is `null`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_UPDATE_ALL_IF_MODIFIED** = `16384`

If this property is modified, all inspector fields will be refreshed.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_SCRIPT_DEFAULT_VALUE** = `32768`

**Deprecated:** This flag is not used by the engine.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_CLASS_IS_ENUM** = `65536`

The property is a variable of enum type, i.e. it only takes named integer constants from its associated enumeration.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_NIL_IS_VARIANT** = `131072`

If property has `nil` as default value, its type will be `Variant<class_Variant>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_ARRAY** = `262144`

The property is the element count of a property array, i.e. a list of groups of related properties. Properties defined with this usage also need a specific `class_name` field in the form of `label,prefix`. The field may also include additional comma-separated options:

- `page_size=N`: Overrides `EditorSettings.interface/inspector/max_array_dictionary_items_per_page<class_EditorSettings_property_interface/inspector/max_array_dictionary_items_per_page>` for this array.
- `add_button_text=text`: The text displayed by the "Add Element" button.
- `static`: The elements can't be re-arranged.
- `const`: New elements can't be added.
- `numbered`: An index will appear next to each element.
- `unfoldable`: The array can't be folded.
- `swap_method=method_name`: The method that will be called when two elements switch places. The method should take 2 `int<class_int>` parameters, which will be indices of the elements being swapped.

Note that making a full-fledged property array requires boilerplate code involving `Object._get_property_list()<class_Object_private_method__get_property_list>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_ALWAYS_DUPLICATE** = `524288`

When duplicating a resource with `Resource.duplicate()<class_Resource_method_duplicate>`, and this flag is set on a property of that resource, the property should always be duplicated, regardless of the `subresources` bool parameter.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_NEVER_DUPLICATE** = `1048576`

When duplicating a resource with `Resource.duplicate()<class_Resource_method_duplicate>`, and this flag is set on a property of that resource, the property should never be duplicated, regardless of the `subresources` bool parameter.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_HIGH_END_GFX** = `2097152`

The property is only shown in the editor if modern renderers are supported (the Compatibility rendering method is excluded).

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_NODE_PATH_FROM_SCENE_ROOT** = `4194304`

The `NodePath<class_NodePath>` property will always be relative to the scene's root. Mostly useful for local resources.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_RESOURCE_NOT_PERSISTENT** = `8388608`

Use when a resource is created on the fly, i.e. the getter will always return a different instance. `ResourceSaver<class_ResourceSaver>` needs this information to properly save such resources.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_KEYING_INCREMENTS** = `16777216`

Inserting an animation key frame of this property will automatically increment the value, allowing to easily keyframe multiple values in a row.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_DEFERRED_SET_RESOURCE** = `33554432`

**Deprecated:** This flag is not used by the engine.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_EDITOR_INSTANTIATE_OBJECT** = `67108864`

When this property is a `Resource<class_Resource>` and base object is a `Node<class_Node>`, a resource instance will be automatically created whenever the node is created in the editor.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_EDITOR_BASIC_SETTING** = `134217728`

The property is considered a basic setting and will appear even when advanced mode is disabled. Used for project settings.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_READ_ONLY** = `268435456`

The property is read-only in the `EditorInspector<class_EditorInspector>`.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_SECRET** = `536870912`

An export preset property with this flag contains confidential information and is stored separately from the rest of the export preset configuration.

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_DEFAULT** = `6`

Default usage (storage and editor).

classref-enumeration-constant

`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>` **PROPERTY_USAGE_NO_EDITOR** = `2`

Default usage but without showing the property in the editor (storage).

classref-item-separator

classref-enumeration

flags **MethodFlags**: `🔗<enum_@GlobalScope_MethodFlags>`

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_NORMAL** = `1`

Flag for a normal method.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_EDITOR** = `2`

Flag for an editor method.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_CONST** = `4`

Flag for a constant method.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_VIRTUAL** = `8`

Flag for a virtual method.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_VARARG** = `16`

Flag for a method with a variable number of arguments.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_STATIC** = `32`

Flag for a static method.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_OBJECT_CORE** = `64`

Used internally. Allows to not dump core virtual methods (such as `Object._notification()<class_Object_private_method__notification>`) to the JSON API.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAG_VIRTUAL_REQUIRED** = `128`

Flag for a virtual method that is required. In GDScript, this flag is set for abstract functions.

classref-enumeration-constant

`MethodFlags<enum_@GlobalScope_MethodFlags>` **METHOD_FLAGS_DEFAULT** = `1`

Default method flags (normal).

classref-item-separator

classref-enumeration

enum **Variant.Type**: `🔗<enum_@GlobalScope_Variant.Type>`

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_NIL** = `0`

Variable is `null`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_BOOL** = `1`

Variable is of type `bool<class_bool>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_INT** = `2`

Variable is of type `int<class_int>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_FLOAT** = `3`

Variable is of type `float<class_float>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_STRING** = `4`

Variable is of type `String<class_String>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_VECTOR2** = `5`

Variable is of type `Vector2<class_Vector2>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_VECTOR2I** = `6`

Variable is of type `Vector2i<class_Vector2i>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_RECT2** = `7`

Variable is of type `Rect2<class_Rect2>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_RECT2I** = `8`

Variable is of type `Rect2i<class_Rect2i>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_VECTOR3** = `9`

Variable is of type `Vector3<class_Vector3>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_VECTOR3I** = `10`

Variable is of type `Vector3i<class_Vector3i>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_TRANSFORM2D** = `11`

Variable is of type `Transform2D<class_Transform2D>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_VECTOR4** = `12`

Variable is of type `Vector4<class_Vector4>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_VECTOR4I** = `13`

Variable is of type `Vector4i<class_Vector4i>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PLANE** = `14`

Variable is of type `Plane<class_Plane>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_QUATERNION** = `15`

Variable is of type `Quaternion<class_Quaternion>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_AABB** = `16`

Variable is of type `AABB<class_AABB>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_BASIS** = `17`

Variable is of type `Basis<class_Basis>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_TRANSFORM3D** = `18`

Variable is of type `Transform3D<class_Transform3D>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PROJECTION** = `19`

Variable is of type `Projection<class_Projection>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_COLOR** = `20`

Variable is of type `Color<class_Color>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_STRING_NAME** = `21`

Variable is of type `StringName<class_StringName>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_NODE_PATH** = `22`

Variable is of type `NodePath<class_NodePath>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_RID** = `23`

Variable is of type `RID<class_RID>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_OBJECT** = `24`

Variable is of type `Object<class_Object>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_CALLABLE** = `25`

Variable is of type `Callable<class_Callable>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_SIGNAL** = `26`

Variable is of type `Signal<class_Signal>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_DICTIONARY** = `27`

Variable is of type `Dictionary<class_Dictionary>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_ARRAY** = `28`

Variable is of type `Array<class_Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_BYTE_ARRAY** = `29`

Variable is of type `PackedByteArray<class_PackedByteArray>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_INT32_ARRAY** = `30`

Variable is of type `PackedInt32Array<class_PackedInt32Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_INT64_ARRAY** = `31`

Variable is of type `PackedInt64Array<class_PackedInt64Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_FLOAT32_ARRAY** = `32`

Variable is of type `PackedFloat32Array<class_PackedFloat32Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_FLOAT64_ARRAY** = `33`

Variable is of type `PackedFloat64Array<class_PackedFloat64Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_STRING_ARRAY** = `34`

Variable is of type `PackedStringArray<class_PackedStringArray>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_VECTOR2_ARRAY** = `35`

Variable is of type `PackedVector2Array<class_PackedVector2Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_VECTOR3_ARRAY** = `36`

Variable is of type `PackedVector3Array<class_PackedVector3Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_COLOR_ARRAY** = `37`

Variable is of type `PackedColorArray<class_PackedColorArray>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_PACKED_VECTOR4_ARRAY** = `38`

Variable is of type `PackedVector4Array<class_PackedVector4Array>`.

classref-enumeration-constant

`Variant.Type<enum_@GlobalScope_Variant.Type>` **TYPE_MAX** = `39`

Represents the size of the `Variant.Type<enum_@GlobalScope_Variant.Type>` enum.

classref-item-separator

classref-enumeration

enum **Variant.Operator**: `🔗<enum_@GlobalScope_Variant.Operator>`

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_EQUAL** = `0`

Equality operator (`==`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_NOT_EQUAL** = `1`

Inequality operator (`!=`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_LESS** = `2`

Less than operator (`<`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_LESS_EQUAL** = `3`

Less than or equal operator (`<=`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_GREATER** = `4`

Greater than operator (`>`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_GREATER_EQUAL** = `5`

Greater than or equal operator (`>=`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_ADD** = `6`

Addition operator (`+`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_SUBTRACT** = `7`

Subtraction operator (`-`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_MULTIPLY** = `8`

Multiplication operator (`*`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_DIVIDE** = `9`

Division operator (`/`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_NEGATE** = `10`

Unary negation operator (`-`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_POSITIVE** = `11`

Unary plus operator (`+`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_MODULE** = `12`

Remainder/modulo operator (`%`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_POWER** = `13`

Power operator (`**`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_SHIFT_LEFT** = `14`

Left shift operator (`<<`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_SHIFT_RIGHT** = `15`

Right shift operator (`>>`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_BIT_AND** = `16`

Bitwise AND operator (`&`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_BIT_OR** = `17`

Bitwise OR operator (`|`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_BIT_XOR** = `18`

Bitwise XOR operator (`^`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_BIT_NEGATE** = `19`

Bitwise NOT operator (`~`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_AND** = `20`

Logical AND operator (`and` or `&&`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_OR** = `21`

Logical OR operator (`or` or `||`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_XOR** = `22`

Logical XOR operator (not implemented in GDScript).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_NOT** = `23`

Logical NOT operator (`not` or `!`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_IN** = `24`

Logical IN operator (`in`).

classref-enumeration-constant

`Variant.Operator<enum_@GlobalScope_Variant.Operator>` **OP_MAX** = `25`

Represents the size of the `Variant.Operator<enum_@GlobalScope_Variant.Operator>` enum.

classref-section-separator

classref-descriptions-group

## Constants

classref-constant

**UINT8_MAX** = `255` `🔗<class_@GlobalScope_constant_UINT8_MAX>`

Maximum value of an 8-bit unsigned integer.

classref-constant

**UINT16_MAX** = `65535` `🔗<class_@GlobalScope_constant_UINT16_MAX>`

Maximum value of a 16-bit unsigned integer.

classref-constant

**UINT32_MAX** = `4294967295` `🔗<class_@GlobalScope_constant_UINT32_MAX>`

Maximum value of a 32-bit unsigned integer.

classref-constant

**INT8_MIN** = `-128` `🔗<class_@GlobalScope_constant_INT8_MIN>`

Minimum value of an 8-bit signed integer.

classref-constant

**INT8_MAX** = `127` `🔗<class_@GlobalScope_constant_INT8_MAX>`

Maximum value of an 8-bit signed integer.

classref-constant

**INT16_MIN** = `-32768` `🔗<class_@GlobalScope_constant_INT16_MIN>`

Minimum value of a 16-bit signed integer.

classref-constant

**INT16_MAX** = `32767` `🔗<class_@GlobalScope_constant_INT16_MAX>`

Maximum value of a 16-bit signed integer.

classref-constant

**INT32_MIN** = `-2147483648` `🔗<class_@GlobalScope_constant_INT32_MIN>`

Minimum value of a 32-bit signed integer.

classref-constant

**INT32_MAX** = `2147483647` `🔗<class_@GlobalScope_constant_INT32_MAX>`

Maximum value of a 32-bit signed integer.

classref-constant

**INT64_MIN** = `-9223372036854775808` `🔗<class_@GlobalScope_constant_INT64_MIN>`

Minimum value of a 64-bit signed integer.

classref-constant

**INT64_MAX** = `9223372036854775807` `🔗<class_@GlobalScope_constant_INT64_MAX>`

Maximum value of a 64-bit signed integer.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`AccessibilityServer<class_AccessibilityServer>` **AccessibilityServer** `🔗<class_@GlobalScope_property_AccessibilityServer>`

The `AccessibilityServer<class_AccessibilityServer>` singleton.

classref-item-separator

classref-property

`AudioServer<class_AudioServer>` **AudioServer** `🔗<class_@GlobalScope_property_AudioServer>`

The `AudioServer<class_AudioServer>` singleton.

classref-item-separator

classref-property

`CameraServer<class_CameraServer>` **CameraServer** `🔗<class_@GlobalScope_property_CameraServer>`

The `CameraServer<class_CameraServer>` singleton.

classref-item-separator

classref-property

`ClassDB<class_ClassDB>` **ClassDB** `🔗<class_@GlobalScope_property_ClassDB>`

The `ClassDB<class_ClassDB>` singleton.

classref-item-separator

classref-property

`DisplayServer<class_DisplayServer>` **DisplayServer** `🔗<class_@GlobalScope_property_DisplayServer>`

The `DisplayServer<class_DisplayServer>` singleton.

classref-item-separator

classref-property

`EditorInterface<class_EditorInterface>` **EditorInterface** `🔗<class_@GlobalScope_property_EditorInterface>`

The `EditorInterface<class_EditorInterface>` singleton.

**Note:** Only available in editor builds.

classref-item-separator

classref-property

`Engine<class_Engine>` **Engine** `🔗<class_@GlobalScope_property_Engine>`

The `Engine<class_Engine>` singleton.

classref-item-separator

classref-property

`EngineDebugger<class_EngineDebugger>` **EngineDebugger** `🔗<class_@GlobalScope_property_EngineDebugger>`

The `EngineDebugger<class_EngineDebugger>` singleton.

classref-item-separator

classref-property

`GDExtensionManager<class_GDExtensionManager>` **GDExtensionManager** `🔗<class_@GlobalScope_property_GDExtensionManager>`

The `GDExtensionManager<class_GDExtensionManager>` singleton.

classref-item-separator

classref-property

`GDScriptLanguageProtocol<class_GDScriptLanguageProtocol>` **GDScriptLanguageProtocol** `🔗<class_@GlobalScope_property_GDScriptLanguageProtocol>`

The `GDScriptLanguageProtocol<class_GDScriptLanguageProtocol>` singleton.

**Note:** Only available in editor builds.

classref-item-separator

classref-property

`Geometry2D<class_Geometry2D>` **Geometry2D** `🔗<class_@GlobalScope_property_Geometry2D>`

The `Geometry2D<class_Geometry2D>` singleton.

classref-item-separator

classref-property

`Geometry3D<class_Geometry3D>` **Geometry3D** `🔗<class_@GlobalScope_property_Geometry3D>`

The `Geometry3D<class_Geometry3D>` singleton.

classref-item-separator

classref-property

`IP<class_IP>` **IP** `🔗<class_@GlobalScope_property_IP>`

The `IP<class_IP>` singleton.

classref-item-separator

classref-property

`Input<class_Input>` **Input** `🔗<class_@GlobalScope_property_Input>`

The `Input<class_Input>` singleton.

classref-item-separator

classref-property

`InputMap<class_InputMap>` **InputMap** `🔗<class_@GlobalScope_property_InputMap>`

The `InputMap<class_InputMap>` singleton.

classref-item-separator

classref-property

`JavaClassWrapper<class_JavaClassWrapper>` **JavaClassWrapper** `🔗<class_@GlobalScope_property_JavaClassWrapper>`

The `JavaClassWrapper<class_JavaClassWrapper>` singleton.

**Note:** Only implemented on Android.

classref-item-separator

classref-property

`JavaScriptBridge<class_JavaScriptBridge>` **JavaScriptBridge** `🔗<class_@GlobalScope_property_JavaScriptBridge>`

The `JavaScriptBridge<class_JavaScriptBridge>` singleton.

**Note:** Only implemented on the Web platform.

classref-item-separator

classref-property

`Marshalls<class_Marshalls>` **Marshalls** `🔗<class_@GlobalScope_property_Marshalls>`

The `Marshalls<class_Marshalls>` singleton.

classref-item-separator

classref-property

`NativeMenu<class_NativeMenu>` **NativeMenu** `🔗<class_@GlobalScope_property_NativeMenu>`

The `NativeMenu<class_NativeMenu>` singleton.

**Note:** Only implemented on macOS.

classref-item-separator

classref-property

`NavigationMeshGenerator<class_NavigationMeshGenerator>` **NavigationMeshGenerator** `🔗<class_@GlobalScope_property_NavigationMeshGenerator>`

The `NavigationMeshGenerator<class_NavigationMeshGenerator>` singleton.

classref-item-separator

classref-property

`NavigationServer2D<class_NavigationServer2D>` **NavigationServer2D** `🔗<class_@GlobalScope_property_NavigationServer2D>`

The `NavigationServer2D<class_NavigationServer2D>` singleton.

classref-item-separator

classref-property

`NavigationServer2DManager<class_NavigationServer2DManager>` **NavigationServer2DManager** `🔗<class_@GlobalScope_property_NavigationServer2DManager>`

The `NavigationServer2DManager<class_NavigationServer2DManager>` singleton.

classref-item-separator

classref-property

`NavigationServer3D<class_NavigationServer3D>` **NavigationServer3D** `🔗<class_@GlobalScope_property_NavigationServer3D>`

The `NavigationServer3D<class_NavigationServer3D>` singleton.

classref-item-separator

classref-property

`NavigationServer3DManager<class_NavigationServer3DManager>` **NavigationServer3DManager** `🔗<class_@GlobalScope_property_NavigationServer3DManager>`

The `NavigationServer3DManager<class_NavigationServer3DManager>` singleton.

classref-item-separator

classref-property

`OS<class_OS>` **OS** `🔗<class_@GlobalScope_property_OS>`

The `OS<class_OS>` singleton.

classref-item-separator

classref-property

`Performance<class_Performance>` **Performance** `🔗<class_@GlobalScope_property_Performance>`

The `Performance<class_Performance>` singleton.

classref-item-separator

classref-property

`PhysicsServer2D<class_PhysicsServer2D>` **PhysicsServer2D** `🔗<class_@GlobalScope_property_PhysicsServer2D>`

The `PhysicsServer2D<class_PhysicsServer2D>` singleton.

classref-item-separator

classref-property

`PhysicsServer2DManager<class_PhysicsServer2DManager>` **PhysicsServer2DManager** `🔗<class_@GlobalScope_property_PhysicsServer2DManager>`

The `PhysicsServer2DManager<class_PhysicsServer2DManager>` singleton.

classref-item-separator

classref-property

`PhysicsServer3D<class_PhysicsServer3D>` **PhysicsServer3D** `🔗<class_@GlobalScope_property_PhysicsServer3D>`

The `PhysicsServer3D<class_PhysicsServer3D>` singleton.

classref-item-separator

classref-property

`PhysicsServer3DManager<class_PhysicsServer3DManager>` **PhysicsServer3DManager** `🔗<class_@GlobalScope_property_PhysicsServer3DManager>`

The `PhysicsServer3DManager<class_PhysicsServer3DManager>` singleton.

classref-item-separator

classref-property

`ProjectSettings<class_ProjectSettings>` **ProjectSettings** `🔗<class_@GlobalScope_property_ProjectSettings>`

The `ProjectSettings<class_ProjectSettings>` singleton.

classref-item-separator

classref-property

`RenderingServer<class_RenderingServer>` **RenderingServer** `🔗<class_@GlobalScope_property_RenderingServer>`

The `RenderingServer<class_RenderingServer>` singleton.

classref-item-separator

classref-property

`ResourceLoader<class_ResourceLoader>` **ResourceLoader** `🔗<class_@GlobalScope_property_ResourceLoader>`

The `ResourceLoader<class_ResourceLoader>` singleton.

classref-item-separator

classref-property

`ResourceSaver<class_ResourceSaver>` **ResourceSaver** `🔗<class_@GlobalScope_property_ResourceSaver>`

The `ResourceSaver<class_ResourceSaver>` singleton.

classref-item-separator

classref-property

`ResourceUID<class_ResourceUID>` **ResourceUID** `🔗<class_@GlobalScope_property_ResourceUID>`

The `ResourceUID<class_ResourceUID>` singleton.

classref-item-separator

classref-property

`TextServerManager<class_TextServerManager>` **TextServerManager** `🔗<class_@GlobalScope_property_TextServerManager>`

The `TextServerManager<class_TextServerManager>` singleton.

classref-item-separator

classref-property

`ThemeDB<class_ThemeDB>` **ThemeDB** `🔗<class_@GlobalScope_property_ThemeDB>`

The `ThemeDB<class_ThemeDB>` singleton.

classref-item-separator

classref-property

`Time<class_Time>` **Time** `🔗<class_@GlobalScope_property_Time>`

The `Time<class_Time>` singleton.

classref-item-separator

classref-property

`TranslationServer<class_TranslationServer>` **TranslationServer** `🔗<class_@GlobalScope_property_TranslationServer>`

The `TranslationServer<class_TranslationServer>` singleton.

classref-item-separator

classref-property

`WorkerThreadPool<class_WorkerThreadPool>` **WorkerThreadPool** `🔗<class_@GlobalScope_property_WorkerThreadPool>`

The `WorkerThreadPool<class_WorkerThreadPool>` singleton.

classref-item-separator

classref-property

`XRServer<class_XRServer>` **XRServer** `🔗<class_@GlobalScope_property_XRServer>`

The `XRServer<class_XRServer>` singleton.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Variant<class_Variant>` **abs**(x: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_abs>`

Returns the absolute value of a `Variant<class_Variant>` parameter `x` (i.e. non-negative value). Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`.

    var a = abs(-1)
    # a is 1

    var b = abs(-1.2)
    # b is 1.2

    var c = abs(Vector2(-3.5, -4))
    # c is (3.5, 4)

    var d = abs(Vector2i(-5, -6))
    # d is (5, 6)

    var e = abs(Vector3(-7, 8.5, -3.8))
    # e is (7, 8.5, 3.8)

    var f = abs(Vector3i(-7, -8, -9))
    # f is (7, 8, 9)

**Note:** For better type safety, use `absf()<class_@GlobalScope_method_absf>`, `absi()<class_@GlobalScope_method_absi>`, `Vector2.abs()<class_Vector2_method_abs>`, `Vector2i.abs()<class_Vector2i_method_abs>`, `Vector3.abs()<class_Vector3_method_abs>`, `Vector3i.abs()<class_Vector3i_method_abs>`, `Vector4.abs()<class_Vector4_method_abs>`, or `Vector4i.abs()<class_Vector4i_method_abs>`.

classref-item-separator

classref-method

`float<class_float>` **absf**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_absf>`

Returns the absolute value of float parameter `x` (i.e. positive value).

    # a is 1.2
    var a = absf(-1.2)

classref-item-separator

classref-method

`int<class_int>` **absi**(x: `int<class_int>`) `🔗<class_@GlobalScope_method_absi>`

Returns the absolute value of int parameter `x` (i.e. positive value).

    # a is 1
    var a = absi(-1)

classref-item-separator

classref-method

`float<class_float>` **acos**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_acos>`

Returns the arc cosine of `x` in radians. Use to get the angle of cosine `x`. `x` will be clamped between `-1.0` and `1.0` (inclusive), in order to prevent `acos()<class_@GlobalScope_method_acos>` from returning `@GDScript.NAN<class_@GDScript_constant_NAN>`.

    # c is 0.523599 or 30 degrees if converted with rad_to_deg(c)
    var c = acos(0.866025)

classref-item-separator

classref-method

`float<class_float>` **acosh**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_acosh>`

Returns the hyperbolic arc (also called inverse) cosine of `x`, returning a value in radians. Use it to get the angle from an angle's cosine in hyperbolic space if `x` is larger or equal to 1. For values of `x` lower than 1, it will return 0, in order to prevent `acosh()<class_@GlobalScope_method_acosh>` from returning `@GDScript.NAN<class_@GDScript_constant_NAN>`.

    var a = acosh(2) # Returns 1.31695789692482
    cosh(a) # Returns 2

    var b = acosh(-1) # Returns 0

classref-item-separator

classref-method

`float<class_float>` **angle_difference**(from: `float<class_float>`, to: `float<class_float>`) `🔗<class_@GlobalScope_method_angle_difference>`

Returns the difference between the two angles (in radians), in the range of `[-PI, +PI]`. When `from` and `to` are opposite, returns `-PI` if `from` is smaller than `to`, or `PI` otherwise.

classref-item-separator

classref-method

`float<class_float>` **asin**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_asin>`

Returns the arc sine of `x` in radians. Use to get the angle of sine `x`. `x` will be clamped between `-1.0` and `1.0` (inclusive), in order to prevent `asin()<class_@GlobalScope_method_asin>` from returning `@GDScript.NAN<class_@GDScript_constant_NAN>`.

    # s is 0.523599 or 30 degrees if converted with rad_to_deg(s)
    var s = asin(0.5)

classref-item-separator

classref-method

`float<class_float>` **asinh**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_asinh>`

Returns the hyperbolic arc (also called inverse) sine of `x`, returning a value in radians. Use it to get the angle from an angle's sine in hyperbolic space.

    var a = asinh(0.9) # Returns 0.8088669356527824
    sinh(a) # Returns 0.9

classref-item-separator

classref-method

`float<class_float>` **atan**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_atan>`

Returns the arc tangent of `x` in radians. Use it to get the angle from an angle's tangent in trigonometry.

The method cannot know in which quadrant the angle should fall. See `atan2()<class_@GlobalScope_method_atan2>` if you have both `y` and `x`.

    var a = atan(0.5) # a is 0.463648

If `x` is between `-PI / 2` and `PI / 2` (inclusive), `atan(tan(x))` is equal to `x`.

classref-item-separator

classref-method

`float<class_float>` **atan2**(y: `float<class_float>`, x: `float<class_float>`) `🔗<class_@GlobalScope_method_atan2>`

Returns the arc tangent of `y/x` in radians. Use to get the angle of tangent `y/x`. To compute the value, the method takes into account the sign of both arguments in order to determine the quadrant.

Important note: The Y coordinate comes first, by convention.

    var a = atan2(0, -1) # a is 3.141593

classref-item-separator

classref-method

`float<class_float>` **atanh**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_atanh>`

Returns the hyperbolic arc (also called inverse) tangent of `x`, returning a value in radians. Use it to get the angle from an angle's tangent in hyperbolic space if `x` is between -1 and 1 (non-inclusive).

In mathematics, the inverse hyperbolic tangent is only defined for -1 \< `x` \< 1 in the real set, so values equal or lower to -1 for `x` return negative `@GDScript.INF<class_@GDScript_constant_INF>` and values equal or higher than 1 return positive `@GDScript.INF<class_@GDScript_constant_INF>` in order to prevent `atanh()<class_@GlobalScope_method_atanh>` from returning `@GDScript.NAN<class_@GDScript_constant_NAN>`.

    var a = atanh(0.9) # Returns 1.47221948958322
    tanh(a) # Returns 0.9

    var b = atanh(-2) # Returns -inf
    tanh(b) # Returns -1

classref-item-separator

classref-method

`float<class_float>` **bezier_derivative**(start: `float<class_float>`, control_1: `float<class_float>`, control_2: `float<class_float>`, end: `float<class_float>`, t: `float<class_float>`) `🔗<class_@GlobalScope_method_bezier_derivative>`

Returns the derivative at the given `t` on a one-dimensional [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by the given `control_1`, `control_2`, and `end` points.

classref-item-separator

classref-method

`float<class_float>` **bezier_interpolate**(start: `float<class_float>`, control_1: `float<class_float>`, control_2: `float<class_float>`, end: `float<class_float>`, t: `float<class_float>`) `🔗<class_@GlobalScope_method_bezier_interpolate>`

Returns the point at the given `t` on a one-dimensional [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) defined by the given `control_1`, `control_2`, and `end` points.

classref-item-separator

classref-method

`Variant<class_Variant>` **bytes_to_var**(bytes: `PackedByteArray<class_PackedByteArray>`) `🔗<class_@GlobalScope_method_bytes_to_var>`

Decodes a byte array back to a `Variant<class_Variant>` value, without decoding objects.

**Note:** If you need object deserialization, see `bytes_to_var_with_objects()<class_@GlobalScope_method_bytes_to_var_with_objects>`.

classref-item-separator

classref-method

`Variant<class_Variant>` **bytes_to_var_with_objects**(bytes: `PackedByteArray<class_PackedByteArray>`) `🔗<class_@GlobalScope_method_bytes_to_var_with_objects>`

Decodes a byte array back to a `Variant<class_Variant>` value. Decoding objects is allowed.

**Warning:** Deserialized object can contain code which gets executed. Do not use this option if the serialized object comes from untrusted sources to avoid potential security threats (remote code execution).

classref-item-separator

classref-method

`Variant<class_Variant>` **ceil**(x: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_ceil>`

Rounds `x` upward (towards positive infinity), returning the smallest whole number that is not less than `x`. Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`.

    var i = ceil(1.45) # i is 2.0
    i = ceil(1.001)    # i is 2.0

See also `floor()<class_@GlobalScope_method_floor>`, `round()<class_@GlobalScope_method_round>`, and `snapped()<class_@GlobalScope_method_snapped>`.

**Note:** For better type safety, use `ceilf()<class_@GlobalScope_method_ceilf>`, `ceili()<class_@GlobalScope_method_ceili>`, `Vector2.ceil()<class_Vector2_method_ceil>`, `Vector3.ceil()<class_Vector3_method_ceil>`, or `Vector4.ceil()<class_Vector4_method_ceil>`.

classref-item-separator

classref-method

`float<class_float>` **ceilf**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_ceilf>`

Rounds `x` upward (towards positive infinity), returning the smallest whole number that is not less than `x`.

A type-safe version of `ceil()<class_@GlobalScope_method_ceil>`, returning a `float<class_float>`.

classref-item-separator

classref-method

`int<class_int>` **ceili**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_ceili>`

Rounds `x` upward (towards positive infinity), returning the smallest whole number that is not less than `x`.

A type-safe version of `ceil()<class_@GlobalScope_method_ceil>`, returning an `int<class_int>`.

classref-item-separator

classref-method

`Variant<class_Variant>` **clamp**(value: `Variant<class_Variant>`, min: `Variant<class_Variant>`, max: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_clamp>`

Clamps the `value`, returning a `Variant<class_Variant>` not less than `min` and not more than `max`. Any values that can be compared with the less than and greater than operators will work.

    var a = clamp(-10, -1, 5)
    # a is -1

    var b = clamp(8.1, 0.9, 5.5)
    # b is 5.5

**Note:** For better type safety, use `clampf()<class_@GlobalScope_method_clampf>`, `clampi()<class_@GlobalScope_method_clampi>`, `Vector2.clamp()<class_Vector2_method_clamp>`, `Vector2i.clamp()<class_Vector2i_method_clamp>`, `Vector3.clamp()<class_Vector3_method_clamp>`, `Vector3i.clamp()<class_Vector3i_method_clamp>`, `Vector4.clamp()<class_Vector4_method_clamp>`, `Vector4i.clamp()<class_Vector4i_method_clamp>`, or `Color.clamp()<class_Color_method_clamp>` (not currently supported by this method).

**Note:** When using this on vectors it will *not* perform component-wise clamping, and will pick `min` if `value < min` or `max` if `value > max`. To perform component-wise clamping use the methods listed above.

classref-item-separator

classref-method

`float<class_float>` **clampf**(value: `float<class_float>`, min: `float<class_float>`, max: `float<class_float>`) `🔗<class_@GlobalScope_method_clampf>`

Clamps the `value`, returning a `float<class_float>` not less than `min` and not more than `max`.

    var speed = 42.1
    var a = clampf(speed, 1.0, 20.5) # a is 20.5

    speed = -10.0
    var b = clampf(speed, -1.0, 1.0) # b is -1.0

classref-item-separator

classref-method

`int<class_int>` **clampi**(value: `int<class_int>`, min: `int<class_int>`, max: `int<class_int>`) `🔗<class_@GlobalScope_method_clampi>`

Clamps the `value`, returning an `int<class_int>` not less than `min` and not more than `max`.

    var speed = 42
    var a = clampi(speed, 1, 20) # a is 20

    speed = -10
    var b = clampi(speed, -1, 1) # b is -1

classref-item-separator

classref-method

`float<class_float>` **cos**(angle_rad: `float<class_float>`) `🔗<class_@GlobalScope_method_cos>`

Returns the cosine of angle `angle_rad` in radians.

    cos(PI * 2)         # Returns 1.0
    cos(PI)             # Returns -1.0
    cos(deg_to_rad(90)) # Returns 0.0

classref-item-separator

classref-method

`float<class_float>` **cosh**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_cosh>`

Returns the hyperbolic cosine of `x` in radians.

    print(cosh(1)) # Prints 1.543081

classref-item-separator

classref-method

`float<class_float>` **cubic_interpolate**(from: `float<class_float>`, to: `float<class_float>`, pre: `float<class_float>`, post: `float<class_float>`, weight: `float<class_float>`) `🔗<class_@GlobalScope_method_cubic_interpolate>`

Cubic interpolates between two values by the factor defined in `weight` with `pre` and `post` values.

classref-item-separator

classref-method

`float<class_float>` **cubic_interpolate_angle**(from: `float<class_float>`, to: `float<class_float>`, pre: `float<class_float>`, post: `float<class_float>`, weight: `float<class_float>`) `🔗<class_@GlobalScope_method_cubic_interpolate_angle>`

Cubic interpolates between two rotation values with shortest path by the factor defined in `weight` with `pre` and `post` values. See also `lerp_angle()<class_@GlobalScope_method_lerp_angle>`.

classref-item-separator

classref-method

`float<class_float>` **cubic_interpolate_angle_in_time**(from: `float<class_float>`, to: `float<class_float>`, pre: `float<class_float>`, post: `float<class_float>`, weight: `float<class_float>`, to_t: `float<class_float>`, pre_t: `float<class_float>`, post_t: `float<class_float>`) `🔗<class_@GlobalScope_method_cubic_interpolate_angle_in_time>`

Cubic interpolates between two rotation values with shortest path by the factor defined in `weight` with `pre` and `post` values. See also `lerp_angle()<class_@GlobalScope_method_lerp_angle>`.

It can perform smoother interpolation than `cubic_interpolate()<class_@GlobalScope_method_cubic_interpolate>` by the time values.

classref-item-separator

classref-method

`float<class_float>` **cubic_interpolate_in_time**(from: `float<class_float>`, to: `float<class_float>`, pre: `float<class_float>`, post: `float<class_float>`, weight: `float<class_float>`, to_t: `float<class_float>`, pre_t: `float<class_float>`, post_t: `float<class_float>`) `🔗<class_@GlobalScope_method_cubic_interpolate_in_time>`

Cubic interpolates between two values by the factor defined in `weight` with `pre` and `post` values.

It can perform smoother interpolation than `cubic_interpolate()<class_@GlobalScope_method_cubic_interpolate>` by the time values.

classref-item-separator

classref-method

`float<class_float>` **db_to_linear**(db: `float<class_float>`) `🔗<class_@GlobalScope_method_db_to_linear>`

Converts from decibels to linear energy (audio).

classref-item-separator

classref-method

`float<class_float>` **deg_to_rad**(deg: `float<class_float>`) `🔗<class_@GlobalScope_method_deg_to_rad>`

Converts an angle expressed in degrees to radians.

    var r = deg_to_rad(180) # r is 3.141593

classref-item-separator

classref-method

`float<class_float>` **ease**(x: `float<class_float>`, curve: `float<class_float>`) `🔗<class_@GlobalScope_method_ease>`

Returns an "eased" value of `x` based on an easing function defined with `curve`. This easing function is based on an exponent. The `curve` can be any floating-point number, with specific values leading to the following behaviors:

``` text
- Lower than -1.0 (exclusive): Ease in-out
- -1.0: Linear
- Between -1.0 and 0.0 (exclusive): Ease out-in
- 0.0: Constant
- Between 0.0 to 1.0 (exclusive): Ease out
- 1.0: Linear
- Greater than 1.0 (exclusive): Ease in
```

[ease() curve values cheatsheet](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/ease_cheatsheet.png)

See also `smoothstep()<class_@GlobalScope_method_smoothstep>`. If you need to perform more advanced transitions, use `Tween.interpolate_value()<class_Tween_method_interpolate_value>`.

classref-item-separator

classref-method

`String<class_String>` **error_string**(error: `int<class_int>`) `🔗<class_@GlobalScope_method_error_string>`

Returns a human-readable name for the given `Error<enum_@GlobalScope_Error>` code.

    print(OK)                              # Prints 0
    print(error_string(OK))                # Prints "OK"
    print(error_string(ERR_BUSY))          # Prints "Busy"
    print(error_string(ERR_OUT_OF_MEMORY)) # Prints "Out of memory"

classref-item-separator

classref-method

`float<class_float>` **exp**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_exp>`

The natural exponential function. It raises the mathematical constant *e* to the power of `x` and returns it.

*e* has an approximate value of 2.71828, and can be obtained with `exp(1)`.

For exponents to other bases use the method `pow()<class_@GlobalScope_method_pow>`.

    var a = exp(2) # Approximately 7.39

classref-item-separator

classref-method

`Variant<class_Variant>` **floor**(x: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_floor>`

Rounds `x` downward (towards negative infinity), returning the largest whole number that is not more than `x`. Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`.

    var a = floor(2.99) # a is 2.0
    a = floor(-2.99)    # a is -3.0

See also `ceil()<class_@GlobalScope_method_ceil>`, `round()<class_@GlobalScope_method_round>`, and `snapped()<class_@GlobalScope_method_snapped>`.

**Note:** For better type safety, use `floorf()<class_@GlobalScope_method_floorf>`, `floori()<class_@GlobalScope_method_floori>`, `Vector2.floor()<class_Vector2_method_floor>`, `Vector3.floor()<class_Vector3_method_floor>`, or `Vector4.floor()<class_Vector4_method_floor>`.

classref-item-separator

classref-method

`float<class_float>` **floorf**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_floorf>`

Rounds `x` downward (towards negative infinity), returning the largest whole number that is not more than `x`.

A type-safe version of `floor()<class_@GlobalScope_method_floor>`, returning a `float<class_float>`.

classref-item-separator

classref-method

`int<class_int>` **floori**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_floori>`

Rounds `x` downward (towards negative infinity), returning the largest whole number that is not more than `x`.

A type-safe version of `floor()<class_@GlobalScope_method_floor>`, returning an `int<class_int>`.

**Note:** This function is *not* the same as `int(x)`, which rounds towards 0.

classref-item-separator

classref-method

`float<class_float>` **fmod**(x: `float<class_float>`, y: `float<class_float>`) `🔗<class_@GlobalScope_method_fmod>`

Returns the floating-point remainder of `x` divided by `y`, keeping the sign of `x`.

    var remainder = fmod(7, 5.5) # remainder is 1.5

For the integer remainder operation, use the `%` operator.

classref-item-separator

classref-method

`float<class_float>` **fposmod**(x: `float<class_float>`, y: `float<class_float>`) `🔗<class_@GlobalScope_method_fposmod>`

Returns the floating-point modulus of `x` divided by `y`, wrapping equally in positive and negative.

    print(" (x)  (fmod(x, 1.5))   (fposmod(x, 1.5))")
    for i in 7:
        var x = i * 0.5 - 1.5
        print("%4.1f           %4.1f  | %4.1f" % [x, fmod(x, 1.5), fposmod(x, 1.5)])

Prints:

``` text
(x)  (fmod(x, 1.5))   (fposmod(x, 1.5))
-1.5           -0.0  |  0.0
-1.0           -1.0  |  0.5
-0.5           -0.5  |  1.0
0.0            0.0  |  0.0
0.5            0.5  |  0.5
1.0            1.0  |  1.0
1.5            0.0  |  0.0
```

classref-item-separator

classref-method

`int<class_int>` **hash**(variable: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_hash>`

Returns the integer hash of the passed `variable`.

gdscript

print(hash("a")) \# Prints 177670

csharp

GD.Print(GD.Hash("a")); // Prints 177670

classref-item-separator

classref-method

`Object<class_Object>` **instance_from_id**(instance_id: `int<class_int>`) `🔗<class_@GlobalScope_method_instance_from_id>`

Returns the `Object<class_Object>` that corresponds to `instance_id`. All Objects have a unique instance ID. See also `Object.get_instance_id()<class_Object_method_get_instance_id>`.

gdscript

var drink = "water"

func ready():
var id = get_instance_id() var instance = instance_from_id(id) print(instance.drink) \# Prints "water"

csharp

public partial class MyNode : Node { public string Drink { get; set; } = "water";

> public override void Ready() { ulong id = GetInstanceId(); var instance = (MyNode)InstanceFromId(Id); GD.Print(instance.Drink); // Prints "water" }

}

classref-item-separator

classref-method

`float<class_float>` **inverse_lerp**(from: `float<class_float>`, to: `float<class_float>`, weight: `float<class_float>`) `🔗<class_@GlobalScope_method_inverse_lerp>`

Returns an interpolation or extrapolation factor considering the range specified in `from` and `to`, and the interpolated value specified in `weight`. The returned value will be between `0.0` and `1.0` if `weight` is between `from` and `to` (inclusive). If `weight` is located outside this range, then an extrapolation factor will be returned (return value lower than `0.0` or greater than `1.0`). Use `clamp()<class_@GlobalScope_method_clamp>` on the result of `inverse_lerp()<class_@GlobalScope_method_inverse_lerp>` if this is not desired.

    # The interpolation ratio in the `lerp()` call below is 0.75.
    var middle = lerp(20, 30, 0.75)
    # middle is now 27.5.

    # Now, we pretend to have forgotten the original ratio and want to get it back.
    var ratio = inverse_lerp(20, 30, 27.5)
    # ratio is now 0.75.

See also `lerp()<class_@GlobalScope_method_lerp>`, which performs the reverse of this operation, and `remap()<class_@GlobalScope_method_remap>` to map a continuous series of values to another.

classref-item-separator

classref-method

`bool<class_bool>` **is_equal_approx**(a: `float<class_float>`, b: `float<class_float>`) `🔗<class_@GlobalScope_method_is_equal_approx>`

Returns `true` if `a` and `b` are approximately equal to each other.

Here, "approximately equal" means that `a` and `b` are within a small internal epsilon of each other, which scales with the magnitude of the numbers.

Infinity values of the same sign are considered equal.

classref-item-separator

classref-method

`bool<class_bool>` **is_finite**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_is_finite>`

Returns whether `x` is a finite value, i.e. it is not `@GDScript.NAN<class_@GDScript_constant_NAN>`, positive infinity, or negative infinity. See also `is_inf()<class_@GlobalScope_method_is_inf>` and `is_nan()<class_@GlobalScope_method_is_nan>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_inf**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_is_inf>`

Returns `true` if `x` is either positive infinity or negative infinity. See also `is_finite()<class_@GlobalScope_method_is_finite>` and `is_nan()<class_@GlobalScope_method_is_nan>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_instance_id_valid**(id: `int<class_int>`) `🔗<class_@GlobalScope_method_is_instance_id_valid>`

Returns `true` if the Object that corresponds to `id` is a valid object (e.g. has not been deleted from memory). All Objects have a unique instance ID.

classref-item-separator

classref-method

`bool<class_bool>` **is_instance_valid**(instance: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_is_instance_valid>`

Returns `true` if `instance` is a valid Object (e.g. has not been deleted from memory).

classref-item-separator

classref-method

`bool<class_bool>` **is_nan**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_is_nan>`

Returns `true` if `x` is a NaN ("Not a Number" or invalid) value. This method is needed as `@GDScript.NAN<class_@GDScript_constant_NAN>` is not equal to itself, which means `x == NAN` can't be used to check whether a value is a NaN.

classref-item-separator

classref-method

`bool<class_bool>` **is_same**(a: `Variant<class_Variant>`, b: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_is_same>`

Returns `true`, for value types, if `a` and `b` share the same value. Returns `true`, for reference types, if the references of `a` and `b` are the same.

    # Vector2 is a value type
    var vec2_a = Vector2(0, 0)
    var vec2_b = Vector2(0, 0)
    var vec2_c = Vector2(1, 1)
    is_same(vec2_a, vec2_a)  # true
    is_same(vec2_a, vec2_b)  # true
    is_same(vec2_a, vec2_c)  # false

    # Array is a reference type
    var arr_a = []
    var arr_b = []
    is_same(arr_a, arr_a)  # true
    is_same(arr_a, arr_b)  # false

These are `Variant<class_Variant>` value types: `null`, `bool<class_bool>`, `int<class_int>`, `float<class_float>`, `String<class_String>`, `StringName<class_StringName>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`, `Rect2<class_Rect2>`, `Rect2i<class_Rect2i>`, `Transform2D<class_Transform2D>`, `Transform3D<class_Transform3D>`, `Plane<class_Plane>`, `Quaternion<class_Quaternion>`, `AABB<class_AABB>`, `Basis<class_Basis>`, `Projection<class_Projection>`, `Color<class_Color>`, `NodePath<class_NodePath>`, `RID<class_RID>`, `Callable<class_Callable>` and `Signal<class_Signal>`.

These are `Variant<class_Variant>` reference types: `Object<class_Object>`, `Dictionary<class_Dictionary>`, `Array<class_Array>`, `PackedByteArray<class_PackedByteArray>`, `PackedInt32Array<class_PackedInt32Array>`, `PackedInt64Array<class_PackedInt64Array>`, `PackedFloat32Array<class_PackedFloat32Array>`, `PackedFloat64Array<class_PackedFloat64Array>`, `PackedStringArray<class_PackedStringArray>`, `PackedVector2Array<class_PackedVector2Array>`, `PackedVector3Array<class_PackedVector3Array>`, `PackedVector4Array<class_PackedVector4Array>`, and `PackedColorArray<class_PackedColorArray>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_zero_approx**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_is_zero_approx>`

Returns `true` if `x` is zero or almost zero. The comparison is done using a tolerance calculation with a small internal epsilon.

This function is faster than using `is_equal_approx()<class_@GlobalScope_method_is_equal_approx>` with one value as zero.

classref-item-separator

classref-method

`Variant<class_Variant>` **lerp**(from: `Variant<class_Variant>`, to: `Variant<class_Variant>`, weight: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_lerp>`

Linearly interpolates between two values by the factor defined in `weight`. To perform interpolation, `weight` should be between `0.0` and `1.0` (inclusive). However, values outside this range are allowed and can be used to perform *extrapolation*. If this is not desired, use `clampf()<class_@GlobalScope_method_clampf>` to limit `weight`.

Both `from` and `to` must be the same type. Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector3<class_Vector3>`, `Vector4<class_Vector4>`, `Color<class_Color>`, `Quaternion<class_Quaternion>`, `Basis<class_Basis>`, `Transform2D<class_Transform2D>`, `Transform3D<class_Transform3D>`.

    lerp(0, 4, 0.75) # Returns 3.0

See also `inverse_lerp()<class_@GlobalScope_method_inverse_lerp>` which performs the reverse of this operation. To perform eased interpolation with `lerp()<class_@GlobalScope_method_lerp>`, combine it with `ease()<class_@GlobalScope_method_ease>` or `smoothstep()<class_@GlobalScope_method_smoothstep>`. See also `remap()<class_@GlobalScope_method_remap>` to map a continuous series of values to another.

**Note:** For better type safety, use `lerpf()<class_@GlobalScope_method_lerpf>`, `Vector2.lerp()<class_Vector2_method_lerp>`, `Vector3.lerp()<class_Vector3_method_lerp>`, `Vector4.lerp()<class_Vector4_method_lerp>`, `Color.lerp()<class_Color_method_lerp>`, `Quaternion.slerp()<class_Quaternion_method_slerp>`, `Basis.slerp()<class_Basis_method_slerp>`, `Transform2D.interpolate_with()<class_Transform2D_method_interpolate_with>`, or `Transform3D.interpolate_with()<class_Transform3D_method_interpolate_with>`.

classref-item-separator

classref-method

`float<class_float>` **lerp_angle**(from: `float<class_float>`, to: `float<class_float>`, weight: `float<class_float>`) `🔗<class_@GlobalScope_method_lerp_angle>`

Linearly interpolates between two angles (in radians) by a `weight` value between 0.0 and 1.0.

Similar to `lerp()<class_@GlobalScope_method_lerp>`, but interpolates correctly when the angles wrap around `@GDScript.TAU<class_@GDScript_constant_TAU>`. To perform eased interpolation with `lerp_angle()<class_@GlobalScope_method_lerp_angle>`, combine it with `ease()<class_@GlobalScope_method_ease>` or `smoothstep()<class_@GlobalScope_method_smoothstep>`.

    extends Sprite
    var elapsed = 0.0
    func _process(delta):
        var min_angle = deg_to_rad(0.0)
        var max_angle = deg_to_rad(90.0)
        rotation = lerp_angle(min_angle, max_angle, elapsed)
        elapsed += delta

**Note:** This function lerps through the shortest path between `from` and `to`. However, when these two angles are approximately `PI + k * TAU` apart for any integer `k`, it's not obvious which way they lerp due to floating-point precision errors. For example, `lerp_angle(0, PI, weight)` lerps counter-clockwise, while `lerp_angle(0, PI + 5 * TAU, weight)` lerps clockwise.

classref-item-separator

classref-method

`float<class_float>` **lerpf**(from: `float<class_float>`, to: `float<class_float>`, weight: `float<class_float>`) `🔗<class_@GlobalScope_method_lerpf>`

Linearly interpolates between two values by the factor defined in `weight`. To perform interpolation, `weight` should be between `0.0` and `1.0` (inclusive). However, values outside this range are allowed and can be used to perform *extrapolation*. If this is not desired, use `clampf()<class_@GlobalScope_method_clampf>` on the result of this function.

    lerpf(0, 4, 0.75) # Returns 3.0

See also `inverse_lerp()<class_@GlobalScope_method_inverse_lerp>` which performs the reverse of this operation. To perform eased interpolation with `lerp()<class_@GlobalScope_method_lerp>`, combine it with `ease()<class_@GlobalScope_method_ease>` or `smoothstep()<class_@GlobalScope_method_smoothstep>`.

classref-item-separator

classref-method

`float<class_float>` **linear_to_db**(lin: `float<class_float>`) `🔗<class_@GlobalScope_method_linear_to_db>`

Converts from linear energy to decibels (audio). Since volume is not normally linear, this can be used to implement volume sliders that behave as expected.

**Example:** Change the Master bus's volume through a `Slider<class_Slider>` node, which ranges from `0.0` to `1.0`:

    AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), linear_to_db($Slider.value))

classref-item-separator

classref-method

`float<class_float>` **log**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_log>`

Returns the [natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm) of `x` (base [e](https://en.wikipedia.org/wiki/E_(mathematical_constant)), with *e* being approximately 2.71828). This is the amount of time needed to reach a certain level of continuous growth.

**Note:** This is not the same as the "log" function on most calculators, which uses a base 10 logarithm. To use base 10 logarithm, use `log(x) / log(10)`.

    log(10) # Returns 2.302585

**Note:** The logarithm of `0` returns `-inf`, while negative values return `-nan`.

classref-item-separator

classref-method

`Variant<class_Variant>` **max**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_max>`

Returns the maximum of the given numeric values. This function can take any number of arguments.

    max(1, 7, 3, -6, 5) # Returns 7

**Note:** When using this on vectors it will *not* perform component-wise maximum, and will pick the largest value when compared using `x < y`. To perform component-wise maximum, use `Vector2.max()<class_Vector2_method_max>`, `Vector2i.max()<class_Vector2i_method_max>`, `Vector3.max()<class_Vector3_method_max>`, `Vector3i.max()<class_Vector3i_method_max>`, `Vector4.max()<class_Vector4_method_max>`, and `Vector4i.max()<class_Vector4i_method_max>`.

classref-item-separator

classref-method

`float<class_float>` **maxf**(a: `float<class_float>`, b: `float<class_float>`) `🔗<class_@GlobalScope_method_maxf>`

Returns the maximum of two `float<class_float>` values.

    maxf(3.6, 24)   # Returns 24.0
    maxf(-3.99, -4) # Returns -3.99

classref-item-separator

classref-method

`int<class_int>` **maxi**(a: `int<class_int>`, b: `int<class_int>`) `🔗<class_@GlobalScope_method_maxi>`

Returns the maximum of two `int<class_int>` values.

    maxi(1, 2)   # Returns 2
    maxi(-3, -4) # Returns -3

classref-item-separator

classref-method

`Variant<class_Variant>` **min**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_min>`

Returns the minimum of the given numeric values. This function can take any number of arguments.

    min(1, 7, 3, -6, 5) # Returns -6

**Note:** When using this on vectors it will *not* perform component-wise minimum, and will pick the smallest value when compared using `x < y`. To perform component-wise minimum, use `Vector2.min()<class_Vector2_method_min>`, `Vector2i.min()<class_Vector2i_method_min>`, `Vector3.min()<class_Vector3_method_min>`, `Vector3i.min()<class_Vector3i_method_min>`, `Vector4.min()<class_Vector4_method_min>`, and `Vector4i.min()<class_Vector4i_method_min>`.

classref-item-separator

classref-method

`float<class_float>` **minf**(a: `float<class_float>`, b: `float<class_float>`) `🔗<class_@GlobalScope_method_minf>`

Returns the minimum of two `float<class_float>` values.

    minf(3.6, 24)   # Returns 3.6
    minf(-3.99, -4) # Returns -4.0

classref-item-separator

classref-method

`int<class_int>` **mini**(a: `int<class_int>`, b: `int<class_int>`) `🔗<class_@GlobalScope_method_mini>`

Returns the minimum of two `int<class_int>` values.

    mini(1, 2)   # Returns 1
    mini(-3, -4) # Returns -4

classref-item-separator

classref-method

`float<class_float>` **move_toward**(from: `float<class_float>`, to: `float<class_float>`, delta: `float<class_float>`) `🔗<class_@GlobalScope_method_move_toward>`

Moves `from` toward `to` by the `delta` amount. Will not go past `to`.

Use a negative `delta` value to move away.

    move_toward(5, 10, 4)    # Returns 9
    move_toward(10, 5, 4)    # Returns 6
    move_toward(5, 10, 9)    # Returns 10
    move_toward(10, 5, -1.5) # Returns 11.5

classref-item-separator

classref-method

`int<class_int>` **nearest_po2**(value: `int<class_int>`) `🔗<class_@GlobalScope_method_nearest_po2>`

Returns the smallest integer power of 2 that is greater than or equal to `value`.

    nearest_po2(3) # Returns 4
    nearest_po2(4) # Returns 4
    nearest_po2(5) # Returns 8

    nearest_po2(0)  # Returns 0 (this may not be expected)
    nearest_po2(-1) # Returns 0 (this may not be expected)

**Warning:** Due to its implementation, this method returns `0` rather than `1` for values less than or equal to `0`, with an exception for `value` being the smallest negative 64-bit integer (`-9223372036854775808`) in which case the `value` is returned unchanged.

classref-item-separator

classref-method

`float<class_float>` **pingpong**(value: `float<class_float>`, length: `float<class_float>`) `🔗<class_@GlobalScope_method_pingpong>`

Wraps `value` between `0` and the `length`. If the limit is reached, the next value the function returns is decreased to the `0` side or increased to the `length` side (like a triangle wave). If `length` is less than zero, it becomes positive.

    pingpong(-3.0, 3.0) # Returns 3.0
    pingpong(-2.0, 3.0) # Returns 2.0
    pingpong(-1.0, 3.0) # Returns 1.0
    pingpong(0.0, 3.0)  # Returns 0.0
    pingpong(1.0, 3.0)  # Returns 1.0
    pingpong(2.0, 3.0)  # Returns 2.0
    pingpong(3.0, 3.0)  # Returns 3.0
    pingpong(4.0, 3.0)  # Returns 2.0
    pingpong(5.0, 3.0)  # Returns 1.0
    pingpong(6.0, 3.0)  # Returns 0.0

classref-item-separator

classref-method

`int<class_int>` **posmod**(x: `int<class_int>`, y: `int<class_int>`) `🔗<class_@GlobalScope_method_posmod>`

Returns the integer modulus of `x` divided by `y` that wraps equally in positive and negative.

    print("#(i)  (i % 3)   (posmod(i, 3))")
    for i in range(-3, 4):
        print("%2d       %2d  | %2d" % [i, i % 3, posmod(i, 3)])

Prints:

``` text
(i)  (i % 3)   (posmod(i, 3))
-3        0  |  0
-2       -2  |  1
-1       -1  |  2
 0        0  |  0
 1        1  |  1
 2        2  |  2
 3        0  |  0
```

classref-item-separator

classref-method

`float<class_float>` **pow**(base: `float<class_float>`, exp: `float<class_float>`) `🔗<class_@GlobalScope_method_pow>`

Returns the result of `base` raised to the power of `exp`.

In GDScript, this is the equivalent of the `**` operator.

    pow(2, 5)   # Returns 32.0
    pow(4, 1.5) # Returns 8.0

classref-item-separator

classref-method

`void (No return value.)` **print**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_print>`

Converts one or more arguments of any type to string in the best way possible and prints them to the console.

gdscript

var a = \[1, 2, 3\] print("a", "b", a) \# Prints "ab\[1, 2, 3\]"

csharp

Godot.Collections.Array a = \[1, 2, 3\]; GD.Print("a", "b", a); // Prints "ab\[1, 2, 3\]"

**Note:** Consider using `push_error()<class_@GlobalScope_method_push_error>` and `push_warning()<class_@GlobalScope_method_push_warning>` to print error and warning messages instead of `print()<class_@GlobalScope_method_print>` or `print_rich()<class_@GlobalScope_method_print_rich>`. This distinguishes them from print messages used for debugging purposes, while also displaying a stack trace when an error or warning is printed. See also `Engine.print_to_stdout<class_Engine_property_print_to_stdout>` and `ProjectSettings.application/run/disable_stdout<class_ProjectSettings_property_application/run/disable_stdout>`.

classref-item-separator

classref-method

`void (No return value.)` **print_rich**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_print_rich>`

Converts one or more arguments of any type to string in the best way possible and prints them to the console.

The following BBCode tags are supported: `b`, `i`, `u`, `s`, `indent`, `code`, `url`, `center`, `right`, `color`, `bgcolor`, `fgcolor`.

URL tags only support URLs wrapped by a URL tag, not URLs with a different title.

When printing to standard output, the supported subset of BBCode is converted to ANSI escape codes for the terminal emulator to display. Support for ANSI escape codes varies across terminal emulators, especially for italic and strikethrough. In standard output, `code` is represented with faint text but without any font change. Unsupported tags are left as-is in standard output.

gdscript

print_rich("\[color=green\]\[b\]Hello world\![/b\]\[/color\]") \# Prints "Hello world!", in green with a bold font.

csharp

GD.PrintRich("\[color=green\]\[b\]Hello world\![/b\]\[/color\]"); // Prints "Hello world!", in green with a bold font.

**Note:** Consider using `push_error()<class_@GlobalScope_method_push_error>` and `push_warning()<class_@GlobalScope_method_push_warning>` to print error and warning messages instead of `print()<class_@GlobalScope_method_print>` or `print_rich()<class_@GlobalScope_method_print_rich>`. This distinguishes them from print messages used for debugging purposes, while also displaying a stack trace when an error or warning is printed.

**Note:** Output displayed in the editor supports clickable `[url=address]text[/url]` tags. The `[url]` tag's `address` value is handled by `OS.shell_open()<class_OS_method_shell_open>` when clicked.

classref-item-separator

classref-method

`void (No return value.)` **print_verbose**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_print_verbose>`

If verbose mode is enabled (`OS.is_stdout_verbose()<class_OS_method_is_stdout_verbose>` returning `true`), converts one or more arguments of any type to string in the best way possible and prints them to the console.

classref-item-separator

classref-method

`void (No return value.)` **printerr**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_printerr>`

Prints one or more arguments to strings in the best way possible to standard error line.

gdscript

printerr("prints to stderr")

csharp

GD.PrintErr("prints to stderr");

classref-item-separator

classref-method

`void (No return value.)` **printraw**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_printraw>`

Prints one or more arguments to strings in the best way possible to the OS terminal. Unlike `print()<class_@GlobalScope_method_print>`, no newline is automatically added at the end.

**Note:** The OS terminal is *not* the same as the editor's Output dock. The output sent to the OS terminal can be seen when running Godot from a terminal. On Windows, this requires using the `console.exe` executable.

gdscript

\# Prints "ABC" to terminal. printraw("A") printraw("B") printraw("C")

csharp

// Prints "ABC" to terminal. GD.PrintRaw("A"); GD.PrintRaw("B"); GD.PrintRaw("C");

classref-item-separator

classref-method

`void (No return value.)` **prints**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_prints>`

Prints one or more arguments to the console with a space between each argument.

gdscript

prints("A", "B", "C") \# Prints "A B C"

csharp

GD.PrintS("A", "B", "C"); // Prints "A B C"

classref-item-separator

classref-method

`void (No return value.)` **printt**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_printt>`

Prints one or more arguments to the console with a tab between each argument.

gdscript

printt("A", "B", "C") \# Prints "A B C"

csharp

GD.PrintT("A", "B", "C"); // Prints "A B C"

classref-item-separator

classref-method

`void (No return value.)` **push_error**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_push_error>`

Pushes an error message to Godot's built-in debugger and to the OS terminal.

gdscript

push_error("test error") \# Prints "test error" to debugger and terminal as an error.

csharp

GD.PushError("test error"); // Prints "test error" to debugger and terminal as an error.

**Note:** This function does not pause project execution. To print an error message and pause project execution in debug builds, use `assert(false, "test error")` instead.

classref-item-separator

classref-method

`void (No return value.)` **push_warning**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_push_warning>`

Pushes a warning message to Godot's built-in debugger and to the OS terminal.

gdscript

push_warning("test warning") \# Prints "test warning" to debugger and terminal as a warning.

csharp

GD.PushWarning("test warning"); // Prints "test warning" to debugger and terminal as a warning.

classref-item-separator

classref-method

`float<class_float>` **rad_to_deg**(rad: `float<class_float>`) `🔗<class_@GlobalScope_method_rad_to_deg>`

Converts an angle expressed in radians to degrees.

    rad_to_deg(0.523599) # Returns 30
    rad_to_deg(PI)       # Returns 180
    rad_to_deg(PI * 2)   # Returns 360

classref-item-separator

classref-method

`PackedInt64Array<class_PackedInt64Array>` **rand_from_seed**(seed: `int<class_int>`) `🔗<class_@GlobalScope_method_rand_from_seed>`

Given a `seed`, returns a `PackedInt64Array<class_PackedInt64Array>` of size `2`, where its first element is the randomized `int<class_int>` value, and the second element is the same as `seed`. Passing the same `seed` consistently returns the same array.

**Note:** "Seed" here refers to the internal state of the pseudo random number generator, currently implemented as a 64 bit integer.

    var a = rand_from_seed(4)

    print(a[0]) # Prints 2879024997
    print(a[1]) # Prints 4

classref-item-separator

classref-method

`float<class_float>` **randf**() `🔗<class_@GlobalScope_method_randf>`

Returns a random floating-point value between `0.0` and `1.0` (inclusive).

gdscript

randf() \# Returns e.g. 0.375671

csharp

GD.Randf(); // Returns e.g. 0.375671

classref-item-separator

classref-method

`float<class_float>` **randf_range**(from: `float<class_float>`, to: `float<class_float>`) `🔗<class_@GlobalScope_method_randf_range>`

Returns a random floating-point value between `from` and `to` (inclusive).

gdscript

randf_range(0, 20.5) \# Returns e.g. 7.45315 randf_range(-10, 10) \# Returns e.g. -3.844535

csharp

GD.RandRange(0.0, 20.5); // Returns e.g. 7.45315 GD.RandRange(-10.0, 10.0); // Returns e.g. -3.844535

classref-item-separator

classref-method

`float<class_float>` **randfn**(mean: `float<class_float>`, deviation: `float<class_float>`) `🔗<class_@GlobalScope_method_randfn>`

Returns a [normally-distributed](https://en.wikipedia.org/wiki/Normal_distribution), pseudo-random floating-point value from the specified `mean` and a standard `deviation`. This is also known as a Gaussian distribution.

**Note:** This method uses the [Box-Muller transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform) algorithm.

classref-item-separator

classref-method

`int<class_int>` **randi**() `🔗<class_@GlobalScope_method_randi>`

Returns a random unsigned 32-bit integer. Use remainder to obtain a random value in the interval `[0, N - 1]` (where N is smaller than 2^32).

gdscript

randi() \# Returns random integer between 0 and 2^32 - 1 randi() % 20 \# Returns random integer between 0 and 19 randi() % 100 \# Returns random integer between 0 and 99 randi() % 100 + 1 \# Returns random integer between 1 and 100

csharp

GD.Randi(); // Returns random integer between 0 and 2^32 - 1 GD.Randi() % 20; // Returns random integer between 0 and 19 GD.Randi() % 100; // Returns random integer between 0 and 99 GD.Randi() % 100 + 1; // Returns random integer between 1 and 100

classref-item-separator

classref-method

`int<class_int>` **randi_range**(from: `int<class_int>`, to: `int<class_int>`) `🔗<class_@GlobalScope_method_randi_range>`

Returns a random signed 32-bit integer between `from` and `to` (inclusive). If `to` is lesser than `from`, they are swapped.

gdscript

randi_range(0, 1) \# Returns either 0 or 1 randi_range(-10, 1000) \# Returns random integer between -10 and 1000

csharp

GD.RandRange(0, 1); // Returns either 0 or 1 GD.RandRange(-10, 1000); // Returns random integer between -10 and 1000

classref-item-separator

classref-method

`void (No return value.)` **randomize**() `🔗<class_@GlobalScope_method_randomize>`

Randomizes the seed (or the internal state) of the random number generator. The current implementation uses a number based on the device's time.

**Note:** This function is called automatically when the project is run. If you need to fix the seed to have consistent, reproducible results, use `seed()<class_@GlobalScope_method_seed>` to initialize the random number generator.

classref-item-separator

classref-method

`float<class_float>` **remap**(value: `float<class_float>`, istart: `float<class_float>`, istop: `float<class_float>`, ostart: `float<class_float>`, ostop: `float<class_float>`) `🔗<class_@GlobalScope_method_remap>`

Maps a `value` from range `[istart, istop]` to `[ostart, ostop]`. See also `lerp()<class_@GlobalScope_method_lerp>` and `inverse_lerp()<class_@GlobalScope_method_inverse_lerp>`. If `value` is outside `[istart, istop]`, then the resulting value will also be outside `[ostart, ostop]`. If this is not desired, use `clamp()<class_@GlobalScope_method_clamp>` on the result of this function.

    remap(75, 0, 100, -1, 1) # Returns 0.5

For complex use cases where multiple ranges are needed, consider using `Curve<class_Curve>` or `Gradient<class_Gradient>` instead.

**Note:** If `istart == istop`, the return value is undefined (most likely NaN, INF, or -INF).

classref-item-separator

classref-method

`int<class_int>` **rid_allocate_id**() `🔗<class_@GlobalScope_method_rid_allocate_id>`

Allocates a unique ID which can be used by the implementation to construct an RID. This is used mainly from native extensions to implement servers.

classref-item-separator

classref-method

`RID<class_RID>` **rid_from_int64**(base: `int<class_int>`) `🔗<class_@GlobalScope_method_rid_from_int64>`

Creates an RID from a `base`. This is used mainly from native extensions to build servers.

classref-item-separator

classref-method

`float<class_float>` **rotate_toward**(from: `float<class_float>`, to: `float<class_float>`, delta: `float<class_float>`) `🔗<class_@GlobalScope_method_rotate_toward>`

Rotates `from` toward `to` by the `delta` amount. Will not go past `to`.

Similar to `move_toward()<class_@GlobalScope_method_move_toward>`, but interpolates correctly when the angles wrap around `@GDScript.TAU<class_@GDScript_constant_TAU>`.

If `delta` is negative, this function will rotate away from `to`, toward the opposite angle, and will not go past the opposite angle.

classref-item-separator

classref-method

`Variant<class_Variant>` **round**(x: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_round>`

Rounds `x` to the nearest whole number, with halfway cases rounded away from 0. Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`.

    round(2.4) # Returns 2
    round(2.5) # Returns 3
    round(2.6) # Returns 3

See also `floor()<class_@GlobalScope_method_floor>`, `ceil()<class_@GlobalScope_method_ceil>`, and `snapped()<class_@GlobalScope_method_snapped>`.

**Note:** For better type safety, use `roundf()<class_@GlobalScope_method_roundf>`, `roundi()<class_@GlobalScope_method_roundi>`, `Vector2.round()<class_Vector2_method_round>`, `Vector3.round()<class_Vector3_method_round>`, or `Vector4.round()<class_Vector4_method_round>`.

classref-item-separator

classref-method

`float<class_float>` **roundf**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_roundf>`

Rounds `x` to the nearest whole number, with halfway cases rounded away from 0.

A type-safe version of `round()<class_@GlobalScope_method_round>`, returning a `float<class_float>`.

classref-item-separator

classref-method

`int<class_int>` **roundi**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_roundi>`

Rounds `x` to the nearest whole number, with halfway cases rounded away from 0.

A type-safe version of `round()<class_@GlobalScope_method_round>`, returning an `int<class_int>`.

classref-item-separator

classref-method

`void (No return value.)` **seed**(base: `int<class_int>`) `🔗<class_@GlobalScope_method_seed>`

Sets the seed for the random number generator to `base`. Setting the seed manually can ensure consistent, repeatable results for most random functions.

gdscript

var my_seed = "Godot Rocks".hash() seed(my_seed) var a = randf() + randi() seed(my_seed) var b = randf() + randi() \# a and b are now identical

csharp

ulong mySeed = (ulong)GD.Hash("Godot Rocks"); GD.Seed(mySeed); var a = GD.Randf() + GD.Randi(); GD.Seed(mySeed); var b = GD.Randf() + GD.Randi(); // a and b are now identical

classref-item-separator

classref-method

`Variant<class_Variant>` **sign**(x: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_sign>`

Returns the same type of `Variant<class_Variant>` as `x`, with `-1` for negative values, `1` for positive values, and `0` for zeros. For `nan` values it returns 0.

Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`.

    sign(-6.0) # Returns -1
    sign(0.0)  # Returns 0
    sign(6.0)  # Returns 1
    sign(NAN)  # Returns 0

    sign(Vector3(-6.0, 0.0, 6.0)) # Returns (-1, 0, 1)

**Note:** For better type safety, use `signf()<class_@GlobalScope_method_signf>`, `signi()<class_@GlobalScope_method_signi>`, `Vector2.sign()<class_Vector2_method_sign>`, `Vector2i.sign()<class_Vector2i_method_sign>`, `Vector3.sign()<class_Vector3_method_sign>`, `Vector3i.sign()<class_Vector3i_method_sign>`, `Vector4.sign()<class_Vector4_method_sign>`, or `Vector4i.sign()<class_Vector4i_method_sign>`.

classref-item-separator

classref-method

`float<class_float>` **signf**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_signf>`

Returns `-1.0` if `x` is negative, `1.0` if `x` is positive, and `0.0` if `x` is zero. For `nan` values of `x` it returns 0.0.

    signf(-6.5) # Returns -1.0
    signf(0.0)  # Returns 0.0
    signf(6.5)  # Returns 1.0
    signf(NAN)  # Returns 0.0

classref-item-separator

classref-method

`int<class_int>` **signi**(x: `int<class_int>`) `🔗<class_@GlobalScope_method_signi>`

Returns `-1` if `x` is negative, `1` if `x` is positive, and `0` if `x` is zero.

    signi(-6) # Returns -1
    signi(0)  # Returns 0
    signi(6)  # Returns 1

classref-item-separator

classref-method

`float<class_float>` **sin**(angle_rad: `float<class_float>`) `🔗<class_@GlobalScope_method_sin>`

Returns the sine of angle `angle_rad` in radians.

    sin(0.523599)       # Returns 0.5
    sin(deg_to_rad(90)) # Returns 1.0

classref-item-separator

classref-method

`float<class_float>` **sinh**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_sinh>`

Returns the hyperbolic sine of `x`.

    var a = log(2.0) # Returns 0.693147
    sinh(a) # Returns 0.75

classref-item-separator

classref-method

`float<class_float>` **smoothstep**(from: `float<class_float>`, to: `float<class_float>`, x: `float<class_float>`) `🔗<class_@GlobalScope_method_smoothstep>`

Returns a smooth cubic Hermite interpolation between `0` and `1`.

For positive ranges (when `from <= to`) the return value is `0` when `x <= from`, and `1` when `x >= to`. If `x` lies between `from` and `to`, the return value follows an S-shaped curve that smoothly transitions from `0` to `1`.

For negative ranges (when `from > to`) the function is mirrored and returns `1` when `x <= to` and `0` when `x >= from`.

This S-shaped curve is the cubic Hermite interpolator, given by `f(y) = 3*y^2 - 2*y^3` where `y = (x-from) / (to-from)`.

    smoothstep(0, 2, -5.0) # Returns 0.0
    smoothstep(0, 2, 0.5) # Returns 0.15625
    smoothstep(0, 2, 1.0) # Returns 0.5
    smoothstep(0, 2, 2.0) # Returns 1.0

Compared to `ease()<class_@GlobalScope_method_ease>` with a curve value of `-1.6521`, `smoothstep()<class_@GlobalScope_method_smoothstep>` returns the smoothest possible curve with no sudden changes in the derivative. If you need to perform more advanced transitions, use `Tween<class_Tween>` or `AnimationPlayer<class_AnimationPlayer>`.

[Comparison between smoothstep() and ease(x, -1.6521) return values](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/smoothstep_ease_comparison.png)

[Smoothstep() return values with positive, zero, and negative ranges](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/smoothstep_range.webp)

classref-item-separator

classref-method

`Variant<class_Variant>` **snapped**(x: `Variant<class_Variant>`, step: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_snapped>`

Returns the multiple of `step` that is the closest to `x`. This can also be used to round a floating-point number to an arbitrary number of decimals.

The returned value is the same type of `Variant<class_Variant>` as `step`. Supported types: `int<class_int>`, `float<class_float>`, `Vector2<class_Vector2>`, `Vector2i<class_Vector2i>`, `Vector3<class_Vector3>`, `Vector3i<class_Vector3i>`, `Vector4<class_Vector4>`, `Vector4i<class_Vector4i>`.

    snapped(100, 32)  # Returns 96
    snapped(3.14159, 0.01)  # Returns 3.14

    snapped(Vector2(34, 70), Vector2(8, 8))  # Returns (32, 72)

See also `ceil()<class_@GlobalScope_method_ceil>`, `floor()<class_@GlobalScope_method_floor>`, and `round()<class_@GlobalScope_method_round>`.

**Note:** For better type safety, use `snappedf()<class_@GlobalScope_method_snappedf>`, `snappedi()<class_@GlobalScope_method_snappedi>`, `Vector2.snapped()<class_Vector2_method_snapped>`, `Vector2i.snapped()<class_Vector2i_method_snapped>`, `Vector3.snapped()<class_Vector3_method_snapped>`, `Vector3i.snapped()<class_Vector3i_method_snapped>`, `Vector4.snapped()<class_Vector4_method_snapped>`, or `Vector4i.snapped()<class_Vector4i_method_snapped>`.

classref-item-separator

classref-method

`float<class_float>` **snappedf**(x: `float<class_float>`, step: `float<class_float>`) `🔗<class_@GlobalScope_method_snappedf>`

Returns the multiple of `step` that is the closest to `x`. This can also be used to round a floating-point number to an arbitrary number of decimals.

A type-safe version of `snapped()<class_@GlobalScope_method_snapped>`, returning a `float<class_float>`.

    snappedf(32.0, 2.5)  # Returns 32.5
    snappedf(3.14159, 0.01)  # Returns 3.14

classref-item-separator

classref-method

`int<class_int>` **snappedi**(x: `float<class_float>`, step: `int<class_int>`) `🔗<class_@GlobalScope_method_snappedi>`

Returns the multiple of `step` that is the closest to `x`.

A type-safe version of `snapped()<class_@GlobalScope_method_snapped>`, returning an `int<class_int>`.

    snappedi(53, 16)  # Returns 48
    snappedi(4096, 100)  # Returns 4100

classref-item-separator

classref-method

`float<class_float>` **sqrt**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_sqrt>`

Returns the square root of `x`, where `x` is a non-negative number.

    sqrt(9)     # Returns 3
    sqrt(10.24) # Returns 3.2
    sqrt(-1)    # Returns NaN

**Note:** Negative values of `x` return NaN ("Not a Number"). In C#, if you need negative inputs, use `System.Numerics.Complex`.

classref-item-separator

classref-method

`int<class_int>` **step_decimals**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_step_decimals>`

Returns the position of the first non-zero digit, after the decimal point. Note that the maximum return value is 10, which is a design decision in the implementation.

    var n = step_decimals(5)       # n is 0
    n = step_decimals(1.0005)      # n is 4
    n = step_decimals(0.000000005) # n is 9

classref-item-separator

classref-method

`String<class_String>` **str**(...) `vararg (This method accepts any number of arguments after the ones described here.)` `🔗<class_@GlobalScope_method_str>`

Converts one or more arguments of any `Variant<class_Variant>` type to a `String<class_String>` in the best way possible.

    var a = [10, 20, 30]
    var b = str(a)
    print(len(a)) # Prints 3 (the number of elements in the array).
    print(len(b)) # Prints 12 (the length of the string "[10, 20, 30]").

classref-item-separator

classref-method

`Variant<class_Variant>` **str_to_var**(string: `String<class_String>`) `🔗<class_@GlobalScope_method_str_to_var>`

Converts a formatted `string` that was returned by `var_to_str()<class_@GlobalScope_method_var_to_str>` to the original `Variant<class_Variant>`.

gdscript

var data = '{ "a": 1, "b": 2 }' \# data is a String var dict = str_to_var(data) \# dict is a Dictionary print(dict\["a"\]) \# Prints 1

csharp

string data = "{ "a": 1, "b": 2 }"; // data is a string var dict = GD.StrToVar(data).AsGodotDictionary(); // dict is a Dictionary GD.Print(dict\["a"\]); // Prints 1

classref-item-separator

classref-method

`float<class_float>` **tan**(angle_rad: `float<class_float>`) `🔗<class_@GlobalScope_method_tan>`

Returns the tangent of angle `angle_rad` in radians.

    tan(deg_to_rad(45)) # Returns 1

classref-item-separator

classref-method

`float<class_float>` **tanh**(x: `float<class_float>`) `🔗<class_@GlobalScope_method_tanh>`

Returns the hyperbolic tangent of `x`.

    var a = log(2.0) # Returns 0.693147
    tanh(a)          # Returns 0.6

classref-item-separator

classref-method

`Variant<class_Variant>` **type_convert**(variant: `Variant<class_Variant>`, type: `int<class_int>`) `🔗<class_@GlobalScope_method_type_convert>`

Converts the given `variant` to the given `type`, using the `Variant.Type<enum_@GlobalScope_Variant.Type>` values. This method is generous with how it handles types, it can automatically convert between array types, convert numeric `String<class_String>`s to `int<class_int>`, and converting most things to `String<class_String>`.

If the type conversion cannot be done, this method will return the default value for that type, for example converting `Rect2<class_Rect2>` to `Vector2<class_Vector2>` will always return `Vector2.ZERO<class_Vector2_constant_ZERO>`. This method will never show error messages as long as `type` is a valid Variant type.

The returned value is a `Variant<class_Variant>`, but the data inside and its type will be the same as the requested type.

    type_convert("Hi!", TYPE_INT) # Returns 0
    type_convert("123", TYPE_INT) # Returns 123
    type_convert(123.4, TYPE_INT) # Returns 123
    type_convert(5, TYPE_VECTOR2) # Returns (0, 0)
    type_convert("Hi!", TYPE_NIL) # Returns null

classref-item-separator

classref-method

`String<class_String>` **type_string**(type: `int<class_int>`) `🔗<class_@GlobalScope_method_type_string>`

Returns a human-readable name of the given `type`, using the `Variant.Type<enum_@GlobalScope_Variant.Type>` values.

    print(TYPE_INT) # Prints 2
    print(type_string(TYPE_INT)) # Prints "int"
    print(type_string(TYPE_STRING)) # Prints "String"

See also `typeof()<class_@GlobalScope_method_typeof>`.

classref-item-separator

classref-method

`int<class_int>` **typeof**(variable: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_typeof>`

Returns the internal type of the given `variable`, using the `Variant.Type<enum_@GlobalScope_Variant.Type>` values.

    var json = JSON.new()
    json.parse('["a", "b", "c"]')
    var result = json.get_data()
    if typeof(result) == TYPE_ARRAY:
        print(result[0]) # Prints "a"
    else:
        print("Unexpected result!")

See also `type_string()<class_@GlobalScope_method_type_string>`.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **var_to_bytes**(variable: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_var_to_bytes>`

Encodes a `Variant<class_Variant>` value to a byte array, without encoding objects. Deserialization can be done with `bytes_to_var()<class_@GlobalScope_method_bytes_to_var>`.

**Note:** If you need object serialization, see `var_to_bytes_with_objects()<class_@GlobalScope_method_var_to_bytes_with_objects>`.

**Note:** Encoding `Callable<class_Callable>` is not supported and will result in an empty value, regardless of the data.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **var_to_bytes_with_objects**(variable: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_var_to_bytes_with_objects>`

Encodes a `Variant<class_Variant>` value to a byte array. Encoding objects is allowed (and can potentially include executable code). Deserialization can be done with `bytes_to_var_with_objects()<class_@GlobalScope_method_bytes_to_var_with_objects>`.

**Note:** Encoding `Callable<class_Callable>` is not supported and will result in an empty value, regardless of the data.

classref-item-separator

classref-method

`String<class_String>` **var_to_str**(variable: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_var_to_str>`

Converts a `Variant<class_Variant>` `variable` to a formatted `String<class_String>` that can then be parsed using `str_to_var()<class_@GlobalScope_method_str_to_var>`.

gdscript

var a = { "a": 1, "b": 2 } print(var_to_str(a))

csharp

var a = new Godot.Collections.Dictionary { \["a"\] = 1, \["b"\] = 2 }; GD.Print(GD.VarToStr(a));

Prints:

``` text
{
    "a": 1,
    "b": 2
}
```

**Note:** Converting `Signal<class_Signal>` or `Callable<class_Callable>` is not supported and will result in an empty value for these types, regardless of their data.

classref-item-separator

classref-method

`Variant<class_Variant>` **weakref**(obj: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_weakref>`

Returns a `WeakRef<class_WeakRef>` instance holding a weak reference to `obj`. Returns an empty `WeakRef<class_WeakRef>` instance if `obj` is `null`. Prints an error and returns `null` if `obj` is neither `Object<class_Object>`-derived nor `null`.

A weak reference to an object is not enough to keep the object alive: when the only remaining references to a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something else. However, until the object is actually destroyed the weak reference may return the object even if there are no strong references to it.

classref-item-separator

classref-method

`Variant<class_Variant>` **wrap**(value: `Variant<class_Variant>`, min: `Variant<class_Variant>`, max: `Variant<class_Variant>`) `🔗<class_@GlobalScope_method_wrap>`

Wraps the `Variant<class_Variant>` `value` between `min` and `max`. `min` is *inclusive* while `max` is *exclusive*. This can be used for creating loop-like behavior or infinite surfaces.

Variant types `int<class_int>` and `float<class_float>` are supported. If any of the arguments is `float<class_float>`, this function returns a `float<class_float>`, otherwise it returns an `int<class_int>`.

    var a = wrap(4, 5, 10)
    # a is 9 (int)

    var a = wrap(7, 5, 10)
    # a is 7 (int)

    var a = wrap(10.5, 5, 10)
    # a is 5.5 (float)

classref-item-separator

classref-method

`float<class_float>` **wrapf**(value: `float<class_float>`, min: `float<class_float>`, max: `float<class_float>`) `🔗<class_@GlobalScope_method_wrapf>`

Wraps the float `value` between `min` and `max`. `min` is *inclusive* while `max` is *exclusive*. This can be used for creating loop-like behavior or infinite surfaces.

    # Infinite loop between 5.0 and 9.9
    value = wrapf(value + 0.1, 5.0, 10.0)

    # Infinite rotation (in radians)
    angle = wrapf(angle + 0.1, 0.0, TAU)

    # Infinite rotation (in radians)
    angle = wrapf(angle + 0.1, -PI, PI)

**Note:** If `min` is `0`, this is equivalent to `fposmod()<class_@GlobalScope_method_fposmod>`, so prefer using that instead. `wrapf()<class_@GlobalScope_method_wrapf>` is more flexible than using the `fposmod()<class_@GlobalScope_method_fposmod>` approach by giving the user control over the minimum value.

classref-item-separator

classref-method

`int<class_int>` **wrapi**(value: `int<class_int>`, min: `int<class_int>`, max: `int<class_int>`) `🔗<class_@GlobalScope_method_wrapi>`

Wraps the integer `value` between `min` and `max`. `min` is *inclusive* while `max` is *exclusive*. This can be used for creating loop-like behavior or infinite surfaces.

    # Infinite loop between 5 and 9
    frame = wrapi(frame + 1, 5, 10)

    # result is -2
    var result = wrapi(-6, -5, -1)