package com.fd.cep.kafka;

import java.io.IOException;

import org.apache.flink.api.common.serialization.DeserializationSchema;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.api.java.typeutils.TypeExtractor;

import com.fd.cep.entity.Transaction;
import com.google.gson.Gson;

public class TransactionDeserializer implements DeserializationSchema<Transaction> {

    /**
     * 
     */
    private static final long serialVersionUID = 5399476269470581352L;

    private Gson gson;

    @Override
    public TypeInformation<Transaction> getProducedType() {
        return TypeExtractor.getForClass(Transaction.class);
    }

    @Override
    public Transaction deserialize(byte[] message) throws IOException {
        if (gson == null) {
            gson = new Gson();
        }
        return gson.fromJson(new String(message), Transaction.class);
    }

    @Override
    public boolean isEndOfStream(Transaction nextElement) {
        return false;
    }

}