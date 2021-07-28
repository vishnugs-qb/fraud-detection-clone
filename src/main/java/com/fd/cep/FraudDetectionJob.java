package com.fd.cep;

import java.util.Properties;

import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaProducer;
import org.apache.flink.streaming.connectors.kafka.KafkaSerializationSchema;

import com.fd.cep.entity.Alert;
import com.fd.cep.entity.Transaction;
import com.fd.cep.kafka.AlertSerializer;
import com.fd.cep.kafka.TransactionDeserializer;

public class FraudDetectionJob {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        Properties p = new Properties();
        p.put("bootstrap.servers", "localhost:9092");
        DataStream<Transaction> transactions = env
                .addSource(new FlinkKafkaConsumer<Transaction>("fd-cep", new TransactionDeserializer(), p));

        DataStream<Alert> alerts = transactions.keyBy(Transaction::getAccountId)
                .process(new FraudDetector())
                .name("fraud-detector");
        KafkaSerializationSchema<Alert> schema = new AlertSerializer();
        alerts.addSink(
                new FlinkKafkaProducer<Alert>("notifications", schema, p, FlinkKafkaProducer.Semantic.EXACTLY_ONCE));
//        alerts.addSink(new AlertSink()).name("send-alerts");

        env.execute("Fraud Detection");
    }
}