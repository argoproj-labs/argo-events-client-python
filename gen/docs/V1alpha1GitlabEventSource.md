# V1alpha1GitlabEventSource

GitlabEventSource refers to event-source related to Gitlab events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**delete_hook_on_finish** | **bool** | DeleteHookOnFinish determines whether to delete the GitLab hook for the project once the event source is stopped. | [optional] 
**enable_ssl_verification** | **bool** | EnableSSLVerification to enable ssl verification | [optional] 
**events** | **list[str]** | Events are gitlab event to listen to. Refer https://github.com/xanzy/go-gitlab/blob/bf34eca5d13a9f4c3f501d8a97b8ac226d55e4d9/projects.go#L794. | 
**gitlab_base_url** | **str** | GitlabBaseURL is the base URL for API requests to a custom endpoint | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**project_id** | **str** | ProjectID is the id of project for which integration needs to setup | 
**webhook** | [**V1alpha1WebhookContext**](V1alpha1WebhookContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


