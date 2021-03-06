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


class V1alpha1KafkaEventSource(object):
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
        'consumer_group': 'V1alpha1KafkaConsumerGroup',
        'json_body': 'bool',
        'limit_events_per_second': 'int',
        'metadata': 'dict(str, str)',
        'partition': 'str',
        'tls': 'CommonTLSConfig',
        'topic': 'str',
        'url': 'str',
        'version': 'str'
    }

    attribute_map = {
        'connection_backoff': 'connectionBackoff',
        'consumer_group': 'consumerGroup',
        'json_body': 'jsonBody',
        'limit_events_per_second': 'limitEventsPerSecond',
        'metadata': 'metadata',
        'partition': 'partition',
        'tls': 'tls',
        'topic': 'topic',
        'url': 'url',
        'version': 'version'
    }

    def __init__(self, connection_backoff=None, consumer_group=None, json_body=None, limit_events_per_second=None, metadata=None, partition=None, tls=None, topic=None, url=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1KafkaEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_backoff = None
        self._consumer_group = None
        self._json_body = None
        self._limit_events_per_second = None
        self._metadata = None
        self._partition = None
        self._tls = None
        self._topic = None
        self._url = None
        self._version = None
        self.discriminator = None

        if connection_backoff is not None:
            self.connection_backoff = connection_backoff
        if consumer_group is not None:
            self.consumer_group = consumer_group
        if json_body is not None:
            self.json_body = json_body
        if limit_events_per_second is not None:
            self.limit_events_per_second = limit_events_per_second
        if metadata is not None:
            self.metadata = metadata
        self.partition = partition
        if tls is not None:
            self.tls = tls
        self.topic = topic
        self.url = url
        if version is not None:
            self.version = version

    @property
    def connection_backoff(self):
        """Gets the connection_backoff of this V1alpha1KafkaEventSource.  # noqa: E501


        :return: The connection_backoff of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: CommonBackoff
        """
        return self._connection_backoff

    @connection_backoff.setter
    def connection_backoff(self, connection_backoff):
        """Sets the connection_backoff of this V1alpha1KafkaEventSource.


        :param connection_backoff: The connection_backoff of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: CommonBackoff
        """

        self._connection_backoff = connection_backoff

    @property
    def consumer_group(self):
        """Gets the consumer_group of this V1alpha1KafkaEventSource.  # noqa: E501


        :return: The consumer_group of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: V1alpha1KafkaConsumerGroup
        """
        return self._consumer_group

    @consumer_group.setter
    def consumer_group(self, consumer_group):
        """Sets the consumer_group of this V1alpha1KafkaEventSource.


        :param consumer_group: The consumer_group of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: V1alpha1KafkaConsumerGroup
        """

        self._consumer_group = consumer_group

    @property
    def json_body(self):
        """Gets the json_body of this V1alpha1KafkaEventSource.  # noqa: E501

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :return: The json_body of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this V1alpha1KafkaEventSource.

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :param json_body: The json_body of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def limit_events_per_second(self):
        """Gets the limit_events_per_second of this V1alpha1KafkaEventSource.  # noqa: E501

        Sets a limit on how many events get read from kafka per second.  # noqa: E501

        :return: The limit_events_per_second of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: int
        """
        return self._limit_events_per_second

    @limit_events_per_second.setter
    def limit_events_per_second(self, limit_events_per_second):
        """Sets the limit_events_per_second of this V1alpha1KafkaEventSource.

        Sets a limit on how many events get read from kafka per second.  # noqa: E501

        :param limit_events_per_second: The limit_events_per_second of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: int
        """

        self._limit_events_per_second = limit_events_per_second

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1KafkaEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1KafkaEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def partition(self):
        """Gets the partition of this V1alpha1KafkaEventSource.  # noqa: E501

        Partition name  # noqa: E501

        :return: The partition of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this V1alpha1KafkaEventSource.

        Partition name  # noqa: E501

        :param partition: The partition of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and partition is None:  # noqa: E501
            raise ValueError("Invalid value for `partition`, must not be `None`")  # noqa: E501

        self._partition = partition

    @property
    def tls(self):
        """Gets the tls of this V1alpha1KafkaEventSource.  # noqa: E501


        :return: The tls of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: CommonTLSConfig
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this V1alpha1KafkaEventSource.


        :param tls: The tls of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: CommonTLSConfig
        """

        self._tls = tls

    @property
    def topic(self):
        """Gets the topic of this V1alpha1KafkaEventSource.  # noqa: E501

        Topic name  # noqa: E501

        :return: The topic of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this V1alpha1KafkaEventSource.

        Topic name  # noqa: E501

        :param topic: The topic of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and topic is None:  # noqa: E501
            raise ValueError("Invalid value for `topic`, must not be `None`")  # noqa: E501

        self._topic = topic

    @property
    def url(self):
        """Gets the url of this V1alpha1KafkaEventSource.  # noqa: E501

        URL to kafka cluster, multiple URLs separated by comma  # noqa: E501

        :return: The url of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha1KafkaEventSource.

        URL to kafka cluster, multiple URLs separated by comma  # noqa: E501

        :param url: The url of this V1alpha1KafkaEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def version(self):
        """Gets the version of this V1alpha1KafkaEventSource.  # noqa: E501

        Specify what kafka version is being connected to enables certain features in sarama, defaults to 1.0.0  # noqa: E501

        :return: The version of this V1alpha1KafkaEventSource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1KafkaEventSource.

        Specify what kafka version is being connected to enables certain features in sarama, defaults to 1.0.0  # noqa: E501

        :param version: The version of this V1alpha1KafkaEventSource.  # noqa: E501
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
        if not isinstance(other, V1alpha1KafkaEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1KafkaEventSource):
            return True

        return self.to_dict() != other.to_dict()
