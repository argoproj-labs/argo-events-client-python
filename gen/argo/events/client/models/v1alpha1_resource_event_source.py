# coding: utf-8

"""
    Argo Events

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from argo.events.client.configuration import Configuration


class V1alpha1ResourceEventSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'event_types': 'list[str]',
        'filter': 'V1alpha1ResourceFilter',
        'group': 'str',
        'metadata': 'dict(str, str)',
        'namespace': 'str',
        'resource': 'str',
        'version': 'str'
    }

    attribute_map = {
        'event_types': 'eventTypes',
        'filter': 'filter',
        'group': 'group',
        'metadata': 'metadata',
        'namespace': 'namespace',
        'resource': 'resource',
        'version': 'version'
    }

    def __init__(self, event_types=None, filter=None, group=None, metadata=None, namespace=None, resource=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ResourceEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_types = None
        self._filter = None
        self._group = None
        self._metadata = None
        self._namespace = None
        self._resource = None
        self._version = None
        self.discriminator = None

        self.event_types = event_types
        if filter is not None:
            self.filter = filter
        self.group = group
        if metadata is not None:
            self.metadata = metadata
        self.namespace = namespace
        self.resource = resource
        self.version = version

    @property
    def event_types(self):
        """Gets the event_types of this V1alpha1ResourceEventSource.  # noqa: E501

        EventTypes is the list of event type to watch. Possible values are - ADD, UPDATE and DELETE.  # noqa: E501

        :return: The event_types of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this V1alpha1ResourceEventSource.

        EventTypes is the list of event type to watch. Possible values are - ADD, UPDATE and DELETE.  # noqa: E501

        :param event_types: The event_types of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and event_types is None:  # noqa: E501
            raise ValueError("Invalid value for `event_types`, must not be `None`")  # noqa: E501

        self._event_types = event_types

    @property
    def filter(self):
        """Gets the filter of this V1alpha1ResourceEventSource.  # noqa: E501


        :return: The filter of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: V1alpha1ResourceFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this V1alpha1ResourceEventSource.


        :param filter: The filter of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: V1alpha1ResourceFilter
        """

        self._filter = filter

    @property
    def group(self):
        """Gets the group of this V1alpha1ResourceEventSource.  # noqa: E501


        :return: The group of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1alpha1ResourceEventSource.


        :param group: The group of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1ResourceEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1ResourceEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1ResourceEventSource.  # noqa: E501

        Namespace where resource is deployed  # noqa: E501

        :return: The namespace of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1ResourceEventSource.

        Namespace where resource is deployed  # noqa: E501

        :param namespace: The namespace of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and namespace is None:  # noqa: E501
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def resource(self):
        """Gets the resource of this V1alpha1ResourceEventSource.  # noqa: E501


        :return: The resource of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1alpha1ResourceEventSource.


        :param resource: The resource of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def version(self):
        """Gets the version of this V1alpha1ResourceEventSource.  # noqa: E501


        :return: The version of this V1alpha1ResourceEventSource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1ResourceEventSource.


        :param version: The version of this V1alpha1ResourceEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1ResourceEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ResourceEventSource):
            return True

        return self.to_dict() != other.to_dict()
