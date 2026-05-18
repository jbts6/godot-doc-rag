github_url
hide

# AudioListener2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

Overrides the location sounds are heard from.

classref-introduction-group

## Description

Once added to the scene tree and enabled using `make_current()<class_AudioListener2D_method_make_current>`, this node will override the location sounds are heard from. Only one **AudioListener2D** can be current. Using `make_current()<class_AudioListener2D_method_make_current>` will disable the previous **AudioListener2D**.

If there is no active **AudioListener2D** in the current `Viewport<class_Viewport>`, center of the screen will be used as a hearing point for the audio. **AudioListener2D** needs to be inside `SceneTree<class_SceneTree>` to function.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **clear_current**() `🔗<class_AudioListener2D_method_clear_current>`

Disables the **AudioListener2D**. If it's not set as current, this method will have no effect.

classref-item-separator

classref-method

`bool<class_bool>` **is_current**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_AudioListener2D_method_is_current>`

Returns `true` if this **AudioListener2D** is currently active.

classref-item-separator

classref-method

`void (No return value.)` **make_current**() `🔗<class_AudioListener2D_method_make_current>`

Makes the **AudioListener2D** active, setting it as the hearing point for the sounds. If there is already another active **AudioListener2D**, it will be disabled.

This method will have no effect if the **AudioListener2D** is not added to `SceneTree<class_SceneTree>`.