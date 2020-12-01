# V1alpha1GenericEventSource

GenericEventSource refers to a generic event source. It can be used to implement a custom event source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **str** | Config is the event source configuration | 
**insecure** | **bool** | Insecure determines the type of connection. | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**url** | **str** | URL of the gRPC server that implements the event source. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


