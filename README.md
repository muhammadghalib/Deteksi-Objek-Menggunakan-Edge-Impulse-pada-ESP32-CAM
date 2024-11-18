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
3. Board ESP32
    - Instal board ESP32 versi 2.0.4 atau lebih tinggi melalui Board Manager di Arduino IDE untuk memastikan kompatibilitas dengan modul ESP32-CAM.

## 📖 Panduan Penggunaan
1️⃣ Pelatihan Model  
Pelatihan model dilakukan menggunakan platform Edge Impulse. Berikut langkah-langkahnya:
1. Kumpulkan Dataset:
    - Gunakan kamera ESP32-CAM atau perangkat lain untuk mengumpulkan gambar.
    - Pastikan dataset memiliki variasi kondisi pencahayaan, sudut, dan latar belakang untuk meningkatkan akurasi.
2. Unggah Dataset ke Edge Impulse:
    - Daftar dan login ke Edge Impulse.
    - Buat proyek baru dan unggah dataset Anda ke bagian Data Acquisition.
3. Labeling Dataset:
    - Lakukan pelabelan dataset menggunakan fitur Bounding Box Labeling di Edge Impulse.
    - Pastikan setiap objek dalam gambar dilabeli dengan benar.
4. Latih Model:
    - Gunakan blok Object Detection di menu Impulse Design.
    - Pilih parameter pelatihan seperti learning rate dan epochs sesuai kebutuhan.
    - Klik Start Training dan tunggu hingga proses selesai.
5. Evaluasi Model:
    - Setelah pelatihan selesai, gunakan tab Model Testing untuk menguji akurasi model.
    - Perbaiki dataset atau parameter jika hasilnya kurang memuaskan.
6. Ekspor Model:
    - Ekspor model ke format ESP32 firmware melalui menu Deployment.
    - Pilih opsi ESP32-CAM dan unduh file firmware-nya.
