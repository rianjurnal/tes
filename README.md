# Portal Web SOP Toko Komputer, Aksesori, dan Servis

Aplikasi web interaktif dan responsif (HP & Laptop) untuk mengelola **Standar Operasional Prosedur (SOP) Toko Komputer, Aksesori, dan Servis**.

## 🌐 Cara Menjalankan di GitHub Pages (Gratis & Online)

1. Upload seluruh file di folder ini (`index.html`, `sop_data.json`, `app.py`, `.nojekyll`, `README.md`) ke repository **GitHub** Anda.
2. Buka menu **Settings** di repository GitHub Anda -> pilih **Pages** di menu sebelah kiri.
3. Pada bagian **Build and deployment** > **Branch**, pilih branch `main` (atau `master`) dan folder `/ (root)`, lalu klik **Save**.
4. Tunggu sekitar 1 menit, maka halaman web SOP Anda akan langsung online di alamat:
   `https://username-anda.github.io/nama-repo/` dan bisa diakses dari HP maupun Laptop dari mana saja!

### Cara Menyimpan Perubahan di GitHub Pages:
* **Untuk Perangkat Sendiri (Otomatis):** Setiap kali Anda mengedit langkah atau mencentang checklist di browser HP/Laptop, perubahan otomatis tersimpan di memori browser (`localStorage`) perangkat tersebut.
* **Untuk Seluruh Tim (Update Permanen ke GitHub):** Setelah selesai mengedit di web, klik tombol **⬇️ Backup JSON** di panel sebelah kiri untuk mengunduh file `sop_data.json` terbaru, lalu upload/ganti file `sop_data.json` tersebut ke repository GitHub Anda.

## 🔐 Halaman Khusus Admin (`admin.html`)

Halaman admin terpisah untuk mengedit judul, menambah langkah kerja, menambah bab SOP baru, dan mengatur identitas toko:
* Buka file `admin.html` di browser atau buka menu **🔐 Admin** dari halaman utama.
* **Default PIN Admin:** `123456` (PIN dapat diubah kapan saja di menu *Edit Info Toko*).
* **Fitur Auto-Publish GitHub:** Di halaman admin, klik tombol **🐙 Set GitHub** dan masukkan token GitHub Anda sekali saja. Setiap kali Anda menekan tombol **💾 Simpan**, file `sop_data.json` di repository GitHub Anda akan otomatis diperbarui dan langsung tampil di GitHub Pages seluruh karyawan.

---

## 💻 Cara Menjalankan dengan Python (Lokal / Wi-Fi Toko)

Jika dijalankan menggunakan Python di komputer kasir/admin toko:
```bash
python app.py
```
* **Akses di Laptop:** `http://localhost:8000` (atau `http://localhost:8000/admin.html`)
* **Akses di HP (Wi-Fi yang sama):** `http://<IP-Laptop>:8000`
* Semua perubahan yang diedit dari halaman Admin lokal akan langsung tersimpan otomatis ke file `sop_data.json`.
