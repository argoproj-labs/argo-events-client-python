# V1alpha1FileEventSource

FileEventSource describes an event-source for file related events.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Type of file operations to watch Refer https://github.com/fsnotify/fsnotify/blob/master/fsnotify.go for more information | 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**polling** | **bool** | Use polling instead of inotify | [optional] 
**watch_path_config** | [**V1alpha1WatchPathConfig**](V1alpha1WatchPathConfig.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


