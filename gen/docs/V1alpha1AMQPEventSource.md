# V1alpha1AMQPEventSource

AMQPEventSource refers to an event-source for AMQP stream events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**exchange_name** | **str** | ExchangeName is the exchange name For more information, visit https://www.rabbitmq.com/tutorials/amqp-concepts.html | 
**exchange_type** | **str** | ExchangeType is rabbitmq exchange type | 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**routing_key** | **str** | Routing key for bindings | 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**url** | **str** | URL for rabbitmq service | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


