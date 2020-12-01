# V1alpha1StandardK8STrigger

StandardK8STrigger is the standard Kubernetes resource trigger
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**live_object** | **bool** | LiveObject specifies whether the resource should be directly fetched from K8s instead of being marshaled from the resource artifact. If set to true, the resource artifact must contain the information required to uniquely identify the resource in the cluster, that is, you must specify \&quot;apiVersion\&quot;, \&quot;kind\&quot; as well as \&quot;name\&quot; and \&quot;namespace\&quot; meta data. Only valid for operation type &#x60;update&#x60; | [optional] 
**operation** | **str** | Operation refers to the type of operation performed on the k8s resource. Default value is Create. | [optional] 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**patch_strategy** | **str** | PatchStrategy controls the K8s object patching strategy when the trigger operation is specified as patch. possible values: \&quot;application/json-patch+json\&quot; \&quot;application/merge-patch+json\&quot; \&quot;application/strategic-merge-patch+json\&quot; \&quot;application/apply-patch+yaml\&quot;. Defaults to \&quot;application/merge-patch+json\&quot; | [optional] 
**resource** | **str** |  | 
**source** | [**V1alpha1ArtifactLocation**](V1alpha1ArtifactLocation.md) |  | [optional] 
**version** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


