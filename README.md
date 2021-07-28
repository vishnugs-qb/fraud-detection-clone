# Transaction Fraud Detection CEP application 
Built using the sample from Apace Flink Docs. See [link](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/try-flink/datastream/) for more details.

# Prerequsites
- Download [Apace Flink](https://www.apache.org/dyn/closer.lua/flink/flink-1.13.1/flink-1.13.1-bin-scala_2.11.tgz)
- Download [Apace Kafka](https://www.apache.org/dyn/closer.cgi?path=/kafka/2.8.0/kafka-2.8.0-src.tgz)

# Install Instructions
```sh
# Setup Kafka
sh ~/kafka/bin/zookeeper-server-start.sh ~/kafka/config/zookeeper.properties
sh ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

# Create source and sink topics
sh ~/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic fd-cep 
sh ~/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic notifications

# Setup Flink
cd ~/flink/bin/ && ./start-cluster.sh
cd ~/flink/bin/ && ./flink run ~/fraud-detection-clone/target/fd-cep-0.0.1-SNAPSHOT-jar-with-dependencies.jar

# Observe sink
sh ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic notifications

# Send in mock transaction data
python ~/fraud-detection-clone/producer/mock_stream.py
```
