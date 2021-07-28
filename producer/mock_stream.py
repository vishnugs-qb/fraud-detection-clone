#!/usr/bin/python

from kafka import KafkaProducer
from random import gauss
from time import sleep
import sys
import json

server = "localhost:9092"

def main():

    ## the topic 
    topic = "fd-cep"

    ## create a Kafka producer with json serializer
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             bootstrap_servers=server)
    print("*** Starting fraud mocking transaction stream on " + server + ", topic : " + topic)
    inputs = [{"accountId":20,"timestamp":0,"amount":0.23},{"accountId":20,"timestamp":0,"amount":700.79},{"accountId":3,"timestamp":0,"amount":112.15}]
    ##[{"accountId":1,"timestamp":0,"amount":188.23},{"accountId":2,"timestamp":0,"amount":374.79},{"accountId":3,"timestamp":0,"amount":112.15},{"accountId":4,"timestamp":0,"amount":478.75},{"accountId":5,"timestamp":0,"amount":208.85},{"accountId":1,"timestamp":0,"amount":379.64},{"accountId":2,"timestamp":0,"amount":351.44},{"accountId":3,"timestamp":0,"amount":320.75},{"accountId":4,"timestamp":0,"amount":259.42},{"accountId":5,"timestamp":0,"amount":273.44},{"accountId":1,"timestamp":0,"amount":267.25},{"accountId":2,"timestamp":0,"amount":397.15},{"accountId":3,"timestamp":0,"amount":0.219},{"accountId":4,"timestamp":0,"amount":231.94},{"accountId":5,"timestamp":0,"amount":384.73},{"accountId":1,"timestamp":0,"amount":419.62},{"accountId":2,"timestamp":0,"amount":412.91},{"accountId":3,"timestamp":0,"amount":0.77},{"accountId":4,"timestamp":0,"amount":22.10},{"accountId":5,"timestamp":0,"amount":377.54},{"accountId":1,"timestamp":0,"amount":375.44},{"accountId":2,"timestamp":0,"amount":230.18},{"accountId":3,"timestamp":0,"amount":0.80},{"accountId":4,"timestamp":0,"amount":350.89},{"accountId":5,"timestamp":0,"amount":127.55},{"accountId":1,"timestamp":0,"amount":483.91},{"accountId":2,"timestamp":0,"amount":228.22},{"accountId":3,"timestamp":0,"amount":871.15},{"accountId":4,"timestamp":0,"amount":64.19},{"accountId":5,"timestamp":0,"amount":79.43},{"accountId":1,"timestamp":0,"amount":56.12},{"accountId":2,"timestamp":0,"amount":256.48},{"accountId":3,"timestamp":0,"amount":148.16},{"accountId":4,"timestamp":0,"amount":199.95},{"accountId":5,"timestamp":0,"amount":252.37},{"accountId":1,"timestamp":0,"amount":274.73},{"accountId":2,"timestamp":0,"amount":473.54},{"accountId":3,"timestamp":0,"amount":119.92},{"accountId":4,"timestamp":0,"amount":323.59},{"accountId":5,"timestamp":0,"amount":353.16},{"accountId":1,"timestamp":0,"amount":211.90},{"accountId":2,"timestamp":0,"amount":280.93},{"accountId":3,"timestamp":0,"amount":347.89},{"accountId":4,"timestamp":0,"amount":459.86},{"accountId":5,"timestamp":0,"amount":82.31},{"accountId":1,"timestamp":0,"amount":373.26},{"accountId":2,"timestamp":0,"amount":479.83},{"accountId":3,"timestamp":0,"amount":454.25},{"accountId":4,"timestamp":0,"amount":83.64},{"accountId":5,"timestamp":0,"amount":292.44}]

    try:
        for input in inputs :
            producer.send(topic, input, key = bytes(input['accountId']))
            print("Sending transaction: %s" % (json.dumps(input).encode('utf-8')))

        sleep(1)

    except KeyboardInterrupt:
        pass

        
    print("\nIntercepted user interruption ..\nBlock until all pending messages are sent..")
    producer.flush()

if __name__ == "__main__":
    main()



