github_url
hide

# RandomNumberGenerator

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Provides methods for generating pseudo-random numbers.

classref-introduction-group

## Description

RandomNumberGenerator is a class for generating pseudo-random numbers. It currently uses [PCG32](https://www.pcg-random.org/).

**Note:** The underlying algorithm is an implementation detail and should not be depended upon.

To generate a random float number (within a given range) based on a time-dependent seed:

    var rng = RandomNumberGenerator.new()
    func _ready():
        var my_random_number = rng.randf_range(-10.0, 10.0)

classref-introduction-group

## Tutorials

- `Random number generation <../tutorials/math/random_number_generation>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **seed** = `0` `🔗<class_RandomNumberGenerator_property_seed>`

classref-property-setget

- `void (No return value.)` **set_seed**(value: `int<class_int>`)
- `int<class_int>` **get_seed**()

Initializes the random number generator state based on the given seed value. A given seed will give a reproducible sequence of pseudo-random numbers.

**Note:** The RNG does not have an avalanche effect, and can output similar random streams given similar seeds. Consider using a hash function to improve your seed quality if they're sourced externally.

**Note:** The default value of this property is pseudo-random, and changes when calling `randomize()<class_RandomNumberGenerator_method_randomize>`. The `0` value documented here is a placeholder, and not the actual default seed.

**Note:** Setting this property produces a side effect of changing the internal `state<class_RandomNumberGenerator_property_state>`, so make sure to initialize the seed *before* modifying the `state<class_RandomNumberGenerator_property_state>`:

    var rng = RandomNumberGenerator.new()
    rng.seed = hash("Godot")
    rng.state = 100 # Restore to some previously saved state.

classref-item-separator

classref-property

`int<class_int>` **state** = `0` `🔗<class_RandomNumberGenerator_property_state>`

classref-property-setget

- `void (No return value.)` **set_state**(value: `int<class_int>`)
- `int<class_int>` **get_state**()

The current state of the random number generator. Save and restore this property to restore the generator to a previous state:

    var rng = RandomNumberGenerator.new()
    print(rng.randf())
    var saved_state = rng.state # Store current state.
    print(rng.randf()) # Advance internal state.
    rng.state = saved_state # Restore the state.
    print(rng.randf()) # Prints the same value as previously.

**Note:** Do not set state to arbitrary values, since the random number generator requires the state to have certain qualities to behave properly. It should only be set to values that came from the state property itself. To initialize the random number generator with arbitrary input, use `seed<class_RandomNumberGenerator_property_seed>` instead.

**Note:** The default value of this property is pseudo-random, and changes when calling `randomize()<class_RandomNumberGenerator_method_randomize>`. The `0` value documented here is a placeholder, and not the actual default state.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **rand_weighted**(weights: `PackedFloat32Array<class_PackedFloat32Array>`) `🔗<class_RandomNumberGenerator_method_rand_weighted>`

Returns a random integer between `0` and the size of the array that is passed as a parameter. Each value in the array should be a floating-point number that represents the relative likelihood that it will be returned as an index. A higher value means the value is more likely to be returned as an index, while a value of `0` means it will never be returned as an index.

For example, if `[0.5, 1, 1, 2]` is passed as a parameter, then the method is twice as likely to return `3` (the index of the value `2`) and twice as unlikely to return `0` (the index of the value `0.5`) compared to the indices `1` and `2`.

Prints an error and returns `-1` if the array is empty.

gdscript

var rng = RandomNumberGenerator.new()

var my_array = \["one", "two", "three", "four"\] var weights = PackedFloat32Array(\[0.5, 1, 1, 2\])

\# Prints one of the four elements in my_array. \# It is more likely to print "four", and less likely to print "one". print(my_array\[rng.rand_weighted(weights)\])

classref-item-separator

classref-method

`float<class_float>` **randf**() `🔗<class_RandomNumberGenerator_method_randf>`

Returns a pseudo-random float between `0.0` and `1.0` (inclusive).

classref-item-separator

classref-method

`float<class_float>` **randf_range**(from: `float<class_float>`, to: `float<class_float>`) `🔗<class_RandomNumberGenerator_method_randf_range>`

Returns a pseudo-random float between `from` and `to` (inclusive).

classref-item-separator

classref-method

`float<class_float>` **randfn**(mean: `float<class_float>` = 0.0, deviation: `float<class_float>` = 1.0) `🔗<class_RandomNumberGenerator_method_randfn>`

Returns a [normally-distributed](https://en.wikipedia.org/wiki/Normal_distribution), pseudo-random floating-point number from the specified `mean` and a standard `deviation`. This is also known as a Gaussian distribution.

**Note:** This method uses the [Box-Muller transform](https://en.wikipedia.org/wiki/Box%E2%80%93Muller_transform) algorithm.

classref-item-separator

classref-method

`int<class_int>` **randi**() `🔗<class_RandomNumberGenerator_method_randi>`

Returns a pseudo-random 32-bit unsigned integer between `0` and `4294967295` (inclusive).

classref-item-separator

classref-method

`int<class_int>` **randi_range**(from: `int<class_int>`, to: `int<class_int>`) `🔗<class_RandomNumberGenerator_method_randi_range>`

Returns a pseudo-random 32-bit signed integer between `from` and `to` (inclusive).

classref-item-separator

classref-method

`void (No return value.)` **randomize**() `🔗<class_RandomNumberGenerator_method_randomize>`

Sets up a time-based seed for this **RandomNumberGenerator** instance. Unlike the `@GlobalScope<class_@GlobalScope>` random number generation functions, different **RandomNumberGenerator** instances can use different seeds.