github_url
hide

# PackedInt64Array

A packed array of 64-bit integers.

classref-introduction-group

## Description

An array specifically designed to hold 64-bit integer values. Packs data tightly, so it saves memory for large array sizes.

**Note:** This type stores signed 64-bit integers, which means it can take values in the interval `[-2^63, 2^63 - 1]`, i.e. `[-9223372036854775808, 9223372036854775807]`. Exceeding those bounds will wrap around. If you only need to pack 32-bit integers tightly, see `PackedInt32Array<class_PackedInt32Array>` for a more memory-friendly alternative.

**Differences between packed arrays, typed arrays, and untyped arrays:** Packed arrays are generally faster to iterate on and modify compared to a typed array of the same type (e.g. **PackedInt64Array** versus `Array[int]`). Also, packed arrays consume less memory. As a downside, packed arrays are less flexible as they don't offer as many convenience methods such as `Array.map()<class_Array_method_map>`. Typed arrays are in turn faster to iterate on and modify than untyped arrays.

**Note:** Packed arrays are always passed by reference. To get a copy of an array that can be modified independently of the original array, use `duplicate()<class_PackedInt64Array_method_duplicate>`. This is *not* the case for built-in properties and methods. In these cases the returned packed array is a copy, and changing it will *not* affect the original value. To update a built-in property of this type, modify the returned array and then assign it to the property again.

**Note:** In a boolean context, a packed array will evaluate to `false` if it's empty. Otherwise, a packed array will always evaluate to `true`.

> [!NOTE]
> There are notable differences when using this API with C#. See `doc_c_sharp_differences` for more information.

classref-reftable-group

## Constructors

classref-reftable-group

## Methods

classref-reftable-group

## Operators

classref-section-separator

classref-descriptions-group

## Constructor Descriptions

classref-constructor

`PackedInt64Array<class_PackedInt64Array>` **PackedInt64Array**() `🔗<class_PackedInt64Array_constructor_PackedInt64Array>`

Constructs an empty **PackedInt64Array**.

classref-item-separator

classref-constructor

`PackedInt64Array<class_PackedInt64Array>` **PackedInt64Array**(from: `PackedInt64Array<class_PackedInt64Array>`)

Constructs a **PackedInt64Array** as a copy of the given **PackedInt64Array**.

classref-item-separator

classref-constructor

`PackedInt64Array<class_PackedInt64Array>` **PackedInt64Array**(from: `Array<class_Array>`)

Constructs a new **PackedInt64Array**. Optionally, you can pass in a generic `Array<class_Array>` that will be converted.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **append**(value: `int<class_int>`) `🔗<class_PackedInt64Array_method_append>`

Appends an element at the end of the array (alias of `push_back()<class_PackedInt64Array_method_push_back>`).

classref-item-separator

classref-method

`void (No return value.)` **append_array**(array: `PackedInt64Array<class_PackedInt64Array>`) `🔗<class_PackedInt64Array_method_append_array>`

Appends a **PackedInt64Array** at the end of this array.

classref-item-separator

classref-method

`int<class_int>` **bsearch**(value: `int<class_int>`, before: `bool<class_bool>` = true) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_bsearch>`

Finds the index of an existing value (or the insertion index that maintains sorting order, if the value is not yet present in the array) using binary search. Optionally, a `before` specifier can be passed. If `false`, the returned index comes after all existing entries of the value in the array.

**Note:** Calling `bsearch()<class_PackedInt64Array_method_bsearch>` on an unsorted array results in unexpected behavior.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_PackedInt64Array_method_clear>`

Clears the array. This is equivalent to using `resize()<class_PackedInt64Array_method_resize>` with a size of `0`.

classref-item-separator

classref-method

`int<class_int>` **count**(value: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_count>`

Returns the number of times an element is in the array.

classref-item-separator

classref-method

`PackedInt64Array<class_PackedInt64Array>` **duplicate**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_duplicate>`

Creates a copy of the array, and returns it.

classref-item-separator

classref-method

`bool<class_bool>` **erase**(value: `int<class_int>`) `🔗<class_PackedInt64Array_method_erase>`

Removes the first occurrence of a value from the array and returns `true`. If the value does not exist in the array, nothing happens and `false` is returned. To remove an element by index, use `remove_at()<class_PackedInt64Array_method_remove_at>` instead.

classref-item-separator

classref-method

`void (No return value.)` **fill**(value: `int<class_int>`) `🔗<class_PackedInt64Array_method_fill>`

Assigns the given value to all elements in the array. This can typically be used together with `resize()<class_PackedInt64Array_method_resize>` to create an array with a given size and initialized elements.

classref-item-separator

classref-method

`int<class_int>` **find**(value: `int<class_int>`, from: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_find>`

Searches the array for a value and returns its index or `-1` if not found. Optionally, the initial search index can be passed.

classref-item-separator

classref-method

`int<class_int>` **get**(index: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_get>`

Returns the 64-bit integer at the given `index` in the array. If `index` is out-of-bounds or negative, this method fails and returns `0`.

This method is similar (but not identical) to the `[]` operator. Most notably, when this method fails, it doesn't pause project execution if run from the editor.

classref-item-separator

classref-method

`bool<class_bool>` **has**(value: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_has>`

Returns `true` if the array contains `value`.

classref-item-separator

classref-method

`int<class_int>` **insert**(at_index: `int<class_int>`, value: `int<class_int>`) `🔗<class_PackedInt64Array_method_insert>`

Inserts a new integer at a given position in the array. The position must be valid, or at the end of the array (`idx == size()`).

classref-item-separator

classref-method

`bool<class_bool>` **is_empty**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_is_empty>`

Returns `true` if the array is empty.

classref-item-separator

classref-method

`bool<class_bool>` **push_back**(value: `int<class_int>`) `🔗<class_PackedInt64Array_method_push_back>`

Appends a value to the array.

classref-item-separator

classref-method

`void (No return value.)` **remove_at**(index: `int<class_int>`) `🔗<class_PackedInt64Array_method_remove_at>`

Removes an element from the array by index.

classref-item-separator

classref-method

`int<class_int>` **resize**(new_size: `int<class_int>`) `🔗<class_PackedInt64Array_method_resize>`

Sets the size of the array. If the array is grown, reserves elements at the end of the array. If the array is shrunk, truncates the array to the new size. Calling `resize()<class_PackedInt64Array_method_resize>` once and assigning the new values is faster than adding new elements one by one.

Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success, or one of the following `Error<enum_@GlobalScope_Error>` constants if this method fails: `@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>` if the size is negative, or `@GlobalScope.ERR_OUT_OF_MEMORY<class_@GlobalScope_constant_ERR_OUT_OF_MEMORY>` if allocations fail. Use `size()<class_PackedInt64Array_method_size>` to find the actual size of the array after resize.

classref-item-separator

classref-method

`void (No return value.)` **reverse**() `🔗<class_PackedInt64Array_method_reverse>`

Reverses the order of the elements in the array.

classref-item-separator

classref-method

`int<class_int>` **rfind**(value: `int<class_int>`, from: `int<class_int>` = -1) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_rfind>`

Searches the array in reverse order. Optionally, a start search index can be passed. If negative, the start index is considered relative to the end of the array.

classref-item-separator

classref-method

`void (No return value.)` **set**(index: `int<class_int>`, value: `int<class_int>`) `🔗<class_PackedInt64Array_method_set>`

Changes the integer at the given index.

classref-item-separator

classref-method

`int<class_int>` **size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_size>`

Returns the number of elements in the array.

classref-item-separator

classref-method

`PackedInt64Array<class_PackedInt64Array>` **slice**(begin: `int<class_int>`, end: `int<class_int>` = 2147483647) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_slice>`

Returns the slice of the **PackedInt64Array**, from `begin` (inclusive) to `end` (exclusive), as a new **PackedInt64Array**.

The absolute value of `begin` and `end` will be clamped to the array size, so the default value for `end` makes it slice to the size of the array by default (i.e. `arr.slice(1)` is a shorthand for `arr.slice(1, arr.size())`).

If either `begin` or `end` are negative, they will be relative to the end of the array (i.e. `arr.slice(0, -2)` is a shorthand for `arr.slice(0, arr.size() - 2)`).

classref-item-separator

classref-method

`void (No return value.)` **sort**() `🔗<class_PackedInt64Array_method_sort>`

Sorts the elements of the array in ascending order.

classref-item-separator

classref-method

`PackedByteArray<class_PackedByteArray>` **to_byte_array**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedInt64Array_method_to_byte_array>`

Returns a copy of the data converted to a `PackedByteArray<class_PackedByteArray>`, where each element has been encoded as 8 bytes.

The size of the new array will be `int64_array.size() * 8`.

classref-section-separator

classref-descriptions-group

## Operator Descriptions

classref-operator

`bool<class_bool>` **operator !=**(right: `PackedInt64Array<class_PackedInt64Array>`) `🔗<class_PackedInt64Array_operator_neq_PackedInt64Array>`

Returns `true` if contents of the arrays differ.

classref-item-separator

classref-operator

`PackedInt64Array<class_PackedInt64Array>` **operator +**(right: `PackedInt64Array<class_PackedInt64Array>`) `🔗<class_PackedInt64Array_operator_sum_PackedInt64Array>`

Returns a new **PackedInt64Array** with contents of `right` added at the end of this array. For better performance, consider using `append_array()<class_PackedInt64Array_method_append_array>` instead.

classref-item-separator

classref-operator

`bool<class_bool>` **operator ==**(right: `PackedInt64Array<class_PackedInt64Array>`) `🔗<class_PackedInt64Array_operator_eq_PackedInt64Array>`

Returns `true` if contents of both arrays are the same, i.e. they have all equal ints at the corresponding indices.

classref-item-separator

classref-operator

`int<class_int>` **operator \[\]**(index: `int<class_int>`) `🔗<class_PackedInt64Array_operator_idx_int>`

Returns the `int<class_int>` at index `index`. Negative indices can be used to access the elements starting from the end. Using index out of array's bounds will result in an error.