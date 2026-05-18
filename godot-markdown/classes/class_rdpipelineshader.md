github_url
hide

# RDPipelineShader

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Pipeline shader (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

Wraps a shader resource and allows specialization constants to be applied at pipeline creation time.

Used by `RenderingDevice.raytracing_pipeline_create()<class_RenderingDevice_method_raytracing_pipeline_create>` for ray generation, miss, and hit shaders. The pipeline selects the required shader stage automatically.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RID<class_RID>` **shader** = `RID()` `🔗<class_RDPipelineShader_property_shader>`

classref-property-setget

- `void (No return value.)` **set_shader**(value: `RID<class_RID>`)
- `RID<class_RID>` **get_shader**()

Shader resource. The required stage is selected by the pipeline.

classref-item-separator

classref-property

`Array<class_Array>`\[`RDPipelineSpecializationConstant<class_RDPipelineSpecializationConstant>`\] **specialization_constants** = `[]` `🔗<class_RDPipelineShader_property_specialization_constants>`

classref-property-setget

- `void (No return value.)` **set_specialization_constants**(value: `Array<class_Array>`\[`RDPipelineSpecializationConstant<class_RDPipelineSpecializationConstant>`\])
- `Array<class_Array>`\[`RDPipelineSpecializationConstant<class_RDPipelineSpecializationConstant>`\] **get_specialization_constants**()

Specialization constants applied to the selected shader stage at pipeline creation time.