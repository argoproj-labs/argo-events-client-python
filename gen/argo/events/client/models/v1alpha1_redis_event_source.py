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


class V1alpha1RedisEventSource(object):
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
        'channels': 'list[str]',
        'db': 'int',
        'host_address': 'str',
        'metadata': 'dict(str, str)',
        'namespace': 'str',
        'password': 'V1SecretKeySelector',
        'tls': 'CommonTLSConfig'
    }

    attribute_map = {
        'channels': 'channels',
        'db': 'db',
        'host_address': 'hostAddress',
        'metadata': 'metadata',
        'namespace': 'namespace',
        'password': 'password',
        'tls': 'tls'
    }

    def __init__(self, channels=None, db=None, host_address=None, metadata=None, namespace=None, password=None, tls=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1RedisEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._channels = None
        self._db = None
        self._host_address = None
        self._metadata = None
        self._namespace = None
        self._password = None
        self._tls = None
        self.discriminator = None

        self.channels = channels
        if db is not None:
            self.db = db
        self.host_address = host_address
        if metadata is not None:
            self.metadata = metadata
        if namespace is not None:
            self.namespace = namespace
        if password is not None:
            self.password = password
        if tls is not None:
            self.tls = tls

    @property
    def channels(self):
        """Gets the channels of this V1alpha1RedisEventSource.  # noqa: E501


        :return: The channels of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this V1alpha1RedisEventSource.


        :param channels: The channels of this V1alpha1RedisEventSource.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and channels is None:  # noqa: E501
            raise ValueError("Invalid value for `channels`, must not be `None`")  # noqa: E501

        self._channels = channels

    @property
    def db(self):
        """Gets the db of this V1alpha1RedisEventSource.  # noqa: E501

        DB to use. If not specified, default DB 0 will be used.  # noqa: E501

        :return: The db of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: int
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this V1alpha1RedisEventSource.

        DB to use. If not specified, default DB 0 will be used.  # noqa: E501

        :param db: The db of this V1alpha1RedisEventSource.  # noqa: E501
        :type: int
        """

        self._db = db

    @property
    def host_address(self):
        """Gets the host_address of this V1alpha1RedisEventSource.  # noqa: E501

        HostAddress refers to the address of the Redis host/server  # noqa: E501

        :return: The host_address of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: str
        """
        return self._host_address

    @host_address.setter
    def host_address(self, host_address):
        """Sets the host_address of this V1alpha1RedisEventSource.

        HostAddress refers to the address of the Redis host/server  # noqa: E501

        :param host_address: The host_address of this V1alpha1RedisEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host_address is None:  # noqa: E501
            raise ValueError("Invalid value for `host_address`, must not be `None`")  # noqa: E501

        self._host_address = host_address

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1RedisEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1RedisEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1RedisEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1RedisEventSource.  # noqa: E501

        Namespace to use to retrieve the password from. It should only be specified if password is declared  # noqa: E501

        :return: The namespace of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1RedisEventSource.

        Namespace to use to retrieve the password from. It should only be specified if password is declared  # noqa: E501

        :param namespace: The namespace of this V1alpha1RedisEventSource.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def password(self):
        """Gets the password of this V1alpha1RedisEventSource.  # noqa: E501


        :return: The password of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this V1alpha1RedisEventSource.


        :param password: The password of this V1alpha1RedisEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._password = password

    @property
    def tls(self):
        """Gets the tls of this V1alpha1RedisEventSource.  # noqa: E501


        :return: The tls of this V1alpha1RedisEventSource.  # noqa: E501
        :rtype: CommonTLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this V1alpha1RedisEventSource.


        :param tls: The tls of this V1alpha1RedisEventSource.  # noqa: E501
        :type: CommonTLSConfig
        """

        self._tls = tls

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
        if not isinstance(other, V1alpha1RedisEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1RedisEventSource):
            return True

        return self.to_dict() != other.to_dict()
