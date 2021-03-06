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


class V1alpha1PubSubEventSource(object):
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
        'credential_secret': 'V1SecretKeySelector',
        'credentials_file': 'str',
        'delete_subscription_on_finish': 'bool',
        'json_body': 'bool',
        'metadata': 'dict(str, str)',
        'project_id': 'str',
        'subscription_id': 'str',
        'topic': 'str',
        'topic_project_id': 'str'
    }

    attribute_map = {
        'credential_secret': 'credentialSecret',
        'credentials_file': 'credentialsFile',
        'delete_subscription_on_finish': 'deleteSubscriptionOnFinish',
        'json_body': 'jsonBody',
        'metadata': 'metadata',
        'project_id': 'projectID',
        'subscription_id': 'subscriptionID',
        'topic': 'topic',
        'topic_project_id': 'topicProjectID'
    }

    def __init__(self, credential_secret=None, credentials_file=None, delete_subscription_on_finish=None, json_body=None, metadata=None, project_id=None, subscription_id=None, topic=None, topic_project_id=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1PubSubEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._credential_secret = None
        self._credentials_file = None
        self._delete_subscription_on_finish = None
        self._json_body = None
        self._metadata = None
        self._project_id = None
        self._subscription_id = None
        self._topic = None
        self._topic_project_id = None
        self.discriminator = None

        if credential_secret is not None:
            self.credential_secret = credential_secret
        self.credentials_file = credentials_file
        if delete_subscription_on_finish is not None:
            self.delete_subscription_on_finish = delete_subscription_on_finish
        if json_body is not None:
            self.json_body = json_body
        if metadata is not None:
            self.metadata = metadata
        if project_id is not None:
            self.project_id = project_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if topic is not None:
            self.topic = topic
        if topic_project_id is not None:
            self.topic_project_id = topic_project_id

    @property
    def credential_secret(self):
        """Gets the credential_secret of this V1alpha1PubSubEventSource.  # noqa: E501


        :return: The credential_secret of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._credential_secret

    @credential_secret.setter
    def credential_secret(self, credential_secret):
        """Sets the credential_secret of this V1alpha1PubSubEventSource.


        :param credential_secret: The credential_secret of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._credential_secret = credential_secret

    @property
    def credentials_file(self):
        """Gets the credentials_file of this V1alpha1PubSubEventSource.  # noqa: E501

        CredentialsFile is the file that contains credentials to authenticate for GCP Deprecated, use CredentialSecret instead  # noqa: E501

        :return: The credentials_file of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._credentials_file

    @credentials_file.setter
    def credentials_file(self, credentials_file):
        """Sets the credentials_file of this V1alpha1PubSubEventSource.

        CredentialsFile is the file that contains credentials to authenticate for GCP Deprecated, use CredentialSecret instead  # noqa: E501

        :param credentials_file: The credentials_file of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and credentials_file is None:  # noqa: E501
            raise ValueError("Invalid value for `credentials_file`, must not be `None`")  # noqa: E501

        self._credentials_file = credentials_file

    @property
    def delete_subscription_on_finish(self):
        """Gets the delete_subscription_on_finish of this V1alpha1PubSubEventSource.  # noqa: E501

        DeleteSubscriptionOnFinish determines whether to delete the GCP PubSub subscription once the event source is stopped.  # noqa: E501

        :return: The delete_subscription_on_finish of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._delete_subscription_on_finish

    @delete_subscription_on_finish.setter
    def delete_subscription_on_finish(self, delete_subscription_on_finish):
        """Sets the delete_subscription_on_finish of this V1alpha1PubSubEventSource.

        DeleteSubscriptionOnFinish determines whether to delete the GCP PubSub subscription once the event source is stopped.  # noqa: E501

        :param delete_subscription_on_finish: The delete_subscription_on_finish of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: bool
        """

        self._delete_subscription_on_finish = delete_subscription_on_finish

    @property
    def json_body(self):
        """Gets the json_body of this V1alpha1PubSubEventSource.  # noqa: E501

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :return: The json_body of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this V1alpha1PubSubEventSource.

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :param json_body: The json_body of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1PubSubEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1PubSubEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def project_id(self):
        """Gets the project_id of this V1alpha1PubSubEventSource.  # noqa: E501

        ProjectID is GCP project ID for the subscription. Required if you run Argo Events outside of GKE/GCE. (otherwise, the default value is its project)  # noqa: E501

        :return: The project_id of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this V1alpha1PubSubEventSource.

        ProjectID is GCP project ID for the subscription. Required if you run Argo Events outside of GKE/GCE. (otherwise, the default value is its project)  # noqa: E501

        :param project_id: The project_id of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this V1alpha1PubSubEventSource.  # noqa: E501

        SubscriptionID is ID of subscription. Required if you use existing subscription. The default value will be auto generated hash based on this eventsource setting, so the subscription might be recreated every time you update the setting, which has a possibility of event loss.  # noqa: E501

        :return: The subscription_id of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this V1alpha1PubSubEventSource.

        SubscriptionID is ID of subscription. Required if you use existing subscription. The default value will be auto generated hash based on this eventsource setting, so the subscription might be recreated every time you update the setting, which has a possibility of event loss.  # noqa: E501

        :param subscription_id: The subscription_id of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def topic(self):
        """Gets the topic of this V1alpha1PubSubEventSource.  # noqa: E501

        Topic to which the subscription should belongs. Required if you want the eventsource to create a new subscription. If you specify this field along with an existing subscription, it will be verified whether it actually belongs to the specified topic.  # noqa: E501

        :return: The topic of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this V1alpha1PubSubEventSource.

        Topic to which the subscription should belongs. Required if you want the eventsource to create a new subscription. If you specify this field along with an existing subscription, it will be verified whether it actually belongs to the specified topic.  # noqa: E501

        :param topic: The topic of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._topic = topic

    @property
    def topic_project_id(self):
        """Gets the topic_project_id of this V1alpha1PubSubEventSource.  # noqa: E501

        TopicProjectID is GCP project ID for the topic. By default, it is same as ProjectID.  # noqa: E501

        :return: The topic_project_id of this V1alpha1PubSubEventSource.  # noqa: E501
        :rtype: str
        """
        return self._topic_project_id

    @topic_project_id.setter
    def topic_project_id(self, topic_project_id):
        """Sets the topic_project_id of this V1alpha1PubSubEventSource.

        TopicProjectID is GCP project ID for the topic. By default, it is same as ProjectID.  # noqa: E501

        :param topic_project_id: The topic_project_id of this V1alpha1PubSubEventSource.  # noqa: E501
        :type: str
        """

        self._topic_project_id = topic_project_id

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
        if not isinstance(other, V1alpha1PubSubEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1PubSubEventSource):
            return True

        return self.to_dict() != other.to_dict()
