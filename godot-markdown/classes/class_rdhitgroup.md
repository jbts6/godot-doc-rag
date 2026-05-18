github_url
hide

# RDHitGroup

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Hit group (used by `RenderingDevice<class_RenderingDevice>`).

classref-introduction-group

## Description

Defines a hit group for use with `RenderingDevice.raytracing_pipeline_create()<class_RenderingDevice_method_raytracing_pipeline_create>`.

A hit group combines shaders that are executed when a ray intersects geometry. It may include a closest-hit shader, any-hit shader, and intersection shader.

Hit groups are referenced by index when populating hit shader binding tables using `RenderingDevice.hit_sbt_range_update()<class_RenderingDevice_method_hit_sbt_range_update>`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`RDPipelineShader<class_RDPipelineShader>` **any_hit_shader** `🔗<class_RDHitGroup_property_any_hit_shader>`

classref-property-setget

- `void (No return value.)` **set_any_hit_shader**(value: `RDPipelineShader<class_RDPipelineShader>`)
- `RDPipelineShader<class_RDPipelineShader>` **get_any_hit_shader**()

Any-hit shader for this hit group. Executed for each potential intersection. Can be `null`.

classref-item-separator

classref-property

`RDPipelineShader<class_RDPipelineShader>` **closest_hit_shader** `🔗<class_RDHitGroup_property_closest_hit_shader>`

classref-property-setget

- `void (No return value.)` **set_closest_hit_shader**(value: `RDPipelineShader<class_RDPipelineShader>`)
- `RDPipelineShader<class_RDPipelineShader>` **get_closest_hit_shader**()

Closest-hit shader for this hit group. Executed for the closest intersection. Can be `null`.

classref-item-separator

classref-property

`RDPipelineShader<class_RDPipelineShader>` **intersection_shader** `🔗<class_RDHitGroup_property_intersection_shader>`

classref-property-setget

- `void (No return value.)` **set_intersection_shader**(value: `RDPipelineShader<class_RDPipelineShader>`)
- `RDPipelineShader<class_RDPipelineShader>` **get_intersection_shader**()

Intersection shader for this hit group. Required for non-triangle geometry. Must be `null` when using for triangle geometry.