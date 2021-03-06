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


class V1alpha1FileEventSource(object):
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
        'event_type': 'str',
        'metadata': 'dict(str, str)',
        'polling': 'bool',
        'watch_path_config': 'V1alpha1WatchPathConfig'
    }

    attribute_map = {
        'event_type': 'eventType',
        'metadata': 'metadata',
        'polling': 'polling',
        'watch_path_config': 'watchPathConfig'
    }

    def __init__(self, event_type=None, metadata=None, polling=None, watch_path_config=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1FileEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._metadata = None
        self._polling = None
        self._watch_path_config = None
        self.discriminator = None

        self.event_type = event_type
        if metadata is not None:
            self.metadata = metadata
        if polling is not None:
            self.polling = polling
        self.watch_path_config = watch_path_config

    @property
    def event_type(self):
        """Gets the event_type of this V1alpha1FileEventSource.  # noqa: E501

        Type of file operations to watch Refer https://github.com/fsnotify/fsnotify/blob/master/fsnotify.go for more information  # noqa: E501

        :return: The event_type of this V1alpha1FileEventSource.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this V1alpha1FileEventSource.

        Type of file operations to watch Refer https://github.com/fsnotify/fsnotify/blob/master/fsnotify.go for more information  # noqa: E501

        :param event_type: The event_type of this V1alpha1FileEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1FileEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1FileEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1FileEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1FileEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def polling(self):
        """Gets the polling of this V1alpha1FileEventSource.  # noqa: E501

        Use polling instead of inotify  # noqa: E501

        :return: The polling of this V1alpha1FileEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._polling

    @polling.setter
    def polling(self, polling):
        """Sets the polling of this V1alpha1FileEventSource.

        Use polling instead of inotify  # noqa: E501

        :param polling: The polling of this V1alpha1FileEventSource.  # noqa: E501
        :type: bool
        """

        self._polling = polling

    @property
    def watch_path_config(self):
        """Gets the watch_path_config of this V1alpha1FileEventSource.  # noqa: E501


        :return: The watch_path_config of this V1alpha1FileEventSource.  # noqa: E501
        :rtype: V1alpha1WatchPathConfig
        """
        return self._watch_path_config

    @watch_path_config.setter
    def watch_path_config(self, watch_path_config):
        """Sets the watch_path_config of this V1alpha1FileEventSource.


        :param watch_path_config: The watch_path_config of this V1alpha1FileEventSource.  # noqa: E501
        :type: V1alpha1WatchPathConfig
        """
        if self.local_vars_configuration.client_side_validation and watch_path_config is None:  # noqa: E501
            raise ValueError("Invalid value for `watch_path_config`, must not be `None`")  # noqa: E501

        self._watch_path_config = watch_path_config

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
        if not isinstance(other, V1alpha1FileEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1FileEventSource):
            return True

        return self.to_dict() != other.to_dict()
