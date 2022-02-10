# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AlertProcessingRulesOperations(object):
    """AlertProcessingRulesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.alertsmanagement.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_subscription(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.AlertProcessingRulesList"]
        """List all alert processing rules in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AlertProcessingRulesList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.alertsmanagement.models.AlertProcessingRulesList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertProcessingRulesList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-08-08"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('AlertProcessingRulesList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/actionRules'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.AlertProcessingRulesList"]
        """List all alert processing rules in a resource group.

        :param resource_group_name: Resource group name where the resource is created.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AlertProcessingRulesList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.alertsmanagement.models.AlertProcessingRulesList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertProcessingRulesList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-08-08"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('AlertProcessingRulesList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules'}  # type: ignore

    def get_by_name(
        self,
        resource_group_name,  # type: str
        processing_rule_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.AlertProcessingRule"
        """Get an alert processing rule by name.

        :param resource_group_name: Resource group name where the resource is created.
        :type resource_group_name: str
        :param processing_rule_name: The name of the alert processing rule that needs to be
         fetched.
        :type processing_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertProcessingRule, or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.AlertProcessingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertProcessingRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-08-08"
        accept = "application/json"

        # Construct URL
        url = self.get_by_name.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'alertProcessingRuleName': self._serialize.url("alert_processing_rule_name", processing_rule_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('AlertProcessingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_by_name.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules/{alertProcessingRuleName}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        processing_rule_name,  # type: str
        alert_processing_rule,  # type: "models.AlertProcessingRule"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.AlertProcessingRule"
        """Create or update an alert processing rule.

        :param resource_group_name: Resource group name where the resource is created.
        :type resource_group_name: str
        :param processing_rule_name: The name of the alert processing rule that needs to be
         created/updated.
        :type processing_rule_name: str
        :param alert_processing_rule: Alert processing rule to be created/updated.
        :type alert_processing_rule: ~azure.mgmt.alertsmanagement.models.AlertProcessingRule
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertProcessingRule, or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.AlertProcessingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertProcessingRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-08-08"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'alertProcessingRuleName': self._serialize.url("alert_processing_rule_name", processing_rule_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(alert_processing_rule, 'AlertProcessingRule')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            deserialized = self._deserialize('AlertProcessingRule', pipeline_response)

        if response.status_code == 201:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
            deserialized = self._deserialize('AlertProcessingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules/{alertProcessingRuleName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        alert_processing_rule_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete an alert processing rule.

        :param resource_group_name: Resource group name where the resource is created.
        :type resource_group_name: str
        :param alert_processing_rule_name: The name of the alert processing rule that needs to be
         deleted.
        :type alert_processing_rule_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-08-08"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'alertProcessingRuleName': self._serialize.url("alert_processing_rule_name", alert_processing_rule_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))

        if response.status_code == 204:
            response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules/{alertProcessingRuleName}'}  # type: ignore

    def update(
        self,
        resource_group_name,  # type: str
        alert_processing_rule_name,  # type: str
        alert_processing_rule_patch,  # type: "models.PatchObject"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.AlertProcessingRule"
        """Enable, disable, or update tags for an alert processing rule.

        :param resource_group_name: Resource group name where the resource is created.
        :type resource_group_name: str
        :param alert_processing_rule_name: The name that needs to be updated.
        :type alert_processing_rule_name: str
        :param alert_processing_rule_patch: Parameters supplied to the operation.
        :type alert_processing_rule_patch: ~azure.mgmt.alertsmanagement.models.PatchObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AlertProcessingRule, or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.AlertProcessingRule
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AlertProcessingRule"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-08-08"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'alertProcessingRuleName': self._serialize.url("alert_processing_rule_name", alert_processing_rule_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(alert_processing_rule_patch, 'PatchObject')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('AlertProcessingRule', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AlertsManagement/actionRules/{alertProcessingRuleName}'}  # type: ignore
