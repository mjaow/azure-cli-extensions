# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._network_manager_deployment_status_operations import build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class NetworkManagerDeploymentStatusOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.network.v2022_02_01_preview.aio.NetworkManagementClient`'s
        :attr:`network_manager_deployment_status` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def list(
        self,
        resource_group_name: str,
        network_manager_name: str,
        parameters: "_models.NetworkManagerDeploymentStatusParameter",
        **kwargs: Any
    ) -> "_models.NetworkManagerDeploymentStatusListResult":
        """Post to List of Network Manager Deployment Status.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_manager_name: The name of the network manager.
        :type network_manager_name: str
        :param parameters: Parameters supplied to specify which Managed Network deployment status is.
        :type parameters:
         ~azure.mgmt.network.v2022_02_01_preview.models.NetworkManagerDeploymentStatusParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: NetworkManagerDeploymentStatusListResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2022_02_01_preview.models.NetworkManagerDeploymentStatusListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.NetworkManagerDeploymentStatusListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-02-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'NetworkManagerDeploymentStatusParameter')

        request = build_list_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            network_manager_name=network_manager_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('NetworkManagerDeploymentStatusListResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/listDeploymentStatus"}  # type: ignore

