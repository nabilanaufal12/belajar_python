# Membuat Data (Create) pada Aplikasi CRUD Python

Fitur "Create Data" memungkinkan pengguna untuk menambahkan entri buku baru ke dalam database aplikasi. Proses ini melibatkan pengambilan input dari pengguna, validasi data, pemrosesan data, dan penulisan data ke dalam file database.

## 1. Implementasi Fungsi `create_console()` di `view.py`

Fungsi `create_console()` bertanggung jawab untuk berinteraksi dengan pengguna, mengambil input data buku baru, dan memvalidasinya sebelum diteruskan ke modul operasi.

### 1.1. Tampilan dan Input Dasar

*   **Deklarasi Fungsi**: Didefinisikan sebagai `def create_console():` di dalam `view.py`.
*   **Tampilan Awal**: Menampilkan judul bagian "Silahkan Tambah Data Buku" dengan pembatas untuk kejelasan.
*   **Input Penulis dan Judul**: Pengguna diminta untuk memasukkan nama penulis dan judul buku. Input ini diambil sebagai string.

### 1.2. Validasi Input Tahun

Input tahun memerlukan validasi khusus untuk memastikan integritas data.

*   **Persyaratan**: Tahun harus berupa angka (`integer`) dan memiliki panjang tepat 4 digit (format `yyyy`).
*   **Mekanisme Validasi**:
    *   Menggunakan perulangan `while True` agar input tahun terus diminta sampai valid.
    *   Blok `try-except` digunakan untuk menangani kesalahan jika input bukan angka. Jika terjadi `except`, pesan kesalahan "Tahun harus angka, silahkan masukan tahun lagi (yyyy)" akan ditampilkan.
    *   Setelah berhasil dikonversi ke `integer`, panjang string dari tahun tersebut diperiksa. Jika tidak 4 digit, pesan "Tahun harus angka 4 digit (yyyy)" akan muncul.
    *   Jika tahun valid (angka dan 4 digit), perulangan akan dihentikan dengan `break`.
*   **Contoh Alur Validasi**:
    *   Jika input "abcd", akan muncul "Tahun harus angka, silahkan masukan tahun lagi (yyyy)".
    *   Jika input "123", akan muncul "Tahun harus angka 4 digit (yyyy)".
    *   Jika input "12345", akan muncul "Tahun harus angka 4 digit (yyyy)".
    *   Jika input "2023", valid dan program berlanjut.

### 1.3. Pemanggilan Fungsi Operasi dan Tampilan Hasil

Setelah semua input divalidasi, data diteruskan ke fungsi `create()` di modul `operasi`.

*   **Pemanggilan `operasi.create()`**: Fungsi ini dipanggil dengan argumen `tahun`, `judul`, dan `penulis` yang telah divalidasi.
*   **Tampilan Data Baru**: Setelah operasi penambahan selesai, fungsi `read_console()` dipanggil untuk menampilkan daftar buku terbaru, termasuk data yang baru saja ditambahkan.

## 2. Implementasi Fungsi `create()` di `operasi.py`

Fungsi `create()` di `operasi.py` bertanggung jawab untuk memproses data buku yang diterima dari `view.py` dan menyimpannya ke dalam file database.

### 2.1. Persiapan Data

Data buku baru perlu diformat agar sesuai dengan struktur database yang ada (CSV).

*   **Mengambil Template**: Salinan dari `database.TEMPLATE` digunakan sebagai dasar untuk data baru.
*   **Primary Key (PK)**: Sebuah `pk` unik (6 karakter acak) dibuat menggunakan fungsi `random_string()` dari modul `util`. = random_string(6)"]
*   **Tanggal Penambahan (`date_add`)**: Waktu saat ini dicatat dalam format `YYYY-MM-DD-HH-MM-SS%z` menggunakan `time.strftime()` dan `time.gmtime()`. = time.strftime"]
*   **Format Penulis dan Judul**: String penulis dan judul ditambahkan spasi di belakangnya hingga mencapai panjang standar yang ditentukan dalam `database.TEMPLATE` untuk menjaga konsistensi format. = penulis + database.TEMPLATE["penulis"] * " ""]
*   **Konversi Tahun**: Nilai `tahun` diubah menjadi string (`str(tahun)`) sebelum disimpan. = str(tahun)"]
*   **Pembentukan String Data**: Semua komponen data digabungkan menjadi satu string format CSV, diakhiri dengan karakter *newline* (`\n`).},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'"]

### 2.2. Penulisan Data ke File Database

Data yang sudah diformat kemudian ditulis ke file `data.txt` (atau `database.DB_NAME`).

*   **Mode Penulisan `Append` (`'a'`)**: File database dibuka dalam mode `append` (`'a'`). Ini adalah kunci utama fitur `create`, karena mode ini akan menambahkan data baru di akhir file tanpa menghapus konten yang sudah ada.
*   **Penulisan String**: Fungsi `file.write(data_str)` digunakan untuk menulis string data buku baru ke dalam file.
*   **Penanganan Kesalahan**: Blok `try-except` digunakan untuk menangani potensi kesalahan saat menulis ke file, menampilkan pesan "Gagal menambahkan data!" jika terjadi masalah.

## 3. Integrasi Modul

Agar fitur "Create Data" dapat diakses, beberapa file perlu diperbarui.

*   **`main.py`**: Pilihan menu untuk "Create Data" (opsi "2") dihubungkan ke fungsi `CRUD.create_console()`.
*   **`CRUD/__init__.py`**: Fungsi `create_console` diimpor dari `view.py` agar dapat diakses melalui modul `CRUD`.

Dengan integrasi ini, pengguna dapat memilih opsi "2" dari menu utama untuk menambahkan data buku baru ke dalam sistem.