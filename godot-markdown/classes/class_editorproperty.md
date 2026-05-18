github_url
hide

# EditorProperty

**Inherits:** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Custom control for editing properties that can be added to the `EditorInspector<class_EditorInspector>`.

classref-introduction-group

## Description

A custom control for editing properties that can be added to the `EditorInspector<class_EditorInspector>`. It is added via `EditorInspectorPlugin<class_EditorInspectorPlugin>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**multiple_properties_changed**(properties: `PackedStringArray<class_PackedStringArray>`, value: `Array<class_Array>`) `🔗<class_EditorProperty_signal_multiple_properties_changed>`

Emit it if you want multiple properties modified at the same time. Do not use if added via `EditorInspectorPlugin._parse_property()<class_EditorInspectorPlugin_private_method__parse_property>`.

classref-item-separator

classref-signal

**object_id_selected**(property: `StringName<class_StringName>`, id: `int<class_int>`) `🔗<class_EditorProperty_signal_object_id_selected>`

Used by sub-inspectors. Emit it if what was selected was an Object ID.

classref-item-separator

classref-signal

**property_can_revert_changed**(property: `StringName<class_StringName>`, can_revert: `bool<class_bool>`) `🔗<class_EditorProperty_signal_property_can_revert_changed>`

Emitted when the revertability (i.e., whether it has a non-default value and thus is displayed with a revert icon) of a property has changed.

classref-item-separator

classref-signal

**property_changed**(property: `StringName<class_StringName>`, value: `Variant<class_Variant>`, field: `StringName<class_StringName>`, changing: `bool<class_bool>`) `🔗<class_EditorProperty_signal_property_changed>`

Do not emit this manually, use the `emit_changed()<class_EditorProperty_method_emit_changed>` method instead.

classref-item-separator

classref-signal

**property_checked**(property: `StringName<class_StringName>`, checked: `bool<class_bool>`) `🔗<class_EditorProperty_signal_property_checked>`

Emitted when a property was checked. Used internally.

classref-item-separator

classref-signal

**property_deleted**(property: `StringName<class_StringName>`) `🔗<class_EditorProperty_signal_property_deleted>`

Emitted when a property was deleted. Used internally.

classref-item-separator

classref-signal

**property_favorited**(property: `StringName<class_StringName>`, favorited: `bool<class_bool>`) `🔗<class_EditorProperty_signal_property_favorited>`

Emit it if you want to mark a property as favorited, making it appear at the top of the inspector.

classref-item-separator

classref-signal

**property_keyed**(property: `StringName<class_StringName>`) `🔗<class_EditorProperty_signal_property_keyed>`

Emit it if you want to add this value as an animation key (check for keying being enabled first).

classref-item-separator

classref-signal

**property_keyed_with_value**(property: `StringName<class_StringName>`, value: `Variant<class_Variant>`) `🔗<class_EditorProperty_signal_property_keyed_with_value>`

Emit it if you want to key a property with a single value.

classref-item-separator

classref-signal

**property_overridden**() `🔗<class_EditorProperty_signal_property_overridden>`

Emitted when a setting override for the current project is requested.

classref-item-separator

classref-signal

**property_pinned**(property: `StringName<class_StringName>`, pinned: `bool<class_bool>`) `🔗<class_EditorProperty_signal_property_pinned>`

Emit it if you want to mark (or unmark) the value of a property for being saved regardless of being equal to the default value.

The default value is the one the property will get when the node is just instantiated and can come from an ancestor scene in the inheritance/instantiation chain, a script or a builtin class.

classref-item-separator

classref-signal

**resource_selected**(path: `String<class_String>`, resource: `Resource<class_Resource>`) `🔗<class_EditorProperty_signal_resource_selected>`

If you want a sub-resource to be edited, emit this signal with the resource.

classref-item-separator

classref-signal

**selected**(path: `String<class_String>`, focusable_idx: `int<class_int>`) `🔗<class_EditorProperty_signal_selected>`

Emitted when selected. Used internally.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **checkable** = `false` `🔗<class_EditorProperty_property_checkable>`

classref-property-setget

- `void (No return value.)` **set_checkable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_checkable**()

Used by the inspector, set to `true` when the property is checkable.

classref-item-separator

classref-property

`bool<class_bool>` **checked** = `false` `🔗<class_EditorProperty_property_checked>`

classref-property-setget

- `void (No return value.)` **set_checked**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_checked**()

Used by the inspector, set to `true` when the property is checked.

classref-item-separator

classref-property

`bool<class_bool>` **deletable** = `false` `🔗<class_EditorProperty_property_deletable>`

classref-property-setget

- `void (No return value.)` **set_deletable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_deletable**()

Used by the inspector, set to `true` when the property can be deleted by the user.

classref-item-separator

classref-property

`bool<class_bool>` **draw_background** = `true` `🔗<class_EditorProperty_property_draw_background>`

classref-property-setget

- `void (No return value.)` **set_draw_background**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_draw_background**()

Used by the inspector, set to `true` when the property background is drawn.

classref-item-separator

classref-property

`bool<class_bool>` **draw_label** = `true` `🔗<class_EditorProperty_property_draw_label>`

classref-property-setget

- `void (No return value.)` **set_draw_label**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_draw_label**()

Used by the inspector, set to `true` when the property label is drawn.

classref-item-separator

classref-property

`bool<class_bool>` **draw_warning** = `false` `🔗<class_EditorProperty_property_draw_warning>`

classref-property-setget

- `void (No return value.)` **set_draw_warning**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_draw_warning**()

Used by the inspector, set to `true` when the property is drawn with the editor theme's warning color. This is used for editable children's properties.

classref-item-separator

classref-property

`bool<class_bool>` **keying** = `false` `🔗<class_EditorProperty_property_keying>`

classref-property-setget

- `void (No return value.)` **set_keying**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_keying**()

Used by the inspector, set to `true` when the property can add keys for animation.

classref-item-separator

classref-property

`String<class_String>` **label** = `""` `🔗<class_EditorProperty_property_label>`

classref-property-setget

- `void (No return value.)` **set_label**(value: `String<class_String>`)
- `String<class_String>` **get_label**()

Set this property to change the label (if you want to show one).

classref-item-separator

classref-property

`float<class_float>` **name_split_ratio** = `0.5` `🔗<class_EditorProperty_property_name_split_ratio>`

classref-property-setget

- `void (No return value.)` **set_name_split_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_name_split_ratio**()

Space distribution ratio between the label and the editing field.

classref-item-separator

classref-property

`bool<class_bool>` **read_only** = `false` `🔗<class_EditorProperty_property_read_only>`

classref-property-setget

- `void (No return value.)` **set_read_only**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_read_only**()

Used by the inspector, set to `true` when the property is read-only.

classref-item-separator

classref-property

`bool<class_bool>` **selectable** = `true` `🔗<class_EditorProperty_property_selectable>`

classref-property-setget

- `void (No return value.)` **set_selectable**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_selectable**()

Used by the inspector, set to `true` when the property is selectable.

classref-item-separator

classref-property

`bool<class_bool>` **use_folding** = `false` `🔗<class_EditorProperty_property_use_folding>`

classref-property-setget

- `void (No return value.)` **set_use_folding**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_folding**()

Used by the inspector, set to `true` when the property is using folding.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_set_read_only**(read_only: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorProperty_private_method__set_read_only>`

Called when the read-only status of the property is changed. It may be used to change custom controls into a read-only or modifiable state.

classref-item-separator

classref-method

`void (No return value.)` **\_update_property**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorProperty_private_method__update_property>`

When this virtual function is called, you must update your editor.

classref-item-separator

classref-method

`void (No return value.)` **add_focusable**(control: `Control<class_Control>`) `🔗<class_EditorProperty_method_add_focusable>`

If any of the controls added can gain keyboard focus, add it here. This ensures that focus will be restored if the inspector is refreshed.

classref-item-separator

classref-method

`void (No return value.)` **deselect**() `🔗<class_EditorProperty_method_deselect>`

Draw property as not selected. Used by the inspector.

classref-item-separator

classref-method

`void (No return value.)` **emit_changed**(property: `StringName<class_StringName>`, value: `Variant<class_Variant>`, field: `StringName<class_StringName>` = &"", changing: `bool<class_bool>` = false) `🔗<class_EditorProperty_method_emit_changed>`

If one or several properties have changed, this must be called. `field` is used in case your editor can modify fields separately (as an example, Vector3.x). The `changing` argument avoids the editor requesting this property to be refreshed (leave as `false` if unsure).

classref-item-separator

classref-method

`Object<class_Object>` **get_edited_object**() `🔗<class_EditorProperty_method_get_edited_object>`

Returns the edited object.

**Note:** This method could return `null` if the editor has not yet been associated with a property. However, in `_update_property()<class_EditorProperty_private_method__update_property>` and `_set_read_only()<class_EditorProperty_private_method__set_read_only>`, this value is *guaranteed* to be non-`null`.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_edited_property**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorProperty_method_get_edited_property>`

Returns the edited property. If your editor is for a single property (added via `EditorInspectorPlugin._parse_property()<class_EditorInspectorPlugin_private_method__parse_property>`), then this will return the property.

**Note:** This method could return `null` if the editor has not yet been associated with a property. However, in `_update_property()<class_EditorProperty_private_method__update_property>` and `_set_read_only()<class_EditorProperty_private_method__set_read_only>`, this value is *guaranteed* to be non-`null`.

classref-item-separator

classref-method

`bool<class_bool>` **is_selected**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorProperty_method_is_selected>`

Returns `true` if property is drawn as selected. Used by the inspector.

classref-item-separator

classref-method

`void (No return value.)` **select**(focusable: `int<class_int>` = -1) `🔗<class_EditorProperty_method_select>`

Draw property as selected. Used by the inspector.

classref-item-separator

classref-method

`void (No return value.)` **set_bottom_editor**(editor: `Control<class_Control>`) `🔗<class_EditorProperty_method_set_bottom_editor>`

Puts the `editor` control below the property label. The control must be previously added using `Node.add_child()<class_Node_method_add_child>`.

classref-item-separator

classref-method

`void (No return value.)` **set_label_reference**(control: `Control<class_Control>`) `🔗<class_EditorProperty_method_set_label_reference>`

Used by the inspector, set to a control that will be used as a reference to calculate the size of the label.

classref-item-separator

classref-method

`void (No return value.)` **set_object_and_property**(object: `Object<class_Object>`, property: `StringName<class_StringName>`) `🔗<class_EditorProperty_method_set_object_and_property>`

Assigns object and property to edit.

classref-item-separator

classref-method

`void (No return value.)` **update_property**() `🔗<class_EditorProperty_method_update_property>`

Forces a refresh of the property display.