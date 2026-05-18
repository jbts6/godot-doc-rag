github_url
hide

# AwaitTweener

**Inherits:** `Tweener<class_Tweener>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Awaits a specified signal.

classref-introduction-group

## Description

**AwaitTweener** is used to await a specified signal, allowing asynchronous steps in `Tween<class_Tween>` animation. See `Tween.tween_await()<class_Tween_method_tween_await>` for more usage information.

The `Tweener.finished<class_Tweener_signal_finished>` signal is emitted when either the awaited signal is received, when timeout is reached, or when the target object is freed.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`AwaitTweener<class_AwaitTweener>` **set_timeout**(timeout: `float<class_float>`) `🔗<class_AwaitTweener_method_set_timeout>`

Sets the maximum time an **AwaitTweener** can wait for the signal. Can be used as a safeguard for signals that may never be emitted. If not specified, the tweener will wait indefinitely.