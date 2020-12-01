# V1alpha1ResourceFilter

ResourceFilter contains K8 ObjectMeta information to further filter resource event objects
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_start** | **bool** | If the resource is created after the start time then the event is treated as valid. | [optional] 
**created_by** | **datetime** | If resource is created before the specified time then the event is treated as valid. | [optional] 
**fields** | [**list[V1alpha1Selector]**](V1alpha1Selector.md) | Fields provide field filters similar to K8s field selector (see https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/). Unlike K8s field selector, it supports arbitrary fileds like \&quot;spec.serviceAccountName\&quot;, and the value could be a string or a regex. Same as K8s field selector, operator \&quot;&#x3D;\&quot;, \&quot;&#x3D;&#x3D;\&quot; and \&quot;!&#x3D;\&quot; are supported. | [optional] 
**labels** | [**list[V1alpha1Selector]**](V1alpha1Selector.md) | Labels provide listing options to K8s API to watch resource/s. Refer https://kubernetes.io/docs/concepts/overview/working-with-objects/label-selectors/ for more info. | [optional] 
**prefix** | **str** | Prefix filter is applied on the resource name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


