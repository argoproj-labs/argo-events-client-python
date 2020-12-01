# V1alpha1OpenWhiskTrigger

OpenWhiskTrigger refers to the specification of the OpenWhisk trigger.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_name** | **str** | Name of the action/function. | 
**auth_token** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**host** | **str** | Host URL of the OpenWhisk. | 
**namespace** | **str** | Namespace for the action. Defaults to \&quot;_\&quot;. | [optional] 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**payload** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | 
**version** | **str** | Version for the API. Defaults to v1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


