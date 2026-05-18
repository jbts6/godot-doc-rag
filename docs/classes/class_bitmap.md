github_url
hide

# BitMap

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Boolean matrix.

classref-introduction-group

## Description

A two-dimensional array of boolean values, can be used to efficiently store a binary matrix (every matrix element takes only one bit) and query the values using natural cartesian coordinates.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Image<class_Image>` **convert_to_image**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BitMap_method_convert_to_image>`

Returns an image of the same size as the bitmap and with an `Format<enum_Image_Format>` of type `Image.FORMAT_L8<class_Image_constant_FORMAT_L8>`. `true` bits of the bitmap are being converted into white pixels, and `false` bits into black.

classref-item-separator

classref-method

`void (No return value.)` **create**(size: `Vector2i<class_Vector2i>`) `🔗<class_BitMap_method_create>`

Creates a bitmap with the specified size, filled with `false`.

classref-item-separator

classref-method

`void (No return value.)` **create_from_image_alpha**(image: `Image<class_Image>`, threshold: `float<class_float>` = 0.1) `🔗<class_BitMap_method_create_from_image_alpha>`

Creates a bitmap that matches the given image dimensions, every element of the bitmap is set to `false` if the alpha value of the image at that position is equal to `threshold` or less, and `true` in other case.

classref-item-separator

classref-method

`bool<class_bool>` **get_bit**(x: `int<class_int>`, y: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BitMap_method_get_bit>`

Returns bitmap's value at the specified position.

classref-item-separator

classref-method

`bool<class_bool>` **get_bitv**(position: `Vector2i<class_Vector2i>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BitMap_method_get_bitv>`

Returns bitmap's value at the specified position.

classref-item-separator

classref-method

`Vector2i<class_Vector2i>` **get_size**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BitMap_method_get_size>`

Returns bitmap's dimensions.

classref-item-separator

classref-method

`int<class_int>` **get_true_bit_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BitMap_method_get_true_bit_count>`

Returns the number of bitmap elements that are set to `true`.

classref-item-separator

classref-method

`void (No return value.)` **grow_mask**(pixels: `int<class_int>`, rect: `Rect2i<class_Rect2i>`) `🔗<class_BitMap_method_grow_mask>`

Applies morphological dilation or erosion to the bitmap. If `pixels` is positive, dilation is applied to the bitmap. If `pixels` is negative, erosion is applied to the bitmap. `rect` defines the area where the morphological operation is applied. Pixels located outside the `rect` are unaffected by `grow_mask()<class_BitMap_method_grow_mask>`.

classref-item-separator

classref-method

`Array<class_Array>`\[`PackedVector2Array<class_PackedVector2Array>`\] **opaque_to_polygons**(rect: `Rect2i<class_Rect2i>`, epsilon: `float<class_float>` = 2.0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_BitMap_method_opaque_to_polygons>`

Creates an `Array<class_Array>` of polygons covering a rectangular portion of the bitmap. It uses a marching squares algorithm, followed by Ramer-Douglas-Peucker (RDP) reduction of the number of vertices. Each polygon is described as a `PackedVector2Array<class_PackedVector2Array>` of its vertices.

To get polygons covering the whole bitmap, pass:

    Rect2(Vector2(), get_size())

`epsilon` is passed to RDP to control how accurately the polygons cover the bitmap: a lower `epsilon` corresponds to more points in the polygons.

classref-item-separator

classref-method

`void (No return value.)` **resize**(new_size: `Vector2i<class_Vector2i>`) `🔗<class_BitMap_method_resize>`

Resizes the image to `new_size`.

classref-item-separator

classref-method

`void (No return value.)` **set_bit**(x: `int<class_int>`, y: `int<class_int>`, bit: `bool<class_bool>`) `🔗<class_BitMap_method_set_bit>`

Sets the bitmap's element at the specified position, to the specified value.

classref-item-separator

classref-method

`void (No return value.)` **set_bit_rect**(rect: `Rect2i<class_Rect2i>`, bit: `bool<class_bool>`) `🔗<class_BitMap_method_set_bit_rect>`

Sets a rectangular portion of the bitmap to the specified value.

classref-item-separator

classref-method

`void (No return value.)` **set_bitv**(position: `Vector2i<class_Vector2i>`, bit: `bool<class_bool>`) `🔗<class_BitMap_method_set_bitv>`

Sets the bitmap's element at the specified position, to the specified value.