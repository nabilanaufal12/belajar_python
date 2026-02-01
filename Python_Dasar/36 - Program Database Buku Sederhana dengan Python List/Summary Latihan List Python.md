# Catatan Belajar: Program Database Buku Sederhana dengan Python List

## Pendahuluan

Catatan ini membahas pembuatan program database buku sederhana menggunakan bahasa pemrograman Python. Program ini memanfaatkan struktur data **list bersarang (nested list)** untuk menyimpan informasi buku, yang terdiri dari judul dan nama penulis. Fokus utama adalah pada konsep input data dari pengguna, penyimpanan data dalam list, menampilkan data secara terstruktur, dan interaksi pengguna untuk melanjutkan atau mengakhiri program.

## Konsep Dasar Program

Program ini dirancang untuk:
*   Menerima input judul buku dan nama penulis dari pengguna.
*   Menyimpan setiap buku sebagai sebuah list di dalam list utama.
*   Menampilkan daftar buku yang telah dimasukkan dengan nomor urut.
*   Memberikan opsi kepada pengguna untuk terus menambahkan buku atau mengakhiri program.

## Struktur Data: Nested List

Program ini menggunakan **nested list** (list di dalam list) sebagai struktur data utama untuk menyimpan informasi buku.
*   **`list_buku`**: Sebuah list kosong yang diinisialisasi untuk menampung semua buku yang akan dimasukkan. Ini adalah list utama."]
*   **`buku_baru`**: Setiap buku baru akan dibuat sebagai sebuah list yang berisi dua elemen: `judul` dan `penulis`. List ini kemudian ditambahkan ke `list_buku`."]

Contoh struktur data setelah beberapa input:
```
list_buku = [
    ["Harry Potter", "J.K. Rowling"],
    ["Laskar Pelangi", "Andrea Hirata"]
]
```

## Alur Program

Program berjalan dalam sebuah loop `while True` yang akan terus berulang hingga pengguna memutuskan untuk mengakhirinya.

### 1. Input Data Buku

Pada setiap iterasi loop, program akan meminta pengguna untuk memasukkan data buku:
*   **Judul Buku**: Diambil menggunakan fungsi `input()`.
*   **Nama Penulis**: Diambil menggunakan fungsi `input()`.

Setelah mendapatkan input, sebuah list `buku_baru` dibuat dengan `[judul, penulis]`, dan kemudian ditambahkan ke `list_buku` menggunakan metode `.append()`.

```python
# Bagian kode untuk input data
print("\nMasukkan Data Buku")
judul = input("Judul Buku\t: ")
penulis = input("Nama Penulis\t: ")

buku_baru = [judul, penulis] # Membuat list buku baru
list_buku.append(buku_baru)  # Menambahkan ke list utama
```

### 2. Menampilkan Data Buku

Setelah data buku baru ditambahkan, program akan menampilkan seluruh daftar buku yang sudah ada.
*   Digunakan loop `for` bersama dengan fungsi `enumerate()` untuk mendapatkan indeks (nomor urut) dan item (list buku) secara bersamaan. `enumerate()` akan menghasilkan pasangan `(index, item)` untuk setiap elemen dalam list.
*   Nomor urut dimulai dari 1 (`index+1`) agar lebih mudah dibaca oleh pengguna.
*   Setiap buku (`buku`) adalah sebuah list, di mana `buku[0]` adalah judul dan `buku[1]` adalah penulis. adalah judul"]
*   Output diformat menggunakan f-string untuk tampilan yang rapi.

```python
# Bagian kode untuk menampilkan data
print("\n" + "="*10 + " Data Buku " + "="*10)
print("No.\t| Judul\t\t\t| Penulis")

for index, buku in enumerate(list_buku):
    # buku[0] adalah judul, buku[1] adalah penulis
    print(f"{index+1}\t| {buku[0]}\t\t| {buku[1]}")
```

### 3. Konfirmasi Lanjut

Untuk mengontrol alur program, pengguna akan ditanya apakah ingin melanjutkan penambahan buku:
*   Input `is_lanjut` diambil dari pengguna (`y` untuk ya, `n` untuk tidak).
*   Jika pengguna memasukkan `n`, maka pernyataan `break` akan dieksekusi, yang akan menghentikan loop `while True` dan mengakhiri program.

```python
# Bagian kode untuk konfirmasi lanjut
print("\n" + "="*20)
is_lanjut = input("Apakah dilanjutkan? (y/n) ")

if is_lanjut == "n":
    break # Keluar dari loop while

print("PROGRAM SELESAI")
```

## Demo Program

Saat program dijalankan, alurnya adalah sebagai berikut:
1.  Program meminta input Judul dan Penulis buku pertama. Contoh: 'Harry Potter', 'J.K. Rowling'.
2.  Setelah input, program akan menampilkan tabel data buku yang sudah ada.
3.  Program akan menanyakan "Apakah dilanjutkan? (y/n)".
4.  Jika pengguna memasukkan `y`, program akan kembali ke langkah 1 untuk input buku kedua.
5.  Jika pengguna memasukkan `n`, program akan berhenti dan menampilkan "PROGRAM SELESAI".

## Kode Sumber Lengkap

Berikut adalah kode sumber lengkap program database buku sederhana:

```python
# Header Program
print("\n" + "="*10 + " PROGRAM LIST BUKU " + "="*10)

list_buku = [] # Inisialisasi list kosong untuk menampung semua buku

while True:
    print("\n" + "="*10 + " Masukkan Data Buku " + "="*10)
    
    judul = input("Judul Buku\t: ")
    penulis = input("Nama Penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    
    print("\n" + "="*10 + " Data Buku " + "="*10)
    print("No.\t| Judul\t\t\t| Penulis") # Menambahkan header kolom untuk tampilan data
    for index, buku in enumerate(list_buku):
        print(f"{index+1}\t| {buku[0]}\t\t| {buku[1]}") # Menambahkan tab untuk format kolom
    
    print("\n" + "="*20)
    is_lanjut = input("Apakah dilanjutkan? (y/n) ")

    if is_lanjut == "n":
        break

print("PROGRAM SELESAI")
```