github_url
hide

# SkeletonModification2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `SkeletonModification2DCCDIK<class_SkeletonModification2DCCDIK>`, `SkeletonModification2DFABRIK<class_SkeletonModification2DFABRIK>`, `SkeletonModification2DJiggle<class_SkeletonModification2DJiggle>`, `SkeletonModification2DLookAt<class_SkeletonModification2DLookAt>`, `SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>`, `SkeletonModification2DStackHolder<class_SkeletonModification2DStackHolder>`, `SkeletonModification2DTwoBoneIK<class_SkeletonModification2DTwoBoneIK>`

Base class for resources that operate on `Bone2D<class_Bone2D>`s in a `Skeleton2D<class_Skeleton2D>`.

classref-introduction-group

## Description

This resource provides an interface that can be expanded so code that operates on `Bone2D<class_Bone2D>` nodes in a `Skeleton2D<class_Skeleton2D>` can be mixed and matched together to create complex interactions.

This is used to provide Godot with a flexible and powerful Inverse Kinematics solution that can be adapted for many different uses.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **enabled** = `true` `🔗<class_SkeletonModification2D_property_enabled>`

classref-property-setget

- `void (No return value.)` **set_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_enabled**()

If `true`, the modification's `_execute()<class_SkeletonModification2D_private_method__execute>` function will be called by the `SkeletonModificationStack2D<class_SkeletonModificationStack2D>`.

classref-item-separator

classref-property

`int<class_int>` **execution_mode** = `0` `🔗<class_SkeletonModification2D_property_execution_mode>`

classref-property-setget

- `void (No return value.)` **set_execution_mode**(value: `int<class_int>`)
- `int<class_int>` **get_execution_mode**()

The execution mode for the modification. This tells the modification stack when to execute the modification. Some modifications have settings that are only available in certain execution modes.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_draw_editor_gizmo**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_SkeletonModification2D_private_method__draw_editor_gizmo>`

Used for drawing **editor-only** modification gizmos. This function will only be called in the Godot editor and can be overridden to draw custom gizmos.

**Note:** You will need to use the Skeleton2D from `SkeletonModificationStack2D.get_skeleton()<class_SkeletonModificationStack2D_method_get_skeleton>` and it's draw functions, as the **SkeletonModification2D** resource cannot draw on its own.

classref-item-separator

classref-method

`void (No return value.)` **\_execute**(delta: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_SkeletonModification2D_private_method__execute>`

Executes the given modification. This is where the modification performs whatever function it is designed to do.

classref-item-separator

classref-method

`void (No return value.)` **\_setup_modification**(modification_stack: `SkeletonModificationStack2D<class_SkeletonModificationStack2D>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_SkeletonModification2D_private_method__setup_modification>`

Called when the modification is setup. This is where the modification performs initialization.

classref-item-separator

classref-method

`float<class_float>` **clamp_angle**(angle: `float<class_float>`, min: `float<class_float>`, max: `float<class_float>`, invert: `bool<class_bool>`) `🔗<class_SkeletonModification2D_method_clamp_angle>`

Takes an angle and clamps it so it is within the passed-in `min` and `max` range. `invert` will inversely clamp the angle, clamping it to the range outside of the given bounds.

classref-item-separator

classref-method

`bool<class_bool>` **get_editor_draw_gizmo**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2D_method_get_editor_draw_gizmo>`

Returns whether this modification will call `_draw_editor_gizmo()<class_SkeletonModification2D_private_method__draw_editor_gizmo>` in the Godot editor to draw modification-specific gizmos.

classref-item-separator

classref-method

`bool<class_bool>` **get_is_setup**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2D_method_get_is_setup>`

Returns whether this modification has been successfully setup or not.

classref-item-separator

classref-method

`SkeletonModificationStack2D<class_SkeletonModificationStack2D>` **get_modification_stack**() `🔗<class_SkeletonModification2D_method_get_modification_stack>`

Returns the `SkeletonModificationStack2D<class_SkeletonModificationStack2D>` that this modification is bound to. Through the modification stack, you can access the Skeleton2D the modification is operating on.

classref-item-separator

classref-method

`void (No return value.)` **set_editor_draw_gizmo**(draw_gizmo: `bool<class_bool>`) `🔗<class_SkeletonModification2D_method_set_editor_draw_gizmo>`

Sets whether this modification will call `_draw_editor_gizmo()<class_SkeletonModification2D_private_method__draw_editor_gizmo>` in the Godot editor to draw modification-specific gizmos.

classref-item-separator

classref-method

`void (No return value.)` **set_is_setup**(is_setup: `bool<class_bool>`) `🔗<class_SkeletonModification2D_method_set_is_setup>`

Manually allows you to set the setup state of the modification. This function should only rarely be used, as the `SkeletonModificationStack2D<class_SkeletonModificationStack2D>` the modification is bound to should handle setting the modification up.