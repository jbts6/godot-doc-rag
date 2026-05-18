github_url
hide

# SkeletonModification2DJiggle

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `SkeletonModification2D<class_SkeletonModification2D>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A modification that jiggles `Bone2D<class_Bone2D>` nodes as they move towards a target.

classref-introduction-group

## Description

This modification moves a series of bones, typically called a bone chain, towards a target. What makes this modification special is that it calculates the velocity and acceleration for each bone in the bone chain, and runs a very light physics-like calculation using the inputted values. This allows the bones to overshoot the target and "jiggle" around. It can be configured to act more like a spring, or sway around like cloth might.

This modification is useful for adding additional motion to things like hair, the edges of clothing, and more. It has several settings to that allow control over how the joint moves when the target moves.

**Note:** The Jiggle modifier has `jiggle_joints`, which are the data objects that hold the data for each joint in the Jiggle chain. This is different from than `Bone2D<class_Bone2D>` nodes! Jiggle joints hold the data needed for each `Bone2D<class_Bone2D>` in the bone chain used by the Jiggle modification.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **damping** = `0.75` `🔗<class_SkeletonModification2DJiggle_property_damping>`

classref-property-setget

- `void (No return value.)` **set_damping**(value: `float<class_float>`)
- `float<class_float>` **get_damping**()

The default amount of damping applied to the Jiggle joints, if they are not overridden. Higher values lead to more of the calculated velocity being applied.

classref-item-separator

classref-property

`Vector2<class_Vector2>` **gravity** = `Vector2(0, 6)` `🔗<class_SkeletonModification2DJiggle_property_gravity>`

classref-property-setget

- `void (No return value.)` **set_gravity**(value: `Vector2<class_Vector2>`)
- `Vector2<class_Vector2>` **get_gravity**()

The default amount of gravity applied to the Jiggle joints, if they are not overridden.

classref-item-separator

classref-property

`int<class_int>` **jiggle_data_chain_length** = `0` `🔗<class_SkeletonModification2DJiggle_property_jiggle_data_chain_length>`

classref-property-setget

- `void (No return value.)` **set_jiggle_data_chain_length**(value: `int<class_int>`)
- `int<class_int>` **get_jiggle_data_chain_length**()

The amount of Jiggle joints in the Jiggle modification.

classref-item-separator

classref-property

`float<class_float>` **mass** = `0.75` `🔗<class_SkeletonModification2DJiggle_property_mass>`

classref-property-setget

- `void (No return value.)` **set_mass**(value: `float<class_float>`)
- `float<class_float>` **get_mass**()

The default amount of mass assigned to the Jiggle joints, if they are not overridden. Higher values lead to faster movements and more overshooting.

classref-item-separator

classref-property

`float<class_float>` **stiffness** = `3.0` `🔗<class_SkeletonModification2DJiggle_property_stiffness>`

classref-property-setget

- `void (No return value.)` **set_stiffness**(value: `float<class_float>`)
- `float<class_float>` **get_stiffness**()

The default amount of stiffness assigned to the Jiggle joints, if they are not overridden. Higher values act more like springs, quickly moving into the correct position.

classref-item-separator

classref-property

`NodePath<class_NodePath>` **target_nodepath** = `NodePath("")` `🔗<class_SkeletonModification2DJiggle_property_target_nodepath>`

classref-property-setget

- `void (No return value.)` **set_target_node**(value: `NodePath<class_NodePath>`)
- `NodePath<class_NodePath>` **get_target_node**()

The NodePath to the node that is the target for the Jiggle modification. This node is what the Jiggle chain will attempt to rotate the bone chain to.

classref-item-separator

classref-property

`bool<class_bool>` **use_gravity** = `false` `🔗<class_SkeletonModification2DJiggle_property_use_gravity>`

classref-property-setget

- `void (No return value.)` **set_use_gravity**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_use_gravity**()

Whether the gravity vector, `gravity<class_SkeletonModification2DJiggle_property_gravity>`, should be applied to the Jiggle joints, assuming they are not overriding the default settings.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **get_collision_mask**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_collision_mask>`

Returns the collision mask used by the Jiggle modifier when collisions are enabled.

classref-item-separator

classref-method

`NodePath<class_NodePath>` **get_jiggle_joint_bone2d_node**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone2d_node>`

Returns the `Bone2D<class_Bone2D>` node assigned to the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`int<class_int>` **get_jiggle_joint_bone_index**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone_index>`

Returns the index of the `Bone2D<class_Bone2D>` node assigned to the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`float<class_float>` **get_jiggle_joint_damping**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_damping>`

Returns the amount of damping of the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`Vector2<class_Vector2>` **get_jiggle_joint_gravity**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_gravity>`

Returns a `Vector2<class_Vector2>` representing the amount of gravity the Jiggle joint at `joint_idx` is influenced by.

classref-item-separator

classref-method

`float<class_float>` **get_jiggle_joint_mass**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_mass>`

Returns the amount of mass of the jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`bool<class_bool>` **get_jiggle_joint_override**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_override>`

Returns a boolean that indicates whether the joint at `joint_idx` is overriding the default Jiggle joint data defined in the modification.

classref-item-separator

classref-method

`float<class_float>` **get_jiggle_joint_stiffness**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_stiffness>`

Returns the stiffness of the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`bool<class_bool>` **get_jiggle_joint_use_gravity**(joint_idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_use_gravity>`

Returns a boolean that indicates whether the joint at `joint_idx` is using gravity or not.

classref-item-separator

classref-method

`bool<class_bool>` **get_use_colliders**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SkeletonModification2DJiggle_method_get_use_colliders>`

Returns whether the jiggle modifier is taking physics colliders into account when solving.

classref-item-separator

classref-method

`void (No return value.)` **reset**() `🔗<class_SkeletonModification2DJiggle_method_reset>`

Resets the internal jiggle simulation state to the current bone positions, clearing velocity, acceleration, and accumulated forces.

classref-item-separator

classref-method

`void (No return value.)` **set_collision_mask**(collision_mask: `int<class_int>`) `🔗<class_SkeletonModification2DJiggle_method_set_collision_mask>`

Sets the collision mask that the Jiggle modifier will use when reacting to colliders, if the Jiggle modifier is set to take colliders into account.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_bone2d_node**(joint_idx: `int<class_int>`, bone2d_node: `NodePath<class_NodePath>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone2d_node>`

Sets the `Bone2D<class_Bone2D>` node assigned to the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_bone_index**(joint_idx: `int<class_int>`, bone_idx: `int<class_int>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone_index>`

Sets the bone index, `bone_idx`, of the Jiggle joint at `joint_idx`. When possible, this will also update the `bone2d_node` of the Jiggle joint based on data provided by the linked skeleton.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_damping**(joint_idx: `int<class_int>`, damping: `float<class_float>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_damping>`

Sets the amount of damping of the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_gravity**(joint_idx: `int<class_int>`, gravity: `Vector2<class_Vector2>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_gravity>`

Sets the gravity vector of the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_mass**(joint_idx: `int<class_int>`, mass: `float<class_float>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_mass>`

Sets the of mass of the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_override**(joint_idx: `int<class_int>`, override: `bool<class_bool>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_override>`

Sets whether the Jiggle joint at `joint_idx` should override the default Jiggle joint settings. Setting this to `true` will make the joint use its own settings rather than the default ones attached to the modification.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_stiffness**(joint_idx: `int<class_int>`, stiffness: `float<class_float>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_stiffness>`

Sets the of stiffness of the Jiggle joint at `joint_idx`.

classref-item-separator

classref-method

`void (No return value.)` **set_jiggle_joint_use_gravity**(joint_idx: `int<class_int>`, use_gravity: `bool<class_bool>`) `🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_use_gravity>`

Sets whether the Jiggle joint at `joint_idx` should use gravity.

classref-item-separator

classref-method

`void (No return value.)` **set_use_colliders**(use_colliders: `bool<class_bool>`) `🔗<class_SkeletonModification2DJiggle_method_set_use_colliders>`

If `true`, the Jiggle modifier will take colliders into account, keeping them from entering into these collision objects.