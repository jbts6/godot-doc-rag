github_url
hide

# InputEventScreenDrag

**Inherits:** `InputEventFromWindow<class_InputEventFromWindow>` **\<** `InputEvent<class_InputEvent>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Represents a screen drag event.

classref-introduction-group

## Description

Stores information about screen drag events. See `Node._input()<class_Node_private_method__input>`.

classref-introduction-group

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **index** = `0` `🔗<class_InputEventScreenDrag_property_index>`

classref-property-setget

- `void (No return value.)` **set_index**(value: `int<class_int>`)
- `int<class_int>` **get_index**()

The drag event index in the case of a multi-drag event.

classref-item-separator

classref-property

`bool<class_bool>` **pen_inverted** = `false` `🔗<class_InputEventScreenDrag_property_pen_inverted>`

classref-property-setget

- `void (No return value.)` **set_pen_inverted**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_pen_inverted**()

Returns `true` when using the eraser end of a stylus pen.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **position** = `Vector2(0, 0)` `🔗<class_InputEventScreenDrag_property_position>`

classref-property-setget

- `void (No return value.)` **set_position**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_position**()

The drag position in the viewport the node is in, using the coordinate system of this viewport.

classref-item-separator

classref-property

`float<class_float>` **pressure** = `0.0` `🔗<class_InputEventScreenDrag_property_pressure>`

classref-property-setget

- `void (No return value.)` **set_pressure**(value: `float<class_float>`)
- `float<class_float>` **get_pressure**()

Represents the pressure the user puts on the pen. Ranges from `0.0` to `1.0`.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **relative** = `Vector2(0, 0)` `🔗<class_InputEventScreenDrag_property_relative>`

classref-property-setget

- `void (No return value.)` **set_relative**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_relative**()

The drag position relative to the previous position (position at the last frame).

**Note:** `relative<class_InputEventScreenDrag_property_relative>` is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using `relative<class_InputEventScreenDrag_property_relative>` in a script that handles touch aiming. To avoid this, use `screen_relative<class_InputEventScreenDrag_property_screen_relative>` instead.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **screen_relative** = `Vector2(0, 0)` `🔗<class_InputEventScreenDrag_property_screen_relative>`

classref-property-setget

- `void (No return value.)` **set_screen_relative**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_screen_relative**()

The unscaled drag position relative to the previous position in screen coordinates (position at the last frame). This position is *not* scaled according to the content scale factor or calls to `InputEvent.xformed_by()<class_InputEvent_method_xformed_by>`. This should be preferred over `relative<class_InputEventScreenDrag_property_relative>` for touch aiming regardless of the project's stretch mode.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **screen_velocity** = `Vector2(0, 0)` `🔗<class_InputEventScreenDrag_property_screen_velocity>`

classref-property-setget

- `void (No return value.)` **set_screen_velocity**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_screen_velocity**()

The unscaled drag velocity in pixels per second in screen coordinates. This velocity is *not* scaled according to the content scale factor or calls to `InputEvent.xformed_by()<class_InputEvent_method_xformed_by>`. This should be preferred over `velocity<class_InputEventScreenDrag_property_velocity>` for touch aiming regardless of the project's stretch mode.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **tilt** = `Vector2(0, 0)` `🔗<class_InputEventScreenDrag_property_tilt>`

classref-property-setget

- `void (No return value.)` **set_tilt**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_tilt**()

Represents the angles of tilt of the pen. Positive X-coordinate value indicates a tilt to the right. Positive Y-coordinate value indicates a tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **velocity** = `Vector2(0, 0)` `🔗<class_InputEventScreenDrag_property_velocity>`

classref-property-setget

- `void (No return value.)` **set_velocity**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_velocity**()

The drag velocity.

**Note:** `velocity<class_InputEventScreenDrag_property_velocity>` is automatically scaled according to the content scale factor, which is defined by the project's stretch mode settings. This means touch sensitivity will appear different depending on resolution when using `velocity<class_InputEventScreenDrag_property_velocity>` in a script that handles touch aiming. To avoid this, use `screen_velocity<class_InputEventScreenDrag_property_screen_velocity>` instead.