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


class V1alpha1WatchPathConfig(object):
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
        'directory': 'str',
        'path': 'str',
        'path_regexp': 'str'
    }

    attribute_map = {
        'directory': 'directory',
        'path': 'path',
        'path_regexp': 'pathRegexp'
    }

    def __init__(self, directory=None, path=None, path_regexp=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1WatchPathConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._directory = None
        self._path = None
        self._path_regexp = None
        self.discriminator = None

        self.directory = directory
        if path is not None:
            self.path = path
        if path_regexp is not None:
            self.path_regexp = path_regexp

    @property
    def directory(self):
        """Gets the directory of this V1alpha1WatchPathConfig.  # noqa: E501

        Directory to watch for events  # noqa: E501

        :return: The directory of this V1alpha1WatchPathConfig.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this V1alpha1WatchPathConfig.

        Directory to watch for events  # noqa: E501

        :param directory: The directory of this V1alpha1WatchPathConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and directory is None:  # noqa: E501
            raise ValueError("Invalid value for `directory`, must not be `None`")  # noqa: E501

        self._directory = directory

    @property
    def path(self):
        """Gets the path of this V1alpha1WatchPathConfig.  # noqa: E501

        Path is relative path of object to watch with respect to the directory  # noqa: E501

        :return: The path of this V1alpha1WatchPathConfig.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1alpha1WatchPathConfig.

        Path is relative path of object to watch with respect to the directory  # noqa: E501

        :param path: The path of this V1alpha1WatchPathConfig.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def path_regexp(self):
        """Gets the path_regexp of this V1alpha1WatchPathConfig.  # noqa: E501

        PathRegexp is regexp of relative path of object to watch with respect to the directory  # noqa: E501

        :return: The path_regexp of this V1alpha1WatchPathConfig.  # noqa: E501
        :rtype: str
        """
        return self._path_regexp

    @path_regexp.setter
    def path_regexp(self, path_regexp):
        """Sets the path_regexp of this V1alpha1WatchPathConfig.

        PathRegexp is regexp of relative path of object to watch with respect to the directory  # noqa: E501

        :param path_regexp: The path_regexp of this V1alpha1WatchPathConfig.  # noqa: E501
        :type: str
        """

        self._path_regexp = path_regexp

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
        if not isinstance(other, V1alpha1WatchPathConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1WatchPathConfig):
            return True

        return self.to_dict() != other.to_dict()
