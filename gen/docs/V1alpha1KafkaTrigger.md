# V1alpha1KafkaTrigger

KafkaTrigger refers to the specification of the Kafka trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compress** | **bool** | Compress determines whether to compress message or not. Defaults to false. If set to true, compresses message using snappy compression. | [optional] 
**flush_frequency** | **int** | FlushFrequency refers to the frequency in milliseconds to flush batches. Defaults to 500 milliseconds. | [optional] 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**partition** | **int** | Partition to write data to. | 
**partitioning_key** | **str** | The partitioning key for the messages put on the Kafka topic. Defaults to broker url. | [optional] 
**payload** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | 
**required_acks** | **int** | RequiredAcks used in producer to tell the broker how many replica acknowledgements Defaults to 1 (Only wait for the leader to ack). | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**topic** | **str** | Name of the topic. More info at https://kafka.apache.org/documentation/#intro_topics | 
**url** | **str** | URL of the Kafka broker. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


