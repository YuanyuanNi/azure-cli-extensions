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

class FilesOperations(object):
    """FilesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datamigration.models
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

    def list(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.FileList"]
        """Get files in a project.

        The project resource is a nested resource representing a stored migration project. This method
        returns a list of files owned by a project resource.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FileList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.datamigration.models.FileList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.FileList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-10-30-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'groupName': self._serialize.url("group_name", group_name, 'str'),
                    'serviceName': self._serialize.url("service_name", service_name, 'str'),
                    'projectName': self._serialize.url("project_name", project_name, 'str'),
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
            deserialized = self._deserialize('FileList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ApiError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files'}  # type: ignore

    def get(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        file_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProjectFile"
        """Get file information.

        The files resource is a nested, proxy-only resource representing a file stored under the
        project resource. This method retrieves information about a file.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param file_name: Name of the File.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectFile, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectFile
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProjectFile"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-10-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'fileName': self._serialize.url("file_name", file_name, 'str'),
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
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProjectFile', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}'}  # type: ignore

    def create_or_update(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        file_name,  # type: str
        parameters,  # type: "models.ProjectFile"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProjectFile"
        """Create a file resource.

        The PUT method creates a new file or updates an existing one.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param file_name: Name of the File.
        :type file_name: str
        :param parameters: Information about the file.
        :type parameters: ~azure.mgmt.datamigration.models.ProjectFile
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectFile, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectFile
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProjectFile"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-10-30-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'fileName': self._serialize.url("file_name", file_name, 'str'),
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
        body_content = self._serialize.body(parameters, 'ProjectFile')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ProjectFile', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ProjectFile', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}'}  # type: ignore

    def delete(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        file_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete file.

        This method deletes a file.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param file_name: Name of the File.
        :type file_name: str
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
        api_version = "2021-10-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'fileName': self._serialize.url("file_name", file_name, 'str'),
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
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}'}  # type: ignore

    def update(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        file_name,  # type: str
        parameters,  # type: "models.ProjectFile"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ProjectFile"
        """Update a file.

        This method updates an existing file.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param file_name: Name of the File.
        :type file_name: str
        :param parameters: Information about the file.
        :type parameters: ~azure.mgmt.datamigration.models.ProjectFile
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectFile, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectFile
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ProjectFile"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-10-30-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'fileName': self._serialize.url("file_name", file_name, 'str'),
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
        body_content = self._serialize.body(parameters, 'ProjectFile')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProjectFile', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}'}  # type: ignore

    def read(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        file_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.FileStorageInfo"
        """Request storage information for downloading the file content.

        This method is used for requesting storage information using which contents of the file can be
        downloaded.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param file_name: Name of the File.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileStorageInfo, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.FileStorageInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.FileStorageInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-10-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.read.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'fileName': self._serialize.url("file_name", file_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FileStorageInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    read.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}/read'}  # type: ignore

    def read_write(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        file_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.FileStorageInfo"
        """Request information for reading and writing file content.

        This method is used for requesting information for reading and writing the file content.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param file_name: Name of the File.
        :type file_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FileStorageInfo, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.FileStorageInfo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.FileStorageInfo"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-10-30-preview"
        accept = "application/json"

        # Construct URL
        url = self.read_write.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'fileName': self._serialize.url("file_name", file_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FileStorageInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    read_write.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/files/{fileName}/readwrite'}  # type: ignore
