package com.fd.cep.kafka;

import org.apache.flink.streaming.connectors.kafka.KafkaSerializationSchema;
import org.apache.kafka.clients.producer.ProducerRecord;

import com.fd.cep.entity.Alert;
import com.google.gson.Gson;

public class AlertSerializer implements KafkaSerializationSchema<Alert> {

    /**
     * 
     */
    private static final long serialVersionUID = -8384695868194054195L;

    private Gson gson;

    @Override
    public ProducerRecord<byte[], byte[]> serialize(Alert element, Long timestamp) {
        if (gson == null) {
            gson = new Gson();
        }
        ProducerRecord<byte[], byte[]> message = new ProducerRecord<byte[], byte[]>("notifications",
                gson.toJson(element).getBytes());
        return message;
    }

}