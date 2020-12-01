# V1alpha1GitArtifact

GitArtifact contains information about an artifact stored in git
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | Branch to use to pull trigger resource | [optional] 
**clone_directory** | **str** | Directory to clone the repository. We clone complete directory because GitArtifact is not limited to any specific Git service providers. Hence we don&#39;t use any specific git provider client. | 
**creds** | [**V1alpha1GitCreds**](V1alpha1GitCreds.md) |  | [optional] 
**file_path** | **str** | Path to file that contains trigger resource definition | 
**ref** | **str** | Ref to use to pull trigger resource. Will result in a shallow clone and fetch. | [optional] 
**remote** | [**V1alpha1GitRemoteConfig**](V1alpha1GitRemoteConfig.md) |  | [optional] 
**ssh_key_path** | **str** | DeprecatedSSHKeyPath is path to your ssh key path. Use this if you don&#39;t want to provide username and password. ssh key path must be mounted in sensor pod. DEPRECATED: use SSHKeySecret instead. | [optional] 
**ssh_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**tag** | **str** | Tag to use to pull trigger resource | [optional] 
**url** | **str** | Git URL | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


