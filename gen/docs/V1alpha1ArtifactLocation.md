# V1alpha1ArtifactLocation

ArtifactLocation describes the source location for an external artifact
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configmap** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) |  | [optional] 
**file** | [**V1alpha1FileArtifact**](V1alpha1FileArtifact.md) |  | [optional] 
**git** | [**V1alpha1GitArtifact**](V1alpha1GitArtifact.md) |  | [optional] 
**inline** | **str** | Inline artifact is embedded in sensor spec as a string | [optional] 
**resource** | [**object**](.md) | Resource is generic template for K8s resource | [optional] 
**s3** | [**CommonS3Artifact**](CommonS3Artifact.md) |  | [optional] 
**url** | [**V1alpha1URLArtifact**](V1alpha1URLArtifact.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


