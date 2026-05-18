github_url
hide

# OpenXRFrameSynthesisExtension

**Inherits:** `OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>` **\<** `Object<class_Object>`

The OpenXR Frame synthesis extension allows for advanced reprojection at low(er) framerates.

classref-introduction-group

## Description

This class implements the [OpenXR Frame synthesis extension](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_frame_synthesis). When enabled in the project settings and supported by the XR runtime in use, frame synthesis uses advanced reprojection techniques to inject additional frames so that your XR experience hits the full frame rate of the device.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **enabled** = `false` `🔗<class_OpenXRFrameSynthesisExtension_property_enabled>`

classref-property-setget

- `void (No return value.)` **set_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_enabled**()

Enable frame synthesis. When `true` motion vector and depth data is provided to the XR runtime.

classref-item-separator

classref-property

`bool<class_bool>` **relax_frame_interval** = `false` `🔗<class_OpenXRFrameSynthesisExtension_property_relax_frame_interval>`

classref-property-setget

- `void (No return value.)` **set_relax_frame_interval**(value: `bool<class_bool>`)
- `bool<class_bool>` **get_relax_frame_interval**()

If `true` this informs the XR runtime we will be providing frames at a greatly reduced rate. Enable this when you expect your application to run at low framerates and wish to inject multiple reprojected frames.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`bool<class_bool>` **is_available**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRFrameSynthesisExtension_method_is_available>`

Returns `true` if frame synthesis is enabled in the project settings and the current XR runtime supports frame synthesis. The value returned will only be valid once OpenXR has been initialized.

classref-item-separator

classref-method

`void (No return value.)` **skip_next_frame**() `🔗<class_OpenXRFrameSynthesisExtension_method_skip_next_frame>`

Queues the next frame to be skipped when supplying motion vector and depth data. Call this after teleporting your player or a similar action has moved the player to prevent incorrect reprojection results due to this movement.