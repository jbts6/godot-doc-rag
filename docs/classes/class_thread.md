github_url
hide

# Thread

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A unit of execution in a process.

classref-introduction-group

## Description

A unit of execution in a process. Can run methods on `Object<class_Object>`s simultaneously. The use of synchronization via `Mutex<class_Mutex>` or `Semaphore<class_Semaphore>` is advised if working with shared objects.

**Warning:** To ensure proper cleanup without crashes or deadlocks, when a **Thread**'s reference count reaches zero and it is therefore destroyed, the following conditions must be met:

- It must not have any `Mutex<class_Mutex>` objects locked.
- It must not be waiting on any `Semaphore<class_Semaphore>` objects.
- `wait_to_finish()<class_Thread_method_wait_to_finish>` should have been called on it.

classref-introduction-group

## Tutorials

- `Using multiple threads <../tutorials/performance/using_multiple_threads>`
- `Thread-safe APIs <../tutorials/performance/thread_safe_apis>`
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **Priority**: `🔗<enum_Thread_Priority>`

classref-enumeration-constant

`Priority<enum_Thread_Priority>` **PRIORITY_LOW** = `0`

A thread running with lower priority than normally.

classref-enumeration-constant

`Priority<enum_Thread_Priority>` **PRIORITY_NORMAL** = `1`

A thread with a standard priority.

classref-enumeration-constant

`Priority<enum_Thread_Priority>` **PRIORITY_HIGH** = `2`

A thread running with higher priority than normally.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`String<class_String>` **get_id**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Thread_method_get_id>`

Returns the current **Thread**'s ID, uniquely identifying it among all threads. If the **Thread** has not started running or if `wait_to_finish()<class_Thread_method_wait_to_finish>` has been called, this returns an empty string.

classref-item-separator

classref-method

`bool<class_bool>` **is_alive**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Thread_method_is_alive>`

Returns `true` if this **Thread** is currently running the provided function. This is useful for determining if `wait_to_finish()<class_Thread_method_wait_to_finish>` can be called without blocking the calling thread.

To check if a **Thread** is joinable, use `is_started()<class_Thread_method_is_started>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_main_thread**() `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Thread_method_is_main_thread>`

Returns `true` if the thread this method was called from is the main thread.

**Note:** This is a static method and isn't associated with a specific **Thread** object.

classref-item-separator

classref-method

`bool<class_bool>` **is_started**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Thread_method_is_started>`

Returns `true` if this **Thread** has been started. Once started, this will return `true` until it is joined using `wait_to_finish()<class_Thread_method_wait_to_finish>`. For checking if a **Thread** is still executing its task, use `is_alive()<class_Thread_method_is_alive>`.

classref-item-separator

classref-method

`void (No return value.)` **set_thread_safety_checks_enabled**(enabled: `bool<class_bool>`) `static (This method doesn't need an instance to be called, so it can be called directly using the class name.)` `🔗<class_Thread_method_set_thread_safety_checks_enabled>`

Sets whether the thread safety checks the engine normally performs in methods of certain classes (e.g., `Node<class_Node>`) should happen **on the current thread**.

The default, for every thread, is that they are enabled (as if called with `enabled` being `true`).

Those checks are conservative. That means that they will only succeed in considering a call thread-safe (and therefore allow it to happen) if the engine can guarantee such safety.

Because of that, there may be cases where the user may want to disable them (`enabled` being `false`) to make certain operations allowed again. By doing so, it becomes the user's responsibility to ensure thread safety (e.g., by using `Mutex<class_Mutex>`) for those objects that are otherwise protected by the engine.

**Note:** This is an advanced usage of the engine. You are advised to use it only if you know what you are doing and there is no safer way.

**Note:** This is useful for scripts running on either arbitrary **Thread** objects or tasks submitted to the `WorkerThreadPool<class_WorkerThreadPool>`. It doesn't apply to code running during `Node<class_Node>` group processing, where the checks will be always performed.

**Note:** Even in the case of having disabled the checks in a `WorkerThreadPool<class_WorkerThreadPool>` task, there's no need to re-enable them at the end. The engine will do so.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **start**(callable: `Callable<class_Callable>`, priority: `Priority<enum_Thread_Priority>` = 1) `🔗<class_Thread_method_start>`

Starts a new **Thread** that calls `callable`.

If the method takes some arguments, you can pass them using `Callable.bind()<class_Callable_method_bind>`.

The `priority` of the **Thread** can be changed by passing a value from the `Priority<enum_Thread_Priority>` enum.

Returns `@GlobalScope.OK<class_@GlobalScope_constant_OK>` on success, or `@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>` on failure.

classref-item-separator

classref-method

`Variant<class_Variant>` **wait_to_finish**() `🔗<class_Thread_method_wait_to_finish>`

Joins the **Thread** and waits for it to finish. Returns the output of the `Callable<class_Callable>` passed to `start()<class_Thread_method_start>`.

Should either be used when you want to retrieve the value returned from the method called by the **Thread** or before freeing the instance that contains the **Thread**.

To determine if this can be called without blocking the calling thread, check if `is_alive()<class_Thread_method_is_alive>` is `false`.