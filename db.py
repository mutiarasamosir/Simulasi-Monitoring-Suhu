import psycopg2
from psycopg2 import OperationalError, Error
from datetime import datetime
from loguru import logger

# Konfigurasi koneksi DB (bisa juga pakai dotenv jika mau)
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "iot_db",
    "user": "iot_user",
    "password": "iot_pass"
}

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except OperationalError as e:
        logger.error(f"[DB] Connection error: {e}")
        return None

def insert_sensor_data(timestamp: datetime, temperature: float, humidity: float, vibration: float):
    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO sensor_data (timestamp, temperature, humidity, vibration)
                VALUES (%s, %s, %s, %s)
                """,
                (timestamp, temperature, humidity, vibration)
            )
            conn.commit()
            logger.info(f"[DB] Sensor data inserted: {timestamp} | Temp={temperature:.2f}, Hum={humidity:.2f}, Vib={vibration:.3f}")
    except Error as e:
        logger.error(f"[DB] Error inserting sensor_data: {e}")
    finally:
        conn.close()

def insert_anomaly_alert(timestamp: datetime, sensor_type: str, value: float, alert_message: str):
    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO anomaly_alert (timestamp, sensor_type, value, alert_message)
                VALUES (%s, %s, %s, %s)
                """,
                (timestamp, sensor_type, value, alert_message)
            )
            conn.commit()
            logger.warning(f"[ALERT] {sensor_type}={value:.2f} at {timestamp} → {alert_message}")
    except Error as e:
        logger.error(f"[DB] Error inserting anomaly_alert: {e}")
    finally:
        conn.close()
