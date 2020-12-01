# CommonTLSConfig

TLSConfig refers to TLS configuration for a client.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_path** | **str** | DeprecatedCACertPath refers the file path that contains the CA cert. Deprecated: use CACertSecret instead | 
**ca_cert_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**client_cert_path** | **str** | DeprecatedClientCertPath refers the file path that contains client cert. Deprecated: use ClientCertSecret instead | 
**client_cert_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**client_key_path** | **str** | DeprecatedClientKeyPath refers the file path that contains client key. Deprecated: use ClientKeySecret instead | 
**client_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


