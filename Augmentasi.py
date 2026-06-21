import albumentations as A
import cv2
import os
import glob

# =========================================================
#  BAGIAN AUTO-DETECT LOKASI (Ini Obatnya!)
# =========================================================
# Script otomatis tahu dia sedang berada di folder mana
LOKASI_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# Kita arahkan folder input & output RELATIF terhadap script ini
FOLDER_INDUK = os.path.join(LOKASI_SCRIPT, "Dataset_Asli")
FOLDER_OUTPUT = os.path.join(LOKASI_SCRIPT, "Dataset_Siap_Train")

JUMLAH_VARIASI = 7  # 1 gambar asli -> 7 gambar baru (Total 8)

# =========================================================
#  PIPELINE AUGMENTASI
# =========================================================
transform = A.Compose([
    # Rotasi & Zoom
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=15, p=0.8),
    
    # Pencahayaan (Penting buat skripsi)
    A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.3, p=0.7),
    
    # Gangguan Visual (Saya ganti teknik noise biar tidak warning merah)
    A.OneOf([
        A.MotionBlur(blur_limit=5, p=1),
        A.ISONoise(p=1), 
    ], p=0.4),

    # Warna
    A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=30, val_shift_limit=20, p=0.5),
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

# =========================================================
#  FUNGSI BANTUAN
# =========================================================
def baca_label_yolo(txt_path):
    bboxes = []
    class_labels = []
    if os.path.exists(txt_path):
        with open(txt_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    cls_id = int(parts[0])
                    x, y, w, h = map(float, parts[1:])
                    bboxes.append([x, y, w, h])
                    class_labels.append(cls_id)
    return bboxes, class_labels

def simpan_label_yolo(txt_path, bboxes, class_labels):
    with open(txt_path, 'w') as f:
        for bbox, cls_id in zip(bboxes, class_labels):
            x, y, w, h = bbox
            # Pastikan koordinat aman (0.0 - 1.0)
            x = max(0, min(1, x))
            y = max(0, min(1, y))
            w = max(0, min(1, w))
            h = max(0, min(1, h))
            f.write(f"{cls_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")

# =========================================================
#  PROGRAM UTAMA
# =========================================================
def jalankan_augmentasi():
    print("=================================================")
    print(f"-> Script berjalan di: {LOKASI_SCRIPT}")
    print(f"-> Target Folder Data: {FOLDER_INDUK}")
    print("=================================================")

    # Setting path ke subfolder 'images' dan 'labels'
    path_images_in = os.path.join(FOLDER_INDUK, "images")
    path_labels_in = os.path.join(FOLDER_INDUK, "labels")

    path_images_out = os.path.join(FOLDER_OUTPUT, "images")
    path_labels_out = os.path.join(FOLDER_OUTPUT, "labels")

    # Cek apakah folder input 'Dataset_Asli' ada?
    if not os.path.exists(FOLDER_INDUK):
        print(f"\n[ERROR] Folder '{FOLDER_INDUK}' TIDAK DITEMUKAN!")
        print("Pastikan folder 'Dataset_Asli' ada tepat di sebelah file python ini.")
        return

    # Cek apakah di dalamnya ada folder 'images'?
    if not os.path.exists(path_images_in):
        print(f"\n[ERROR] Folder '{path_images_in}' TIDAK DITEMUKAN!")
        print("Pastikan struktur foldernya: Dataset_Asli > images > (file foto)")
        return

    # Buat folder output
    if not os.path.exists(path_images_out): os.makedirs(path_images_out)
    if not os.path.exists(path_labels_out): os.makedirs(path_labels_out)

    # Ambil semua foto
    exts = ['*.jpg', '*.jpeg', '*.png', '*.JPG']
    list_foto = []
    for ext in exts:
        list_foto.extend(glob.glob(os.path.join(path_images_in, ext)))

    if len(list_foto) == 0:
        print("[WARNING] Folder 'images' kosong! Tidak ada foto yang diproses.")
        return

    print(f"-> Ditemukan {len(list_foto)} gambar asli.")
    print("-> Mulai proses augmentasi... (Tunggu Sebentar)")

    count_sukses = 0
    for path_img in list_foto:
        image = cv2.imread(path_img)
        if image is None: continue
        
        # Cari labelnya di folder sebelah
        nama_file = os.path.splitext(os.path.basename(path_img))[0]
        ext_file = os.path.splitext(os.path.basename(path_img))[1]
        path_txt = os.path.join(path_labels_in, nama_file + ".txt")

        if not os.path.exists(path_txt): 
            # print(f"Skip: {nama_file} (Label tidak ada)")
            continue

        bboxes, class_labels = baca_label_yolo(path_txt)
        if len(bboxes) == 0: continue

        # 1. Simpan ASLI
        cv2.imwrite(os.path.join(path_images_out, f"{nama_file}_orig{ext_file}"), image)
        simpan_label_yolo(os.path.join(path_labels_out, f"{nama_file}_orig.txt"), bboxes, class_labels)

        # 2. Simpan AUGMENTASI
        for i in range(JUMLAH_VARIASI):
            try:
                augmented = transform(image=image, bboxes=bboxes, class_labels=class_labels)
                nama_baru = f"{nama_file}_aug_{i+1}"
                cv2.imwrite(os.path.join(path_images_out, f"{nama_baru}{ext_file}"), augmented['image'])
                simpan_label_yolo(os.path.join(path_labels_out, f"{nama_baru}.txt"), augmented['bboxes'], augmented['class_labels'])
            except:
                pass
        
        count_sukses += 1
        if count_sukses % 20 == 0:
            print(f"   Berhasil memproses {count_sukses} foto...")

    print("\n=================================================")
    print(f"[SELESAI] Cek folder: {FOLDER_OUTPUT}")
    print("=================================================")

if __name__ == "__main__":
    jalankan_augmentasi()