import os
import shutil
import random
import glob

# ==========================================
# KONFIGURASI
# ==========================================
FOLDER_INPUT = "Dataset_Siap_Train"  # Folder hasil augmentasi tadi
FOLDER_OUTPUT = "Dataset_Final_YOLO" # Folder hasil splitting (Siap Upload)

# Rasio pembagian (Total 1.0)
# Train 80%, Val 10%, Test 10%
RATIO_TRAIN = 0.8
RATIO_VAL = 0.1
RATIO_TEST = 0.1

# ==========================================
# PROGRAM UTAMA
# ==========================================
def split_dataset():
    # 1. Buat Struktur Folder YOLO
    for split in ['train', 'val', 'test']:
        os.makedirs(f"{FOLDER_OUTPUT}/{split}/images", exist_ok=True)
        os.makedirs(f"{FOLDER_OUTPUT}/{split}/labels", exist_ok=True)

    # 2. Ambil daftar semua gambar
    print("-> Sedang mendata file gambar...")
    list_gambar = glob.glob(f"{FOLDER_INPUT}/images/*.*")
    
    # Acak urutan biar adil (Shuffle)
    random.shuffle(list_gambar)
    
    total_data = len(list_gambar)
    print(f"-> Total Dataset: {total_data} gambar")

    # Hitung jumlah per bagian
    count_train = int(total_data * RATIO_TRAIN)
    count_val = int(total_data * RATIO_VAL)
    # Sisanya masuk test
    
    # 3. Mulai Memindahkan
    print("-> Mulai membagi dataset...")
    
    for i, path_img in enumerate(list_gambar):
        # Tentukan mau masuk folder mana
        if i < count_train:
            target = "train"
        elif i < count_train + count_val:
            target = "val"
        else:
            target = "test"

        # Nama file
        filename = os.path.basename(path_img)
        nama_tanpa_ext = os.path.splitext(filename)[0]
        
        # Path Label Asal
        path_lbl = f"{FOLDER_INPUT}/labels/{nama_tanpa_ext}.txt"
        
        # Pindahkan Gambar
        shutil.copy(path_img, f"{FOLDER_OUTPUT}/{target}/images/{filename}")
        
        # Pindahkan Label (Kalau ada)
        if os.path.exists(path_lbl):
            shutil.copy(path_lbl, f"{FOLDER_OUTPUT}/{target}/labels/{nama_tanpa_ext}.txt")
        
        if i % 500 == 0:
            print(f"   Memproses {i}/{total_data} files...")

    print("\n[SELESAI] Dataset siap!")
    print(f"Lokasi: {FOLDER_OUTPUT}")
    print(f"Train: {count_train}, Val: {count_val}, Test: {total_data - count_train - count_val}")

if __name__ == "__main__":
    split_dataset()