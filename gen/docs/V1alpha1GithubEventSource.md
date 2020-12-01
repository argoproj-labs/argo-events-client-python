# V1alpha1GithubEventSource

GithubEventSource refers to event-source for github related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Active refers to status of the webhook for event deliveries. https://developer.github.com/webhooks/creating/#active | [optional] 
**api_token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**content_type** | **str** | ContentType of the event delivery | [optional] 
**delete_hook_on_finish** | **bool** | DeleteHookOnFinish determines whether to delete the GitHub hook for the repository once the event source is stopped. | [optional] 
**events** | **list[str]** |  | 
**github_base_url** | **str** | GitHub base URL (for GitHub Enterprise) | [optional] 
**github_upload_url** | **str** | GitHub upload URL (for GitHub Enterprise) | [optional] 
**id** | **int** | Id is the webhook&#39;s id | 
**insecure** | **bool** | Insecure tls verification | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**owner** | **str** | Owner refers to GitHub owner name i.e. argoproj | 
**repository** | **str** | Repository refers to GitHub repo name i.e. argo-events | 
**webhook** | [**V1alpha1WebhookContext**](V1alpha1WebhookContext.md) |  | [optional] 
**webhook_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


