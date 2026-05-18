github_url
hide

# EditorExportPlatformAndroid

**Inherits:** `EditorExportPlatform<class_EditorExportPlatform>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Exporter for Android.

classref-introduction-group

## Tutorials

- `Exporting for Android <../tutorials/export/exporting_for_android>`
- `Gradle builds for Android <../tutorials/export/android_gradle_build>`
- `Android plugins documentation index <../tutorials/platform/index>`

classref-reftable-group

## Properties

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **architectures/arm64-v8a** `🔗<class_EditorExportPlatformAndroid_property_architectures/arm64-v8a>`

If `true`, `arm64` binaries are included into exported project.

classref-item-separator

classref-property

`bool<class_bool>` **architectures/armeabi-v7a** `🔗<class_EditorExportPlatformAndroid_property_architectures/armeabi-v7a>`

If `true`, `arm32` binaries are included into exported project.

classref-item-separator

classref-property

`bool<class_bool>` **architectures/x86** `🔗<class_EditorExportPlatformAndroid_property_architectures/x86>`

If `true`, `x86_32` binaries are included into exported project.

classref-item-separator

classref-property

`bool<class_bool>` **architectures/x86_64** `🔗<class_EditorExportPlatformAndroid_property_architectures/x86_64>`

If `true`, `x86_64` binaries are included into exported project.

classref-item-separator

classref-property

`String<class_String>` **command_line/extra_args** `🔗<class_EditorExportPlatformAndroid_property_command_line/extra_args>`

A list of additional command line arguments, separated by space, which the exported project will receive when started.

classref-item-separator

classref-property

`String<class_String>` **custom_template/debug** `🔗<class_EditorExportPlatformAndroid_property_custom_template/debug>`

Path to an APK file to use as a custom export template for debug exports. If left empty, default template is used.

**Note:** This is only used if `gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>` is disabled.

classref-item-separator

classref-property

`String<class_String>` **custom_template/release** `🔗<class_EditorExportPlatformAndroid_property_custom_template/release>`

Path to an APK file to use as a custom export template for release exports. If left empty, default template is used.

**Note:** This is only used if `gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>` is disabled.

classref-item-separator

classref-property

`bool<class_bool>` **gesture/swipe_to_dismiss** `🔗<class_EditorExportPlatformAndroid_property_gesture/swipe_to_dismiss>`

If `true`, [Swipe to dismiss](https://developer.android.com/design/ui/wear/guides/components/swipe-to-dismiss) will be enabled.

This functionality is intended for smartwatches and is generally ignored on standard Android devices. However, some devices may not ignore it. Therefore, it is recommended to keep this feature disabled for standard Android apps to avoid unexpected behavior.

**Note:** This is `false` by default. To enable this behavior, `gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>` is required.

classref-item-separator

classref-property

`String<class_String>` **gradle_build/android_source_template** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/android_source_template>`

Path to a ZIP file holding the source for the export template used in a Gradle build. If left empty, the default template is used.

classref-item-separator

classref-property

`bool<class_bool>` **gradle_build/compress_native_libraries** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/compress_native_libraries>`

If `true`, native libraries are compressed when performing a Gradle build.

**Note:** While enabling compression can reduce the size of the binary, it may result in slower application startup because the native libraries must be extracted before use, rather than being loaded directly.

If you're distributing your app via the Play Store, it's generally recommended to keep this option `false`, see [official documentation](https://developer.android.com/build/releases/past-releases/agp-3-6-0-release-notes#extractNativeLibs).

classref-item-separator

classref-property

`Dictionary<class_Dictionary>` **gradle_build/custom_theme_attributes** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/custom_theme_attributes>`

A dictionary of custom theme attributes to include in the exported Android project. Each entry defines a theme attribute name and its value, and will be added to the **GodotAppMainTheme**.

For example, the key `android:windowSwipeToDismiss` with the value `false` is resolved to `<item name="android:windowSwipeToDismiss">false</item>`.

**Note:** To add a custom attribute to the **GodotAppSplashTheme**, prefix the attribute name with `[splash]`.

**Note:** Reserved attributes configured via other export options or project settings cannot be overridden by `custom_theme_attributes` and are skipped during export.

classref-item-separator

classref-property

`int<class_int>` **gradle_build/export_format** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/export_format>`

Application export format (\*.apk or \*.aab).

classref-item-separator

classref-property

`String<class_String>` **gradle_build/gradle_build_directory** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/gradle_build_directory>`

Path to the Gradle build directory. If left empty, then `res://android` will be used.

classref-item-separator

classref-property

`String<class_String>` **gradle_build/min_sdk** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/min_sdk>`

Minimum Android API level required for the application to run (used during Gradle build). See [android:minSdkVersion](https://developer.android.com/guide/topics/manifest/uses-sdk-element#uses).

classref-item-separator

classref-property

`String<class_String>` **gradle_build/target_sdk** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/target_sdk>`

The Android API level on which the application is designed to run (used during Gradle build). See [android:targetSdkVersion](https://developer.android.com/guide/topics/manifest/uses-sdk-element#uses).

classref-item-separator

classref-property

`bool<class_bool>` **gradle_build/use_gradle_build** `🔗<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>`

If `true`, Gradle build is used instead of pre-built APK.

classref-item-separator

classref-property

`bool<class_bool>` **graphics/opengl_debug** `🔗<class_EditorExportPlatformAndroid_property_graphics/opengl_debug>`

If `true`, OpenGL ES debug context will be created (additional runtime checking, validation, and logging).

classref-item-separator

classref-property

`String<class_String>` **keystore/debug** `🔗<class_EditorExportPlatformAndroid_property_keystore/debug>`

Path of the debug keystore file.

Can be overridden with the environment variable `GODOT_ANDROID_KEYSTORE_DEBUG_PATH`.

Fallbacks to `EditorSettings.export/android/debug_keystore` if empty.

classref-item-separator

classref-property

`String<class_String>` **keystore/debug_password** `🔗<class_EditorExportPlatformAndroid_property_keystore/debug_password>`

Password for the debug keystore file.

Can be overridden with the environment variable `GODOT_ANDROID_KEYSTORE_DEBUG_PASSWORD`.

Fallbacks to `EditorSettings.export/android/debug_keystore_pass` if both it and `keystore/debug<class_EditorExportPlatformAndroid_property_keystore/debug>` are empty.

classref-item-separator

classref-property

`String<class_String>` **keystore/debug_user** `🔗<class_EditorExportPlatformAndroid_property_keystore/debug_user>`

User name for the debug keystore file.

Can be overridden with the environment variable `GODOT_ANDROID_KEYSTORE_DEBUG_USER`.

Fallbacks to `EditorSettings.export/android/debug_keystore_user` if both it and `keystore/debug<class_EditorExportPlatformAndroid_property_keystore/debug>` are empty.

classref-item-separator

classref-property

`String<class_String>` **keystore/release** `🔗<class_EditorExportPlatformAndroid_property_keystore/release>`

Path of the release keystore file.

Can be overridden with the environment variable `GODOT_ANDROID_KEYSTORE_RELEASE_PATH`.

classref-item-separator

classref-property

`String<class_String>` **keystore/release_password** `🔗<class_EditorExportPlatformAndroid_property_keystore/release_password>`

Password for the release keystore file.

Can be overridden with the environment variable `GODOT_ANDROID_KEYSTORE_RELEASE_PASSWORD`.

classref-item-separator

classref-property

`String<class_String>` **keystore/release_user** `🔗<class_EditorExportPlatformAndroid_property_keystore/release_user>`

User name for the release keystore file.

Can be overridden with the environment variable `GODOT_ANDROID_KEYSTORE_RELEASE_USER`.

classref-item-separator

classref-property

`String<class_String>` **launcher_icons/adaptive_background_432x432** `🔗<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_background_432x432>`

Background layer of the application adaptive icon file. See [Design adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons).

classref-item-separator

classref-property

`String<class_String>` **launcher_icons/adaptive_foreground_432x432** `🔗<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_foreground_432x432>`

Foreground layer of the application adaptive icon file. See [Design adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons).

classref-item-separator

classref-property

`String<class_String>` **launcher_icons/adaptive_monochrome_432x432** `🔗<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_monochrome_432x432>`

Monochrome layer of the application adaptive icon file. See [Design adaptive icons](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons).

classref-item-separator

classref-property

`String<class_String>` **launcher_icons/main_192x192** `🔗<class_EditorExportPlatformAndroid_property_launcher_icons/main_192x192>`

Application icon file. If left empty, it will fallback to `ProjectSettings.application/config/icon<class_ProjectSettings_property_application/config/icon>`.

classref-item-separator

classref-property

`int<class_int>` **package/app_category** `🔗<class_EditorExportPlatformAndroid_property_package/app_category>`

Application category for the Google Play Store. Only define this if your application fits one of the categories well. See [android:appCategory](https://developer.android.com/guide/topics/manifest/application-element#appCategory).

classref-item-separator

classref-property

`bool<class_bool>` **package/exclude_from_recents** `🔗<class_EditorExportPlatformAndroid_property_package/exclude_from_recents>`

If `true`, task initiated by main activity will be excluded from the list of recently used applications. See [android:excludeFromRecents](https://developer.android.com/guide/topics/manifest/activity-element#exclude).

classref-item-separator

classref-property

`String<class_String>` **package/name** `🔗<class_EditorExportPlatformAndroid_property_package/name>`

Name of the application.

classref-item-separator

classref-property

`bool<class_bool>` **package/retain_data_on_uninstall** `🔗<class_EditorExportPlatformAndroid_property_package/retain_data_on_uninstall>`

If `true`, when the user uninstalls an app, a prompt to keep the app's data will be shown. See [android:hasFragileUserData](https://developer.android.com/guide/topics/manifest/application-element#fragileuserdata).

classref-item-separator

classref-property

`bool<class_bool>` **package/show_as_launcher_app** `🔗<class_EditorExportPlatformAndroid_property_package/show_as_launcher_app>`

If `true`, the user will be able to set this app as the system launcher in Android preferences.

classref-item-separator

classref-property

`bool<class_bool>` **package/show_in_android_tv** `🔗<class_EditorExportPlatformAndroid_property_package/show_in_android_tv>`

If `true`, this app will show in Android TV launcher UI.

classref-item-separator

classref-property

`bool<class_bool>` **package/show_in_app_library** `🔗<class_EditorExportPlatformAndroid_property_package/show_in_app_library>`

If `true`, this app will show in the device's app library.

**Note:** This is `true` by default.

classref-item-separator

classref-property

`bool<class_bool>` **package/signed** `🔗<class_EditorExportPlatformAndroid_property_package/signed>`

If `true`, package signing is enabled.

classref-item-separator

classref-property

`String<class_String>` **package/unique_name** `🔗<class_EditorExportPlatformAndroid_property_package/unique_name>`

Unique application identifier in a reverse-DNS format. The reverse DNS format should preferably match a domain name you control, but this is not strictly required. For instance, if you own `example.com`, your package unique name should preferably be of the form `com.example.mygame`. This identifier can only contain lowercase alphanumeric characters (`a-z`, and `0-9`), underscores (`_`), and periods (`.`). Each component of the reverse DNS format must start with a letter: for instance, `com.example.8game` is not valid.

If `$genname` is present in the value, it will be replaced by the project name converted to lowercase. If there are invalid characters in the project name, they will be stripped. If all characters in the project name are stripped, `$genname` is replaced by `noname`.

**Note:** Changing the package name will cause the package to be considered as a new package, with its own installation and data paths. The new package won't be usable to update existing installations.

**Note:** When publishing to Google Play, the package name must be *globally* unique. This means no other apps published on Google Play must be using the same package name as yours. Otherwise, you'll be prevented from publishing your app on Google Play.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_checkin_properties** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_checkin_properties>`

Allows read/write access to the "properties" table in the checkin database. See [ACCESS_CHECKIN_PROPERTIES](https://developer.android.com/reference/android/Manifest.permission#ACCESS_CHECKIN_PROPERTIES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_coarse_location** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_coarse_location>`

Allows access to the approximate location information. See [ACCESS_COARSE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_fine_location** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_fine_location>`

Allows access to the precise location information. See [ACCESS_FINE_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_location_extra_commands** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_location_extra_commands>`

Allows access to the extra location provider commands. See [ACCESS_LOCATION_EXTRA_COMMANDS](https://developer.android.com/reference/android/Manifest.permission#ACCESS_LOCATION_EXTRA_COMMANDS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_media_location** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_media_location>`

Allows an application to access any geographic locations persisted in the user's shared collection. See [ACCESS_MEDIA_LOCATION](https://developer.android.com/reference/android/Manifest.permission#ACCESS_MEDIA_LOCATION).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_mock_location** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_mock_location>`

Allows an application to create mock location providers for testing.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_network_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_network_state>`

Allows access to the information about networks. See [ACCESS_NETWORK_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_surface_flinger** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_surface_flinger>`

Allows an application to use SurfaceFlinger's low level features.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/access_wifi_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/access_wifi_state>`

Allows access to the information about Wi-Fi networks. See [ACCESS_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/account_manager** `🔗<class_EditorExportPlatformAndroid_property_permissions/account_manager>`

Allows applications to call into AccountAuthenticators. See [ACCOUNT_MANAGER](https://developer.android.com/reference/android/Manifest.permission#ACCOUNT_MANAGER).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/add_voicemail** `🔗<class_EditorExportPlatformAndroid_property_permissions/add_voicemail>`

Allows an application to add voicemails into the system. See [ADD_VOICEMAIL](https://developer.android.com/reference/android/Manifest.permission#ADD_VOICEMAIL).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/authenticate_accounts** `🔗<class_EditorExportPlatformAndroid_property_permissions/authenticate_accounts>`

Allows an application to act as an AccountAuthenticator for the AccountManager.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/battery_stats** `🔗<class_EditorExportPlatformAndroid_property_permissions/battery_stats>`

Allows an application to collect battery statistics. See [BATTERY_STATS](https://developer.android.com/reference/android/Manifest.permission#BATTERY_STATS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_accessibility_service** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_accessibility_service>`

Must be required by an AccessibilityService, to ensure that only the system can bind to it. See [BIND_ACCESSIBILITY_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_ACCESSIBILITY_SERVICE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_appwidget** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_appwidget>`

Allows an application to tell the AppWidget service which application can access AppWidget's data. See [BIND_APPWIDGET](https://developer.android.com/reference/android/Manifest.permission#BIND_APPWIDGET).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_device_admin** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_device_admin>`

Must be required by device administration receiver, to ensure that only the system can interact with it. See [BIND_DEVICE_ADMIN](https://developer.android.com/reference/android/Manifest.permission#BIND_DEVICE_ADMIN).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_input_method** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_input_method>`

Must be required by an InputMethodService, to ensure that only the system can bind to it. See [BIND_INPUT_METHOD](https://developer.android.com/reference/android/Manifest.permission#BIND_INPUT_METHOD).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_nfc_service** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_nfc_service>`

Must be required by a HostApduService or OffHostApduService to ensure that only the system can bind to it. See [BIND_NFC_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_NFC_SERVICE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_notification_listener_service** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_notification_listener_service>`

Must be required by a NotificationListenerService, to ensure that only the system can bind to it. See [BIND_NOTIFICATION_LISTENER_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_NOTIFICATION_LISTENER_SERVICE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_print_service** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_print_service>`

Must be required by a PrintService, to ensure that only the system can bind to it. See [BIND_PRINT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_PRINT_SERVICE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_remoteviews** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_remoteviews>`

Must be required by a RemoteViewsService, to ensure that only the system can bind to it. See [BIND_REMOTEVIEWS](https://developer.android.com/reference/android/Manifest.permission#BIND_REMOTEVIEWS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_text_service** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_text_service>`

Must be required by a TextService (e.g. SpellCheckerService) to ensure that only the system can bind to it. See [BIND_TEXT_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_TEXT_SERVICE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_vpn_service** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_vpn_service>`

Must be required by a VpnService, to ensure that only the system can bind to it. See [BIND_VPN_SERVICE](https://developer.android.com/reference/android/Manifest.permission#BIND_VPN_SERVICE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bind_wallpaper** `🔗<class_EditorExportPlatformAndroid_property_permissions/bind_wallpaper>`

Must be required by a WallpaperService, to ensure that only the system can bind to it. See [BIND_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#BIND_WALLPAPER).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bluetooth** `🔗<class_EditorExportPlatformAndroid_property_permissions/bluetooth>`

Allows applications to connect to paired bluetooth devices. See [BLUETOOTH](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bluetooth_admin** `🔗<class_EditorExportPlatformAndroid_property_permissions/bluetooth_admin>`

Allows applications to discover and pair bluetooth devices. See [BLUETOOTH_ADMIN](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_ADMIN).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/bluetooth_privileged** `🔗<class_EditorExportPlatformAndroid_property_permissions/bluetooth_privileged>`

Allows applications to pair bluetooth devices without user interaction, and to allow or disallow phonebook access or message access. See [BLUETOOTH_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#BLUETOOTH_PRIVILEGED).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/brick** `🔗<class_EditorExportPlatformAndroid_property_permissions/brick>`

Required to be able to disable the device (very dangerous!).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/broadcast_package_removed** `🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_package_removed>`

Allows an application to broadcast a notification that an application package has been removed. See [BROADCAST_PACKAGE_REMOVED](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_PACKAGE_REMOVED).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/broadcast_sms** `🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_sms>`

Allows an application to broadcast an SMS receipt notification. See [BROADCAST_SMS](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_SMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/broadcast_sticky** `🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_sticky>`

Allows an application to broadcast sticky intents. See [BROADCAST_STICKY](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_STICKY).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/broadcast_wap_push** `🔗<class_EditorExportPlatformAndroid_property_permissions/broadcast_wap_push>`

Allows an application to broadcast a WAP PUSH receipt notification. See [BROADCAST_WAP_PUSH](https://developer.android.com/reference/android/Manifest.permission#BROADCAST_WAP_PUSH).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/call_phone** `🔗<class_EditorExportPlatformAndroid_property_permissions/call_phone>`

Allows an application to initiate a phone call without going through the Dialer user interface. See [CALL_PHONE](https://developer.android.com/reference/android/Manifest.permission#CALL_PHONE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/call_privileged** `🔗<class_EditorExportPlatformAndroid_property_permissions/call_privileged>`

Allows an application to call any phone number, including emergency numbers, without going through the Dialer user interface. See [CALL_PRIVILEGED](https://developer.android.com/reference/android/Manifest.permission#CALL_PRIVILEGED).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/camera** `🔗<class_EditorExportPlatformAndroid_property_permissions/camera>`

Required to be able to access the camera device. See [CAMERA](https://developer.android.com/reference/android/Manifest.permission#CAMERA).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/capture_audio_output** `🔗<class_EditorExportPlatformAndroid_property_permissions/capture_audio_output>`

Allows an application to capture audio output. See [CAPTURE_AUDIO_OUTPUT](https://developer.android.com/reference/android/Manifest.permission#CAPTURE_AUDIO_OUTPUT).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/capture_secure_video_output** `🔗<class_EditorExportPlatformAndroid_property_permissions/capture_secure_video_output>`

Allows an application to capture secure video output.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/capture_video_output** `🔗<class_EditorExportPlatformAndroid_property_permissions/capture_video_output>`

Allows an application to capture video output.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/change_component_enabled_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/change_component_enabled_state>`

Allows an application to change whether an application component (other than its own) is enabled or not. See [CHANGE_COMPONENT_ENABLED_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_COMPONENT_ENABLED_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/change_configuration** `🔗<class_EditorExportPlatformAndroid_property_permissions/change_configuration>`

Allows an application to modify the current configuration, such as locale. See [CHANGE_CONFIGURATION](https://developer.android.com/reference/android/Manifest.permission#CHANGE_CONFIGURATION).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/change_network_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/change_network_state>`

Allows applications to change network connectivity state. See [CHANGE_NETWORK_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_NETWORK_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/change_wifi_multicast_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/change_wifi_multicast_state>`

Allows applications to enter Wi-Fi Multicast mode. See [CHANGE_WIFI_MULTICAST_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_MULTICAST_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/change_wifi_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/change_wifi_state>`

Allows applications to change Wi-Fi connectivity state. See [CHANGE_WIFI_STATE](https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/clear_app_cache** `🔗<class_EditorExportPlatformAndroid_property_permissions/clear_app_cache>`

Allows an application to clear the caches of all installed applications on the device. See [CLEAR_APP_CACHE](https://developer.android.com/reference/android/Manifest.permission#CLEAR_APP_CACHE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/clear_app_user_data** `🔗<class_EditorExportPlatformAndroid_property_permissions/clear_app_user_data>`

Allows an application to clear user data.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/control_location_updates** `🔗<class_EditorExportPlatformAndroid_property_permissions/control_location_updates>`

Allows enabling/disabling location update notifications from the radio. See [CONTROL_LOCATION_UPDATES](https://developer.android.com/reference/android/Manifest.permission#CONTROL_LOCATION_UPDATES).

classref-item-separator

classref-property

`PackedStringArray<class_PackedStringArray>` **permissions/custom_permissions** `🔗<class_EditorExportPlatformAndroid_property_permissions/custom_permissions>`

Array of custom permission strings.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See `PackedStringArray<class_PackedStringArray>` for more details.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/delete_cache_files** `🔗<class_EditorExportPlatformAndroid_property_permissions/delete_cache_files>`

**Deprecated:** This property may be changed or removed in future versions.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/delete_packages** `🔗<class_EditorExportPlatformAndroid_property_permissions/delete_packages>`

Allows an application to delete packages. See [DELETE_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#DELETE_PACKAGES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/device_power** `🔗<class_EditorExportPlatformAndroid_property_permissions/device_power>`

Allows low-level access to power management.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/diagnostic** `🔗<class_EditorExportPlatformAndroid_property_permissions/diagnostic>`

Allows applications to RW to diagnostic resources. See [DIAGNOSTIC](https://developer.android.com/reference/android/Manifest.permission#DIAGNOSTIC).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/disable_keyguard** `🔗<class_EditorExportPlatformAndroid_property_permissions/disable_keyguard>`

Allows applications to disable the keyguard if it is not secure. See [DISABLE_KEYGUARD](https://developer.android.com/reference/android/Manifest.permission#DISABLE_KEYGUARD).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/dump** `🔗<class_EditorExportPlatformAndroid_property_permissions/dump>`

Allows an application to retrieve state dump information from system services. See [DUMP](https://developer.android.com/reference/android/Manifest.permission#DUMP).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/expand_status_bar** `🔗<class_EditorExportPlatformAndroid_property_permissions/expand_status_bar>`

Allows an application to expand or collapse the status bar. See [EXPAND_STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#EXPAND_STATUS_BAR).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/factory_test** `🔗<class_EditorExportPlatformAndroid_property_permissions/factory_test>`

Run as a manufacturer test application, running as the root user. See [FACTORY_TEST](https://developer.android.com/reference/android/Manifest.permission#FACTORY_TEST).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/flashlight** `🔗<class_EditorExportPlatformAndroid_property_permissions/flashlight>`

Allows access to the flashlight.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/force_back** `🔗<class_EditorExportPlatformAndroid_property_permissions/force_back>`

Allows an application to force a BACK operation on whatever is the top activity.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/get_accounts** `🔗<class_EditorExportPlatformAndroid_property_permissions/get_accounts>`

Allows access to the list of accounts in the Accounts Service. See [GET_ACCOUNTS](https://developer.android.com/reference/android/Manifest.permission#GET_ACCOUNTS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/get_package_size** `🔗<class_EditorExportPlatformAndroid_property_permissions/get_package_size>`

Allows an application to find out the space used by any package. See [GET_PACKAGE_SIZE](https://developer.android.com/reference/android/Manifest.permission#GET_PACKAGE_SIZE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/get_tasks** `🔗<class_EditorExportPlatformAndroid_property_permissions/get_tasks>`

**Deprecated:** Deprecated in API level 21.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/get_top_activity_info** `🔗<class_EditorExportPlatformAndroid_property_permissions/get_top_activity_info>`

Allows an application to retrieve private information about the current top activity.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/global_search** `🔗<class_EditorExportPlatformAndroid_property_permissions/global_search>`

Used on content providers to allow the global search system to access their data. See [GLOBAL_SEARCH](https://developer.android.com/reference/android/Manifest.permission#GLOBAL_SEARCH).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/hardware_test** `🔗<class_EditorExportPlatformAndroid_property_permissions/hardware_test>`

Allows access to hardware peripherals.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/inject_events** `🔗<class_EditorExportPlatformAndroid_property_permissions/inject_events>`

Allows an application to inject user events (keys, touch, trackball) into the event stream and deliver them to ANY window.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/install_location_provider** `🔗<class_EditorExportPlatformAndroid_property_permissions/install_location_provider>`

Allows an application to install a location provider into the Location Manager. See [INSTALL_LOCATION_PROVIDER](https://developer.android.com/reference/android/Manifest.permission#INSTALL_LOCATION_PROVIDER).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/install_packages** `🔗<class_EditorExportPlatformAndroid_property_permissions/install_packages>`

Allows an application to install packages. See [INSTALL_PACKAGES](https://developer.android.com/reference/android/Manifest.permission#INSTALL_PACKAGES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/install_shortcut** `🔗<class_EditorExportPlatformAndroid_property_permissions/install_shortcut>`

Allows an application to install a shortcut in Launcher. See [INSTALL_SHORTCUT](https://developer.android.com/reference/android/Manifest.permission#INSTALL_SHORTCUT).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/internal_system_window** `🔗<class_EditorExportPlatformAndroid_property_permissions/internal_system_window>`

Allows an application to open windows that are for use by parts of the system user interface.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/internet** `🔗<class_EditorExportPlatformAndroid_property_permissions/internet>`

Allows applications to open network sockets. See [INTERNET](https://developer.android.com/reference/android/Manifest.permission#INTERNET).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/kill_background_processes** `🔗<class_EditorExportPlatformAndroid_property_permissions/kill_background_processes>`

Allows an application to call ActivityManager.killBackgroundProcesses(String). See [KILL_BACKGROUND_PROCESSES](https://developer.android.com/reference/android/Manifest.permission#KILL_BACKGROUND_PROCESSES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/location_hardware** `🔗<class_EditorExportPlatformAndroid_property_permissions/location_hardware>`

Allows an application to use location features in hardware, such as the geofencing api. See [LOCATION_HARDWARE](https://developer.android.com/reference/android/Manifest.permission#LOCATION_HARDWARE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/manage_accounts** `🔗<class_EditorExportPlatformAndroid_property_permissions/manage_accounts>`

Allows an application to manage the list of accounts in the AccountManager.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/manage_app_tokens** `🔗<class_EditorExportPlatformAndroid_property_permissions/manage_app_tokens>`

Allows an application to manage (create, destroy, Z-order) application tokens in the window manager.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/manage_documents** `🔗<class_EditorExportPlatformAndroid_property_permissions/manage_documents>`

Allows an application to manage access to documents, usually as part of a document picker. See [MANAGE_DOCUMENTS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_DOCUMENTS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/manage_external_storage** `🔗<class_EditorExportPlatformAndroid_property_permissions/manage_external_storage>`

Allows an application a broad access to external storage in scoped storage. See [MANAGE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#MANAGE_EXTERNAL_STORAGE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/manage_media** `🔗<class_EditorExportPlatformAndroid_property_permissions/manage_media>`

Allows an application to modify and delete media files on this device or any connected storage device without user confirmation. Applications must already be granted the `READ_EXTERNAL_STORAGE` or `MANAGE_EXTERNAL_STORAGE` permissions for this permission to take effect. See [MANAGE_MEDIA](https://developer.android.com/reference/android/Manifest.permission#MANAGE_MEDIA).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/master_clear** `🔗<class_EditorExportPlatformAndroid_property_permissions/master_clear>`

See [MASTER_CLEAR](https://developer.android.com/reference/android/Manifest.permission#MASTER_CLEAR).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/media_content_control** `🔗<class_EditorExportPlatformAndroid_property_permissions/media_content_control>`

Allows an application to know what content is playing and control its playback. See [MEDIA_CONTENT_CONTROL](https://developer.android.com/reference/android/Manifest.permission#MEDIA_CONTENT_CONTROL).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/modify_audio_settings** `🔗<class_EditorExportPlatformAndroid_property_permissions/modify_audio_settings>`

Allows an application to modify global audio settings. See [MODIFY_AUDIO_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#MODIFY_AUDIO_SETTINGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/modify_phone_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/modify_phone_state>`

Allows modification of the telephony state - power on, mmi, etc. Does not include placing calls. See [MODIFY_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#MODIFY_PHONE_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/mount_format_filesystems** `🔗<class_EditorExportPlatformAndroid_property_permissions/mount_format_filesystems>`

Allows formatting file systems for removable storage. See [MOUNT_FORMAT_FILESYSTEMS](https://developer.android.com/reference/android/Manifest.permission#MOUNT_FORMAT_FILESYSTEMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/mount_unmount_filesystems** `🔗<class_EditorExportPlatformAndroid_property_permissions/mount_unmount_filesystems>`

Allows mounting and unmounting file systems for removable storage. See [MOUNT_UNMOUNT_FILESYSTEMS](https://developer.android.com/reference/android/Manifest.permission#MOUNT_UNMOUNT_FILESYSTEMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/nfc** `🔗<class_EditorExportPlatformAndroid_property_permissions/nfc>`

Allows applications to perform I/O operations over NFC. See [NFC](https://developer.android.com/reference/android/Manifest.permission#NFC).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/persistent_activity** `🔗<class_EditorExportPlatformAndroid_property_permissions/persistent_activity>`

**Deprecated:** Deprecated in API level 15.

Allows an application to make its activities persistent.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/post_notifications** `🔗<class_EditorExportPlatformAndroid_property_permissions/post_notifications>`

Allows an application to post notifications. Added in API level 33. See [Notification runtime permission](https://developer.android.com/develop/ui/views/notifications/notification-permission).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/process_outgoing_calls** `🔗<class_EditorExportPlatformAndroid_property_permissions/process_outgoing_calls>`

**Deprecated:** Deprecated in API level 29.

Allows an application to see the number being dialed during an outgoing call with the option to redirect the call to a different number or abort the call altogether. See [PROCESS_OUTGOING_CALLS](https://developer.android.com/reference/android/Manifest.permission#PROCESS_OUTGOING_CALLS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_calendar** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_calendar>`

Allows an application to read the user's calendar data. See [READ_CALENDAR](https://developer.android.com/reference/android/Manifest.permission#READ_CALENDAR).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_call_log** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_call_log>`

Allows an application to read the user's call log. See [READ_CALL_LOG](https://developer.android.com/reference/android/Manifest.permission#READ_CALL_LOG).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_contacts** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_contacts>`

Allows an application to read the user's contacts data. See [READ_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_external_storage** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_external_storage>`

**Deprecated:** Deprecated in API level 33.

Allows an application to read from external storage. See [READ_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#READ_EXTERNAL_STORAGE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_frame_buffer** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_frame_buffer>`

Allows an application to take screen shots and more generally get access to the frame buffer data.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_history_bookmarks** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_history_bookmarks>`

Allows an application to read (but not write) the user's browsing history and bookmarks.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_input_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_input_state>`

**Deprecated:** Deprecated in API level 16.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_logs** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_logs>`

Allows an application to read the low-level system log files. See [READ_LOGS](https://developer.android.com/reference/android/Manifest.permission#READ_LOGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_media_audio** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_audio>`

Allows an application to read audio files from external storage. See [READ_MEDIA_AUDIO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_AUDIO).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_media_images** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_images>`

Allows an application to read image files from external storage. See [READ_MEDIA_IMAGES](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_media_video** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_video>`

Allows an application to read video files from external storage. See [READ_MEDIA_VIDEO](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_media_visual_user_selected** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_media_visual_user_selected>`

Allows an application to read image or video files from external storage that a user has selected via the permission prompt photo picker. See [READ_MEDIA_VISUAL_USER_SELECTED](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VISUAL_USER_SELECTED).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_phone_state** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_phone_state>`

Allows read only access to phone state. See [READ_PHONE_STATE](https://developer.android.com/reference/android/Manifest.permission#READ_PHONE_STATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_profile** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_profile>`

Allows an application to read the user's personal profile data.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_sms** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_sms>`

Allows an application to read SMS messages. See [READ_SMS](https://developer.android.com/reference/android/Manifest.permission#READ_SMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_social_stream** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_social_stream>`

Allows an application to read from the user's social stream.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_sync_settings** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_sync_settings>`

Allows applications to read the sync settings. See [READ_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_SETTINGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_sync_stats** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_sync_stats>`

Allows applications to read the sync stats. See [READ_SYNC_STATS](https://developer.android.com/reference/android/Manifest.permission#READ_SYNC_STATS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/read_user_dictionary** `🔗<class_EditorExportPlatformAndroid_property_permissions/read_user_dictionary>`

Allows an application to read the user dictionary.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/reboot** `🔗<class_EditorExportPlatformAndroid_property_permissions/reboot>`

Required to be able to reboot the device. See [REBOOT](https://developer.android.com/reference/android/Manifest.permission#REBOOT).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/receive_boot_completed** `🔗<class_EditorExportPlatformAndroid_property_permissions/receive_boot_completed>`

Allows an application to receive the Intent.ACTION_BOOT_COMPLETED that is broadcast after the system finishes booting. See [RECEIVE_BOOT_COMPLETED](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_BOOT_COMPLETED).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/receive_mms** `🔗<class_EditorExportPlatformAndroid_property_permissions/receive_mms>`

Allows an application to monitor incoming MMS messages. See [RECEIVE_MMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_MMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/receive_sms** `🔗<class_EditorExportPlatformAndroid_property_permissions/receive_sms>`

Allows an application to receive SMS messages. See [RECEIVE_SMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_SMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/receive_wap_push** `🔗<class_EditorExportPlatformAndroid_property_permissions/receive_wap_push>`

Allows an application to receive WAP push messages. See [RECEIVE_WAP_PUSH](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_WAP_PUSH).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/record_audio** `🔗<class_EditorExportPlatformAndroid_property_permissions/record_audio>`

Allows an application to record audio. See [RECORD_AUDIO](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/reorder_tasks** `🔗<class_EditorExportPlatformAndroid_property_permissions/reorder_tasks>`

Allows an application to change the Z-order of tasks. See [REORDER_TASKS](https://developer.android.com/reference/android/Manifest.permission#REORDER_TASKS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/restart_packages** `🔗<class_EditorExportPlatformAndroid_property_permissions/restart_packages>`

**Deprecated:** Deprecated in API level 15.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/send_respond_via_message** `🔗<class_EditorExportPlatformAndroid_property_permissions/send_respond_via_message>`

Allows an application (Phone) to send a request to other applications to handle the respond-via-message action during incoming calls. See [SEND_RESPOND_VIA_MESSAGE](https://developer.android.com/reference/android/Manifest.permission#SEND_RESPOND_VIA_MESSAGE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/send_sms** `🔗<class_EditorExportPlatformAndroid_property_permissions/send_sms>`

Allows an application to send SMS messages. See [SEND_SMS](https://developer.android.com/reference/android/Manifest.permission#SEND_SMS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_activity_watcher** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_activity_watcher>`

Allows an application to watch and control how activities are started globally in the system.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_alarm** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_alarm>`

Allows an application to broadcast an Intent to set an alarm for the user. See [SET_ALARM](https://developer.android.com/reference/android/Manifest.permission#SET_ALARM).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_always_finish** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_always_finish>`

Allows an application to control whether activities are immediately finished when put in the background. See [SET_ALWAYS_FINISH](https://developer.android.com/reference/android/Manifest.permission#SET_ALWAYS_FINISH).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_animation_scale** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_animation_scale>`

Allows to modify the global animation scaling factor. See [SET_ANIMATION_SCALE](https://developer.android.com/reference/android/Manifest.permission#SET_ANIMATION_SCALE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_debug_app** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_debug_app>`

Configure an application for debugging. See [SET_DEBUG_APP](https://developer.android.com/reference/android/Manifest.permission#SET_DEBUG_APP).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_orientation** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_orientation>`

Allows low-level access to setting the orientation (actually rotation) of the screen.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_pointer_speed** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_pointer_speed>`

Allows low-level access to setting the pointer speed.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_preferred_applications** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_preferred_applications>`

**Deprecated:** Deprecated in API level 15.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_process_limit** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_process_limit>`

Allows an application to set the maximum number of (not needed) application processes that can be running. See [SET_PROCESS_LIMIT](https://developer.android.com/reference/android/Manifest.permission#SET_PROCESS_LIMIT).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_time** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_time>`

Allows applications to set the system time directly. See [SET_TIME](https://developer.android.com/reference/android/Manifest.permission#SET_TIME).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_time_zone** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_time_zone>`

Allows applications to set the system time zone directly. See [SET_TIME_ZONE](https://developer.android.com/reference/android/Manifest.permission#SET_TIME_ZONE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_wallpaper** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_wallpaper>`

Allows applications to set the wallpaper. See [SET_WALLPAPER](https://developer.android.com/reference/android/Manifest.permission#SET_WALLPAPER).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/set_wallpaper_hints** `🔗<class_EditorExportPlatformAndroid_property_permissions/set_wallpaper_hints>`

Allows applications to set the wallpaper hints. See [SET_WALLPAPER_HINTS](https://developer.android.com/reference/android/Manifest.permission#SET_WALLPAPER_HINTS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/signal_persistent_processes** `🔗<class_EditorExportPlatformAndroid_property_permissions/signal_persistent_processes>`

Allow an application to request that a signal be sent to all persistent processes. See [SIGNAL_PERSISTENT_PROCESSES](https://developer.android.com/reference/android/Manifest.permission#SIGNAL_PERSISTENT_PROCESSES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/status_bar** `🔗<class_EditorExportPlatformAndroid_property_permissions/status_bar>`

Allows an application to open, close, or disable the status bar and its icons. See [STATUS_BAR](https://developer.android.com/reference/android/Manifest.permission#STATUS_BAR).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/subscribed_feeds_read** `🔗<class_EditorExportPlatformAndroid_property_permissions/subscribed_feeds_read>`

Allows an application to allow access the subscribed feeds ContentProvider.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/subscribed_feeds_write** `🔗<class_EditorExportPlatformAndroid_property_permissions/subscribed_feeds_write>`

**Deprecated:** This property may be changed or removed in future versions.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/system_alert_window** `🔗<class_EditorExportPlatformAndroid_property_permissions/system_alert_window>`

Allows an app to create windows using the type WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY, shown on top of all other apps. See [SYSTEM_ALERT_WINDOW](https://developer.android.com/reference/android/Manifest.permission#SYSTEM_ALERT_WINDOW).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/transmit_ir** `🔗<class_EditorExportPlatformAndroid_property_permissions/transmit_ir>`

Allows using the device's IR transmitter, if available. See [TRANSMIT_IR](https://developer.android.com/reference/android/Manifest.permission#TRANSMIT_IR).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/uninstall_shortcut** `🔗<class_EditorExportPlatformAndroid_property_permissions/uninstall_shortcut>`

**Deprecated:** This property may be changed or removed in future versions.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/update_device_stats** `🔗<class_EditorExportPlatformAndroid_property_permissions/update_device_stats>`

Allows an application to update device statistics. See [UPDATE_DEVICE_STATS](https://developer.android.com/reference/android/Manifest.permission#UPDATE_DEVICE_STATS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/use_credentials** `🔗<class_EditorExportPlatformAndroid_property_permissions/use_credentials>`

Allows an application to request authtokens from the AccountManager.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/use_sip** `🔗<class_EditorExportPlatformAndroid_property_permissions/use_sip>`

Allows an application to use SIP service. See [USE_SIP](https://developer.android.com/reference/android/Manifest.permission#USE_SIP).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/vibrate** `🔗<class_EditorExportPlatformAndroid_property_permissions/vibrate>`

Allows access to the vibrator. See [VIBRATE](https://developer.android.com/reference/android/Manifest.permission#VIBRATE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/wake_lock** `🔗<class_EditorExportPlatformAndroid_property_permissions/wake_lock>`

Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. See [WAKE_LOCK](https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_apn_settings** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_apn_settings>`

Allows applications to write the apn settings and read sensitive fields of an existing apn settings like user and password. See [WRITE_APN_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_APN_SETTINGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_calendar** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_calendar>`

Allows an application to write the user's calendar data. See [WRITE_CALENDAR](https://developer.android.com/reference/android/Manifest.permission#WRITE_CALENDAR).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_call_log** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_call_log>`

Allows an application to write (but not read) the user's call log data. See [WRITE_CALL_LOG](https://developer.android.com/reference/android/Manifest.permission#WRITE_CALL_LOG).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_contacts** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_contacts>`

Allows an application to write the user's contacts data. See [WRITE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#WRITE_CONTACTS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_external_storage** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_external_storage>`

Allows an application to write to external storage. See [WRITE_EXTERNAL_STORAGE](https://developer.android.com/reference/android/Manifest.permission#WRITE_EXTERNAL_STORAGE).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_gservices** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_gservices>`

Allows an application to modify the Google service map. See [WRITE_GSERVICES](https://developer.android.com/reference/android/Manifest.permission#WRITE_GSERVICES).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_history_bookmarks** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_history_bookmarks>`

Allows an application to write (but not read) the user's browsing history and bookmarks.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_profile** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_profile>`

Allows an application to write (but not read) the user's personal profile data.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_secure_settings** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_secure_settings>`

Allows an application to read or write the secure system settings. See [WRITE_SECURE_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SECURE_SETTINGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_settings** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_settings>`

Allows an application to read or write the system settings. See [WRITE_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SETTINGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_sms** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_sms>`

Allows an application to write SMS messages.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_social_stream** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_social_stream>`

Allows an application to write (but not read) the user's social stream data.

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_sync_settings** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_sync_settings>`

Allows applications to write the sync settings. See [WRITE_SYNC_SETTINGS](https://developer.android.com/reference/android/Manifest.permission#WRITE_SYNC_SETTINGS).

classref-item-separator

classref-property

`bool<class_bool>` **permissions/write_user_dictionary** `🔗<class_EditorExportPlatformAndroid_property_permissions/write_user_dictionary>`

Allows an application to write to the user dictionary.

classref-item-separator

classref-property

`Color<class_Color>` **screen/background_color** `🔗<class_EditorExportPlatformAndroid_property_screen/background_color>`

The background color used for the root window. By default it's `Color.BLACK<class_Color_constant_BLACK>`.

classref-item-separator

classref-property

`bool<class_bool>` **screen/edge_to_edge** `🔗<class_EditorExportPlatformAndroid_property_screen/edge_to_edge>`

If `true`, this makes the navigation and status bars translucent and allows the application content to extend edge to edge.

**Note:** You should ensure that none of the application content is occluded by system elements by using the `DisplayServer.get_display_safe_area()<class_DisplayServer_method_get_display_safe_area>` and `DisplayServer.get_display_cutouts()<class_DisplayServer_method_get_display_cutouts>` methods.

classref-item-separator

classref-property

`bool<class_bool>` **screen/immersive_mode** `🔗<class_EditorExportPlatformAndroid_property_screen/immersive_mode>`

If `true`, hides the navigation and status bar. Set `DisplayServer.window_set_mode()<class_DisplayServer_method_window_set_mode>` to change this at runtime.

classref-item-separator

classref-property

`bool<class_bool>` **screen/support_large** `🔗<class_EditorExportPlatformAndroid_property_screen/support_large>`

Indicates whether the application supports larger screen form-factors.

classref-item-separator

classref-property

`bool<class_bool>` **screen/support_normal** `🔗<class_EditorExportPlatformAndroid_property_screen/support_normal>`

Indicates whether an application supports the "normal" screen form-factors.

classref-item-separator

classref-property

`bool<class_bool>` **screen/support_small** `🔗<class_EditorExportPlatformAndroid_property_screen/support_small>`

Indicates whether the application supports smaller screen form-factors.

classref-item-separator

classref-property

`bool<class_bool>` **screen/support_xlarge** `🔗<class_EditorExportPlatformAndroid_property_screen/support_xlarge>`

Indicates whether the application supports extra large screen form-factors.

classref-item-separator

classref-property

`bool<class_bool>` **shader_baker/enabled** `🔗<class_EditorExportPlatformAndroid_property_shader_baker/enabled>`

If `true`, shaders will be compiled and embedded in the application. This option is only supported when using the Forward+ or Mobile renderers.

**Note:** When exporting as a dedicated server, the shader baker is always disabled since no rendering is performed.

classref-item-separator

classref-property

`Color<class_Color>` **splash_screen/background_color** `🔗<class_EditorExportPlatformAndroid_property_splash_screen/background_color>`

The background color used for the system splash screen window.

If not set, it will fallback to `launcher_icons/adaptive_background_432x432<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_background_432x432>`.

**Note:** This is only applied if `gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>` is enabled.

classref-item-separator

classref-property

`String<class_String>` **splash_screen/branding_image** `🔗<class_EditorExportPlatformAndroid_property_splash_screen/branding_image>`

System splash screen branding image file. If left empty, no branding image will be used. See [splash-screen dimensions](https://developer.android.com/develop/ui/views/launch/splash-screen#dimensions).

**Note:** Can be used to set an image to be shown at the bottom of the splash screen.

classref-item-separator

classref-property

`bool<class_bool>` **splash_screen/disable_godot_boot_splash** `🔗<class_EditorExportPlatformAndroid_property_splash_screen/disable_godot_boot_splash>`

If `true`, Godot's boot splash will not be shown, and the system boot splash will remain visible for a longer time, until the mainloop starts.

classref-item-separator

classref-property

`String<class_String>` **splash_screen/icon** `🔗<class_EditorExportPlatformAndroid_property_splash_screen/icon>`

System splash screen icon file. If left empty, it will fall back to `launcher_icons/adaptive_foreground_432x432<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_foreground_432x432>`. See [splash-screen dimensions](https://developer.android.com/develop/ui/views/launch/splash-screen#dimensions).

**Note:** You can provide an [AnimatedVectorDrawable (AVD)](https://developer.android.com/reference/android/graphics/drawable/AnimatedVectorDrawable) XML. However, the XML file will only be used if `gradle_build/use_gradle_build<class_EditorExportPlatformAndroid_property_gradle_build/use_gradle_build>` is enabled. If not, it will fall back to `launcher_icons/adaptive_background_432x432<class_EditorExportPlatformAndroid_property_launcher_icons/adaptive_background_432x432>`.

classref-item-separator

classref-property

`bool<class_bool>` **user_data_backup/allow** `🔗<class_EditorExportPlatformAndroid_property_user_data_backup/allow>`

If `true`, allows the application to participate in the backup and restore infrastructure.

classref-item-separator

classref-property

`int<class_int>` **version/code** `🔗<class_EditorExportPlatformAndroid_property_version/code>`

Machine-readable application version. This must be incremented for every new release pushed to the Play Store.

classref-item-separator

classref-property

`String<class_String>` **version/name** `🔗<class_EditorExportPlatformAndroid_property_version/name>`

Application version visible to the user. Falls back to `ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>` if left empty.

classref-item-separator

classref-property

`int<class_int>` **xr_features/xr_mode** `🔗<class_EditorExportPlatformAndroid_property_xr_features/xr_mode>`

The extended reality (XR) mode for this application.