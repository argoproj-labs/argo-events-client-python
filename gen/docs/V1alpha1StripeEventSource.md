# V1alpha1StripeEventSource

StripeEventSource describes the event source for stripe webhook notifications More info at https://stripe.com/docs/webhooks
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**create_webhook** | **bool** | CreateWebhook if specified creates a new webhook programmatically. | [optional] 
**event_filter** | **list[str]** | EventFilter describes the type of events to listen to. If not specified, all types of events will be processed. More info at https://stripe.com/docs/api/events/list | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**webhook** | [**V1alpha1WebhookContext**](V1alpha1WebhookContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


