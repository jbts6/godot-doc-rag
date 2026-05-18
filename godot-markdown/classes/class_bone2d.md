github_url
hide

# Bone2D

**Inherits:** `Node2D<class_Node2D>` **\<** `CanvasItem<class_CanvasItem>` **\<** `Node<class_Node>` **\<** `Object<class_Object>`

A joint used with `Skeleton2D<class_Skeleton2D>` to control and animate other nodes.

classref-introduction-group

## Description

A hierarchy of **Bone2D**s can be bound to a `Skeleton2D<class_Skeleton2D>` to control and animate other `Node2D<class_Node2D>` nodes.

You can use **Bone2D** and `Skeleton2D<class_Skeleton2D>` nodes to animate 2D meshes created with the `Polygon2D<class_Polygon2D>` UV editor.

Each bone has a `rest<class_Bone2D_property_rest>` transform that you can reset to with `apply_rest()<class_Bone2D_method_apply_rest>`. These rest poses are relative to the bone's parent.

If in the editor, you can set the rest pose of an entire skeleton using a menu option, from the code, you need to iterate over the bones to set their individual rest poses.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Transform2D<class_Transform2D>` **rest** = `Transform2D(0, 0, 0, 0, 0, 0)` `🔗<class_Bone2D_property_rest>`

classref-property-setget

- `void (No return value.)` **set_rest**(value: `Transform2D<class_Transform2D>`)
- `Transform2D<class_Transform2D>` **get_rest**()

Rest transform of the bone. You can reset the node's transforms to this value using `apply_rest()<class_Bone2D_method_apply_rest>`.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **apply_rest**() `🔗<class_Bone2D_method_apply_rest>`

Resets the bone to the rest pose. This is equivalent to setting `Node2D.transform<class_Node2D_property_transform>` to `rest<class_Bone2D_property_rest>`.

classref-item-separator

classref-method

`bool<class_bool>` **get_autocalculate_length_and_angle**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Bone2D_method_get_autocalculate_length_and_angle>`

Returns whether this **Bone2D** is going to autocalculate its length and bone angle using its first **Bone2D** child node, if one exists. If there are no **Bone2D** children, then it cannot autocalculate these values and will print a warning.

classref-item-separator

classref-method

`float<class_float>` **get_bone_angle**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Bone2D_method_get_bone_angle>`

Returns the angle of the bone in the **Bone2D**.

**Note:** This is different from the **Bone2D**'s rotation. The bone's angle is the rotation of the bone shown by the gizmo, which is unaffected by the **Bone2D**'s `Node2D.transform<class_Node2D_property_transform>`.

classref-item-separator

classref-method

`int<class_int>` **get_index_in_skeleton**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Bone2D_method_get_index_in_skeleton>`

Returns the node's index as part of the entire skeleton. See `Skeleton2D<class_Skeleton2D>`.

classref-item-separator

classref-method

`float<class_float>` **get_length**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Bone2D_method_get_length>`

Returns the length of the bone in the **Bone2D** node.

classref-item-separator

classref-method

`Transform2D<class_Transform2D>` **get_skeleton_rest**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Bone2D_method_get_skeleton_rest>`

Returns the node's `rest<class_Bone2D_property_rest>` `Transform2D<class_Transform2D>` if it doesn't have a parent, or its rest pose relative to its parent.

classref-item-separator

classref-method

`void (No return value.)` **set_autocalculate_length_and_angle**(auto_calculate: `bool<class_bool>`) `🔗<class_Bone2D_method_set_autocalculate_length_and_angle>`

When set to `true`, the **Bone2D** node will attempt to automatically calculate the bone angle and length using the first child **Bone2D** node, if one exists. If none exist, the **Bone2D** cannot automatically calculate these values and will print a warning.

classref-item-separator

classref-method

`void (No return value.)` **set_bone_angle**(angle: `float<class_float>`) `🔗<class_Bone2D_method_set_bone_angle>`

Sets the bone angle for the **Bone2D**. This is typically set to the rotation from the **Bone2D** to a child **Bone2D** node.

**Note:** This is different from the **Bone2D**'s rotation. The bone's angle is the rotation of the bone shown by the gizmo, which is unaffected by the **Bone2D**'s `Node2D.transform<class_Node2D_property_transform>`.

classref-item-separator

classref-method

`void (No return value.)` **set_length**(length: `float<class_float>`) `🔗<class_Bone2D_method_set_length>`

Sets the length of the bone in the **Bone2D**.