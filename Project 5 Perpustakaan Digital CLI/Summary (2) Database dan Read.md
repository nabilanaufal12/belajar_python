# Pengembangan Aplikasi CRUD Python: Inisialisasi Database & Operasi Baca (Read)

Catatan ini merangkum proses inisialisasi database dan implementasi operasi baca (read) dalam proyek CRUD (Create, Read, Update, Delete) menggunakan Python. Fokus utamanya adalah memastikan database tersedia saat program dijalankan dan menampilkan data yang ada dengan rapi.

## 1. Inisialisasi Database (`init_console`)

### 1.1. Konsep dan Tujuan
Fungsi `init_console` bertujuan untuk memeriksa keberadaan file database (`data.txt`) saat program pertama kali dijalankan. Jika database belum ada, program akan secara otomatis membuatnya untuk mencegah *error*. Ini memastikan program siap digunakan tanpa perlu intervensi manual untuk pembuatan file database awal.

### 1.2. Implementasi Cek Database dengan `try-except`
Pengecekan database dilakukan menggunakan blok `try-except` di dalam fungsi `init_console` yang berada di modul `database.py`.

*   **Blok `try`**: Program mencoba membuka file `data.txt` dalam mode baca (`'r'`). Jika berhasil, ini menandakan database sudah tersedia.
*   **Blok `except`**: Jika terjadi `FileNotFoundError` (atau *exception* lain yang relevan), berarti file database belum ada. Dalam kasus ini, program akan mencetak pesan bahwa database tidak ditemukan dan memanggil fungsi `operasi.create_first_data()` untuk membuat database baru.

### 1.3. Struktur Data dan Template
Untuk menjaga konsistensi dan kemudahan pengelolaan data, setiap baris data dalam `data.txt` harus memiliki format yang seragam dengan panjang karakter yang tetap.

Sebuah *dictionary* `TEMPLATE` didefinisikan di `database.py` untuk menentukan struktur dan panjang setiap kolom data:
*   `pk` (Primary Key): String acak 6 karakter yang unik.
*   `date_add`: Tanggal dan waktu penambahan data dalam format `YYYY-MM-DD-HH-MM-SS%z` (termasuk zona waktu GMT).
*   `judul`: String dengan panjang tetap 255 karakter.
*   `penulis`: String dengan panjang tetap 255 karakter.
*   `tahun`: String dengan panjang tetap 4 karakter.

Untuk menghasilkan `pk` acak, digunakan fungsi `random_string()` dari modul `util.py`. Sedangkan untuk `date_add`, digunakan `time.strftime()` dan `time.gmtime()`.

### 1.4. Fungsi `create_first_data()`
Fungsi ini berada di `operasi.py` dan bertanggung jawab untuk membuat data pertama kali saat database belum ada.

Langkah-langkahnya meliputi:
1.  Meminta *input* dari pengguna untuk `penulis`, `judul`, dan `tahun`.
2.  Menggunakan salinan (`.copy()`) dari `database.TEMPLATE` untuk mengisi data.
3.  Menghasilkan `pk` acak menggunakan `util.random_string(6)`.
4.  Menentukan `date_add` menggunakan `time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())`.
5.  Mengisi `penulis` dan `judul` dan menambahkan spasi di belakangnya hingga mencapai panjang karakter yang ditentukan dalam `TEMPLATE` (255 karakter).
6.  Mengubah `tahun` menjadi *string* dan memastikan panjangnya 4 karakter.
7.  Menggabungkan semua data menjadi satu *string* dengan pemisah koma (`,`) dan menambahkan karakter *newline* (`\n`) di akhir.
8.  Menulis *string* data ini ke `data.txt` dalam mode tulis (`'w'`) dengan *encoding* `utf-8`.

## 2. Operasi Baca (Read Data)

### 2.1. Alur dan Pembagian Tugas
Operasi baca data diimplementasikan melalui alur modular: `main.py` memanggil `view.read_console()`, yang kemudian memanggil `operasi.read()`.
*   **`operasi.py`**: Bertanggung jawab untuk berinteraksi langsung dengan file database (membaca data).
*   **`view.py`**: Bertanggung jawab untuk menampilkan data yang sudah dibaca ke konsol dengan format yang rapi.

### 2.2. Membaca Data dari File (`operasi.read()`)
Fungsi `read()` di `operasi.py` bertugas membaca seluruh isi file `data.txt`.
1.  Mencoba membuka `data.txt` dalam mode baca (`'r'`).
2.  Menggunakan `file.readlines()` untuk membaca semua baris file dan mengembalikannya sebagai daftar (*list*) *string*, di mana setiap elemen daftar adalah satu baris data dari file.
3.  Menangani *exception* jika terjadi kesalahan saat membaca database.

### 2.3. Menampilkan Data di Konsol (`view.read_console()`)
Fungsi `read_console()` di `view.py` menerima data dari `operasi.read()` dan menampilkannya dalam format tabel di konsol.

Langkah-langkahnya meliputi:
1.  Memanggil `operasi.read()` untuk mendapatkan daftar baris data.
2.  Mendefinisikan *header* tabel: `No`, `Judul`, `Penulis`, `Tahun`.
3.  Mencetak garis pemisah (`=`) dan *header* tabel yang diformat dengan lebar kolom tertentu (misalnya, `No:4`, `Judul:40`, `Penulis:40`, `Tahun:5`).
4.  Melakukan iterasi pada setiap baris data yang diterima dari `operasi.read()` menggunakan `enumerate` untuk mendapatkan indeks baris.
5.  Untuk setiap baris data:
    *   Memecah *string* baris data menjadi daftar elemen menggunakan `data.split(',')` karena data dipisahkan oleh koma.
    *   Mengekstrak nilai `pk`, `date_add`, `penulis`, `judul`, dan `tahun` dari daftar yang sudah dipecah.
    *   Mencetak data yang sudah diformat ke konsol menggunakan *f-string* dengan lebar kolom yang ditentukan (misalnya, `judul:.40` untuk memotong judul jika terlalu panjang).
    *   Menggunakan `end=""` pada fungsi `print` untuk mencegah penambahan *newline* ekstra, karena karakter *newline* sudah ada di akhir data `tahun`.
    *   Menambahkan `+1` pada indeks untuk menampilkan nomor urut yang dimulai dari 1.
6.  Mencetak garis pemisah (`=`) sebagai *footer* tabel.

## 3. Struktur Proyek

Proyek ini diorganisir dalam beberapa modul Python untuk memisahkan tanggung jawab dan meningkatkan modularitas:

*   **`main.py`**: Berisi menu utama aplikasi, penanganan *input* pengguna, dan memanggil fungsi-fungsi dari modul lain. Ini adalah titik masuk utama program.
*   **`CRUD/database.py`**: Mengelola konfigurasi database seperti nama file (`DB_NAME`) dan *template* struktur data (`TEMPLATE`). Juga berisi fungsi `init_console()` untuk inisialisasi database.
*   **`CRUD/util.py`**: Berisi fungsi-fungsi utilitas umum yang dapat digunakan di seluruh proyek, seperti `random_string()` untuk menghasilkan *string* acak.
*   **`CRUD/operasi.py`**: Berisi fungsi-fungsi yang berinteraksi langsung dengan file database, seperti `create_first_data()` untuk membuat data awal dan `read()` untuk membaca data.
*   **`CRUD/view.py`**: Berisi fungsi-fungsi yang bertanggung jawab untuk menampilkan data ke pengguna di konsol, seperti `read_console()` untuk menampilkan data dalam format tabel.