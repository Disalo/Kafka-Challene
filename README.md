# Kafka-Challene

Example Python App Consuming and Producing to Kafka topic

## Environment Setup
Follow the instructions below to configure your local machine to run and develop this example Python application.

### Local Docker Environment
The example code relies on a running Kafka service, the repo contains a Docker compose file that will spin up a configured Kafka.

* Install Docker : https://docs.docker.com/get-docker/

* Run the docker environment `docker-compose up`

This will launch a kafka service listening on port `9092` initialised with a Topic called `Wickipedia`.

Now you can run the producer.py and consumer.py in two different bash terminals to see the interactions.
