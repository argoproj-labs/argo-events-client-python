# V1alpha1WebhookContext

WebhookContext holds a general purpose REST API context
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**endpoint** | **str** | REST API endpoint | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**method** | **str** | Method is HTTP request method that indicates the desired action to be performed for a given resource. See RFC7231 Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content | 
**port** | **str** | Port on which HTTP server is listening for incoming events. | 
**server_cert_path** | **str** | DeprecatedServerCertPath refers the file that contains the cert. | [optional] 
**server_cert_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**server_key_path** | **str** | DeprecatedServerKeyPath refers the file that contains private key | [optional] 
**server_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**url** | **str** | URL is the url of the server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


