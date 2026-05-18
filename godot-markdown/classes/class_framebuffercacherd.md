github_url
hide

# FramebufferCacheRD

**Inherits:** `Object<class_Object>`

Framebuffer cache manager for Rendering Device based renderers.

classref-introduction-group

## Description

Framebuffer cache manager for `RenderingDevice<class_RenderingDevice>`-based renderers. Provides a way to create a framebuffer and reuse it in subsequent calls for as long as the used textures exists. Framebuffers will automatically be cleaned up when dependent objects are freed.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **get_cache_multipass**(textures: `Array<class_Array>`\[`RID<class_RID>`\], passes: `Array<class_Array>`\[`RDFramebufferPass<class_RDFramebufferPass>`\], views: `int<class_int>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_FramebufferCacheRD_method_get_cache_multipass>`

Creates, or obtains a cached, framebuffer. `textures` lists textures accessed. `passes` defines the subpasses and texture allocation, if left empty a single pass is created and textures are allocated depending on their usage flags. `views` defines the number of views used when rendering.