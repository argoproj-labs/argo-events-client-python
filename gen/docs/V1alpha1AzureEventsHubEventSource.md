# V1alpha1AzureEventsHubEventSource

AzureEventsHubEventSource describes the event source for azure events hub More info at https://docs.microsoft.com/en-us/azure/event-hubs/
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | FQDN of the EventHubs namespace you created More info at https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-get-connection-string | 
**hub_name** | **str** | Event Hub path/name | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**shared_access_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**shared_access_key_name** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


