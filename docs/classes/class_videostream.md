github_url
hide

# VideoStream

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `VideoStreamTheora<class_VideoStreamTheora>`

Base resource for video streams.

classref-introduction-group

## Description

Base resource type for all video streams. Classes that derive from **VideoStream** can all be used as resource types to play back videos in `VideoStreamPlayer<class_VideoStreamPlayer>`.

classref-introduction-group

## Tutorials

- `Playing videos <../tutorials/animation/playing_videos>`
- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **file** = `""` `🔗<class_VideoStream_property_file>`

classref-property-setget

- `void (No return value.)` **set_file**(value: `String<class_String>`)
- `String<class_String>` **get_file**()

The video file path or URI that this **VideoStream** resource handles.

For `VideoStreamTheora<class_VideoStreamTheora>`, this filename should be an Ogg Theora video file with the `.ogv` extension.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`VideoStreamPlayback<class_VideoStreamPlayback>` **\_instantiate_playback**() `virtual (This method should typically be overridden by the user to have any effect.)` `required (This method is required to be overridden when extending its base class.)` `🔗<class_VideoStream_private_method__instantiate_playback>`

Called when the video starts playing, to initialize and return a subclass of `VideoStreamPlayback<class_VideoStreamPlayback>`.