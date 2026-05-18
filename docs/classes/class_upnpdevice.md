github_url
hide

# UPNPDevice

**Inherits:** `RefCounted<class_RefCounted>` **\<** `Object<class_Object>`

Universal Plug and Play (UPnP) device.

classref-introduction-group

## Description

Universal Plug and Play (UPnP) device. See `UPNP<class_UPNP>` for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows to manage port mappings (port forwarding) and to query network information of the device (like local and external IP address and status). Note that methods on this class are synchronous and block the calling thread.

classref-reftable-group

## Properties

classref-reftable-group

## Methods

classref-section-separator

classref-descriptions-group

## Enumerations

classref-enumeration

enum **IGDStatus**: `🔗<enum_UPNPDevice_IGDStatus>`

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_OK** = `0`

OK.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_HTTP_ERROR** = `1`

HTTP error.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_HTTP_EMPTY** = `2`

Empty HTTP response.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_NO_URLS** = `3`

**Deprecated:** This value is no longer used.

Returned response contained no URLs.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_NO_IGD** = `4`

Not a valid IGD.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_DISCONNECTED** = `5`

Disconnected.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_UNKNOWN_DEVICE** = `6`

Unknown device.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_INVALID_CONTROL** = `7`

Invalid control.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_MALLOC_ERROR** = `8`

**Deprecated:** This value is no longer used.

Memory allocation error.

classref-enumeration-constant

`IGDStatus<enum_UPNPDevice_IGDStatus>` **IGD_STATUS_UNKNOWN_ERROR** = `9`

Unknown error.

classref-section-separator

classref-descriptions-group

## Property Descriptions

classref-property

`String<class_String>` **description_url** = `""` `🔗<class_UPNPDevice_property_description_url>`

classref-property-setget

- `void (No return value.)` **set_description_url**(value: `String<class_String>`)
- `String<class_String>` **get_description_url**()

URL to the device description.

classref-item-separator

classref-property

`String<class_String>` **igd_control_url** = `""` `🔗<class_UPNPDevice_property_igd_control_url>`

classref-property-setget

- `void (No return value.)` **set_igd_control_url**(value: `String<class_String>`)
- `String<class_String>` **get_igd_control_url**()

IDG control URL.

classref-item-separator

classref-property

`String<class_String>` **igd_our_addr** = `""` `🔗<class_UPNPDevice_property_igd_our_addr>`

classref-property-setget

- `void (No return value.)` **set_igd_our_addr**(value: `String<class_String>`)
- `String<class_String>` **get_igd_our_addr**()

Address of the local machine in the network connecting it to this **UPNPDevice**.

classref-item-separator

classref-property

`String<class_String>` **igd_service_type** = `""` `🔗<class_UPNPDevice_property_igd_service_type>`

classref-property-setget

- `void (No return value.)` **set_igd_service_type**(value: `String<class_String>`)
- `String<class_String>` **get_igd_service_type**()

IGD service type.

classref-item-separator

classref-property

`IGDStatus<enum_UPNPDevice_IGDStatus>` **igd_status** = `9` `🔗<class_UPNPDevice_property_igd_status>`

classref-property-setget

- `void (No return value.)` **set_igd_status**(value: `IGDStatus<enum_UPNPDevice_IGDStatus>`)
- `IGDStatus<enum_UPNPDevice_IGDStatus>` **get_igd_status**()

IGD status.

classref-item-separator

classref-property

`String<class_String>` **service_type** = `""` `🔗<class_UPNPDevice_property_service_type>`

classref-property-setget

- `void (No return value.)` **set_service_type**(value: `String<class_String>`)
- `String<class_String>` **get_service_type**()

Service type.

classref-section-separator

classref-descriptions-group

## Method Descriptions

classref-method

`int<class_int>` **add_port_mapping**(port: `int<class_int>`, port_internal: `int<class_int>` = 0, desc: `String<class_String>` = "", proto: `String<class_String>` = "UDP", duration: `int<class_int>` = 0) `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_UPNPDevice_method_add_port_mapping>`

Adds a port mapping to forward the given external port on this **UPNPDevice** for the given protocol to the local machine. See `UPNP.add_port_mapping()<class_UPNP_method_add_port_mapping>`.

classref-item-separator

classref-method

`int<class_int>` **delete_port_mapping**(port: `int<class_int>`, proto: `String<class_String>` = "UDP") `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_UPNPDevice_method_delete_port_mapping>`

Deletes the port mapping identified by the given port and protocol combination on this device. See `UPNP.delete_port_mapping()<class_UPNP_method_delete_port_mapping>`.

classref-item-separator

classref-method

`bool<class_bool>` **is_valid_gateway**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_UPNPDevice_method_is_valid_gateway>`

Returns `true` if this is a valid IGD (InternetGatewayDevice) which potentially supports port forwarding.

classref-item-separator

classref-method

`String<class_String>` **query_external_address**() `const (This method has no side effects. It doesn't modify any of the instance's member variables.)` `🔗<class_UPNPDevice_method_query_external_address>`

Returns the external IP address of this **UPNPDevice** or an empty string.