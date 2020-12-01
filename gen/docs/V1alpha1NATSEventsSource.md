# V1alpha1NATSEventsSource

NATSEventsSource refers to event-source for NATS related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**subject** | **str** | Subject holds the name of the subject onto which messages are published | 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**url** | **str** | URL to connect to NATS cluster | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


