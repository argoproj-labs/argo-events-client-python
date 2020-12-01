# V1alpha1RedisEventSource

RedisEventSource describes an event source for the Redis PubSub. More info at https://godoc.org/github.com/go-redis/redis#example-PubSub
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **list[str]** |  | 
**db** | **int** | DB to use. If not specified, default DB 0 will be used. | [optional] 
**host_address** | **str** | HostAddress refers to the address of the Redis host/server | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**namespace** | **str** | Namespace to use to retrieve the password from. It should only be specified if password is declared | [optional] 
**password** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


