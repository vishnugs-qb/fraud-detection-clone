# Transaction Fraud Detection CEP application 
Built using the sample from Apace Flink Docs. See [link](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/try-flink/datastream/) for more details.

# Prerequsites
- Download [Apace Flink](https://www.apache.org/dyn/closer.lua/flink/flink-1.13.1/flink-1.13.1-bin-scala_2.11.tgz)
- Download [Apace Kafka](https://www.apache.org/dyn/closer.cgi?path=/kafka/2.8.0/kafka-2.8.0-src.tgz)

# Install Instructions
```sh
sh ~/kafka/bin/zookeeper-server-start.sh ~/kafka/config/zookeeper.properties

sh ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties

cd ~/flink/bin/ && ./start-cluster.sh

cd ~/flink/bin/ && ./flink run ~/fraud-detection-clone/target/fd-cep-0.0.1-SNAPSHOT-jar-with-dependencies.jar

sh ~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic notifications

python ~/fraud-detection-clone/producer/mock_stream.py
```
