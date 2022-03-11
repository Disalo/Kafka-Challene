from kafka import KafkaConsumer
from time import sleep
import pandas as pd
import json

# create consumer to read each message as an event
consumer = KafkaConsumer(
    'Wickipedia',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest')

# collect events in a json file
for event in consumer:
    collected_events = json.loads(event)
    collected_events.update(event)
    json.dumps(collected_events)
    sleep(1)

# transofom dictionary to dataframe
df = pd.DataFrame.from_dict(collected_events)

# transform 'meta_dt' to datetime type
df["meta_dt"] = pd.to_datetime(df["meta_dt"])

# extract based on minutes
df['minutes'] = pd.to_datetime(df["meta_dt"]).dt.minute

# count number of edits per minute
Globale_Anzahl = df.groupby(['minutes'])['minutes'].count()

# create sub_dataframe from original one to filter those starts with "https://de"
df_de = df[df['server_url'].str.contains("https://de")]

# count number of edits by Germans per minute
Deutsche_Anzahl = df_de.groupby(['minutes'])['minutes'].count()

# print the results in tow for loops which could be output to two different platforms
for i in range(2):
    key = Globale_Anzahl.index[i]
    value = Globale_Anzahl.iloc[i]
    data = {key:value}
    print(data)
    sleep(1)

for j in range(2):
    key = Deutsche_Anzahl.index[j]
    value = Deutsche_Anzahl.iloc[j]
    data = {key:value}
    print(data)
    sleep(1)
