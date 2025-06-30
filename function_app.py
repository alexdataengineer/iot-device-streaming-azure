import logging
import json
import azure.functions as func

def main(event: func.EventHubEvent):
    try:
        message = event.get_body().decode('utf-8')
        data = json.loads(message)

        temperature = data.get("temperature")
        humidity = data.get("humidity")

        logging.info(f"📡 Mensagem recebida do IoT Hub:")
        logging.info(f"🌡️ Temperatura: {temperature}°C")
        logging.info(f"💧 Umidade: {humidity}%")

        if temperature and float(temperature) > 30:
            logging.warning("🚨 Alerta: Temperatura alta detectada!")

    except Exception as e:
        logging.error(f"Erro ao processar mensagem: {e}") 