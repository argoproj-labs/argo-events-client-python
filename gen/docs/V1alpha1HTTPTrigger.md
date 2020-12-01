# V1alpha1HTTPTrigger

HTTPTrigger is the trigger for the HTTP request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**V1alpha1BasicAuth**](V1alpha1BasicAuth.md) |  | [optional] 
**headers** | **dict(str, str)** | Headers for the HTTP request. | [optional] 
**method** | **str** | Method refers to the type of the HTTP request. Refer https://golang.org/src/net/http/method.go for more info. Default value is POST. | [optional] 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**payload** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | 
**timeout** | **int** | Timeout refers to the HTTP request timeout in seconds. Default value is 60 seconds. | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**url** | **str** | URL refers to the URL to send HTTP request to. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


