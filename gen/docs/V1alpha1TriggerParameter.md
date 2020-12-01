# V1alpha1TriggerParameter

TriggerParameter indicates a passed parameter to a service template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest** | **str** | Dest is the JSONPath of a resource key. A path is a series of keys separated by a dot. The colon character can be escaped with &#39;.&#39; The -1 key can be used to append a value to an existing array. See https://github.com/tidwall/sjson#path-syntax for more information about how this is used. | 
**operation** | **str** | Operation is what to do with the existing value at Dest, whether to &#39;prepend&#39;, &#39;overwrite&#39;, or &#39;append&#39; it. | [optional] 
**src** | [**V1alpha1TriggerParameterSource**](V1alpha1TriggerParameterSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


