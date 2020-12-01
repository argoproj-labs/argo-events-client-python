# V1alpha1TriggerTemplate

TriggerTemplate is the template that describes trigger specification.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argo_workflow** | [**V1alpha1ArgoWorkflowTrigger**](V1alpha1ArgoWorkflowTrigger.md) |  | [optional] 
**aws_lambda** | [**V1alpha1AWSLambdaTrigger**](V1alpha1AWSLambdaTrigger.md) |  | [optional] 
**conditions** | **str** | Conditions is the conditions to execute the trigger. For example: \&quot;(dep01 || dep02) &amp;&amp; dep04\&quot; | [optional] 
**custom** | [**V1alpha1CustomTrigger**](V1alpha1CustomTrigger.md) |  | [optional] 
**http** | [**V1alpha1HTTPTrigger**](V1alpha1HTTPTrigger.md) |  | [optional] 
**k8s** | [**V1alpha1StandardK8STrigger**](V1alpha1StandardK8STrigger.md) |  | [optional] 
**kafka** | [**V1alpha1KafkaTrigger**](V1alpha1KafkaTrigger.md) |  | [optional] 
**name** | **str** | Name is a unique name of the action to take. | 
**nats** | [**V1alpha1NATSTrigger**](V1alpha1NATSTrigger.md) |  | [optional] 
**open_whisk** | [**V1alpha1OpenWhiskTrigger**](V1alpha1OpenWhiskTrigger.md) |  | [optional] 
**slack** | [**V1alpha1SlackTrigger**](V1alpha1SlackTrigger.md) |  | [optional] 
**switch** | [**V1alpha1TriggerSwitch**](V1alpha1TriggerSwitch.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


