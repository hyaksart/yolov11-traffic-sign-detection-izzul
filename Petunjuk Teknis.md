# yolov11-traffic-sign-detection-izzul
Real-time traffic sign detection system for an autonomous miniature car prototype using YOLOv11.
# 🚗 Deteksi Rambu Lalu Lintas Menggunakan YOLOv11

Halo! Selamat datang di tempat penyimpanan kodingan Skripsi saya. 

Kodingan di sini berfungsi untuk membuat komputer / miniatur mobil bisa "melihat" dan mengenali rambu lalu lintas secara langsung lewat kamera. Sistem ini menggunakan teknologi kecerdasan buatan bernama **YOLOv11**.

---

🛠️ Cara Menyiapkan Aplikasi (Bagi Pemula)

Jika Anda ingin mencoba menjalankan kodingan ini di laptop Anda, ikuti 2 langkah mudah ini:

**Langkah 1: Download File "Otak" Kecerdasan Buatan**
Sistem ini butuh file khusus agar bisa pintar mengenali rambu (bernama `v3.pt`). Karena filenya besar, saya menyimpannya terpisah.
* Silakan download filenya di sini: `https://drive.google.com/drive/folders/1wCp0ctpYq4hFTbAdTC-YxQTaL-hx5Bn8?usp=sharing` (di drive juga tertera wiring didalam buku panduan)
* Setelah didownload, taruh file tersebut dicampur ke dalam folder kodingan ini.

**Langkah 2: Install Bahan-bahan di Laptop**
Pastikan laptop Anda sudah terpasang aplikasi Python. Buka CMD (Command Prompt) di laptop Anda, lalu ketik tulisan di bawah ini dan tekan Enter:
`pip install ultralytics opencv-python`

---

---

## 🚀 Cara Menjalankan Kamera & Menghubungkan ke Mobil (ESP32)

Sistem ini tidak hanya mendeteksi rambu, tetapi juga mengirimkan hasil deteksinya ke mikrokontroler (ESP32) pada prototipe mobil miniatur. Oleh karena itu, laptop dan mobil harus terhubung ke jaringan WiFi yang sama sebelum program dijalankan.

**Tahap 1: Aktifkan Hotspot Laptop**
1. Buka pengaturan jaringan atau **Mobile Hotspot** di laptop Anda.
2. Edit pengaturan hotspot dengan detail berikut:
   * Nama WiFi (Network name / SSID): `h1`
   * Kata Sandi (Password): `12345678`
3. Nyalakan Mobile Hotspot di laptop Anda.
4. Nyalakan prototipe mobil miniatur (ESP32). Tunggu beberapa saat agar mobil otomatis tersambung ke hotspot laptop Anda.

**Tahap 2: Jalankan Program Deteksi**
1. Pastikan Anda masih membuka folder kodingan ini di dalam **Visual Studio Code (VS Code)**.
2. Pastikan file "otak" kecerdasan buatan (seperti `v3.pt`) sudah berada di folder yang sama.
3. Buka tab `Terminal` di bagian bawah layar VS Code.
4. Ketik perintah berikut lalu tekan Enter:
   ```bash
   python demobismillah.py
---

## 📂 Fungsi File Lainnya (Untuk Kebutuhan Tingkat Lanjut)
Jika Anda penasaran untuk apa file-file lainnya, ini dia fungsinya:
* `pengambilan data.py` = Untuk memotret gambar rambu baru.
* `mengubahvidkefoto.py` = Untuk mengubah rekaman video rambu menjadi potongan-potongan foto.
* `Augmentasi.py` = Untuk mengedit banyak foto sekaligus secara otomatis (agar data lebih banyak).
* `Splitting.py` = Untuk memilah-milah foto sebelum komputer mulai belajar mengenali rambu.

Terima kasih sudah berkunjung!
