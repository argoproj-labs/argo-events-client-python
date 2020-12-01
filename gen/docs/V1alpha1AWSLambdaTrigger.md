# V1alpha1AWSLambdaTrigger

AWSLambdaTrigger refers to specification of the trigger to invoke an AWS Lambda function
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**function_name** | **str** | FunctionName refers to the name of the function to invoke. | 
**parameters** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | [optional] 
**payload** | [**list[V1alpha1TriggerParameter]**](V1alpha1TriggerParameter.md) |  | 
**region** | **str** | Region is AWS region | 
**secret_key** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


