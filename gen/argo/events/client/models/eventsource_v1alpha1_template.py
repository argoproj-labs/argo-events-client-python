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


class EventsourceV1alpha1Template(object):
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
        'affinity': 'V1Affinity',
        'container': 'V1Container',
        'metadata': 'CommonMetadata',
        'node_selector': 'dict(str, str)',
        'security_context': 'V1PodSecurityContext',
        'service_account_name': 'str',
        'tolerations': 'list[V1Toleration]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'affinity': 'affinity',
        'container': 'container',
        'metadata': 'metadata',
        'node_selector': 'nodeSelector',
        'security_context': 'securityContext',
        'service_account_name': 'serviceAccountName',
        'tolerations': 'tolerations',
        'volumes': 'volumes'
    }

    def __init__(self, affinity=None, container=None, metadata=None, node_selector=None, security_context=None, service_account_name=None, tolerations=None, volumes=None, local_vars_configuration=None):  # noqa: E501
        """EventsourceV1alpha1Template - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._affinity = None
        self._container = None
        self._metadata = None
        self._node_selector = None
        self._security_context = None
        self._service_account_name = None
        self._tolerations = None
        self._volumes = None
        self.discriminator = None

        if affinity is not None:
            self.affinity = affinity
        if container is not None:
            self.container = container
        if metadata is not None:
            self.metadata = metadata
        if node_selector is not None:
            self.node_selector = node_selector
        if security_context is not None:
            self.security_context = security_context
        if service_account_name is not None:
            self.service_account_name = service_account_name
        if tolerations is not None:
            self.tolerations = tolerations
        if volumes is not None:
            self.volumes = volumes

    @property
    def affinity(self):
        """Gets the affinity of this EventsourceV1alpha1Template.  # noqa: E501


        :return: The affinity of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """Sets the affinity of this EventsourceV1alpha1Template.


        :param affinity: The affinity of this EventsourceV1alpha1Template.  # noqa: E501
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def container(self):
        """Gets the container of this EventsourceV1alpha1Template.  # noqa: E501


        :return: The container of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: V1Container
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this EventsourceV1alpha1Template.


        :param container: The container of this EventsourceV1alpha1Template.  # noqa: E501
        :type: V1Container
        """

        self._container = container

    @property
    def metadata(self):
        """Gets the metadata of this EventsourceV1alpha1Template.  # noqa: E501


        :return: The metadata of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: CommonMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this EventsourceV1alpha1Template.


        :param metadata: The metadata of this EventsourceV1alpha1Template.  # noqa: E501
        :type: CommonMetadata
        """

        self._metadata = metadata

    @property
    def node_selector(self):
        """Gets the node_selector of this EventsourceV1alpha1Template.  # noqa: E501

        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/  # noqa: E501

        :return: The node_selector of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """Sets the node_selector of this EventsourceV1alpha1Template.

        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/  # noqa: E501

        :param node_selector: The node_selector of this EventsourceV1alpha1Template.  # noqa: E501
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def security_context(self):
        """Gets the security_context of this EventsourceV1alpha1Template.  # noqa: E501


        :return: The security_context of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: V1PodSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this EventsourceV1alpha1Template.


        :param security_context: The security_context of this EventsourceV1alpha1Template.  # noqa: E501
        :type: V1PodSecurityContext
        """

        self._security_context = security_context

    @property
    def service_account_name(self):
        """Gets the service_account_name of this EventsourceV1alpha1Template.  # noqa: E501

        ServiceAccountName is the name of the ServiceAccount to use to run event source pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/  # noqa: E501

        :return: The service_account_name of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this EventsourceV1alpha1Template.

        ServiceAccountName is the name of the ServiceAccount to use to run event source pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/  # noqa: E501

        :param service_account_name: The service_account_name of this EventsourceV1alpha1Template.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def tolerations(self):
        """Gets the tolerations of this EventsourceV1alpha1Template.  # noqa: E501

        If specified, the pod's tolerations.  # noqa: E501

        :return: The tolerations of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """Sets the tolerations of this EventsourceV1alpha1Template.

        If specified, the pod's tolerations.  # noqa: E501

        :param tolerations: The tolerations of this EventsourceV1alpha1Template.  # noqa: E501
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def volumes(self):
        """Gets the volumes of this EventsourceV1alpha1Template.  # noqa: E501

        Volumes is a list of volumes that can be mounted by containers in an eventsource.  # noqa: E501

        :return: The volumes of this EventsourceV1alpha1Template.  # noqa: E501
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this EventsourceV1alpha1Template.

        Volumes is a list of volumes that can be mounted by containers in an eventsource.  # noqa: E501

        :param volumes: The volumes of this EventsourceV1alpha1Template.  # noqa: E501
        :type: list[V1Volume]
        """

        self._volumes = volumes

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
        if not isinstance(other, EventsourceV1alpha1Template):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventsourceV1alpha1Template):
            return True

        return self.to_dict() != other.to_dict()
