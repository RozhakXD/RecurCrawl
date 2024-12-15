# RecurCrawl - Analisis Algoritma Crawler Iteratif dan Rekursif

## Deskripsi Proyek
**RecurCrawl** adalah aplikasi berbasis web yang membandingkan efisiensi runtime antara algoritma crawler iteratif dan rekursif dalam pengumpulan data balasan dari platform Threads. Pengujian dilakukan di hosting **Anymhost** dengan memori 10GB untuk melihat performa pada dataset ukuran 1000, 5000, dan 10.000.

## Fitur
- **Unggah Dataset**: Pengguna dapat mengunggah file JSON sebagai dataset untuk pengujian.
- **Pilih Algoritma**: Pilih antara metode iteratif atau rekursif.
- **Hasil Visual**: Hasil runtime ditampilkan secara dinamis dalam bentuk tabel dan grafik.
- **Analisis Performa**: Membandingkan performa kedua algoritma pada dataset yang berbeda ukuran.

## Teknologi
- Backend: Flask (Python)
- Frontend: HTML, Tailwindcss, JavaScript
- Hosting: Anymhost

## Instalasi dan Menjalankan Proyek
1. Clone Repository:

    ```bash
    git clone https://github.com/RozhakXD/RecurCrawl.git
    cd RecurCrawl
    ```
2. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```
3. Jalankan Server:

    ```bash
    python run.py
    ```
4. Akses Web: Buka `http://localhost:5000/` di browser.

## Hasil Pengujian
<details>
  <summary>Klik untuk melihat gambar</summary>

  ![RecurCrawl - Analisis Algoritma](https://github.com/user-attachments/assets/9e275350-a0dd-4126-937c-7f16ce453bee)

</details>

| Ukuran Data | Iterative Time (s) | Recursive Time (s) |
|:------------|:-------------------|:-------------------|
| 1000        | 0.0039             | 0.0023             |
| 5000        | 0.1121             | 0.0126             |
| 10000       | 0.0392             | 0.0277             |

## Kesimpulan
Algoritma iteratif lebih stabil untuk dataset besar, sedangkan rekursif unggul untuk dataset kecil. Anymhost dengan memori 10GB mendukung performa optimal dalam pengujian ini.

## Referensi
- [Analisis Perbandingan Kinerja Metode Rekursif dan Iteratif](https://ojs.unikom.ac.id/index.php/komputika/article/view/5493)
