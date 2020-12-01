# V1alpha1EmitterEventSource

EmitterEventSource describes the event source for emitter More info at https://emitter.io/develop/getting-started/
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker** | **str** | Broker URI to connect to. | 
**channel_key** | **str** | ChannelKey refers to the channel key | 
**channel_name** | **str** | ChannelName refers to the channel name | 
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**password** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**username** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


