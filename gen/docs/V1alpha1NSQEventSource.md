# V1alpha1NSQEventSource

NSQEventSource describes the event source for NSQ PubSub More info at https://godoc.org/github.com/nsqio/go-nsq
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **str** | Channel used for subscription | 
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**host_address** | **str** | HostAddress is the address of the host for NSQ lookup | 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**topic** | **str** | Topic to subscribe to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


