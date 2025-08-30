import random
import time
from datetime import datetime
from loguru import logger

from db import insert_sensor_data, insert_anomaly_alert
from anomaly import detect_anomaly

# Simulasi pembacaan sensor
def simulate_sensor_data():
    temperature = random.gauss(25, 3)         # suhu normal sekitar 25°C ± 3
    humidity = random.gauss(60, 10)           # kelembapan sekitar 60% ± 10
    vibration = random.gauss(0.02, 0.015)     # getaran sekitar 0.02 ± 0.015
    return temperature, humidity, vibration

# Fungsi utama streaming sensor
def stream_sensor_data(interval=5):
    logger.info("Starting simulated sensor stream...")

    while True:
        timestamp = datetime.now()
        temp, hum, vib = simulate_sensor_data()

        # Simpan ke DB
        insert_sensor_data(timestamp, temp, hum, vib)
        logger.info(f"[DATA] {timestamp} → Temp={temp:.2f}°C, Humidity={hum:.1f}%, Vibration={vib:.3f}")

        # Cek dan simpan anomali jika ada
        alerts = detect_anomaly(temp, hum, vib)
        for sensor_type, value, msg in alerts:
            insert_anomaly_alert(timestamp, sensor_type, value, msg)
            logger.warning(f"[ALERT] {sensor_type.upper()}={value:.2f} → {msg}")

        time.sleep(interval)

if __name__ == "__main__":
    stream_sensor_data()
