# V1alpha1HDFSEventSource

HDFSEventSource refers to event-source for HDFS related events
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **list[str]** |  | 
**check_interval** | **str** | CheckInterval is a string that describes an interval duration to check the directory state, e.g. 1s, 30m, 2h... (defaults to 1m) | [optional] 
**directory** | **str** | Directory to watch for events | 
**hdfs_user** | **str** | HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used. | [optional] 
**krb_c_cache_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**krb_config_config_map** | [**V1ConfigMapKeySelector**](V1ConfigMapKeySelector.md) |  | [optional] 
**krb_keytab_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**krb_realm** | **str** | KrbRealm is the Kerberos realm used with Kerberos keytab It must be set if keytab is used. | [optional] 
**krb_service_principal_name** | **str** | KrbServicePrincipalName is the principal name of Kerberos service It must be set if either ccache or keytab is used. | [optional] 
**krb_username** | **str** | KrbUsername is the Kerberos username used with Kerberos keytab It must be set if keytab is used. | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**path** | **str** | Path is relative path of object to watch with respect to the directory | [optional] 
**path_regexp** | **str** | PathRegexp is regexp of relative path of object to watch with respect to the directory | [optional] 
**type** | **str** | Type of file operations to watch | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


