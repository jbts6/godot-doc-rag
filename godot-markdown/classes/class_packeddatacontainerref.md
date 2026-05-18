github_url
hide

# PackedDataContainerRef

**Deprecated:** Use `@GlobalScope.var_to_bytes()<class_@GlobalScope_method_var_to_bytes>` or `FileAccess.store_var()<class_FileAccess_method_store_var>` instead. To enable data compression, use `PackedByteArray.compress()<class_PackedByteArray_method_compress>` or `FileAccess.open_compressed()<class_FileAccess_method_open_compressed>`.

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

An internal class used by `PackedDataContainer<class_PackedDataContainer>` to pack nested arrays and dictionaries.

classref-introduction-group

## Description

When packing nested containers using `PackedDataContainer<class_PackedDataContainer>`, they are recursively packed into **PackedDataContainerRef** (only applies to `Array<class_Array>` and `Dictionary<class_Dictionary>`). Their data can be retrieved the same way as from `PackedDataContainer<class_PackedDataContainer>`.

    var packed = PackedDataContainer.new()
    packed.pack([1, 2, 3, ["nested1", "nested2"], 4, 5, 6])

    for element in packed:
        if element is PackedDataContainerRef:
            for subelement in element:
                print("::", subelement)
        else:
            print(element)

Prints:

``` text
1
2
3
::nested1
::nested2
4
5
6
```

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_PackedDataContainerRef_method_size>`

Returns the size of the packed container (see `Array.size()<class_Array_method_size>` and `Dictionary.size()<class_Dictionary_method_size>`).