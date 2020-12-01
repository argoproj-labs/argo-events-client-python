# V1alpha1SNSEventSource

SNSEventSource refers to event-source for AWS SNS related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**region** | **str** | Region is AWS region | 
**role_arn** | **str** | RoleARN is the Amazon Resource Name (ARN) of the role to assume. | [optional] 
**secret_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**topic_arn** | **str** | TopicArn | 
**webhook** | [**V1alpha1WebhookContext**](V1alpha1WebhookContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


