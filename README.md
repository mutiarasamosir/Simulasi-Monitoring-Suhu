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
