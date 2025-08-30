-- Table 1: Menyimpan data sensor
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    vibration FLOAT NOT NULL,
    device_id INTEGER REFERENCES device_info(device_id)
);

-- Table 2: Menyimpan alert anomali yang terdeteksi
CREATE TABLE IF NOT EXISTS anomaly_alert (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    sensor_type VARCHAR(20) NOT NULL,
    value FLOAT NOT NULL,
    alert_message TEXT NOT NULL,
    device_id INTEGER REFERENCES device_info(device_id)
);

-- Table 3: Menyimpan info perangkat sensor
CREATE TABLE IF NOT EXISTS device_info (
    device_id SERIAL PRIMARY KEY,
    device_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active',
    installed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 4: Konfigurasi threshold tiap jenis sensor (bisa diedit dinamis)
CREATE TABLE IF NOT EXISTS sensor_config (
    id SERIAL PRIMARY KEY,
    sensor_type VARCHAR(20) NOT NULL,
    min_threshold FLOAT,
    max_threshold FLOAT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table 5: Log error dan info penting (opsional untuk debugging & monitoring)
CREATE TABLE IF NOT EXISTS log_error (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    module VARCHAR(50),
    error_message TEXT
);
