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
* Silakan download filenya di sini: `https://drive.google.com/drive/folders/1b0SCrw-XLCO7AxQwFAzWQ3ekMXB8_NQZ?usp=sharing`
* Setelah didownload, taruh file tersebut dicampur ke dalam folder kodingan ini.

**Langkah 2: Install Bahan-bahan di Laptop**
Pastikan laptop Anda sudah terpasang aplikasi Python. Buka CMD (Command Prompt) di laptop Anda, lalu ketik tulisan di bawah ini dan tekan Enter:
`pip install ultralytics opencv-python`

---

## 🚀 Cara Menjalankan Kamera & Deteksi

Jika semua persiapan di atas sudah selesai, saatnya mencoba!
1. Buka CMD, dan arahkan ke folder tempat kodingan ini berada.
2. Ketik tulisan ini dan tekan Enter:
`python demobismillah.py`
3. Kamera laptop Anda akan menyala, dan cobalah hadapkan gambar rambu lalu lintas ke kamera.

---

## 📂 Fungsi File Lainnya (Untuk Kebutuhan Tingkat Lanjut)
Jika Anda penasaran untuk apa file-file lainnya, ini dia fungsinya:
* `pengambilan data.py` = Untuk memotret gambar rambu baru.
* `mengubahvidkefoto.py` = Untuk mengubah rekaman video rambu menjadi potongan-potongan foto.
* `Augmentasi.py` = Untuk mengedit banyak foto sekaligus secara otomatis (agar data lebih banyak).
* `Splitting.py` = Untuk memilah-milah foto sebelum komputer mulai belajar mengenali rambu.

Terima kasih sudah berkunjung!
