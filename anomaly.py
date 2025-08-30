import psycopg2
import time
from loguru import logger

# Konfigurasi DB
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "iot_db",
    "user": "iot_user",
    "password": "iot_pass"
}

# Fungsi deteksi anomali berdasarkan threshold
def detect_anomaly(temperature, humidity, vibration):
    alerts = []
    if temperature < 15 or temperature > 35:
        alerts.append(("temperature", temperature, "Temperature out of safe range!"))
    if humidity < 20 or humidity > 80:
        alerts.append(("humidity", humidity, "Humidity out of safe range!"))
    if vibration > 0.05:
        alerts.append(("vibration", vibration, "Vibration level too high!"))
    return alerts

# Fungsi koneksi database
def get_connection():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.OperationalError as e:
        logger.error(f"DB Connection Error: {e}")
        return None

# Fungsi utama untuk membaca data dan menyimpan alert
def monitor_anomalies():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    last_checked_id = 0

    while True:
        try:
            cursor.execute("""
                SELECT id, timestamp, temperature, humidity, vibration
                FROM sensor_data
                WHERE id > %s
                ORDER BY id
            """, (last_checked_id,))
            rows = cursor.fetchall()

            for row in rows:
                row_id, timestamp, temp, hum, vib = row
                alerts = detect_anomaly(temp, hum, vib)

                for sensor_type, value, message in alerts:
                    cursor.execute(
                        """
                        INSERT INTO anomaly_alert (timestamp, sensor_type, value, alert_message)
                        VALUES (%s, %s, %s, %s)
                        """,
                        (timestamp, sensor_type, value, message)
                    )
                    logger.warning(f"[ALERT] {sensor_type.upper()} anomaly at {timestamp} → {value:.2f} | {message}")

                last_checked_id = row_id

            conn.commit()
            time.sleep(5)  # interval cek
        except Exception as e:
            logger.error(f"Error monitoring anomalies: {e}")
            time.sleep(5)

if __name__ == "__main__":
    logger.info("Starting anomaly detection service...")
    monitor_anomalies()
