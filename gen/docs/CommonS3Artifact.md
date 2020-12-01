# CommonS3Artifact

S3Artifact contains information about an S3 connection and bucket
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | 
**bucket** | [**CommonS3Bucket**](CommonS3Bucket.md) |  | 
**endpoint** | **str** |  | 
**events** | **list[str]** |  | [optional] 
**filter** | [**CommonS3Filter**](CommonS3Filter.md) |  | [optional] 
**insecure** | **bool** |  | [optional] 
**metadata** | **dict(str, str)** |  | [optional] 
**region** | **str** |  | [optional] 
**secret_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


