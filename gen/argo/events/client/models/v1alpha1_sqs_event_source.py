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


class V1alpha1SQSEventSource(object):
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
        'access_key': 'V1SecretKeySelector',
        'json_body': 'bool',
        'metadata': 'dict(str, str)',
        'queue': 'str',
        'queue_account_id': 'str',
        'region': 'str',
        'role_arn': 'str',
        'secret_key': 'V1SecretKeySelector',
        'wait_time_seconds': 'int'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'json_body': 'jsonBody',
        'metadata': 'metadata',
        'queue': 'queue',
        'queue_account_id': 'queueAccountId',
        'region': 'region',
        'role_arn': 'roleARN',
        'secret_key': 'secretKey',
        'wait_time_seconds': 'waitTimeSeconds'
    }

    def __init__(self, access_key=None, json_body=None, metadata=None, queue=None, queue_account_id=None, region=None, role_arn=None, secret_key=None, wait_time_seconds=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1SQSEventSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._json_body = None
        self._metadata = None
        self._queue = None
        self._queue_account_id = None
        self._region = None
        self._role_arn = None
        self._secret_key = None
        self._wait_time_seconds = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if json_body is not None:
            self.json_body = json_body
        if metadata is not None:
            self.metadata = metadata
        self.queue = queue
        if queue_account_id is not None:
            self.queue_account_id = queue_account_id
        self.region = region
        if role_arn is not None:
            self.role_arn = role_arn
        if secret_key is not None:
            self.secret_key = secret_key
        self.wait_time_seconds = wait_time_seconds

    @property
    def access_key(self):
        """Gets the access_key of this V1alpha1SQSEventSource.  # noqa: E501


        :return: The access_key of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this V1alpha1SQSEventSource.


        :param access_key: The access_key of this V1alpha1SQSEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._access_key = access_key

    @property
    def json_body(self):
        """Gets the json_body of this V1alpha1SQSEventSource.  # noqa: E501

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :return: The json_body of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._json_body

    @json_body.setter
    def json_body(self, json_body):
        """Sets the json_body of this V1alpha1SQSEventSource.

        JSONBody specifies that all event body payload coming from this source will be JSON  # noqa: E501

        :param json_body: The json_body of this V1alpha1SQSEventSource.  # noqa: E501
        :type: bool
        """

        self._json_body = json_body

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1SQSEventSource.  # noqa: E501

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :return: The metadata of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1SQSEventSource.

        Metadata holds the user defined metadata which will passed along the event payload.  # noqa: E501

        :param metadata: The metadata of this V1alpha1SQSEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._metadata = metadata

    @property
    def queue(self):
        """Gets the queue of this V1alpha1SQSEventSource.  # noqa: E501

        Queue is AWS SQS queue to listen to for messages  # noqa: E501

        :return: The queue of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this V1alpha1SQSEventSource.

        Queue is AWS SQS queue to listen to for messages  # noqa: E501

        :param queue: The queue of this V1alpha1SQSEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and queue is None:  # noqa: E501
            raise ValueError("Invalid value for `queue`, must not be `None`")  # noqa: E501

        self._queue = queue

    @property
    def queue_account_id(self):
        """Gets the queue_account_id of this V1alpha1SQSEventSource.  # noqa: E501

        QueueAccountID is the ID of the account that created the queue to monitor  # noqa: E501

        :return: The queue_account_id of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._queue_account_id

    @queue_account_id.setter
    def queue_account_id(self, queue_account_id):
        """Sets the queue_account_id of this V1alpha1SQSEventSource.

        QueueAccountID is the ID of the account that created the queue to monitor  # noqa: E501

        :param queue_account_id: The queue_account_id of this V1alpha1SQSEventSource.  # noqa: E501
        :type: str
        """

        self._queue_account_id = queue_account_id

    @property
    def region(self):
        """Gets the region of this V1alpha1SQSEventSource.  # noqa: E501

        Region is AWS region  # noqa: E501

        :return: The region of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this V1alpha1SQSEventSource.

        Region is AWS region  # noqa: E501

        :param region: The region of this V1alpha1SQSEventSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def role_arn(self):
        """Gets the role_arn of this V1alpha1SQSEventSource.  # noqa: E501

        RoleARN is the Amazon Resource Name (ARN) of the role to assume.  # noqa: E501

        :return: The role_arn of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: str
        """
        return self._role_arn

    @role_arn.setter
    def role_arn(self, role_arn):
        """Sets the role_arn of this V1alpha1SQSEventSource.

        RoleARN is the Amazon Resource Name (ARN) of the role to assume.  # noqa: E501

        :param role_arn: The role_arn of this V1alpha1SQSEventSource.  # noqa: E501
        :type: str
        """

        self._role_arn = role_arn

    @property
    def secret_key(self):
        """Gets the secret_key of this V1alpha1SQSEventSource.  # noqa: E501


        :return: The secret_key of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: V1SecretKeySelector
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this V1alpha1SQSEventSource.


        :param secret_key: The secret_key of this V1alpha1SQSEventSource.  # noqa: E501
        :type: V1SecretKeySelector
        """

        self._secret_key = secret_key

    @property
    def wait_time_seconds(self):
        """Gets the wait_time_seconds of this V1alpha1SQSEventSource.  # noqa: E501

        WaitTimeSeconds is The duration (in seconds) for which the call waits for a message to arrive in the queue before returning.  # noqa: E501

        :return: The wait_time_seconds of this V1alpha1SQSEventSource.  # noqa: E501
        :rtype: int
        """
        return self._wait_time_seconds

    @wait_time_seconds.setter
    def wait_time_seconds(self, wait_time_seconds):
        """Sets the wait_time_seconds of this V1alpha1SQSEventSource.

        WaitTimeSeconds is The duration (in seconds) for which the call waits for a message to arrive in the queue before returning.  # noqa: E501

        :param wait_time_seconds: The wait_time_seconds of this V1alpha1SQSEventSource.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and wait_time_seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `wait_time_seconds`, must not be `None`")  # noqa: E501

        self._wait_time_seconds = wait_time_seconds

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
        if not isinstance(other, V1alpha1SQSEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1SQSEventSource):
            return True

        return self.to_dict() != other.to_dict()