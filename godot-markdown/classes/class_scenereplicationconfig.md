github_url
hide

# SceneReplicationConfig

**Inherits:** `Resource<class_Resource>` **\<** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Configuration for properties to synchronize with a `MultiplayerSynchronizer<class_MultiplayerSynchronizer>`.

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **ReplicationMode**: `🔗<enum_SceneReplicationConfig_ReplicationMode>`

classref-enumeration-constant

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>` **REPLICATION_MODE_NEVER** = `0`

Do not keep the given property synchronized.

classref-enumeration-constant

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>` **REPLICATION_MODE_ALWAYS** = `1`

Replicate the given property on process by constantly sending updates using unreliable transfer mode.

classref-enumeration-constant

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>` **REPLICATION_MODE_ON_CHANGE** = `2`

Replicate the given property on process by sending updates using reliable transfer mode when its value changes.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`void (No return value.)` **add_property**(path: `NodePath<class_NodePath>`, index: `int<class_int>` = -1) `🔗<class_SceneReplicationConfig_method_add_property>`

Adds the property identified by the given `path` to the list of the properties being synchronized, optionally passing an `index`.

**Note:** For details on restrictions and limitations on property synchronization, see `MultiplayerSynchronizer<class_MultiplayerSynchronizer>`.

classref-item-separator

classref-method

`Array<class_Array>`\[`NodePath<class_NodePath>`\] **get_properties**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SceneReplicationConfig_method_get_properties>`

Returns a list of synchronized property `NodePath<class_NodePath>`s.

classref-item-separator

classref-method

`bool<class_bool>` **has_property**(path: `NodePath<class_NodePath>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SceneReplicationConfig_method_has_property>`

Returns `true` if the given `path` is configured for synchronization.

classref-item-separator

classref-method

`int<class_int>` **property_get_index**(path: `NodePath<class_NodePath>`) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_SceneReplicationConfig_method_property_get_index>`

Finds the index of the given `path`.

classref-item-separator

classref-method

`ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>` **property_get_replication_mode**(path: `NodePath<class_NodePath>`) `🔗<class_SceneReplicationConfig_method_property_get_replication_mode>`

Returns the replication mode for the property identified by the given `path`.

classref-item-separator

classref-method

`bool<class_bool>` **property_get_spawn**(path: `NodePath<class_NodePath>`) `🔗<class_SceneReplicationConfig_method_property_get_spawn>`

Returns `true` if the property identified by the given `path` is configured to be synchronized on spawn.

classref-item-separator

classref-method

`bool<class_bool>` **property_get_sync**(path: `NodePath<class_NodePath>`) `🔗<class_SceneReplicationConfig_method_property_get_sync>`

**Deprecated:** Use `property_get_replication_mode()<class_SceneReplicationConfig_method_property_get_replication_mode>` instead.

Returns `true` if the property identified by the given `path` is configured to be synchronized on process.

classref-item-separator

classref-method

`bool<class_bool>` **property_get_watch**(path: `NodePath<class_NodePath>`) `🔗<class_SceneReplicationConfig_method_property_get_watch>`

**Deprecated:** Use `property_get_replication_mode()<class_SceneReplicationConfig_method_property_get_replication_mode>` instead.

Returns `true` if the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

classref-item-separator

classref-method

`void (No return value.)` **property_set_replication_mode**(path: `NodePath<class_NodePath>`, mode: `ReplicationMode<enum_SceneReplicationConfig_ReplicationMode>`) `🔗<class_SceneReplicationConfig_method_property_set_replication_mode>`

Sets the synchronization mode for the property identified by the given `path`.

classref-item-separator

classref-method

`void (No return value.)` **property_set_spawn**(path: `NodePath<class_NodePath>`, enabled: `bool<class_bool>`) `🔗<class_SceneReplicationConfig_method_property_set_spawn>`

Sets whether the property identified by the given `path` is configured to be synchronized on spawn.

classref-item-separator

classref-method

`void (No return value.)` **property_set_sync**(path: `NodePath<class_NodePath>`, enabled: `bool<class_bool>`) `🔗<class_SceneReplicationConfig_method_property_set_sync>`

**Deprecated:** Use `property_set_replication_mode()<class_SceneReplicationConfig_method_property_set_replication_mode>` with `REPLICATION_MODE_ALWAYS<class_SceneReplicationConfig_constant_REPLICATION_MODE_ALWAYS>` instead.

Sets whether the property identified by the given `path` is configured to be synchronized on process.

classref-item-separator

classref-method

`void (No return value.)` **property_set_watch**(path: `NodePath<class_NodePath>`, enabled: `bool<class_bool>`) `🔗<class_SceneReplicationConfig_method_property_set_watch>`

**Deprecated:** Use `property_set_replication_mode()<class_SceneReplicationConfig_method_property_set_replication_mode>` with `REPLICATION_MODE_ON_CHANGE<class_SceneReplicationConfig_constant_REPLICATION_MODE_ON_CHANGE>` instead.

Sets whether the property identified by the given `path` is configured to be reliably synchronized when changes are detected on process.

classref-item-separator

classref-method

`void (No return value.)` **remove_property**(path: `NodePath<class_NodePath>`) `🔗<class_SceneReplicationConfig_method_remove_property>`

Removes the property identified by the given `path` from the configuration.