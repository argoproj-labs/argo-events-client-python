# V1alpha1StorageGridEventSource

StorageGridEventSource refers to event-source for StorageGrid related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** | APIURL is the url of the storagegrid api. | 
**auth_token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | 
**bucket** | **str** | Name of the bucket to register notifications for. | 
**events** | **list[str]** |  | [optional] 
**filter** | [**V1alpha1StorageGridFilter**](V1alpha1StorageGridFilter.md) |  | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**region** | **str** | S3 region. Defaults to us-east-1 | [optional] 
**topic_arn** | **str** | TopicArn | 
**webhook** | [**V1alpha1WebhookContext**](V1alpha1WebhookContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


