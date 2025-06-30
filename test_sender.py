import os
import json
import random
from azure.eventhub import EventHubProducerClient, EventData

# Get connection string from environment variable
CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STRING")
if not CONNECTION_STR:
    raise RuntimeError("Please set the EVENT_HUB_CONNECTION_STRING environment variable.")

def send_test_messages():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_STR,
        eventhub_name="alex"
    )
    try:
        event_data_batch = producer.create_batch()
        for i in range(5):
            temperature = random.uniform(20, 35)
            humidity = random.uniform(40, 80)
            message = {
                "temperature": round(temperature, 1),
                "humidity": round(humidity, 1),
                "timestamp": "2025-06-30T02:30:00Z",
                "device_id": f"device_{i+1}"
            }
            event_data_batch.add(EventData(json.dumps(message)))
            print(f"📤 Enviando: {message}")
        producer.send_batch(event_data_batch)
        print("✅ Mensagens enviadas com sucesso!")
    finally:
        producer.close()

if __name__ == "__main__":
    send_test_messages() 