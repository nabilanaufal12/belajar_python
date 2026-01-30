# Fitur Delete (Hapus Data) pada Proyek CRUD Python

Fitur "Delete" adalah komponen terakhir dalam proyek CRUD (Create, Read, Update, Delete) berbasis file teks ini. Proses penghapusan data dari file teks memiliki tantangan tersendiri dibandingkan dengan database tradisional, sehingga memerlukan strategi khusus untuk implementasinya.

## Konsep Penghapusan Data dari File Teks

Menghapus baris tertentu di tengah file teks (`.txt`) secara langsung adalah hal yang rumit. Kita tidak bisa hanya mengosongkan baris tersebut karena akan meninggalkan baris kosong yang dapat mengganggu struktur data. Oleh karena itu, strategi yang digunakan adalah teknik **penggantian file** (file renaming).

**Strategi Penggantian File:**
1.  **Baca File Asli**: File database asli (`database.DB_NAME`) dibaca baris per baris.
2.  **Buat File Sementara**: Sebuah file baru, misalnya `data_temp.txt`, dibuat untuk menampung data yang akan dipertahankan.
3.  **Salin Data (Kecuali yang Dihapus)**: Semua baris dari file asli disalin ke file sementara, **kecuali** baris yang sesuai dengan nomor buku yang ingin dihapus. Baris yang ingin dihapus akan dilewati (di-*skip*).
4.  **Hapus File Asli**: Setelah semua data yang relevan disalin, file database asli dihapus.
5.  **Ganti Nama File Sementara**: File sementara (`data_temp.txt`) kemudian diganti namanya menjadi nama file database asli (`database.DB_NAME`), sehingga secara efektif menggantikan file lama dengan versi yang sudah diperbarui (tanpa data yang dihapus).

Untuk melakukan operasi hapus dan ganti nama file, modul `os` dari Python diperlukan dan harus diimpor.

## Implementasi Fitur Delete

Fitur delete diimplementasikan melalui dua fungsi utama: `delete_console()` di `view.py` untuk interaksi pengguna, dan `delete()` di `operasi.py` untuk logika backend.

### 1. Fungsi `delete_console()` di `CRUD/view.py`

Fungsi ini bertanggung jawab untuk berinteraksi dengan pengguna dan mengelola alur penghapusan data.

*   **Menampilkan Data**: Pertama, semua data buku yang ada ditampilkan kepada pengguna menggunakan `read_console()` agar pengguna dapat melihat nomor buku yang tersedia.
*   **Meminta Input Nomor Buku**: Pengguna diminta untuk memasukkan nomor buku yang ingin dihapus.
*   **Validasi dan Pengambilan Data**:
    *   Input nomor buku divalidasi. Jika nomor tidak valid, pengguna diminta untuk memasukkan kembali.
    *   Data buku yang sesuai dengan nomor yang dimasukkan diambil menggunakan `operasi.read(index=no_buku)`.
*   **Konfirmasi Penghapusan**:
    *   Detail data buku yang akan dihapus ditampilkan kepada pengguna untuk konfirmasi.
    *   Pengguna diminta untuk mengonfirmasi (`y/n`) apakah mereka yakin ingin menghapus data tersebut.
    *   Jika pengguna menjawab 'n' (tidak yakin), proses akan diulang, meminta nomor buku lagi.
    *   Jika pengguna menjawab 'y' (yakin), barulah fungsi `operasi.delete()` dipanggil.
*   **Pesan Sukses**: Setelah penghapusan berhasil, pesan "Data berhasil dihapus" ditampilkan.

```python
# CRUD/view.py
from . import operasi

def delete_console():
    read_console() # Tampilkan semua data buku
    
    while True:
        print("Silahkan pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            # Parsing data buku untuk ditampilkan
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            
            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku) # Panggil fungsi delete di operasi.py
                break # Keluar dari loop setelah berhasil menghapus
            else:
                # Jika tidak yakin, loop akan berlanjut meminta nomor buku lagi
                print("Penghapusan dibatalkan. Silahkan pilih nomor buku lain.")
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil dihapus")
```

### 2. Fungsi `delete()` di `CRUD/operasi.py`

Fungsi ini mengimplementasikan logika inti dari strategi penggantian file untuk menghapus data.

*   **Membuka File**:
    *   File database asli (`database.DB_NAME`) dibuka dalam mode baca (`'r'`).
    *   File sementara (`data_temp.txt`) dibuka dalam mode tambah (`'a'`) dengan encoding `utf-8` untuk menulis data yang dipertahankan.
*   **Iterasi dan Penyalinan Data**:
    *   Sebuah `counter` digunakan untuk melacak nomor baris saat membaca file.
    *   Loop `while True` membaca file baris per baris menggunakan `file.readline()`.
    *   **Kondisi Akhir File**: Jika `len(content) == 0`, berarti sudah mencapai akhir file, dan loop dihentikan (`break`).
    *   **Melewatkan Baris yang Dihapus**: Jika `counter` sama dengan `no_buku - 1` (karena `counter` dimulai dari 0, sedangkan `no_buku` dimulai dari 1), baris tersebut dilewati (`pass`) dan tidak ditulis ke file sementara.
    *   **Menulis Baris yang Dipertahankan**: Untuk baris lainnya, `content` ditulis ke `data_temp.txt`.
    *   `counter` ditingkatkan (`counter += 1`) di setiap iterasi.
*   **Penanganan Kesalahan**: Blok `try-except` digunakan untuk menangani potensi kesalahan saat operasi file, seperti `Database Error`.
*   **Penggantian File**:
    *   Setelah loop selesai, file database asli dihapus menggunakan `os.remove(database.DB_NAME)`.
    *   File sementara diganti namanya menjadi nama file database asli menggunakan `os.rename("data_temp.txt", database.DB_NAME)`.
*   **Debugging Penting**: Perhatikan penulisan nama file sementara (`data_temp.txt`). Kesalahan penulisan (misalnya, `data_Temp.txt` dengan 'T' kapital) dapat menyebabkan `No such file or directory` error.

```python
# CRUD/operasi.py
from . import database
import os # Import modul os

def delete(no_buku):
    try:
        with open(database.DB_NAME, 'r') as file:
            counter = 0
            
            while True:
                content = file.readline()
                if len(content) == 0:
                    break # Akhir file
                elif counter == no_buku - 1:
                    pass # Lewati baris yang ingin dihapus
                else:
                    # Tulis ke file sementara
                    with open("data_temp.txt", 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("Database Error")

    # Rename file temporary jadi file utama
    os.remove(database.DB_NAME) # Hapus file database asli
    os.rename("data_temp.txt", database.DB_NAME) # Ganti nama file sementara
```

## Integrasi ke Aplikasi Utama

Agar fungsi `delete_console()` dapat diakses dari menu utama aplikasi, beberapa perubahan perlu dilakukan:

*   **`main.py`**: Tambahkan `case "4": CRUD.delete_console()` ke dalam struktur `match user_option` untuk memanggil fungsi delete saat pengguna memilih opsi 4.
*   **`CRUD/__init__.py`**: Impor `delete_console` dari `view.py` agar dapat diakses melalui modul `CRUD`.

Dengan implementasi ini, proyek CRUD berbasis file teks telah selesai, mencakup semua operasi dasar: Create, Read, Update, dan Delete.