# V1alpha1SlackEventSource

SlackEventSource refers to event-source for Slack related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**signing_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**webhook** | [**V1alpha1WebhookContext**](V1alpha1WebhookContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


