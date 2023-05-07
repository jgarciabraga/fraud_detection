import faust
import address

app = faust.App('fraud_detection_app', broker='kafka://127.0.0.1:9092', value_serializer='raw')

kafka_topic = app.topic(address.kafka_topic)

@app.agent(kafka_topic)
async def process(transactions):
    async for message in transactions:
        print('Fraud detection result: ' + str(message))

if __name__ == '__main__':    
    app.main()
