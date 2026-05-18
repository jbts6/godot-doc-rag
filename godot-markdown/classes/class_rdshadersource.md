github_url
hide

# RDShaderSource

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Shader source code (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

Shader source code in text form.

See also `RDShaderFile<class_RDShaderFile>`. **RDShaderSource** is only meant to be used with the `RenderingDevice<class_RenderingDevice>` API. It should not be confused with Godot's own `Shader<class_Shader>` resource, which is what Godot's various nodes use for high-level shader programming.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`ShaderLanguage<enum_RenderingDevice_ShaderLanguage>` **language** = `0` `🔗<class_RDShaderSource_property_language>`

classref-property-setget

- `void (No return value.)` **set_language**(value: `ShaderLanguage<enum_RenderingDevice_ShaderLanguage>`)
- `ShaderLanguage<enum_RenderingDevice_ShaderLanguage>` **get_language**()

The language the shader is written in.

classref-item-separator

classref-property

`String<class_String>` **source_any_hit** = `""` `🔗<class_RDShaderSource_property_source_any_hit>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's any hit stage.

classref-item-separator

classref-property

`String<class_String>` **source_closest_hit** = `""` `🔗<class_RDShaderSource_property_source_closest_hit>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's closest hit stage.

classref-item-separator

classref-property

`String<class_String>` **source_compute** = `""` `🔗<class_RDShaderSource_property_source_compute>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's compute stage.

classref-item-separator

classref-property

`String<class_String>` **source_fragment** = `""` `🔗<class_RDShaderSource_property_source_fragment>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's fragment stage.

classref-item-separator

classref-property

`String<class_String>` **source_intersection** = `""` `🔗<class_RDShaderSource_property_source_intersection>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's intersection stage.

classref-item-separator

classref-property

`String<class_String>` **source_miss** = `""` `🔗<class_RDShaderSource_property_source_miss>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's miss stage.

classref-item-separator

classref-property

`String<class_String>` **source_raygen** = `""` `🔗<class_RDShaderSource_property_source_raygen>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's ray generation stage.

classref-item-separator

classref-property

`String<class_String>` **source_tesselation_control** = `""` `🔗<class_RDShaderSource_property_source_tesselation_control>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's tessellation control stage.

classref-item-separator

classref-property

`String<class_String>` **source_tesselation_evaluation** = `""` `🔗<class_RDShaderSource_property_source_tesselation_evaluation>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's tessellation evaluation stage.

classref-item-separator

classref-property

`String<class_String>` **source_vertex** = `""` `🔗<class_RDShaderSource_property_source_vertex>`

classref-property-setget

- `void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`)
- `String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`

Source code for the shader's vertex stage.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_RDShaderSource_method_get_stage_source>`

Returns source code for the specified shader `stage`. Equivalent to getting one of `source_compute<class_RDShaderSource_property_source_compute>`, `source_fragment<class_RDShaderSource_property_source_fragment>`, `source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>`, `source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>` or `source_vertex<class_RDShaderSource_property_source_vertex>`.

classref-item-separator

classref-method

`void (No return value.)` **set_stage_source**(stage: `ShaderStage<enum_RenderingDevice_ShaderStage>`, source: `String<class_String>`) `🔗<class_RDShaderSource_method_set_stage_source>`

Sets `source` code for the specified shader `stage`. Equivalent to setting one of `source_compute<class_RDShaderSource_property_source_compute>`, `source_fragment<class_RDShaderSource_property_source_fragment>`, `source_tesselation_control<class_RDShaderSource_property_source_tesselation_control>`, `source_tesselation_evaluation<class_RDShaderSource_property_source_tesselation_evaluation>` or `source_vertex<class_RDShaderSource_property_source_vertex>`.

**Note:** If you set the compute shader source code using this method directly, remember to remove the Godot-specific hint `#[compute]`.