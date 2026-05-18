github_url
hide

# ThemeDB

**Inherits:** `Object<class_Object>`

A singleton that provides access to static information about `Theme<class_Theme>` resources used by the engine and by your project.

classref-introduction-group

## Description

This singleton provides access to static information about `Theme<class_Theme>` resources used by the engine and by your projects. You can fetch the default engine theme, as well as your project configured theme.

**ThemeDB** also contains fallback values for theme properties.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Signals

classref-signal

**fallback_changed**() `🔗<class_ThemeDB_signal_fallback_changed>`

Emitted when one of the fallback values had been changed. Use it to refresh the look of controls that may rely on the fallback theme items.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`float<class_float>` **fallback_base_scale** = `1.0` `🔗<class_ThemeDB_property_fallback_base_scale>`

classref-property-setget

- `void (No return value.)` **set_fallback_base_scale**(value: `float<class_float>`)
- `float<class_float>` **get_fallback_base_scale**()

The fallback base scale factor of every `Control<class_Control>` node and `Theme<class_Theme>` resource. Used when no other value is available to the control.

See also `Theme.default_base_scale<class_Theme_property_default_base_scale>`.

classref-item-separator

classref-property

`Font<class_Font>` **fallback_font** `🔗<class_ThemeDB_property_fallback_font>`

classref-property-setget

- `void (No return value.)` **set_fallback_font**(value: `Font<class_Font>`)
- `Font<class_Font>` **get_fallback_font**()

The fallback font of every `Control<class_Control>` node and `Theme<class_Theme>` resource. Used when no other value is available to the control.

See also `Theme.default_font<class_Theme_property_default_font>`.

classref-item-separator

classref-property

`int<class_int>` **fallback_font_size** = `16` `🔗<class_ThemeDB_property_fallback_font_size>`

classref-property-setget

- `void (No return value.)` **set_fallback_font_size**(value: `int<class_int>`)
- `int<class_int>` **get_fallback_font_size**()

The fallback font size of every `Control<class_Control>` node and `Theme<class_Theme>` resource. Used when no other value is available to the control.

See also `Theme.default_font_size<class_Theme_property_default_font_size>`.

classref-item-separator

classref-property

`Texture2D<class_Texture2D>` **fallback_icon** `🔗<class_ThemeDB_property_fallback_icon>`

classref-property-setget

- `void (No return value.)` **set_fallback_icon**(value: `Texture2D<class_Texture2D>`)
- `Texture2D<class_Texture2D>` **get_fallback_icon**()

The fallback icon of every `Control<class_Control>` node and `Theme<class_Theme>` resource. Used when no other value is available to the control.

classref-item-separator

classref-property

`StyleBox<class_StyleBox>` **fallback_stylebox** `🔗<class_ThemeDB_property_fallback_stylebox>`

classref-property-setget

- `void (No return value.)` **set_fallback_stylebox**(value: `StyleBox<class_StyleBox>`)
- `StyleBox<class_StyleBox>` **get_fallback_stylebox**()

The fallback stylebox of every `Control<class_Control>` node and `Theme<class_Theme>` resource. Used when no other value is available to the control.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Theme<class_Theme>` **get_default_theme**() `🔗<class_ThemeDB_method_get_default_theme>`

Returns a reference to the default engine `Theme<class_Theme>`. This theme resource is responsible for the out-of-the-box look of `Control<class_Control>` nodes and cannot be overridden.

classref-item-separator

classref-method

`Theme<class_Theme>` **get_project_theme**() `🔗<class_ThemeDB_method_get_project_theme>`

Returns a reference to the custom project `Theme<class_Theme>`. This theme resources allows to override the default engine theme for every control node in the project.

To set the project theme, see `ProjectSettings.gui/theme/custom<class_ProjectSettings_property_gui/theme/custom>`.