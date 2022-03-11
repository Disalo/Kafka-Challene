from kafka import KafkaProducer
import pandas as pd
from time import sleep

# read dataframe
df = pd.read_csv('de_challenge_sample_data (1).csv')

# create a producer which generates messages that are published to Kafka 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], retries=5)

# to read each row as one message and send to Kafka
for i in range(1):
    key = df.index[i]
    value = df.iloc[i]
    data = {key:value}
    producer.send('Wickipedia', value=data)
    sleep(1)