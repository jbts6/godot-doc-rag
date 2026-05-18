github_url
hide

# ZIPPacker

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Allows the creation of ZIP files.

classref-introduction-group

## Description

This class implements a writer that allows storing the multiple blobs in a ZIP archive. See also `ZIPReader<class_ZIPReader>` and `PCKPacker<class_PCKPacker>`.

    # Create a ZIP archive with a single file at its root.
    func write_zip_file():
        var writer = ZIPPacker.new()
        var err = writer.open("user://archive.zip")
        if err != OK:
            return err
        writer.start_file("hello.txt")
        writer.write_file("Hello World".to_utf8_buffer())
        writer.close_file()

        writer.close()
        return OK

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ZipAppend**: `🔗<enum_ZIPPacker_ZipAppend>`

classref-enumeration-constant

`ZipAppend<enum_ZIPPacker_ZipAppend>` **APPEND_CREATE** = `0`

Create a new zip archive at the given path.

classref-enumeration-constant

`ZipAppend<enum_ZIPPacker_ZipAppend>` **APPEND_CREATEAFTER** = `1`

Append a new zip archive to the end of the already existing file at the given path.

classref-enumeration-constant

`ZipAppend<enum_ZIPPacker_ZipAppend>` **APPEND_ADDINZIP** = `2`

Add new files to the existing zip archive at the given path.

classref-item-separator

classref-enumeration

enum **CompressionLevel**: `🔗<enum_ZIPPacker_CompressionLevel>`

classref-enumeration-constant

`CompressionLevel<enum_ZIPPacker_CompressionLevel>` **COMPRESSION_DEFAULT** = `-1`

Start a file with the default Deflate compression level (`6`). This is a good compromise between speed and file size.

classref-enumeration-constant

`CompressionLevel<enum_ZIPPacker_CompressionLevel>` **COMPRESSION_NONE** = `0`

Start a file with no compression. This is also known as the "Store" compression mode and is the fastest method of packing files inside a ZIP archive. Consider using this mode for files that are already compressed (such as JPEG, PNG, MP3, or Ogg Vorbis files).

classref-enumeration-constant

`CompressionLevel<enum_ZIPPacker_CompressionLevel>` **COMPRESSION_FAST** = `1`

Start a file with the fastest Deflate compression level (`1`). This is fast to compress, but results in larger file sizes than `COMPRESSION_DEFAULT<class_ZIPPacker_constant_COMPRESSION_DEFAULT>`. Decompression speed is generally unaffected by the chosen compression level.

classref-enumeration-constant

`CompressionLevel<enum_ZIPPacker_CompressionLevel>` **COMPRESSION_BEST** = `9`

Start a file with the best Deflate compression level (`9`). This is slow to compress, but results in smaller file sizes than `COMPRESSION_DEFAULT<class_ZIPPacker_constant_COMPRESSION_DEFAULT>`. Decompression speed is generally unaffected by the chosen compression level.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`int<class_int>` **compression_level** = `-1` `🔗<class_ZIPPacker_property_compression_level>`

classref-property-setget

- `void (No return value.)` **set_compression_level**(value: `int<class_int>`)
- `int<class_int>` **get_compression_level**()

The compression level used when `start_file()<class_ZIPPacker_method_start_file>` is called. Use `CompressionLevel<enum_ZIPPacker_CompressionLevel>` as a reference.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Error<enum_@GlobalScope_Error>` **add_directory**(path: `String<class_String>`, permissions: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`\] = 493, modified_time: `int<class_int>` = 0) `🔗<class_ZIPPacker_method_add_directory>`

Adds directory to the archive. If `modified_time` is set to `0`, current system time is used.

**Note:** Directories are automatically created when `start_file()<class_ZIPPacker_method_start_file>` is called, use this function before adding files to create directories with custom permissions and modification time.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **close**() `🔗<class_ZIPPacker_method_close>`

Closes the underlying resources used by this instance.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **close_file**() `🔗<class_ZIPPacker_method_close_file>`

Stops writing to a file within the archive.

It will fail if there is no open file.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **open**(path: `String<class_String>`, append: `ZipAppend<enum_ZIPPacker_ZipAppend>` = 0) `🔗<class_ZIPPacker_method_open>`

Opens a zip file for writing at the given path using the specified write mode.

This must be called before everything else.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **start_file**(path: `String<class_String>`, permissions: `BitField (This value is an integer composed as a bitmask of the following flags.)`\[`UnixPermissionFlags<enum_FileAccess_UnixPermissionFlags>`\] = 420, modified_time: `int<class_int>` = 0) `🔗<class_ZIPPacker_method_start_file>`

Starts writing to a file within the archive. Only one file can be written at the same time. If `modified_time` is set to `0`, current system time is used.

Must be called after `open()<class_ZIPPacker_method_open>`.

classref-item-separator

classref-method

`Error<enum_@GlobalScope_Error>` **write_file**(data: `PackedByteArray<class_PackedByteArray>`) `🔗<class_ZIPPacker_method_write_file>`

Write the given `data` to the file.

Needs to be called after `start_file()<class_ZIPPacker_method_start_file>`.