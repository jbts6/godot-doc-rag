github_url
hide

# TranslationDomain

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

A self-contained collection of `Translation<class_Translation>` resources.

classref-introduction-group

## Description

**TranslationDomain** is a self-contained collection of `Translation<class_Translation>` resources. Translations can be added to or removed from it.

If you're working with the main translation domain, it is more convenient to use the wrap methods on `TranslationServer<class_TranslationServer>`.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`bool<class_bool>` **enabled** = `true` `🔗<class_TranslationDomain_property_enabled>`

classref-property-setget

- `void (No return value.)` **set_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_enabled**()

If `true`, translation is enabled. Otherwise, `translate()<class_TranslationDomain_method_translate>` and `translate_plural()<class_TranslationDomain_method_translate_plural>` will return the input message unchanged regardless of the current locale.

classref-item-separator

classref-property

`bool<class_bool>` **pseudolocalization_accents_enabled** = `true` `🔗<class_TranslationDomain_property_pseudolocalization_accents_enabled>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_accents_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pseudolocalization_accents_enabled**()

Replace all characters with their accented variants during pseudolocalization.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`bool<class_bool>` **pseudolocalization_double_vowels_enabled** = `false` `🔗<class_TranslationDomain_property_pseudolocalization_double_vowels_enabled>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_double_vowels_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pseudolocalization_double_vowels_enabled**()

Double vowels in strings during pseudolocalization to simulate the lengthening of text due to localization.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`bool<class_bool>` **pseudolocalization_enabled** = `false` `🔗<class_TranslationDomain_property_pseudolocalization_enabled>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pseudolocalization_enabled**()

If `true`, enables pseudolocalization for the project. This can be used to spot untranslatable strings or layout issues that may occur once the project is localized to languages that have longer strings than the source language.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`float<class_float>` **pseudolocalization_expansion_ratio** = `0.0` `🔗<class_TranslationDomain_property_pseudolocalization_expansion_ratio>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_expansion_ratio**(value: `float<class_float>`)
- `float<class_float>` **get_pseudolocalization_expansion_ratio**()

The expansion ratio to use during pseudolocalization. A value of `0.3` is sufficient for most practical purposes, and will increase the length of each string by 30%.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`bool<class_bool>` **pseudolocalization_fake_bidi_enabled** = `false` `🔗<class_TranslationDomain_property_pseudolocalization_fake_bidi_enabled>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_fake_bidi_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pseudolocalization_fake_bidi_enabled**()

If `true`, emulate bidirectional (right-to-left) text when pseudolocalization is enabled. This can be used to spot issues with RTL layout and UI mirroring that will crop up if the project is localized to RTL languages such as Arabic or Hebrew.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`bool<class_bool>` **pseudolocalization_override_enabled** = `false` `🔗<class_TranslationDomain_property_pseudolocalization_override_enabled>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_override_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pseudolocalization_override_enabled**()

Replace all characters in the string with `*`. Useful for finding non-localizable strings.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`String<class_String>` **pseudolocalization_prefix** = `"["` `🔗<class_TranslationDomain_property_pseudolocalization_prefix>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_prefix**(value: `String<class_String>`)
- `String<class_String>` **get_pseudolocalization_prefix**()

Prefix that will be prepended to the pseudolocalized string.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`bool<class_bool>` **pseudolocalization_skip_placeholders_enabled** = `true` `🔗<class_TranslationDomain_property_pseudolocalization_skip_placeholders_enabled>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_skip_placeholders_enabled**(value: `bool<class_bool>`)
- `bool<class_bool>` **is_pseudolocalization_skip_placeholders_enabled**()

Skip placeholders for string formatting like `%s` or `%f` during pseudolocalization. Useful to identify strings which need additional control characters to display correctly.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-item-separator

classref-property

`String<class_String>` **pseudolocalization_suffix** = `"]"` `🔗<class_TranslationDomain_property_pseudolocalization_suffix>`

classref-property-setget

- `void (No return value.)` **set_pseudolocalization_suffix**(value: `String<class_String>`)
- `String<class_String>` **get_pseudolocalization_suffix**()

Suffix that will be appended to the pseudolocalized string.

**Note:** Updating this property does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` notification manually after you have finished modifying pseudolocalization related options.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_translation**(translation: `Translation<class_Translation>`) `🔗<class_TranslationDomain_method_add_translation>`

Adds a translation.

classref-item-separator

classref-method

`void (No return value.)` **clear**() `🔗<class_TranslationDomain_method_clear>`

Removes all translations.

classref-item-separator

classref-method

`Array<class_Array>`\[`Translation<class_Translation>`\] **find_translations**(locale: `String<class_String>`, exact: `bool<class_bool>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_find_translations>`

Returns the `Translation<class_Translation>` instances that match `locale` (see `TranslationServer.compare_locales()<class_TranslationServer_method_compare_locales>`). If `exact` is `true`, only instances whose locale exactly equals `locale` will be returned.

classref-item-separator

classref-method

`String<class_String>` **get_locale_override**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_get_locale_override>`

Returns the locale override of the domain. Returns an empty string if locale override is disabled.

classref-item-separator

classref-method

`Translation<class_Translation>` **get_translation_object**(locale: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_get_translation_object>`

**Deprecated:** Use `find_translations()<class_TranslationDomain_method_find_translations>` instead.

Returns the `Translation<class_Translation>` instance that best matches `locale`. Returns `null` if there are no matches.

classref-item-separator

classref-method

`Array<class_Array>`\[`Translation<class_Translation>`\] **get_translations**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_get_translations>`

Returns all available `Translation<class_Translation>` instances as added by `add_translation()<class_TranslationDomain_method_add_translation>`.

classref-item-separator

classref-method

`bool<class_bool>` **has_translation**(translation: `Translation<class_Translation>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_has_translation>`

Returns `true` if this translation domain contains the given `translation`.

classref-item-separator

classref-method

`bool<class_bool>` **has_translation_for_locale**(locale: `String<class_String>`, exact: `bool<class_bool>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_has_translation_for_locale>`

Returns `true` if there are any `Translation<class_Translation>` instances that match `locale` (see `TranslationServer.compare_locales()<class_TranslationServer_method_compare_locales>`). If `exact` is `true`, only instances whose locale exactly equals `locale` are considered.

classref-item-separator

classref-method

`StringName<class_StringName>` **pseudolocalize**(message: `StringName<class_StringName>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_pseudolocalize>`

Returns the pseudolocalized string based on the `message` passed in.

classref-item-separator

classref-method

`void (No return value.)` **remove_translation**(translation: `Translation<class_Translation>`) `🔗<class_TranslationDomain_method_remove_translation>`

Removes the given translation.

classref-item-separator

classref-method

`void (No return value.)` **set_locale_override**(locale: `String<class_String>`) `🔗<class_TranslationDomain_method_set_locale_override>`

Sets the locale override of the domain.

If `locale` is an empty string, locale override is disabled. Otherwise, `locale` will be standardized to match known locales (e.g. `en-US` would be matched to `en_US`).

**Note:** Calling this method does not automatically update texts in the scene tree. Please propagate the `MainLoop.NOTIFICATION_TRANSLATION_CHANGED<class_MainLoop_constant_NOTIFICATION_TRANSLATION_CHANGED>` signal manually.

classref-item-separator

classref-method

`StringName<class_StringName>` **translate**(message: `StringName<class_StringName>`, context: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_translate>`

Returns the current locale's translation for the given message and context.

classref-item-separator

classref-method

`StringName<class_StringName>` **translate_plural**(message: `StringName<class_StringName>`, message_plural: `StringName<class_StringName>`, n: `int<class_int>`, context: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_TranslationDomain_method_translate_plural>`

Returns the current locale's translation for the given message, plural message and context.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.