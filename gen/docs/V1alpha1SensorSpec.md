# V1alpha1SensorSpec

SensorSpec represents desired sensor state
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**circuit** | **str** | Circuit is a boolean expression of dependency groups DEPRECATED: Use Switch in triggers instead. | [optional] 
**dependencies** | [**list[V1alpha1EventDependency]**](V1alpha1EventDependency.md) | Dependencies is a list of the events that this sensor is dependent on. | 
**dependency_groups** | [**list[V1alpha1DependencyGroup]**](V1alpha1DependencyGroup.md) | DependencyGroups is a list of the groups of events. | [optional] 
**error_on_failed_round** | **bool** | ErrorOnFailedRound if set to true, marks sensor state as &#x60;error&#x60; if the previous trigger round fails. Once sensor state is set to &#x60;error&#x60;, no further triggers will be processed. | [optional] 
**event_bus_name** | **str** | EventBusName references to a EventBus name. By default the value is \&quot;default\&quot; | [optional] 
**template** | [**SensorV1alpha1Template**](SensorV1alpha1Template.md) |  | [optional] 
**triggers** | [**list[V1alpha1Trigger]**](V1alpha1Trigger.md) | Triggers is a list of the things that this sensor evokes. These are the outputs from this sensor. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


