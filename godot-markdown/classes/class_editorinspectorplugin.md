github_url
hide

# EditorInspectorPlugin

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Plugin for adding custom property editors on the inspector.

classref-introduction-group

## Description

**EditorInspectorPlugin** allows adding custom property editors to `EditorInspector<class_EditorInspector>`.

When an object is edited, the `_can_handle()<class_EditorInspectorPlugin_private_method__can_handle>` function is called and must return `true` if the object type is supported.

If supported, the function `_parse_begin()<class_EditorInspectorPlugin_private_method__parse_begin>` will be called, allowing to place custom controls at the beginning of the class.

Subsequently, the `_parse_category()<class_EditorInspectorPlugin_private_method__parse_category>` and `_parse_property()<class_EditorInspectorPlugin_private_method__parse_property>` are called for every category and property. They offer the ability to add custom controls to the inspector too.

Finally, `_parse_end()<class_EditorInspectorPlugin_private_method__parse_end>` will be called.

On each of these calls, the "add" functions can be called.

To use **EditorInspectorPlugin**, register it using the `EditorPlugin.add_inspector_plugin()<class_EditorPlugin_method_add_inspector_plugin>` method first.

classref-introduction-group

## Tutorials

- `Inspector plugins <../tutorials/plugins/editor/inspector_plugins>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **\_can_handle**(object: `Object<class_Object>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorInspectorPlugin_private_method__can_handle>`

Returns `true` if this object can be handled by this plugin.

classref-item-separator

classref-method

`void (No return value.)` **\_parse_begin**(object: `Object<class_Object>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorInspectorPlugin_private_method__parse_begin>`

Called to allow adding controls at the beginning of the property list for `object`.

classref-item-separator

classref-method

`void (No return value.)` **\_parse_category**(object: `Object<class_Object>`, category: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorInspectorPlugin_private_method__parse_category>`

Called to allow adding controls at the beginning of a category in the property list for `object`.

classref-item-separator

classref-method

`void (No return value.)` **\_parse_end**(object: `Object<class_Object>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorInspectorPlugin_private_method__parse_end>`

Called to allow adding controls at the end of the property list for `object`.

classref-item-separator

classref-method

`void (No return value.)` **\_parse_group**(object: `Object<class_Object>`, group: `String<class_String>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorInspectorPlugin_private_method__parse_group>`

Called to allow adding controls at the beginning of a group or a sub-group in the property list for `object`.

classref-item-separator

classref-method

`bool<class_bool>` **\_parse_property**(object: `Object<class_Object>`, type: `Variant.Type<enum_@GlobalScope_Variant.Type>`, name: `String<class_String>`, hint_type: `PropertyHint<enum_@GlobalScope_PropertyHint>`, hint_string: `String<class_String>`, usage_flags: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`\], wide: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorInspectorPlugin_private_method__parse_property>`

Called to allow adding property-specific editors to the property list for `object`. The added editor control must extend `EditorProperty<class_EditorProperty>`. Returning `true` removes the built-in editor for this property, otherwise allows to insert a custom editor before the built-in one.

classref-item-separator

classref-method

`void (No return value.)` **add_custom_control**(control: `Control<class_Control>`) `🔗<class_EditorInspectorPlugin_method_add_custom_control>`

Adds a custom control, which is not necessarily a property editor.

classref-item-separator

classref-method

`void (No return value.)` **add_property_editor**(property: `String<class_String>`, editor: `Control<class_Control>`, add_to_end: `bool<class_bool>` = false, label: `String<class_String>` = "") `🔗<class_EditorInspectorPlugin_method_add_property_editor>`

Adds a property editor for an individual property. The `editor` control must extend `EditorProperty<class_EditorProperty>`.

There can be multiple property editors for a property. If `add_to_end` is `true`, this newly added editor will be displayed after all the other editors of the property whose `add_to_end` is `false`. For example, the editor uses this parameter to add an "Edit Region" button for `Sprite2D.region_rect<class_Sprite2D_property_region_rect>` below the regular `Rect2<class_Rect2>` editor.

`label` can be used to choose a custom label for the property editor in the inspector. If left empty, the label is computed from the name of the property instead.

classref-item-separator

classref-method

`void (No return value.)` **add_property_editor_for_multiple_properties**(label: `String<class_String>`, properties: `PackedStringArray<class_PackedStringArray>`, editor: `Control<class_Control>`) `🔗<class_EditorInspectorPlugin_method_add_property_editor_for_multiple_properties>`

Adds an editor that allows modifying multiple properties. The `editor` control must extend `EditorProperty<class_EditorProperty>`.