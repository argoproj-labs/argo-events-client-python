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


class CommonBackoff(object):
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
        'duration': 'int',
        'factor': 'float',
        'jitter': 'float',
        'steps': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'factor': 'factor',
        'jitter': 'jitter',
        'steps': 'steps'
    }

    def __init__(self, duration=None, factor=None, jitter=None, steps=None, local_vars_configuration=None):  # noqa: E501
        """CommonBackoff - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._duration = None
        self._factor = None
        self._jitter = None
        self._steps = None
        self.discriminator = None

        self.duration = duration
        self.factor = factor
        if jitter is not None:
            self.jitter = jitter
        if steps is not None:
            self.steps = steps

    @property
    def duration(self):
        """Gets the duration of this CommonBackoff.  # noqa: E501

        Duration is the duration in nanoseconds  # noqa: E501

        :return: The duration of this CommonBackoff.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this CommonBackoff.

        Duration is the duration in nanoseconds  # noqa: E501

        :param duration: The duration of this CommonBackoff.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def factor(self):
        """Gets the factor of this CommonBackoff.  # noqa: E501

        Duration is multiplied by factor each iteration  # noqa: E501

        :return: The factor of this CommonBackoff.  # noqa: E501
        :rtype: float
        """
        return self._factor

    @factor.setter
    def factor(self, factor):
        """Sets the factor of this CommonBackoff.

        Duration is multiplied by factor each iteration  # noqa: E501

        :param factor: The factor of this CommonBackoff.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and factor is None:  # noqa: E501
            raise ValueError("Invalid value for `factor`, must not be `None`")  # noqa: E501

        self._factor = factor

    @property
    def jitter(self):
        """Gets the jitter of this CommonBackoff.  # noqa: E501

        The amount of jitter applied each iteration  # noqa: E501

        :return: The jitter of this CommonBackoff.  # noqa: E501
        :rtype: float
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        """Sets the jitter of this CommonBackoff.

        The amount of jitter applied each iteration  # noqa: E501

        :param jitter: The jitter of this CommonBackoff.  # noqa: E501
        :type: float
        """

        self._jitter = jitter

    @property
    def steps(self):
        """Gets the steps of this CommonBackoff.  # noqa: E501

        Exit with error after this many steps  # noqa: E501

        :return: The steps of this CommonBackoff.  # noqa: E501
        :rtype: int
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this CommonBackoff.

        Exit with error after this many steps  # noqa: E501

        :param steps: The steps of this CommonBackoff.  # noqa: E501
        :type: int
        """

        self._steps = steps

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
        if not isinstance(other, CommonBackoff):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommonBackoff):
            return True

        return self.to_dict() != other.to_dict()
