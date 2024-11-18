## 📷 Proyek Deteksi Objek dengan Edge Impulse & ESP32-CAM
Proyek ini bertujuan untuk mengembangkan sistem deteksi objek berbasis machine learning yang diterapkan pada perangkat ESP32-CAM menggunakan platform Edge Impulse. Sistem ini akan mampu mengidentifikasi objek dalam gambar secara efisien meskipun dengan perangkat keras berdaya rendah.

## 🚀 Tentang Proyek
Proyek ini bertujuan untuk mengembangkan sistem deteksi objek yang dapat mengenali dua objek utama dalam arena perlombaan KRSRI 2024, yaitu korban dan dummy. Menggunakan platform Edge Impulse untuk melatih model machine learning dan perangkat ESP32-CAM, sistem ini diharapkan dapat memberikan solusi deteksi objek yang cepat dan akurat dalam kondisi lapangan yang dinamis. Tantangan utama dalam proyek ini adalah mengidentifikasi kedua objek tersebut secara efisien, mengingat keterbatasan sumber daya pada perangkat keras yang digunakan, serta variabilitas kondisi pencahayaan dan posisi objek di arena perlombaan.

Apa yang dapat dilakukan?
- ✅ Deteksi Objek Korban dan Dummy.
- ✅ Penggunaan Platform Edge Impulse.

## 🛠️ Fitur Utama
- Deteksi Objek Akurat dengan Machine Learning
- Integrasi dengan ESP32-CAM untuk Deteksi Real-Time
- Optimasi Perangkat Keras Berdaya Rendah

## 📋 Prasyarat
**Perangkat Keras**
1. ESP32-CAM
2. Kabel jumper (Opsional - Sesuai versi ESP32-CAM)
3. Sumber Daya Listrik (baterai atau kabel USB).

**Perangkat Lunak**
1. Akun Edge Impulse – [Daftar di sini](https://www.edgeimpulse.com)
2. Arduino IDE 1.8.19.
3. Board ESP32 2.0.4.

## 📖 Panduan Penggunaan
1️⃣ Pelatihan Model  
Pelatihan model dilakukan menggunakan platform Edge Impulse. Berikut langkah-langkahnya:
1. Kumpulkan Dataset:
    - Gunakan kamera ESP32-CAM untuk mengumpulkan gambar.
    - Pastikan dataset memiliki variasi kondisi pencahayaan, sudut, dan latar belakang untuk meningkatkan akurasi.
    - Pastikan dataset memiliki resolusi 320 x 240, karena kamera bekerja dengan resolusi tersebut saat pendeteksian objek.
2. Dashboard:
    - Pastikan sudah daftar dan login ke Edge Impulse.
    - Buat proyek baru dan pilih Add existing data di halaman Dashboard.
    - Pilih Upload Data dan pilih file dataset anda.
3. Data acquisition:
    - Di halaman Data Acquisition, pilih Labeling Queue.
    - Tandai objek pada gambar dan beri label sesuai keinginan, kemudian simpan label tersebut.
4. Create Impulse:
    - Di halaman Create Impulse. Jika muncul Configure your target device and application budget, pilih Espressif ESP-EYE (ESP32 240MHZ) lalu save.
    - Pilih Image pada Add a processing block.
    - Pilih Object Detection (images) pada Add a learning block dan simpan impulse.
5. Image:
    - Pada halaman Image, pilih Grayscale untuk color depth dan Save parameters.
    - Klik Generate Features, dan pastikan statusnya Job completed (success).
6. Object Detection:
    - Di halaman Object Detection, atur Number of training cycles ke 60, Learning rate ke 0.005, dan pilih model FOMO MobileNetV2 0.35. Kemudian klik Save & Train.
    - Pastikan statusnya Job completed (success).
7. Ekspor Model:
    - Pada Search deployment options pilih Arduino library. Lalu klik Build.

2️⃣ Pengunggahan ke ESP32-CAM

3️⃣ Uji dan Implementasi
