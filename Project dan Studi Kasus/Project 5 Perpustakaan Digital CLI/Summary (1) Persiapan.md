# Catatan Studi: Persiapan Proyek Perpustakaan Digital dengan Python (CLI)

Proyek ini bertujuan untuk membangun aplikasi perpustakaan digital berbasis *Command Line Interface* (CLI) menggunakan Python. Fokus utama adalah mengimplementasikan operasi dasar *Create, Read, Update, Delete* (CRUD) untuk mengelola data buku, serta membangun struktur proyek yang modular dan rapi.

## 1. Konsep Proyek: Perpustakaan Digital CLI

Aplikasi ini akan memungkinkan pengguna untuk berinteraksi dengan database perpustakaan melalui terminal. Data buku akan disimpan secara persisten dalam sebuah file teks bernama `data.txt`.

### 1.1 Fitur Utama (CRUD)
Proyek ini akan mengimplementasikan empat operasi dasar:
*   **Read Data**: Melihat daftar buku yang ada di perpustakaan.
*   **Create Data**: Menambahkan data buku baru ke database.
*   **Update Data**: Mengubah informasi buku yang sudah ada.
*   **Delete Data**: Menghapus data buku dari database.

### 1.2 Struktur Proyek
Proyek akan diorganisir dengan struktur folder sebagai berikut untuk menjaga modularitas dan keterbacaan kode:

```text
project_perpustakaan/
│
├── main.py          <-- File Utama
└── CRUD/            <-- Package CRUD
    └── __init__.py
```

*   `main.py`: Berisi logika utama program, termasuk menu interaktif dan penanganan input pengguna.
*   `CRUD/`: Sebuah *package* Python yang akan menampung fungsi-fungsi spesifik untuk operasi CRUD. Ini membantu mengorganisir kode agar lebih rapi.
*   `__init__.py`: File kosong yang menandakan bahwa `CRUD` adalah sebuah *package* Python.

## 2. Implementasi `main.py`: Menu Utama CLI

File `main.py` bertanggung jawab untuk menampilkan menu, menerima input dari pengguna, dan mengarahkan alur program.

### 2.1 Inisialisasi Program dan Deteksi Sistem Operasi
Program dimulai dengan blok `if __name__ == "__main__":`, yang merupakan konvensi umum di Python untuk memastikan kode hanya berjalan saat skrip dieksekusi langsung.

Modul `os` digunakan untuk mendeteksi sistem operasi pengguna (`os.name`) dan membersihkan layar terminal. Ini penting agar tampilan CLI selalu rapi setiap kali menu ditampilkan.

*   `os.name` akan mengembalikan `"posix"` untuk sistem operasi berbasis Unix (seperti Linux atau macOS) atau `"nt"` untuk Windows.
*   Perintah pembersihan layar disesuaikan: `os.system("clear")` untuk `posix` dan `os.system("cls")` untuk `nt`.

```python
import os
import CRUD as CRUD # Akan digunakan di episode selanjutnya

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
        case "posix": os.system("clear") # Linux / Mac
        case "nt": os.system("cls")      # Windows

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")
    # ... (lanjutan kode)
```

### 2.2 Loop Menu Utama
Menu utama program diimplementasikan dalam sebuah *loop* `while True` agar program terus berjalan dan menampilkan menu sampai pengguna memilih untuk keluar.

Setiap iterasi *loop*, layar terminal akan dibersihkan terlebih dahulu untuk memastikan tampilan menu selalu segar dan rapi.

```python
    while True:
        # Pilihan Menu
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
            
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")
        
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("Masukan opsi: ")

        print("\n=========================\n")
        # ... (lanjutan kode)
```

### 2.3 Penanganan Pilihan Pengguna
Input pengguna untuk memilih opsi menu ditangkap menggunakan fungsi `input()`. Pilihan ini kemudian diproses menggunakan pernyataan `match case` untuk menentukan tindakan yang sesuai. Saat ini, setiap pilihan hanya akan mencetak nama operasi yang dipilih.

```python
        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")
```

### 2.4 Mekanisme Keluar Program
Setelah setiap operasi, program akan menanyakan kepada pengguna apakah mereka ingin selesai (`Apakah Selesai (y/n)?`). Jika pengguna memasukkan 'y' atau 'Y', *loop* `while True` akan dihentikan menggunakan `break`, dan program akan berakhir.

```python
        print("\n=========================\n")
        
        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir, Terima Kasih")
```

## 3. Package `CRUD`

*Package* `CRUD` disiapkan sebagai tempat untuk mengorganisir semua fungsi yang berkaitan dengan operasi *Create, Read, Update, Delete* pada data buku. Saat ini, file `CRUD/__init__.py` masih kosong, namun akan diisi dengan logika program di episode-episode selanjutnya.