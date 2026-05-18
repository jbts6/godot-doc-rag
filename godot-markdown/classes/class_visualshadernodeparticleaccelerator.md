github_url
hide

# VisualShaderNodeParticleAccelerator

**Inherits:** `VisualShaderNode<class_VisualShaderNode>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A visual shader node that accelerates particles.

classref-introduction-group

## Description

Particle accelerator can be used in "process" step of particle shader. It will accelerate the particles. Connect it to the Velocity output port.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Mode**: `🔗<enum_VisualShaderNodeParticleAccelerator_Mode>`

classref-enumeration-constant

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` **MODE_LINEAR** = `0`

The particles will be accelerated based on their velocity.

classref-enumeration-constant

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` **MODE_RADIAL** = `1`

The particles will be accelerated towards or away from the center.

classref-enumeration-constant

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` **MODE_TANGENTIAL** = `2`

The particles will be accelerated tangentially to the radius vector from center to their position.

classref-enumeration-constant

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` **MODE_MAX** = `3`

Represents the size of the `Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` enum.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` **mode** = `0` `🔗<class_VisualShaderNodeParticleAccelerator_property_mode>`

classref-property-setget

- `void (No return value.)` **set_mode**(value: `Mode<enum_VisualShaderNodeParticleAccelerator_Mode>`)
- `Mode<enum_VisualShaderNodeParticleAccelerator_Mode>` **get_mode**()

Defines in what manner the particles will be accelerated.