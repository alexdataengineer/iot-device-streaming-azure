# IoT Device Streaming Azure Function

Este projeto contém uma Azure Function em Python que processa dados de dispositivos IoT através do Azure IoT Hub.

## Estrutura do Projeto

```
iot-device-streaming-azure/
├── ProcessIoTData/
│   ├── function.json          # Configuração do trigger Event Hub
│   └── __init__.py           # Arquivo de inicialização do pacote
├── function_app.py           # Código principal da função
├── host.json                 # Configurações do host
├── local.settings.json       # Configurações locais (não versionado)
├── requirements.txt          # Dependências Python
├── .gitignore               # Arquivos ignorados pelo Git
└── README.md                # Este arquivo
```

## Configuração

### Pré-requisitos

- Python 3.12
- Azure Functions Core Tools
- Azure CLI (para publicação)

### Instalação

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure o arquivo `local.settings.json` com suas credenciais do Event Hub

## Funcionalidade

A função `ProcessIoTData`:

- Escuta mensagens do IoT Hub através do Event Hub-compatible endpoint
- Decodifica mensagens JSON recebidas
- Extrai os campos `temperature` e `humidity`
- Faz log dos valores no console
- Emite alerta quando a temperatura ultrapassa 30°C

## Teste Local

Para testar a função localmente:

```bash
func start
```

## Publicação

Para publicar na Azure Function App `iotdevice`:

```bash
func azure functionapp publish iotdevice
```

## Configurações da Function App

- **Nome**: iotdevice
- **Região**: West Europe
- **Runtime**: Python 3.12
- **Resource Group**: datateam
- **Hosting Plan**: Flex Consumption
- **Hostname**: iotdevice-byffeucde8hsbrbf.westeurope-01.azurewebsites.net
- **Instance Size**: 2048 MB
- **Zone Redundancy**: Enabled

## Consumer Group

- **Nome**: function-consumer

## Connection String

A connection string do Event Hub está configurada como `AzureWebJobsEventHubConnectionString` no arquivo `local.settings.json`.

## Business Value & ROI of IoT + Azure Integration

**Author:** Alexsander Silveira

### Overview

This project demonstrates how integrating IoT devices (such as a Raspberry Pi) with Microsoft Azure can deliver significant business value and a strong Return on Investment (ROI). By automating the collection and processing of environmental data (temperature, humidity, etc.), organizations can reduce operational costs, prevent losses, and enable real-time decision-making.

### Business Impact

- **Cost Reduction:**  
  Automating data collection eliminates manual checks, reducing labor costs and minimizing human error.
- **Loss Prevention:**  
  Real-time monitoring and alerting help prevent losses due to environmental anomalies (e.g., overheating, excessive humidity), which is critical for industries like logistics, manufacturing, healthcare, and agriculture.
- **Scalability:**  
  Azure's serverless architecture allows the solution to scale seamlessly as the number of devices or data volume grows, with pay-as-you-go pricing.
- **Data-Driven Decisions:**  
  Immediate access to sensor data enables faster and more informed business decisions.

### Example ROI Calculation

| Item                        | Annual Value (BRL) |
|-----------------------------|--------------------|
| Cost of IoT device + Azure  | R$ 1,600           |
| Estimated annual savings    | R$ 6,000           |
| **ROI (1 year)**            | **275%**           |

*ROI = (Savings - Investment) / Investment*

### Development Summary

- **Device:** Raspberry Pi (simulated sensor data)
- **Cloud:** Azure IoT Hub, Event Hub, Azure Functions (Python)
- **Features:**  
  - Real-time data ingestion and processing  
  - Automated alerts for abnormal temperature  
  - Scalable, serverless architecture  
  - Easy integration with dashboards and analytics

### Conclusion

By leveraging IoT and Azure, businesses can achieve rapid ROI, operational efficiency, and improved risk management. This project, developed by Alexsander Silveira, is a practical example of how modern cloud and edge technologies can transform business processes and outcomes.

## TODO

- [ ] **Deploy on Real Hardware:**  
  Test the solution with a real Raspberry Pi and physical sensors for temperature and humidity.

- [ ] **Device Provisioning Automation:**  
  Automate device registration and provisioning in Azure IoT Hub for large-scale deployments.

- [ ] **Dashboard Integration:**  
  Integrate with Power BI or Azure Dashboard for real-time data visualization and analytics.

- [ ] **Alerting Improvements:**  
  Add email, SMS, or Teams notifications for critical alerts.

- [ ] **Security Enhancements:**  
  Implement device authentication and secure communication (TLS, certificates).

- [ ] **Cost Optimization:**  
  Monitor Azure usage and optimize resources for better ROI.

- [ ] **Documentation:**  
  Expand documentation with setup guides, troubleshooting, and architecture diagrams.

### Running the Test Sender

Before running `test_sender.py`, set your Event Hub connection string as an environment variable:

**Linux/macOS:**
```bash
export EVENT_HUB_CONNECTION_STRING="<your-event-hub-connection-string>"
```

**Windows (CMD):**
```cmd
set EVENT_HUB_CONNECTION_STRING=<your-event-hub-connection-string>
```

Then run:
```bash
python test_sender.py
```