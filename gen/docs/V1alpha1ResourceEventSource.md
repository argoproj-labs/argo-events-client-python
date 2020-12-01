# V1alpha1ResourceEventSource

ResourceEventSource refers to a event-source for K8s resource related events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_types** | **list[str]** | EventTypes is the list of event type to watch. Possible values are - ADD, UPDATE and DELETE. | 
**filter** | [**V1alpha1ResourceFilter**](V1alpha1ResourceFilter.md) |  | [optional] 
**group** | **str** |  | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**namespace** | **str** | Namespace where resource is deployed | 
**resource** | **str** |  | 
**version** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


