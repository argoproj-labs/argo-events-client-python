# V1alpha1KafkaEventSource

KafkaEventSource refers to event-source for Kafka related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**consumer_group** | [**V1alpha1KafkaConsumerGroup**](V1alpha1KafkaConsumerGroup.md) |  | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**limit_events_per_second** | **int** | Sets a limit on how many events get read from kafka per second. | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**partition** | **str** | Partition name | 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**topic** | **str** | Topic name | 
**url** | **str** | URL to kafka cluster, multiple URLs separated by comma | 
**version** | **str** | Specify what kafka version is being connected to enables certain features in sarama, defaults to 1.0.0 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


