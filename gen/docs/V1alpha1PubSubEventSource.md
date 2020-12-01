# V1alpha1PubSubEventSource

PubSubEventSource refers to event-source for GCP PubSub related events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**credentials_file** | **str** | CredentialsFile is the file that contains credentials to authenticate for GCP Deprecated, use CredentialSecret instead | 
**delete_subscription_on_finish** | **bool** | DeleteSubscriptionOnFinish determines whether to delete the GCP PubSub subscription once the event source is stopped. | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**project_id** | **str** | ProjectID is GCP project ID for the subscription. Required if you run Argo Events outside of GKE/GCE. (otherwise, the default value is its project) | [optional] 
**subscription_id** | **str** | SubscriptionID is ID of subscription. Required if you use existing subscription. The default value will be auto generated hash based on this eventsource setting, so the subscription might be recreated every time you update the setting, which has a possibility of event loss. | [optional] 
**topic** | **str** | Topic to which the subscription should belongs. Required if you want the eventsource to create a new subscription. If you specify this field along with an existing subscription, it will be verified whether it actually belongs to the specified topic. | [optional] 
**topic_project_id** | **str** | TopicProjectID is GCP project ID for the topic. By default, it is same as ProjectID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


