# V1alpha1K8SResourcePolicy

K8SResourcePolicy refers to the policy used to check the state of K8s based triggers using labels
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoff** | [**CommonBackoff**](CommonBackoff.md) |  | 
**error_on_backoff_timeout** | **bool** | ErrorOnBackoffTimeout determines whether sensor should transition to error state if the trigger policy is unable to determine the state of the resource | 
**labels** | **dict(str, str)** | Labels required to identify whether a resource is in success state | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


