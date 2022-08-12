from kafka.admin import KafkaAdminClient, NewTopic, ConfigResource, ConfigResourceType

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='payam')
topic_list = []
new_topic = NewTopic(name="ash", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)
configs = admin_client.describe_configs(config_resources=[ConfigResource(ConfigResourceType.TOPIC, "ash")])
#---
from kafka.producer import KafkaProducer
import json

producer = KafkaProducer(value_serializer=lambda value: json.dumps(value).encode('utf-8'))
producer.send("ash", {'atmid':1, 'transid':100})
#---
from kafka.consumer import KafkaConsumer

consumer = KafkaConsumer('ash', bootstrap_servers=['localhost:9092'])
for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.value.decode('utf-8')))