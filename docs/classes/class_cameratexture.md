github_url
hide

# CameraTexture

**Inherits:** `Texture2D<class_Texture2D>` **\<** `Texture<class_Texture>` **\<** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Texture provided by a `CameraFeed<class_CameraFeed>`.

classref-introduction-group

## Description

This texture gives access to the camera texture provided by a `CameraFeed<class_CameraFeed>`.

**Note:** Many cameras supply YCbCr images which need to be converted in a shader.

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **camera_feed_id** = `0` `🔗<class_CameraTexture_property_camera_feed_id>`

classref-property-setget

- `void (No return value.)` **set_camera_feed_id**(value: `int<class_int>`)
- `int<class_int>` **get_camera_feed_id**()

The ID of the `CameraFeed<class_CameraFeed>` for which we want to display the image.

classref-item-separator

classref-property

`bool<class_bool>` **camera_is_active** = `false` `🔗<class_CameraTexture_property_camera_is_active>`

classref-property-setget

- `void (No return value.)` **set_camera_active**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_camera_active**()

Convenience property that gives access to the active property of the `CameraFeed<class_CameraFeed>`.

classref-item-separator

classref-property

`FeedImage<enum_CameraServer_FeedImage>` **which_feed** = `0` `🔗<class_CameraTexture_property_which_feed>`

classref-property-setget

- `void (No return value.)` **set_which_feed**(value: `FeedImage<enum_CameraServer_FeedImage>`)
- `FeedImage<enum_CameraServer_FeedImage>` **get_which_feed**()

Which image within the `CameraFeed<class_CameraFeed>` we want access to, important if the camera image is split in a Y and CbCr component.