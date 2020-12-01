# V1Volume

Volume represents a named volume in a pod that may be accessed by any container in the pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_elastic_block_store** | [**V1VolumeAwsElasticBlockStore**](V1VolumeAwsElasticBlockStore.md) |  | [optional] 
**azure_disk** | [**V1VolumeAzureDisk**](V1VolumeAzureDisk.md) |  | [optional] 
**azure_file** | [**V1VolumeAzureFile**](V1VolumeAzureFile.md) |  | [optional] 
**cephfs** | [**V1VolumeCephfs**](V1VolumeCephfs.md) |  | [optional] 
**cinder** | [**V1VolumeCinder**](V1VolumeCinder.md) |  | [optional] 
**config_map** | [**V1VolumeConfigMap**](V1VolumeConfigMap.md) |  | [optional] 
**csi** | [**V1VolumeCsi**](V1VolumeCsi.md) |  | [optional] 
**downward_api** | [**V1VolumeDownwardAPI**](V1VolumeDownwardAPI.md) |  | [optional] 
**empty_dir** | [**V1VolumeEmptyDir**](V1VolumeEmptyDir.md) |  | [optional] 
**fc** | [**V1VolumeFc**](V1VolumeFc.md) |  | [optional] 
**flex_volume** | [**V1VolumeFlexVolume**](V1VolumeFlexVolume.md) |  | [optional] 
**flocker** | [**V1VolumeFlocker**](V1VolumeFlocker.md) |  | [optional] 
**gce_persistent_disk** | [**V1VolumeGcePersistentDisk**](V1VolumeGcePersistentDisk.md) |  | [optional] 
**git_repo** | [**V1VolumeGitRepo**](V1VolumeGitRepo.md) |  | [optional] 
**glusterfs** | [**V1VolumeGlusterfs**](V1VolumeGlusterfs.md) |  | [optional] 
**host_path** | [**V1VolumeHostPath**](V1VolumeHostPath.md) |  | [optional] 
**iscsi** | [**V1VolumeIscsi**](V1VolumeIscsi.md) |  | [optional] 
**name** | **str** | Volume&#39;s name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 
**nfs** | [**V1VolumeNfs**](V1VolumeNfs.md) |  | [optional] 
**persistent_volume_claim** | [**V1VolumePersistentVolumeClaim**](V1VolumePersistentVolumeClaim.md) |  | [optional] 
**photon_persistent_disk** | [**V1VolumePhotonPersistentDisk**](V1VolumePhotonPersistentDisk.md) |  | [optional] 
**portworx_volume** | [**V1VolumePortworxVolume**](V1VolumePortworxVolume.md) |  | [optional] 
**projected** | [**V1VolumeProjected**](V1VolumeProjected.md) |  | [optional] 
**quobyte** | [**V1VolumeQuobyte**](V1VolumeQuobyte.md) |  | [optional] 
**rbd** | [**V1VolumeRbd**](V1VolumeRbd.md) |  | [optional] 
**scale_io** | [**V1VolumeScaleIO**](V1VolumeScaleIO.md) |  | [optional] 
**secret** | [**V1VolumeSecret**](V1VolumeSecret.md) |  | [optional] 
**storageos** | [**V1VolumeStorageos**](V1VolumeStorageos.md) |  | [optional] 
**vsphere_volume** | [**V1VolumeVsphereVolume**](V1VolumeVsphereVolume.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


