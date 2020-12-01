# V1alpha1CustomTrigger

CustomTrigger refers to the specification of the custom trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_file_path** | **str** | DeprecatedCertFilePath is path to the cert file within sensor for secure connection between sensor and custom trigger gRPC server. DEPRECATED: use CertSecret instead | [optional] 
**cert_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**payload** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | 
**secure** | **bool** | Secure refers to type of the connection between sensor to custom trigger gRPC | 
**server_name_override** | **str** | ServerNameOverride for the secure connection between sensor and custom trigger gRPC server. | [optional] 
**server_url** | **str** | ServerURL is the url of the gRPC server that executes custom trigger | 
**spec** | **dict(str, str)** | Spec is the custom trigger resource specification that custom trigger gRPC server knows how to interpret. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


