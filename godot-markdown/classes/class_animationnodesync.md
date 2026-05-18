github_url
hide

# AnimationNodeSync

**Inherits:** `AnimationNode<class_AnimationNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `AnimationNodeAdd2<class_AnimationNodeAdd2>`, `AnimationNodeAdd3<class_AnimationNodeAdd3>`, `AnimationNodeBlend2<class_AnimationNodeBlend2>`, `AnimationNodeBlend3<class_AnimationNodeBlend3>`, `AnimationNodeOneShot<class_AnimationNodeOneShot>`, `AnimationNodeSub2<class_AnimationNodeSub2>`, `AnimationNodeTransition<class_AnimationNodeTransition>`

Base class for `AnimationNode<class_AnimationNode>`s with multiple input ports that must be synchronized.

classref-introduction-group

## Description

An animation node used to combine, mix, or blend two or more animations together while keeping them synchronized within an `AnimationTree<class_AnimationTree>`.

classref-introduction-group

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **sync** = `false` `🔗<class_AnimationNodeSync_property_sync>`

classref-property-setget

- `void (No return value.)` **set_use_sync**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_using_sync**()

If `false`, the blended animations' frame are stopped when the blend value is `0`.

If `true`, forcing the blended animations to advance frame.