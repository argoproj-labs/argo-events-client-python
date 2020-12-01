# V1alpha1PulsarEventSource

PulsarEventSource describes the event source for Apache Pulsar
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_backoff** | [**CommonBackoff**](CommonBackoff.md) |  | [optional] 
**json_body** | **bool** | JSONBody specifies that all event body payload coming from this source will be JSON | [optional] 
**metadata** | **dict(str, str)** | Metadata holds the user defined metadata which will passed along the event payload. | [optional] 
**tls** | [**CommonTLSConfig**](CommonTLSConfig.md) |  | [optional] 
**tls_allow_insecure_connection** | **bool** | Whether the Pulsar client accept untrusted TLS certificate from broker. | [optional] 
**tls_trust_certs_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) |  | [optional] 
**tls_validate_hostname** | **bool** | Whether the Pulsar client verify the validity of the host name from broker. | [optional] 
**topics** | **list[str]** | Name of the topics to subscribe to. | 
**type** | **str** | Type of the subscription. Only \&quot;exclusive\&quot; and \&quot;shared\&quot; is supported. Defaults to exclusive. | [optional] 
**url** | **str** | Configure the service URL for the Pulsar service. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


