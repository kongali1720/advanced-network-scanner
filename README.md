# Advanced Network Scanner

Scanner port canggih dengan dukungan multithread, output dalam format JSON/CSV, dan deteksi layanan.

## Cara Menggunakan

```bash
python advanced_scanner.py <host> <start_port> <end_port> [--threads THREADS] [--json] [--csv]

python advanced_scanner.py 192.168.1.1 1 1000 --threads 50 --json
```

## Fitur

- 🔎 Pemindaian port TCP  
- 🚀 Multithreading (lebih cepat)  
- 📄 Output ke JSON atau CSV  
- 💬 Deteksi banner layanan (service banner)  

## Instalasi

```bash
git clone https://github.com/kongali1720/advanced-network-scanner.git
cd advanced-network-scanner
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ☕ Dukungan

Jika kamu merasa proyek ini bermanfaat dan ingin mendukung pengembangan lebih lanjut, kamu bisa mentransfer sedikit dukungan melalui PayPal:

[Buy Me a Coffee via PayPal](https://www.paypal.com/paypalme/bungtempong99)

## Lisensi

Distributed under the MIT License. See LICENSE for more information.

## Kontak

- **Nama**: Kongali1720  
- **Email**: [kongali1720@gmail.com](mailto:kongali1720@gmail.com)  
- **GitHub**: [https://github.com/kongali1720](https://github.com/kongali1720)
