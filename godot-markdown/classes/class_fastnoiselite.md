github_url
hide

# FastNoiseLite

**Inherits:** `Noise<class_Noise>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Generates noise using the FastNoiseLite library.

classref-introduction-group

## Description

This class generates noise using the FastNoiseLite library, which is a collection of several noise algorithms including Cellular, Perlin, Value, and more.

Most generated noise values are in the range of `[-1, 1]`, but not always. Some of the cellular noise algorithms return results above `1`.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **NoiseType**: `🔗<enum_FastNoiseLite_NoiseType>`

classref-enumeration-constant

`NoiseType<enum_FastNoiseLite_NoiseType>` **TYPE_VALUE** = `5`

A lattice of points are assigned random values then interpolated based on neighboring values.

classref-enumeration-constant

`NoiseType<enum_FastNoiseLite_NoiseType>` **TYPE_VALUE_CUBIC** = `4`

Similar to value noise (`TYPE_VALUE<class_FastNoiseLite_constant_TYPE_VALUE>`), but slower. Has more variance in peaks and valleys.

Cubic noise can be used to avoid certain artifacts when using value noise to create a bumpmap. In general, you should always use this mode if the value noise is being used for a heightmap or bumpmap.

classref-enumeration-constant

`NoiseType<enum_FastNoiseLite_NoiseType>` **TYPE_PERLIN** = `3`

A lattice of random gradients. Their dot products are interpolated to obtain values in between the lattices.

classref-enumeration-constant

`NoiseType<enum_FastNoiseLite_NoiseType>` **TYPE_CELLULAR** = `2`

Cellular includes both Worley noise and Voronoi diagrams which creates various regions of the same value.

classref-enumeration-constant

`NoiseType<enum_FastNoiseLite_NoiseType>` **TYPE_SIMPLEX** = `0`

As opposed to `TYPE_PERLIN<class_FastNoiseLite_constant_TYPE_PERLIN>`, gradients exist in a simplex lattice rather than a grid lattice, avoiding directional artifacts. Internally uses FastNoiseLite's OpenSimplex2 noise type.

classref-enumeration-constant

`NoiseType<enum_FastNoiseLite_NoiseType>` **TYPE_SIMPLEX_SMOOTH** = `1`

Modified, higher quality version of `TYPE_SIMPLEX<class_FastNoiseLite_constant_TYPE_SIMPLEX>`, but slower. Internally uses FastNoiseLite's OpenSimplex2S noise type.

classref-item-separator

classref-enumeration

enum **FractalType**: `🔗<enum_FastNoiseLite_FractalType>`

classref-enumeration-constant

`FractalType<enum_FastNoiseLite_FractalType>` **FRACTAL_NONE** = `0`

No fractal noise.

classref-enumeration-constant

`FractalType<enum_FastNoiseLite_FractalType>` **FRACTAL_FBM** = `1`

Method using Fractional Brownian Motion to combine octaves into a fractal.

classref-enumeration-constant

`FractalType<enum_FastNoiseLite_FractalType>` **FRACTAL_RIDGED** = `2`

Method of combining octaves into a fractal resulting in a "ridged" look.

classref-enumeration-constant

`FractalType<enum_FastNoiseLite_FractalType>` **FRACTAL_PING_PONG** = `3`

Method of combining octaves into a fractal with a ping pong effect.

classref-item-separator

classref-enumeration

enum **CellularDistanceFunction**: `🔗<enum_FastNoiseLite_CellularDistanceFunction>`

classref-enumeration-constant

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>` **DISTANCE_EUCLIDEAN** = `0`

Euclidean distance to the nearest point.

classref-enumeration-constant

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>` **DISTANCE_EUCLIDEAN_SQUARED** = `1`

Squared Euclidean distance to the nearest point.

classref-enumeration-constant

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>` **DISTANCE_MANHATTAN** = `2`

Manhattan distance (taxicab metric) to the nearest point.

classref-enumeration-constant

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>` **DISTANCE_HYBRID** = `3`

Blend of `DISTANCE_EUCLIDEAN<class_FastNoiseLite_constant_DISTANCE_EUCLIDEAN>` and `DISTANCE_MANHATTAN<class_FastNoiseLite_constant_DISTANCE_MANHATTAN>` to give curved cell boundaries.

classref-item-separator

classref-enumeration

enum **CellularReturnType**: `🔗<enum_FastNoiseLite_CellularReturnType>`

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_CELL_VALUE** = `0`

The cellular distance function will return the same value for all points within a cell.

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_DISTANCE** = `1`

The cellular distance function will return a value determined by the distance to the nearest point.

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_DISTANCE2** = `2`

The cellular distance function returns the distance to the second-nearest point.

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_DISTANCE2_ADD** = `3`

The distance to the nearest point is added to the distance to the second-nearest point.

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_DISTANCE2_SUB** = `4`

The distance to the nearest point is subtracted from the distance to the second-nearest point.

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_DISTANCE2_MUL** = `5`

The distance to the nearest point is multiplied with the distance to the second-nearest point.

classref-enumeration-constant

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **RETURN_DISTANCE2_DIV** = `6`

The distance to the nearest point is divided by the distance to the second-nearest point.

classref-item-separator

classref-enumeration

enum **DomainWarpType**: `🔗<enum_FastNoiseLite_DomainWarpType>`

classref-enumeration-constant

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>` **DOMAIN_WARP_SIMPLEX** = `0`

The domain is warped using the simplex noise algorithm.

classref-enumeration-constant

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>` **DOMAIN_WARP_SIMPLEX_REDUCED** = `1`

The domain is warped using a simplified version of the simplex noise algorithm.

classref-enumeration-constant

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>` **DOMAIN_WARP_BASIC_GRID** = `2`

The domain is warped using a simple noise grid (not as smooth as the other methods, but more performant).

classref-item-separator

classref-enumeration

enum **DomainWarpFractalType**: `🔗<enum_FastNoiseLite_DomainWarpFractalType>`

classref-enumeration-constant

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>` **DOMAIN_WARP_FRACTAL_NONE** = `0`

No fractal noise for warping the space.

classref-enumeration-constant

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>` **DOMAIN_WARP_FRACTAL_PROGRESSIVE** = `1`

Warping the space progressively, octave for octave, resulting in a more "liquified" distortion.

classref-enumeration-constant

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>` **DOMAIN_WARP_FRACTAL_INDEPENDENT** = `2`

Warping the space independently for each octave, resulting in a more chaotic distortion.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>` **cellular_distance_function** = `0` `🔗<class_FastNoiseLite_property_cellular_distance_function>`

classref-property-setget

- `void (No return value.)` **set_cellular_distance_function**(value: `CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>`)
- `CellularDistanceFunction<enum_FastNoiseLite_CellularDistanceFunction>` **get_cellular_distance_function**()

Determines how the distance to the nearest/second-nearest point is computed.

classref-item-separator

classref-property

`float<class_float>` **cellular_jitter** = `1.0` `🔗<class_FastNoiseLite_property_cellular_jitter>`

classref-property-setget

- `void (No return value.)` **set_cellular_jitter**(value: `float<class_float>`)
- `float<class_float>` **get_cellular_jitter**()

Maximum distance a point can move off of its grid position. Set to `0` for an even grid.

classref-item-separator

classref-property

`CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **cellular_return_type** = `1` `🔗<class_FastNoiseLite_property_cellular_return_type>`

classref-property-setget

- `void (No return value.)` **set_cellular_return_type**(value: `CellularReturnType<enum_FastNoiseLite_CellularReturnType>`)
- `CellularReturnType<enum_FastNoiseLite_CellularReturnType>` **get_cellular_return_type**()

Return type from cellular noise calculations.

classref-item-separator

classref-property

`float<class_float>` **domain_warp_amplitude** = `30.0` `🔗<class_FastNoiseLite_property_domain_warp_amplitude>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_amplitude**(value: `float<class_float>`)
- `float<class_float>` **get_domain_warp_amplitude**()

Sets the maximum warp distance from the origin.

classref-item-separator

classref-property

`bool<class_bool>` **domain_warp_enabled** = `false` `🔗<class_FastNoiseLite_property_domain_warp_enabled>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_domain_warp_enabled**()

If enabled, another FastNoiseLite instance is used to warp the space, resulting in a distortion of the noise.

classref-item-separator

classref-property

`float<class_float>` **domain_warp_fractal_gain** = `0.5` `🔗<class_FastNoiseLite_property_domain_warp_fractal_gain>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_fractal_gain**(value: `float<class_float>`)
- `float<class_float>` **get_domain_warp_fractal_gain**()

Determines the strength of each subsequent layer of the noise which is used to warp the space.

A low value places more emphasis on the lower frequency base layers, while a high value puts more emphasis on the higher frequency layers.

classref-item-separator

classref-property

`float<class_float>` **domain_warp_fractal_lacunarity** = `6.0` `🔗<class_FastNoiseLite_property_domain_warp_fractal_lacunarity>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_fractal_lacunarity**(value: `float<class_float>`)
- `float<class_float>` **get_domain_warp_fractal_lacunarity**()

The change in frequency between octaves, also known as "lacunarity", of the fractal noise which warps the space. Increasing this value results in higher octaves, producing noise with finer details and a rougher appearance.

classref-item-separator

classref-property

`int<class_int>` **domain_warp_fractal_octaves** = `5` `🔗<class_FastNoiseLite_property_domain_warp_fractal_octaves>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_fractal_octaves**(value: `int<class_int>`)
- `int<class_int>` **get_domain_warp_fractal_octaves**()

The number of noise layers that are sampled to get the final value for the fractal noise which warps the space.

classref-item-separator

classref-property

`DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>` **domain_warp_fractal_type** = `1` `🔗<class_FastNoiseLite_property_domain_warp_fractal_type>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_fractal_type**(value: `DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>`)
- `DomainWarpFractalType<enum_FastNoiseLite_DomainWarpFractalType>` **get_domain_warp_fractal_type**()

The method for combining octaves into a fractal which is used to warp the space.

classref-item-separator

classref-property

`float<class_float>` **domain_warp_frequency** = `0.05` `🔗<class_FastNoiseLite_property_domain_warp_frequency>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_frequency**(value: `float<class_float>`)
- `float<class_float>` **get_domain_warp_frequency**()

Frequency of the noise which warps the space. Low frequency results in smooth noise while high frequency results in rougher, more granular noise.

classref-item-separator

classref-property

`DomainWarpType<enum_FastNoiseLite_DomainWarpType>` **domain_warp_type** = `0` `🔗<class_FastNoiseLite_property_domain_warp_type>`

classref-property-setget

- `void (No return value.)` **set_domain_warp_type**(value: `DomainWarpType<enum_FastNoiseLite_DomainWarpType>`)
- `DomainWarpType<enum_FastNoiseLite_DomainWarpType>` **get_domain_warp_type**()

The warp algorithm.

classref-item-separator

classref-property

`float<class_float>` **fractal_gain** = `0.5` `🔗<class_FastNoiseLite_property_fractal_gain>`

classref-property-setget

- `void (No return value.)` **set_fractal_gain**(value: `float<class_float>`)
- `float<class_float>` **get_fractal_gain**()

Determines the strength of each subsequent layer of noise in fractal noise.

A low value places more emphasis on the lower frequency base layers, while a high value puts more emphasis on the higher frequency layers.

classref-item-separator

classref-property

`float<class_float>` **fractal_lacunarity** = `2.0` `🔗<class_FastNoiseLite_property_fractal_lacunarity>`

classref-property-setget

- `void (No return value.)` **set_fractal_lacunarity**(value: `float<class_float>`)
- `float<class_float>` **get_fractal_lacunarity**()

Frequency multiplier between subsequent octaves. Increasing this value results in higher octaves producing noise with finer details and a rougher appearance.

classref-item-separator

classref-property

`int<class_int>` **fractal_octaves** = `5` `🔗<class_FastNoiseLite_property_fractal_octaves>`

classref-property-setget

- `void (No return value.)` **set_fractal_octaves**(value: `int<class_int>`)
- `int<class_int>` **get_fractal_octaves**()

The number of noise layers that are sampled to get the final value for fractal noise types.

classref-item-separator

classref-property

`float<class_float>` **fractal_ping_pong_strength** = `2.0` `🔗<class_FastNoiseLite_property_fractal_ping_pong_strength>`

classref-property-setget

- `void (No return value.)` **set_fractal_ping_pong_strength**(value: `float<class_float>`)
- `float<class_float>` **get_fractal_ping_pong_strength**()

Sets the strength of the fractal ping pong type.

classref-item-separator

classref-property

`FractalType<enum_FastNoiseLite_FractalType>` **fractal_type** = `1` `🔗<class_FastNoiseLite_property_fractal_type>`

classref-property-setget

- `void (No return value.)` **set_fractal_type**(value: `FractalType<enum_FastNoiseLite_FractalType>`)
- `FractalType<enum_FastNoiseLite_FractalType>` **get_fractal_type**()

The method for combining octaves into a fractal.

classref-item-separator

classref-property

`float<class_float>` **fractal_weighted_strength** = `0.0` `🔗<class_FastNoiseLite_property_fractal_weighted_strength>`

classref-property-setget

- `void (No return value.)` **set_fractal_weighted_strength**(value: `float<class_float>`)
- `float<class_float>` **get_fractal_weighted_strength**()

Higher weighting means higher octaves have less impact if lower octaves have a large impact.

classref-item-separator

classref-property

`float<class_float>` **frequency** = `0.01` `🔗<class_FastNoiseLite_property_frequency>`

classref-property-setget

- `void (No return value.)` **set_frequency**(value: `float<class_float>`)
- `float<class_float>` **get_frequency**()

The frequency for all noise types. Low frequency results in smooth noise while high frequency results in rougher, more granular noise.

classref-item-separator

classref-property

`NoiseType<enum_FastNoiseLite_NoiseType>` **noise_type** = `1` `🔗<class_FastNoiseLite_property_noise_type>`

classref-property-setget

- `void (No return value.)` **set_noise_type**(value: `NoiseType<enum_FastNoiseLite_NoiseType>`)
- `NoiseType<enum_FastNoiseLite_NoiseType>` **get_noise_type**()

The noise algorithm used.

classref-item-separator

classref-property

`Vector3<class_Vector3>` **offset** = `Vector3(0, 0, 0)` `🔗<class_FastNoiseLite_property_offset>`

classref-property-setget

- `void (No return value.)` **set_offset**(value: `Vector3<class_Vector3>`)
- `Vector3<class_Vector3>` **get_offset**()

Translate the noise input coordinates by the given `Vector3<class_Vector3>`.

classref-item-separator

classref-property

`int<class_int>` **seed** = `0` `🔗<class_FastNoiseLite_property_seed>`

classref-property-setget

- `void (No return value.)` **set_seed**(value: `int<class_int>`)
- `int<class_int>` **get_seed**()

The random number seed for all noise types.