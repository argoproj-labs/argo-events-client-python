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


class V1alpha1CustomTrigger(object):
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
        'cert_file_path': 'str',
        'cert_secret': 'V1SecretKeySelector',
        'parameters': 'list[V1alpha1TriggerParameter]',
        'payload': 'list[V1alpha1TriggerParameter]',
        'secure': 'bool',
        'server_name_override': 'str',
        'server_url': 'str',
        'spec': 'dict(str, str)'
    }

    attribute_map = {
        'cert_file_path': 'certFilePath',
        'cert_secret': 'certSecret',
        'parameters': 'parameters',
        'payload': 'payload',
        'secure': 'secure',
        'server_name_override': 'serverNameOverride',
        'server_url': 'serverURL',
        'spec': 'spec'
    }

    def __init__(self, cert_file_path=None, cert_secret=None, parameters=None, payload=None, secure=None, server_name_override=None, server_url=None, spec=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1CustomTrigger - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cert_file_path = None
        self._cert_secret = None
        self._parameters = None
        self._payload = None
        self._secure = None
        self._server_name_override = None
        self._server_url = None
        self._spec = None
        self.discriminator = None

        if cert_file_path is not None:
            self.cert_file_path = cert_file_path
        if cert_secret is not None:
            self.cert_secret = cert_secret
        if parameters is not None:
            self.parameters = parameters
        self.payload = payload
        self.secure = secure
        if server_name_override is not None:
            self.server_name_override = server_name_override
        self.server_url = server_url
        self.spec = spec

    @property
    def cert_file_path(self):
        """Gets the cert_file_path of this V1alpha1CustomTrigger.  # noqa: E501

        DeprecatedCertFilePath is path to the cert file within sensor for secure connection between sensor and custom trigger gRPC server. DEPRECATED: use CertSecret instead  # noqa: E501

        :return: The cert_file_path of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: str
        """
        return self._cert_file_path

    @cert_file_path.setter
    def cert_file_path(self, cert_file_path):
        """Sets the cert_file_path of this V1alpha1CustomTrigger.

        DeprecatedCertFilePath is path to the cert file within sensor for secure connection between sensor and custom trigger gRPC server. DEPRECATED: use CertSecret instead  # noqa: E501

        :param cert_file_path: The cert_file_path of this V1alpha1CustomTrigger.  # noqa: E501
        :type: str
        """

        self._cert_file_path = cert_file_path

    @property
    def cert_secret(self):
        """Gets the cert_secret of this V1alpha1CustomTrigger.  # noqa: E501


        :return: The cert_secret of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._cert_secret

    @cert_secret.setter
    def cert_secret(self, cert_secret):
        """Sets the cert_secret of this V1alpha1CustomTrigger.


        :param cert_secret: The cert_secret of this V1alpha1CustomTrigger.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._cert_secret = cert_secret

    @property
    def parameters(self):
        """Gets the parameters of this V1alpha1CustomTrigger.  # noqa: E501


        :return: The parameters of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: list[V1alpha1TriggerParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1alpha1CustomTrigger.


        :param parameters: The parameters of this V1alpha1CustomTrigger.  # noqa: E501
        :type: list[V1alpha1TriggerParameter]
        """

        self._parameters = parameters

    @property
    def payload(self):
        """Gets the payload of this V1alpha1CustomTrigger.  # noqa: E501


        :return: The payload of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: list[V1alpha1TriggerParameter]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this V1alpha1CustomTrigger.


        :param payload: The payload of this V1alpha1CustomTrigger.  # noqa: E501
        :type: list[V1alpha1TriggerParameter]
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def secure(self):
        """Gets the secure of this V1alpha1CustomTrigger.  # noqa: E501

        Secure refers to type of the connection between sensor to custom trigger gRPC  # noqa: E501

        :return: The secure of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """Sets the secure of this V1alpha1CustomTrigger.

        Secure refers to type of the connection between sensor to custom trigger gRPC  # noqa: E501

        :param secure: The secure of this V1alpha1CustomTrigger.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and secure is None:  # noqa: E501
            raise ValueError("Invalid value for `secure`, must not be `None`")  # noqa: E501

        self._secure = secure

    @property
    def server_name_override(self):
        """Gets the server_name_override of this V1alpha1CustomTrigger.  # noqa: E501

        ServerNameOverride for the secure connection between sensor and custom trigger gRPC server.  # noqa: E501

        :return: The server_name_override of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: str
        """
        return self._server_name_override

    @server_name_override.setter
    def server_name_override(self, server_name_override):
        """Sets the server_name_override of this V1alpha1CustomTrigger.

        ServerNameOverride for the secure connection between sensor and custom trigger gRPC server.  # noqa: E501

        :param server_name_override: The server_name_override of this V1alpha1CustomTrigger.  # noqa: E501
        :type: str
        """

        self._server_name_override = server_name_override

    @property
    def server_url(self):
        """Gets the server_url of this V1alpha1CustomTrigger.  # noqa: E501

        ServerURL is the url of the gRPC server that executes custom trigger  # noqa: E501

        :return: The server_url of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """Sets the server_url of this V1alpha1CustomTrigger.

        ServerURL is the url of the gRPC server that executes custom trigger  # noqa: E501

        :param server_url: The server_url of this V1alpha1CustomTrigger.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and server_url is None:  # noqa: E501
            raise ValueError("Invalid value for `server_url`, must not be `None`")  # noqa: E501

        self._server_url = server_url

    @property
    def spec(self):
        """Gets the spec of this V1alpha1CustomTrigger.  # noqa: E501

        Spec is the custom trigger resource specification that custom trigger gRPC server knows how to interpret.  # noqa: E501

        :return: The spec of this V1alpha1CustomTrigger.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this V1alpha1CustomTrigger.

        Spec is the custom trigger resource specification that custom trigger gRPC server knows how to interpret.  # noqa: E501

        :param spec: The spec of this V1alpha1CustomTrigger.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and spec is None:  # noqa: E501
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

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
        if not isinstance(other, V1alpha1CustomTrigger):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1CustomTrigger):
            return True

        return self.to_dict() != other.to_dict()
