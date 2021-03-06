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


class V1alpha1PulsarEventSource(object):
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
        'connection_backoff': 'CommonBackoff',
        'json_body': 'bool',
        'metadata': 'dict(str, str)',
        'tls': 'CommonTLSConfig',
        'tls_allow_insecure_connection': 'bool',
        'tls_trust_certs_secret': 'V1SecretKeySelector',
        'tls_validate_hostname': 'bool',
        'topics': 'list[str]',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'connection_backoff': 'connectionBackoff',
        'json_body': 'jsonBody',
        'metadata': 'metadata',
        'tls': 'tls',
        'tls_allow_insecure_connection': 'tlsAllowInsecureConnection',
        'tls_trust_certs_secret': 'tlsTrustCertsSecret',
        'tls_validate_hostname': 'tlsValidateHostname',
        'topics': 'topics',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, connection_backoff=None, json_body=None, metadata=None, tls=None, tls_allow_insecure_connection=None, tls_trust_certs_secret=None, tls_validate_hostname=None, topics=None, type=None, url=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1PulsarEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_backoff = None
        self._json_body = None
        self._metadata = None
        self._tls = None
        self._tls_allow_insecure_connection = None
        self._tls_trust_certs_secret = None
        self._tls_validate_hostname = None
        self._topics = None
        self._type = None
        self._url = None
        self.discriminator = None

        if connection_backoff is not None:
            self.connection_backoff = connection_backoff
        if json_body is not None:
            self.json_body = json_body
        if metadata is not None:
            self.metadata = metadata
        if tls is not None:
            self.tls = tls
        if tls_allow_insecure_connection is not None:
            self.tls_allow_insecure_connection = tls_allow_insecure_connection
        if tls_trust_certs_secret is not None:
            self.tls_trust_certs_secret = tls_trust_certs_secret
        if tls_validate_hostname is not None:
            self.tls_validate_hostname = tls_validate_hostname
        self.topics = topics
        if type is not None:
            self.type = type
        self.url = url

    @property
    def connection_backoff(self):
        """Gets the connection_backoff of this V1alpha1PulsarEventSource.  # noqa: E501


        :return: The connection_backoff of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: CommonBackoff
        """
        return self._connection_backoff

    @connection_backoff.setter
    def connection_backoff(self, connection_backoff):
        """Sets the connection_backoff of this V1alpha1PulsarEventSource.


        :param connection_backoff: The connection_backoff of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: CommonBackoff
        """

        self._connection_backoff = connection_backoff

    @property
    def json_body(self):
        """Gets the json_body of this V1alpha1PulsarEventSource.  # noqa: E501

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :return: The json_body of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this V1alpha1PulsarEventSource.

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :param json_body: The json_body of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1PulsarEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1PulsarEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def tls(self):
        """Gets the tls of this V1alpha1PulsarEventSource.  # noqa: E501


        :return: The tls of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: CommonTLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this V1alpha1PulsarEventSource.


        :param tls: The tls of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: CommonTLSConfig
        """

        self._tls = tls

    @property
    def tls_allow_insecure_connection(self):
        """Gets the tls_allow_insecure_connection of this V1alpha1PulsarEventSource.  # noqa: E501

        Whether the Pulsar client accept untrusted TLS certificate from broker.  # noqa: E501

        :return: The tls_allow_insecure_connection of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._tls_allow_insecure_connection

    @tls_allow_insecure_connection.setter
    def tls_allow_insecure_connection(self, tls_allow_insecure_connection):
        """Sets the tls_allow_insecure_connection of this V1alpha1PulsarEventSource.

        Whether the Pulsar client accept untrusted TLS certificate from broker.  # noqa: E501

        :param tls_allow_insecure_connection: The tls_allow_insecure_connection of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: bool
        """

        self._tls_allow_insecure_connection = tls_allow_insecure_connection

    @property
    def tls_trust_certs_secret(self):
        """Gets the tls_trust_certs_secret of this V1alpha1PulsarEventSource.  # noqa: E501


        :return: The tls_trust_certs_secret of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._tls_trust_certs_secret

    @tls_trust_certs_secret.setter
    def tls_trust_certs_secret(self, tls_trust_certs_secret):
        """Sets the tls_trust_certs_secret of this V1alpha1PulsarEventSource.


        :param tls_trust_certs_secret: The tls_trust_certs_secret of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._tls_trust_certs_secret = tls_trust_certs_secret

    @property
    def tls_validate_hostname(self):
        """Gets the tls_validate_hostname of this V1alpha1PulsarEventSource.  # noqa: E501

        Whether the Pulsar client verify the validity of the host name from broker.  # noqa: E501

        :return: The tls_validate_hostname of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._tls_validate_hostname

    @tls_validate_hostname.setter
    def tls_validate_hostname(self, tls_validate_hostname):
        """Sets the tls_validate_hostname of this V1alpha1PulsarEventSource.

        Whether the Pulsar client verify the validity of the host name from broker.  # noqa: E501

        :param tls_validate_hostname: The tls_validate_hostname of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: bool
        """

        self._tls_validate_hostname = tls_validate_hostname

    @property
    def topics(self):
        """Gets the topics of this V1alpha1PulsarEventSource.  # noqa: E501

        Name of the topics to subscribe to.  # noqa: E501

        :return: The topics of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this V1alpha1PulsarEventSource.

        Name of the topics to subscribe to.  # noqa: E501

        :param topics: The topics of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and topics is None:  # noqa: E501
            raise ValueError("Invalid value for `topics`, must not be `None`")  # noqa: E501

        self._topics = topics

    @property
    def type(self):
        """Gets the type of this V1alpha1PulsarEventSource.  # noqa: E501

        Type of the subscription. Only \"exclusive\" and \"shared\" is supported. Defaults to exclusive.  # noqa: E501

        :return: The type of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1PulsarEventSource.

        Type of the subscription. Only \"exclusive\" and \"shared\" is supported. Defaults to exclusive.  # noqa: E501

        :param type: The type of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this V1alpha1PulsarEventSource.  # noqa: E501

        Configure the service URL for the Pulsar service.  # noqa: E501

        :return: The url of this V1alpha1PulsarEventSource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha1PulsarEventSource.

        Configure the service URL for the Pulsar service.  # noqa: E501

        :param url: The url of this V1alpha1PulsarEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if not isinstance(other, V1alpha1PulsarEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1PulsarEventSource):
            return True

        return self.to_dict() != other.to_dict()
