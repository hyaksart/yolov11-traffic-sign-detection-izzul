import cv2
import os

# =========================================================================
#  BAGIAN INI YANG KAMU GANTI SESUAI VIDEO
# =========================================================================

# 1. Tulis nama file videomu (Misal: kanan.mp4, kiri.MOV)
NAMA_VIDEO = "belok kanan.mp4" 

# 2. Nama depan file gambar nanti
LABEL_GAMBAR = "belo kanan"

# 3. Jumlah gambar yang diinginkan
JUMLAH_TARGET = 100

# 4. Interval (Ambil tiap berapa frame)
INTERVAL_FRAME = 9

# =========================================================================
#  JANGAN UBAH KODE DI BAWAH INI
# =========================================================================

def crop_center_square(frame):
    # Ambil ukuran asli video
    h, w, _ = frame.shape
    
    # Cari sisi terpendek (biar jadi patokan kotak)
    min_dim = min(h, w)
    
    # Hitung titik tengah biar crop-nya pas di center
    start_x = (w - min_dim) // 2
    start_y = (h - min_dim) // 2
    
    # Potong frame (Crop)
    cropped = frame[start_y : start_y+min_dim, start_x : start_x+min_dim]
    
    return cropped

def jalankan_konversi():
    if not os.path.exists(NAMA_VIDEO):
        print(f"Error: File '{NAMA_VIDEO}' TIDAK DITEMUKAN!")
        return

    folder_hasil = "Hasil_Crop_" + LABEL_GAMBAR
    if not os.path.exists(folder_hasil):
        os.makedirs(folder_hasil)
        print(f"-> Folder '{folder_hasil}' berhasil dibuat.")

    cap = cv2.VideoCapture(NAMA_VIDEO)
    count = 0
    saved = 0

    print("-> Mulai memproses (Mode: Center Crop)...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % INTERVAL_FRAME == 0:
            try:
                # 1. Lakukan CROP dulu biar jadi kotak presisi
                frame_kotak = crop_center_square(frame)

                # 2. Baru di-resize ke 640x640 (Standar YOLO)
                #    Hasilnya tidak akan menceng/gepeng
                frame_final = cv2.resize(frame_kotak, (640, 640))
                
                nama_file = f"{folder_hasil}/{LABEL_GAMBAR}_{saved}.jpg"
                cv2.imwrite(nama_file, frame_final)
                saved += 1
                print(f"   Disimpan: {nama_file}")

                if saved >= JUMLAH_TARGET:
                    print(f"\n[SUKSES] Target {JUMLAH_TARGET} gambar tercapai!")
                    break
            except Exception as e:
                print(f"Gagal memproses frame: {e}")
        
        count += 1

    cap.release()
    print("Selesai. Gambarmu sekarang kotak sempurna (tidak gepeng).")

if __name__ == "__main__":
    jalankan_konversi()