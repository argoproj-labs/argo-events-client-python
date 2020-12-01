# V1alpha1NativeStrategy

NativeStrategy indicates to install a native NATS service
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_affinity** | **bool** |  | [optional] 
**auth** | **str** |  | [optional] 
**container_template** | [**V1alpha1ContainerTemplate**](V1alpha1ContainerTemplate.md) |  | [optional] 
**max_age** | **str** | Max Age of existing messages, i.e. \&quot;72h\&quot;, “4h35m” | [optional] 
**metadata** | [**CommonMetadata**](CommonMetadata.md) |  | [optional] 
**metrics_container_template** | [**V1alpha1ContainerTemplate**](V1alpha1ContainerTemplate.md) |  | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node&#39;s labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ | [optional] 
**persistence** | [**V1alpha1PersistenceStrategy**](V1alpha1PersistenceStrategy.md) |  | [optional] 
**replicas** | **int** | Size is the NATS StatefulSet size | [optional] 
**security_context** | [**V1PodSecurityContext**](V1PodSecurityContext.md) |  | [optional] 
**tolerations** | [**list[V1Toleration]**](V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


