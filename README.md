# Kafka-Python
Example of Kafka-Python App to produce and consume json files

## Environment Setup
Follow the instructions below to configure your local machine to run and develop the Kafka-Python application.

### Instruction to Run
After downloading the Kafka, navigate terminal to the downloaded file, then:
1. Start ZooKeeper: bin/zookeeper-server-start.sh config/zookeeper.properties 
(in case error, download and install binary version)
2. Start the Kafka broker service: bin/kafka-server-start.sh config/server.properties
3. Install kafka-python: pip install kafka-python
4. Open the jupyter_notebook file and run the cells.


### Hints:
list topics: kafka-topics.sh --list --bootstrap-server localhost:9092
delete a topic: kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic <topic_name>

Good training source: https://www.conduktor.io/kafka/kafka-topics-cli-tutorial