# IoT Device Streaming with Azure Function

This project demonstrates a solution for ingesting and processing data from IoT devices using Azure IoT Hub, Event Hub, and Azure Functions in Python.

## Project Structure

```
iot-device-streaming-azure/
├── ProcessIoTData/
│   ├── function.json          # Event Hub trigger configuration
│   └── __init__.py           # Function main code
├── host.json                 # Host settings
├── local.settings.json       # Local settings (not versioned)
├── requirements.txt          # Python dependencies
├── .gitignore                # Files ignored by Git
└── README.md                 # Project documentation
```

## Setup

**Requirements:**
- Python 3.12
- Azure CLI
- Azure Functions Core Tools
- VS Code with Azure Functions extension

**Installation:**
```bash
pip install -r requirements.txt
```

**local.settings.json:**
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "AzureWebJobsEventHubConnectionString": "<YOUR_EVENT_HUB_CONNECTION_STRING>",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

## Functionality

The function `ProcessIoTData`:
- Listens to JSON messages from the Event Hub (IoT Hub-compatible endpoint)
- Extracts temperature and humidity
- Logs the values
- Triggers an alert if temperature > 30°C

**Example code:**
```python
import logging
import json
import azure.functions as func

def main(event: func.EventHubEvent):
    try:
        message = event.get_body().decode('utf-8')
        data = json.loads(message)

        temperature = data.get("temperature")
        humidity = data.get("humidity")

        logging.info(f"🌡️ Temp: {temperature} °C | 💧 Humidity: {humidity}%")

        if temperature and float(temperature) > 30:
            logging.warning("🚨 ALERT: Temperature above 30°C!")

    except Exception as e:
        logging.error(f"Error processing message: {e}")
```

## Deployment to Azure

```bash
func azure functionapp publish iotdevice
```

### Function App Details
- **Name:** iotdevice
- **Region:** West Europe
- **Runtime:** Python 3.12
- **Resource Group:** datateam
- **Hosting Plan:** Flex Consumption
- **Hostname:** iotdevice-byffeucde8hsbrbf.westeurope-01.azurewebsites.net
- **Consumer Group:** function-consumer

## Event Hub Metrics (Last hour)
- **Incoming Requests:** 58
- **Successful Requests:** 57
- **Incoming Messages:** 54
- **Incoming Bytes:** 21.62 kB
- **Errors:** 0
- **Outgoing Messages:** 0

These metrics confirm that the IoT device is actively sending telemetry (temperature and humidity) to the IoT Hub, which is successfully being ingested into the Event Hub. This validates the data flow between the Raspberry Pi device and the Azure backend.

## Business Value & ROI

| Metric                    | Estimated Annual Value (BRL) |
|--------------------------|------------------------------|
| IoT Device + Azure Cost  | R$ 1,600                     |
| Estimated Annual Savings | R$ 6,000                     |
| **ROI (1 year)**         | **275%**                     |

*ROI = (Savings - Investment) / Investment*

### Business Impact
- Operational Cost Reduction through automated sensor data collection
- Loss Prevention with real-time alerts
- Faster Decision-Making through live sensor data
- Auto-Scaling with Azure's serverless model

## Future Improvements
- Deploy on real hardware (Raspberry Pi + sensors)
- Automate device provisioning in IoT Hub
- Integrate with dashboards (Power BI, Azure Dashboard)
- Add advanced alerting (email, SMS, Teams)
- Enhance security (device authentication, TLS)
- Optimize Azure resource usage for cost
- Expand documentation and troubleshooting

---

*Note: This project was developed by Alexsander Silveira as a proof of concept to demonstrate the business value of IoT integrations using Azure services, enabling real-time monitoring and operational intelligence.*