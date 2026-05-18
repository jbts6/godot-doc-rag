github_url
hide

# OpenXRFutureResult

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Result object tracking the asynchronous result of an OpenXR Future object.

classref-introduction-group

## Description

Result object tracking the asynchronous result of an OpenXR Future object, you can use this object to track the result status.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**completed**(result: `OpenXRFutureResult<class_OpenXRFutureResult>`) `🔗<class_OpenXRFutureResult_signal_completed>`

Emitted when the asynchronous function is finished or has been cancelled.

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ResultStatus**: `🔗<enum_OpenXRFutureResult_ResultStatus>`

classref-enumeration-constant

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>` **RESULT_RUNNING** = `0`

The asynchronous function is running.

classref-enumeration-constant

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>` **RESULT_FINISHED** = `1`

The asynchronous function has finished.

classref-enumeration-constant

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>` **RESULT_CANCELLED** = `2`

The asynchronous function has been cancelled.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **cancel_future**() `🔗<class_OpenXRFutureResult_method_cancel_future>`

Cancel this future, this will interrupt and stop the asynchronous function.

classref-item-separator

classref-method

`int<class_int>` **get_future**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRFutureResult_method_get_future>`

Return the `XrFutureEXT` value this result relates to.

classref-item-separator

classref-method

`Variant<class_Variant>` **get_result_value**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRFutureResult_method_get_result_value>`

Returns the result value of our asynchronous function (if set by the extension). The type of this result value depends on the function being called. Consult the documentation of the relevant function.

classref-item-separator

classref-method

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>` **get_status**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_OpenXRFutureResult_method_get_status>`

Returns the status of this result.

classref-item-separator

classref-method

`void (No return value.)` **set_result_value**(result_value: `Variant<class_Variant>`) `🔗<class_OpenXRFutureResult_method_set_result_value>`

Stores the result value we expose to the user.

**Note:** This method should only be called by an OpenXR extension that implements an asynchronous function.