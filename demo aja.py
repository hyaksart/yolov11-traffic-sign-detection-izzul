# import cv2
# from ultralytics import YOLO

# # 1. SETUP MODEL
# MODEL_PATH = r"D:\Documents\Yolo V2 TA\v3.pt"
# model = YOLO(MODEL_PATH)

# # 2. FUNGSI AUTO-SCAN KAMERA (Mencegah Index Out of Range)
# def get_camera():
#     for index in [1, 0, 2]: # Coba index 1 (external), lalu 0 (internal)
#         cap = cv2.VideoCapture(index)
#         if cap.isOpened():
#             print(f"✅ Kamera ditemukan di Index: {index}")
#             return cap
#     return None

# cap = get_camera()

# if cap is None:
#     print("❌ ERROR: Tidak ada kamera yang terdeteksi!")
#     exit()

# # Optimasi agar enteng
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# print("--- SISTEM AKTIF: Tekan 'q' untuk keluar ---")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ Gagal mengambil gambar dari kamera.")
#         break

#     # 3. DETEKSI RINGAN (imgsz=320 agar lancar)
#     results = model.predict(frame, conf=0.25, imgsz=320, verbose=False)

#     for r in results:
#         for box in r.boxes:
#             cls = int(box.cls[0])
#             label = model.names[cls]
#             conf = float(box.conf[0])
            
#             # Print ke Terminal (Serial Monitor)
#             print(f"TERDETEKSI: {label} ({conf:.2f})")

#             # Gambar Kotak & Label
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, f"{label}", (x1, y1 - 10), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # 4. TAMPILKAN
#     cv2.imshow("Demo Skripsi YOLO", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import time
from ultralytics import YOLO

# 1. SETUP MODEL
MODEL_PATH = r"D:\Documents\Yolo V2 TA\v3.pt"
model = YOLO(MODEL_PATH)

# 2. FUNGSI KAMERA BAWAAN LAPTOP (Index 0)
def get_camera():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    if cap.isOpened():
        print("✅ Kamera internal (Index 0) berhasil diakses!")
        return cap
    return None

cap = get_camera()
if cap is None:
    print("❌ ERROR: Tidak ada kamera yang terdeteksi!")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("--- SISTEM AKTIF: Tekan 'q' untuk keluar ---")

prev_time = 0
frame_count = 0
frame_skip = 5  # YOLO hanya akan berpikir setiap 5 frame sekali
last_boxes = [] # Menyimpan posisi kotak terakhir
inference_ms = 0.0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    frame_count += 1

    # 3. DETEKSI (Hanya jalan tiap kelipatan 5 frame agar CPU tidak ngos-ngosan)
    if frame_count % frame_skip == 0:
        results = model.predict(frame, conf=0.25, imgsz=320, verbose=False)
        last_boxes = [] # Reset kotak
        for r in results:
            inference_ms = r.speed['inference']
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                last_boxes.append((label, conf, x1, y1, x2, y2))

    # 4. GAMBAR KOTAK (Menggambar dari memori terakhir agar video tetap mulus)
    for (label, conf, x1, y1, x2, y2) in last_boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 5. TAMPILKAN TEKS FPS DAN MS
    cv2.putText(frame, f"FPS Kamera: {fps:.2f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f"Inferensi AI: {inference_ms:.2f} ms", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Demo Skripsi YOLO", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()