# V1alpha1EventContext

EventContext holds the context of the cloudevent received from an event source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacontenttype** | **str** | DataContentType - A MIME (RFC2046) string describing the media type of &#x60;data&#x60;. | 
**id** | **str** | ID of the event; must be non-empty and unique within the scope of the producer. | 
**source** | **str** | Source - A URI describing the event producer. | 
**specversion** | **str** | SpecVersion - The version of the CloudEvents specification used by the event. | 
**subject** | **str** | Subject - The subject of the event in the context of the event producer | 
**time** | **datetime** | Time - A Timestamp when the event happened. | 
**type** | **str** | Type - The type of the occurrence which has happened. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


