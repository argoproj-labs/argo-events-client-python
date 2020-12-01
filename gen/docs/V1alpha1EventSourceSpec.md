# V1alpha1EventSourceSpec

EventSourceSpec refers to specification of event-source resource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amqp** | [**dict(str, V1alpha1AMQPEventSource)**](V1alpha1AMQPEventSource.md) | AMQP event sources | [optional] 
**azure_events_hub** | [**dict(str, V1alpha1AzureEventsHubEventSource)**](V1alpha1AzureEventsHubEventSource.md) | AzureEventsHub event sources | [optional] 
**calendar** | [**dict(str, V1alpha1CalendarEventSource)**](V1alpha1CalendarEventSource.md) | Calendar event sources | [optional] 
**emitter** | [**dict(str, V1alpha1EmitterEventSource)**](V1alpha1EmitterEventSource.md) | Emitter event source | [optional] 
**event_bus_name** | **str** | EventBusName references to a EventBus name. By default the value is \&quot;default\&quot; | [optional] 
**file** | [**dict(str, V1alpha1FileEventSource)**](V1alpha1FileEventSource.md) | File event sources | [optional] 
**generic** | [**dict(str, V1alpha1GenericEventSource)**](V1alpha1GenericEventSource.md) | Generic event source | [optional] 
**github** | [**dict(str, V1alpha1GithubEventSource)**](V1alpha1GithubEventSource.md) | Github event sources | [optional] 
**gitlab** | [**dict(str, V1alpha1GitlabEventSource)**](V1alpha1GitlabEventSource.md) | Gitlab event sources | [optional] 
**hdfs** | [**dict(str, V1alpha1HDFSEventSource)**](V1alpha1HDFSEventSource.md) | HDFS event sources | [optional] 
**kafka** | [**dict(str, V1alpha1KafkaEventSource)**](V1alpha1KafkaEventSource.md) | Kafka event sources | [optional] 
**minio** | [**dict(str, CommonS3Artifact)**](CommonS3Artifact.md) | Minio event sources | [optional] 
**mqtt** | [**dict(str, V1alpha1MQTTEventSource)**](V1alpha1MQTTEventSource.md) | MQTT event sources | [optional] 
**nats** | [**dict(str, V1alpha1NATSEventsSource)**](V1alpha1NATSEventsSource.md) | NATS event sources | [optional] 
**nsq** | [**dict(str, V1alpha1NSQEventSource)**](V1alpha1NSQEventSource.md) | NSQ event source | [optional] 
**pub_sub** | [**dict(str, V1alpha1PubSubEventSource)**](V1alpha1PubSubEventSource.md) | PubSub event sources | [optional] 
**pulsar** | [**dict(str, V1alpha1PulsarEventSource)**](V1alpha1PulsarEventSource.md) | Pulsar event source | [optional] 
**redis** | [**dict(str, V1alpha1RedisEventSource)**](V1alpha1RedisEventSource.md) | Redis event source | [optional] 
**replica** | **int** | Replica is the event source deployment replicas | [optional] 
**resource** | [**dict(str, V1alpha1ResourceEventSource)**](V1alpha1ResourceEventSource.md) | Resource event sources | [optional] 
**service** | [**V1alpha1Service**](V1alpha1Service.md) |  | [optional] 
**slack** | [**dict(str, V1alpha1SlackEventSource)**](V1alpha1SlackEventSource.md) | Slack event sources | [optional] 
**sns** | [**dict(str, V1alpha1SNSEventSource)**](V1alpha1SNSEventSource.md) | SNS event sources | [optional] 
**sqs** | [**dict(str, V1alpha1SQSEventSource)**](V1alpha1SQSEventSource.md) | SQS event sources | [optional] 
**storage_grid** | [**dict(str, V1alpha1StorageGridEventSource)**](V1alpha1StorageGridEventSource.md) | StorageGrid event sources | [optional] 
**stripe** | [**dict(str, V1alpha1StripeEventSource)**](V1alpha1StripeEventSource.md) | Stripe event sources | [optional] 
**template** | [**EventsourceV1alpha1Template**](EventsourceV1alpha1Template.md) |  | [optional] 
**webhook** | [**dict(str, V1alpha1WebhookContext)**](V1alpha1WebhookContext.md) | Webhook event sources | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


