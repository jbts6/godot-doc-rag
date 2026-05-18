github_url
hide

# FoldableGroup

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A group of foldable containers that doesn't allow more than one container to be expanded at a time.

classref-introduction-group

## Description

A group of `FoldableContainer<class_FoldableContainer>`-derived nodes. Only one container can be expanded at a time.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**expanded**(container: `FoldableContainer<class_FoldableContainer>`) `🔗<class_FoldableGroup_signal_expanded>`

Emitted when one of the containers of the group is expanded.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **allow_folding_all** = `false` `🔗<class_FoldableGroup_property_allow_folding_all>`

classref-property-setget

- `void (No return value.)` **set_allow_folding_all**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_allow_folding_all**()

If `true`, it is possible to fold all containers in this FoldableGroup.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Array<class_Array>`\[`FoldableContainer<class_FoldableContainer>`\] **get_containers**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FoldableGroup_method_get_containers>`

Returns an `Array<class_Array>` of `FoldableContainer<class_FoldableContainer>`s that have this as their FoldableGroup (see `FoldableContainer.foldable_group<class_FoldableContainer_property_foldable_group>`). This is equivalent to `ButtonGroup<class_ButtonGroup>` but for FoldableContainers.

classref-item-separator

classref-method

`FoldableContainer<class_FoldableContainer>` **get_expanded_container**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_FoldableGroup_method_get_expanded_container>`

Returns the current expanded container.