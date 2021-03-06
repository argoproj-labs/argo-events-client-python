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


class V1alpha1ArgoWorkflowTrigger(object):
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
        'group': 'str',
        'operation': 'str',
        'parameters': 'list[V1alpha1TriggerParameter]',
        'resource': 'str',
        'source': 'V1alpha1ArtifactLocation',
        'version': 'str'
    }

    attribute_map = {
        'group': 'group',
        'operation': 'operation',
        'parameters': 'parameters',
        'resource': 'resource',
        'source': 'source',
        'version': 'version'
    }

    def __init__(self, group=None, operation=None, parameters=None, resource=None, source=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ArgoWorkflowTrigger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._operation = None
        self._parameters = None
        self._resource = None
        self._source = None
        self._version = None
        self.discriminator = None

        self.group = group
        if operation is not None:
            self.operation = operation
        if parameters is not None:
            self.parameters = parameters
        self.resource = resource
        if source is not None:
            self.source = source
        self.version = version

    @property
    def group(self):
        """Gets the group of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501


        :return: The group of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1alpha1ArgoWorkflowTrigger.


        :param group: The group of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group is None:  # noqa: E501
            raise ValueError("Invalid value for `group`, must not be `None`")  # noqa: E501

        self._group = group

    @property
    def operation(self):
        """Gets the operation of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501

        Operation refers to the type of operation performed on the argo workflow resource. Default value is Submit.  # noqa: E501

        :return: The operation of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this V1alpha1ArgoWorkflowTrigger.

        Operation refers to the type of operation performed on the argo workflow resource. Default value is Submit.  # noqa: E501

        :param operation: The operation of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def parameters(self):
        """Gets the parameters of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501


        :return: The parameters of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :rtype: list[V1alpha1TriggerParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1alpha1ArgoWorkflowTrigger.


        :param parameters: The parameters of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :type: list[V1alpha1TriggerParameter]
        """

        self._parameters = parameters

    @property
    def resource(self):
        """Gets the resource of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501


        :return: The resource of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1alpha1ArgoWorkflowTrigger.


        :param resource: The resource of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def source(self):
        """Gets the source of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501


        :return: The source of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :rtype: V1alpha1ArtifactLocation
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this V1alpha1ArgoWorkflowTrigger.


        :param source: The source of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :type: V1alpha1ArtifactLocation
        """

        self._source = source

    @property
    def version(self):
        """Gets the version of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501


        :return: The version of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1ArgoWorkflowTrigger.


        :param version: The version of this V1alpha1ArgoWorkflowTrigger.  # noqa: E501
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
        if not isinstance(other, V1alpha1ArgoWorkflowTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ArgoWorkflowTrigger):
            return True

        return self.to_dict() != other.to_dict()
