github_url
hide

# CameraFeed

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A camera feed gives you access to a single physical camera attached to your device.

classref-introduction-group

## Description

A camera feed gives you access to a single physical camera attached to your device. When enabled, Godot will start capturing frames from the camera which can then be used. See also `CameraServer<class_CameraServer>`.

**Note:** Many cameras will return YCbCr images which are split into two textures and need to be combined in a shader. Godot does this automatically for you if you set the environment to show the camera image in the background.

**Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no **CameraFeed**s will be available. To get a **CameraFeed** on iOS, enable `EditorExportPlatformIOS.modules/camera<class_EditorExportPlatformIOS_property_modules/camera>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**format_changed**() `🔗<class_CameraFeed_signal_format_changed>`

Emitted when the format has changed.

classref-item-separator

classref-signal

**frame_changed**() `🔗<class_CameraFeed_signal_frame_changed>`

Emitted when a new frame is available.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FeedDataType**: `🔗<enum_CameraFeed_FeedDataType>`

classref-enumeration-constant

`FeedDataType<enum_CameraFeed_FeedDataType>` **FEED_NOIMAGE** = `0`

No image set for the feed.

classref-enumeration-constant

`FeedDataType<enum_CameraFeed_FeedDataType>` **FEED_RGB** = `1`

Feed supplies RGB images.

classref-enumeration-constant

`FeedDataType<enum_CameraFeed_FeedDataType>` **FEED_YCBCR** = `2`

Feed supplies YCbCr images that need to be converted to RGB.

classref-enumeration-constant

`FeedDataType<enum_CameraFeed_FeedDataType>` **FEED_YCBCR_SEP** = `3`

Feed supplies separate Y and CbCr images that need to be combined and converted to RGB.

classref-enumeration-constant

`FeedDataType<enum_CameraFeed_FeedDataType>` **FEED_EXTERNAL** = `4`

Feed supplies external image.

classref-item-separator

classref-enumeration

enum **FeedPosition**: `🔗<enum_CameraFeed_FeedPosition>`

classref-enumeration-constant

`FeedPosition<enum_CameraFeed_FeedPosition>` **FEED_UNSPECIFIED** = `0`

Unspecified position.

classref-enumeration-constant

`FeedPosition<enum_CameraFeed_FeedPosition>` **FEED_FRONT** = `1`

Camera is mounted at the front of the device.

classref-enumeration-constant

`FeedPosition<enum_CameraFeed_FeedPosition>` **FEED_BACK** = `2`

Camera is mounted at the back of the device.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **feed_is_active** = `false` `🔗<class_CameraFeed_property_feed_is_active>`

classref-property-setget

- `void (No return value.)` **set_active**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_active**()

If `true`, the feed is active.

classref-item-separator

classref-property

`Transform2D<class_Transform2D>` **feed_transform** = `Transform2D(1, 0, 0, -1, 0, 1)` `🔗<class_CameraFeed_property_feed_transform>`

classref-property-setget

- `void (No return value.)` **set_transform**(value: `Transform2D<class_Transform2D>`)
- `Transform2D<class_Transform2D>` **get_transform**()

The transform applied to the camera's image.

classref-item-separator

classref-property

`Array<class_Array>` **formats** = `[]` `🔗<class_CameraFeed_property_formats>`

classref-property-setget

- `Array<class_Array>` **get_formats**()

Formats supported by the feed. Each entry is a `Dictionary<class_Dictionary>` describing format parameters.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **\_activate_feed**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CameraFeed_private_method__activate_feed>`

Called when the camera feed is activated.

classref-item-separator

classref-method

`void (No return value.)` **\_deactivate_feed**() `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CameraFeed_private_method__deactivate_feed>`

Called when the camera feed is deactivated.

classref-item-separator

classref-method

`Array<class_Array>` **\_get_formats**() `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CameraFeed_private_method__get_formats>`

Override this method to define supported formats of the camera feed.

classref-item-separator

classref-method

`bool<class_bool>` **\_set_format**(index: `int<class_int>`, parameters: `Dictionary<class_Dictionary>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_CameraFeed_private_method__set_format>`

Override this method to set the format of the camera feed.

classref-item-separator

classref-method

`FeedDataType<enum_CameraFeed_FeedDataType>` **get_datatype**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CameraFeed_method_get_datatype>`

Returns feed image data type.

classref-item-separator

classref-method

`int<class_int>` **get_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CameraFeed_method_get_id>`

Returns the unique ID for this feed.

classref-item-separator

classref-method

`String<class_String>` **get_name**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CameraFeed_method_get_name>`

Returns the camera's name.

classref-item-separator

classref-method

`FeedPosition<enum_CameraFeed_FeedPosition>` **get_position**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_CameraFeed_method_get_position>`

Returns the position of camera on the device.

classref-item-separator

classref-method

`int<class_int>` **get_texture_tex_id**(feed_image_type: `FeedImage<enum_CameraServer_FeedImage>`) `🔗<class_CameraFeed_method_get_texture_tex_id>`

Returns the texture backend ID (usable by some external libraries that need a handle to a texture to write data).

classref-item-separator

classref-method

`void (No return value.)` **set_external**(width: `int<class_int>`, height: `int<class_int>`) `🔗<class_CameraFeed_method_set_external>`

Sets the feed as external feed provided by another library.

classref-item-separator

classref-method

`bool<class_bool>` **set_format**(index: `int<class_int>`, parameters: `Dictionary<class_Dictionary>`) `🔗<class_CameraFeed_method_set_format>`

Sets the feed format parameters for the given `index` in the `formats<class_CameraFeed_property_formats>` array. Returns `true` on success. By default, the YUYV encoded stream is transformed to `FEED_RGB<class_CameraFeed_constant_FEED_RGB>`. The YUYV encoded stream output format can be changed by setting `parameters`'s `output` entry to one of the following:

- `"separate"` will result in `FEED_YCBCR_SEP<class_CameraFeed_constant_FEED_YCBCR_SEP>`;
- `"grayscale"` will result in desaturated `FEED_RGB<class_CameraFeed_constant_FEED_RGB>`;
- `"copy"` will result in `FEED_YCBCR<class_CameraFeed_constant_FEED_YCBCR>`.

classref-item-separator

classref-method

`void (No return value.)` **set_name**(name: `String<class_String>`) `🔗<class_CameraFeed_method_set_name>`

Sets the camera's name.

classref-item-separator

classref-method

`void (No return value.)` **set_position**(position: `FeedPosition<enum_CameraFeed_FeedPosition>`) `🔗<class_CameraFeed_method_set_position>`

Sets the position of this camera.

classref-item-separator

classref-method

`void (No return value.)` **set_rgb_image**(rgb_image: `Image<class_Image>`) `🔗<class_CameraFeed_method_set_rgb_image>`

Sets RGB image for this feed.

classref-item-separator

classref-method

`void (No return value.)` **set_ycbcr_image**(ycbcr_image: `Image<class_Image>`) `🔗<class_CameraFeed_method_set_ycbcr_image>`

Sets YCbCr image for this feed.

classref-item-separator

classref-method

`void (No return value.)` **set_ycbcr_images**(y_image: `Image<class_Image>`, cbcr_image: `Image<class_Image>`) `🔗<class_CameraFeed_method_set_ycbcr_images>`

Sets Y and CbCr images for this feed.