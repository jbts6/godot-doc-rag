github_url
hide

# EditorScenePostImport

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Post-processes scenes after import.

classref-introduction-group

## Description

Imported scenes can be automatically modified right after import by setting their **Custom Script** Import property to a `tool` script that inherits from this class.

The `_post_import()<class_EditorScenePostImport_private_method__post_import>` callback receives the imported scene's root node and returns the modified version of the scene:

gdscript

@tool \# Needed so it runs in editor. extends EditorScenePostImport

\# This sample changes all node names. \# Called right after the scene is imported and gets the root node. func post_import(scene): \# Change all node names to "modified\_\[oldnodename\]" iterate(scene) return scene \# Remember to return the imported scene

func iterate(node):
if node != null:
node.name = "modified\_" + node.name for child in node.get_children(): iterate(child)

csharp

using Godot;

// This sample changes all node names. // Called right after the scene is imported and gets the root node. \[Tool\] public partial class NodeRenamer : EditorScenePostImport { public override GodotObject PostImport(Node scene) { // Change all node names to "modified\_\[oldnodename\]" Iterate(scene); return scene; // Remember to return the imported scene }

> public void Iterate(Node node) { if (node != null) { node.Name = \$"modified\_{node.Name}"; foreach (Node child in node.GetChildren()) { Iterate(child); } } }

}

classref-introduction-group

## Tutorials

- [Importing 3D scenes: Configuration: Using import scripts for automation](../tutorials/assets_pipeline/importing_3d_scenes/import_configuration.html#using-import-scripts-for-automation)

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`Object<class_Object>` **\_post_import**(scene: `Node<class_Node>`) `virtual (This method should typically be overridden by the user to have any effect.)` `🔗<class_EditorScenePostImport_private_method__post_import>`

Called after the scene was imported. This method must return the modified version of the scene.

classref-item-separator

classref-method

`String<class_String>` **get_source_file**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_EditorScenePostImport_method_get_source_file>`

Returns the source file path which got imported (e.g. `res://scene.dae`).