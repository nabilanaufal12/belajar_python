# Catatan Studi: Program Menghitung Luas dan Keliling Persegi Panjang dengan Python

Catatan ini merangkum langkah-langkah dan konsep-konsep dalam membuat program Python untuk menghitung luas dan keliling persegi panjang, dengan fokus pada penggunaan fungsi untuk modularitas dan keterbacaan kode. Program ini dirancang agar interaktif dan dapat berjalan secara berulang.

## Pengenalan Program

Program ini bertujuan untuk menghitung luas dan keliling persegi panjang berdasarkan input lebar dan panjang dari pengguna. Implementasinya menggunakan beberapa fungsi terpisah untuk setiap tugas, mengikuti prinsip desain perangkat lunak yang baik.

## Prinsip Desain: Single Responsibility Principle

Salah satu prinsip penting yang diterapkan dalam program ini adalah **Single Responsibility Principle** (Prinsip Tanggung Jawab Tunggal). Prinsip ini menyatakan bahwa setiap fungsi atau modul sebaiknya hanya memiliki satu alasan untuk berubah, atau dengan kata lain, hanya melakukan satu tugas spesifik. Ini membantu menjaga kode tetap bersih, mudah dipelihara, dan mudah diuji.

## Struktur Program Berbasis Fungsi

Program ini dipecah menjadi beberapa fungsi yang masing-masing memiliki tanggung jawab spesifik:

### 1. Fungsi `header()`

Fungsi ini bertanggung jawab untuk menampilkan judul program dan membersihkan layar konsol agar tampilan lebih rapi setiap kali program dijalankan.

*   **Tujuan**: Menampilkan judul program dan membersihkan layar.
*   **Implementasi**:
    *   Menggunakan modul `os` untuk membersihkan layar (`os.system("cls")` untuk Windows, `os.system("clear")` untuk Mac/Linux).
    *   Menggunakan f-string untuk memformat dan menengahkan teks judul.

```python
import os

def header():
    '''Fungsi Header'''
    os.system("cls") # Gunakan "clear" untuk Mac/Linux
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")
```

### 2. Fungsi `input_user()`

Fungsi ini khusus menangani pengambilan input nilai lebar dan panjang dari pengguna.

*   **Tujuan**: Meminta pengguna memasukkan nilai lebar dan panjang.
*   **Implementasi**:
    *   Menggunakan fungsi `input()` untuk mendapatkan masukan dari pengguna.
    *   Mengkonversi input (yang selalu berupa string) menjadi integer menggunakan `int()`.
    *   Mengembalikan dua nilai (`lebar` dan `panjang`) yang akan digunakan oleh fungsi lain.

```python
def input_user():
    '''Fungsi Input User'''
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar, panjang
```

### 3. Fungsi `hitung_luas()`

Fungsi ini bertanggung jawab penuh untuk menghitung luas persegi panjang.

*   **Tujuan**: Menghitung luas persegi panjang.
*   **Rumus**: $Luas = lebar \times panjang$.
*   **Implementasi**: Menerima `lebar` dan `panjang` sebagai argumen, lalu mengembalikan hasil perkalian keduanya.

```python
def hitung_luas(lebar, panjang):
    '''Fungsi Luas'''
    return lebar * panjang
```

### 4. Fungsi `hitung_keliling()`

Fungsi ini bertanggung jawab penuh untuk menghitung keliling persegi panjang.

*   **Tujuan**: Menghitung keliling persegi panjang.
*   **Rumus**: $Keliling = 2 \times (lebar + panjang)$.
*   **Implementasi**: Menerima `lebar` dan `panjang` sebagai argumen, lalu mengembalikan hasil perhitungan keliling.

```python
def hitung_keliling(lebar, panjang):
    '''Fungsi Keliling'''
    return 2 * (lebar + panjang)
```

### 5. Fungsi `display()`

Fungsi ini bertugas untuk menampilkan hasil perhitungan ke layar dengan format yang seragam.

*   **Tujuan**: Menampilkan pesan dan nilai hasil perhitungan.
*   **Implementasi**: Menerima `message` (misalnya "Luas" atau "Keliling") dan `value` (nilai hasil perhitungan) sebagai argumen, lalu mencetaknya ke konsol.

```python
def display(message, value):
    '''Fungsi Display'''
    print(f"Hasil perhitungan {message} = {value}")
```

## Program Utama (Main Loop)

Bagian program utama adalah tempat semua fungsi di atas diorkestrasi. Program ini dirancang untuk berjalan dalam sebuah *loop* tak terbatas (`while True`) sehingga pengguna dapat melakukan perhitungan berulang kali hingga memilih untuk berhenti.

*   **Alur Kerja**:
    1.  Memanggil `header()` untuk membersihkan layar dan menampilkan judul.
    2.  Memanggil `input_user()` untuk mendapatkan `LEBAR` dan `PANJANG`.
    3.  Memanggil `hitung_luas()` dan `hitung_keliling()` untuk mendapatkan `LUAS` dan `KELILING`.
    4.  Memanggil `display()` dua kali untuk menampilkan hasil luas dan keliling.
    5.  Meminta konfirmasi kepada pengguna apakah ingin melanjutkan (`y/n`).
    6.  Jika pengguna memasukkan 'n' (atau 'N'), *loop* akan dihentikan (`break`).
    7.  Jika tidak, *loop* akan berlanjut ke iterasi berikutnya.

```python
# --- PROGRAM UTAMA ---
while True:
    header()
    
    # 1. Ambil Input
    LEBAR, PANJANG = input_user()
    
    # 2. Hitung Luas & Keliling
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)
    
    # 3. Tampilkan Hasil
    print("-" * 40)
    display("Luas", LUAS)
    display("Keliling", KELILING)
    
    # 4. Konfirmasi Lanjut
    isContinue = input("\nApakah lanjut (y/n)? ")
    if isContinue.lower() == "n":
        break

print("Program selesai, terima kasih")
```

## Kode Lengkap Program

Berikut adalah rangkuman seluruh kode program yang menggabungkan semua fungsi dan logika program utama:

```python
import os

def header():
    '''Fungsi Header'''
    os.system("cls") # Gunakan "clear" untuk Mac/Linux
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''Fungsi Input User'''
    # Mengambil input lebar dan panjang dari user
    lebar = int(input("Masukkan nilai lebar: "))
    panjang = int(input("Masukkan nilai panjang: "))
    return lebar, panjang

def hitung_luas(lebar, panjang):
    '''Fungsi Hitung Luas'''
    return lebar * panjang

def hitung_keliling(lebar, panjang):
    '''Fungsi Hitung Keliling'''
    return 2 * (lebar + panjang)

def display(message, value):
    '''Fungsi Display Hasil'''
    print(f"Hasil perhitungan {message} = {value}")

# --- PROGRAM UTAMA ---
while True:
    header()
    
    # 1. Ambil Input
    LEBAR, PANJANG = input_user()
    
    # 2. Hitung Luas & Keliling
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)
    
    # 3. Tampilkan Hasil
    print("-" * 40)
    display("Luas", LUAS)
    display("Keliling", KELILING)
    
    # 4. Konfirmasi Lanjut
    isContinue = input("\nApakah lanjut (y/n)? ")
    if isContinue.lower() == "n":
        break

print("Program selesai, terima kasih")
```