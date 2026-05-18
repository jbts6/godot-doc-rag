github_url
hide

# RenderSceneBuffersExtension

**Inherits:** `RenderSceneBuffers<class_RenderSceneBuffers>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

classref-introduction-group

## Description

This class allows for a RenderSceneBuffer implementation to be made in GDExtension.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **\_configure**(config: `RenderSceneBuffersConfiguration<class_RenderSceneBuffersConfiguration>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_RenderSceneBuffersExtension_private_method__configure>`

Implement this in GDExtension to handle the (re)sizing of a viewport.

classref-item-separator

classref-method

`void (No return value.)` **\_set_anisotropic_filtering_level**(anisotropic_filtering_level: `int<class_int>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_RenderSceneBuffersExtension_private_method__set_anisotropic_filtering_level>`

Implement this in GDExtension to change the anisotropic filtering level.

classref-item-separator

classref-method

`void (No return value.)` **\_set_fsr_sharpness**(fsr_sharpness: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_RenderSceneBuffersExtension_private_method__set_fsr_sharpness>`

Implement this in GDExtension to record a new FSR sharpness value.

classref-item-separator

classref-method

`void (No return value.)` **\_set_texture_mipmap_bias**(texture_mipmap_bias: `float<class_float>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_RenderSceneBuffersExtension_private_method__set_texture_mipmap_bias>`

Implement this in GDExtension to change the texture mipmap bias.

classref-item-separator

classref-method

`void (No return value.)` **\_set_use_debanding**(use_debanding: `bool<class_bool>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_RenderSceneBuffersExtension_private_method__set_use_debanding>`

Implement this in GDExtension to react to the debanding flag changing.