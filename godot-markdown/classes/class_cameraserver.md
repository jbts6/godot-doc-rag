github_url
hide

# CameraServer

**Inherits:** `Object<class_Object>`

Server keeping track of different cameras accessible in Godot.

classref-introduction-group

## Description

The **CameraServer** keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

It is notably used to provide AR modules with a video feed from the camera.

**Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no `CameraFeed<class_CameraFeed>`s will be available. To get a `CameraFeed<class_CameraFeed>` on iOS, enable `EditorExportPlatformIOS.modules/camera<class_EditorExportPlatformIOS_property_modules/camera>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**camera_feed_added**(id: `int<class_int>`) `🔗<class_CameraServer_signal_camera_feed_added>`

Emitted when a `CameraFeed<class_CameraFeed>` is added (e.g. a webcam is plugged in).

classref-item-separator

classref-signal

**camera_feed_removed**(id: `int<class_int>`) `🔗<class_CameraServer_signal_camera_feed_removed>`

Emitted when a `CameraFeed<class_CameraFeed>` is removed (e.g. a webcam is unplugged).

classref-item-separator

classref-signal

**camera_feeds_updated**() `🔗<class_CameraServer_signal_camera_feeds_updated>`

Emitted when camera feeds are updated.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **FeedImage**: `🔗<enum_CameraServer_FeedImage>`

classref-enumeration-constant

`FeedImage<enum_CameraServer_FeedImage>` **FEED_RGBA_IMAGE** = `0`

The RGBA camera image.

classref-enumeration-constant

`FeedImage<enum_CameraServer_FeedImage>` **FEED_YCBCR_IMAGE** = `0`

The [YCbCr](https://en.wikipedia.org/wiki/YCbCr) camera image.

classref-enumeration-constant

`FeedImage<enum_CameraServer_FeedImage>` **FEED_Y_IMAGE** = `0`

The Y component camera image.

classref-enumeration-constant

`FeedImage<enum_CameraServer_FeedImage>` **FEED_CBCR_IMAGE** = `1`

The CbCr component camera image.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **monitoring_feeds** = `false` `🔗<class_CameraServer_property_monitoring_feeds>`

classref-property-setget

- `void (No return value.)` **set_monitoring_feeds**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_monitoring_feeds**()

If `true`, the server is actively monitoring available camera feeds.

This has a performance cost, so only set it to `true` when you're actively accessing the camera.

**Note:** After setting it to `true`, you can receive updated camera feeds through the `camera_feeds_updated<class_CameraServer_signal_camera_feeds_updated>` signal.

gdscript

func ready():
CameraServer.camera_feeds_updated.connect(on_camera_feeds_updated) CameraServer.monitoring_feeds = true

func on_camera_feeds_updated():
var feeds = CameraServer.feeds()

csharp

public override void Ready() { CameraServer.CameraFeedsUpdated += OnCameraFeedsUpdated; CameraServer.MonitoringFeeds = true; }

void OnCameraFeedsUpdated() { var feeds = CameraServer.Feeds(); }

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_feed**(feed: `CameraFeed<class_CameraFeed>`) `🔗<class_CameraServer_method_add_feed>`

Adds the camera `feed` to the camera server.

classref-item-separator

classref-method

`Array<class_Array>`\[`CameraFeed<class_CameraFeed>`\] **feeds**() `🔗<class_CameraServer_method_feeds>`

Returns an array of `CameraFeed<class_CameraFeed>`s.

classref-item-separator

classref-method

`CameraFeed<class_CameraFeed>` **get_feed**(index: `int<class_int>`) `🔗<class_CameraServer_method_get_feed>`

Returns the `CameraFeed<class_CameraFeed>` corresponding to the camera with the given `index`.

classref-item-separator

classref-method

`int<class_int>` **get_feed_count**() `🔗<class_CameraServer_method_get_feed_count>`

Returns the number of `CameraFeed<class_CameraFeed>`s registered.

classref-item-separator

classref-method

`void (No return value.)` **remove_feed**(feed: `CameraFeed<class_CameraFeed>`) `🔗<class_CameraServer_method_remove_feed>`

Removes the specified camera `feed`.