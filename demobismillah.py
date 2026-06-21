import cv2
import time
import socket
from ultralytics import YOLO

# ==========================================
# 1. SETUP WIFI UDP (MODE BROADCAST)
# ==========================================qqqq
# .255 berarti mengirim ke semua perangkat di jaringan hotspot,
# ESP32 otomatis menangkap tanpa perlu IP Statis.
ESP32_IP = "192.168.137.255" 
ESP32_PORT = 4210

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Izinkan Broadcast

# ==========================================
# 2. SETUP MODEL YOLO
# ==========================================
MODEL_PATH = r"C:\Users\USER\Downloads\Sidang Kompre\Sidang Kompre\Codingan\v3.pt"
model = YOLO(MODEL_PATH)

# ==========================================
# 3. SETUP KAMERA
# ==========================================
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("❌ ERROR: Tidak ada kamera yang terdeteksi!")
    exit()

print("✅ SISTEM AKTIF: Memancarkan sinyal ke ESP32...")
print("✅ Tekan 'q' pada jendela video untuk keluar.")

# ==========================================
# 4. VARIABEL OPTIMASI KINERJA
# ==========================================
frame_count = 0
frame_skip = 5       # AI hanya mikir tiap 5 frame (Biar kamera nggak lemot)
last_boxes = []      # Memori letak kotak rambu
last_cmd = 'F'       # Default Maju
last_label = "Kosong (Maju)"

prev_time = time.time()

# ==========================================
# 5. LOOP UTAMA
# ==========================================
while True:
    ret, frame = cap.read()
    if not ret: 
        print("❌ Kamera terputus.")
        break

    frame_count += 1
    
    # Hitung FPS Kamera
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time

    # --- A. PROSES DETEKSI AI (Setiap 5 Frame) ---
    if frame_count % frame_skip == 0:
        results = model.predict(frame, conf=0.4, imgsz=320, verbose=False)
        
        last_boxes = [] # Bersihkan memori kotak lama
        temp_cmd = 'F'  # Reset paksa ke Maju jika tidak ada rambu
        temp_label = "Kosong (Maju)"
        
        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                # Simpan kotak untuk digambar
                last_boxes.append((label, conf, x1, y1, x2, y2))
                
                label_lower = label.lower()
                temp_label = label
                
                # Logika Perintah Mobil
                if "stop" in label_lower:
                    temp_cmd = 'S'
                elif "belok kanan" in label_lower or "right" in label_lower:
                    temp_cmd = 'R'
                elif "belok kiri" in label_lower or "left" in label_lower:
                    temp_cmd = 'L'

        # Simpan perintah final
        last_cmd = temp_cmd
        last_label = temp_label

        # --- B. KIRIM PERINTAH KE ESP32 ---
        # POSISI BENAR: Di dalam blok 'if' supaya tidak nyepam WiFi
        sock.sendto(last_cmd.encode(), (ESP32_IP, ESP32_PORT))

    # --- C. MENGGAMBAR VISUAL (Berjalan setiap frame agar mulus) ---
    for (label, conf, x1, y1, x2, y2) in last_boxes:
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} ({conf:.2f})", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Menulis status di pojok layar
    cv2.putText(frame, f"CMD ESP32: {last_cmd} | Deteksi: {last_label}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # --- D. TAMPILKAN VIDEO ---
    cv2.imshow("Demo Prototype Mobil Otonom", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()