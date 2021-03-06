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


class V1alpha1KafkaConsumerGroup(object):
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
        'group_name': 'str',
        'oldest': 'bool',
        'rebalance_strategy': 'str'
    }

    attribute_map = {
        'group_name': 'groupName',
        'oldest': 'oldest',
        'rebalance_strategy': 'rebalanceStrategy'
    }

    def __init__(self, group_name=None, oldest=None, rebalance_strategy=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1KafkaConsumerGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_name = None
        self._oldest = None
        self._rebalance_strategy = None
        self.discriminator = None

        self.group_name = group_name
        if oldest is not None:
            self.oldest = oldest
        if rebalance_strategy is not None:
            self.rebalance_strategy = rebalance_strategy

    @property
    def group_name(self):
        """Gets the group_name of this V1alpha1KafkaConsumerGroup.  # noqa: E501

        The name for the consumer group to use  # noqa: E501

        :return: The group_name of this V1alpha1KafkaConsumerGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this V1alpha1KafkaConsumerGroup.

        The name for the consumer group to use  # noqa: E501

        :param group_name: The group_name of this V1alpha1KafkaConsumerGroup.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def oldest(self):
        """Gets the oldest of this V1alpha1KafkaConsumerGroup.  # noqa: E501

        When starting up a new group do we want to start from the oldest event (true) or the newest event (false), defaults to false  # noqa: E501

        :return: The oldest of this V1alpha1KafkaConsumerGroup.  # noqa: E501
        :rtype: bool
        """
        return self._oldest

    @oldest.setter
    def oldest(self, oldest):
        """Sets the oldest of this V1alpha1KafkaConsumerGroup.

        When starting up a new group do we want to start from the oldest event (true) or the newest event (false), defaults to false  # noqa: E501

        :param oldest: The oldest of this V1alpha1KafkaConsumerGroup.  # noqa: E501
        :type: bool
        """

        self._oldest = oldest

    @property
    def rebalance_strategy(self):
        """Gets the rebalance_strategy of this V1alpha1KafkaConsumerGroup.  # noqa: E501

        Rebalance strategy can be one of: sticky, roundrobin, range. Range is the default.  # noqa: E501

        :return: The rebalance_strategy of this V1alpha1KafkaConsumerGroup.  # noqa: E501
        :rtype: str
        """
        return self._rebalance_strategy

    @rebalance_strategy.setter
    def rebalance_strategy(self, rebalance_strategy):
        """Sets the rebalance_strategy of this V1alpha1KafkaConsumerGroup.

        Rebalance strategy can be one of: sticky, roundrobin, range. Range is the default.  # noqa: E501

        :param rebalance_strategy: The rebalance_strategy of this V1alpha1KafkaConsumerGroup.  # noqa: E501
        :type: str
        """

        self._rebalance_strategy = rebalance_strategy

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
        if not isinstance(other, V1alpha1KafkaConsumerGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1KafkaConsumerGroup):
            return True

        return self.to_dict() != other.to_dict()
