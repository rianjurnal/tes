#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplikasi Web SOP Toko Komputer, Aksesori, dan Servis
----------------------------------------------------
Fitur:
- Dapat diakses dari Laptop (http://localhost:8000) maupun HP dalam satu jaringan Wi-Fi
- Menyediakan REST API (/api/sop) untuk membaca, mengedit, menambah langkah/SOP baru,
  dan menyimpan perubahan langsung ke file `sop_data.json`
- Menggunakan library standar Python (tidak memerlukan `pip install` tambahan)

Cara Menjalankan:
    python app.py
"""

import json
import os
import socket
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "sop_data.json")
PORT = int(os.environ.get("PORT", 8000))


def get_local_ip():
    """Mendapatkan alamat IP lokal (LAN/Wi-Fi) agar bisa dibuka dari HP."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


class SOPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        # Izinkan akses CORS agar fleksibel saat diakses dari perangkat berbeda
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path).path

        if parsed_path == "/api/sop":
            self.handle_get_sop()
        elif parsed_path == "/api/info":
            self.handle_get_info()
        else:
            super().do_GET()

    def do_POST(self):
        parsed_path = urlparse(self.path).path
        if parsed_path == "/api/sop":
            self.handle_save_sop()
        else:
            self.send_error(404, "Endpoint tidak ditemukan")

    def handle_get_info(self):
        local_ip = get_local_ip()
        info = {
            "status": "online",
            "mode": "python_server",
            "local_url": f"http://localhost:{PORT}",
            "network_url": f"http://{local_ip}:{PORT}",
            "data_file": "sop_data.json"
        }
        self._send_json(200, info)

    def handle_get_sop(self):
        if not os.path.exists(DATA_FILE):
            self._send_json(404, {"error": "File sop_data.json tidak ditemukan"})
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._send_json(200, data)
        except Exception as e:
            self._send_json(500, {"error": str(e)})

    def handle_save_sop(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length).decode("utf-8")
            payload = json.loads(raw_body)

            # Validasi struktur dasar
            if not isinstance(payload, dict) or "metadata" not in payload or "sections" not in payload:
                self._send_json(400, {"error": "Format data SOP tidak valid"})
                return

            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)

            self._send_json(200, {"status": "success", "message": "Data SOP berhasil disimpan ke sop_data.json"})
        except Exception as e:
            self._send_json(500, {"error": f"Gagal menyimpan data: {str(e)}"})

    def _send_json(self, status_code, data):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    local_ip = get_local_ip()
    server_address = ("0.0.0.0", PORT)
    httpd = ThreadingHTTPServer(server_address, SOPRequestHandler)

    print("=" * 65)
    print("  SERVER WEB SOP TOKO KOMPUTER, AKSESORI, DAN SERVIS AKTIF")
    print("=" * 65)
    print(f"  - Buka di Laptop ini : http://localhost:{PORT}")
    print(f"  - Buka di HP (Wi-Fi) : http://{local_ip}:{PORT}")
    print(f"  - File Penyimpanan   : {DATA_FILE}")
    print("=" * 65)
    print("  Tekan Ctrl+C untuk menghentikan server.")
    print()

    try:
        webbrowser.open(f"http://localhost:{PORT}")
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
        httpd.server_close()


if __name__ == "__main__":
    main()
