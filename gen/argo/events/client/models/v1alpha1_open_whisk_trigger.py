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


class V1alpha1OpenWhiskTrigger(object):
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
        'action_name': 'str',
        'auth_token': 'V1SecretKeySelector',
        'host': 'str',
        'namespace': 'str',
        'parameters': 'list[V1alpha1TriggerParameter]',
        'payload': 'list[V1alpha1TriggerParameter]',
        'version': 'str'
    }

    attribute_map = {
        'action_name': 'actionName',
        'auth_token': 'authToken',
        'host': 'host',
        'namespace': 'namespace',
        'parameters': 'parameters',
        'payload': 'payload',
        'version': 'version'
    }

    def __init__(self, action_name=None, auth_token=None, host=None, namespace=None, parameters=None, payload=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1OpenWhiskTrigger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action_name = None
        self._auth_token = None
        self._host = None
        self._namespace = None
        self._parameters = None
        self._payload = None
        self._version = None
        self.discriminator = None

        self.action_name = action_name
        if auth_token is not None:
            self.auth_token = auth_token
        self.host = host
        if namespace is not None:
            self.namespace = namespace
        if parameters is not None:
            self.parameters = parameters
        self.payload = payload
        if version is not None:
            self.version = version

    @property
    def action_name(self):
        """Gets the action_name of this V1alpha1OpenWhiskTrigger.  # noqa: E501

        Name of the action/function.  # noqa: E501

        :return: The action_name of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this V1alpha1OpenWhiskTrigger.

        Name of the action/function.  # noqa: E501

        :param action_name: The action_name of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action_name is None:  # noqa: E501
            raise ValueError("Invalid value for `action_name`, must not be `None`")  # noqa: E501

        self._action_name = action_name

    @property
    def auth_token(self):
        """Gets the auth_token of this V1alpha1OpenWhiskTrigger.  # noqa: E501


        :return: The auth_token of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this V1alpha1OpenWhiskTrigger.


        :param auth_token: The auth_token of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._auth_token = auth_token

    @property
    def host(self):
        """Gets the host of this V1alpha1OpenWhiskTrigger.  # noqa: E501

        Host URL of the OpenWhisk.  # noqa: E501

        :return: The host of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this V1alpha1OpenWhiskTrigger.

        Host URL of the OpenWhisk.  # noqa: E501

        :param host: The host of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1OpenWhiskTrigger.  # noqa: E501

        Namespace for the action. Defaults to \"_\".  # noqa: E501

        :return: The namespace of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1OpenWhiskTrigger.

        Namespace for the action. Defaults to \"_\".  # noqa: E501

        :param namespace: The namespace of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def parameters(self):
        """Gets the parameters of this V1alpha1OpenWhiskTrigger.  # noqa: E501


        :return: The parameters of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: list[V1alpha1TriggerParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1alpha1OpenWhiskTrigger.


        :param parameters: The parameters of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: list[V1alpha1TriggerParameter]
        """

        self._parameters = parameters

    @property
    def payload(self):
        """Gets the payload of this V1alpha1OpenWhiskTrigger.  # noqa: E501


        :return: The payload of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: list[V1alpha1TriggerParameter]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this V1alpha1OpenWhiskTrigger.


        :param payload: The payload of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: list[V1alpha1TriggerParameter]
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def version(self):
        """Gets the version of this V1alpha1OpenWhiskTrigger.  # noqa: E501

        Version for the API. Defaults to v1.  # noqa: E501

        :return: The version of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1OpenWhiskTrigger.

        Version for the API. Defaults to v1.  # noqa: E501

        :param version: The version of this V1alpha1OpenWhiskTrigger.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, V1alpha1OpenWhiskTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1OpenWhiskTrigger):
            return True

        return self.to_dict() != other.to_dict()
