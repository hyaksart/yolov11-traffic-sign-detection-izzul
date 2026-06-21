
// #include <WiFi.h>
// #include <WiFiUdp.h>

// // --- KONFIGURASI WIFI ---
// const char* ssid = "hq";
// const char* password = "12345678";

// // --- KONFIGURASI UDP ---
// WiFiUDP udp;
// unsigned int localUdpPort = 4210;  // Port untuk menerima perintah
// char packetBuffer[255]; 

// // --- PIN MOTOR L298N (Sesuaikan dengan Pin ESP32) ---
// int IN1 = 12; 
// int IN2 = 13; 
// int IN3 = 14; 
// int IN4 = 27; 

// void setup() {
//   Serial.begin(115200);
  
//   pinMode(IN1, OUTPUT);
//   pinMode(IN2, OUTPUT);
//   pinMode(IN3, OUTPUT);
//   pinMode(IN4, OUTPUT);
//   stopMobil();

//   // Koneksi ke WiFi
//   WiFi.begin(ssid, password);
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }
  
//   Serial.println("");
//   Serial.println("WiFi Terhubung!");
//   Serial.print("IP Address ESP32: ");
//   Serial.println(WiFi.localIP()); // CATAT IP INI UNTUK DI PYTHON

//   udp.begin(localUdpPort);
// }

// void loop() {
//   int packetSize = udp.parsePacket();
//   if (packetSize) {
//     int len = udp.read(packetBuffer, 255);
//     if (len > 0) packetBuffer[len] = 0;
    
//     char perintah = packetBuffer[0];
//     Serial.print("Menerima perintah: ");
//     Serial.println(perintah);

//     if (perintah == 'F') maju();
//     else if (perintah == 'R') kanan();
//     else if (perintah == 'L') kiri();
//     else if (perintah == 'S') stopMobil();
//   }
// }

// void maju() {
//   digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
// }

// void kanan() {
//   digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH);
// }

// void kiri() {
//   digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH);
//   digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
// }

// void stopMobil() {
//   digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);
// }

// #include <WiFi.h>
// #include <WiFiUdp.h>

// // --- KONFIGURASI WIFI ---
// const char* ssid = "hq";
// const char* password = "12345678";

// // --- KONFIGURASI UDP ---
// WiFiUDP udp;
// unsigned int localUdpPort = 4210;  // Port untuk menerima perintah
// char packetBuffer[255]; 

// // --- PIN MOTOR L298N (Sesuaikan dengan Pin ESP32) ---
// int IN1 = 12; 
// int IN2 = 13; 
// int IN3 = 14; 
// int IN4 = 27; 

// // --- PIN LED (Sesuaikan dengan Pin ESP32) ---
// int LED_KIRI = 25;   // Lampu sein kiri
// int LED_KANAN = 26;  // Lampu sein kanan
// int LED_STOP = 32;   // Lampu rem/stop

// void setup() {
//   Serial.begin(115200);
  
//   // Setup Pin Motor
//   pinMode(IN1, OUTPUT);
//   pinMode(IN2, OUTPUT);
//   pinMode(IN3, OUTPUT);
//   pinMode(IN4, OUTPUT);

//   // Setup Pin LED
//   pinMode(LED_KIRI, OUTPUT);
//   pinMode(LED_KANAN, OUTPUT);
//   pinMode(LED_STOP, OUTPUT);

//   stopMobil(); // Kondisi awal mati semua

//   // Koneksi ke WiFi
//   WiFi.begin(ssid, password);
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }
  
//   Serial.println("");
//   Serial.println("WiFi Terhubung!");
//   Serial.print("IP Address ESP32: ");
//   Serial.println(WiFi.localIP()); // CATAT IP INI UNTUK DI PYTHON

//   udp.begin(localUdpPort);
// }

// void loop() {
//   int packetSize = udp.parsePacket();
//   if (packetSize) {
//     int len = udp.read(packetBuffer, 255);
//     if (len > 0) packetBuffer[len] = 0;
    
//     char perintah = packetBuffer[0];
//     Serial.print("Menerima perintah: ");
//     Serial.println(perintah);

//     if (perintah == 'F') maju();
//     else if (perintah == 'R') kanan();
//     else if (perintah == 'L') kiri();
//     else if (perintah == 'S') stopMobil();
//   }
// }

// // --- FUNGSI PERGERAKAN & LED ---

// void maju() {
//   // Motor Maju
//   digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);

//   // Semua LED Mati saat maju lurus
//   digitalWrite(LED_KIRI, LOW);
//   digitalWrite(LED_KANAN, LOW);
//   digitalWrite(LED_STOP, LOW);
// }

// void kanan() {
//   // Motor Belok Kanan
//   digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH);

//   // LED Kanan Nyala
//   digitalWrite(LED_KIRI, LOW);
//   digitalWrite(LED_KANAN, HIGH);
//   digitalWrite(LED_STOP, LOW);
// }

// void kiri() {
//   // Motor Belok Kiri
//   digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH);
//   digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);

//   // LED Kiri Nyala
//   digitalWrite(LED_KIRI, HIGH);
//   digitalWrite(LED_KANAN, LOW);
//   digitalWrite(LED_STOP, LOW);
// }

// void stopMobil() {
//   // Motor Berhenti
//   digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);

//   // LED Stop Nyala
//   digitalWrite(LED_KIRI, LOW);
//   digitalWrite(LED_KANAN, LOW);
//   digitalWrite(LED_STOP, HIGH);
// }


// #include <WiFi.h>
// #include <WiFiUdp.h>

// // --- KONFIGURASI WIFI ---
// const char* ssid = "hq";
// const char* password = "12345678";

// // --- KONFIGURASI IP STATIS (Agar IP Paten/Tidak Berubah) ---
// IPAddress local_IP(192, 168, 137, 23); 
// IPAddress gateway(192, 168, 137, 1);   
// IPAddress subnet(255, 255, 255, 0);

// // --- KONFIGURASI UDP ---
// WiFiUDP udp;
// unsigned int localUdpPort = 4210;  // Port untuk menerima perintah
// char packetBuffer[255]; 

// // --- PIN MOTOR L298N (Sesuaikan dengan Pin ESP32) ---
// int IN1 = 12; 
// int IN2 = 13; 
// int IN3 = 14; 
// int IN4 = 27; 

// // --- PIN LED (Total 6 Pin Terpisah Agar ESP32 Aman) ---
// // Lampu Sein Kiri
// int LED_KIRI_1 = 15;  // Kiri Depan
// int LED_KIRI_2 = 23;  // Kiri Belakang

// // Lampu Sein Kanan
// int LED_KANAN_1 = 16; // Kanan Depan
// int LED_KANAN_2 = 21; // Kanan Belakang

// // Lampu Stop/Rem
// int LED_STOP_1 = 22;   // Stop Kiri Belakang
// int LED_STOP_2 = 19;   // Stop Kanan Belakang

// void setup() {
//   Serial.begin(115200);
  
//   // Setup Pin Motor
//   pinMode(IN1, OUTPUT);
//   pinMode(IN2, OUTPUT);
//   pinMode(IN3, OUTPUT);
//   pinMode(IN4, OUTPUT);

//   // Setup Pin LED
//   pinMode(LED_KIRI_1, OUTPUT);
//   pinMode(LED_KIRI_2, OUTPUT);
//   pinMode(LED_KANAN_1, OUTPUT);
//   pinMode(LED_KANAN_2, OUTPUT);
//   pinMode(LED_STOP_1, OUTPUT);
//   pinMode(LED_STOP_2, OUTPUT);

//   stopMobil(); // Kondisi awal mati semua

//   // --- PASANG IP STATIS ---
//   if (!WiFi.config(local_IP, gateway, subnet)) {
//     Serial.println("Gagal mengatur IP Statis");
//   }

//   // Koneksi ke WiFi
//   WiFi.begin(ssid, password);
//   while (WiFi.status() != WL_CONNECTED) {
//     delay(500);
//     Serial.print(".");
//   }
  
//   Serial.println("");
//   Serial.println("WiFi Terhubung!");
//   Serial.print("IP Address ESP32 (Paten): ");
//   Serial.println(WiFi.localIP());

//   udp.begin(localUdpPort);
// }

// void loop() {
//   int packetSize = udp.parsePacket();
//   if (packetSize) {
//     int len = udp.read(packetBuffer, 255);
//     if (len > 0) packetBuffer[len] = 0;
    
//     char perintah = packetBuffer[0];
//     Serial.print("Menerima perintah: ");
//     Serial.println(perintah);

//     if (perintah == 'F') maju();
//     else if (perintah == 'R') kanan();
//     else if (perintah == 'L') kiri();
//     else if (perintah == 'S') stopMobil();
//   }
// }

// // --- FUNGSI PERGERAKAN & LOGIKA 6 LED ---

// void maju() {
//   // Motor Maju
//   digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);

//   // Semua 6 LED Mati saat maju lurus
//   digitalWrite(LED_KIRI_1, LOW);
//   digitalWrite(LED_KIRI_2, LOW);
//   digitalWrite(LED_KANAN_1, LOW);
//   digitalWrite(LED_KANAN_2, LOW);
//   digitalWrite(LED_STOP_1, LOW);
//   digitalWrite(LED_STOP_2, LOW);
// }

// void kanan() {
//   // Motor Belok Kanan
//   digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH);

//   // 2 LED Kanan Nyala, Sisanya Mati
//   digitalWrite(LED_KIRI_1, LOW);
//   digitalWrite(LED_KIRI_2, LOW);
  
//   digitalWrite(LED_KANAN_1, HIGH); // Nyala
//   digitalWrite(LED_KANAN_2, HIGH); // Nyala
  
//   digitalWrite(LED_STOP_1, LOW);
//   digitalWrite(LED_STOP_2, LOW);
// }

// void kiri() {
//   // Motor Belok Kiri
//   digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH);
//   digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);

//   // 2 LED Kiri Nyala, Sisanya Mati
//   digitalWrite(LED_KIRI_1, HIGH); // Nyala
//   digitalWrite(LED_KIRI_2, HIGH); // Nyala
  
//   digitalWrite(LED_KANAN_1, LOW);
//   digitalWrite(LED_KANAN_2, LOW);
  
//   digitalWrite(LED_STOP_1, LOW);
//   digitalWrite(LED_STOP_2, LOW);
// }

// void stopMobil() {
//   // Motor Berhenti
//   digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
//   digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);

//   // 2 LED Stop Nyala, Sisanya Mati
//   digitalWrite(LED_KIRI_1, LOW);
//   digitalWrite(LED_KIRI_2, LOW);
  
//   digitalWrite(LED_KANAN_1, LOW);
//   digitalWrite(LED_KANAN_2, LOW);
  
//   digitalWrite(LED_STOP_1, HIGH); // Nyala
//   digitalWrite(LED_STOP_2, HIGH); // Nyala
// }
#include <WiFi.h>
#include <WiFiUdp.h>

// --- KONFIGURASI WIFI ---
const char* ssid = "hq";
const char* password = "12345678";

// --- KONFIGURASI IP STATIS (Agar IP Paten 192.168.137.23) ---
IPAddress local_IP(192, 168, 137, 23); 
IPAddress gateway(192, 168, 137, 1);   
IPAddress subnet(255, 255, 255, 0);

// --- KONFIGURASI UDP ---
WiFiUDP udp;
unsigned int localUdpPort = 4210;  // Port untuk menerima perintah
char packetBuffer[255]; 

// --- PIN MOTOR L298N ---
int IN1 = 12; 
int IN2 = 13; 
int IN3 = 14; 
int IN4 = 27; 

void setup() {
  Serial.begin(115200);
  
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  stopMobil();

  // --- PASANG IP STATIS DI SINI ---
  if (!WiFi.config(local_IP, gateway, subnet)) {
    Serial.println("Gagal mengatur IP Statis");
  }

  // Koneksi ke WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi Terhubung!");
  Serial.print("IP Address ESP32 (Paten): ");
  Serial.println(WiFi.localIP()); 

  udp.begin(localUdpPort);
}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    int len = udp.read(packetBuffer, 255);
    if (len > 0) packetBuffer[len] = 0;
    
    char perintah = packetBuffer[0];
    Serial.print("Menerima perintah: ");
    Serial.println(perintah);

    if (perintah == 'F') maju();
    else if (perintah == 'R') kanan();
    else if (perintah == 'L') kiri();
    else if (perintah == 'S') stopMobil();
  }
}

void maju() {
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
}

void kanan() {
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);  digitalWrite(IN4, HIGH);
}

void kiri() {
  digitalWrite(IN1, LOW);  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
}

void stopMobil() {
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);
}