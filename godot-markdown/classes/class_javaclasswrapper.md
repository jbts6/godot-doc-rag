github_url
hide

# JavaClassWrapper

**Inherits:** `Object<class_Object>`

Provides access to the Java Native Interface.

classref-introduction-group

## Description

The JavaClassWrapper singleton provides a way for the Godot application to send and receive data through the [Java Native Interface](https://developer.android.com/training/articles/perf-jni) (JNI).

**Note:** This singleton is only available in Android builds.

    var LocalDateTime = JavaClassWrapper.wrap("java.time.LocalDateTime")
    var DateTimeFormatter = JavaClassWrapper.wrap("java.time.format.DateTimeFormatter")

    var datetime = LocalDateTime.now()
    var formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")

    print(datetime.format(formatter))

**Warning:** When calling Java methods, be sure to check `get_exception()<class_JavaClassWrapper_method_get_exception>` to check if the method threw an exception.

classref-introduction-group

## Tutorials

- `Integrating with Android APIs <../tutorials/platform/android/javaclasswrapper_and_androidruntimeplugin>`

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`JavaObject<class_JavaObject>` **create_proxy**(object: `Object<class_Object>`, interfaces: `PackedStringArray<class_PackedStringArray>`) `🔗<class_JavaClassWrapper_method_create_proxy>`

Creates a `JavaObject<class_JavaObject>` implementing the given Java interfaces using the given `Object<class_Object>` as the implementation.

The `object` must contain methods signatures matching the methods signatures from the passed Java `interfaces`. Invoking methods from the Java `interfaces` will route to the matching `object` method.

    class PrintProxy:
        func println(content: String) -> void:
            print(content)

    var print_proxy = PrintProxy.new()
    var printer_object = JavaClassWrapper.create_proxy(print_proxy, ["android.util.Printer"])
    printer_object.println("Hello Godot World!")

**Note:** This method only works on Android. On every other platform, this method will always return `null`.

classref-item-separator

classref-method

`JavaObject<class_JavaObject>` **create_sam_callback**(sam_interface: `String<class_String>`, callable: `Callable<class_Callable>`) `🔗<class_JavaClassWrapper_method_create_sam_callback>`

Creates a `JavaObject<class_JavaObject>` implementing the Java Single Abstract Method (SAM) interface using the Godot `Callable<class_Callable>` as the implementation.

The `sam_interface` **must be** a Java SAM interface, meaning it must only have a single abstract method to implement.

The `callable` must be able to handle the same parameter types as the SAM interface method, and must provide the same return type. The `callable` will be invoked as a callback, passing the arguments from the Java SAM interface method.

    var cb = func (content: String) -> void:
        print(content)
    var callback = JavaClassWrapper.create_sam_callback("android.util.Printer", cb)
    callback.println("Hello Godot World!")

**Note:** This method only works on Android. On every other platform, this method will always return `null`.

classref-item-separator

classref-method

`JavaObject<class_JavaObject>` **get_exception**() `🔗<class_JavaClassWrapper_method_get_exception>`

Returns the Java exception from the last call into a Java class. If there was no exception, it will return `null`.

**Note:** This method only works on Android. On every other platform, this method will always return `null`.

classref-item-separator

classref-method

`JavaClass<class_JavaClass>` **wrap**(name: `String<class_String>`) `🔗<class_JavaClassWrapper_method_wrap>`

Wraps a class defined in Java, and returns it as a `JavaClass<class_JavaClass>` `Object<class_Object>` type that Godot can interact with.

When wrapping inner (nested) classes, use `$` instead of `.` to separate them. For example, `JavaClassWrapper.wrap("android.view.WindowManager$LayoutParams")` wraps the **WindowManager.LayoutParams** class.

**Note:** To invoke a constructor, call a method with the same name as the class. For example:

    var Intent = JavaClassWrapper.wrap("android.content.Intent")
    var intent = Intent.Intent()

**Note:** This method only works on Android. On every other platform, this method does nothing and returns an empty `JavaClass<class_JavaClass>`.