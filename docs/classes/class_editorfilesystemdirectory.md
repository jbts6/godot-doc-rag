github_url
hide

# EditorFileSystemDirectory

**Inherits:** `Object<class_Object>`

A directory for the resource filesystem.

classref-introduction-group

## Description

A more generalized, low-level variation of the directory concept.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **find_dir_index**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_find_dir_index>`

Returns the index of the directory with name `name` or `-1` if not found.

classref-item-separator

classref-method

`int<class_int>` **find_file_index**(name: `String<class_String>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_find_file_index>`

Returns the index of the file with name `name` or `-1` if not found.

classref-item-separator

classref-method

`String<class_String>` **get_file**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file>`

Returns the name of the file at index `idx`.

classref-item-separator

classref-method

`int<class_int>` **get_file_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file_count>`

Returns the number of files in this directory.

classref-item-separator

classref-method

`bool<class_bool>` **get_file_import_is_valid**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file_import_is_valid>`

Returns `true` if the file at index `idx` imported properly.

classref-item-separator

classref-method

`String<class_String>` **get_file_path**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file_path>`

Returns the path to the file at index `idx`.

classref-item-separator

classref-method

`String<class_String>` **get_file_script_class_extends**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file_script_class_extends>`

Returns the base class of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

classref-item-separator

classref-method

`String<class_String>` **get_file_script_class_name**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file_script_class_name>`

Returns the name of the script class defined in the file at index `idx`. If the file doesn't define a script class using the `class_name` syntax, this will return an empty string.

classref-item-separator

classref-method

`StringName<class_StringName>` **get_file_type**(idx: `int<class_int>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_file_type>`

Returns the resource type of the file at index `idx`. This returns a string such as `"Resource"` or `"GDScript"`, *not* a file extension such as `".gd"`.

classref-item-separator

classref-method

`String<class_String>` **get_name**() `🔗<class_EditorFileSystemDirectory_method_get_name>`

Returns the name of this directory.

classref-item-separator

classref-method

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` **get_parent**() `🔗<class_EditorFileSystemDirectory_method_get_parent>`

Returns the parent directory for this directory or `null` if called on a directory at `res://` or `user://`.

classref-item-separator

classref-method

`String<class_String>` **get_path**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_path>`

Returns the path to this directory.

classref-item-separator

classref-method

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>` **get_subdir**(idx: `int<class_int>`) `🔗<class_EditorFileSystemDirectory_method_get_subdir>`

Returns the subdirectory at index `idx`.

classref-item-separator

classref-method

`int<class_int>` **get_subdir_count**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorFileSystemDirectory_method_get_subdir_count>`

Returns the number of subdirectories in this directory.