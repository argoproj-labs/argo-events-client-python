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


class V1alpha1NATSConfig(object):
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
        'access_secret': 'V1SecretKeySelector',
        'auth': 'str',
        'cluster_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'access_secret': 'accessSecret',
        'auth': 'auth',
        'cluster_id': 'clusterID',
        'url': 'url'
    }

    def __init__(self, access_secret=None, auth=None, cluster_id=None, url=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1NATSConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_secret = None
        self._auth = None
        self._cluster_id = None
        self._url = None
        self.discriminator = None

        if access_secret is not None:
            self.access_secret = access_secret
        if auth is not None:
            self.auth = auth
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if url is not None:
            self.url = url

    @property
    def access_secret(self):
        """Gets the access_secret of this V1alpha1NATSConfig.  # noqa: E501


        :return: The access_secret of this V1alpha1NATSConfig.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._access_secret

    @access_secret.setter
    def access_secret(self, access_secret):
        """Sets the access_secret of this V1alpha1NATSConfig.


        :param access_secret: The access_secret of this V1alpha1NATSConfig.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._access_secret = access_secret

    @property
    def auth(self):
        """Gets the auth of this V1alpha1NATSConfig.  # noqa: E501

        Auth strategy, default to AuthStrategyNone  # noqa: E501

        :return: The auth of this V1alpha1NATSConfig.  # noqa: E501
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this V1alpha1NATSConfig.

        Auth strategy, default to AuthStrategyNone  # noqa: E501

        :param auth: The auth of this V1alpha1NATSConfig.  # noqa: E501
        :type: str
        """

        self._auth = auth

    @property
    def cluster_id(self):
        """Gets the cluster_id of this V1alpha1NATSConfig.  # noqa: E501

        Cluster ID for nats streaming  # noqa: E501

        :return: The cluster_id of this V1alpha1NATSConfig.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this V1alpha1NATSConfig.

        Cluster ID for nats streaming  # noqa: E501

        :param cluster_id: The cluster_id of this V1alpha1NATSConfig.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def url(self):
        """Gets the url of this V1alpha1NATSConfig.  # noqa: E501

        NATS streaming url  # noqa: E501

        :return: The url of this V1alpha1NATSConfig.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this V1alpha1NATSConfig.

        NATS streaming url  # noqa: E501

        :param url: The url of this V1alpha1NATSConfig.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, V1alpha1NATSConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1NATSConfig):
            return True

        return self.to_dict() != other.to_dict()
