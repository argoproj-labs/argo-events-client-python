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


class V1alpha1EventDependencyFilter(object):
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
        'context': 'V1alpha1EventContext',
        'data': 'list[V1alpha1DataFilter]',
        'time': 'V1alpha1TimeFilter'
    }

    attribute_map = {
        'context': 'context',
        'data': 'data',
        'time': 'time'
    }

    def __init__(self, context=None, data=None, time=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1EventDependencyFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._context = None
        self._data = None
        self._time = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if data is not None:
            self.data = data
        if time is not None:
            self.time = time

    @property
    def context(self):
        """Gets the context of this V1alpha1EventDependencyFilter.  # noqa: E501


        :return: The context of this V1alpha1EventDependencyFilter.  # noqa: E501
        :rtype: V1alpha1EventContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this V1alpha1EventDependencyFilter.


        :param context: The context of this V1alpha1EventDependencyFilter.  # noqa: E501
        :type: V1alpha1EventContext
        """

        self._context = context

    @property
    def data(self):
        """Gets the data of this V1alpha1EventDependencyFilter.  # noqa: E501

        Data filter constraints with escalation  # noqa: E501

        :return: The data of this V1alpha1EventDependencyFilter.  # noqa: E501
        :rtype: list[V1alpha1DataFilter]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this V1alpha1EventDependencyFilter.

        Data filter constraints with escalation  # noqa: E501

        :param data: The data of this V1alpha1EventDependencyFilter.  # noqa: E501
        :type: list[V1alpha1DataFilter]
        """

        self._data = data

    @property
    def time(self):
        """Gets the time of this V1alpha1EventDependencyFilter.  # noqa: E501


        :return: The time of this V1alpha1EventDependencyFilter.  # noqa: E501
        :rtype: V1alpha1TimeFilter
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this V1alpha1EventDependencyFilter.


        :param time: The time of this V1alpha1EventDependencyFilter.  # noqa: E501
        :type: V1alpha1TimeFilter
        """

        self._time = time

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
        if not isinstance(other, V1alpha1EventDependencyFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1EventDependencyFilter):
            return True

        return self.to_dict() != other.to_dict()
