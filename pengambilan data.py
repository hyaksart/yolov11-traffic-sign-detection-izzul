import cv2
from ultralytics import YOLO
import time
import threading
import pandas as pd
import numpy as np
import os
from datetime import datetime

# ==========================================
# 1. KONFIGURASI
# ==========================================
MODEL_PATH = r"D:\Documents\Yolo V2 TA\v3.pt" 
OUTPUT_FILE = "Dataterbaru_Penelitian_YOLO.csv"
RECORD_DURATION = 5.0   

# Setting AI
AI_IMAGE_SIZE = 320     
CONF_THRESHOLD = 0.01   

# ==========================================
# 2. SISTEM (JANGAN DIUBAH)
# ==========================================
frame_to_process = None
detection_results = [] 
is_running = True
is_model_loaded = False

# --- THREAD AI ---
def ai_worker():
    global frame_to_process, detection_results, is_running, is_model_loaded
    try:
        print(f"📂 Memuat model...")
        # PERBAIKAN 1: Hapus 'model_path=', langsung variabelnya
        model = YOLO(MODEL_PATH) 
        is_model_loaded = True
        print("✅ Model AI Siap!")
    except Exception as e:
        print(f"❌ Error fatal pada Model: {e}")
        is_running = False
        return

    while is_running:
        if frame_to_process is not None:
            # Inference
            results = model.predict(frame_to_process, imgsz=AI_IMAGE_SIZE, conf=CONF_THRESHOLD, max_det=1, verbose=False)
            
            temp_results = []
            for r in results:
                for box in r.boxes:
                    name = model.names[int(box.cls[0])]
                    conf = float(box.conf[0])
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    temp_results.append((name, conf, x1, y1, x2, y2))
            
            detection_results = temp_results
            frame_to_process = None 
            time.sleep(0.01) 
        else:
            time.sleep(0.01)

# --- THREAD UTAMA ---
# Jalankan AI di background
t = threading.Thread(target=ai_worker)
t.daemon = True
t.start()

# Setup Input
print("\n=== SETUP ===")
try:
    current_lux = input("Nilai LUX: ")
    current_sign = input("Jenis Rambu: ")
except:
    current_lux = "0"
    current_sign = "Test"

# PERBAIKAN 2: HAPUS 'cv2.CAP_DSHOW'. Biarkan default.
# Coba buka kamera eksternal (1) dulu
print("\nMencoba membuka kamera index 1...")
cap = cv2.VideoCapture(0)

# Jika index 1 gagal/tidak ada, pindah ke 0
if not cap.isOpened():
    print("⚠️ Kamera 1 gagal. Pindah ke Kamera 0 (Laptop)...")
    cap.release()
    cap = cv2.VideoCapture(0)

# Set Resolusi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("❌ ERROR PARAH: Tidak ada kamera yang terdeteksi di index 0 atau 1.")
    print("Pastikan kabel webcam tertancap atau tidak ada aplikasi lain (Zoom/Meet) yang jalan.")
    exit()

print("🔵 KAMERA MENYALA! Tekan 'R' Rekam, 'Q' Keluar.")

# Variabel Rekam
is_recording = False
start_record_time = 0
recorded_confidences = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: 
        print("❌ Frame Error (Kamera putus/blank).")
        break

    # Kirim ke AI
    if is_model_loaded and frame_to_process is None:
        frame_to_process = frame.copy()

    # --- VISUALISASI ---
    current_conf = 0.0 
    
    if len(detection_results) > 0:
        for (name, conf, x1, y1, x2, y2) in detection_results:
            current_conf = conf 
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{name} {conf:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # --- PEREKAMAN ---
    if is_recording:
        elapsed = time.time() - start_record_time
        remaining = RECORD_DURATION - elapsed
        recorded_confidences.append(current_conf)

        cv2.circle(frame, (30, 30), 15, (0, 0, 255), -1)
        cv2.putText(frame, f"REC: {remaining:.1f}s", (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        if elapsed >= RECORD_DURATION:
            is_recording = False
            if len(recorded_confidences) > 0:
                avg_conf = np.mean(recorded_confidences)
                max_conf = np.max(recorded_confidences)
                frames_detected = [x for x in recorded_confidences if x > 0]
                detection_rate = (len(frames_detected) / len(recorded_confidences)) * 100
                
                print(f"\n[HASIL] {current_sign} @ {current_lux} Lux | Avg: {avg_conf:.4f} | Rate: {detection_rate:.1f}%")
                
                data = {
                    'Timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    'Lux': [current_lux],
                    'Rambu': [current_sign],
                    'Avg_Confidence': [round(avg_conf, 4)],
                    'Max_Confidence': [round(max_conf, 4)],
                    'Detection_Rate': [round(detection_rate, 2)],
                    'Frames': [len(recorded_confidences)]
                }
                df = pd.DataFrame(data)
                hdr = not os.path.isfile(OUTPUT_FILE)
                df.to_csv(OUTPUT_FILE, mode='a', header=hdr, index=False)
                print(" >> Data Tersimpan!")

    else:
        cv2.putText(frame, f"Standby | {current_sign} | {current_lux} Lux", (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        cv2.putText(frame, "[R]ekam  [L]ux  [Q]uit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Sistem Data Skripsi", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        is_running = False
        break
    elif key == ord('r') and not is_recording:
        is_recording = True
        start_record_time = time.time()
        recorded_confidences = []
        print("\n--- Merekam ---")
    elif key == ord('l'):
        print("\n=== UBAH SETTING ===")
        try:
            current_lux = input("Lux Baru: ")
            current_sign = input("Rambu Baru: ")
        except:
            pass
        print("Lanjut...")

cap.release()
cv2.destroyAllWindows()