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


class V1alpha1NATSBus(object):
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
        'exotic': 'V1alpha1NATSConfig',
        'native': 'V1alpha1NativeStrategy'
    }

    attribute_map = {
        'exotic': 'exotic',
        'native': 'native'
    }

    def __init__(self, exotic=None, native=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1NATSBus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exotic = None
        self._native = None
        self.discriminator = None

        if exotic is not None:
            self.exotic = exotic
        if native is not None:
            self.native = native

    @property
    def exotic(self):
        """Gets the exotic of this V1alpha1NATSBus.  # noqa: E501


        :return: The exotic of this V1alpha1NATSBus.  # noqa: E501
        :rtype: V1alpha1NATSConfig
        """
        return self._exotic

    @exotic.setter
    def exotic(self, exotic):
        """Sets the exotic of this V1alpha1NATSBus.


        :param exotic: The exotic of this V1alpha1NATSBus.  # noqa: E501
        :type: V1alpha1NATSConfig
        """

        self._exotic = exotic

    @property
    def native(self):
        """Gets the native of this V1alpha1NATSBus.  # noqa: E501


        :return: The native of this V1alpha1NATSBus.  # noqa: E501
        :rtype: V1alpha1NativeStrategy
        """
        return self._native

    @native.setter
    def native(self, native):
        """Sets the native of this V1alpha1NATSBus.


        :param native: The native of this V1alpha1NATSBus.  # noqa: E501
        :type: V1alpha1NativeStrategy
        """

        self._native = native

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
        if not isinstance(other, V1alpha1NATSBus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1NATSBus):
            return True

        return self.to_dict() != other.to_dict()
