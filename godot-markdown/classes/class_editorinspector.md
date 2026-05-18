github_url
hide

# EditorInspector

**Inherits:** `ScrollContainer<class_ScrollContainer>` **\<** `Container<class_Container>` **\<** `Control<class_Control>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A control used to edit properties of an object.

classref-introduction-group

## Description

This is the control that implements property editing in the editor's Settings dialogs, the Inspector dock, etc. To get the **EditorInspector** used in the editor's Inspector dock, use `EditorInterface.get_inspector()<class_EditorInterface_method_get_inspector>`.

**EditorInspector** will show properties in the same order as the array returned by `Object.get_property_list()<class_Object_method_get_property_list>`.

If a property's name is path-like (i.e. if it contains forward slashes), **EditorInspector** will create nested sections for "directories" along the path. For example, if a property is named `highlighting/gdscript/node_path_color`, it will be shown as "Node Path Color" inside the "GDScript" section nested inside the "Highlighting" section.

If a property has `@GlobalScope.PROPERTY_USAGE_GROUP<class_@GlobalScope_constant_PROPERTY_USAGE_GROUP>` usage, it will group subsequent properties whose name starts with the property's hint string. The group ends when a property does not start with that hint string or when a new group starts. An empty group name effectively ends the current group. **EditorInspector** will create a top-level section for each group. For example, if a property with group usage is named `Collide With` and its hint string is `collide_with_`, a subsequent `collide_with_area` property will be shown as "Area" inside the "Collide With" section. There is also a special case: when the hint string contains the name of a property, that property is grouped too. This is mainly to help grouping properties like `font`, `font_color` and `font_size` (using the hint string `font_`).

If a property has `@GlobalScope.PROPERTY_USAGE_SUBGROUP<class_@GlobalScope_constant_PROPERTY_USAGE_SUBGROUP>` usage, a subgroup will be created in the same way as a group, and a second-level section will be created for each subgroup.

**Note:** Unlike sections created from path-like property names, **EditorInspector** won't capitalize the name for sections created from groups. So properties with group usage usually use capitalized names instead of snake_cased names.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**edited_object_changed**() `🔗<class_EditorInspector_signal_edited_object_changed>`

Emitted when the object being edited by the inspector has changed.

classref-item-separator

classref-signal

**object_id_selected**(id: `int<class_int>`) `🔗<class_EditorInspector_signal_object_id_selected>`

Emitted when the Edit button of an `Object<class_Object>` has been pressed in the inspector. This is mainly used in the remote scene tree Inspector.

classref-item-separator

classref-signal

**property_deleted**(property: `String<class_String>`) `🔗<class_EditorInspector_signal_property_deleted>`

Emitted when a property is removed from the inspector.

classref-item-separator

classref-signal

**property_edited**(property: `String<class_String>`) `🔗<class_EditorInspector_signal_property_edited>`

Emitted when a property is edited in the inspector.

classref-item-separator

classref-signal

**property_keyed**(property: `String<class_String>`, value: `Variant<class_Variant>`, advance: `bool<class_bool>`) `🔗<class_EditorInspector_signal_property_keyed>`

Emitted when a property is keyed in the inspector. Properties can be keyed by clicking the "key" icon next to a property when the Animation panel is toggled.

classref-item-separator

classref-signal

**property_selected**(property: `String<class_String>`) `🔗<class_EditorInspector_signal_property_selected>`

Emitted when a property is selected in the inspector.

classref-item-separator

classref-signal

**property_toggled**(property: `String<class_String>`, checked: `bool<class_bool>`) `🔗<class_EditorInspector_signal_property_toggled>`

Emitted when a boolean property is toggled in the inspector.

**Note:** This signal is never emitted if the internal `autoclear` property enabled. Since this property is always enabled in the editor inspector, this signal is never emitted by the editor itself.

classref-item-separator

classref-signal

**resource_selected**(resource: `Resource<class_Resource>`, path: `String<class_String>`) `🔗<class_EditorInspector_signal_resource_selected>`

Emitted when a resource is selected in the inspector.

classref-item-separator

classref-signal

**restart_requested**() `🔗<class_EditorInspector_signal_restart_requested>`

Emitted when a property that requires a restart to be applied is edited in the inspector. This is only used in the Project Settings and Editor Settings.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **collapse_all_folding**() `🔗<class_EditorInspector_method_collapse_all_folding>`

Collapses all foldable sections.

classref-item-separator

classref-method

`EditorInspector<class_EditorInspector>` **create_default_inspector**(filter_line_edit: `LineEdit<class_LineEdit>` = null) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_EditorInspector_method_create_default_inspector>`

Creates an inspector with the same configuration as the one used in the editor's Inspector dock. When passing a `LineEdit<class_LineEdit>` into `filter_line_edit`, the inspector will filter its properties based on `LineEdit.text<class_LineEdit_property_text>` whenever `LineEdit.text_changed<class_LineEdit_signal_text_changed>` is emitted.

classref-item-separator

classref-method

`void (No return value.)` **edit**(object: `Object<class_Object>`) `🔗<class_EditorInspector_method_edit>`

Shows the properties of the given `object` in this inspector for editing. To clear the inspector, call this method with `null`.

**Note:** If you want to edit an object in the editor's main inspector, use the `edit_*` methods in `EditorInterface<class_EditorInterface>` instead.

classref-item-separator

classref-method

`void (No return value.)` **expand_all_folding**() `🔗<class_EditorInspector_method_expand_all_folding>`

Expands all foldable sections.

classref-item-separator

classref-method

`void (No return value.)` **expand_revertable**() `🔗<class_EditorInspector_method_expand_revertable>`

Expands only the foldable sections that contain a revertable (i.e. non-default) property.

classref-item-separator

classref-method

`Object<class_Object>` **get_edited_object**() `🔗<class_EditorInspector_method_get_edited_object>`

Returns the object currently selected in this inspector.

classref-item-separator

classref-method

`String<class_String>` **get_selected_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorInspector_method_get_selected_path>`

Gets the path of the currently selected property.

classref-item-separator

classref-method

`EditorProperty<class_EditorProperty>` **instantiate_property_editor**(object: `Object<class_Object>`, type: `Variant.Type<enum_@GlobalScope_Variant.Type>`, path: `String<class_String>`, hint: `PropertyHint<enum_@GlobalScope_PropertyHint>`, hint_text: `String<class_String>`, usage: `int<class_int>`, wide: `bool<class_bool>` = false) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_EditorInspector_method_instantiate_property_editor>`

Creates a property editor that can be used by plugin UI to edit the specified property of an `object`.