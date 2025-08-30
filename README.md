# 🌡️ Simulasi Monitoring Suhu

Proyek ini merupakan **simulasi sistem monitoring suhu secara real-time** menggunakan **Python, PostgreSQL, dan Docker**.  
Sistem ini terdiri dari beberapa komponen utama:
1. **Simulasi sensor** → Menghasilkan data suhu berkala (`sensor_stream.py`).
2. **Database PostgreSQL** → Menyimpan data suhu.
3. **Anomaly detection** → Mendeteksi suhu yang dianggap tidak normal (`anomaly.py`).
4. **Dashboard Metabase** → Visualisasi data suhu dalam bentuk grafik interaktif.

---

## 📂 Struktur Proyek
simulasi-monitoring-suhu/
│── anomaly.py # Script deteksi anomali
│── db.py # Koneksi dan operasi database
│── docker-compose.yml # Konfigurasi Docker (PostgreSQL + Metabase)
│── init_db.sql # Skrip inisialisasi database
│── requirements.txt # Dependensi Python
│── sensor_stream.py # Simulasi data sensor suhu
│── images/ # Folder berisi gambar/visualisasi
└── README.md # Dokumentasi proyek


---

## ⚙️ Teknologi yang Digunakan
- **Python 3.9+**
- **PostgreSQL** (Database)
- **Docker & Docker Compose**
- **Metabase** (Visualisasi data)
- **Pandas & Psycopg2** (Pengolahan & koneksi database)
- **Random & Time** (Simulasi data sensor)

---

## 📊 Arsitektur Sistem

```mermaid
flowchart LR
    A[Sensor Stream] -->|Insert data suhu| B[(PostgreSQL Database)]
    B --> C[Anomaly Detection]
    B --> D[Metabase Dashboard]
    C -->|Laporan Anomali| D


🚀 Cara Menjalankan
1. Clone Repository
git clone https://github.com/username/simulasi-monitoring-suhu.git
cd simulasi-monitoring-suhu

2. Jalankan Database & Dashboard

Jalankan Docker untuk menghidupkan PostgreSQL dan Metabase:
docker-compose up -d
PostgreSQL → port 5432
Metabase → http://localhost:3000

3. Inisialisasi Database
Database akan otomatis dibuat menggunakan init_db.sql.
Tabel temperature_readings berfungsi untuk menyimpan data suhu hasil simulasi.

4. Install Dependensi Python
pip install -r requirements.txt

5. Jalankan Simulasi Sensor
python sensor_stream.py
Script ini akan mengirim data suhu ke database setiap beberapa detik.

6. Jalankan Deteksi Anomali
python anomaly.py
Script ini akan membaca data dari database dan menandai suhu yang terdeteksi anomali.

📊 Visualisasi Dashboard
Dengan Metabase, kamu bisa membuat dashboard interaktif untuk memantau data suhu secara real-time.
