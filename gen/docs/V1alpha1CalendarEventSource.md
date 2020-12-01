# V1alpha1CalendarEventSource

CalendarEventSource describes a time based dependency. One of the fields (schedule, interval, or recurrence) must be passed. Schedule takes precedence over interval; interval takes precedence over recurrence
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusion_dates** | **list[str]** |  | [optional] 
**interval** | **str** | Interval is a string that describes an interval duration, e.g. 1s, 30m, 2h... | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**persistence** | [**V1alpha1EventPersistence**](V1alpha1EventPersistence.md) |  | [optional] 
**schedule** | **str** | Schedule is a cron-like expression. For reference, see: https://en.wikipedia.org/wiki/Cron | 
**timezone** | **str** | Timezone in which to run the schedule | [optional] 
**user_payload** | **str** | UserPayload will be sent to sensor as extra data once the event is triggered Deprecated. Please use Metadata instead. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


