from kafka import KafkaProducer
import address
import time
import pandas as pd
from uuid import uuid4

if __name__ == '__main__':
    
    
    df_input_producer = pd.read_csv("input_producer.csv", sep=";", index_col=0)
    df_input_producer = df_input_producer.reset_index(drop=True)
    producer = KafkaProducer(bootstrap_servers=address.kafka_servers)
    
    for i in range(len(df_input_producer)):
        message = {}
        for k in range(len(list(df_input_producer.columns))):
            message[list(df_input_producer.columns)[k]] = df_input_producer.at[i, list(df_input_producer.columns)[k]]
        key = bytes(str(uuid4), encoding='ascii')
        message_byte = bytes(str(message), encoding='ascii')
        producer.send(address.kafka_topic, key=key, value=message_byte)
        producer.flush()
        print(f'message {key} sended')
        time.sleep(2)
