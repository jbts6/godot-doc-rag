github_url
hide

# Compositor

**Experimental:** More customization of the rendering pipeline will be added in the future.

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Stores attributes used to customize how a Viewport is rendered.

classref-introduction-group

## Description

The compositor resource stores attributes used to customize how a `Viewport<class_Viewport>` is rendered.

classref-introduction-group

## Tutorials

- `The Compositor <../tutorials/rendering/compositor>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Array<class_Array>`\[`CompositorEffect<class_CompositorEffect>`\] **compositor_effects** = `[]` `🔗<class_Compositor_property_compositor_effects>`

classref-property-setget

- `void (No return value.)` **set_compositor_effects**(value: `Array<class_Array>`\[`CompositorEffect<class_CompositorEffect>`\])
- `Array<class_Array>`\[`CompositorEffect<class_CompositorEffect>`\] **get_compositor_effects**()

The custom `CompositorEffect<class_CompositorEffect>`s that are applied during rendering of viewports using this compositor.