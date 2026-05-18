github_url
hide

# PhysicsMaterial

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Holds physics-related properties of a surface, namely its roughness and bounciness.

classref-introduction-group

## Description

Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **absorbent** = `false` `🔗<class_PhysicsMaterial_property_absorbent>`

classref-property-setget

- `void (No return value.)` **set_absorbent**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_absorbent**()

If `true`, subtracts the bounciness from the colliding object's bounciness instead of adding it.

classref-item-separator

classref-property

`float<class_float>` **bounce** = `0.0` `🔗<class_PhysicsMaterial_property_bounce>`

classref-property-setget

- `void (No return value.)` **set_bounce**(value: `float<class_float>`)
- `float<class_float>` **get_bounce**()

The body's bounciness. Values range from `0` (no bounce) to `1` (full bounciness).

**Note:** Even with `bounce<class_PhysicsMaterial_property_bounce>` set to `1.0`, some energy will be lost over time due to linear and angular damping. To have a physics body that preserves all its energy over time, set `bounce<class_PhysicsMaterial_property_bounce>` to `1.0`, the body's linear damp mode to **Replace** (if applicable), its linear damp to `0.0`, its angular damp mode to **Replace** (if applicable), and its angular damp to `0.0`.

classref-item-separator

classref-property

`float<class_float>` **friction** = `1.0` `🔗<class_PhysicsMaterial_property_friction>`

classref-property-setget

- `void (No return value.)` **set_friction**(value: `float<class_float>`)
- `float<class_float>` **get_friction**()

The body's friction. Values range from `0` (frictionless) to `1` (maximum friction).

classref-item-separator

classref-property

`bool<class_bool>` **rough** = `false` `🔗<class_PhysicsMaterial_property_rough>`

classref-property-setget

- `void (No return value.)` **set_rough**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_rough**()

If `true`, the physics engine will use the friction of the object marked as "rough" when two objects collide. If `false`, the physics engine will use the lowest friction of all colliding objects instead. If `true` for both colliding objects, the physics engine will use the highest friction.