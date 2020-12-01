# V1alpha1PersistenceStrategy

PersistenceStrategy defines the strategy of persistence
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** | Available access modes such as ReadWriteOnce, ReadWriteMany https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes | [optional] 
**storage_class_name** | **str** | Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_size** | **str** | Volume size, e.g. 10Gi | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


