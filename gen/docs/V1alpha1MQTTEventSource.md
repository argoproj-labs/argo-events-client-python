# V1alpha1MQTTEventSource

MQTTEventSource refers to event-source for MQTT related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | ClientID is the id of the client | 
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**topic** | **str** | Topic name | 
**url** | **str** | URL to connect to broker | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


