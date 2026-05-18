github_url
hide

# Translation

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

**Inherited By:** `OptimizedTranslation<class_OptimizedTranslation>`

A language translation that maps a collection of strings to their individual translations.

classref-introduction-group

## Description

**Translation** maps a collection of strings to their individual translations, and also provides convenience methods for pluralization.

A **Translation** consists of messages. A message is identified by its context and untranslated string. Unlike [gettext](https://www.gnu.org/software/gettext/), using an empty context string in Godot means not using any context.

classref-introduction-group

## Tutorials

- `Internationalizing games <../tutorials/i18n/internationalizing_games>`
- `Localization using gettext <../tutorials/i18n/localization_using_gettext>`
- `Locales <../tutorials/i18n/locales>`

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **locale** = `"en"` `🔗<class_Translation_property_locale>`

classref-property-setget

- `void (No return value.)` **set_locale**(value: `String<class_String>`)
- `String<class_String>` **get_locale**()

The locale of the translation.

classref-item-separator

classref-property

`String<class_String>` **plural_rules_override** = `""` `🔗<class_Translation_property_plural_rules_override>`

classref-property-setget

- `void (No return value.)` **set_plural_rules_override**(value: `String<class_String>`)
- `String<class_String>` **get_plural_rules_override**()

The plural rules string to enforce. See [GNU gettext](https://www.gnu.org/software/gettext/manual/html_node/Plural-forms.html) for examples and more info.

If empty or invalid, default plural rules from `TranslationServer.get_plural_rules()<class_TranslationServer_method_get_plural_rules>` are used. The English plural rules are used as a fallback.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`StringName<class_StringName>` **\_get_message**(src_message: `StringName<class_StringName>`, context: `StringName<class_StringName>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_private_method__get_message>`

Virtual method to override `get_message()<class_Translation_method_get_message>`.

classref-item-separator

classref-method

`StringName<class_StringName>` **\_get_plural_message**(src_message: `StringName<class_StringName>`, src_plural_message: `StringName<class_StringName>`, n: `int<class_int>`, context: `StringName<class_StringName>`) `virtual (This method should typically be overridden by the user to have any effect.)` `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_private_method__get_plural_message>`

Virtual method to override `get_plural_message()<class_Translation_method_get_plural_message>`.

classref-item-separator

classref-method

`void (No return value.)` **add_message**(src_message: `StringName<class_StringName>`, xlated_message: `StringName<class_StringName>`, context: `StringName<class_StringName>` = &"") `🔗<class_Translation_method_add_message>`

Adds a message if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

classref-item-separator

classref-method

`void (No return value.)` **add_plural_message**(src_message: `StringName<class_StringName>`, xlated_messages: `PackedStringArray<class_PackedStringArray>`, context: `StringName<class_StringName>` = &"") `🔗<class_Translation_method_add_plural_message>`

Adds a message involving plural translation if nonexistent, followed by its translation.

An additional context could be used to specify the translation context or differentiate polysemic words.

classref-item-separator

classref-method

`void (No return value.)` **erase_message**(src_message: `StringName<class_StringName>`, context: `StringName<class_StringName>` = &"") `🔗<class_Translation_method_erase_message>`

Erases a message.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_message**(src_message: `StringName<class_StringName>`, context: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_method_get_message>`

Returns a message's translation.

classref-item-separator

classref-method

`int<class_int>` **get_message_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_method_get_message_count>`

Returns the number of existing messages.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_message_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_method_get_message_list>`

Returns the keys of all messages, that is, the context and untranslated strings of each message.

**Note:** If a message does not use a context, the corresponding element is the untranslated string. Otherwise, the corresponding element is the context and untranslated string separated by the EOT character (`U+0004`). This is done for compatibility purposes.

    for key in translation.get_message_list():
        var p = key.find("\u0004")
        if p == -1:
            var untranslated = key
            print("Message %s" % untranslated)
        else:
            var context = key.substr(0, p)
            var untranslated = key.substr(p + 1)
            print("Message %s with context %s" % [untranslated, context])

classref-item-separator

classref-method

`StringName<class_StringName>` **get_plural_message**(src_message: `StringName<class_StringName>`, src_plural_message: `StringName<class_StringName>`, n: `int<class_int>`, context: `StringName<class_StringName>` = &"") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_method_get_plural_message>`

Returns a message's translation involving plurals.

The number `n` is the number or quantity of the plural object. It will be used to guide the translation system to fetch the correct plural form for the selected language.

**Note:** Plurals are only supported in `gettext-based translations (PO) <../tutorials/i18n/localization_using_gettext>`, not CSV.

classref-item-separator

classref-method

`PackedStringArray<class_PackedStringArray>` **get_translated_message_list**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_Translation_method_get_translated_message_list>`

Returns all the translated strings.