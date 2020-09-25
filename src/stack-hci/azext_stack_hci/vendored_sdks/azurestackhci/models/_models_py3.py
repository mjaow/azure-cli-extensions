# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Cluster(TrackedResource):
    """Cluster details.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :ivar provisioning_state: Provisioning state. Possible values include: "Succeeded", "Failed",
     "Canceled", "Accepted", "Provisioning".
    :vartype provisioning_state: str or ~azure_stack_hci_client.models.ProvisioningState
    :ivar status: Status of the cluster agent. Possible values include: "NeverConnected",
     "ConnectedRecently", "NotConnectedRecently", "Expired", "Error".
    :vartype status: str or ~azure_stack_hci_client.models.Status
    :ivar cloud_id: Unique, immutable resource id.
    :vartype cloud_id: str
    :param aad_client_id: App id of cluster AAD identity.
    :type aad_client_id: str
    :param aad_tenant_id: Tenant id of cluster AAD identity.
    :type aad_tenant_id: str
    :ivar trial_days_remaining: Number of days remaining in the trial period.
    :vartype trial_days_remaining: float
    :ivar billing_model: Type of billing applied to the resource.
    :vartype billing_model: str
    :ivar cluster_name: Name of the on-prem cluster connected to this resource.
    :vartype cluster_name: str
    :ivar cluster_id: Unique id generated by the on-prem cluster.
    :vartype cluster_id: str
    :ivar cluster_version: Version of the cluster software.
    :vartype cluster_version: str
    :ivar nodes: List of nodes reported by the cluster.
    :vartype nodes: list[~azure_stack_hci_client.models.ClusterNode]
    :ivar last_updated: Last time the cluster reported the data.
    :vartype last_updated: ~datetime.datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'cloud_id': {'readonly': True},
        'trial_days_remaining': {'readonly': True},
        'billing_model': {'readonly': True},
        'cluster_name': {'readonly': True},
        'cluster_id': {'readonly': True},
        'cluster_version': {'readonly': True},
        'nodes': {'readonly': True},
        'last_updated': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'cloud_id': {'key': 'properties.cloudId', 'type': 'str'},
        'aad_client_id': {'key': 'properties.aadClientId', 'type': 'str'},
        'aad_tenant_id': {'key': 'properties.aadTenantId', 'type': 'str'},
        'trial_days_remaining': {'key': 'properties.trialDaysRemaining', 'type': 'float'},
        'billing_model': {'key': 'properties.billingModel', 'type': 'str'},
        'cluster_name': {'key': 'properties.reportedProperties.clusterName', 'type': 'str'},
        'cluster_id': {'key': 'properties.reportedProperties.clusterId', 'type': 'str'},
        'cluster_version': {'key': 'properties.reportedProperties.clusterVersion', 'type': 'str'},
        'nodes': {'key': 'properties.reportedProperties.nodes', 'type': '[ClusterNode]'},
        'last_updated': {'key': 'properties.reportedProperties.lastUpdated', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        aad_client_id: Optional[str] = None,
        aad_tenant_id: Optional[str] = None,
        **kwargs
    ):
        super(Cluster, self).__init__(tags=tags, location=location, **kwargs)
        self.provisioning_state = None
        self.status = None
        self.cloud_id = None
        self.aad_client_id = aad_client_id
        self.aad_tenant_id = aad_tenant_id
        self.trial_days_remaining = None
        self.billing_model = None
        self.cluster_name = None
        self.cluster_id = None
        self.cluster_version = None
        self.nodes = None
        self.last_updated = None


class ClusterList(msrest.serialization.Model):
    """List of clusters.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of clusters.
    :type value: list[~azure_stack_hci_client.models.Cluster]
    :ivar next_link: Link to the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Cluster]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Cluster"]] = None,
        **kwargs
    ):
        super(ClusterList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class ClusterNode(msrest.serialization.Model):
    """Cluster node details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the cluster node.
    :vartype name: str
    :ivar id: Id of the node in the cluster.
    :vartype id: float
    :ivar manufacturer: Manufacturer of the cluster node hardware.
    :vartype manufacturer: str
    :ivar model: Model name of the cluster node hardware.
    :vartype model: str
    :ivar os_name: Operating system running on the cluster node.
    :vartype os_name: str
    :ivar os_version: Version of the operating system running on the cluster node.
    :vartype os_version: str
    :ivar serial_number: Immutable id of the cluster node.
    :vartype serial_number: str
    :ivar core_count: Number of physical cores on the cluster node.
    :vartype core_count: float
    :ivar memory_in_gi_b: Total available memory on the cluster node (in GiB).
    :vartype memory_in_gi_b: float
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'manufacturer': {'readonly': True},
        'model': {'readonly': True},
        'os_name': {'readonly': True},
        'os_version': {'readonly': True},
        'serial_number': {'readonly': True},
        'core_count': {'readonly': True},
        'memory_in_gi_b': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'float'},
        'manufacturer': {'key': 'manufacturer', 'type': 'str'},
        'model': {'key': 'model', 'type': 'str'},
        'os_name': {'key': 'osName', 'type': 'str'},
        'os_version': {'key': 'osVersion', 'type': 'str'},
        'serial_number': {'key': 'serialNumber', 'type': 'str'},
        'core_count': {'key': 'coreCount', 'type': 'float'},
        'memory_in_gi_b': {'key': 'memoryInGiB', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ClusterNode, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.manufacturer = None
        self.model = None
        self.os_name = None
        self.os_version = None
        self.serial_number = None
        self.core_count = None
        self.memory_in_gi_b = None


class ClusterUpdate(msrest.serialization.Model):
    """Cluster details to update.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ClusterUpdate, self).__init__(**kwargs)
        self.tags = tags


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: object
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(msrest.serialization.Model):
    """The resource management error response.

    :param error: The error object.
    :type error: ~azure_stack_hci_client.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponseError"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseError(msrest.serialization.Model):
    """The error object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure_stack_hci_client.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure_stack_hci_client.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponse]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class Operation(msrest.serialization.Model):
    """Operation details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the operation.
    :vartype name: str
    :param display: Operation properties.
    :type display: ~azure_stack_hci_client.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        display: Optional["OperationDisplay"] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """Operation properties.

    :param provider: Resource provider name.
    :type provider: str
    :param resource: Resource type name.
    :type resource: str
    :param operation: Operation name.
    :type operation: str
    :param description: Operation description.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationList(msrest.serialization.Model):
    """List of available operations.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of operations.
    :type value: list[~azure_stack_hci_client.models.Operation]
    :ivar next_link: Link to the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None