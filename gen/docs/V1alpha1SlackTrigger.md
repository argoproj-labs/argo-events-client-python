# V1alpha1SlackTrigger

SlackTrigger refers to the specification of the slack notification trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel refers to which Slack channel to send slack message. | [optional] 
**message** | **str** | Message refers to the message to send to the Slack channel. | [optional] 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**slack_token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


