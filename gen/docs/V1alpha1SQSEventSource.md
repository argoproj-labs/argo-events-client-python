# V1alpha1SQSEventSource

SQSEventSource refers to event-source for AWS SQS related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**queue** | **str** | Queue is AWS SQS queue to listen to for messages | 
**queue_account_id** | **str** | QueueAccountID is the ID of the account that created the queue to monitor | [optional] 
**region** | **str** | Region is AWS region | 
**role_arn** | **str** | RoleARN is the Amazon Resource Name (ARN) of the role to assume. | [optional] 
**secret_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**wait_time_seconds** | **int** | WaitTimeSeconds is The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


