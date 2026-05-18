github_url
hide

# UniformSetCacheRD

**Inherits:** `Object<class_Object>`

Uniform set cache manager for Rendering Device based renderers.

classref-introduction-group

## Description

Uniform set cache manager for `RenderingDevice<class_RenderingDevice>`-based renderers. Provides a way to create a uniform set and reuse it in subsequent calls for as long as the uniform set exists. Uniform set will automatically be cleaned up when dependent objects are freed.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`RID<class_RID>` **get_cache**(shader: `RID<class_RID>`, set: `int<class_int>`, uniforms: `Array<class_Array>`\[`RDUniform<class_RDUniform>`\]) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_UniformSetCacheRD_method_get_cache>`

Creates/returns a cached uniform set based on the provided uniforms for a given shader.