# EventsourceV1alpha1Template

Template holds the information of an EventSource deployment template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity** | [**V1Affinity**](V1Affinity.md) |  | [optional] 
**container** | [**V1Container**](V1Container.md) |  | [optional] 
**metadata** | [**CommonMetadata**](CommonMetadata.md) |  | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node&#39;s labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ | [optional] 
**security_context** | [**V1PodSecurityContext**](V1PodSecurityContext.md) |  | [optional] 
**service_account_name** | **str** | ServiceAccountName is the name of the ServiceAccount to use to run event source pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 
**volumes** | [**list[V1Volume]**](V1Volume.md) | Volumes is a list of volumes that can be mounted by containers in an eventsource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


